#!/usr/bin/env python3
"""Fetch live PR state and deterministic maintainer-feedback/readiness evidence."""

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/agent-checkpoint-contract.json"
API_ROOT = "https://api.github.com"


def load_contract(path: Path) -> Dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("contract_version") != 1:
        raise ValueError("unsupported contract_version: {!r}".format(value.get("contract_version")))
    return value


def request_json(url: str, token: str) -> Tuple[object, Dict[str, str]]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(token),
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ua-agent-checkpoint",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))
        headers = {key.lower(): value for key, value in response.headers.items()}
    return data, headers


def next_link(link_header: str) -> Optional[str]:
    for item in (link_header or "").split(","):
        parts = [part.strip() for part in item.split(";")]
        if len(parts) < 2 or 'rel="next"' not in parts[1:]:
            continue
        url = parts[0]
        if url.startswith("<") and url.endswith(">"):
            return url[1:-1]
    return None


def paged_list(url: str, token: str) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    current: Optional[str] = url
    while current:
        value, headers = request_json(current, token)
        if not isinstance(value, list):
            raise ValueError("expected list response from {}".format(current))
        items.extend(item for item in value if isinstance(item, dict))
        current = next_link(headers.get("link", ""))
    return items


def paged_object_items(url: str, token: str, key: str) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    current: Optional[str] = url
    while current:
        value, headers = request_json(current, token)
        if not isinstance(value, dict) or not isinstance(value.get(key), list):
            raise ValueError("expected object response with {!r} list from {}".format(key, current))
        items.extend(item for item in value[key] if isinstance(item, dict))
        current = next_link(headers.get("link", ""))
    return items


def body_digest(value: object) -> str:
    text = value if isinstance(value, str) else ""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def marker_regex(marker: str) -> re.Pattern[str]:
    return re.compile(r"<!--\s*" + re.escape(marker) + r"\s*(\{.*?\})\s*-->", re.DOTALL)


def marker_objects(body: object, marker: str) -> List[Dict[str, object]]:
    text = body if isinstance(body, str) else ""
    records: List[Dict[str, object]] = []
    for raw in marker_regex(marker).findall(text):
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            records.append(value)
    return records


def checkpoint_sha256(body: str, marker: str) -> str:
    blocks = marker_objects(body, marker)
    if len(blocks) != 1:
        return ""
    canonical = json.dumps(blocks[0], sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def canonical_pr_body_without_checkpoint(body: str, marker: str) -> str:
    stripped = marker_regex(marker).sub("", body or "", count=1).rstrip()
    return stripped + "\n" if stripped else ""


def pr_body_sha256(body: str, marker: str) -> str:
    canonical = canonical_pr_body_without_checkpoint(body, marker)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def is_trusted_feedback(item: Dict[str, object], trusted: Iterable[str]) -> bool:
    association = str(item.get("author_association") or "")
    if association not in set(trusted):
        return False
    user = item.get("user")
    if not isinstance(user, dict):
        return False
    login = str(user.get("login") or "")
    user_type = str(user.get("type") or "")
    return bool(login) and not login.endswith("[bot]") and user_type != "Bot"


def feedback_record(kind: str, item: Dict[str, object]) -> Dict[str, object]:
    user = item.get("user") if isinstance(item.get("user"), dict) else {}
    created = item.get("submitted_at") or item.get("created_at") or ""
    updated = item.get("updated_at") or item.get("dismissed_at") or created
    return {
        "kind": kind,
        "id": int(item.get("id") or 0),
        "author": str(user.get("login") or ""),
        "author_association": str(item.get("author_association") or ""),
        "state": str(item.get("state") or ""),
        "created_at": str(created or ""),
        "updated_at": str(updated or ""),
        "body_sha256": body_digest(item.get("body")),
    }


def feedback_sha256(repository: str, pr_number: int, token: str, trusted: Iterable[str]) -> str:
    """Hash trusted review feedback attached to the PR head lifecycle."""
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    endpoints = (
        ("review", "{}/repos/{}/pulls/{}/reviews?per_page=100".format(API_ROOT, encoded_repo, pr_number)),
        ("review-comment", "{}/repos/{}/pulls/{}/comments?per_page=100".format(API_ROOT, encoded_repo, pr_number)),
    )
    records: List[Dict[str, object]] = []
    for kind, url in endpoints:
        for item in paged_list(url, token):
            if is_trusted_feedback(item, trusted):
                records.append(feedback_record(kind, item))
    records.sort(key=lambda item: (str(item["kind"]), int(item["id"])))
    canonical = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def fetch_text_file(repository: str, path: str, ref: str, token: str) -> str:
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    url = "{}/repos/{}/contents/{}?ref={}".format(
        API_ROOT,
        encoded_repo,
        "/".join(urllib.parse.quote(part, safe="") for part in path.split("/")),
        urllib.parse.quote(ref, safe=""),
    )
    value, _ = request_json(url, token)
    if not isinstance(value, dict) or value.get("encoding") != "base64":
        raise ValueError("unable to read {} from target branch".format(path))
    raw = str(value.get("content") or "").replace("\n", "")
    return base64.b64decode(raw).decode("utf-8")


def global_codeowners(text: str) -> Set[str]:
    owners: Set[str] = set()
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if not parts or parts[0] != "*":
            continue
        for token in parts[1:]:
            if token.startswith("@") and "/" not in token:
                owners.add(token[1:])
    if not owners:
        raise ValueError("target-branch CODEOWNERS has no global user owner for maintainer authorization")
    return owners


def collaborator_permission(repository: str, login: str, token: str) -> str:
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    url = "{}/repos/{}/collaborators/{}/permission".format(
        API_ROOT, encoded_repo, urllib.parse.quote(login, safe="")
    )
    value, _ = request_json(url, token)
    if not isinstance(value, dict):
        return ""
    return str(value.get("role_name") or value.get("permission") or "")


def authorized_codeowners(repository: str, owners: Set[str], token: str) -> Set[str]:
    allowed = {"admin", "maintain", "write"}
    authorized = {
        login for login in owners
        if collaborator_permission(repository, login, token) in allowed
    }
    if not authorized:
        raise ValueError("target-branch global CODEOWNERS has no current write/maintain/admin maintainer")
    return authorized


def is_codeowner_comment(
    item: Dict[str, object], codeowners: Set[str], trusted_associations: Iterable[str]
) -> bool:
    if str(item.get("author_association") or "") not in set(trusted_associations):
        return False
    user = item.get("user")
    if not isinstance(user, dict):
        return False
    login = str(user.get("login") or "")
    user_type = str(user.get("type") or "")
    return bool(login) and login in codeowners and not login.endswith("[bot]") and user_type != "Bot"


def readiness_state_from_timeline(events: Iterable[Dict[str, object]]) -> Tuple[str, str]:
    """Return the current ready head and latest ready transition time."""
    last_commit = ""
    ready_head = ""
    ready_at = ""
    for event in events:
        kind = str(event.get("event") or "")
        if kind == "committed":
            sha = str(event.get("sha") or "")
            if sha:
                last_commit = sha
        elif kind == "ready_for_review":
            ready_head = last_commit
            ready_at = str(event.get("created_at") or "") if ready_head else ""
        elif kind == "convert_to_draft":
            ready_head = ""
            ready_at = ""
    return ready_head, ready_at


def issue_comments(repository: str, pr_number: int, token: str) -> List[Dict[str, object]]:
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    return paged_list(
        "{}/repos/{}/issues/{}/comments?per_page=100".format(API_ROOT, encoded_repo, pr_number),
        token,
    )


def agent_none_approved(
    comments: Iterable[Dict[str, object]],
    codeowners: Set[str],
    trusted_associations: Iterable[str],
    marker: str,
    head_sha: str,
) -> bool:
    """Require a current-authority CODEOWNER opt-out bound to the exact current head."""
    expected = {"agent_assistance": "none", "head_sha": head_sha}
    for item in comments:
        if not is_codeowner_comment(item, codeowners, trusted_associations):
            continue
        for value in marker_objects(item.get("body"), marker):
            if value == expected:
                return True
    return False


def readiness_approval(
    comments: Iterable[Dict[str, object]],
    codeowners: Set[str],
    trusted_associations: Iterable[str],
    marker: str,
    head_sha: str,
    merge_sha: str,
    current_checkpoint_sha256: str,
    current_pr_body_sha256: str,
    ready_at: str,
) -> Tuple[bool, bool]:
    """Return (durable body/head/merge approval, exact transition authorization)."""
    approval_present = False
    transition_authorized = False
    if not ready_at:
        return approval_present, transition_authorized
    for item in comments:
        if not is_codeowner_comment(item, codeowners, trusted_associations):
            continue
        created_at = str(item.get("created_at") or "")
        updated_at = str(item.get("updated_at") or created_at)
        # An approval created or edited after Ready cannot authorize that Ready cycle.
        if not created_at or created_at > ready_at or not updated_at or updated_at > ready_at:
            continue
        for value in marker_objects(item.get("body"), marker):
            if value.get("head_sha") != head_sha:
                continue
            if value.get("merge_sha") != merge_sha:
                continue
            if value.get("pr_body_sha256") != current_pr_body_sha256:
                continue
            approval_present = True
            if (
                current_checkpoint_sha256
                and value.get("checkpoint_sha256") == current_checkpoint_sha256
            ):
                transition_authorized = True
    return approval_present, transition_authorized


def _run_and_job_from_details(details_url: str) -> Tuple[Optional[int], Optional[int]]:
    match = re.search(r"/actions/runs/(\d+)/job/(\d+)(?:$|[/?#])", details_url or "")
    if not match:
        return None, None
    return int(match.group(1)), int(match.group(2))


def readiness_check_passed(
    repository: str,
    pr_number: int,
    head_sha: str,
    ready_at: str,
    token: str,
    check_name: str,
    workflow_path: str,
    readiness_step_name: str,
) -> bool:
    """Verify successful readiness evidence from the exact Actions workflow/job provenance."""
    if not head_sha or not ready_at:
        return False
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    checks_url = "{}/repos/{}/commits/{}/check-runs?per_page=100&filter=all".format(
        API_ROOT, encoded_repo, urllib.parse.quote(head_sha, safe="")
    )
    for item in paged_object_items(checks_url, token, "check_runs"):
        if str(item.get("name") or "") != check_name:
            continue
        if str(item.get("conclusion") or "") != "success":
            continue
        completed_at = str(item.get("completed_at") or "")
        if not completed_at or completed_at < ready_at:
            continue
        app = item.get("app") if isinstance(item.get("app"), dict) else {}
        if str(app.get("slug") or "") != "github-actions":
            continue
        run_id, job_id = _run_and_job_from_details(str(item.get("details_url") or ""))
        if run_id is None or job_id is None:
            continue

        run_url = "{}/repos/{}/actions/runs/{}".format(API_ROOT, encoded_repo, run_id)
        run, _ = request_json(run_url, token)
        if not isinstance(run, dict):
            continue
        if str(run.get("path") or "") != workflow_path:
            continue
        if str(run.get("event") or "") != "pull_request":
            continue
        if str(run.get("head_sha") or "") != head_sha:
            continue
        if str(run.get("created_at") or "") < ready_at:
            continue
        suite = item.get("check_suite") if isinstance(item.get("check_suite"), dict) else {}
        if int(run.get("check_suite_id") or 0) != int(suite.get("id") or 0):
            continue
        pull_numbers = {
            int(pr.get("number") or 0)
            for pr in run.get("pull_requests", [])
            if isinstance(pr, dict)
        }
        if pr_number not in pull_numbers:
            continue

        job_url = "{}/repos/{}/actions/jobs/{}".format(API_ROOT, encoded_repo, job_id)
        job, _ = request_json(job_url, token)
        if not isinstance(job, dict):
            continue
        if int(job.get("run_id") or 0) != run_id:
            continue
        if str(job.get("name") or "") != check_name or str(job.get("conclusion") or "") != "success":
            continue
        steps = [step for step in job.get("steps", []) if isinstance(step, dict)]
        if not any(
            str(step.get("name") or "") == readiness_step_name
            and str(step.get("conclusion") or "") == "success"
            for step in steps
        ):
            continue
        return True
    return False


def fetch_context(
    repository: str,
    pr_number: int,
    merge_sha: str,
    event_name: str,
    event_action: str,
    token: str,
    contract: Dict[str, object],
) -> Dict[str, object]:
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    pr_url = "{}/repos/{}/pulls/{}".format(API_ROOT, encoded_repo, pr_number)
    pr, _ = request_json(pr_url, token)
    if not isinstance(pr, dict):
        raise ValueError("pull request response is not an object")

    base = pr.get("base") if isinstance(pr.get("base"), dict) else {}
    head = pr.get("head") if isinstance(pr.get("head"), dict) else {}
    base_ref = str(base.get("ref") or "")
    if not base_ref:
        raise ValueError("pull request has no base ref")

    branch_url = "{}/repos/{}/branches/{}".format(
        API_ROOT, encoded_repo, urllib.parse.quote(base_ref, safe="")
    )
    branch, _ = request_json(branch_url, token)
    if not isinstance(branch, dict) or not isinstance(branch.get("commit"), dict):
        raise ValueError("base branch response lacks commit data")
    base_tip_sha = str(branch["commit"].get("sha") or "")

    api_merge_sha = str(pr.get("merge_commit_sha") or "")
    if api_merge_sha and api_merge_sha != merge_sha:
        raise ValueError(
            "checked-out tested merge {} does not match GitHub PR merge {}".format(
                merge_sha, api_merge_sha
            )
        )

    body = str(pr.get("body") or "")
    head_sha = str(head.get("sha") or "")
    timeline_url = "{}/repos/{}/issues/{}/timeline?per_page=100".format(
        API_ROOT, encoded_repo, pr_number
    )
    timeline = paged_list(timeline_url, token)
    ready_head_sha, ready_at = readiness_state_from_timeline(timeline)

    codeowners_text = fetch_text_file(
        repository,
        str(contract.get("maintainer_authority_path") or ".github/CODEOWNERS"),
        base_tip_sha,
        token,
    )
    declared_codeowners = global_codeowners(codeowners_text)
    codeowners = authorized_codeowners(repository, declared_codeowners, token)
    trusted = [str(item) for item in contract.get("trusted_feedback_author_associations", [])]
    comments = issue_comments(repository, pr_number, token)
    checkpoint_marker = str(contract.get("pr_checkpoint_marker") or "ua-agent-checkpoint")
    current_checkpoint_hash = checkpoint_sha256(body, checkpoint_marker)
    current_body_hash = pr_body_sha256(body, checkpoint_marker)
    ready_approval_present, ready_transition_authorized = readiness_approval(
        comments,
        codeowners,
        trusted,
        str(contract.get("ready_approval_marker") or "ua-agent-ready-approval"),
        head_sha,
        merge_sha,
        current_checkpoint_hash,
        current_body_hash,
        ready_at,
    )
    durable_ready_check = readiness_check_passed(
        repository,
        pr_number,
        head_sha,
        ready_at,
        token,
        str(contract.get("readiness_check_name") or "Agent protocol / readiness authorization"),
        str(contract.get("readiness_workflow_path") or ".github/workflows/change-coupling.yml"),
        str(contract.get("readiness_step_name") or "Record successful head-bound readiness authorization"),
    )

    labels = [
        str(item.get("name"))
        for item in pr.get("labels", [])
        if isinstance(item, dict) and item.get("name")
    ]
    return {
        "repository": repository,
        "pr_number": pr_number,
        "body": body,
        "pr_body_sha256": current_body_hash,
        "diff_base_sha": str(base.get("sha") or ""),
        "base_ref": base_ref,
        "base_tip_sha": base_tip_sha,
        "head_sha": head_sha,
        "merge_sha": merge_sha,
        "draft": bool(pr.get("draft")),
        "ready_head_sha": ready_head_sha,
        "ready_at": ready_at,
        "ready_approval_present": ready_approval_present,
        "ready_transition_authorized": ready_transition_authorized,
        "ready_check_passed": durable_ready_check,
        "checkpoint_sha256": current_checkpoint_hash,
        "agent_none_approved": agent_none_approved(
            comments,
            codeowners,
            trusted,
            str(contract.get("agent_none_approval_marker") or "ua-agent-assistance-none"),
            head_sha,
        ),
        "event_name": event_name,
        "event_action": event_action,
        "feedback_sha256": feedback_sha256(repository, pr_number, token, trusted),
        "labels": sorted(labels),
        "maintainer_codeowners": sorted(codeowners),
        "pr_author": str((pr.get("user") or {}).get("login") if isinstance(pr.get("user"), dict) else ""),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--pr-number", required=True, type=int)
    parser.add_argument("--merge-sha", required=True)
    parser.add_argument("--event-name", default="")
    parser.add_argument("--event-action", default="")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("Missing GITHUB_TOKEN", file=sys.stderr)
        return 2
    try:
        contract = load_contract(args.contract.resolve())
        context = fetch_context(
            args.repository,
            args.pr_number,
            args.merge_sha,
            args.event_name,
            args.event_action,
            token,
            contract,
        )
    except Exception as exc:
        print("Agent-checkpoint context error: {}".format(exc), file=sys.stderr)
        return 2
    args.output.write_text(json.dumps(context, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "Agent-checkpoint context collected: PR #{}, base-tip {}, head {}, merge {}, "
        "ready-head {}, ready-check {}, transition-approval {}, checkpoint {}, feedback {}.".format(
            context["pr_number"], context["base_tip_sha"], context["head_sha"],
            context["merge_sha"], context["ready_head_sha"], context["ready_check_passed"],
            context["ready_transition_authorized"], context["checkpoint_sha256"],
            context["feedback_sha256"],
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
