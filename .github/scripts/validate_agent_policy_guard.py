#!/usr/bin/env python3
"""Validate AI-agent control invariants from trusted target-branch code.

This script is designed for pull_request_target and target-branch push events. It
reads pull-request content only as data and never executes candidate-branch code.
It posts a commit status on each PR head so target-branch advances can invalidate
stale agent checkpoints even when the PR head itself did not change.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from fetch_agent_checkpoint_context import (
    API_ROOT,
    agent_none_approved,
    authorized_codeowners,
    checkpoint_sha256,
    feedback_sha256,
    global_codeowners,
    issue_comments,
    marker_objects,
    paged_list,
    pr_body_sha256,
    readiness_approval,
    readiness_state_from_timeline,
    request_json,
)

ROOT = Path(__file__).resolve().parents[2]
CHANGE_CONTRACT = ROOT / ".github/policy/change-coupling-contract.json"
CHECKPOINT_CONTRACT = ROOT / ".github/policy/agent-checkpoint-contract.json"
STATUS_CONTEXT = "Agent protocol / trusted-base guard"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class Finding:
    def __init__(self, severity: str, message: str) -> None:
        self.severity = severity
        self.message = message


def load_json(path: Path) -> Dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("contract_version") != 1:
        raise ValueError("unsupported contract_version in {}".format(path))
    return value


def encoded_repo(repository: str) -> str:
    return "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))


def request_json_write(url: str, token: str, method: str, payload: Dict[str, object]) -> object:
    request = urllib.request.Request(
        url,
        method=method,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ua-agent-policy-guard",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8")
    return json.loads(raw) if raw else {}


def post_status(
    repository: str,
    head_sha: str,
    token: str,
    state: str,
    description: str,
    target_url: str,
) -> None:
    url = "{}/repos/{}/statuses/{}".format(
        API_ROOT, encoded_repo(repository), urllib.parse.quote(head_sha, safe="")
    )
    request_json_write(
        url,
        token,
        "POST",
        {
            "state": state,
            "context": STATUS_CONTEXT,
            "description": description[:140],
            "target_url": target_url,
        },
    )


def branch_tip(repository: str, branch: str, token: str) -> str:
    url = "{}/repos/{}/branches/{}".format(
        API_ROOT, encoded_repo(repository), urllib.parse.quote(branch, safe="")
    )
    value, _ = request_json(url, token)
    if not isinstance(value, dict) or not isinstance(value.get("commit"), dict):
        raise ValueError("unable to resolve current target branch tip")
    sha = str(value["commit"].get("sha") or "")
    if not SHA_RE.fullmatch(sha):
        raise ValueError("target branch returned invalid commit SHA")
    return sha


def fetch_pr(repository: str, pr_number: int, token: str) -> Dict[str, object]:
    url = "{}/repos/{}/pulls/{}".format(API_ROOT, encoded_repo(repository), pr_number)
    value, _ = request_json(url, token)
    if not isinstance(value, dict):
        raise ValueError("pull request response is not an object")
    return value


def open_prs(repository: str, base: str, token: str) -> List[Dict[str, object]]:
    url = "{}/repos/{}/pulls?state=open&base={}&per_page=100".format(
        API_ROOT, encoded_repo(repository), urllib.parse.quote(base, safe="")
    )
    return paged_list(url, token)


def pr_files(repository: str, pr_number: int, token: str) -> List[Dict[str, object]]:
    url = "{}/repos/{}/pulls/{}/files?per_page=100".format(
        API_ROOT, encoded_repo(repository), pr_number
    )
    return paged_list(url, token)


def all_changed_paths(files: Iterable[Dict[str, object]]) -> Set[str]:
    paths: Set[str] = set()
    for item in files:
        filename = str(item.get("filename") or "")
        previous = str(item.get("previous_filename") or "")
        if filename:
            paths.add(filename)
        if previous:
            paths.add(previous)
    return paths


def path_matches(path: str, prefixes: Iterable[str]) -> bool:
    return any(path == prefix or path.startswith(prefix) for prefix in prefixes)


def fetch_file_optional(repository: str, path: str, ref: str, token: str) -> Optional[str]:
    url = "{}/repos/{}/contents/{}?ref={}".format(
        API_ROOT,
        encoded_repo(repository),
        "/".join(urllib.parse.quote(part, safe="") for part in path.split("/")),
        urllib.parse.quote(ref, safe=""),
    )
    try:
        value, _ = request_json(url, token)
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise
    if not isinstance(value, dict) or value.get("encoding") != "base64":
        return None
    raw = str(value.get("content") or "").replace("\n", "")
    return base64.b64decode(raw).decode("utf-8")


def frontmatter_status(text: Optional[str]) -> str:
    if not text or not text.startswith("---"):
        return ""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            break
        if stripped.startswith("status:"):
            return stripped.split(":", 1)[1].strip().strip("\"'")
    return ""


def observed_draft_statuses(
    base_repository: str,
    head_repository: str,
    base_tip: str,
    head_sha: str,
    files: Sequence[Dict[str, object]],
    protected: Iterable[str],
    token: str,
) -> Set[str]:
    protected_set = set(str(item) for item in protected)
    observed: Set[str] = set()
    for item in files:
        status = str(item.get("status") or "")
        filename = str(item.get("filename") or "")
        previous = str(item.get("previous_filename") or filename)
        if previous.endswith(".md") and status != "added":
            old_status = frontmatter_status(
                fetch_file_optional(base_repository, previous, base_tip, token)
            )
            if old_status in protected_set:
                observed.add(old_status)
        if filename.endswith(".md") and status != "removed":
            new_status = frontmatter_status(
                fetch_file_optional(head_repository, filename, head_sha, token)
            )
            if new_status in protected_set:
                observed.add(new_status)
    return observed


def parse_exact_block(body: str, marker: str) -> Tuple[Optional[Dict[str, object]], Optional[str]]:
    blocks = marker_objects(body, marker)
    if len(blocks) != 1:
        return None, "PR body must contain exactly one {} JSON block".format(marker)
    return blocks[0], None


def has_exception(labels: Set[str], contract: Dict[str, object], category: str) -> bool:
    for label, categories in contract.get("exception_labels", {}).items():
        if label in labels and isinstance(categories, list) and category in categories:
            return True
    return False


def trusted_guard_status_passed(
    repository: str, head_sha: str, ready_at: str, token: str
) -> bool:
    if not ready_at:
        return False
    url = "{}/repos/{}/commits/{}/statuses?per_page=100".format(
        API_ROOT, encoded_repo(repository), urllib.parse.quote(head_sha, safe="")
    )
    for status in paged_list(url, token):
        if str(status.get("context") or "") != STATUS_CONTEXT:
            continue
        if str(status.get("state") or "") != "success":
            continue
        created_at = str(status.get("created_at") or "")
        if created_at and created_at >= ready_at:
            return True
    return False


def validate_pr(
    repository: str,
    pr: Dict[str, object],
    token: str,
    change_contract: Dict[str, object],
    checkpoint_contract: Dict[str, object],
    event_name: str,
    event_action: str,
) -> List[Finding]:
    findings: List[Finding] = []
    pr_number = int(pr.get("number") or 0)
    body = str(pr.get("body") or "")
    user = pr.get("user") if isinstance(pr.get("user"), dict) else {}
    pr_author = str(user.get("login") or "")
    base = pr.get("base") if isinstance(pr.get("base"), dict) else {}
    head = pr.get("head") if isinstance(pr.get("head"), dict) else {}
    base_ref = str(base.get("ref") or "")
    head_sha = str(head.get("sha") or "")
    if not base_ref or not SHA_RE.fullmatch(head_sha):
        return [Finding("error", "PR lacks a valid base ref or head SHA")]
    base_tip = branch_tip(repository, base_ref, token)
    merge_sha = str(pr.get("merge_commit_sha") or "")
    if not SHA_RE.fullmatch(merge_sha):
        findings.append(Finding("error", "GitHub has no current tested merge SHA for this PR"))

    head_repo = head.get("repo") if isinstance(head.get("repo"), dict) else {}
    head_repository = str(head_repo.get("full_name") or repository)
    files = pr_files(repository, pr_number, token)
    paths = all_changed_paths(files)
    repository_policy_changed = any(
        path_matches(path, change_contract.get("repository_policy_prefixes", []))
        for path in paths
    )
    draft_statuses = observed_draft_statuses(
        repository,
        head_repository,
        base_tip,
        head_sha,
        files,
        change_contract.get("draft_required_document_statuses", []),
        token,
    )

    labels = {
        str(item.get("name"))
        for item in pr.get("labels", [])
        if isinstance(item, dict) and item.get("name")
    }
    change, change_error = parse_exact_block(
        body, str(checkpoint_contract.get("pr_change_contract_marker") or "ua-change-contract")
    )
    contract_exception = bool(change_error and has_exception(labels, change_contract, "pr-contract"))
    if change_error and not contract_exception:
        findings.append(Finding("error", change_error))
        return findings
    if contract_exception:
        findings.append(
            Finding(
                "warning",
                change_error + "; trusted-base guard uses safe agent-assisted defaults and does not bypass checkpoint/Draft controls",
            )
        )
        change = {"agent_assistance": "used", "change_class": "maintenance"}
    assert change is not None

    change_class = str(change.get("change_class") or "")
    assistance = str(change.get("agent_assistance") or "")
    if repository_policy_changed and change_class != "repository-policy":
        findings.append(
            Finding(
                "error",
                "trusted-base classification: repository-policy paths require change_class 'repository-policy'",
            )
        )
    if draft_statuses and change_class not in {"repository-policy", "draft-normative", "normative"}:
        findings.append(
            Finding(
                "error",
                "trusted-base classification: protected document status {} cannot be downgraded by change_class {!r}".format(
                    ", ".join(sorted(draft_statuses)), change_class
                ),
            )
        )

    codeowners_path = str(checkpoint_contract.get("maintainer_authority_path") or ".github/CODEOWNERS")
    codeowners_text = fetch_file_optional(repository, codeowners_path, base_tip, token)
    if codeowners_text is None:
        findings.append(Finding("error", "unable to read target-branch CODEOWNERS"))
        return findings
    declared_codeowners = global_codeowners(codeowners_text)
    authorized = authorized_codeowners(repository, declared_codeowners, token)
    trusted = [str(item) for item in checkpoint_contract.get("trusted_feedback_author_associations", [])]
    comments = issue_comments(repository, pr_number, token)

    if pr_author == "dependabot[bot]":
        return findings

    if assistance == "none":
        if not agent_none_approved(
            comments,
            authorized,
            trusted,
            str(checkpoint_contract.get("agent_none_approval_marker") or "ua-agent-assistance-none"),
            head_sha,
        ):
            findings.append(
                Finding(
                    "error",
                    "trusted-base guard: agent_assistance 'none' lacks current-head approval from a current authorized CODEOWNER",
                )
            )
        return findings
    if assistance != "used":
        findings.append(Finding("error", "trusted-base guard requires agent_assistance 'used' or approved 'none'"))
        return findings

    checkpoint_marker = str(checkpoint_contract.get("pr_checkpoint_marker") or "ua-agent-checkpoint")
    checkpoint, checkpoint_error = parse_exact_block(body, checkpoint_marker)
    if checkpoint_error:
        findings.append(Finding("error", checkpoint_error))
        return findings
    assert checkpoint is not None
    current_body_hash = pr_body_sha256(body, checkpoint_marker)
    current_checkpoint_hash = checkpoint_sha256(body, checkpoint_marker)
    current_feedback_hash = feedback_sha256(repository, pr_number, token, trusted)

    expected = {
        "reviewed_base_tip_sha": base_tip,
        "reviewed_head_sha": head_sha,
        "reviewed_pr_body_sha256": current_body_hash,
        "reviewed_feedback_sha256": current_feedback_hash,
    }
    if SHA_RE.fullmatch(merge_sha):
        expected["reviewed_merge_sha"] = merge_sha
    for field, expected_value in expected.items():
        if str(checkpoint.get(field) or "") != expected_value:
            findings.append(
                Finding(
                    "error",
                    "trusted-base guard: checkpoint {} is stale; expected {}".format(field, expected_value),
                )
            )

    declared_high_impact = change_class in set(
        str(item) for item in checkpoint_contract.get("draft_required_change_classes", [])
    )
    high_impact = repository_policy_changed or bool(draft_statuses) or declared_high_impact
    if high_impact and not bool(pr.get("draft")):
        timeline_url = "{}/repos/{}/issues/{}/timeline?per_page=100".format(
            API_ROOT, encoded_repo(repository), pr_number
        )
        ready_head, ready_at = readiness_state_from_timeline(paged_list(timeline_url, token))
        approval_present, transition_authorized = readiness_approval(
            comments,
            authorized,
            trusted,
            str(checkpoint_contract.get("ready_approval_marker") or "ua-agent-ready-approval"),
            head_sha,
            merge_sha,
            current_checkpoint_hash,
            current_body_hash,
            ready_at,
        )
        if ready_head != head_sha or not approval_present:
            findings.append(
                Finding(
                    "error",
                    "trusted-base guard: non-Draft high-impact PR lacks current state-bound CODEOWNER Ready approval",
                )
            )
        elif event_name == "pull_request_target" and event_action == "ready_for_review":
            if not transition_authorized:
                findings.append(
                    Finding(
                        "error",
                        "trusted-base guard: Ready transition lacks approval for the exact current checkpoint fingerprint",
                    )
                )
        elif not trusted_guard_status_passed(repository, head_sha, ready_at, token):
            findings.append(
                Finding(
                    "error",
                    "trusted-base guard: current Ready cycle has no prior successful trusted-base status after the Ready transition",
                )
            )
    return findings


def status_description(findings: Sequence[Finding]) -> Tuple[str, str]:
    errors = [item.message for item in findings if item.severity == "error"]
    if errors:
        return "failure", errors[0]
    warnings = [item.message for item in findings if item.severity == "warning"]
    if warnings:
        return "success", "Trusted-base guard passed with controlled exception warning"
    return "success", "Trusted-base agent control invariants are current"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--event-name", default="")
    parser.add_argument("--event-action", default="")
    parser.add_argument("--pr-number", type=int, default=0)
    parser.add_argument("--base-branch", default="main")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("Missing GITHUB_TOKEN", file=sys.stderr)
        return 2
    change_contract = load_json(CHANGE_CONTRACT)
    checkpoint_contract = load_json(CHECKPOINT_CONTRACT)
    target_url = "{}/{}/actions/runs/{}".format(
        os.environ.get("GITHUB_SERVER_URL", "https://github.com"),
        args.repository,
        os.environ.get("GITHUB_RUN_ID", ""),
    )

    try:
        if args.pr_number:
            prs = [fetch_pr(args.repository, args.pr_number, token)]
        else:
            prs = open_prs(args.repository, args.base_branch, token)
        any_errors = False
        for pr in prs:
            head = pr.get("head") if isinstance(pr.get("head"), dict) else {}
            head_sha = str(head.get("sha") or "")
            if not SHA_RE.fullmatch(head_sha):
                continue
            findings = validate_pr(
                args.repository,
                pr,
                token,
                change_contract,
                checkpoint_contract,
                args.event_name,
                args.event_action,
            )
            state, description = status_description(findings)
            post_status(args.repository, head_sha, token, state, description, target_url)
            for finding in findings:
                print("{}: PR #{}: {}".format(finding.severity.upper(), pr.get("number"), finding.message))
            any_errors = any_errors or state == "failure"
        # A pull_request_target run should be visibly red when its PR violates
        # trusted-base invariants. A target-branch push may invalidate several
        # open PRs; those failures belong on their head statuses, not on main.
        if args.pr_number and any_errors:
            return 1
        return 0
    except Exception as exc:
        print("Trusted-base agent policy guard error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
