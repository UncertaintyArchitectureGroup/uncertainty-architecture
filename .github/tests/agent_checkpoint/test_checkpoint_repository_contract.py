#!/usr/bin/env python3
"""Mutation fixtures for repository-contract protection of the agent checkpoint surface."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_repository_contract.py"
EXTENSION_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract-agent-checkpoint.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_repository_contract", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load repository-contract validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_extension():
    return json.loads(EXTENSION_PATH.read_text(encoding="utf-8"))


def validate_surface(validator, root: Path, extension) -> List[str]:
    errors: List[str] = []
    validator.validate_required_paths(root, extension, errors)
    validator.validate_critical_files(root, extension, errors)
    return errors


def materialize_surface(root: Path, extension) -> None:
    for item in extension["required_paths"]:
        relative = item["path"]
        source = REPOSITORY_ROOT / relative
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_dir():
            shutil.copytree(source, target, dirs_exist_ok=True)
        else:
            shutil.copy2(source, target)


def assert_workflow_mutation_blocked(
    validator, extension, marker: str, replacement: str,
    label: str, failures: List[str],
) -> None:
    with tempfile.TemporaryDirectory(prefix="ua-checkpoint-contract-") as temp:
        root = Path(temp)
        materialize_surface(root, extension)
        workflow = root / ".github/workflows/change-coupling.yml"
        original = workflow.read_text(encoding="utf-8")
        if marker not in original:
            failures.append("{}: fixture could not find protected marker {!r}".format(label, marker))
            return
        workflow.write_text(original.replace(marker, replacement, 1), encoding="utf-8")
        errors = validate_surface(validator, root, extension)
        if not any("missing protected text" in error and marker in error for error in errors):
            failures.append("{}: mutation did not trigger repository-contract failure: {}".format(label, errors))
        else:
            print("PASS: {}".format(label))


def main() -> int:
    validator = load_validator()
    extension = load_extension()
    failures: List[str] = []

    baseline_errors = validate_surface(validator, REPOSITORY_ROOT, extension)
    if baseline_errors:
        failures.append("baseline checkpoint control surface is invalid: {}".format(baseline_errors))
    else:
        print("PASS: checkpoint control surface satisfies repository contract")

    assert_workflow_mutation_blocked(
        validator, extension,
        "name: Agent protocol / checked-state checkpoint",
        "name: Agent protocol / removed-checkpoint-fixture",
        "removing checkpoint job marker is blocked by repository contract",
        failures,
    )
    assert_workflow_mutation_blocked(
        validator, extension,
        "pull_request_review_comment:",
        "pull_request_review_comment_removed:",
        "removing GitHub review-comment feedback trigger is blocked",
        failures,
    )
    assert_workflow_mutation_blocked(
        validator, extension,
        "github.event.review.author_association",
        "github.event.review.untrusted_association",
        "removing trusted-review author boundary is blocked",
        failures,
    )

    workflow_text = (REPOSITORY_ROOT / ".github/workflows/change-coupling.yml").read_text(encoding="utf-8")
    if "issue_comment:" not in workflow_text:
        print("PASS: top-level issue comments do not masquerade as PR-head checkpoint events")
    else:
        failures.append("issue_comment trigger must remain outside the deterministic PR-head checkpoint workflow")

    if "issues: read" not in workflow_text:
        print("PASS: checkpoint workflow does not request unused Issues permission")
    else:
        failures.append("checkpoint workflow retains unnecessary Issues permission")

    if failures:
        print("Agent-checkpoint repository-contract fixture failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Agent-checkpoint repository-contract fixture passed: 6 assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
