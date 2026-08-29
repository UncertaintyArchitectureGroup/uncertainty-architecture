#!/usr/bin/env python3
"""Dependency-free regression tests for diff-aware change coupling."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_change_coupling.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/change-coupling-contract.json"
CASES_PATH = Path(__file__).with_name("cases.json")

REQUIRED_CASE_NAMES: Set[str] = {
    "valid repository policy change with companion updates passes",
    "repository policy paths cannot be declared maintenance",
    "agent guidance policy path cannot be declared maintenance",
    "draft normative status cannot be downgraded to maintenance",
    "missing PR contract is rejected",
    "duplicate PR contract is rejected",
    "malformed PR contract JSON is rejected",
    "missing required PR field is rejected",
    "unknown PR field is rejected",
    "uncontrolled change class is rejected",
    "uncontrolled agent assistance is rejected",
    "notable change without changelog is rejected",
    "changelog declaration without file change is rejected",
    "changed changelog without updated declaration is rejected",
    "glossary declaration without glossary change is rejected",
    "changed glossary without updated declaration is rejected",
    "repository policy change without roadmap is rejected",
    "roadmap declaration without roadmap change is rejected",
    "research state decision without traceability is rejected",
    "traceability declaration without file change is rejected",
    "maintained deletion without compatibility decision is rejected",
    "maintained deletion without changelog is rejected",
    "maintained rename without compatibility decision is rejected",
    "owning path outside diff is rejected",
    "changelog exception label bypasses only changelog requirement",
    "wrong exception label does not bypass changelog requirement",
    "PR contract exception label bypasses missing block as warning",
}


def run(root: Path, *args: str) -> None:
    result = subprocess.run(
        list(args), cwd=str(root), text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise AssertionError(
            "command failed: {}\n{}\n{}".format(
                " ".join(args), result.stdout, result.stderr
            )
        )


def write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_change_coupling", VALIDATOR_PATH
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("unable to load validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def default_pr() -> Dict[str, object]:
    return {
        "change_class": "maintenance",
        "agent_assistance": "none",
        "owning_paths": ["README.md"],
        "decision_levels": ["none"],
        "capability_families": ["none"],
        "terminology_impact": "unchanged",
        "research_state": "unchanged",
        "compatibility": "preserved",
        "changelog": "not-required",
        "glossary": "unchanged",
        "roadmap": "unchanged",
        "traceability": "unchanged",
    }


def contract_body(data: Dict[str, object]) -> str:
    return "<!-- ua-change-contract\n{}\n-->".format(
        json.dumps(data, sort_keys=True)
    )


def case_body(case: Dict[str, object]) -> str:
    if "body" in case:
        return str(case["body"])

    data = default_pr()
    explicit = case.get("pr")
    if isinstance(explicit, dict):
        data.update(explicit)
    overrides = case.get("set_pr_field")
    if isinstance(overrides, dict):
        data.update(overrides)
    remove = case.get("remove_pr_field")
    if isinstance(remove, str):
        data.pop(remove, None)
    extra = case.get("extra_pr_field")
    if isinstance(extra, dict):
        data.update(extra)

    body = contract_body(data)
    if case.get("body_mode") == "duplicate":
        body += "\n" + contract_body(data)
    return body


def materialize_repository(case: Dict[str, object]):
    temporary = tempfile.TemporaryDirectory(prefix="ua-change-coupling-")
    root = Path(temporary.name)
    run(root, "git", "init", "-q")
    run(root, "git", "config", "user.email", "fixture@example.com")
    run(root, "git", "config", "user.name", "Fixture")

    baseline = {
        "README.md": "baseline\n",
        "CHANGELOG.md": "baseline\n",
        "ROADMAP.md": "baseline\n",
        "00-doctrine/glossary.md": "baseline\n",
        "content/research/framework-traceability.md": "baseline\n",
    }
    extra_base = case.get("base_files")
    if isinstance(extra_base, dict):
        baseline.update({str(k): str(v) for k, v in extra_base.items()})

    for path, text in baseline.items():
        write(root, path, text)

    run(root, "git", "add", ".")
    run(root, "git", "commit", "-qm", "baseline")
    base = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=str(root), text=True
    ).strip()

    files = case.get("files")
    if isinstance(files, dict):
        for path, text in files.items():
            write(root, str(path), str(text))

    deletes = case.get("delete_files")
    if isinstance(deletes, list):
        for path in deletes:
            target = root / str(path)
            if target.exists():
                target.unlink()

    renames = case.get("rename_files")
    if isinstance(renames, dict):
        for old, new in renames.items():
            source = root / str(old)
            target = root / str(new)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(target))

    run(root, "git", "add", "-A")
    run(root, "git", "commit", "--allow-empty", "-qm", "change")
    head = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=str(root), text=True
    ).strip()
    return temporary, root, base, head


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


def messages(findings: List[object]) -> str:
    return "\n".join(item.message for item in findings)


def run_synced_target_scope_regression(validator, failures: List[str]) -> None:
    with tempfile.TemporaryDirectory(prefix="ua-change-coupling-sync-") as temp:
        root = Path(temp)
        run(root, "git", "init", "-q")
        run(root, "git", "config", "user.email", "fixture@example.com")
        run(root, "git", "config", "user.name", "Fixture")
        write(root, "notes/item.md", "base\n")
        write(root, ".github/policy/target-only.json", "{}\n")
        write(root, "CHANGELOG.md", "base\n")
        write(root, "ROADMAP.md", "base\n")
        write(root, "00-doctrine/glossary.md", "base\n")
        write(root, "content/research/framework-traceability.md", "base\n")
        run(root, "git", "add", ".")
        run(root, "git", "commit", "-qm", "base")
        base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()

        run(root, "git", "checkout", "-qb", "feature")
        write(root, "notes/item.md", "feature\n")
        run(root, "git", "add", ".")
        run(root, "git", "commit", "-qm", "feature")

        run(root, "git", "checkout", "-qb", "target", base)
        write(root, ".github/policy/target-only.json", "{\"target\": true}\n")
        run(root, "git", "add", ".")
        run(root, "git", "commit", "-qm", "target advance")
        base_tip = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()

        run(root, "git", "checkout", "-q", "feature")
        run(root, "git", "merge", "--no-ff", "target", "-m", "sync target")
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()

        declaration = default_pr()
        declaration["owning_paths"] = ["notes/item.md"]
        findings = validator.validate(
            root, CONTRACT_PATH, base_tip, head, contract_body(declaration), set()
        )
        errors = [item.message for item in findings if item.severity == "error"]
        if errors:
            failures.append("synchronized target-only changes leaked into PR-owned change coupling: {}".format(errors))
        else:
            print("PASS: synchronized target-only changes are excluded from change-coupling PR scope")


def main() -> int:
    validator = load_validator()
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    failures = validate_case_manifest(cases)

    for case in cases:
        temporary, root, base, head = materialize_repository(case)
        try:
            labels = {
                str(item) for item in case.get("labels", [])
                if isinstance(item, str)
            }
            actor = str(case.get("actor", ""))
            findings = validator.validate(
                root, CONTRACT_PATH, base, head, case_body(case), labels,
                actor=actor,
            )
            errors = [item for item in findings if item.severity == "error"]
            text = messages(findings)

            if case.get("expected_valid"):
                if errors:
                    failures.append(
                        "{}: expected no errors, got {}".format(case["name"], text)
                    )
                else:
                    print("PASS: {}".format(case["name"]))
                continue

            expected = str(case.get("expected_message", ""))
            if expected not in text:
                failures.append(
                    "{}: expected {!r}, got {}".format(
                        case["name"], expected, text
                    )
                )
            else:
                print("PASS: {}".format(case["name"]))
        finally:
            temporary.cleanup()

    run_synced_target_scope_regression(validator, failures)

    if failures:
        print("Change coupling self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print(
        "Change coupling self-tests passed: {} manifest fixtures plus synchronized-target scope regression.".format(
            len(cases)
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
