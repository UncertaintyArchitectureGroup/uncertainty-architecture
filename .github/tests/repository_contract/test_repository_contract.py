#!/usr/bin/env python3
"""Regression tests for the machine-readable repository contract."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_repository_contract.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract.json"
CASES_PATH = Path(__file__).with_name("cases.json")


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_repository_contract", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load repository contract validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, text: str = "fixture\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def materialize_valid_repository(root: Path, contract: Dict[str, object]) -> None:
    """Build a minimal synthetic repository satisfying the current contract."""
    allowed = contract["allowed_top_level"]

    for directory in allowed["directories"]:
        (root / directory).mkdir(parents=True, exist_ok=True)
    for filename in allowed["files"]:
        write_text(root / filename)

    for required in contract["required_paths"]:
        path = root / required["path"]
        if required["type"] == "directory":
            path.mkdir(parents=True, exist_ok=True)
        else:
            write_text(path)

    for rule in contract["critical_files"]:
        parts: List[str] = []
        parts.extend(rule.get("required_headings", []))
        parts.extend(rule.get("required_text", []))
        parts.extend("[fixture]({})".format(target) for target in rule.get("required_links", []))
        write_text(root / rule["path"], "\n\n".join(parts) + "\n")

    for marker in contract["protected_markers"]:
        path = root / marker["path"]
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        write_text(path, existing + marker["text"] + "\n")


def apply_mutation(root: Path, mutation: Dict[str, str]) -> None:
    mutation_type = mutation["type"]
    if mutation_type == "none":
        return

    path = root / mutation["path"]
    if mutation_type == "delete_path":
        if path.is_dir():
            shutil.rmtree(str(path))
        elif path.exists():
            path.unlink()
        return
    if mutation_type == "remove_text":
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(mutation["text"], "", 1), encoding="utf-8")
        return
    if mutation_type == "add_directory":
        path.mkdir(parents=True, exist_ok=True)
        return
    if mutation_type == "add_file":
        write_text(path)
        return

    raise ValueError("Unsupported fixture mutation: {}".format(mutation_type))


def main() -> int:
    validator = load_validator()
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    failures: List[str] = []

    for case in cases:
        with tempfile.TemporaryDirectory(prefix="ua-contract-") as temporary:
            root = Path(temporary)
            materialize_valid_repository(root, contract)
            apply_mutation(root, case["mutation"])
            errors = validator.validate(root, CONTRACT_PATH)

        if case.get("expected_valid"):
            if errors:
                failures.append("{}: expected success, got {}".format(case["name"], errors))
            else:
                print("PASS: {}".format(case["name"]))
            continue

        expected = case["expected_error"]
        if not any(expected in error for error in errors):
            failures.append(
                "{}: expected error containing {!r}, got {}".format(
                    case["name"], expected, errors
                )
            )
        else:
            print("PASS: {}".format(case["name"]))

    if failures:
        print("Repository contract self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print("Repository contract self-tests passed: {} regression fixtures.".format(len(cases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
