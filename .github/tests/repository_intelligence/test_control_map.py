#!/usr/bin/env python3
"""Map transport must retain the accepted producer's facts and impact boundary."""
import sys
import tempfile
import unittest
from pathlib import Path

import test_repository_intelligence as fixtures

sys.path.insert(0, str(fixtures.REPOSITORY_ROOT / ".github/scripts"))
import build_repository_control_map as builder

RI = builder.intelligence


class ControlMapTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="ua-map-test-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        fixtures.materialize_repository(self.root)
        self.contract = RI.load_contract(self.root / ".github/policy/repository-intelligence-contract.json")
        self.surface = self.root / self.contract["compact_surface_path"]
        self.refresh()
        self.head = fixtures.init_git(self.root)

    def refresh(self):
        fixtures.write(self.surface, RI.serialize_json(RI.materialize_agent_surface(RI.build_projection(self.root), self.contract)))

    def test_transport_preserves_graph_and_producer_impact(self):
        data = builder.build_payload(self.root, self.head)
        projection, _ = RI.projection_from_git_ref(self.root, self.head, self.contract)
        graph = RI.materialize_graph_view(projection)
        self.assertEqual(data["projection"], graph)
        self.assertEqual(data["source_state"], {"kind": "accepted", "ref": self.head})
        self.assertEqual(data["live_overlay"]["state"], "unavailable")
        for path, actual in data["impact_by_path"].items():
            self.assertEqual(actual, RI.impact_for_paths(graph, [path]))

    def test_local_edits_are_preview_and_staleness_fails(self):
        self.assertEqual(builder.build_payload(self.root)["source_state"], {"kind": "preview", "ref": self.head})
        source = self.root / "AGENTS.md"
        source.write_text(source.read_text() + "\nLocal change.\n")
        with self.assertRaisesRegex(ValueError, "stale"):
            builder.build_payload(self.root)
        self.refresh()
        self.assertEqual(builder.build_payload(self.root)["source_state"], {"kind": "preview", "ref": None})

    def test_published_snapshot_ignores_local_data_and_rejects_stale_committed_surface(self):
        original = builder.build_payload(self.root, self.head)
        fixtures.write(self.root / ".git/info/exclude", "private/\n")
        fixtures.write(self.root / "private/AGENTS.md", "# Uncommitted instructions\n")
        self.assertEqual(builder.build_payload(self.root, self.head), original)
        self.refresh()
        head = fixtures.commit_all(self.root, "surface contains an ignored input")
        with self.assertRaisesRegex(ValueError, "stale"):
            builder.build_payload(self.root, head)

    def test_published_ref_and_interpretation_are_bound(self):
        with self.assertRaisesRegex(ValueError, "exact checkout commit"):
            builder.build_payload(self.root, "main")
        path = self.root / ".github/scripts/repository_intelligence.py"
        path.write_text(path.read_text() + "\n# local interpretation edit\n")
        with self.assertRaisesRegex(ValueError, "interpretation differs"):
            builder.build_payload(self.root, self.head)


if __name__ == "__main__":
    unittest.main()
