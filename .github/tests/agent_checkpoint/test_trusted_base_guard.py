#!/usr/bin/env python3
"""Regression tests for the trusted-base agent policy guard."""

import importlib.util
import json
import sys
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPOSITORY_ROOT / ".github/scripts/validate_agent_policy_guard.py"


def load_module():
    sys.path.insert(0, str(SCRIPT_PATH.parent))
    spec = importlib.util.spec_from_file_location("validate_agent_policy_guard", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load trusted-base guard")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def block(marker: str, value: Dict[str, object]) -> str:
    return "<!-- {}\n{}\n-->".format(marker, json.dumps(value, sort_keys=True))


def make_body(module, base_tip: str, head: str, merge: str, change_class: str = "maintenance") -> str:
    change = {
        "change_class": change_class,
        "agent_assistance": "used",
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
    prefix = block("ua-change-contract", change) + "\n"
    checkpoint = {
        "checkpoint_version": 1,
        "reviewed_base_sha": base_tip,
        "reviewed_base_tip_sha": base_tip,
        "reviewed_head_sha": head,
        "reviewed_merge_sha": merge,
        "reviewed_pr_body_sha256": "0" * 64,
        "reviewed_feedback_sha256": "f" * 64,
        "applicable_agents": [{"path": "AGENTS.md", "blob_sha": "a" * 40}],
        "diff_recheck": "completed",
        "pr_description_recheck": "completed",
        "corrective_feedback_review": "completed",
        "feedback_disposition": "none",
        "completion_recheck": "completed",
    }
    provisional = prefix + block("ua-agent-checkpoint", checkpoint)
    checkpoint["reviewed_pr_body_sha256"] = module.pr_body_sha256(provisional, "ua-agent-checkpoint")
    return prefix + block("ua-agent-checkpoint", checkpoint)


def make_pr(body: str, head: str, merge: str, draft: bool = True) -> Dict[str, object]:
    return {
        "number": 104,
        "body": body,
        "draft": draft,
        "merge_commit_sha": merge,
        "labels": [],
        "user": {"login": "contributor"},
        "base": {"ref": "main", "sha": "b" * 40},
        "head": {
            "sha": head,
            "repo": {"full_name": "owner/repo"},
        },
    }


def error_messages(findings) -> List[str]:
    return [item.message for item in findings if item.severity == "error"]


def main() -> int:
    module = load_module()
    failures: List[str] = []
    base_tip = "1" * 40
    head = "2" * 40
    merge = "3" * 40
    change_contract = {
        "contract_version": 1,
        "repository_policy_prefixes": [".github/", "AGENTS.md", "CONTRIBUTING.md", "DOCUMENT-METADATA.md"],
        "draft_required_document_statuses": ["draft-normative", "normative"],
        "exception_labels": {"ua-exception/pr-contract": ["pr-contract"]},
    }
    checkpoint_contract = {
        "contract_version": 1,
        "pr_change_contract_marker": "ua-change-contract",
        "pr_checkpoint_marker": "ua-agent-checkpoint",
        "agent_none_approval_marker": "ua-agent-assistance-none",
        "ready_approval_marker": "ua-agent-ready-approval",
        "maintainer_authority_path": ".github/CODEOWNERS",
        "trusted_feedback_author_associations": ["OWNER", "MEMBER", "COLLABORATOR"],
        "draft_required_change_classes": ["repository-policy", "draft-normative", "normative"],
    }

    original = {
        name: getattr(module, name)
        for name in (
            "branch_tip", "pr_files", "observed_draft_statuses", "fetch_file_optional",
            "global_codeowners", "authorized_codeowners", "issue_comments", "feedback_sha256",
        )
    }
    try:
        module.branch_tip = lambda repository, branch, token: base_tip
        module.fetch_file_optional = lambda repository, path, ref, token: "* @maintainer\n"
        module.global_codeowners = lambda text: {"maintainer"}
        module.authorized_codeowners = lambda repository, owners, token: {"maintainer"}
        module.issue_comments = lambda repository, pr_number, token: []
        module.feedback_sha256 = lambda repository, pr_number, token, trusted: "f" * 64

        body = make_body(module, base_tip, head, merge, change_class="maintenance")
        pr = make_pr(body, head, merge)

        module.pr_files = lambda repository, pr_number, token: [
            {"filename": ".github/workflows/example.yml", "status": "modified"}
        ]
        module.observed_draft_statuses = lambda *args, **kwargs: set()
        findings = module.validate_pr("owner/repo", pr, "token", change_contract, checkpoint_contract, "pull_request_target", "synchronize")
        if any("repository-policy paths require change_class" in item for item in error_messages(findings)):
            print("PASS: trusted-base policy classification cannot be weakened by candidate declaration")
        else:
            failures.append("repository-policy misclassification was not rejected")

        module.pr_files = lambda repository, pr_number, token: [
            {"filename": "00-doctrine/example.md", "status": "modified"}
        ]
        module.observed_draft_statuses = lambda *args, **kwargs: {"draft-normative"}
        findings = module.validate_pr("owner/repo", pr, "token", change_contract, checkpoint_contract, "pull_request_target", "synchronize")
        if any("protected document status" in item for item in error_messages(findings)):
            print("PASS: draft-normative content cannot be disguised as maintenance")
        else:
            failures.append("normative-status misclassification was not rejected")

        module.pr_files = lambda repository, pr_number, token: [
            {"filename": "README.md", "status": "modified"}
        ]
        module.observed_draft_statuses = lambda *args, **kwargs: set()
        stale_body = make_body(module, "9" * 40, head, merge)
        stale_pr = make_pr(stale_body, head, merge)
        findings = module.validate_pr("owner/repo", stale_pr, "token", change_contract, checkpoint_contract, "push", "")
        if any("reviewed_base_tip_sha is stale" in item for item in error_messages(findings)):
            print("PASS: target-branch advance invalidates a stale checkpoint without head change")
        else:
            failures.append("base-tip advance did not stale the trusted-base checkpoint")

        exception_pr = make_pr(block("ua-agent-checkpoint", {
            "reviewed_base_tip_sha": base_tip,
            "reviewed_head_sha": head,
            "reviewed_merge_sha": merge,
            "reviewed_pr_body_sha256": "0" * 64,
            "reviewed_feedback_sha256": "f" * 64,
        }), head, merge)
        exception_pr["labels"] = [{"name": "ua-exception/pr-contract"}]
        findings = module.validate_pr("owner/repo", exception_pr, "token", change_contract, checkpoint_contract, "pull_request_target", "edited")
        if any("reviewed_pr_body_sha256 is stale" in item for item in error_messages(findings)):
            print("PASS: PR-contract exception does not bypass the agent checkpoint")
        else:
            failures.append("PR-contract exception still acted as a checkpoint escape")
    finally:
        for name, value in original.items():
            setattr(module, name, value)

    if failures:
        print("Trusted-base guard self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Trusted-base guard self-tests passed: 4 regression assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
