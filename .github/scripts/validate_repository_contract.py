#!/usr/bin/env python3
"""Validate deterministic Uncertainty Architecture repository invariants.

The validator intentionally checks observable repository structure rather than
attempting to judge architectural correctness. It is dependency-free and may
be run from any working directory.
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

DEFAULT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = DEFAULT_ROOT / ".github/policy/repository-contract.json"
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def load_contract(path: Path) -> Dict[str, object]:
    """Load and minimally validate the repository contract document."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise ValueError("Contract file does not exist: {}".format(path))
    except json.JSONDecodeError as exc:
        raise ValueError("Contract JSON is invalid: {}".format(exc))

    if data.get("contract_version") != 1:
        raise ValueError("Unsupported contract_version: {!r}".format(data.get("contract_version")))

    for key in (
        "allowed_top_level",
        "required_paths",
        "critical_files",
        "protected_markers",
    ):
        if key not in data:
            raise ValueError("Contract lacks required key: {}".format(key))

    return data


def repository_path(root: Path, relative: str) -> Optional[Path]:
    """Resolve a contract path and reject paths that escape the repository."""
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    return candidate


def markdown_link_targets(text: str) -> Set[str]:
    """Return Markdown link targets without fragments or surrounding spaces."""
    targets: Set[str] = set()
    for raw_target in LINK_PATTERN.findall(text):
        target = raw_target.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        targets.add(target.split("#", 1)[0])
    return targets


def validate_top_level(root: Path, contract: Dict[str, object], errors: List[str]) -> None:
    """Reject unexpected root files or directories."""
    allowed = contract["allowed_top_level"]
    allowed_directories = set(allowed["directories"])
    allowed_files = set(allowed["files"])

    for entry in sorted(root.iterdir(), key=lambda path: path.name):
        if entry.name == ".git":
            continue
        if entry.is_dir() and entry.name not in allowed_directories:
            errors.append("Unexpected top-level directory: {}".format(entry.name))
        elif entry.is_file() and entry.name not in allowed_files:
            errors.append("Unexpected top-level file: {}".format(entry.name))
        elif not entry.is_dir() and not entry.is_file():
            errors.append("Unexpected top-level entry type: {}".format(entry.name))


def validate_required_paths(root: Path, contract: Dict[str, object], errors: List[str]) -> None:
    """Require protected repository files and directories to exist."""
    for item in contract["required_paths"]:
        relative = item["path"]
        expected_type = item["type"]
        path = repository_path(root, relative)

        if path is None:
            errors.append("Required path escapes repository: {}".format(relative))
            continue
        if not path.exists():
            errors.append("Missing required {}: {}".format(expected_type, relative))
            continue
        if expected_type == "file" and not path.is_file():
            errors.append("Required file is not a file: {}".format(relative))
        elif expected_type == "directory" and not path.is_dir():
            errors.append("Required directory is not a directory: {}".format(relative))
        elif expected_type not in ("file", "directory"):
            errors.append("Unsupported required path type {!r}: {}".format(expected_type, relative))


def validate_critical_files(root: Path, contract: Dict[str, object], errors: List[str]) -> None:
    """Protect stable document functions without freezing complete prose."""
    for rule in contract["critical_files"]:
        relative = rule["path"]
        path = repository_path(root, relative)
        if path is None:
            errors.append("Critical path escapes repository: {}".format(relative))
            continue
        if not path.is_file():
            errors.append("Missing critical file: {}".format(relative))
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append("Critical file is not valid UTF-8: {}".format(relative))
            continue

        lines = {line.rstrip() for line in text.splitlines()}
        for heading in rule.get("required_headings", []):
            if heading not in lines:
                errors.append("{}: missing required heading {!r}".format(relative, heading))

        for marker in rule.get("required_text", []):
            if marker not in text:
                errors.append("{}: missing protected text {!r}".format(relative, marker))

        targets = markdown_link_targets(text)
        for target in rule.get("required_links", []):
            if target not in targets:
                errors.append("{}: missing required Markdown link to {}".format(relative, target))


def validate_protected_markers(root: Path, contract: Dict[str, object], errors: List[str]) -> None:
    """Protect explicit compatibility and provenance markers."""
    for rule in contract["protected_markers"]:
        relative = rule["path"]
        path = repository_path(root, relative)
        if path is None:
            errors.append("Protected marker path escapes repository: {}".format(relative))
            continue
        if not path.is_file():
            errors.append("Missing protected-marker file: {}".format(relative))
            continue
        text = path.read_text(encoding="utf-8")
        if rule["text"] not in text:
            errors.append(
                "{}: missing protected marker {!r} ({})".format(
                    relative,
                    rule["text"],
                    rule.get("purpose", "no purpose recorded"),
                )
            )


def validate(root: Path, contract_path: Path) -> List[str]:
    """Return all repository-contract violations."""
    root = root.resolve()
    contract = load_contract(contract_path.resolve())
    errors: List[str] = []

    if not root.is_dir():
        return ["Repository root does not exist or is not a directory: {}".format(root)]

    validate_top_level(root, contract, errors)
    validate_required_paths(root, contract, errors)
    validate_critical_files(root, contract, errors)
    validate_protected_markers(root, contract, errors)
    return sorted(set(errors))


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="Repository root. Defaults to the root containing this script.",
    )
    parser.add_argument(
        "--contract",
        type=Path,
        default=DEFAULT_CONTRACT,
        help="Path to repository-contract.json.",
    )
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        errors = validate(args.root, args.contract)
    except ValueError as exc:
        print("Repository contract configuration error: {}".format(exc))
        return 2

    if errors:
        print("Repository contract validation failed:")
        for error in errors:
            print("- {}".format(error))
        return 1

    print("Repository contract valid: critical paths, sections, links, markers, and top-level namespace are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
