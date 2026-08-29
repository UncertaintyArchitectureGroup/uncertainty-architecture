#!/usr/bin/env python3
"""Regression tests for the AI-agent checked-state checkpoint validator."""

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
        list(args), cwd=str(root), text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
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
    run(root, "git", "-c", "user.name=UA Test", "-c", "user.email=ua-test@example.invalid", "commit", "-m", message)
    return run(root, "git", "rev-parse", "HEAD")


def render_block(marker: str, data: Dict[str, object]) -> str:
    return "<!-- {}\n{}\n-->".format(marker, json.dumps(data, indent=2))


def change_contract(agent_assistance: str = "used", change_class: str = "maintenance") -> Dict[str, object]:
    return {
        "change_class": change_class,
        "agent_assistance": agent_assistance,
        "owning_paths": ["AGENTS.md"],
        "decision_levels": ["none"],
        "capability_families": ["none"],
        "terminology_impact": "unchanged",
        "research_state": "unchanged",
        "compatibility": "preserved",
        "changelog": "updated",
        "glossary": "unchanged",
        "roadmap": "updated",
        "traceability": "unchanged",
    }


def context_for(
    body: str,
    diff_base: str,
    base_tip: str,
    head: str,
    merge: str,
    feedback: str = "1" * 64,
    draft: bool = True,
    ready_head: str = "",
    ready_approval_present: bool = False,
    ready_transition_authorized: bool = False,
    ready_check_passed: bool = False,
    agent_none_approved: bool = False,
    action: str = "synchronize",
    event_name: str = "pull_request",
    labels=None,
    pr_author: str = "contributor",
) -> Dict[str, object]:
    return {
        "body": body,
        "diff_base_sha": diff_base,
        "base_tip_sha": base_tip,
        "head_sha": head,
        "merge_sha": merge,
        "feedback_sha256": feedback,
        "draft": draft,
        "ready_head_sha": ready_head,
        "ready_approval_present": ready_approval_present,
        "ready_transition_authorized": ready_transition_authorized,
        "ready_check_passed": ready_check_passed,
        "agent_none_approved": agent_none_approved,
        "event_name": event_name,
        "event_action": action,
        "labels": list(labels or []),
        "pr_author": pr_author,
    }


def body_for(
    validator,
    root: Path,
    diff_base: str,
    base_tip: str,
    head: str,
    merge: str,
    assistance: str = "used",
    change_class: str = "maintenance",
    feedback: str = "1" * 64,
    **overrides,
) -> str:
    prefix = "## Summary\n\nfixture PR\n\n" + render_block("ua-change-contract", change_contract(assistance, change_class)) + "\n\n"
    if assistance == "none":
        return prefix
    data: Dict[str, object] = {
        "checkpoint_version": 1,
        "reviewed_base_sha": diff_base,
        "reviewed_base_tip_sha": base_tip,
        "reviewed_head_sha": head,
        "reviewed_merge_sha": merge,
        "reviewed_pr_body_sha256": "0" * 64,
        "reviewed_feedback_sha256": feedback,
        "applicable_agents": validator.applicable_agent_records(root, base_tip, head, merge),
        "diff_recheck": "completed",
        "pr_description_recheck": "completed",
        "corrective_feedback_review": "completed",
        "feedback_disposition": "none",
        "completion_recheck": "completed",
    }
    data.update(overrides)
    provisional = prefix + render_block("ua-agent-checkpoint", data)
    if "reviewed_pr_body_sha256" not in overrides:
        data["reviewed_pr_body_sha256"] = validator.pr_body_sha256(provisional, "ua-agent-checkpoint")
    return prefix + render_block("ua-agent-checkpoint", data)


def messages(findings) -> List[str]:
    return [item.message for item in findings]


def expect_valid(validator, root: Path, context: Dict[str, object], name: str, failures: List[str]) -> None:
    findings = validator.validate(root, CONTRACT_PATH, context)
    errors = [item for item in findings if item.severity == "error"]
    if errors:
        failures.append("{}: expected no errors, got {}".format(name, messages(findings)))
    else:
        print("PASS: {}".format(name))


def expect_error(validator, root: Path, context: Dict[str, object], needle: str, name: str, failures: List[str]) -> None:
    findings = validator.validate(root, CONTRACT_PATH, context)
    if not any(item.severity == "error" and needle in item.message for item in findings):
        failures.append("{}: expected error containing {!r}, got {}".format(name, needle, messages(findings)))
    else:
        print("PASS: {}".format(name))


def expect_error_without(
    validator, root: Path, context: Dict[str, object], needle: str, forbidden: str,
    name: str, failures: List[str],
) -> None:
    findings = validator.validate(root, CONTRACT_PATH, context)
    text = messages(findings)
    if not any(item.severity == "error" and needle in item.message for item in findings):
        failures.append("{}: expected error containing {!r}, got {}".format(name, needle, text))
    elif any(forbidden in item.message for item in findings):
        failures.append("{}: unexpected {!r} finding: {}".format(name, forbidden, text))
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
        head = commit(root, "feature")

        human_body = body_for(validator, root, base, base, head, head, assistance="none")
        expect_error(
            validator, root,
            context_for(human_body, base, base, head, head, draft=False),
            "maintainer-controlled opt-out",
            "human-only self-attestation cannot disable checkpoint without CODEOWNER approval",
            failures,
        )
        expect_valid(
            validator, root,
            context_for(human_body, base, base, head, head, draft=False, agent_none_approved=True),
            "CODEOWNER-approved human-only PR needs no agent checkpoint",
            failures,
        )
        expect_valid(
            validator, root,
            context_for(human_body, base, base, head, head, draft=False, pr_author="dependabot[bot]"),
            "Dependabot none path remains exempt",
            failures,
        )

        assisted_missing = "## Summary\n\nfixture\n\n" + render_block("ua-change-contract", change_contract("used"))
        expect_error(validator, root, context_for(assisted_missing, base, base, head, head), "ua-agent-checkpoint", "assisted PR missing checkpoint is rejected", failures)

        expect_error(
            validator, root,
            context_for("No contract here.", base, base, head, head, labels=["ua-exception/pr-contract"]),
            "ua-agent-checkpoint",
            "PR-contract exception does not bypass the agent checkpoint",
            failures,
        )

        valid_body = body_for(validator, root, base, base, head, head)
        valid_context = context_for(valid_body, base, base, head, head)
        expect_valid(validator, root, valid_context, "assisted root checkpoint passes", failures)

        for field, value, needle, name in (
            ("reviewed_head_sha", base, "reviewed_head_sha", "stale head is rejected"),
            ("reviewed_base_tip_sha", head, "reviewed_base_tip_sha", "stale base tip is rejected"),
            ("reviewed_merge_sha", base, "reviewed_merge_sha", "stale merge is rejected"),
            ("reviewed_feedback_sha256", "2" * 64, "reviewed_feedback_sha256", "new trusted review feedback invalidates checkpoint"),
        ):
            body = body_for(validator, root, base, base, head, head, **{field: value})
            expect_error(validator, root, context_for(body, base, base, head, head), needle, name, failures)

        edited = valid_body.replace("fixture PR", "edited PR description", 1)
        expect_error(validator, root, context_for(edited, base, base, head, head), "reviewed_pr_body_sha256", "PR description edit invalidates checkpoint", failures)

        repo_policy_body = body_for(validator, root, base, base, head, head, change_class="repository-policy")
        expect_error(
            validator, root,
            context_for(repo_policy_body, base, base, head, head, draft=False),
            "must remain Draft",
            "active assisted repository-policy PR must be Draft before readiness",
            failures,
        )
        expect_error(
            validator, root,
            context_for(
                repo_policy_body, base, base, head, head,
                draft=False, ready_head=head, action="ready_for_review",
                ready_transition_authorized=False,
            ),
            "must remain Draft",
            "author-controlled ready event without CODEOWNER checkpoint approval is rejected",
            failures,
        )
        expect_valid(
            validator, root,
            context_for(
                repo_policy_body, base, base, head, head,
                draft=False, ready_head=head, action="ready_for_review",
                ready_approval_present=True, ready_transition_authorized=True,
            ),
            "CODEOWNER-authorized ready transition with fresh checkpoint passes",
            failures,
        )
        expect_error(
            validator, root,
            context_for(
                repo_policy_body, base, base, head, head,
                draft=False, ready_head=head, action="edited",
                ready_approval_present=True, ready_transition_authorized=True,
                ready_check_passed=False,
            ),
            "must remain Draft",
            "failed ready transition cannot be legalized later by checkpoint edit",
            failures,
        )
        expect_valid(
            validator, root,
            context_for(
                repo_policy_body, base, base, head, head,
                draft=False, ready_head=head, event_name="pull_request_review", action="submitted",
                ready_approval_present=True, ready_check_passed=True,
            ),
            "successful readiness check keeps same head ready during review",
            failures,
        )
        expect_error_without(
            validator, root,
            context_for(
                repo_policy_body, base, base, head, head,
                feedback="2" * 64, draft=False, ready_head=head,
                event_name="pull_request_review", action="submitted",
                ready_approval_present=True, ready_check_passed=True,
            ),
            "reviewed_feedback_sha256",
            "must remain Draft",
            "trusted review feedback stales checkpoint without revoking successful readiness",
            failures,
        )

        write(root, "README.md", "changed again\n")
        newer_head = commit(root, "new repository iteration")
        newer_body = body_for(validator, root, base, base, newer_head, newer_head, change_class="repository-policy")
        expect_error(
            validator, root,
            context_for(
                newer_body, base, base, newer_head, newer_head,
                draft=False, ready_head=head,
                ready_approval_present=True, ready_check_passed=False,
            ),
            "must remain Draft",
            "new head after readiness requires Draft again",
            failures,
        )

        write(root, "content/research/note.md", "changed research\n")
        nested_head = commit(root, "nested")
        nested_body = body_for(validator, root, base, base, nested_head, nested_head)
        expect_valid(validator, root, context_for(nested_body, base, base, nested_head, nested_head), "nested AGENTS scope passes", failures)
        root_only = [validator.applicable_agent_records(root, base, nested_head, nested_head)[0]]
        missing_nested = body_for(validator, root, base, base, nested_head, nested_head, applicable_agents=root_only)
        expect_error(validator, root, context_for(missing_nested, base, base, nested_head, nested_head), "applicable_agents", "missing nested AGENTS is rejected", failures)

        suffix = "<!-- ua-agent-checkpoint" + nested_body.split("<!-- ua-agent-checkpoint", 1)[1]
        expect_error(validator, root, context_for(nested_body + "\n" + suffix, base, base, nested_head, nested_head), "exactly one ua-agent-checkpoint", "duplicate checkpoint is rejected", failures)

        run(root, "git", "mv", "content/research/note.md", "moved-note.md")
        rename_head = commit(root, "rename")
        rename_records = validator.applicable_agent_records(root, nested_head, rename_head, rename_head)
        if any(item["path"] == "content/research/AGENTS.md" for item in rename_records):
            print("PASS: rename retains old nested AGENTS scope")
        else:
            failures.append("rename did not retain old nested AGENTS scope")

        research_blob = validator.blob_sha_at(root, rename_head, "content/research/AGENTS.md")
        (root / "content/research/AGENTS.md").unlink()
        deleted_head = commit(root, "delete nested guidance")
        deleted_records = validator.applicable_agent_records(root, rename_head, deleted_head, deleted_head)
        record = next((item for item in deleted_records if item["path"] == "content/research/AGENTS.md"), None)
        if record and record["blob_sha"] == research_blob:
            print("PASS: deleted nested AGENTS uses governing current-base blob")
        else:
            failures.append("deleted nested AGENTS did not retain governing base blob")

    with tempfile.TemporaryDirectory(prefix="ua-agent-sync-") as temp:
        root = Path(temp)
        run(root, "git", "init", "-q")
        write(root, "AGENTS.md", "root\n")
        write(root, "src/item.md", "base\n")
        write(root, "target-only/AGENTS.md", "target only rules\n")
        write(root, "target-only/item.md", "base\n")
        base = commit(root, "base")

        run(root, "git", "checkout", "-q", "-b", "feature")
        write(root, "src/item.md", "feature\n")
        feature_before_sync = commit(root, "feature")

        run(root, "git", "checkout", "-q", "-b", "target", base)
        write(root, "target-only/item.md", "target changed\n")
        base_tip = commit(root, "target advance")

        run(root, "git", "checkout", "-q", "feature")
        run(root, "git", "-c", "user.name=UA Test", "-c", "user.email=ua-test@example.invalid", "merge", "--no-ff", "target", "-m", "sync target")
        synced_head = run(root, "git", "rev-parse", "HEAD")
        paths = validator.changed_paths(root, base_tip, synced_head)
        if paths == ["src/item.md"]:
            print("PASS: synchronized target-only changes are excluded from PR-owned scope")
        else:
            failures.append("synchronized diff scope expected ['src/item.md'], got {}".format(paths))
        records = validator.applicable_agent_records(root, base_tip, synced_head, synced_head)
        if any(item["path"] == "target-only/AGENTS.md" for item in records):
            failures.append("target-only nested AGENTS incorrectly activated after feature sync")
        else:
            print("PASS: synchronized target-only AGENTS does not activate")

        run(root, "git", "checkout", "-q", "target")
        write(root, "src/AGENTS.md", "new target src rules\n")
        newer_base_tip = commit(root, "target adds src rules")
        run(root, "git", "checkout", "-q", "feature")
        run(root, "git", "reset", "--hard", feature_before_sync)
        feature_head = run(root, "git", "rev-parse", "HEAD")
        run(root, "git", "-c", "user.name=UA Test", "-c", "user.email=ua-test@example.invalid", "merge", "--no-ff", "target", "-m", "tested merge")
        tested_merge = run(root, "git", "rev-parse", "HEAD")
        records = validator.applicable_agent_records(root, newer_base_tip, feature_head, tested_merge)
        if any(item["path"] == "src/AGENTS.md" for item in records):
            print("PASS: advanced target contributes new nested AGENTS to tested merge")
        else:
            failures.append("advanced target nested AGENTS was not included")

    with tempfile.TemporaryDirectory(prefix="ua-agent-policy-class-") as temp:
        root = Path(temp)
        run(root, "git", "init", "-q")
        write(root, "AGENTS.md", "root rules\n")
        write(root, ".github/policy/example.json", "{}\n")
        base = commit(root, "base")
        write(root, ".github/policy/example.json", "{\"changed\": true}\n")
        head = commit(root, "policy change")
        weak_body = body_for(validator, root, base, base, head, head, change_class="maintenance")
        expect_error(
            validator, root,
            context_for(weak_body, base, base, head, head, draft=True),
            "require change_class 'repository-policy'",
            "repository-policy diff cannot disable controls with maintenance declaration",
            failures,
        )

    with tempfile.TemporaryDirectory(prefix="ua-agent-normative-class-") as temp:
        root = Path(temp)
        run(root, "git", "init", "-q")
        write(root, "AGENTS.md", "root rules\n")
        write(root, "00-doctrine/example.md", "---\nstatus: draft-normative\n---\nbase\n")
        base = commit(root, "base")
        write(root, "00-doctrine/example.md", "---\nstatus: informative\n---\nchanged\n")
        head = commit(root, "attempt status downgrade")
        weak_body = body_for(validator, root, base, base, head, head, change_class="maintenance")
        expect_error(
            validator, root,
            context_for(weak_body, base, base, head, head, draft=True),
            "protected status draft-normative",
            "normative-status document cannot disable controls by status and class downgrade",
            failures,
        )

    if failures:
        print("Agent checkpoint self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Agent checkpoint self-tests passed: 26 regression assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
