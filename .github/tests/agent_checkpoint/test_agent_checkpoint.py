#!/usr/bin/env python3
"""Regression tests for the exact-state agent checkpoint validator."""

import importlib.util
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_agent_checkpoint.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/agent-checkpoint-contract.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_agent_checkpoint", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load agent checkpoint validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(root: Path, *args: str) -> str:
    result = subprocess.run(
        list(args),
        cwd=str(root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError("{} failed: {}".format(" ".join(args), result.stderr))
    return result.stdout.strip()


def write(root: Path, path: str, text: str) -> None:
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def commit(root: Path, message: str) -> str:
    run(root, "git", "add", ".")
    run(
        root,
        "git",
        "-c",
        "user.name=UA Test",
        "-c",
        "user.email=ua-test@example.invalid",
        "commit",
        "-m",
        message,
    )
    return run(root, "git", "rev-parse", "HEAD")


def render_checkpoint(data: Dict[str, object]) -> str:
    return "<!-- ua-agent-checkpoint\n{}\n-->".format(json.dumps(data, indent=2))


def body_for(validator, root: Path, base: str, head: str, **overrides) -> str:
    prefix = "## Summary\n\nfixture PR description\n\n"
    data: Dict[str, object] = {
        "checkpoint_version": 1,
        "reviewed_base_sha": base,
        "reviewed_head_sha": head,
        "reviewed_pr_body_sha256": "0" * 64,
        "applicable_agents": validator.applicable_agent_records(root, base, head),
        "diff_recheck": "completed",
        "pr_description_recheck": "completed",
        "corrective_feedback_review": "completed",
        "feedback_disposition": "none",
        "completion_recheck": "completed",
    }
    data.update(overrides)
    contract = validator.load_json(CONTRACT_PATH)
    provisional = prefix + render_checkpoint(data)
    if "reviewed_pr_body_sha256" not in overrides:
        data["reviewed_pr_body_sha256"] = validator.pr_body_sha256(provisional, contract)
    return prefix + render_checkpoint(data)


def messages(findings) -> List[str]:
    return [item.message for item in findings]


def expect_valid(validator, root: Path, base: str, head: str, body: str, name: str, failures: List[str]) -> None:
    findings = validator.validate(root, CONTRACT_PATH, base, head, body)
    if findings:
        failures.append("{}: expected success, got {}".format(name, messages(findings)))
    else:
        print("PASS: {}".format(name))


def expect_error(validator, root: Path, base: str, head: str, body: str, needle: str, name: str, failures: List[str]) -> None:
    findings = validator.validate(root, CONTRACT_PATH, base, head, body)
    if not any(needle in item.message for item in findings):
        failures.append("{}: expected error containing {!r}, got {}".format(name, needle, messages(findings)))
    else:
        print("PASS: {}".format(name))


def main() -> int:
    validator = load_validator()
    failures: List[str] = []

    with tempfile.TemporaryDirectory(prefix="ua-agent-checkpoint-") as temp:
        root = Path(temp)
        run(root, "git", "init", "-q")
        write(root, "AGENTS.md", "root rules\n")
        write(root, "README.md", "base\n")
        write(root, "content/research/AGENTS.md", "research rules\n")
        write(root, "content/research/note.md", "base note\n")
        base = commit(root, "base")

        write(root, "README.md", "changed\n")
        root_head = commit(root, "root change")
        valid_root = body_for(validator, root, base, root_head)
        expect_valid(validator, root, base, root_head, valid_root, "root-only checkpoint passes", failures)

        stale_head = body_for(validator, root, base, root_head, reviewed_head_sha=base)
        expect_error(
            validator,
            root,
            base,
            root_head,
            stale_head,
            "reviewed_head_sha",
            "stale head is rejected",
            failures,
        )

        stale_base = body_for(validator, root, base, root_head, reviewed_base_sha=root_head)
        expect_error(
            validator,
            root,
            base,
            root_head,
            stale_base,
            "reviewed_base_sha",
            "stale base is rejected",
            failures,
        )

        edited_description = valid_root.replace("fixture PR description", "description edited after checkpoint", 1)
        expect_error(
            validator,
            root,
            base,
            root_head,
            edited_description,
            "reviewed_pr_body_sha256",
            "PR description edit invalidates checkpoint",
            failures,
        )

        expect_error(
            validator,
            root,
            base,
            root_head,
            "## Summary\n\nmissing checkpoint\n",
            "exactly one ua-agent-checkpoint",
            "missing checkpoint is rejected",
            failures,
        )

        write(root, "content/research/note.md", "changed research note\n")
        nested_head = commit(root, "nested change")
        nested_valid = body_for(validator, root, base, nested_head)
        expect_valid(
            validator,
            root,
            base,
            nested_head,
            nested_valid,
            "nested AGENTS scope checkpoint passes",
            failures,
        )

        root_only_records = [validator.applicable_agent_records(root, base, nested_head)[0]]
        missing_nested = body_for(
            validator,
            root,
            base,
            nested_head,
            applicable_agents=root_only_records,
        )
        expect_error(
            validator,
            root,
            base,
            nested_head,
            missing_nested,
            "applicable_agents does not match",
            "missing nested AGENTS attestation is rejected",
            failures,
        )

        records = validator.applicable_agent_records(root, base, nested_head)
        bad_records = [dict(item) for item in records]
        bad_records[-1]["blob_sha"] = "0" * 40
        stale_rules = body_for(
            validator,
            root,
            base,
            nested_head,
            applicable_agents=bad_records,
        )
        expect_error(
            validator,
            root,
            base,
            nested_head,
            stale_rules,
            "applicable_agents does not match",
            "stale AGENTS blob is rejected",
            failures,
        )

        bad_status = body_for(
            validator,
            root,
            base,
            nested_head,
            completion_recheck="pending",
        )
        expect_error(
            validator,
            root,
            base,
            nested_head,
            bad_status,
            "completion_recheck",
            "incomplete checkpoint state is rejected",
            failures,
        )

        duplicate = nested_valid + "\n" + nested_valid
        expect_error(
            validator,
            root,
            base,
            nested_head,
            duplicate,
            "exactly one ua-agent-checkpoint",
            "duplicate checkpoint is rejected",
            failures,
        )

    if failures:
        print("Agent checkpoint self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print("Agent checkpoint self-tests passed: 10 regression fixtures.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
