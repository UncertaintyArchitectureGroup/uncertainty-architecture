#!/usr/bin/env python3
"""Mutation-based regression tests for UA metadata validation."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_metadata.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/metadata-contract.json"
CASES_PATH = Path(__file__).with_name("cases.json")

REQUIRED_CASE_NAMES: Set[str] = {
    "valid synthetic metadata repository passes",
    "required frontmatter deletion is rejected",
    "uncontrolled artifact type is rejected",
    "uncontrolled status is rejected",
    "uncontrolled maturity is rejected",
    "uncontrolled module is rejected",
    "uncontrolled topic is rejected",
    "missing structural tag is rejected",
    "contradictory structural tag is rejected",
    "topic projection contradiction is rejected",
    "duplicate active canonical owner is rejected",
    "superseded canonical claim does not conflict",
    "protected glossary entry deletion is rejected",
    "duplicate protected glossary entry is rejected",
    "historical category usage produces warning",
    "runtime reauthorization label produces warning",
    "duplicate frontmatter field is rejected",
    "unclosed frontmatter is rejected",
}


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_metadata", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load metadata validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def title_for(path: str) -> str:
    name = Path(path).stem
    if name.lower() == "readme":
        name = Path(path).parent.name or "Repository"
    return name.replace("-", " ").replace("_", " ").title()


def valid_document(path: str) -> str:
    title = title_for(path)
    return """---
title: {title}
artifact_type: doctrine
status: informative
maturity: active
module: doctrine
topics:
  - control-loop
tags:
  - ua/module/doctrine
  - ua/type/doctrine
  - ua/status/informative
  - ua/topic/control-loop
---

# {title}

Fixture document.
""".format(title=title)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def materialize_valid_repository(root: Path, contract: Dict[str, object]) -> None:
    paths: Set[str] = set(str(item) for item in contract["required_frontmatter_paths"])
    paths.update(str(item) for item in contract["frontmatter_scan_files"])

    for relative in paths:
        write_text(root / relative, valid_document(relative))

    for scan_root in contract["frontmatter_scan_roots"]:
        (root / str(scan_root)).mkdir(parents=True, exist_ok=True)

    glossary = contract["glossary"]
    glossary_path = str(glossary["path"])
    glossary_text = valid_document(glossary_path)
    glossary_text += "\n".join(
        "### {}\n\nProtected fixture definition.\n".format(entry)
        for entry in glossary["protected_entries"]
    )
    write_text(root / glossary_path, glossary_text)


def replace_once(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError("Fixture source text not found in {}: {!r}".format(path, old))
    path.write_text(text.replace(old, new, 1), encoding="utf-8")


def apply_mutation(root: Path, mutation: Dict[str, str]) -> None:
    path = root / mutation["path"]
    mutation_type = mutation["type"]

    if mutation_type == "replace":
        replace_once(path, mutation["old"], mutation["new"])
        return
    if mutation_type == "append":
        with path.open("a", encoding="utf-8") as handle:
            handle.write(mutation["text"])
        return
    if mutation_type == "remove_frontmatter":
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        closing = lines.index("---", 1)
        path.write_text("\n".join(lines[closing + 1 :]).lstrip() + "\n", encoding="utf-8")
        return
    if mutation_type == "remove_closing_frontmatter":
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        closing = lines.index("---", 1)
        del lines[closing]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return
    if mutation_type == "insert_frontmatter":
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        closing = lines.index("---", 1)
        insertion = mutation["text"].rstrip("\n").splitlines()
        lines[closing:closing] = insertion
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    raise ValueError("Unsupported metadata fixture mutation: {}".format(mutation_type))


def validate_case_manifest(cases: List[Dict[str, object]]) -> List[str]:
    names = [str(case.get("name", "")) for case in cases]
    errors: List[str] = []

    missing = sorted(REQUIRED_CASE_NAMES - set(names))
    if missing:
        errors.append("missing required cases: {}".format(", ".join(missing)))

    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append("duplicate case names: {}".format(", ".join(duplicates)))

    unnamed = [str(index) for index, name in enumerate(names, start=1) if not name]
    if unnamed:
        errors.append("unnamed cases at positions: {}".format(", ".join(unnamed)))

    return errors


def main() -> int:
    validator = load_validator()
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    failures = validate_case_manifest(cases)

    for case in cases:
        with tempfile.TemporaryDirectory(prefix="ua-metadata-") as temporary:
            root = Path(temporary)
            materialize_valid_repository(root, contract)
            for mutation in case.get("mutations", []):
                apply_mutation(root, mutation)
            findings = validator.validate(root, CONTRACT_PATH, str(case["mode"]))

        if case.get("expected_valid"):
            blocking = [item for item in findings if item.severity == "error"]
            if blocking:
                failures.append(
                    "{}: expected no errors, got {}".format(
                        case["name"], [item.message for item in blocking]
                    )
                )
            else:
                print("PASS: {}".format(case["name"]))
            continue

        severity = str(case["expected_severity"])
        message = str(case["expected_message"])
        if not any(
            item.severity == severity and message in item.message for item in findings
        ):
            failures.append(
                "{}: expected {} containing {!r}, got {}".format(
                    case["name"],
                    severity,
                    message,
                    [(item.severity, item.message) for item in findings],
                )
            )
        else:
            print("PASS: {}".format(case["name"]))

    if failures:
        print("Metadata contract self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print("Metadata contract self-tests passed: {} regression fixtures.".format(len(cases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
