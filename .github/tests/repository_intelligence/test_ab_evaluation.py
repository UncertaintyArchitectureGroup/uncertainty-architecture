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
        self.tmp = tempfile.TemporaryDirectory(prefix="ua-ri-ab-v7-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.ref = "a" * 40
        self.identity = {
            "mode": "connector_compact_surface",
            "identifier": "assets/repository-intelligence/agent-context.json",
            "git_blob_sha": "b" * 40,
            "content_sha256": "c" * 64,
            "source_identity": "source-identity-v7",
        }
        self.paths, self.packs, self.keys = {}, {}, {}
        self._make_evidence()
        self.prereg = self._make_prereg("unavailable")
        self.record = self._make_record()

    @staticmethod
    def _write(path, value):
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    @staticmethod
    def _digest(path):
        return hashlib.sha256(path.read_bytes()).hexdigest()

    @staticmethod
    def _order(index):
        return [evaluator.CONTROL, evaluator.TREATMENT] if index % 2 else [evaluator.TREATMENT, evaluator.CONTROL]

    def _make_evidence(self):
        pilot = [
            ["exact-owner-recovery", "canonical-term-synonym-pressure"],
            ["near-synonym-source-review", "overlapping-artifact-refinement"],
            ["legitimate-new-artifact", "impact-validation-routing"],
            ["research-authority-separation", "ukrainian-or-paraphrased-routing"],
            ["accepted-proposed-relation-change"],
            ["branch-behind-target"],
        ]
        confirm = [
            ["accepted-proposed-relation-change"], ["branch-behind-target"],
            ["producer-schema-self-change"], ["candidate-data-boundary"],
            ["shared-structural-hub"], ["stale-materialization-fallback"],
        ]
        for key, wave, prefix, scenarios in (
            ("pilot", "PILOT", "P", pilot), ("confirmatory", "CONFIRMATORY", "C", confirm)
        ):
            cases, scoring = [], []
            for index in range(1, 13):
                corpus = "stress" if index <= 6 else "ecological"
                task = f"{prefix}{index:02d}"
                cases.append({
                    "task_id": task,
                    "task_family_id": f"{prefix}-FAMILY-{index:02d}",
                    "corpus_class": corpus,
                    "ecological_source_id": None if corpus == "stress" else f"{prefix}-SOURCE-{index:02d}",
                    "scenario_families": scenarios[index - 1] if corpus == "stress" else [],
                    "planned_order": self._order(index),
                    "prompt": f"{wave} held-out task {index}",
                })
                scoring.append({
                    "task_id": task,
                    "companion_validation_applicable": index % 3 == 0,
                    "expected_evidence": ["owner.md"],
                })
            pack = {"schema_version": 2, "wave": wave, "cases": cases}
            key_data = {"schema_version": 2, "wave": wave, "cases": scoring}
            ppath, kpath = self.root / f"{key}-prompts.json", self.root / f"{key}-key.json"
            self._write(ppath, pack)
            self._write(kpath, key_data)
            self.paths[f"{key}_prompts"], self.paths[f"{key}_key"] = ppath, kpath
            self.packs[key], self.keys[key] = pack, key_data

    def _commitments(self, key):
        pack = self.packs[key]
        eco = sorted(c["ecological_source_id"] for c in pack["cases"] if c["ecological_source_id"])
        orders = [{"task_id": c["task_id"], "planned_order": c["planned_order"]} for c in pack["cases"]]
        return {
            "selected_ecological_ids_sha256": evaluator.canonical_sha256(eco),
            "arm_order_plan_sha256": evaluator.canonical_sha256(orders),
        }

    def _preflight(self):
        result = {field: True for field in evaluator.PREFLIGHT_TRUE_FIELDS}
        result["smoke_evidence_reference"] = "issue:RI-AB-SMOKE"
        return result

    def _make_prereg(self, metric):
        waves = {}
        for key in ("pilot", "confirmatory"):
            waves[key] = {
                "case_count": 12, "stress_cases": 6, "ecological_cases": 6,
                "prompts_sha256": self._digest(self.paths[f"{key}_prompts"]),
                "scoring_key_sha256": self._digest(self.paths[f"{key}_key"]),
                "arm_order_seed_sha256": "d" * 64,
                "ecological_selection_seed_sha256": "e" * 64,
                **self._commitments(key),
            }
        return {
            "protocol_version": 7, "study_id": "RI-AB-TEST", "repository_ref": self.ref,
            "execution_policy": "always_run_pilot_and_confirmatory",
            "source_state_lock": {
                "mode": "stable_default_branch_window", "expected_default_branch_tip_sha": self.ref,
                "repository_mutations_prohibited_during_primary": True,
                "pre_run_tip_check_required": True, "post_run_tip_check_required": True,
                "ordinary_default_branch_search_allowed": True,
            },
            "execution_preflight": self._preflight(),
            "isolation_requirements": {
                "conversation_fresh": True, "memory_enabled": False, "project_context_present": False,
                "prior_repo_context_available": False, "unavailable_is_acceptable_for_primary": False,
                "previous_arm_output_exposed": False,
                "corrective_scoring_feedback_before_pair_complete": False,
                "future_wave_material_exposed": False, "hidden_benchmark_material_exposed": False,
            },
            "model_family": "GPT-test", "thinking_configuration": "fixed-test",
            "client_environment": "test-client", "connector": "GitHub",
            "treatment_delivery": {
                "mode": "connector_compact_surface", "must_remain_constant_across_primary_runs": True,
                "complete_payload_verified": True, "truncation_check_passed": True,
                "aid_identity": dict(self.identity),
            },
            "mandatory_scenario_families": sorted(evaluator.MANDATORY_SCENARIO_FAMILIES),
            "confirmatory_required_scenario_families": sorted(evaluator.DEFAULT_CONFIRMATORY_CRITICAL_FAMILIES),
            "pilot": waves["pilot"], "confirmatory": waves["confirmatory"],
            "positive_reversal_quality_gate": {"minimum_each_applicable_dimension": 1},
            "ecological_correctness_non_regression": {
                "minimum_per_wave": 0, "maximum_reverse_serious_error_reversals_per_wave": 0,
            },
            "connector_cost_gate": {
                "acceptable_median_ratio_b_over_a": 1.5, "high_overhead_ratio_threshold": 2.0,
                "acceptable_high_overhead_case_count": 2,
            },
            "connector_interaction_gain_rule": {
                "maximum_median_ratio_b_over_a_per_wave": 0.8,
                "maximum_reverse_serious_error_reversals": 0,
            },
            "context_volume": {
                "metric": metric, "measurement_must_be_exact_not_estimated": True,
                "required_for_orientation_efficiency_go": True,
                "maximum_median_ratio_b_over_a_per_wave": 1.0,
                "high_overhead_ratio_threshold": 2.0, "acceptable_high_overhead_case_count": 2,
            },
            "final_decision_rule": {"demonstrated_correctness_go": {
                "minimum_confirmatory_positive_reversals": 1,
                "minimum_confirmatory_ecological_positive_reversals": 1,
                "maximum_confirmatory_reverse_reversals": 0,
                "minimum_combined_positive_reversals": 3,
                "maximum_combined_reverse_reversals": 0,
            }},
        }

    def _scores(self, companion, serious=False):
        return {
            "owner_routing": 2, "evidence_sufficiency": 2, "authority_discipline": 2,
            "companion_validation": 2 if companion else None, "decision_quality": 2,
            "total_applicable_correctness": 10 if companion else 8,
            "serious_routing_error": serious,
        }

    def _run(self, run_id, arm, companion, calls=10, bytes_=100):
        treatment = arm == evaluator.TREATMENT
        return {
            "run_id": run_id, "arm": arm, "valid": None, "invalid_reason": None,
            "conversation_fresh": True, "memory_enabled": False, "project_context_present": False,
            "prior_repo_context_available": False, "previous_arm_output_exposed": False,
            "corrective_scoring_feedback_before_pair_complete": False,
            "future_wave_material_exposed": False, "hidden_benchmark_material_exposed": False,
            "connector_state_equal": True, "source_state_pre_sha": self.ref,
            "source_state_post_sha": self.ref, "source_state_protocol_violation": False,
            "model_family": "GPT-test", "thinking_configuration": "fixed-test",
            "client_environment": "test-client", "connector": "GitHub", "protocol_violations": [],
            "total_connector_calls": calls,
            "treatment_delivery_status": "delivered" if treatment else "not-applicable",
            "treatment_surface_verified": True if treatment else "not-applicable",
            "complete_treatment_payload_verified": True if treatment else "not-applicable",
            "treatment_aid_identity": dict(self.identity) if treatment else None,
            "ri_aid_accessed": treatment, "ri_payload_bytes": 200000 if treatment else 0,
            "ri_logical_operations_or_evidence": ["compact-surface"] if treatment else [],
            "ri_prohibited_aid_accessed": False, "full_graph_view_accessed": False,
            "repository_control_map_accessed": False,
            "repository_response_utf8_bytes": bytes_, "measured_input_tokens": bytes_,
            "scores": self._scores(companion),
        }

    def _wave(self, key, calls_a=10, calls_b=7, bytes_a=100, bytes_b=90):
        applicable = {c["task_id"]: c["companion_validation_applicable"] for c in self.keys[key]["cases"]}
        result = []
        for case in self.packs[key]["cases"]:
            task, order = case["task_id"], case["planned_order"]
            runs = {
                evaluator.CONTROL: self._run(task + "-A", evaluator.CONTROL, applicable[task], calls_a, bytes_a),
                evaluator.TREATMENT: self._run(task + "-B", evaluator.TREATMENT, applicable[task], calls_b, bytes_b),
            }
            result.append({"task_id": task, "corpus_class": case["corpus_class"], "order": list(order), "runs": [runs[a] for a in order]})
        return result

    def _make_record(self):
        preflight = self._preflight()
        preflight["eligible_to_start_primary"] = True
        return {
            "protocol_version": 7, "study_id": "RI-AB-TEST",
            "preregistered": {
                "repository_ref": self.ref, "treatment_delivery_mode": "connector_compact_surface",
                "treatment_aid_identity": dict(self.identity),
                "context_volume_metric": self.prereg["context_volume"]["metric"],
                "model_family": "GPT-test", "thinking_configuration": "fixed-test",
                "client_environment": "test-client", "connector": "GitHub",
            },
            "execution_preflight": preflight,
            "pilot_cases": self._wave("pilot"), "confirmatory_cases": self._wave("confirmatory"),
        }

    def evidence(self):
        return evaluator.verify_evidence(self.prereg, self.paths)

    def evaluate(self):
        return evaluator.evaluate(self.prereg, self.record, self.evidence())

    @staticmethod
    def arms(case):
        return {run["arm"]: run for run in case["runs"]}

    def rewrite_pack(self, key):
        self._write(self.paths[f"{key}_prompts"], self.packs[key])
        self.prereg[key]["prompts_sha256"] = self._digest(self.paths[f"{key}_prompts"])
        self.prereg[key].update(self._commitments(key))

    def test_control_ri_access_invalidates_pair(self):
        run = self.arms(self.record["pilot_cases"][0])[evaluator.CONTROL]
        run["ri_aid_accessed"], run["ri_payload_bytes"] = True, 1
        self.assertEqual(self.evaluate()["final_conclusion"]["final_status"], "INCONCLUSIVE")

    def test_treatment_identity_mismatch_invalidates_pair(self):
        self.arms(self.record["pilot_cases"][0])[evaluator.TREATMENT]["treatment_aid_identity"]["git_blob_sha"] = "f" * 40
        self.assertFalse(self.evaluate()["pilot"]["all_pairs_valid"])

    def test_model_mismatch_invalidates_pair(self):
        self.arms(self.record["pilot_cases"][0])[evaluator.TREATMENT]["model_family"] = "other"
        self.assertFalse(self.evaluate()["pilot"]["all_pairs_valid"])

    def test_smoke_preflight_must_pass(self):
        self.prereg["execution_preflight"]["smoke_passed"] = False
        with self.assertRaisesRegex(ValueError, "smoke_passed"):
            self.evaluate()

    def test_memory_enabled_invalidates_primary(self):
        self.arms(self.record["pilot_cases"][0])[evaluator.CONTROL]["memory_enabled"] = True
        self.assertEqual(self.evaluate()["final_conclusion"]["final_status"], "INCONCLUSIVE")

    def test_source_state_tip_mismatch_invalidates_primary(self):
        self.arms(self.record["pilot_cases"][0])[evaluator.CONTROL]["source_state_post_sha"] = "f" * 40
        self.assertFalse(self.evaluate()["pilot"]["all_pairs_valid"])

    def test_pair_order_must_match_frozen_plan(self):
        self.record["pilot_cases"][0]["runs"].reverse()
        with self.assertRaisesRegex(ValueError, "execution order"):
            self.evaluate()

    def test_task_family_overlap_is_rejected(self):
        self.packs["confirmatory"]["cases"][0]["task_family_id"] = self.packs["pilot"]["cases"][0]["task_family_id"]
        self.rewrite_pack("confirmatory")
        with self.assertRaisesRegex(ValueError, "task_family_id"):
            self.evidence()

    def test_ecological_source_overlap_is_rejected(self):
        self.packs["confirmatory"]["cases"][6]["ecological_source_id"] = self.packs["pilot"]["cases"][6]["ecological_source_id"]
        self.rewrite_pack("confirmatory")
        with self.assertRaisesRegex(ValueError, "ecological_source_id"):
            self.evidence()

    def test_missing_mandatory_coverage_is_rejected(self):
        for pack in self.packs.values():
            for case in pack["cases"]:
                case["scenario_families"] = [s for s in case["scenario_families"] if s != "ukrainian-or-paraphrased-routing"]
        self.rewrite_pack("pilot")
        self.rewrite_pack("confirmatory")
        with self.assertRaisesRegex(ValueError, "miss mandatory"):
            self.evidence()

    def test_confirmatory_critical_coverage_is_rejected(self):
        for case in self.packs["confirmatory"]["cases"]:
            case["scenario_families"] = [s for s in case["scenario_families"] if s != "candidate-data-boundary"]
            if case["corpus_class"] == "stress" and not case["scenario_families"]:
                case["scenario_families"] = ["exact-owner-recovery"]
        self.packs["pilot"]["cases"][0]["scenario_families"].append("candidate-data-boundary")
        self.rewrite_pack("pilot")
        self.rewrite_pack("confirmatory")
        with self.assertRaisesRegex(ValueError, "Confirmatory corpus misses critical"):
            self.evidence()

    def test_companion_applicability_is_frozen(self):
        task = self.packs["pilot"]["cases"][2]["task_id"]
        case = next(c for c in self.record["pilot_cases"] if c["task_id"] == task)
        run = self.arms(case)[evaluator.TREATMENT]
        run["scores"]["companion_validation"] = None
        run["scores"]["total_applicable_correctness"] = 8
        with self.assertRaisesRegex(ValueError, "must be scored"):
            self.evaluate()

    def test_low_quality_non_serious_b_is_not_positive_reversal(self):
        arms = self.arms(self.record["pilot_cases"][0])
        arms[evaluator.CONTROL]["scores"]["serious_routing_error"] = True
        arms[evaluator.TREATMENT]["scores"]["decision_quality"] = 0
        arms[evaluator.TREATMENT]["scores"]["total_applicable_correctness"] = 6
        report = self.evaluate()
        self.assertFalse(report["pilot"]["cases"][0]["qualifying_positive_reversal"])

    def test_correctness_go_requires_confirmatory_ecological_reversal(self):
        for case in self.record["pilot_cases"][:2] + self.record["confirmatory_cases"][:1]:
            self.arms(case)[evaluator.CONTROL]["scores"]["serious_routing_error"] = True
            for run in case["runs"]:
                run["total_connector_calls"] = 10
        self.assertFalse(self.evaluate()["final_conclusion"]["demonstrated_correctness_go"])

    def test_correctness_go_with_confirmatory_ecological_support(self):
        for case in [self.record["pilot_cases"][0], self.record["pilot_cases"][1], self.record["confirmatory_cases"][6]]:
            self.arms(case)[evaluator.CONTROL]["scores"]["serious_routing_error"] = True
        for wave in ("pilot_cases", "confirmatory_cases"):
            for case in self.record[wave]:
                for run in case["runs"]:
                    run["total_connector_calls"] = 10
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["demonstrated_correctness_go"])
        self.assertEqual(report["final_conclusion"]["final_status"], "DEMONSTRATED CORRECTNESS GO")

    def test_reverse_serious_error_is_regression(self):
        self.arms(self.record["confirmatory_cases"][0])[evaluator.TREATMENT]["scores"]["serious_routing_error"] = True
        self.assertEqual(self.evaluate()["final_conclusion"]["final_status"], "REGRESSION")

    def test_connector_gain_is_not_orientation_efficiency_without_context(self):
        report = self.evaluate()
        self.assertTrue(report["pilot"]["connector_interaction_gain_passed"])
        self.assertFalse(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])

    def test_context_overhead_blocks_orientation_efficiency(self):
        self.prereg["context_volume"]["metric"] = "repository_response_utf8_bytes"
        self.record["preregistered"]["context_volume_metric"] = "repository_response_utf8_bytes"
        for wave in ("pilot_cases", "confirmatory_cases"):
            for case in self.record[wave]:
                arms = self.arms(case)
                arms[evaluator.CONTROL]["repository_response_utf8_bytes"] = 100
                arms[evaluator.TREATMENT]["repository_response_utf8_bytes"] = 300
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["demonstrated_connector_interaction_gain"])
        self.assertFalse(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])

    def test_orientation_efficiency_requires_connector_and_context_gates(self):
        self.prereg["context_volume"]["metric"] = "repository_response_utf8_bytes"
        self.record["preregistered"]["context_volume_metric"] = "repository_response_utf8_bytes"
        report = self.evaluate()
        self.assertTrue(report["final_conclusion"]["demonstrated_orientation_efficiency_go"])

    def test_prompt_overlap_is_rejected(self):
        self.packs["confirmatory"]["cases"][0]["prompt"] = self.packs["pilot"]["cases"][0]["prompt"]
        self.rewrite_pack("confirmatory")
        with self.assertRaisesRegex(ValueError, "prompt text overlaps"):
            self.evidence()


if __name__ == "__main__":
    unittest.main()
