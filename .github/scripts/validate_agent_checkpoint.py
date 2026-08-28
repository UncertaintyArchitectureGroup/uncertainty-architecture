#!/usr/bin/env python3
"""Validate that a PR agent checkpoint is bound to the exact reviewed PR state."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/agent-checkpoint-contract.json"
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


def git(root: Path, args: Sequence[str], check: bool = True) -> str:
    result = subprocess.run(
        ["git"] + list(args),
        cwd=str(root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if check and result.returncode != 0:
        raise ValueError("git {} failed: {}".format(" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def changed_paths(root: Path, base: str, head: str) -> List[str]:
    """Return both sides of renames/copies so old and new instruction scopes are reviewed."""
    output = git(root, ["diff", "--name-status", "-M", base, head])
    paths = set()
    for line in output.splitlines():
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        status = parts[0]
        if status.startswith(("R", "C")) and len(parts) >= 3:
            paths.add(parts[1])
            paths.add(parts[2])
        else:
            paths.add(parts[-1])
    return sorted(path for path in paths if path)


def path_exists_at(root: Path, ref: str, path: str) -> bool:
    result = subprocess.run(
        ["git", "cat-file", "-e", "{}:{}".format(ref, path)],
        cwd=str(root),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def blob_sha_at(root: Path, ref: str, path: str) -> str:
    value = git(root, ["rev-parse", "{}:{}".format(ref, path)])
    if not SHA_RE.fullmatch(value):
        raise ValueError("unexpected blob SHA for {} at {}: {!r}".format(path, ref, value))
    return value


def applicable_instruction_blob(
    root: Path,
    base_tip: str,
    merge: str,
    path: str,
) -> Optional[str]:
    """Prefer tested merge-result guidance; fall back to current base guidance when the PR deletes it."""
    if path_exists_at(root, merge, path):
        return blob_sha_at(root, merge, path)
    if path_exists_at(root, base_tip, path):
        return blob_sha_at(root, base_tip, path)
    return None


def applicable_agent_records(
    root: Path,
    base: str,
    base_tip: str,
    head: str,
    merge: str,
) -> List[Dict[str, str]]:
    candidates = set()
    if applicable_instruction_blob(root, base_tip, merge, "AGENTS.md") is not None:
        candidates.add("AGENTS.md")

    for changed in changed_paths(root, base, head):
        parent = PurePosixPath(changed).parent
        while str(parent) not in (".", ""):
            candidate = "{}/AGENTS.md".format(parent.as_posix())
            if applicable_instruction_blob(root, base_tip, merge, candidate) is not None:
                candidates.add(candidate)
            parent = parent.parent

    records = []
    for path in sorted(candidates):
        blob_sha = applicable_instruction_blob(root, base_tip, merge, path)
        if blob_sha is None:
            continue
        records.append({"path": path, "blob_sha": blob_sha})
    return records


def checkpoint_regex(contract: Dict[str, object]) -> re.Pattern[str]:
    marker = re.escape(str(contract["pr_checkpoint_marker"]))
    return re.compile(r"<!--\s*" + marker + r"\s*(\{.*?\})\s*-->", re.DOTALL)


def canonical_pr_body_without_checkpoint(body: str, contract: Dict[str, object]) -> str:
    """Return the PR body state being attested, excluding the attestation itself."""
    stripped = checkpoint_regex(contract).sub("", body or "", count=1).rstrip()
    return stripped + "\n" if stripped else ""


def pr_body_sha256(body: str, contract: Dict[str, object]) -> str:
    canonical = canonical_pr_body_without_checkpoint(body, contract)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def parse_checkpoint(body: str, contract: Dict[str, object]) -> Tuple[Optional[Dict[str, object]], Optional[str]]:
    blocks = checkpoint_regex(contract).findall(body or "")
    marker = str(contract["pr_checkpoint_marker"])
    if len(blocks) != 1:
        return None, "PR body must contain exactly one {} JSON block".format(marker)
    try:
        value = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        return None, "{} JSON is invalid: {}".format(marker, exc)
    if not isinstance(value, dict):
        return None, "{} must be a JSON object".format(marker)
    return value, None


def validate_schema(data: Dict[str, object], contract: Dict[str, object]) -> List[Finding]:
    findings: List[Finding] = []
    required = set(str(item) for item in contract["required_fields"])
    for field in sorted(required - set(data)):
        findings.append(Finding("error", "agent checkpoint is missing field {!r}".format(field)))
    for field in sorted(set(data) - required):
        findings.append(Finding("error", "agent checkpoint contains unknown field {!r}".format(field)))

    if data.get("checkpoint_version") != contract["checkpoint_version"]:
        findings.append(
            Finding(
                "error",
                "agent checkpoint_version must be {!r}".format(contract["checkpoint_version"]),
            )
        )

    for field in (
        "reviewed_base_sha",
        "reviewed_base_tip_sha",
        "reviewed_head_sha",
        "reviewed_merge_sha",
    ):
        value = data.get(field)
        if not isinstance(value, str) or not SHA_RE.fullmatch(value):
            findings.append(
                Finding(
                    "error",
                    "{} must be a full lowercase 40-character commit SHA".format(field),
                )
            )

    body_hash = data.get("reviewed_pr_body_sha256")
    if not isinstance(body_hash, str) or not SHA256_RE.fullmatch(body_hash):
        findings.append(
            Finding(
                "error",
                "reviewed_pr_body_sha256 must be a lowercase 64-character SHA-256 digest",
            )
        )

    records = data.get("applicable_agents")
    if not isinstance(records, list) or not records:
        findings.append(Finding("error", "applicable_agents must be a non-empty list"))
    else:
        seen = set()
        normalized_paths = []
        for index, record in enumerate(records):
            if not isinstance(record, dict) or set(record) != {"path", "blob_sha"}:
                findings.append(
                    Finding("error", "applicable_agents[{}] must contain exactly path and blob_sha".format(index))
                )
                continue
            path = record.get("path")
            sha = record.get("blob_sha")
            if not isinstance(path, str) or not path.endswith("AGENTS.md"):
                findings.append(Finding("error", "applicable_agents[{}].path must name an AGENTS.md file".format(index)))
            elif path in seen:
                findings.append(Finding("error", "applicable_agents contains duplicate path {!r}".format(path)))
            else:
                seen.add(path)
                normalized_paths.append(path)
            if not isinstance(sha, str) or not SHA_RE.fullmatch(sha):
                findings.append(Finding("error", "applicable_agents[{}].blob_sha must be a full blob SHA".format(index)))
        if normalized_paths and normalized_paths != sorted(normalized_paths):
            findings.append(Finding("error", "applicable_agents must be sorted by path"))

    for field, allowed in contract["controlled_values"].items():
        value = data.get(field)
        if not isinstance(value, str) or value not in set(str(item) for item in allowed):
            findings.append(
                Finding("error", "agent checkpoint field {!r} uses uncontrolled value {!r}".format(field, value))
            )
    return findings


def validate(
    root: Path,
    contract_path: Path,
    base: str,
    base_tip: str,
    head: str,
    merge: str,
    body: str,
) -> List[Finding]:
    contract = load_json(contract_path)
    data, error = parse_checkpoint(body, contract)
    if error:
        return [Finding("error", error)]
    assert data is not None

    findings = validate_schema(data, contract)
    if findings:
        return findings

    expected_shas = {
        "reviewed_base_sha": base,
        "reviewed_base_tip_sha": base_tip,
        "reviewed_head_sha": head,
        "reviewed_merge_sha": merge,
    }
    for field, expected in expected_shas.items():
        actual = str(data[field])
        if actual != expected:
            findings.append(
                Finding(
                    "error",
                    "agent checkpoint is stale: {} {} does not match current {}.".format(
                        field, actual, expected
                    ),
                )
            )

    expected_body_hash = pr_body_sha256(body, contract)
    if data["reviewed_pr_body_sha256"] != expected_body_hash:
        findings.append(
            Finding(
                "error",
                "agent checkpoint is stale: reviewed_pr_body_sha256 does not match the current PR description. "
                "Expected {}.".format(expected_body_hash),
            )
        )

    expected_agents = applicable_agent_records(root, base, base_tip, head, merge)
    actual_agents = data["applicable_agents"]
    if actual_agents != expected_agents:
        findings.append(
            Finding(
                "error",
                "applicable_agents does not match the current PR diff and tested merge result. Expected: {}".format(
                    json.dumps(expected_agents, sort_keys=True)
                ),
            )
        )

    if findings:
        findings.append(
            Finding(
                "error",
                "Re-read the exact applicable AGENTS.md files from the tested merge state, current diff, "
                "current PR description, available corrective feedback, and end-of-session protocol, "
                "then refresh ua-agent-checkpoint.",
            )
        )
    else:
        print(
            "Agent context accepted: base-tip {}, head {}, merge {}, applicable instructions {}.".format(
                base_tip,
                head,
                merge,
                json.dumps(expected_agents, sort_keys=True),
            )
        )
    return findings


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--base", required=True, help="PR diff-base SHA supplied by GitHub")
    parser.add_argument("--base-tip", required=True, help="Current tip SHA of the target branch")
    parser.add_argument("--head", required=True, help="Current PR head SHA")
    parser.add_argument("--merge", required=True, help="GitHub tested merge-result SHA")
    parser.add_argument("--pr-body-file", type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    body = (
        args.pr_body_file.read_text(encoding="utf-8")
        if args.pr_body_file
        else os.environ.get("PR_BODY", "")
    )
    try:
        findings = validate(
            args.root.resolve(),
            args.contract.resolve(),
            args.base,
            args.base_tip,
            args.head,
            args.merge,
            body,
        )
    except ValueError as exc:
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
