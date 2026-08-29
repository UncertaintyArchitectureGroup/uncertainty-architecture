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


def load_validator(path: Path = VALIDATOR_PATH):
    spec = importlib.util.spec_from_file_location("validate_repository_contract", path)
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


def assert_file_mutation_blocked(
    validator, extension, relative_path: str, marker: str, replacement: str,
    label: str, failures: List[str],
) -> None:
    with tempfile.TemporaryDirectory(prefix="ua-checkpoint-contract-") as temp:
        root = Path(temp)
        materialize_surface(root, extension)
        target = root / relative_path
        original = target.read_text(encoding="utf-8")
        if marker not in original:
            failures.append("{}: fixture could not find protected marker {!r}".format(label, marker))
            return
        target.write_text(original.replace(marker, replacement, 1), encoding="utf-8")
        errors = validate_surface(validator, root, extension)
        if not errors:
            failures.append("{}: mutation did not trigger repository-contract failure".format(label))
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

    if any(path.name == "repository-contract-agent-checkpoint.json" for path in validator.DEFAULT_EXTENSIONS):
        print("PASS: repository validator registers the agent-checkpoint extension")
    else:
        failures.append("repository validator does not register the agent-checkpoint extension")

    assert_file_mutation_blocked(
        validator, extension,
        ".github/workflows/change-coupling.yml",
        "name: Agent protocol / checked-state checkpoint",
        "name: Agent protocol / removed-checkpoint-fixture",
        "removing checkpoint job marker is blocked by repository contract",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/workflows/change-coupling.yml",
        "name: Agent protocol / readiness authorization",
        "name: Agent protocol / removed-readiness-fixture",
        "removing durable readiness-authorization job is blocked",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/workflows/change-coupling.yml",
        "github.event.review.author_association",
        "github.event.review.untrusted_association",
        "removing trusted-review author boundary is blocked",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/workflows/agent-policy-guard.yml",
        "pull_request_target:",
        "pull_request:",
        "replacing trusted-base trigger with candidate-controlled PR trigger is blocked",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/workflows/agent-policy-guard.yml",
        "statuses: write",
        "statuses: read",
        "removing trusted head-status write capability is blocked",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/scripts/validate_agent_policy_guard.py",
        "reviewed_base_tip_sha",
        "removed_base_tip_guard",
        "removing base-advance checkpoint invalidation is blocked",
        failures,
    )
    assert_file_mutation_blocked(
        validator, extension,
        ".github/scripts/validate_repository_contract.py",
        "repository-contract-agent-checkpoint.json",
        "repository-contract-agent-checkpoint.removed.json",
        "removing checkpoint-extension registration is blocked by independent mutation assertion",
        failures,
    )

    workflow_text = (REPOSITORY_ROOT / ".github/workflows/change-coupling.yml").read_text(encoding="utf-8")
    if "issue_comment:" not in workflow_text:
        print("PASS: top-level issue comments do not masquerade as PR-head checkpoint events")
    else:
        failures.append("issue_comment trigger must remain outside the deterministic PR-head checkpoint workflow")

    if "issues: read" in workflow_text and "checks: read" in workflow_text:
        print("PASS: candidate workflow requests only read surfaces for CODEOWNER approval and readiness evidence")
    else:
        failures.append("candidate workflow lacks required read permissions for authorization comments or readiness checks")

    guard_text = (REPOSITORY_ROOT / ".github/workflows/agent-policy-guard.yml").read_text(encoding="utf-8")
    if "pull_request_target:" in guard_text and "github.event.repository.default_branch" in guard_text:
        print("PASS: trusted-base guard executes target-branch code rather than candidate checkout")
    else:
        failures.append("trusted-base guard lost its target-branch execution boundary")

    if failures:
        print("Agent-checkpoint repository-contract fixture failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Agent-checkpoint repository-contract fixture passed: 12 assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
