#!/usr/bin/env python3
"""Observable v11 behavior and retained evidence-boundary regressions."""

import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "score_repository_intelligence_ab.py"
SPEC = importlib.util.spec_from_file_location("ri_ab", SCRIPT)
E = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(E)


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.invocations = 0
        self.payload = '{"source_identity":{"digest":"synthetic-fixture"}}\n'
        self.study = {
            "protocol_version": 11, "study_id": "synthetic-only", "repository": "owner/repo",
            "repository_ref": "a" * 40, "default_branch": "main",
            "configuration": {"model": "test-model", "thinking": "high", "client": "test-client", "connector": "GitHub"},
            "assessor": "fixture assessor", "selection_note": "Synthetic regression tasks, not independent evidence",
            "frozen_before_execution": True, "smoke_evidence": "capture://smoke",
            "ri_surface_sha256": E.text_digest(self.payload), "context_metric": "repository_response_utf8_bytes",
            "follow_up_rule": "Separate new study only if the routing decision is unresolved",
            "tasks": [
                {"task_id": f"T{i:02d}", "prompt": f"Fixture routing question {i}", "source_reference": f"source://{i}",
                 "expected": ["Correct owner and its authoritative evidence"], "serious_errors": ["Treat research as normative authority"]}
                for i in range(1, 13)
            ],
        }
        self.runs = E.initial_records(self.study)
        self.runs["conditions_confirmed"] = True
        self.runs["source_window"] = {
            boundary: {"tool": "GitHub", "repository": "owner/repo", "branch": "main", "sha": "a" * 40, "evidence": f"capture://{boundary}"}
            for boundary in ("before", "after")
        }
        for index, run in enumerate(self.runs["runs"]):
            run.update(session_id=f"independent-session-{index}", evidence=f"capture://{index}", response=f"Visible answer {index}")
            run["events"] = [self.event(), self.event(resource="CONTRIBUTING.md")]
            if run["arm"] == E.TREATMENT:
                run["events"][0] = self.event(resource="assets/repository-intelligence/agent-context.json", response_bytes=len(self.payload.encode()), kind="ri_compact", delivery="verified", content_sha256=self.study["ri_surface_sha256"])

    def event(self, **changes):
        return {"tool": "GitHub", "operation": "fetch", "repository": "owner/repo", "resource": "AGENTS.md", "ref": self.study["repository_ref"], "response_bytes": 100, **changes}

    def arm_runs(self, arm):
        return [run for run in self.runs["runs"] if run["arm"] == arm]

    def scored(self):
        packet = E.blind_packet(self.study, self.runs, E.validate_runs(self.study, self.runs))
        packet.update(scorer="independent fixture scorer", scored_before_reveal=True)
        for entry in packet["responses"]:
            entry.update(quality=2, serious_error=False)
        return packet

    def quality(self, packet, run, value, serious=False):
        rid = E.text_digest(run["session_id"])
        entry = next(entry for entry in packet["responses"] if entry["response_id"] == rid)
        entry.update(quality=value, serious_error=serious)

    def evaluate(self, packet=None):
        return E.evaluate(self.study, self.runs, self.scored() if packet is None else packet)

    def invoke(self, command, packet=None):
        self.invocations += 1
        paths = {}
        for name, value in (("study", self.study), ("runs", self.runs), ("scores", packet)):
            paths[name] = self.root / f"{name}.json"
            paths[name].write_text(json.dumps(value), encoding="utf-8")
        output = self.root / f"output-{self.invocations}.json"
        args = [sys.executable, str(SCRIPT), command, "--study", str(paths["study"]), "--output", str(output)]
        if command != "init":
            args += ["--runs", str(paths["runs"])]
        if command == "score":
            args += ["--scores", str(paths["scores"])]
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        return result, json.loads(output.read_text()) if output.exists() else None

    def test_init_generates_24_counterbalanced_messages_without_answer_keys(self):
        result, output = self.invoke("init")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(output["runs"]), 24)
        self.assertEqual([run["arm"] for run in output["runs"][:4]], [E.CONTROL, E.TREATMENT, E.TREATMENT, E.CONTROL])
        self.assertNotIn("Correct owner and its authoritative evidence", json.dumps(output))
        self.assertEqual(output["study_sha256"], E.digest(self.study))

    def test_prepare_exports_only_blind_content_and_derived_identities(self):
        result, output = self.invoke("prepare")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(output["responses"]), 24)
        for marker in ("RI-AB-CONTROL", "RI-AB-TREATMENT", "events", "delivery", "session_id"):
            self.assertNotIn(marker, json.dumps(output))
        self.assertFalse(output["scored_before_reveal"])
        self.assertTrue(all(entry["quality"] is None for entry in output["responses"]))

    def test_equal_quality_and_cost_shows_no_benefit(self):
        result, report = self.invoke("score", self.scored())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["final_status"], "NO BENEFIT SHOWN")
        self.assertEqual(report["valid_pairs"], 12)

    def test_two_quality_wins_can_show_benefit(self):
        packet = self.scored()
        for run in self.arm_runs(E.CONTROL)[:2]:
            self.quality(packet, run, 0, serious=True)
        result, report = self.invoke("score", packet)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["final_status"], "BENEFIT SHOWN")
        self.assertEqual(report["removed_serious_errors"], 2)

    def test_efficiency_needs_actual_context_measurement(self):
        for run in self.arm_runs(E.CONTROL):
            run["events"].append(self.event(resource="README.md"))
        self.assertEqual(self.evaluate()["final_status"], "BENEFIT SHOWN")
        self.arm_runs(E.TREATMENT)[0]["events"][0]["response_bytes"] = None
        report = self.evaluate()
        self.assertEqual(report["final_status"], "NO BENEFIT SHOWN")
        self.assertIsNone(report["context_ratio_b_over_a"])

    def test_any_quality_loss_or_new_serious_error_reports_regression(self):
        for quality, serious in ((1, False), (0, True)):
            with self.subTest(quality=quality):
                packet = self.scored()
                self.quality(packet, self.arm_runs(E.TREATMENT)[0], quality, serious)
                self.assertEqual(self.evaluate(packet)["final_status"], "REGRESSION")

    def test_faster_incorrect_answers_and_partial_repairs_are_not_benefit(self):
        for run in self.arm_runs(E.CONTROL):
            run["events"].append(self.event(resource="README.md"))
        packet = self.scored()
        for entry in packet["responses"]:
            entry.update(quality=0, serious_error=True)
        self.assertEqual(self.evaluate(packet)["final_status"], "NO BENEFIT SHOWN")
        for run in self.arm_runs(E.TREATMENT)[:2]:
            self.quality(packet, run, 1)
        report = self.evaluate(packet)
        self.assertEqual(report["quality_wins"], 2)
        self.assertEqual(report["usable_quality_wins"], 0)
        self.assertEqual(report["final_status"], "NO BENEFIT SHOWN")

    def test_direct_owner_route_does_not_require_ri_or_claim_its_benefit(self):
        for run in self.arm_runs(E.TREATMENT):
            run["events"] = [self.event()]
        report = self.evaluate()
        self.assertEqual(report["valid_pairs"], 12)
        self.assertEqual(report["final_status"], "NO BENEFIT SHOWN")
        self.assertEqual(report["totals_over_valid_pairs"]["B"]["ri_attempts"], 0)

    def test_unverified_and_unavailable_delivery_allow_observed_fallback(self):
        for outcome in ("unverified", "unavailable"):
            with self.subTest(outcome=outcome):
                event = self.arm_runs(E.TREATMENT)[0]["events"][0]
                event.update(delivery=outcome, content_sha256="b" * 64)
                report = self.evaluate()
                self.assertEqual(report["valid_pairs"], 12)
                self.assertEqual(report["cases"][0]["B"]["ri_verified"], 0)
                self.assertEqual(report["cases"][0]["B"]["calls"], 2)

    def test_repeated_reads_are_charged_without_exactly_once_delivery_rule(self):
        run = self.arm_runs(E.TREATMENT)[0]
        run["events"].append(copy.deepcopy(run["events"][0]))
        report = self.evaluate()
        self.assertEqual(report["valid_pairs"], 12)
        self.assertEqual(report["cases"][0]["B"]["calls"], 3)

    def test_source_ref_and_transport_regressions_through_cli(self):
        original = copy.deepcopy(self.runs)
        mutations = [{"ref": "b" * 40}, {"ref": "other"}, {"ref": "main"}, {"ref": None}, {"observed_ref_sha": "b" * 40}, {"repository": "other/repo"}]
        for arm in (E.CONTROL, E.TREATMENT):
            for change in mutations:
                with self.subTest(arm=arm, change=change):
                    self.runs = copy.deepcopy(original)
                    self.arm_runs(arm)[0]["events"][0].update(change)
                    result, report = self.invoke("prepare")
                    self.assertEqual(result.returncode, 2, result.stderr)
                    self.assertIsNone(report)
        self.runs = original

    def test_locked_search_and_resolved_default_reads_remain_supported(self):
        for run in self.runs["runs"]:
            run["events"][-1].update(ref="main", observed_ref_sha="a" * 40)
            run["events"].append(self.event(operation="search", resource="routing", ref=None))
        self.assertEqual(self.evaluate()["valid_pairs"], 12)

    def test_normal_workflow_metadata_reads_are_supported_and_counted(self):
        run = self.arm_runs(E.TREATMENT)[0]
        run["events"].append(self.event(operation="inspect", resource="actions/jobs/123/logs", observed_ref_sha="a" * 40))
        self.assertEqual(self.evaluate()["cases"][0]["B"]["calls"], 3)
        run["events"][-1]["observed_ref_sha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "source evidence"):
            self.evaluate()

    def test_control_cannot_hide_ri_by_kind_path_or_identity(self):
        original = copy.deepcopy(self.runs)
        for change in ({"resource": "assets/repository-intelligence/agent-context.json", "kind": "source"}, {"content_sha256": self.study["ri_surface_sha256"], "kind": "source"}, {"phase": "study_infrastructure"}, {"resource": "assets/repository-intelligence/./agent-context.json"}):
            with self.subTest(change=change):
                self.runs = copy.deepcopy(original)
                self.arm_runs(E.CONTROL)[0]["events"][0].update(change)
                with self.assertRaises(ValueError):
                    self.evaluate()
        self.runs = original
        self.arm_runs(E.CONTROL)[0]["events"][0] = copy.deepcopy(self.arm_runs(E.TREATMENT)[0]["events"][0])
        self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")

    def test_local_transport_query_and_other_ri_cannot_support_acceptance(self):
        original = copy.deepcopy(self.runs)
        for change in ({"tool": "local_cli"}, {"operation": "query"}, {"resource": "assets/repository-intelligence/graph.json", "kind": "ri_other"}):
            with self.subTest(change=change):
                self.runs = copy.deepcopy(original)
                event = self.arm_runs(E.TREATMENT)[0]["events"][-1]
                event.update(change)
                self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")

    def test_verified_surface_hash_must_match_frozen_surface(self):
        self.arm_runs(E.TREATMENT)[0]["events"][0]["response_bytes"] = 0
        with self.assertRaisesRegex(ValueError, "zero response bytes"):
            self.evaluate()
        self.arm_runs(E.TREATMENT)[0]["events"][0]["response_bytes"] = 100
        self.arm_runs(E.TREATMENT)[0]["events"][0]["content_sha256"] = "b" * 64
        with self.assertRaisesRegex(ValueError, "verified RI content"):
            self.evaluate()

    def test_mutable_or_short_study_refs_rejected(self):
        for ref in ("main", "a" * 7, "g" * 40):
            with self.subTest(ref=ref):
                self.study["repository_ref"] = ref
                result, _ = self.invoke("init")
                self.assertEqual(result.returncode, 2)

    def test_invalid_measurements_rejected_for_both_metrics_and_arms(self):
        original = copy.deepcopy(self.runs)
        for metric in ("input_tokens", "unavailable"):
            self.study["context_metric"] = metric
            for arm in (E.CONTROL, E.TREATMENT):
                for value in (-1, True, "100", 1.5, float("nan"), float("inf")):
                    with self.subTest(metric=metric, arm=arm, value=value):
                        self.runs = copy.deepcopy(original)
                        self.runs["study_sha256"] = E.digest(self.study)
                        self.arm_runs(arm)[0]["input_tokens"] = value
                        with self.assertRaises(ValueError):
                            self.evaluate()
        self.runs = original
        self.runs["study_sha256"] = E.digest(self.study)
        self.arm_runs(E.CONTROL)[0]["events"][0]["response_bytes"] = -1
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_zero_null_and_unbounded_token_comparisons_are_valid_json(self):
        self.study["context_metric"] = "input_tokens"
        self.runs["study_sha256"] = E.digest(self.study)
        for run in self.runs["runs"]:
            run["input_tokens"] = 0
        self.assertEqual(self.evaluate()["context_ratio_b_over_a"], 1)
        self.arm_runs(E.TREATMENT)[0]["input_tokens"] = 1
        report = self.evaluate()
        self.assertIsNone(report["context_ratio_b_over_a"])
        json.dumps(report, allow_nan=False)
        self.arm_runs(E.TREATMENT)[0]["input_tokens"] = None
        self.assertIsNone(self.evaluate()["context_ratio_b_over_a"])

    def test_blind_packet_rejects_metadata_and_changed_content(self):
        for container, field, value in (("packet", "arm", "A"), ("packet", "tool_events", []), ("entry", "delivery", "verified"), ("entry", "quality", {"value": 2, "arm": "B"}), ("entry", "expected", ["Changed rubric"]), ("entry", "response", "Changed response")):
            with self.subTest(container=container, field=field):
                packet = self.scored()
                target = packet if container == "packet" else packet["responses"][0]
                target[field] = value
                result, report = self.invoke("score", packet)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertIsNone(report)

    def test_missing_duplicate_unblinded_or_inconsistent_scores_rejected(self):
        for mutation in ("missing", "duplicate", "unblinded", "serious-with-two"):
            with self.subTest(mutation=mutation):
                packet = self.scored()
                if mutation == "missing":
                    packet["responses"].pop()
                elif mutation == "duplicate":
                    packet["responses"].append(copy.deepcopy(packet["responses"][0]))
                elif mutation == "unblinded":
                    packet["scored_before_reveal"] = False
                else:
                    packet["responses"][0]["serious_error"] = True
                with self.assertRaises(ValueError):
                    self.evaluate(packet)

    def test_study_and_run_edits_after_freeze_are_detected(self):
        packet = self.scored()
        self.runs["runs"][0]["response"] += " edited"
        with self.assertRaisesRegex(ValueError, "frozen evidence"):
            self.evaluate(packet)
        self.study["tasks"][0]["prompt"] += " edited"
        with self.assertRaisesRegex(ValueError, "study changed"):
            self.evaluate()

    def test_all_invalid_empty_and_partial_samples_write_inconclusive(self):
        for run in self.runs["runs"]:
            run["deviations"] = ["client configuration changed"]
        result, report = self.invoke("score", self.scored())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(report["final_status"], "INCONCLUSIVE")
        self.assertIsNone(report["connector_ratio_b_over_a"])
        self.runs["runs"] = self.runs["runs"][:2]
        for run in self.runs["runs"]:
            run["deviations"] = []
        self.assertEqual(self.evaluate()["valid_pairs"], 1)
        self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")
        self.runs["runs"] = []
        self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")

    def test_source_window_and_session_parity_failures_cannot_pass(self):
        for field, bad_value in (("sha", "b" * 40), ("tool", "local_cli"), ("branch", "other")):
            with self.subTest(field=field):
                window = copy.deepcopy(self.runs["source_window"])
                self.runs["source_window"]["after"][field] = bad_value
                self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")
                self.runs["source_window"] = window
        self.runs["conditions_confirmed"] = False
        self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")

    def test_duplicate_sessions_extra_hints_and_order_changes_are_detected(self):
        original = copy.deepcopy(self.runs)
        self.runs["runs"][1]["session_id"] = self.runs["runs"][0]["session_id"]
        with self.assertRaises(ValueError):
            self.evaluate()
        self.runs = copy.deepcopy(original)
        self.runs["runs"][0]["submitted_message"] += " Extra hint"
        self.assertEqual(self.evaluate()["final_status"], "INCONCLUSIVE")
        self.runs = original
        self.runs["runs"].reverse()
        with self.assertRaises(ValueError):
            self.evaluate()

    def test_output_refuses_to_overwrite_frozen_evidence(self):
        path = self.root / "frozen.json"
        path.write_text("original", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            E.write_json(path, {})
        self.assertEqual(path.read_text(), "original")


if __name__ == "__main__":
    unittest.main()
