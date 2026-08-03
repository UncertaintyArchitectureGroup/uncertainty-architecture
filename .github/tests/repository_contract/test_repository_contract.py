#!/usr/bin/env python3
"""Regression tests for the machine-readable repository contract."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_repository_contract.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract.json"
CASES_PATH = Path(__file__).with_name("cases.json")

REQUIRED_CASE_NAMES: Set[str] = {
    "valid synthetic repository passes",
    "critical file deletion is rejected",
    "critical README section deletion is rejected",
    "protected attribution text deletion is rejected",
    "required canonical link deletion is rejected",
    "unexpected top-level directory is rejected",
    "unexpected top-level file is rejected",
    "legacy runtime anchor deletion is rejected",
    "compatibility path deletion is rejected",
    "immutable documentation license modification is rejected",
    "CODEOWNERS default ownership deletion is rejected",
    "PR contract marker deletion is rejected",
    "CITATION author deletion is rejected",
    "link-integrity citation step deletion is rejected",
    "navigation routing declaration deletion is rejected",
}


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

    for immutable in contract["immutable_files"]:
        source = REPOSITORY_ROOT / immutable["path"]
        destination = root / immutable["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(str(source), str(destination))

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
    if mutation_type == "append_text":
        with path.open("a", encoding="utf-8") as handle:
            handle.write(mutation["text"])
        return
    if mutation_type == "add_directory":
        path.mkdir(parents=True, exist_ok=True)
        return
    if mutation_type == "add_file":
        write_text(path)
        return

    raise ValueError("Unsupported fixture mutation: {}".format(mutation_type))


def validate_case_manifest(cases: List[Dict[str, object]]) -> List[str]:
    """Ensure the regression suite itself cannot silently lose required cases."""
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
