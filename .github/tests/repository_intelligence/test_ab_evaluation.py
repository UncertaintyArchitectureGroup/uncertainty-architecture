#!/usr/bin/env python3
"""Regression tests for the Repository Intelligence A/B evaluator."""

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / ".github/scripts"))
import score_repository_intelligence_ab as evaluator


class RepositoryIntelligenceABEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ua-ri-ab-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.repository_ref = "a" * 40
        self.paths = {}
        self.packs = {}
        for key, wave, prefix in (("pilot", "PILOT", "P"), ("confirmatory", "CONFIRMATORY", "C")):
            pack = {
                "schema_version": 1,
                "wave": wave,
                "cases": [
                    {
                        "task_id": "{}{:02d}".format(prefix, index),
                        "corpus_class": "stress" if index <= 6 else "ecological",
                        "ecological_source_id": None if index <= 6 else "{}-E{:02d}".format(prefix, index - 6),
                        "prompt": "{} held-out prompt {}".format(wave, index),
                    }
                    for index in range(1, 13)
                ],
            }
            scoring_key = {
                "schema_version": 1,
                "wave": wave,
                "cases": [
                    {"task_id": case["task_id"], "expected_evidence": ["owner.md"]}
                    for case in pack["cases"]
                ],
            }
            prompt_path = self.root / (key + "-prompts.json")
            key_path = self.root / (key + "-key.json")
            self.write_json(prompt_path, pack)
            self.write_json(key_path, scoring_key)
            self.paths[key + "_prompts"] = prompt_path
            self.paths[key + "_key"] = key_path
            self.packs[key] = pack
        self.preregistration = self.make_preregistration("unavailable")
        self.run_record = self.make_run_record()

    @staticmethod
    def write_json(path, value):
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @staticmethod
    def digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    def make_preregistration(self, context_metric):
        return {
            "protocol_version": 6,
            "study_id": "RI-AB-TEST",
            "repository_ref": self.repository_ref,
            "execution_policy": "always_run_pilot_and_confirmatory",
            "source_state_lock": {
                "mode": "stable_default_branch_window",
                "expected_default_branch_tip_sha": self.repository_ref,
                "repository_mutations_prohibited_during_primary": True,
                "pre_run_tip_check_required": True,
                "post_run_tip_check_required": True,
                "ordinary_default_branch_search_allowed": True,
            },
            "isolation_requirements": {
                "conversation_fresh": True,
                "memory_enabled": False,
                "project_context_present": False,
                "prior_repo_context_available": False,
                "unavailable_is_acceptable_for_primary": False,
                "previous_arm_output_exposed": False,
            },
            "treatment_delivery": {
                "mode": "connector_compact_surface",
                "must_remain_constant_across_primary_runs": True,
            },
            "pilot": {
                "case_count": 12,
                "stress_cases": 6,
                "ecological_cases": 6,
                "prompts_sha256": self.digest(self.paths["pilot_prompts"]),
                "scoring_key_sha256": self.digest(self.paths["pilot_key"]),
            },
            "confirmatory": {
                "case_count": 12,
                "stress_cases": 6,
                "ecological_cases": 6,
                "prompts_sha256": self.digest(self.paths["confirmatory_prompts"]),
                "scoring_key_sha256": self.digest(self.paths["confirmatory_key"]),
            },
            "ecological_correctness_non_regression": {
                "minimum_per_wave": 0,
                "maximum_reverse_serious_error_reversals_per_wave": 0,
            },
            "connector_cost_gate": {
                "acceptable_median_ratio_b_over_a": 1.5,
                "high_overhead_ratio_threshold": 2.0,
                "acceptable_high_overhead_case_count": 2,
            },
            "connector_interaction_gain_rule": {
                "maximum_median_ratio_b_over_a_per_wave": 0.8,
                "maximum_reverse_serious_error_reversals": 0,
            },
            "context_volume": {
                "metric": context_metric,
                "measurement_must_be_exact_not_estimated": True,
                "required_for_orientation_efficiency_go": True,
                "maximum_median_ratio_b_over_a_per_wave": 1.0,
                "high_overhead_ratio_threshold": 2.0,
                "acceptable_high_overhead_case_count": 2,
            },
            "final_decision_rule": {
                "demonstrated_correctness_go": {
                    "minimum_confirmatory_positive_reversals": 1,
                    "maximum_confirmatory_reverse_reversals": 0,
                    "minimum_combined_positive_reversals": 3,
                    "maximum_combined_reverse_reversals": 0,
                }
            },
        }

    def make_run(self, run_id, arm, connector_calls, context_bytes=100, serious=False):
        treatment = arm == evaluator.TREATMENT
        return {
            "run_id": run_id,
            "arm": arm,
            "valid": None,
            "invalid_reason": None,
            "conversation_fresh": True,
            "memory_enabled": False,
            "project_context_present": False,
            "prior_repo_context_available": False,
            "previous_arm_output_exposed": False,
            "connector_state_equal": True,
            "source_state_pre_sha": self.repository_ref,
            "source_state_post_sha": self.repository_ref,
            "source_state_protocol_violation": False,
            "total_connector_calls": connector_calls,
            "treatment_delivery_status": "delivered" if treatment else "not-applicable",
            "treatment_surface_verified": True if treatment else "not-applicable",
            "repository_response_utf8_bytes": context_bytes,
            "measured_input_tokens": context_bytes,
            "scores": {
                "owner_routing": 2,
                "evidence_sufficiency": 2,
                "authority_discipline": 2,
                "companion_validation": None,
                "decision_quality": 2,
                "total_applicable_correctness": 8,
                "serious_routing_error": serious,
            },
        }

    def make_wave_cases(self, key, calls_a=10, calls_b=7, bytes_a=100, bytes_b=90):
        cases = []
        for case in self.packs[key]["cases"]:
            task_id = case["task_id"]
            cases.append(
                {
                    "task_id": task_id,
                    "corpus_class": case["corpus_class"],
                    "runs": [
                        self.make_run(task_id + "-A", evaluator.CONTROL, calls_a, bytes_a),
                        self.make_run(task_id + "-B", evaluator.TREATMENT, calls_b, bytes_b),
                    ],
                }
            )
        return cases

    def make_run_record(self):
        return {
            "protocol_version": 6,
            "study_id": "RI-AB-TEST",
            "preregistered": {
                "repository_ref": self.repository_ref,
                "treatment_delivery_mode": "connector_compact_surface",
                "context_volume_metric": self.preregistration["context_volume"]["metric"],
            },
            "pilot_cases": self.make_wave_cases("pilot"),
            "confirmatory_cases": self.make_wave_cases("confirmatory"),
        }

    def evidence(self):
        return evaluator.verify_evidence(self.preregistration, self.paths)

    def evaluate(self):
        return evaluator.evaluate(self.preregistration, self.run_record, self.evidence())

    def set_context_metric(self, metric, bytes_a=100, bytes_b=90):
        self.preregistration = self.make_preregistration(metric)
        self.run_record = self.make_run_record()
        self.run_record["preregistered"]["context_volume_metric"] = metric
        for wave in ("pilot_cases", "confirmatory_cases"):
            for case in self.run_record[wave]:
                by_arm = {run["arm"]: run for run in case["runs"]}
                by_arm[evaluator.CONTROL]["repository_response_utf8_bytes"] = bytes_a
                by_arm[evaluator.TREATMENT]["repository_response_utf8_bytes"] = bytes_b
                by_arm[evaluator.CONTROL]["measured_input_tokens"] = bytes_a
                by_arm[evaluator.TREATMENT]["measured_input_tokens"] = bytes_b

    def test_memory_enabled_invalidates_primary_study(self):
        self.run_record["pilot_cases"][0]["runs"][0]["memory_enabled"] = True
        report = self.evaluate()
        self.assertFalse(report["pilot"]["all_pairs_valid"])
        self.assertEqual(report["final_conclusion"]["final_status"], "INCONCLUSIVE")

    def test_source_state_tip_mismatch_invalidates_primary_study(self):
        self.run_record["pilot_cases"][0]["runs"][0]["source_state_post_sha"] = "b" * 40
        report = self.evaluate()
        self.assertFalse(report["pilot"]["all_pairs_valid"])
        self.assertEqual(report["final_conclusion"]["final_status"], "INCONCLUSIVE")

    def test_connector_gain_is_not_orientation_efficiency_when_context_unavailable(self):
        report = self.evaluate()
        self.assertTrue(report["pilot"]["connector_interaction_gain_passed"])
        self.assertEqual(report["pilot"]["context_volume_status"], "unavailable")
        self.assertFalse(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])
        self.assertEqual(report["final_conclusion"]["final_status"], "DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY")

    def test_context_overhead_blocks_orientation_efficiency(self):
        self.set_context_metric("repository_response_utf8_bytes", bytes_a=100, bytes_b=300)
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["demonstrated_connector_interaction_gain"])
        self.assertEqual(report["pilot"]["context_volume_status"], "fail")
        self.assertFalse(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])
        self.assertEqual(report["final_conclusion"]["final_status"], "DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY")

    def test_orientation_efficiency_requires_connector_and_context_gates(self):
        self.set_context_metric("repository_response_utf8_bytes", bytes_a=100, bytes_b=80)
        report = self.evaluate()
        self.assertTrue(report["pilot"]["orientation_efficiency_passed"])
        self.assertTrue(report["confirmatory"]["orientation_efficiency_passed"])
        self.assertTrue(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])
        self.assertEqual(report["final_conclusion"]["final_status"], "DEMONSTRATED ORIENTATION EFFICIENCY GO")

    def test_correctness_go_requires_confirmatory_and_combined_reversals(self):
        for wave in ("pilot_cases", "confirmatory_cases"):
            for case in self.run_record[wave]:
                for run in case["runs"]:
                    run["total_connector_calls"] = 10
        for case in self.run_record["pilot_cases"][:2] + self.run_record["confirmatory_cases"][:1]:
            by_arm = {run["arm"]: run for run in case["runs"]}
            by_arm[evaluator.CONTROL]["scores"]["serious_routing_error"] = True
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["demonstrated_correctness_go"])
        self.assertFalse(report["final_conclusion"]["demonstrated_connector_interaction_gain"])
        self.assertEqual(report["final_conclusion"]["final_status"], "DEMONSTRATED CORRECTNESS GO")

    def test_reverse_serious_error_is_regression(self):
        case = self.run_record["confirmatory_cases"][0]
        by_arm = {run["arm"]: run for run in case["runs"]}
        by_arm[evaluator.TREATMENT]["scores"]["serious_routing_error"] = True
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["regression"])
        self.assertEqual(report["final_conclusion"]["final_status"], "REGRESSION")

    def test_prompt_overlap_is_rejected_even_with_updated_hash(self):
        confirmatory = json.loads(self.paths["confirmatory_prompts"].read_text())
        confirmatory["cases"][0]["prompt"] = self.packs["pilot"]["cases"][0]["prompt"]
        self.write_json(self.paths["confirmatory_prompts"], confirmatory)
        self.preregistration["confirmatory"]["prompts_sha256"] = self.digest(self.paths["confirmatory_prompts"])
        with self.assertRaisesRegex(ValueError, "overlaps"):
            self.evidence()

    def test_hash_mismatch_is_rejected(self):
        self.preregistration["pilot"]["prompts_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self.evidence()

    def test_prefilled_total_cannot_disagree_with_dimension_scores(self):
        self.run_record["pilot_cases"][0]["runs"][0]["scores"]["total_applicable_correctness"] = 9
        with self.assertRaisesRegex(ValueError, "total_applicable_correctness"):
            self.evaluate()


if __name__ == "__main__":
    unittest.main()
