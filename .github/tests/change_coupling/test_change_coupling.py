#!/usr/bin/env python3
"""Dependency-free regression tests for diff-aware change coupling."""

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_change_coupling.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/change-coupling-contract.json"


def run(root: Path, *args: str) -> None:
    result = subprocess.run(list(args), cwd=str(root), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise AssertionError("command failed: {}\n{}".format(" ".join(args), result.stderr))


def write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_change_coupling", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def body(**overrides: object) -> str:
    data: Dict[str, object] = {
        "change_class": "maintenance",
        "owning_paths": ["README.md"],
        "decision_levels": ["none"],
        "capability_families": ["none"],
        "terminology_impact": "unchanged",
        "research_state": "unchanged",
        "compatibility": "preserved",
        "changelog": "updated",
        "glossary": "unchanged",
        "roadmap": "unchanged",
        "traceability": "unchanged"
    }
    data.update(overrides)
    return "<!-- ua-change-contract\n{}\n-->".format(json.dumps(data))


def repository(change_path: str, delete: bool = False) -> tuple:
    temporary = tempfile.TemporaryDirectory(prefix="ua-change-coupling-")
    root = Path(temporary.name)
    run(root, "git", "init", "-q")
    run(root, "git", "config", "user.email", "fixture@example.com")
    run(root, "git", "config", "user.name", "Fixture")
    for path in ("README.md", "CHANGELOG.md", "ROADMAP.md", "00-doctrine/glossary.md", "content/research/framework-traceability.md"):
        write(root, path, "baseline\n")
    write(root, change_path, "baseline\n")
    run(root, "git", "add", ".")
    run(root, "git", "commit", "-qm", "baseline")
    base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()
    if delete:
        (root / change_path).unlink()
    else:
        write(root, change_path, "changed\n")
    run(root, "git", "add", "-A")
    run(root, "git", "commit", "-qm", "change")
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()
    return temporary, root, base, head


def messages(findings: List[object]) -> str:
    return "\n".join(item.message for item in findings)


def main() -> int:
    validator = load_validator()
    failures: List[str] = []

    cases = []

    temp, root, base, head = repository("README.md")
    cases.append(("notable change requires changelog", temp, root, base, head, body(changelog="not-required"), set(), "notable change requires CHANGELOG.md"))

    temp, root, base, head = repository("00-doctrine/glossary.md")
    cases.append(("glossary change requires declaration", temp, root, base, head, body(owning_paths=["00-doctrine/glossary.md"]), set(), "does not declare glossary updated"))

    temp, root, base, head = repository("ROADMAP.md")
    cases.append(("roadmap change requires declaration", temp, root, base, head, body(owning_paths=["ROADMAP.md"]), set(), "does not declare roadmap updated"))

    temp, root, base, head = repository("content/research/framework-traceability.md")
    cases.append(("traceability change requires declaration", temp, root, base, head, body(owning_paths=["content/research/framework-traceability.md"], changelog="not-required"), set(), "does not declare traceability updated"))

    temp, root, base, head = repository("00-doctrine/removed.md", delete=True)
    cases.append(("deletion requires compatibility", temp, root, base, head, body(owning_paths=["00-doctrine/removed.md"], compatibility="not-applicable"), set(), "requires an explicit compatibility decision"))

    temp, root, base, head = repository("README.md")
    cases.append(("missing PR contract is rejected", temp, root, base, head, "", set(), "exactly one ua-change-contract"))

    temp, root, base, head = repository("README.md")
    cases.append(("maintainer changelog exception works", temp, root, base, head, body(changelog="not-required"), {"ua-exception/changelog"}, None))

    for name, temp, root, base, head, pr_body, labels, expected in cases:
        findings = validator.validate(root, CONTRACT_PATH, base, head, pr_body, labels)
        errors = [item for item in findings if item.severity == "error"]
        text = messages(findings)
        if expected is None:
            if errors:
                failures.append("{}: expected no errors, got {}".format(name, text))
            else:
                print("PASS: {}".format(name))
        elif expected not in text:
            failures.append("{}: expected {!r}, got {}".format(name, expected, text))
        else:
            print("PASS: {}".format(name))
        temp.cleanup()

    if failures:
        print("Change coupling self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Change coupling self-tests passed: {} regression fixtures.".format(len(cases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
