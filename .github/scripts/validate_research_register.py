#!/usr/bin/env python3
"""Validate the canonical Research Item Register and provenance links."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_REGISTER = ROOT / "content/research/research-register.md"
DEFAULT_NOTES_INDEX = ROOT / "content/research/notes/README.md"
BLOCK = re.compile(r"<!--\s*ua-research-register\s*(\{.*?\})\s*-->", re.DOTALL)
TABLE_BLOCK = re.compile(
    r"## Current material items\s*(.*?)\s*## Machine-readable register",
    re.DOTALL,
)
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$")
TABLE_ID_PATTERN = re.compile(r"`([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+)`")

ALLOWED_CLASSES: Set[str] = {
    "term",
    "hypothesis",
    "comparison",
    "process",
    "artifact",
    "evidence",
    "example",
    "provenance",
}
ALLOWED_STATUSES: Set[str] = {
    "open",
    "under-validation",
    "resolved",
    "superseded",
    "rejected",
}
ALLOWED_ORIGINS: Set[str] = {
    "external-dialogue",
    "external-review",
    "published-source",
    "repository-source",
    "internal-synthesis",
    "worked-application",
    "operational-observation",
}
EXTERNAL_ORIGINS = {"external-dialogue", "external-review"}
REQUIRED_ITEM_FIELDS: Sequence[str] = (
    "id",
    "title",
    "item_class",
    "status",
    "origin_kind",
    "provenance_record",
    "owning_record",
    "next_step",
)


class Finding:
    def __init__(self, severity: str, message: str) -> None:
        self.severity = severity
        self.message = message


def repository_path(root: Path, relative: str) -> Optional[Path]:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def parse_register(text: str) -> Dict[str, object]:
    matches = BLOCK.findall(text)
    if len(matches) != 1:
        raise ValueError("research register must contain exactly one ua-research-register JSON block")
    try:
        value = json.loads(matches[0])
    except json.JSONDecodeError as exc:
        raise ValueError("ua-research-register JSON is invalid: {}".format(exc))
    if not isinstance(value, dict):
        raise ValueError("ua-research-register must be a JSON object")
    return value


def status_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


def parse_human_table(text: str) -> Tuple[Dict[str, str], List[str]]:
    match = TABLE_BLOCK.search(text)
    if not match:
        return {}, ["research register must contain a Current material items table before the machine-readable block"]

    rows: Dict[str, str] = {}
    errors: List[str] = []
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) < 7 or cells[0] in {"ID", "---"} or set(cells[0]) <= {"-", ":"}:
            continue
        id_match = TABLE_ID_PATTERN.fullmatch(cells[0])
        if not id_match:
            continue
        item_id = id_match.group(1)
        if item_id in rows:
            errors.append("duplicate research-item ID {!r} in human-readable table".format(item_id))
            continue
        rows[item_id] = status_slug(cells[4])
    return rows, errors


def nonempty_string(item: Dict[str, object], field: str) -> bool:
    value = item.get(field)
    return isinstance(value, str) and bool(value.strip())


def validate(
    root: Path = ROOT,
    register_path: Path = DEFAULT_REGISTER,
    notes_index_path: Path = DEFAULT_NOTES_INDEX,
) -> List[Finding]:
    findings: List[Finding] = []
    if not register_path.is_file():
        return [Finding("error", "Research Item Register is missing: {}".format(register_path))]

    try:
        register_text = register_path.read_text(encoding="utf-8")
        data = parse_register(register_text)
    except (OSError, ValueError) as exc:
        return [Finding("error", str(exc))]

    table_rows, table_errors = parse_human_table(register_text)
    findings.extend(Finding("error", message) for message in table_errors)

    if data.get("version") != 1:
        findings.append(Finding("error", "unsupported research-register version: {!r}".format(data.get("version"))))

    items = data.get("items")
    if not isinstance(items, list) or not items:
        findings.append(Finding("error", "research register 'items' must be a non-empty list"))
        return findings

    seen: Set[str] = set()
    machine_statuses: Dict[str, str] = {}
    notes_index = notes_index_path.read_text(encoding="utf-8") if notes_index_path.is_file() else ""

    for position, raw_item in enumerate(items, start=1):
        if not isinstance(raw_item, dict):
            findings.append(Finding("error", "research item {} must be an object".format(position)))
            continue
        item: Dict[str, object] = raw_item
        label = str(item.get("id", "item-{}".format(position)))

        for field in REQUIRED_ITEM_FIELDS:
            if not nonempty_string(item, field):
                findings.append(Finding("error", "{} has missing or empty field {!r}".format(label, field)))

        item_id = item.get("id")
        if isinstance(item_id, str):
            if not ID_PATTERN.match(item_id):
                findings.append(Finding("error", "{} has invalid stable research-item ID".format(label)))
            if item_id in seen:
                findings.append(Finding("error", "duplicate research-item ID {!r}".format(item_id)))
            seen.add(item_id)

        item_class = item.get("item_class")
        if isinstance(item_class, str) and item_class not in ALLOWED_CLASSES:
            findings.append(Finding("error", "{} uses uncontrolled item_class {!r}".format(label, item_class)))

        status = item.get("status")
        if isinstance(status, str):
            if status not in ALLOWED_STATUSES:
                findings.append(Finding("error", "{} uses uncontrolled research lifecycle state {!r}".format(label, status)))
            if isinstance(item_id, str):
                machine_statuses[item_id] = status

        origin = item.get("origin_kind")
        if isinstance(origin, str) and origin not in ALLOWED_ORIGINS:
            findings.append(Finding("error", "{} uses uncontrolled origin_kind {!r}".format(label, origin)))

        resolved_paths: Dict[str, Path] = {}
        for field in ("provenance_record", "owning_record"):
            relative = item.get(field)
            if not isinstance(relative, str) or not relative.strip():
                continue
            path = repository_path(root, relative)
            if path is None:
                findings.append(Finding("error", "{} {} escapes repository: {!r}".format(label, field, relative)))
            elif not path.is_file():
                findings.append(Finding("error", "{} {} does not exist: {!r}".format(label, field, relative)))
            else:
                resolved_paths[field] = path

        provenance = item.get("provenance_record")
        if isinstance(origin, str) and origin in EXTERNAL_ORIGINS and isinstance(provenance, str):
            if not provenance.startswith("content/research/notes/"):
                findings.append(Finding("error", "{} external origin must use a bounded provenance record under content/research/notes/".format(label)))
            basename = Path(provenance).name
            if basename and basename not in notes_index:
                findings.append(Finding("error", "{} provenance record is not indexed in content/research/notes/README.md".format(label)))
            provenance_path = resolved_paths.get("provenance_record")
            if provenance_path is not None and isinstance(item_id, str):
                provenance_text = provenance_path.read_text(encoding="utf-8")
                if item_id not in provenance_text:
                    findings.append(Finding("error", "{} external provenance record does not reference its stable research-item ID".format(label)))

    machine_ids = set(machine_statuses)
    table_ids = set(table_rows)
    missing_from_table = sorted(machine_ids - table_ids)
    extra_in_table = sorted(table_ids - machine_ids)
    if missing_from_table:
        findings.append(Finding("error", "machine research items missing from human-readable table: {}".format(", ".join(missing_from_table))))
    if extra_in_table:
        findings.append(Finding("error", "human-readable research items missing from machine block: {}".format(", ".join(extra_in_table))))
    for item_id in sorted(machine_ids & table_ids):
        if table_rows[item_id] != machine_statuses[item_id]:
            findings.append(Finding("error", "{} research lifecycle state differs between human table ({}) and machine block ({})".format(item_id, table_rows[item_id], machine_statuses[item_id])))

    return findings


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--register", type=Path)
    parser.add_argument("--notes-index", type=Path)
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    register = args.register.resolve() if args.register else root / "content/research/research-register.md"
    notes_index = args.notes_index.resolve() if args.notes_index else root / "content/research/notes/README.md"
    findings = validate(root, register, notes_index)
    for finding in findings:
        print("::{}::{}".format(finding.severity, finding.message))
        print("{}: {}".format(finding.severity.upper(), finding.message))
    errors = [item for item in findings if item.severity == "error"]
    print("Research-register validation complete: {} error(s), {} finding(s).".format(len(errors), len(findings)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
