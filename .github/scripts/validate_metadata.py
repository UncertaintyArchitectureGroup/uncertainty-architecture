#!/usr/bin/env python3
"""Validate UA frontmatter, controlled metadata, canonical ownership, and terms.

The validator implements the bounded metadata contract in
.github/policy/metadata-contract.json. It uses only the Python standard library,
works from any current directory, reports all errors in one pass, and keeps
terminology findings non-blocking unless --warnings-as-errors is requested.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple, Union

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/metadata-contract.json"
HEADING_PATTERN = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
TAG_PATTERN = re.compile(r"^ua/(module|type|status|topic)/[a-z0-9]+(?:-[a-z0-9]+)*$")
KEBAB_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

Scalar = Union[str, bool, int, float, None]
MetadataValue = Union[Scalar, List[Scalar]]


class Finding:
    """One deterministic validator result."""

    def __init__(self, severity: str, path: str, message: str, line: int = 1) -> None:
        self.severity = severity
        self.path = path
        self.message = message
        self.line = line

    def key(self) -> Tuple[str, str, int, str]:
        return (self.severity, self.path, self.line, self.message)


def load_contract(path: Path) -> Dict[str, object]:
    try:
        contract = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError("Metadata contract does not exist: {}".format(path))
    except json.JSONDecodeError as exc:
        raise ValueError("Metadata contract JSON is invalid: {}".format(exc))

    if contract.get("contract_version") != 1:
        raise ValueError(
            "Unsupported metadata contract_version: {!r}".format(
                contract.get("contract_version")
            )
        )

    required_keys = (
        "required_fields",
        "optional_fields",
        "list_fields",
        "controlled_values",
        "required_frontmatter_paths",
        "frontmatter_scan_roots",
        "frontmatter_scan_files",
        "frontmatter_exclude_prefixes",
        "tag_projection",
        "canonical_ownership",
        "glossary",
        "terminology_warnings",
    )
    for key in required_keys:
        if key not in contract:
            raise ValueError("Metadata contract lacks required key: {}".format(key))

    return contract


def repository_path(root: Path, relative: str) -> Optional[Path]:
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        return None
    return candidate


def relative_path(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def unquote(value: str) -> Scalar:
    value = value.strip()
    if value == "":
        return ""
    if value == "[]":
        return []
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in ("null", "none", "~"):
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return value[1:-1]
    if re.match(r"^-?\d+$", value):
        try:
            return int(value)
        except ValueError:
            pass
    if re.match(r"^-?\d+\.\d+$", value):
        try:
            return float(value)
        except ValueError:
            pass
    return value


def extract_frontmatter(text: str) -> Tuple[Optional[List[str]], int, Optional[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, 0, None

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[1:index], index + 2, None

    return None, 0, "frontmatter starts with '---' but has no closing delimiter"


def parse_frontmatter(lines: Sequence[str]) -> Tuple[Dict[str, MetadataValue], List[str]]:
    metadata: Dict[str, MetadataValue] = {}
    errors: List[str] = []
    current_key: Optional[str] = None

    for number, raw_line in enumerate(lines, start=2):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith("  - ") or raw_line.startswith("- "):
            if current_key is None:
                errors.append("line {}: list item has no owning field".format(number))
                continue
            current = metadata.get(current_key)
            if not isinstance(current, list):
                errors.append(
                    "line {}: field {!r} mixes scalar and list values".format(
                        number, current_key
                    )
                )
                continue
            current.append(unquote(raw_line.split("- ", 1)[1]))
            continue

        if raw_line[:1].isspace():
            errors.append(
                "line {}: unsupported indented frontmatter syntax; use top-level scalars or two-space list items".format(
                    number
                )
            )
            continue

        if ":" not in raw_line:
            errors.append("line {}: malformed top-level field".format(number))
            current_key = None
            continue

        key, raw_value = raw_line.split(":", 1)
        key = key.strip()
        if not key:
            errors.append("line {}: empty field name".format(number))
            current_key = None
            continue
        if key in metadata:
            errors.append("line {}: duplicate field {!r}".format(number, key))
            current_key = key
            continue

        value = unquote(raw_value)
        metadata[key] = [] if value == "" else value
        current_key = key

    return metadata, errors


def is_excluded(relative: str, contract: Dict[str, object]) -> bool:
    return any(
        relative.startswith(str(prefix))
        for prefix in contract["frontmatter_exclude_prefixes"]
    )


def discover_documents(root: Path, contract: Dict[str, object]) -> List[Path]:
    discovered: Set[Path] = set()

    for relative in contract["frontmatter_scan_files"]:
        path = repository_path(root, str(relative))
        if path is not None and path.is_file():
            discovered.add(path)

    for relative in contract["frontmatter_scan_roots"]:
        path = repository_path(root, str(relative))
        if path is None or not path.is_dir():
            continue
        discovered.update(item for item in path.rglob("*.md") if item.is_file())

    for relative in contract["required_frontmatter_paths"]:
        path = repository_path(root, str(relative))
        if path is not None and path.is_file():
            discovered.add(path)

    return sorted(
        (
            item
            for item in discovered
            if not is_excluded(relative_path(root, item), contract)
        ),
        key=lambda item: relative_path(root, item),
    )


def first_h1(text: str) -> Optional[str]:
    match = HEADING_PATTERN.search(text)
    return match.group(1).strip() if match else None


def normalized_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def as_string_list(value: MetadataValue) -> Optional[List[str]]:
    if not isinstance(value, list):
        return None
    if any(not isinstance(item, str) for item in value):
        return None
    return [str(item) for item in value]


def validate_document_metadata(
    root: Path,
    path: Path,
    text: str,
    metadata: Dict[str, MetadataValue],
    contract: Dict[str, object],
) -> List[Finding]:
    relative = relative_path(root, path)
    findings: List[Finding] = []
    required_fields = set(str(item) for item in contract["required_fields"])
    optional_fields = set(str(item) for item in contract["optional_fields"])
    allowed_fields = required_fields | optional_fields
    list_fields = set(str(item) for item in contract["list_fields"])

    for field in sorted(set(metadata) - allowed_fields):
        findings.append(Finding("error", relative, "unknown frontmatter field {!r}".format(field)))

    for field in sorted(required_fields - set(metadata)):
        findings.append(Finding("error", relative, "missing required field {!r}".format(field)))

    for field in sorted(list_fields):
        if field in metadata and not isinstance(metadata[field], list):
            findings.append(Finding("error", relative, "field {!r} must be a YAML list".format(field)))

    title = metadata.get("title")
    if "title" in metadata and (not isinstance(title, str) or not title.strip()):
        findings.append(Finding("error", relative, "title must be a non-empty scalar"))
    elif isinstance(title, str):
        heading = first_h1(text)
        if heading is None:
            findings.append(Finding("warning", relative, "document has metadata title but no H1 heading"))
        elif normalized_title(title) != normalized_title(heading):
            findings.append(
                Finding(
                    "warning",
                    relative,
                    "metadata title {!r} does not closely match H1 {!r}".format(title, heading),
                )
            )

    controlled = contract["controlled_values"]
    for field in ("artifact_type", "status", "maturity", "module"):
        if field not in metadata:
            continue
        value = metadata[field]
        allowed = set(str(item) for item in controlled[field])
        if not isinstance(value, str):
            findings.append(Finding("error", relative, "field {!r} must be a scalar".format(field)))
        elif value not in allowed:
            findings.append(
                Finding(
                    "error",
                    relative,
                    "field {!r} uses uncontrolled value {!r}".format(field, value),
                )
            )

    topics = as_string_list(metadata.get("topics", []))
    if topics is None:
        findings.append(Finding("error", relative, "topics must contain only string values"))
        topics = []
    elif not topics:
        findings.append(Finding("error", relative, "topics must contain at least one controlled topic"))
    else:
        allowed_topics = set(str(item) for item in controlled["topics"])
        for topic in topics:
            if topic not in allowed_topics:
                findings.append(
                    Finding("error", relative, "topics contains uncontrolled value {!r}".format(topic))
                )
        for duplicate in sorted({item for item in topics if topics.count(item) > 1}):
            findings.append(Finding("error", relative, "topics contains duplicate {!r}".format(duplicate)))

    tags = as_string_list(metadata.get("tags", []))
    if tags is None:
        findings.append(Finding("error", relative, "tags must contain only string values"))
        tags = []
    else:
        projection = contract["tag_projection"]
        minimum = int(projection["minimum_tags"])
        recommended_maximum = int(projection["recommended_maximum_tags"])
        if len(tags) < minimum:
            findings.append(
                Finding(
                    "error",
                    relative,
                    "tags must contain at least {} values, found {}".format(minimum, len(tags)),
                )
            )
        elif len(tags) > recommended_maximum:
            findings.append(
                Finding(
                    "warning",
                    relative,
                    "tags normally contain at most {} values, found {}".format(
                        recommended_maximum, len(tags)
                    ),
                )
            )

        for duplicate in sorted({item for item in tags if tags.count(item) > 1}):
            findings.append(Finding("error", relative, "tags contains duplicate {!r}".format(duplicate)))
        for tag in tags:
            if not TAG_PATTERN.match(tag):
                findings.append(Finding("error", relative, "invalid controlled tag {!r}".format(tag)))

        substitutions = {
            "module": metadata.get("module"),
            "artifact_type": metadata.get("artifact_type"),
            "status": metadata.get("status"),
        }
        if all(isinstance(value, str) for value in substitutions.values()):
            expected = {
                template.format(**substitutions)
                for template in projection["required_exact"]
            }
            for missing in sorted(expected - set(tags)):
                findings.append(Finding("error", relative, "missing projected tag {!r}".format(missing)))

            structural_prefixes = ("ua/module/", "ua/type/", "ua/status/")
            for tag in tags:
                if tag.startswith(structural_prefixes) and tag not in expected:
                    findings.append(
                        Finding("error", relative, "tag {!r} contradicts structured fields".format(tag))
                    )

        topic_prefix = str(projection["topic_prefix"])
        topic_set = set(topics)
        for tag in tags:
            if tag.startswith(topic_prefix):
                projected_topic = tag[len(topic_prefix) :]
                if projected_topic not in topic_set:
                    findings.append(
                        Finding(
                            "error",
                            relative,
                            "topic tag {!r} is not present in topics".format(tag),
                        )
                    )

    canonical_values = as_string_list(metadata.get("canonical_for", []))
    if canonical_values is None:
        findings.append(Finding("error", relative, "canonical_for must contain only string values"))
    else:
        for value in canonical_values:
            if not KEBAB_PATTERN.match(value):
                findings.append(
                    Finding("error", relative, "canonical_for contains invalid value {!r}".format(value))
                )
        for duplicate in sorted(
            {item for item in canonical_values if canonical_values.count(item) > 1}
        ):
            findings.append(
                Finding("error", relative, "canonical_for contains duplicate {!r}".format(duplicate))
            )

    return findings


def collect_metadata(
    root: Path,
    contract: Dict[str, object],
    validate_fields: bool,
) -> Tuple[Dict[str, Dict[str, MetadataValue]], List[Finding]]:
    records: Dict[str, Dict[str, MetadataValue]] = {}
    findings: List[Finding] = []
    required = set(str(item) for item in contract["required_frontmatter_paths"])

    for relative in sorted(required):
        path = repository_path(root, relative)
        if path is None:
            findings.append(Finding("error", relative, "required metadata path escapes repository"))
        elif not path.is_file():
            findings.append(Finding("error", relative, "required metadata document is missing"))

    for path in discover_documents(root, contract):
        relative = relative_path(root, path)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(Finding("error", relative, "document is not valid UTF-8"))
            continue

        lines, _, delimiter_error = extract_frontmatter(text)
        if delimiter_error:
            findings.append(Finding("error", relative, delimiter_error))
            continue
        if lines is None:
            if relative in required:
                findings.append(Finding("error", relative, "required document has no YAML frontmatter"))
            continue

        metadata, parse_errors = parse_frontmatter(lines)
        for message in parse_errors:
            findings.append(Finding("error", relative, message))
        records[relative] = metadata
        if validate_fields:
            findings.extend(validate_document_metadata(root, path, text, metadata, contract))

    return records, findings


def validate_canonical_ownership(
    records: Dict[str, Dict[str, MetadataValue]], contract: Dict[str, object]
) -> List[Finding]:
    findings: List[Finding] = []
    inactive = set(str(item) for item in contract["canonical_ownership"]["inactive_maturities"])
    allowed_duplicates = set(
        str(item) for item in contract["canonical_ownership"]["allow_duplicate_values"]
    )
    claims: Dict[str, List[str]] = {}

    for path, metadata in records.items():
        maturity = metadata.get("maturity")
        if isinstance(maturity, str) and maturity in inactive:
            continue
        values = as_string_list(metadata.get("canonical_for", [])) or []
        for value in values:
            claims.setdefault(value, []).append(path)

    for value, owners in sorted(claims.items()):
        if value in allowed_duplicates or len(owners) <= 1:
            continue
        findings.append(
            Finding(
                "error",
                owners[0],
                "active canonical_for {!r} has multiple owners: {}".format(
                    value, ", ".join(sorted(owners))
                ),
            )
        )

    return findings


def validate_glossary(root: Path, contract: Dict[str, object]) -> List[Finding]:
    glossary = contract["glossary"]
    relative = str(glossary["path"])
    path = repository_path(root, relative)
    if path is None or not path.is_file():
        return [Finding("error", relative, "protected glossary document is missing")]

    text = path.read_text(encoding="utf-8")
    headings = [
        line[4:].strip()
        for line in text.splitlines()
        if line.startswith("### ") and line[4:].strip()
    ]
    findings: List[Finding] = []

    for entry in glossary["protected_entries"]:
        count = headings.count(str(entry))
        if count == 0:
            findings.append(
                Finding("error", relative, "protected glossary entry {!r} is missing".format(entry))
            )
        elif count > 1:
            findings.append(
                Finding(
                    "error",
                    relative,
                    "protected glossary entry {!r} appears {} times".format(entry, count),
                )
            )

    return findings


def expand_scan_path(root: Path, relative: str) -> List[Path]:
    path = repository_path(root, relative)
    if path is None:
        return []
    if path.is_file() and path.suffix.lower() == ".md":
        return [path]
    if path.is_dir():
        return sorted(item for item in path.rglob("*.md") if item.is_file())
    return []


def terminology_findings(root: Path, contract: Dict[str, object]) -> List[Finding]:
    findings: List[Finding] = []

    for rule in contract["terminology_warnings"]:
        allowed = set(str(item) for item in rule["allow_paths"])
        files: Set[Path] = set()
        for scan_path in rule["scan_paths"]:
            files.update(expand_scan_path(root, str(scan_path)))

        for path in sorted(files, key=lambda item: relative_path(root, item)):
            relative = relative_path(root, path)
            if relative in allowed:
                continue
            text = path.read_text(encoding="utf-8")
            for line_number, line in enumerate(text.splitlines(), start=1):
                for pattern in rule["patterns"]:
                    if str(pattern) in line:
                        findings.append(
                            Finding(
                                "warning",
                                relative,
                                "{} [{}]".format(rule["message"], rule["id"]),
                                line_number,
                            )
                        )
                        break

    return findings


def validate(root: Path, contract_path: Path, mode: str = "all") -> List[Finding]:
    root = root.resolve()
    contract = load_contract(contract_path.resolve())
    findings: List[Finding] = []

    if not root.is_dir():
        return [Finding("error", str(root), "repository root is not a directory")]

    records: Dict[str, Dict[str, MetadataValue]] = {}
    if mode in ("all", "metadata"):
        records, metadata_findings = collect_metadata(root, contract, True)
        findings.extend(metadata_findings)
    elif mode == "canonical":
        records, collection_findings = collect_metadata(root, contract, False)
        findings.extend(collection_findings)

    if mode in ("all", "canonical"):
        findings.extend(validate_canonical_ownership(records, contract))

    if mode in ("all", "terminology"):
        findings.extend(validate_glossary(root, contract))
        findings.extend(terminology_findings(root, contract))

    unique = {finding.key(): finding for finding in findings}
    return [unique[key] for key in sorted(unique)]


def emit(finding: Finding) -> None:
    message = finding.message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    path = finding.path.replace("%", "%25").replace(",", "%2C")
    print("::{} file={},line={}::{}".format(finding.severity, path, finding.line, message))
    print("{}: {}:{}: {}".format(finding.severity.upper(), finding.path, finding.line, finding.message))


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument(
        "--mode",
        choices=("all", "metadata", "canonical", "terminology"),
        default="all",
    )
    parser.add_argument("--warnings-as-errors", action="store_true")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        findings = validate(args.root, args.contract, args.mode)
    except ValueError as exc:
        print("Metadata contract configuration error: {}".format(exc))
        return 2

    for finding in findings:
        emit(finding)

    errors = [item for item in findings if item.severity == "error"]
    warnings = [item for item in findings if item.severity == "warning"]
    print(
        "Metadata validation complete: {} error(s), {} warning(s), mode={}.".format(
            len(errors), len(warnings), args.mode
        )
    )

    if errors or (warnings and args.warnings_as_errors):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())