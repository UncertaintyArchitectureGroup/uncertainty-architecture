#!/usr/bin/env python3
"""Validate the deterministic checked-state checkpoint for AI-assisted pull requests."""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/agent-checkpoint-contract.json"
DEFAULT_CHANGE_CONTRACT = ROOT / ".github/policy/change-coupling-contract.json"
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class Finding:
    def __init__(self, severity: str, message: str) -> None:
        self.severity = severity
        self.message = message


def load_json(path: Path) -> Dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError("contract does not exist: {}".format(path))
    except json.JSONDecodeError as exc:
        raise ValueError("contract JSON is invalid: {}".format(exc))
    if value.get("contract_version") != 1:
        raise ValueError("unsupported contract_version: {!r}".format(value.get("contract_version")))
    return value


def git(root: Path, args: Sequence[str]) -> str:
    result = subprocess.run(
        ["git"] + list(args), cwd=str(root), text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if result.returncode != 0:
        raise ValueError("git {} failed: {}".format(" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def merge_base(root: Path, base_tip: str, head: str) -> str:
    value = git(root, ["merge-base", base_tip, head])
    if not SHA_RE.fullmatch(value):
        raise ValueError("unexpected merge-base SHA: {!r}".format(value))
    return value


def changed_paths(root: Path, base_tip: str, head: str) -> List[str]:
    """Return PR-owned changed paths from current-target merge-base to head."""
    comparison_base = merge_base(root, base_tip, head)
    output = git(root, ["diff", "--name-status", "-M", comparison_base, head])
    paths = set()
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0]
        if status.startswith("R") and len(parts) >= 3:
            paths.add(parts[1])
            paths.add(parts[2])
        else:
            paths.add(parts[-1])
    return sorted(path for path in paths if path)


def path_matches(path: str, prefixes: Iterable[str]) -> bool:
    return any(path == prefix or path.startswith(prefix) for prefix in prefixes)


def path_exists_at(root: Path, ref: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", "{}:{}".format(ref, path)],
        cwd=str(root), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def blob_sha_at(root: Path, ref: str, path: str) -> str:
    value = git(root, ["rev-parse", "{}:{}".format(ref, path)])
    if not SHA_RE.fullmatch(value):
        raise ValueError("unexpected blob SHA for {} at {}: {!r}".format(path, ref, value))
    return value


def applicable_instruction_blob(root: Path, base_tip: str, merge: str, path: str) -> Optional[str]:
    """Prefer tested merge guidance; use current-target guidance if the PR deletes it."""
    if path_exists_at(root, merge, path):
        return blob_sha_at(root, merge, path)
    if path_exists_at(root, base_tip, path):
        return blob_sha_at(root, base_tip, path)
    return None


def applicable_agent_records(
    root: Path, base_tip: str, head: str, merge: str
) -> List[Dict[str, str]]:
    candidates = set()
    if applicable_instruction_blob(root, base_tip, merge, "AGENTS.md") is not None:
        candidates.add("AGENTS.md")

    for changed in changed_paths(root, base_tip, head):
        parent = PurePosixPath(changed).parent
        while str(parent) not in (".", ""):
            candidate = "{}/AGENTS.md".format(parent.as_posix())
            if applicable_instruction_blob(root, base_tip, merge, candidate) is not None:
                candidates.add(candidate)
            parent = parent.parent

    records: List[Dict[str, str]] = []
    for path in sorted(candidates):
        sha = applicable_instruction_blob(root, base_tip, merge, path)
        if sha is not None:
            records.append({"path": path, "blob_sha": sha})
    return records


def marker_regex(marker: str) -> re.Pattern[str]:
    return re.compile(r"<!--\s*" + re.escape(marker) + r"\s*(\{.*?\})\s*-->", re.DOTALL)


def parse_block(body: str, marker: str) -> Tuple[Optional[Dict[str, object]], Optional[str]]:
    blocks = marker_regex(marker).findall(body or "")
    if len(blocks) != 1:
        return None, "PR body must contain exactly one {} JSON block".format(marker)
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        return None, "{} JSON is invalid: {}".format(marker, exc)
    if not isinstance(value, dict):
        return None, "{} must be a JSON object".format(marker)
    return value, None


def canonical_pr_body_without_checkpoint(body: str, checkpoint_marker: str) -> str:
    stripped = marker_regex(checkpoint_marker).sub("", body or "", count=1).rstrip()
    return stripped + "\n" if stripped else ""


def pr_body_sha256(body: str, checkpoint_marker: str) -> str:
    canonical = canonical_pr_body_without_checkpoint(body, checkpoint_marker)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def exception_labels_for(change_contract: Dict[str, object], category: str) -> Set[str]:
    labels: Set[str] = set()
    for label, categories in change_contract.get("exception_labels", {}).items():
        if isinstance(categories, list) and category in categories:
            labels.add(str(label))
    return labels


def validate_checkpoint_schema(data: Dict[str, object], contract: Dict[str, object]) -> List[Finding]:
    findings: List[Finding] = []
    required = set(str(item) for item in contract["required_fields"])
    for field in sorted(required - set(data)):
        findings.append(Finding("error", "agent checkpoint is missing field {!r}".format(field)))
    for field in sorted(set(data) - required):
        findings.append(Finding("error", "agent checkpoint contains unknown field {!r}".format(field)))

    if data.get("checkpoint_version") != contract["checkpoint_version"]:
        findings.append(Finding("error", "agent checkpoint_version must be {!r}".format(contract["checkpoint_version"])))

    for field in ("reviewed_base_sha", "reviewed_base_tip_sha", "reviewed_head_sha", "reviewed_merge_sha"):
        value = data.get(field)
        if not isinstance(value, str) or not SHA_RE.fullmatch(value):
            findings.append(Finding("error", "{} must be a full lowercase 40-character commit SHA".format(field)))

    for field in ("reviewed_pr_body_sha256", "reviewed_feedback_sha256"):
        value = data.get(field)
        if not isinstance(value, str) or not SHA256_RE.fullmatch(value):
            findings.append(Finding("error", "{} must be a lowercase 64-character SHA-256 digest".format(field)))

    records = data.get("applicable_agents")
    if not isinstance(records, list) or not records:
        findings.append(Finding("error", "applicable_agents must be a non-empty list"))
    else:
        seen = set()
        ordered: List[str] = []
        for index, record in enumerate(records):
            if not isinstance(record, dict) or set(record) != {"path", "blob_sha"}:
                findings.append(Finding("error", "applicable_agents[{}] must contain exactly path and blob_sha".format(index)))
                continue
            path = record.get("path")
            sha = record.get("blob_sha")
            if not isinstance(path, str) or not path.endswith("AGENTS.md"):
                findings.append(Finding("error", "applicable_agents[{}].path must name an AGENTS.md file".format(index)))
            elif path in seen:
                findings.append(Finding("error", "applicable_agents contains duplicate path {!r}".format(path)))
            else:
                seen.add(path)
                ordered.append(path)
            if not isinstance(sha, str) or not SHA_RE.fullmatch(sha):
                findings.append(Finding("error", "applicable_agents[{}].blob_sha must be a full blob SHA".format(index)))
        if ordered and ordered != sorted(ordered):
            findings.append(Finding("error", "applicable_agents must be sorted by path"))

    for field, allowed in contract["controlled_values"].items():
        value = data.get(field)
        if not isinstance(value, str) or value not in set(str(item) for item in allowed):
            findings.append(Finding("error", "agent checkpoint field {!r} uses uncontrolled value {!r}".format(field, value)))
    return findings


def validate(
    root: Path,
    contract_path: Path,
    context: Dict[str, object],
    change_contract_path: Path = DEFAULT_CHANGE_CONTRACT,
) -> List[Finding]:
    contract = load_json(contract_path)
    change_contract = load_json(change_contract_path)
    body = str(context.get("body") or "")
    labels = {
        str(item) for item in context.get("labels", [])
        if isinstance(item, str)
    }

    change, change_error = parse_block(body, str(contract["pr_change_contract_marker"]))
    if change_error:
        allowed_exceptions = exception_labels_for(change_contract, "pr-contract")
        if labels.intersection(allowed_exceptions):
            return [
                Finding(
                    "warning",
                    change_error + "; agent checkpoint bypassed by the same maintainer PR-contract exception",
                )
            ]
        return [Finding("error", change_error)]
    assert change is not None

    assistance = change.get("agent_assistance")
    pr_author = str(context.get("pr_author") or "")
    if assistance == "none":
        if pr_author == "dependabot[bot]" or bool(context.get("agent_none_approved")):
            return []
        return [
            Finding(
                "error",
                "agent_assistance 'none' is a maintainer-controlled, head-bound opt-out. A target-branch CODEOWNER must add the structured ua-agent-assistance-none approval for the current head before the checkpoint can be disabled.",
            )
        ]
    if assistance != "used":
        if pr_author == "dependabot[bot]" and assistance is None:
            return []
        return [Finding("error", "ua-change-contract must declare agent_assistance as 'used' or 'none'")]

    checkpoint, checkpoint_error = parse_block(body, str(contract["pr_checkpoint_marker"]))
    if checkpoint_error:
        return [Finding("error", checkpoint_error)]
    assert checkpoint is not None

    findings = validate_checkpoint_schema(checkpoint, contract)
    if findings:
        return findings

    base_tip = str(context.get("base_tip_sha") or "")
    head = str(context.get("head_sha") or "")
    merge = str(context.get("merge_sha") or "")
    owned_paths = changed_paths(root, base_tip, head)
    repository_policy_prefixes = [
        str(item) for item in change_contract.get("repository_policy_prefixes", [])
    ]
    repository_policy_changed = any(
        path_matches(path, repository_policy_prefixes) for path in owned_paths
    )

    change_class = str(change.get("change_class") or "")
    if repository_policy_changed and change_class != "repository-policy":
        findings.append(
            Finding(
                "error",
                "PR-owned repository-policy paths require change_class 'repository-policy'; declaration {!r} cannot disable repository-policy controls.".format(change_class),
            )
        )

    draft_required = set(str(item) for item in contract.get("draft_required_change_classes", []))
    effective_draft_required = change_class in draft_required or repository_policy_changed
    is_draft = bool(context.get("draft"))
    ready_head = str(context.get("ready_head_sha") or "")
    event_name = str(context.get("event_name") or "")
    event_action = str(context.get("event_action") or "")
    transition_ready = (
        event_name == "pull_request"
        and event_action == "ready_for_review"
        and ready_head == head
        and bool(context.get("ready_transition_authorized"))
    )
    durable_ready = (
        ready_head == head
        and bool(context.get("ready_approval_present"))
        and bool(context.get("ready_check_passed"))
    )
    if effective_draft_required and not is_draft and not (transition_ready or durable_ready):
        effective_label = "repository-policy" if repository_policy_changed else change_class
        findings.append(
            Finding(
                "error",
                "AI-assisted {} PR must remain Draft during repository-changing iterations. "
                "Leaving Draft requires a target-branch CODEOWNER approval bound to the current head, tested merge state, PR-body digest, and fresh checkpoint, followed by verified readiness-authorization workflow evidence.".format(effective_label),
            )
        )

    expected_shas = {
        "reviewed_base_sha": str(context.get("diff_base_sha") or ""),
        "reviewed_base_tip_sha": base_tip,
        "reviewed_head_sha": head,
        "reviewed_merge_sha": merge,
    }
    for field, expected in expected_shas.items():
        actual = str(checkpoint[field])
        if actual != expected:
            findings.append(Finding("error", "agent checkpoint is stale: {} {} does not match current {}.".format(field, actual, expected)))

    body_hash = pr_body_sha256(body, str(contract["pr_checkpoint_marker"]))
    if checkpoint["reviewed_pr_body_sha256"] != body_hash:
        findings.append(Finding("error", "agent checkpoint is stale: reviewed_pr_body_sha256 does not match the current PR description. Expected {}.".format(body_hash)))

    feedback_hash = str(context.get("feedback_sha256") or "")
    if checkpoint["reviewed_feedback_sha256"] != feedback_hash:
        findings.append(Finding("error", "agent checkpoint is stale: reviewed_feedback_sha256 does not match current trusted PR review feedback. Expected {}.".format(feedback_hash)))

    expected_agents = applicable_agent_records(root, base_tip, head, merge)
    if checkpoint["applicable_agents"] != expected_agents:
        findings.append(Finding("error", "applicable_agents does not match PR-owned changed paths and the tested merge result. Expected: {}".format(json.dumps(expected_agents, sort_keys=True))))

    if findings:
        findings.append(
            Finding(
                "error",
                "Re-read the effective AGENTS.md files from the tested merge state, PR-owned diff, current PR description, external conversation corrective signals, trusted PR review feedback, maintainer approval evidence, and end-of-session protocol, then refresh ua-agent-checkpoint.",
            )
        )
    else:
        print(
            "Agent checkpoint accepted: base-tip {}, head {}, merge {}, ready-head {}, durable-ready {}, feedback {}, instructions {}.".format(
                base_tip, head, merge, ready_head, durable_ready, feedback_hash,
                json.dumps(expected_agents, sort_keys=True),
            )
        )
    return findings


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--change-contract", type=Path, default=DEFAULT_CHANGE_CONTRACT)
    parser.add_argument("--context-file", type=Path, required=True)
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        context = json.loads(args.context_file.read_text(encoding="utf-8"))
        if not isinstance(context, dict):
            raise ValueError("context file must contain a JSON object")
        findings = validate(
            args.root.resolve(), args.contract.resolve(), context,
            change_contract_path=args.change_contract.resolve(),
        )
    except (ValueError, FileNotFoundError, json.JSONDecodeError) as exc:
        print("Agent-checkpoint configuration error: {}".format(exc))
        return 2
    for finding in findings:
        print("::{}::{}".format(finding.severity, finding.message))
        print("{}: {}".format(finding.severity.upper(), finding.message))
    errors = [item for item in findings if item.severity == "error"]
    print("Agent-checkpoint validation complete: {} error(s), {} finding(s).".format(len(errors), len(findings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
