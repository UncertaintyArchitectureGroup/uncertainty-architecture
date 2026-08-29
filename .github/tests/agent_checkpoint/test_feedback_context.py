#!/usr/bin/env python3
"""Regression tests for deterministic maintainer GitHub-feedback watermarking."""

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
        "issues": [
            {
                "id": 1,
                "user": user("maintainer"),
                "author_association": "OWNER",
                "created_at": "2026-08-29T08:00:00Z",
                "updated_at": "2026-08-29T08:00:00Z",
                "body": "do the opposite",
            },
            {
                "id": 2,
                "user": user("visitor"),
                "author_association": "NONE",
                "created_at": "2026-08-29T08:01:00Z",
                "updated_at": "2026-08-29T08:01:00Z",
                "body": "untrusted noise",
            },
        ],
        "reviews": [
            {
                "id": 3,
                "user": user("reviewer"),
                "author_association": "COLLABORATOR",
                "submitted_at": "2026-08-29T08:02:00Z",
                "state": "CHANGES_REQUESTED",
                "body": "scope is wrong",
            }
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

    def fake_paged(url: str, token: str):
        if "/issues/" in url:
            return fixtures["issues"]
        if url.endswith("/reviews?per_page=100"):
            return fixtures["reviews"]
        return fixtures["pull-comments"]

    module.paged_list = fake_paged
    trusted = ["OWNER", "MEMBER", "COLLABORATOR"]
    first = module.feedback_sha256("owner/repo", 104, "token", trusted)
    second = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if first == second:
        print("PASS: feedback watermark is deterministic")
    else:
        failures.append("feedback watermark changed without input change")

    fixtures["issues"][1]["body"] = "different untrusted noise"
    if module.feedback_sha256("owner/repo", 104, "token", trusted) == first:
        print("PASS: untrusted commenter does not change maintainer feedback watermark")
    else:
        failures.append("untrusted feedback changed the watermark")

    fixtures["issues"][0]["body"] = "edited maintainer correction"
    edited = module.feedback_sha256("owner/repo", 104, "token", trusted)
    if edited != first:
        print("PASS: edited trusted feedback invalidates watermark")
    else:
        failures.append("trusted feedback edit did not change watermark")

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
        failures.append("trusted feedback deletion did not change watermark")

    if failures:
        print("Feedback-context self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Feedback-context self-tests passed: 5 regression assertions.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
