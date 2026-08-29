#!/usr/bin/env python3
"""Fetch live PR state and deterministic maintainer-feedback evidence for agent checkpoint validation."""

import argparse
import hashlib
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/agent-checkpoint-contract.json"
API_ROOT = "https://api.github.com"


def load_contract(path: Path) -> Dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("contract_version") != 1:
        raise ValueError("unsupported contract_version: {!r}".format(value.get("contract_version")))
    return value


def request_json(url: str, token: str) -> Tuple[object, Dict[str, str]]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(token),
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "ua-agent-checkpoint",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read().decode("utf-8"))
        headers = {key.lower(): value for key, value in response.headers.items()}
    return data, headers


def next_link(link_header: str) -> Optional[str]:
    for item in (link_header or "").split(","):
        parts = [part.strip() for part in item.split(";")]
        if len(parts) < 2 or 'rel="next"' not in parts[1:]:
            continue
        url = parts[0]
        if url.startswith("<") and url.endswith(">"):
            return url[1:-1]
    return None


def paged_list(url: str, token: str) -> List[Dict[str, object]]:
    items: List[Dict[str, object]] = []
    current: Optional[str] = url
    while current:
        value, headers = request_json(current, token)
        if not isinstance(value, list):
            raise ValueError("expected list response from {}".format(current))
        items.extend(item for item in value if isinstance(item, dict))
        current = next_link(headers.get("link", ""))
    return items


def body_digest(value: object) -> str:
    text = value if isinstance(value, str) else ""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def is_trusted_feedback(item: Dict[str, object], trusted: Iterable[str]) -> bool:
    association = str(item.get("author_association") or "")
    if association not in set(trusted):
        return False
    user = item.get("user")
    if not isinstance(user, dict):
        return False
    login = str(user.get("login") or "")
    user_type = str(user.get("type") or "")
    return bool(login) and not login.endswith("[bot]") and user_type != "Bot"


def feedback_record(kind: str, item: Dict[str, object]) -> Dict[str, object]:
    user = item.get("user") if isinstance(item.get("user"), dict) else {}
    created = item.get("submitted_at") or item.get("created_at") or ""
    updated = item.get("updated_at") or item.get("dismissed_at") or created
    return {
        "kind": kind,
        "id": int(item.get("id") or 0),
        "author": str(user.get("login") or ""),
        "author_association": str(item.get("author_association") or ""),
        "state": str(item.get("state") or ""),
        "created_at": str(created or ""),
        "updated_at": str(updated or ""),
        "body_sha256": body_digest(item.get("body")),
    }


def feedback_sha256(repository: str, pr_number: int, token: str, trusted: Iterable[str]) -> str:
    """Hash feedback whose workflow events are attached to the PR merge/head lifecycle.

    Top-level PR conversation comments are deliberately excluded. GitHub emits
    `issue_comment` workflows on the default-branch ref/SHA, so those comments
    remain a semantic feedback surface for the agent but are not represented as
    a deterministic PR-head merge-gate signal.
    """
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    endpoints = (
        ("review", "{}/repos/{}/pulls/{}/reviews?per_page=100".format(API_ROOT, encoded_repo, pr_number)),
        ("review-comment", "{}/repos/{}/pulls/{}/comments?per_page=100".format(API_ROOT, encoded_repo, pr_number)),
    )
    records: List[Dict[str, object]] = []
    for kind, url in endpoints:
        for item in paged_list(url, token):
            if is_trusted_feedback(item, trusted):
                records.append(feedback_record(kind, item))
    records.sort(key=lambda item: (str(item["kind"]), int(item["id"])))
    canonical = json.dumps(records, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def ready_head_sha_from_timeline(events: Iterable[Dict[str, object]]) -> str:
    """Return the last committed PR head that was explicitly marked ready.

    `ready_for_review` timeline events have no commit_id on GitHub, so readiness
    is bound to the last `committed` event observed before the latest ready
    transition. A later `convert_to_draft` clears readiness. A later repository
    commit does not change the returned SHA, causing the current head to differ
    and therefore requiring Draft again.
    """
    last_commit = ""
    ready_head = ""
    ready_active = False
    for event in events:
        kind = str(event.get("event") or "")
        if kind == "committed":
            sha = str(event.get("sha") or "")
            if sha:
                last_commit = sha
        elif kind == "ready_for_review":
            ready_head = last_commit
            ready_active = bool(ready_head)
        elif kind == "convert_to_draft":
            ready_head = ""
            ready_active = False
    return ready_head if ready_active else ""


def fetch_context(
    repository: str,
    pr_number: int,
    merge_sha: str,
    event_name: str,
    event_action: str,
    token: str,
    contract: Dict[str, object],
) -> Dict[str, object]:
    encoded_repo = "/".join(urllib.parse.quote(part, safe="") for part in repository.split("/"))
    pr_url = "{}/repos/{}/pulls/{}".format(API_ROOT, encoded_repo, pr_number)
    pr, _ = request_json(pr_url, token)
    if not isinstance(pr, dict):
        raise ValueError("pull request response is not an object")

    base = pr.get("base") if isinstance(pr.get("base"), dict) else {}
    head = pr.get("head") if isinstance(pr.get("head"), dict) else {}
    base_ref = str(base.get("ref") or "")
    if not base_ref:
        raise ValueError("pull request has no base ref")

    branch_url = "{}/repos/{}/branches/{}".format(
        API_ROOT, encoded_repo, urllib.parse.quote(base_ref, safe="")
    )
    branch, _ = request_json(branch_url, token)
    if not isinstance(branch, dict) or not isinstance(branch.get("commit"), dict):
        raise ValueError("base branch response lacks commit data")
    base_tip_sha = str(branch["commit"].get("sha") or "")

    api_merge_sha = str(pr.get("merge_commit_sha") or "")
    if api_merge_sha and api_merge_sha != merge_sha:
        raise ValueError(
            "checked-out tested merge {} does not match GitHub PR merge {}".format(
                merge_sha, api_merge_sha
            )
        )

    timeline_url = "{}/repos/{}/issues/{}/timeline?per_page=100".format(
        API_ROOT, encoded_repo, pr_number
    )
    timeline = paged_list(timeline_url, token)
    trusted = [str(item) for item in contract.get("trusted_feedback_author_associations", [])]
    labels = [
        str(item.get("name"))
        for item in pr.get("labels", [])
        if isinstance(item, dict) and item.get("name")
    ]
    return {
        "repository": repository,
        "pr_number": pr_number,
        "body": str(pr.get("body") or ""),
        "diff_base_sha": str(base.get("sha") or ""),
        "base_ref": base_ref,
        "base_tip_sha": base_tip_sha,
        "head_sha": str(head.get("sha") or ""),
        "merge_sha": merge_sha,
        "draft": bool(pr.get("draft")),
        "ready_head_sha": ready_head_sha_from_timeline(timeline),
        "event_name": event_name,
        "event_action": event_action,
        "feedback_sha256": feedback_sha256(repository, pr_number, token, trusted),
        "labels": sorted(labels),
        "pr_author": str((pr.get("user") or {}).get("login") if isinstance(pr.get("user"), dict) else ""),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--pr-number", required=True, type=int)
    parser.add_argument("--merge-sha", required=True)
    parser.add_argument("--event-name", default="")
    parser.add_argument("--event-action", default="")
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("Missing GITHUB_TOKEN", file=sys.stderr)
        return 2
    try:
        contract = load_contract(args.contract.resolve())
        context = fetch_context(
            args.repository,
            args.pr_number,
            args.merge_sha,
            args.event_name,
            args.event_action,
            token,
            contract,
        )
    except Exception as exc:
        print("Agent-checkpoint context error: {}".format(exc), file=sys.stderr)
        return 2
    args.output.write_text(json.dumps(context, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "Agent-checkpoint context collected: PR #{}, base-tip {}, head {}, merge {}, ready-head {}, feedback {}.".format(
            context["pr_number"], context["base_tip_sha"], context["head_sha"],
            context["merge_sha"], context["ready_head_sha"], context["feedback_sha256"],
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
