#!/usr/bin/env python3
"""Adapt the existing projection for Quartz; preserve producer-owned semantics."""

import argparse
import json
import re
import sys
from pathlib import Path

import repository_intelligence as intelligence

ROOT = Path(__file__).resolve().parents[2]


def build_payload(root, accepted_ref=None):
    contract = intelligence.load_contract(root / ".github/policy/repository-intelligence-contract.json")
    surface_path = root / contract["compact_surface_path"]
    head = intelligence.git_text(root, ["rev-parse", "HEAD"])
    if accepted_ref:
        if not re.fullmatch(r"[0-9a-f]{40}", accepted_ref) or accepted_ref != head:
            raise ValueError("Published map requires an exact checkout commit")
        matches, paths = intelligence.local_interpretation_matches_ref(root, head, contract)
        if not matches:
            raise ValueError("Executing interpretation differs from published commit: " + ", ".join(paths))
        # Git objects avoid ignored files, index flags and filesystem indirection
        # masquerading as accepted content. The workflow selects accepted main.
        projection, _boundary = intelligence.projection_from_git_ref(root, head, contract)
        surface = intelligence.materialize_agent_surface(projection, contract)
        committed = intelligence.git_bytes(root, ["cat-file", "blob", head + ":" + contract["compact_surface_path"]])
        if json.loads(committed) != surface:
            raise ValueError("Committed compact surface is stale for published Git snapshot")
        state = {"kind": "accepted", "ref": head}
    else:
        surface = intelligence.load_fresh_surface(root, contract, surface_path)
        projection = intelligence.build_projection(root)
        # Local edits may describe facts absent at HEAD. Source links use main
        # only as fallback in that case and the inspector states the limitation.
        committed_projection, _boundary = intelligence.projection_from_git_ref(root, head, contract)
        same_state = projection == committed_projection
        state = {"kind": "preview", "ref": head if same_state else None}
    graph = intelligence.materialize_graph_view(projection)
    paths = sorted({node["path"] for node in graph["graph"]["nodes"] if node.get("path")})
    return {
        "map_version": 1,
        "source_state": state,
        "projection": graph,
        "impact_by_path": {path: intelligence.impact_for_paths(graph, [path]) for path in paths},
        "validation_by_path": {
            path: intelligence.validation_plan(surface, path, owner_paths=[path]) for path in paths
        },
        "live_overlay": {"state": "unavailable", "reason": "Live PR state is not connected in this build."},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--accepted-ref")
    args = parser.parse_args(argv)
    try:
        value = build_payload(args.root.resolve(), args.accepted_ref)
        print(intelligence.serialize_json(value), end="")
        return 0
    except (OSError, ValueError) as exc:
        print("Control Map build failed: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
