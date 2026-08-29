#!/usr/bin/env python3
"""Regression tests for deterministic PR feedback and readiness context."""

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

    timeline = [
        {"event": "committed", "sha": "1" * 40},
        {"event": "committed", "sha": "2" * 40},
        {"event": "ready_for_review"},
    ]
    if module.ready_head_sha_from_timeline(timeline) == "2" * 40:
        print("PASS: readiness binds to the latest committed head before ready transition")
    else:
        failures.append("ready transition did not bind to latest committed head")

    timeline.append({"event": "committed", "sha": "3" * 40})
    if module.ready_head_sha_from_timeline(timeline) == "2" * 40:
        print("PASS: later repository commit does not inherit prior ready authorization")
    else:
        failures.append("new commit incorrectly inherited prior ready authorization")

    timeline.append({"event": "convert_to_draft"})
    if module.ready_head_sha_from_timeline(timeline) == "":
        print("PASS: convert-to-draft clears ready authorization")
    else:
        failures.append("convert-to-draft did not clear ready authorization")

    if failures:
        print("Feedback-context self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Feedback-context self-tests passed: 9 regression assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
