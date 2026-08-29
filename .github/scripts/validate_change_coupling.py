#!/usr/bin/env python3
"""Validate PR declarations and companion-file coupling against the PR-owned git diff."""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/change-coupling-contract.json"
PR_BLOCK = re.compile(r"<!--\s*ua-change-contract\s*(\{.*?\})\s*-->", re.DOTALL)


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
        ["git"] + list(args), cwd=str(root), text=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )
    if result.returncode != 0:
        raise ValueError("git {} failed: {}".format(" ".join(args), result.stderr.strip()))
    return result.stdout.strip()


def merge_base(root: Path, base_tip: str, head: str) -> str:
    value = git(root, ["merge-base", base_tip, head])
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("unexpected merge-base SHA: {!r}".format(value))
    return value


def changed_entries(root: Path, base_tip: str, head: str) -> List[Tuple[str, str, Optional[str]]]:
    """Return PR-owned changes from current-target merge-base through PR head."""
    comparison_base = merge_base(root, base_tip, head)
    output = git(root, ["diff", "--name-status", "-M", comparison_base, head])
    entries: List[Tuple[str, str, Optional[str]]] = []
    for raw in output.splitlines():
        parts = raw.split("\t")
        if not parts:
            continue
        status = parts[0]
        if status.startswith("R") and len(parts) == 3:
            entries.append(("R", parts[1], parts[2]))
        elif len(parts) == 2:
            entries.append((status[:1], parts[1], None))
    return entries


def all_paths(entries: Iterable[Tuple[str, str, Optional[str]]]) -> Set[str]:
    paths: Set[str] = set()
    for _, old, new in entries:
        paths.add(old)
        if new:
            paths.add(new)
    return paths


def matches(path: str, prefixes: Iterable[str]) -> bool:
    return any(path == prefix or path.startswith(prefix) for prefix in prefixes)


def parse_pr_contract(body: str) -> Tuple[Optional[Dict[str, object]], Optional[str]]:
    matches_found = PR_BLOCK.findall(body or "")
    if len(matches_found) != 1:
        return None, "PR body must contain exactly one ua-change-contract JSON block"
    try:
        value = json.loads(matches_found[0])
    except json.JSONDecodeError as exc:
        return None, "ua-change-contract JSON is invalid: {}".format(exc)
    if not isinstance(value, dict):
        return None, "ua-change-contract must be a JSON object"
    return value, None


def has_exception(labels: Set[str], contract: Dict[str, object], category: str) -> bool:
    for label, categories in contract["exception_labels"].items():
        if label in labels and category in categories:
            return True
    return False


def validate_schema(data: Dict[str, object], contract: Dict[str, object]) -> List[Finding]:
    findings: List[Finding] = []
    required = set(str(item) for item in contract["required_pr_fields"])
    unknown = set(data) - required
    for field in sorted(required - set(data)):
        findings.append(Finding("error", "PR contract is missing field {!r}".format(field)))
    for field in sorted(unknown):
        findings.append(Finding("error", "PR contract contains unknown field {!r}".format(field)))

    controlled = contract["controlled_values"]
    list_fields = ("owning_paths", "decision_levels", "capability_families")
    for field in list_fields:
        value = data.get(field)
        if not isinstance(value, list) or not value or any(not isinstance(item, str) for item in value):
            findings.append(Finding("error", "PR contract field {!r} must be a non-empty string list".format(field)))
            continue
        if field in controlled:
            allowed = set(str(item) for item in controlled[field])
            for item in value:
                if item not in allowed:
                    findings.append(Finding("error", "PR contract field {!r} contains uncontrolled value {!r}".format(field, item)))

    for field, allowed_values in controlled.items():
        if field in list_fields or field not in data:
            continue
        value = data[field]
        if not isinstance(value, str) or value not in set(str(item) for item in allowed_values):
            findings.append(Finding("error", "PR contract field {!r} uses uncontrolled value {!r}".format(field, value)))
    return findings


def validate_coupling(
    entries: List[Tuple[str, str, Optional[str]]], data: Dict[str, object], labels: Set[str],
    contract: Dict[str, object],
) -> List[Finding]:
    findings: List[Finding] = []
    paths = all_paths(entries)
    changed_files = {new or old for _, old, new in entries}

    notable = any(matches(path, contract["notable_change_prefixes"]) for path in paths)
    changelog_owner = str(contract["changelog_owner"])
    if notable and changelog_owner not in changed_files and not has_exception(labels, contract, "changelog"):
        findings.append(Finding("error", "notable change requires {} or maintainer exception label".format(changelog_owner)))
    if data.get("changelog") == "updated" and changelog_owner not in changed_files:
        findings.append(Finding("error", "PR contract declares changelog updated but {} is unchanged".format(changelog_owner)))
    if changelog_owner in changed_files and data.get("changelog") != "updated":
        findings.append(Finding("error", "{} changed but PR contract does not declare changelog updated".format(changelog_owner)))

    companion_rules = (
        ("glossary", "terminology_impact", "updated", str(contract["terminology_owner"])),
        ("roadmap", "roadmap", "updated", str(contract["roadmap_owner"])),
        ("traceability", "traceability", "updated", str(contract["traceability_owner"])),
    )
    for category, declaration, updated_value, owner in companion_rules:
        declared = data.get(declaration)
        if declared == updated_value and owner not in changed_files:
            findings.append(Finding("error", "PR contract declares {} updated but {} is unchanged".format(category, owner)))
        if owner in changed_files and declared != updated_value:
            findings.append(Finding("error", "{} changed but PR contract does not declare {} updated".format(owner, category)))

    research_state = data.get("research_state")
    if research_state in ("accepted", "narrowed", "rejected", "superseded", "reopened"):
        owner = str(contract["traceability_owner"])
        if owner not in changed_files and not has_exception(labels, contract, "traceability"):
            findings.append(Finding("error", "research-state decision requires {} or maintainer exception label".format(owner)))

    repository_policy_changed = any(matches(path, contract["repository_policy_prefixes"]) for path in paths)
    if repository_policy_changed and data.get("roadmap") != "updated" and not has_exception(labels, contract, "roadmap"):
        findings.append(Finding("error", "repository-policy baseline change requires roadmap update or maintainer exception label"))

    protected_moves = [entry for entry in entries if entry[0] in ("D", "R") and matches(entry[1], contract["deletion_rename_prefixes"])]
    if protected_moves:
        if data.get("compatibility") == "not-applicable" and not has_exception(labels, contract, "deletion-rename"):
            findings.append(Finding("error", "deletion or rename of maintained material requires an explicit compatibility decision"))
        if changelog_owner not in changed_files and not has_exception(labels, contract, "changelog"):
            findings.append(Finding("error", "deletion or rename of maintained material requires changelog update"))

    owning_paths = data.get("owning_paths") if isinstance(data.get("owning_paths"), list) else []
    if owning_paths:
        intersects = any(
            changed == owner or changed.startswith(owner.rstrip("/") + "/")
            for owner in owning_paths
            for changed in paths
        )
        if not intersects:
            findings.append(Finding("error", "none of the declared owning_paths intersects the PR-owned diff"))

    return findings


def validate(
    root: Path,
    contract_path: Path,
    base: str,
    head: str,
    body: str,
    labels: Set[str],
    actor: str = "",
) -> List[Finding]:
    contract = load_json(contract_path)
    data, error = parse_pr_contract(body)
    if error:
        if has_exception(labels, contract, "pr-contract"):
            return [Finding("warning", error + "; bypassed by maintainer exception label")]
        return [Finding("error", error)]
    assert data is not None

    # Dependabot does not author repository PR templates. Treat its PRs as
    # explicitly non-agent-assisted so the universal declaration does not
    # break dependency updates while human PRs remain required to declare it.
    if actor == "dependabot[bot]" and "agent_assistance" not in data:
        data = dict(data)
        data["agent_assistance"] = "none"

    findings = validate_schema(data, contract)
    entries = changed_entries(root, base, head)
    findings.extend(validate_coupling(entries, data, labels, contract))
    return findings


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--base", required=True, help="current target-branch tip SHA/ref")
    parser.add_argument("--head", required=True)
    parser.add_argument("--pr-body-file", type=Path)
    parser.add_argument("--labels", default="")
    parser.add_argument("--actor", default="")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    body = args.pr_body_file.read_text(encoding="utf-8") if args.pr_body_file else os.environ.get("PR_BODY", "")
    labels = {item.strip() for item in args.labels.split(",") if item.strip()}
    try:
        findings = validate(
            args.root.resolve(), args.contract.resolve(), args.base, args.head,
            body, labels, actor=args.actor,
        )
    except ValueError as exc:
        print("Change-coupling configuration error: {}".format(exc))
        return 2
    for finding in findings:
        print("::{}::{}".format(finding.severity, finding.message))
        print("{}: {}".format(finding.severity.upper(), finding.message))
    errors = [item for item in findings if item.severity == "error"]
    print("Change-coupling validation complete: {} error(s), {} finding(s).".format(len(errors), len(findings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
