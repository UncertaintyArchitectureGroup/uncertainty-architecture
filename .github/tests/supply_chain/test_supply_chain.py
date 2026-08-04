#!/usr/bin/env python3
"""Regression tests for workflow action and container pinning policy."""

import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_workflow_supply_chain.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/supply-chain-contract.json"
CASES_PATH = Path(__file__).with_name("cases.json")

REQUIRED_CASE_NAMES: Set[str] = {
    "full action SHA with version comment passes",
    "local action reference passes",
    "action tag is rejected",
    "short action SHA is rejected",
    "missing action version comment is rejected",
    "container digest passes",
    "container tag is rejected",
    "docker action image tag is rejected",
}


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_workflow_supply_chain", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load supply-chain validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def validate_manifest(cases: List[Dict[str, object]]) -> List[str]:
    names = [str(case.get("name", "")) for case in cases]
    errors: List[str] = []
    missing = sorted(REQUIRED_CASE_NAMES - set(names))
    if missing:
        errors.append("missing required cases: {}".format(", ".join(missing)))
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append("duplicate case names: {}".format(", ".join(duplicates)))
    return errors


def main() -> int:
    validator = load_validator()
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    failures = validate_manifest(cases)

    for case in cases:
        with tempfile.TemporaryDirectory(prefix="ua-supply-chain-") as temporary:
            root = Path(temporary)
            workflow = root / ".github/workflows/fixture.yml"
            workflow.parent.mkdir(parents=True, exist_ok=True)
            workflow.write_text(str(case["workflow"]), encoding="utf-8")
            errors = validator.validate(root, CONTRACT_PATH)

        if case.get("expected_valid"):
            if errors:
                failures.append("{}: expected success, got {}".format(case["name"], errors))
            else:
                print("PASS: {}".format(case["name"]))
            continue

        expected = str(case["expected_error"])
        if not any(expected in error for error in errors):
            failures.append("{}: expected error containing {!r}, got {}".format(case["name"], expected, errors))
        else:
            print("PASS: {}".format(case["name"]))

    if failures:
        print("Supply-chain self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print("Supply-chain self-tests passed: {} regression fixtures.".format(len(cases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
