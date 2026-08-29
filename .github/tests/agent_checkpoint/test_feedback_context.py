#!/usr/bin/env python3
"""Regression tests for deterministic PR feedback, CODEOWNER approval, and readiness context."""

import importlib.util
import sys
from pathlib import Path
from typing import Dict, List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPOSITORY_ROOT / ".github/scripts/fetch_agent_checkpoint_context.py"


def load_module():
    spec = importlib.util.spec_from_file_location("fetch_agent_checkpoint_context", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load feedback context script")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def user(login: str, user_type: str = "User") -> Dict[str, object]:
    return {"login": login, "type": user_type}


def main() -> int:
    module = load_module()
    failures: List[str] = []
    fixtures: Dict[str, List[Dict[str, object]]] = {
        "reviews": [
            {
                "id": 3,
                "user": user("reviewer"),
                "author_association": "COLLABORATOR",
                "submitted_at": "2026-08-29T08:02:00Z",
                "state": "CHANGES_REQUESTED",
                "body": "scope is wrong",
            },
            {
                "id": 6,
                "user": user("visitor"),
                "author_association": "NONE",
                "submitted_at": "2026-08-29T08:02:30Z",
                "state": "COMMENTED",
                "body": "untrusted review noise",
            },
        ],
        "pull-comments": [
            {
                "id": 4,
                "user": user("member"),
                "author_association": "MEMBER",
                "created_at": "2026-08-29T08:03:00Z",
                "updated_at": "2026-08-29T08:03:00Z",
                "body": "inline correction",
            },
            {
                "id": 5,
                "user": user("bot[bot]", "Bot"),
                "author_association": "MEMBER",
                "created_at": "2026-08-29T08:04:00Z",
                "updated_at": "2026-08-29T08:04:00Z",
                "body": "bot output",
            },
        ],
    }
    calls: List[str] = []

    def fake_paged(url: str, token: str):
        calls.append(url)
        if url.endswith("/reviews?per_page=100"):
            return fixtures["reviews"]
        if url.endswith("/pulls/104/comments?per_page=100"):
            return fixtures["pull-comments"]
        raise AssertionError("unexpected deterministic feedback endpoint: {}".format(url))

    module.paged_list = fake_paged
    trusted = ["OWNER", "MEMBER", "COLLABORATOR"]
    first = module.feedback_sha256("owner/repo", 104, "token", trusted)
    second = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if first == second:
        print("PASS: feedback watermark is deterministic")
    else:
        failures.append("feedback watermark changed without input change")

    if all("/issues/104/comments" not in url for url in calls):
        print("PASS: top-level PR comments are excluded from deterministic PR-head feedback")
    else:
        failures.append("top-level PR comments were queried by deterministic feedback watermark")

    fixtures["reviews"][1]["body"] = "different untrusted review noise"
    if module.feedback_sha256("owner/repo", 104, "token", trusted) == first:
        print("PASS: untrusted reviewer does not change feedback watermark")
    else:
        failures.append("untrusted review changed the watermark")

    fixtures["reviews"][0]["body"] = "edited maintainer correction"
    edited = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if edited != first:
        print("PASS: edited trusted review invalidates watermark")
    else:
        failures.append("trusted review edit did not change watermark")

    fixtures["reviews"][0]["state"] = "DISMISSED"
    dismissed = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if dismissed != edited:
        print("PASS: review state change invalidates watermark")
    else:
        failures.append("review state change did not change watermark")

    fixtures["pull-comments"] = []
    deleted = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if deleted != dismissed:
        print("PASS: deleted trusted inline feedback invalidates watermark")
    else:
        failures.append("trusted inline feedback deletion did not change watermark")

    owners = module.global_codeowners("# owners\n* @maintainer\n/content/ @other\n")
    if owners == {"maintainer"}:
        print("PASS: authorization authority comes from target-branch global CODEOWNER")
    else:
        failures.append("unexpected global CODEOWNER set: {}".format(owners))

    checkpoint_body = "<!-- ua-agent-checkpoint\n{\"checkpoint_version\":1}\n-->"
    checkpoint_hash = module.checkpoint_sha256(checkpoint_body, "ua-agent-checkpoint")
    if len(checkpoint_hash) == 64 and checkpoint_hash == module.checkpoint_sha256(checkpoint_body, "ua-agent-checkpoint"):
        print("PASS: checkpoint fingerprint is canonical and deterministic")
    else:
        failures.append("checkpoint fingerprint is invalid or unstable")

    head = "a" * 40
    other_head = "b" * 40
    none_marker = "<!-- ua-agent-assistance-none\n{\"agent_assistance\":\"none\",\"head_sha\":\"%s\"}\n-->" % head
    none_comments = [
        {
            "id": 12,
            "user": user("maintainer"),
            "created_at": "2026-08-29T08:00:00Z",
            "updated_at": "2026-08-29T08:00:00Z",
            "body": none_marker,
        }
    ]
    if module.agent_none_approved(none_comments, {"maintainer"}, "ua-agent-assistance-none", head):
        print("PASS: CODEOWNER none opt-out is bound to the exact current head")
    else:
        failures.append("head-bound CODEOWNER none approval was not recognized")
    if not module.agent_none_approved(none_comments, {"maintainer"}, "ua-agent-assistance-none", other_head):
        print("PASS: new repository head invalidates prior agent-assistance-none approval")
    else:
        failures.append("old none approval survived a new head")
    if not module.agent_none_approved(none_comments, {"someone-else"}, "ua-agent-assistance-none", head):
        print("PASS: non-CODEOWNER comment cannot opt a PR out of agent checkpoint")
    else:
        failures.append("non-CODEOWNER disabled agent checkpoint")

    ready_at = "2026-08-29T09:00:00Z"
    merge = "c" * 40
    body_hash = "d" * 64
    approval_body = (
        "<!-- ua-agent-ready-approval\n"
        "{\"head_sha\":\"%s\",\"merge_sha\":\"%s\",\"pr_body_sha256\":\"%s\",\"checkpoint_sha256\":\"%s\"}\n"
        "-->"
    ) % (head, merge, body_hash, checkpoint_hash)
    comments = [
        {
            "id": 10,
            "user": user("maintainer"),
            "created_at": "2026-08-29T08:59:00Z",
            "updated_at": "2026-08-29T08:59:00Z",
            "body": approval_body,
        },
        {
            "id": 11,
            "user": user("visitor"),
            "created_at": "2026-08-29T08:59:30Z",
            "updated_at": "2026-08-29T08:59:30Z",
            "body": approval_body,
        },
    ]
    present, authorized = module.readiness_approval(
        comments, {"maintainer"}, "ua-agent-ready-approval",
        head, merge, checkpoint_hash, body_hash, ready_at,
    )
    if present and authorized:
        print("PASS: CODEOWNER Ready approval binds head, merge, PR body, and checkpoint fingerprint")
    else:
        failures.append("valid CODEOWNER readiness approval was not recognized")

    stale_body_present, stale_body_authorized = module.readiness_approval(
        comments, {"maintainer"}, "ua-agent-ready-approval",
        head, merge, checkpoint_hash, "e" * 64, ready_at,
    )
    if not stale_body_present and not stale_body_authorized:
        print("PASS: substantive PR-body change invalidates durable Ready approval")
    else:
        failures.append("Ready approval survived a changed PR-body digest")

    stale_merge_present, _ = module.readiness_approval(
        comments, {"maintainer"}, "ua-agent-ready-approval",
        head, "f" * 40, checkpoint_hash, body_hash, ready_at,
    )
    if not stale_merge_present:
        print("PASS: changed tested-merge state invalidates Ready approval")
    else:
        failures.append("Ready approval survived a changed merge state")

    _, wrong_checkpoint = module.readiness_approval(
        comments, {"maintainer"}, "ua-agent-ready-approval",
        head, merge, "1" * 64, body_hash, ready_at,
    )
    if not wrong_checkpoint:
        print("PASS: stale checkpoint fingerprint cannot authorize ready transition")
    else:
        failures.append("stale checkpoint fingerprint authorized ready transition")

    late_comments = [dict(comments[0], created_at="2026-08-29T09:01:00Z", updated_at="2026-08-29T09:01:00Z")]
    late_present, late_authorized = module.readiness_approval(
        late_comments, {"maintainer"}, "ua-agent-ready-approval",
        head, merge, checkpoint_hash, body_hash, ready_at,
    )
    if not late_present and not late_authorized:
        print("PASS: approval created after ready event cannot retroactively authorize transition")
    else:
        failures.append("late approval retroactively authorized ready transition")

    edited_old_comments = [dict(comments[0], updated_at="2026-08-29T09:01:00Z")]
    edited_present, edited_authorized = module.readiness_approval(
        edited_old_comments, {"maintainer"}, "ua-agent-ready-approval",
        head, merge, checkpoint_hash, body_hash, ready_at,
    )
    if not edited_present and not edited_authorized:
        print("PASS: pre-Ready comment edited after Ready cannot retroactively authorize transition")
    else:
        failures.append("edited old comment retroactively authorized Ready")

    timeline = [
        {"event": "committed", "sha": "1" * 40},
        {"event": "committed", "sha": "2" * 40},
        {"event": "ready_for_review", "created_at": ready_at},
    ]
    ready_head, observed_ready_at = module.readiness_state_from_timeline(timeline)
    if ready_head == "2" * 40 and observed_ready_at == ready_at:
        print("PASS: readiness binds to latest committed head and transition time")
    else:
        failures.append("ready transition did not bind to latest committed head/time")

    timeline.append({"event": "committed", "sha": "3" * 40})
    later_ready_head, _ = module.readiness_state_from_timeline(timeline)
    if later_ready_head == "2" * 40:
        print("PASS: later repository commit does not inherit prior ready authorization")
    else:
        failures.append("new commit incorrectly inherited prior ready authorization")

    timeline.append({"event": "convert_to_draft"})
    cleared_head, cleared_at = module.readiness_state_from_timeline(timeline)
    if cleared_head == "" and cleared_at == "":
        print("PASS: convert-to-draft clears ready authorization")
    else:
        failures.append("convert-to-draft did not clear ready authorization")

    original_request = module.request_json
    try:
        check_name = "Agent protocol / readiness authorization"
        workflow_path = ".github/workflows/change-coupling.yml"
        step_name = "Record successful head-bound readiness authorization"
        run_id = 123
        job_id = 456
        suite_id = 77
        requested: List[str] = []

        def good_request(url: str, token: str):
            requested.append(url)
            if "/commits/{}/check-runs".format(head) in url:
                return ({
                    "check_runs": [{
                        "name": check_name,
                        "conclusion": "success",
                        "completed_at": "2026-08-29T09:00:05Z",
                        "details_url": "https://github.com/owner/repo/actions/runs/{}/job/{}".format(run_id, job_id),
                        "check_suite": {"id": suite_id},
                        "app": {"slug": "github-actions"},
                    }]
                }, {})
            if url.endswith("/actions/runs/{}".format(run_id)):
                return ({
                    "path": workflow_path,
                    "event": "pull_request",
                    "head_sha": head,
                    "created_at": "2026-08-29T09:00:01Z",
                    "check_suite_id": suite_id,
                    "pull_requests": [{"number": 104}],
                }, {})
            if url.endswith("/actions/jobs/{}".format(job_id)):
                return ({
                    "run_id": run_id,
                    "name": check_name,
                    "conclusion": "success",
                    "steps": [{"name": step_name, "conclusion": "success"}],
                }, {})
            raise AssertionError("unexpected readiness provenance URL: {}".format(url))

        module.request_json = good_request
        if module.readiness_check_passed(
            "owner/repo", 104, head, ready_at, "token", check_name, workflow_path, step_name
        ):
            print("PASS: durable readiness requires exact Actions workflow/run/job/step provenance")
        else:
            failures.append("valid readiness workflow provenance was not recognized")
        if any("/commits/{}/check-runs".format(head) in url for url in requested):
            print("PASS: readiness checks are read from the PR head SHA, not synthetic merge SHA")
        else:
            failures.append("readiness evidence was not queried on the PR head SHA")

        def spoofed_workflow(url: str, token: str):
            value, headers = good_request(url, token)
            if url.endswith("/actions/runs/{}".format(run_id)) and isinstance(value, dict):
                value = dict(value)
                value["path"] = ".github/workflows/spoof.yml"
            return value, headers

        module.request_json = spoofed_workflow
        if not module.readiness_check_passed(
            "owner/repo", 104, head, ready_at, "token", check_name, workflow_path, step_name
        ):
            print("PASS: same-named success from another workflow cannot satisfy readiness")
        else:
            failures.append("same-named check from wrong workflow spoofed readiness")

        def wrong_step(url: str, token: str):
            value, headers = good_request(url, token)
            if url.endswith("/actions/jobs/{}".format(job_id)) and isinstance(value, dict):
                value = dict(value)
                value["steps"] = [{"name": "Not readiness authorization", "conclusion": "success"}]
            return value, headers

        module.request_json = wrong_step
        if not module.readiness_check_passed(
            "owner/repo", 104, head, ready_at, "token", check_name, workflow_path, step_name
        ):
            print("PASS: same-named job without protected readiness step cannot satisfy readiness")
        else:
            failures.append("wrong job implementation spoofed readiness")
    finally:
        module.request_json = original_request

    if failures:
        print("Feedback-context self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Feedback-context self-tests passed: 22 regression assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
