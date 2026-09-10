#!/usr/bin/env python3
"""Blind scoring, paired analysis, and final classification for RI A/B."""

from _ri_ab_base import (
    CONTROL, PREFLIGHT, PRIMARY_ARMS, PROTOCOL_VERSION, TREATMENT, exact_fields, load, med,
    rat, req, s256f, valid_sha256,
)
from _ri_ab_events import run_valid, score_total
from _ri_ab_prereg import validate_prereg

def validate_blind_scores(path, record, p, evidence):
    cfg = record.get("blind_scoring")
    req(isinstance(cfg, dict), "run record blind_scoring block required")
    req(valid_sha256(cfg.get("scoring_bundle_sha256")), "blind scoring bundle SHA-256 required")
    req(s256f(path) == cfg["scoring_bundle_sha256"], "blind scoring bundle hash mismatch")
    bundle = load(path, "blind scoring bundle")
    # Closed schemas keep arm-revealing metadata out of the assessor's bundle,
    # including metadata nested inside otherwise valid responses or scores.
    exact_fields(bundle, {
        "schema_version", "study_id", "scorer_identity", "scoring_evidence_reference",
        "scoring_completed_before_arm_reveal", "arm_labels_present",
        "pilot_scoring_key_sha256", "confirmatory_scoring_key_sha256", "responses",
    }, "blind scoring bundle")
    req(bundle.get("schema_version") == 1 and bundle.get("study_id") == p["study_id"], "blind scoring bundle protocol/study mismatch")
    req(bundle.get("scoring_completed_before_arm_reveal") is True, "blind scoring must finish before arm reveal")
    req(bundle.get("arm_labels_present") is False, "blind scoring bundle must not contain arm labels")
    req(isinstance(bundle.get("scorer_identity"), str) and bundle["scorer_identity"], "blind scorer identity required")
    req(isinstance(bundle.get("scoring_evidence_reference"), str) and bundle["scoring_evidence_reference"], "blind scoring evidence reference required")
    req(bundle.get("pilot_scoring_key_sha256") == p["pilot"]["scoring_key_sha256"], "blind scoring Pilot key mismatch")
    req(bundle.get("confirmatory_scoring_key_sha256") == p["confirmatory"]["scoring_key_sha256"], "blind scoring Confirmatory key mismatch")
    entries = bundle.get("responses")
    req(isinstance(entries, list) and len(entries) == 48, "blind scoring bundle must contain exactly 48 responses")
    by_id = {}
    for entry in entries:
        exact_fields(entry, {"blind_response_id", "task_id", "model_response_sha256", "scores"}, "blind scoring response")
        response_id = entry.get("blind_response_id")
        req(isinstance(response_id, str) and response_id and response_id not in by_id, "blind_response_id duplicate or missing in blind scoring bundle")
        req(isinstance(entry.get("task_id"), str) and entry["task_id"], "blind scoring task_id required")
        req(valid_sha256(entry.get("model_response_sha256")), "blind scoring response hash required")
        by_id[response_id] = entry
    seen_run_ids = set()
    score_map = {}
    for wave_key, cases_key in (("pilot", "pilot_cases"), ("confirmatory", "confirmatory_cases")):
        key_map = evidence["keys"][wave_key]
        cases = record.get(cases_key)
        req(isinstance(cases, list), f"{cases_key} required")
        for case in cases:
            task_id = case.get("task_id")
            for run in case.get("runs", []):
                rid = run.get("blind_response_id")
                req(rid not in seen_run_ids, "blind_response_id must be unique across primary runs")
                seen_run_ids.add(rid)
                req(rid in by_id, "primary run missing from blind scoring bundle")
                entry = by_id[rid]
                req(entry["task_id"] == task_id, "blind scoring task_id does not match run")
                req(entry["model_response_sha256"] == run.get("model_response_sha256"), "blind scoring response hash does not match run response")
                score_total(entry.get("scores"), key_map[task_id])
                score_map[rid] = entry["scores"]
    req(set(by_id) == seen_run_ids, "blind scoring bundle contains responses outside primary runs")
    return score_map


def eval_case(case, pack, key, wave, p, treatment, score_map):
    task_id = case.get("task_id")
    req(task_id in pack["ids"] and case.get("corpus_class") == pack["classes"][task_id], "run case mismatch")
    order = pack["orders"][task_id]
    req(case.get("order") == order, "run order mismatch")
    runs = case.get("runs")
    req(isinstance(runs, list) and len(runs) == 2 and [run.get("arm") for run in runs] == order, "execution order mismatch")
    by_arm = {run["arm"]: run for run in runs}
    req(set(by_arm) == PRIMARY_ARMS, "pair requires both arms")
    invalid, derived = {}, {}
    for arm in (CONTROL, TREATMENT):
        invalid[arm], derived[arm] = run_valid(by_arm[arm], arm, wave, task_id, pack["prompt_text"][task_id], pack["prompts"][task_id], order, p, treatment)
    if invalid[CONTROL] or invalid[TREATMENT]:
        return {"task_id": task_id, "corpus_class": case["corpus_class"], "valid": False, "invalid_reasons": invalid}
    a_scores = score_map[by_arm[CONTROL]["blind_response_id"]]
    b_scores = score_map[by_arm[TREATMENT]["blind_response_id"]]
    a_total, a_serious, _ = score_total(a_scores, key)
    b_total, b_serious, b_values = score_total(b_scores, key)
    state = "A-serious/B-no-serious" if a_serious and not b_serious else "A-no-serious/B-serious" if b_serious and not a_serious else "both-serious" if a_serious else "neither-serious"
    quality = all(value >= p["positive_reversal_quality_gate"]["minimum_each_applicable_dimension"] for value in b_values.values())
    metric = p["context_volume"]["metric"]
    volume_a = derived[CONTROL]["repo_bytes"] if metric == "repository_response_utf8_bytes" else by_arm[CONTROL].get("measured_input_tokens") if metric == "input_tokens" else None
    volume_b = derived[TREATMENT]["repo_bytes"] if metric == "repository_response_utf8_bytes" else by_arm[TREATMENT].get("measured_input_tokens") if metric == "input_tokens" else None
    return {
        "task_id": task_id,
        "corpus_class": case["corpus_class"],
        "valid": True,
        "correctness_delta_b_minus_a": b_total - a_total,
        "serious_error_outcome": state,
        "qualifying_positive_reversal": state == "A-serious/B-no-serious" and quality,
        "connector_ratio_b_over_a": rat(derived[TREATMENT]["calls"], derived[CONTROL]["calls"]),
        "context_volume_ratio_b_over_a": None if volume_a is None or volume_b is None else rat(volume_b, volume_a),
        "equal_correctness_pair": a_total == b_total and a_serious == b_serious,
        "derived_infrastructure_calls_a": derived[CONTROL]["infrastructure_calls"],
        "derived_infrastructure_calls_b": derived[TREATMENT]["infrastructure_calls"],
    }


def eval_wave(name, cases, pack, keys, p, treatment, score_map):
    req(isinstance(cases, list) and len(cases) == 12, f"{name} needs 12 cases")
    by_id = {case.get("task_id"): case for case in cases}
    req(set(by_id) == set(pack["ids"]), f"{name} task IDs mismatch")
    evaluated = [eval_case(by_id[task_id], pack, keys[task_id], name, p, treatment, score_map) for task_id in pack["ids"]]
    valid = [case for case in evaluated if case["valid"]]
    ecological = [case for case in valid if case["corpus_class"] == "ecological"]
    all_valid = len(valid) == 12 and len(ecological) == 6
    positive = sum(case.get("qualifying_positive_reversal") is True for case in valid)
    ecological_positive = sum(case.get("qualifying_positive_reversal") is True for case in ecological)
    reverse = sum(case.get("serious_error_outcome") == "A-no-serious/B-serious" for case in valid)
    ecological_reverse = sum(case.get("serious_error_outcome") == "A-no-serious/B-serious" for case in ecological)
    deltas = [case["correctness_delta_b_minus_a"] for case in ecological]
    nonreg = all_valid and med(deltas) >= p["ecological_correctness_non_regression"]["minimum_per_wave"] and ecological_reverse == 0
    connector_ratios = [case["connector_ratio_b_over_a"] for case in ecological]
    connector_median = med(connector_ratios)
    connector_gate = all_valid and connector_median <= p["connector_cost_gate"]["acceptable_median_ratio_b_over_a"] and sum(value > p["connector_cost_gate"]["high_overhead_ratio_threshold"] for value in connector_ratios) <= p["connector_cost_gate"]["acceptable_high_overhead_case_count"]
    connector_gain = all_valid and nonreg and reverse == 0 and connector_median <= p["connector_interaction_gain_rule"]["maximum_median_ratio_b_over_a_per_wave"]
    volume_ratios = [case["context_volume_ratio_b_over_a"] for case in ecological]
    # all([]) is true, but an empty sample has no median or acceptance evidence.
    complete_volume = bool(volume_ratios) and p["context_volume"]["metric"] != "unavailable" and all(value is not None for value in volume_ratios)
    volume_gate = all_valid and complete_volume and med(volume_ratios) <= p["context_volume"]["maximum_median_ratio_b_over_a_per_wave"] and sum(value > p["context_volume"]["high_overhead_ratio_threshold"] for value in volume_ratios) <= p["context_volume"]["acceptable_high_overhead_case_count"]
    return {
        "name": name,
        "cases": evaluated,
        "all_pairs_valid": all_valid,
        "qualifying_positive_reversals": positive,
        "qualifying_ecological_positive_reversals": ecological_positive,
        "reverse_serious_reversals": reverse,
        "ecological_correctness_non_regression_passed": nonreg,
        "ecological_median_connector_ratio": connector_median,
        "connector_cost_gate_passed": connector_gate,
        "connector_interaction_gain_passed": connector_gain,
        "ecological_median_context_volume_ratio": med(volume_ratios) if complete_volume else None,
        "context_volume_gate_passed": volume_gate,
        "orientation_efficiency_passed": connector_gain and volume_gate,
    }


def final(pilot, confirmatory, p):
    all_valid = pilot["all_pairs_valid"] and confirmatory["all_pairs_valid"]
    positive = pilot["qualifying_positive_reversals"] + confirmatory["qualifying_positive_reversals"]
    reverse = pilot["reverse_serious_reversals"] + confirmatory["reverse_serious_reversals"]
    rule = p["final_decision_rule"]["engineering_acceptance_correctness"]
    thresholds = confirmatory["qualifying_positive_reversals"] >= rule["minimum_confirmatory_positive_reversals"] and confirmatory["qualifying_ecological_positive_reversals"] >= rule["minimum_confirmatory_ecological_positive_reversals"] and positive >= rule["minimum_combined_positive_reversals"] and reverse <= rule["maximum_combined_reverse_serious_reversals"] and pilot["ecological_correctness_non_regression_passed"] and confirmatory["ecological_correctness_non_regression_passed"]
    cost_ok = pilot["connector_cost_gate_passed"] and confirmatory["connector_cost_gate_passed"]
    correctness_acceptance = all_valid and thresholds and cost_ok
    connector_signal = all_valid and reverse == 0 and pilot["connector_interaction_gain_passed"] and confirmatory["connector_interaction_gain_passed"]
    efficiency_acceptance = connector_signal and pilot["orientation_efficiency_passed"] and confirmatory["orientation_efficiency_passed"]
    regression = all_valid and (reverse > 0 or not pilot["ecological_correctness_non_regression_passed"] or not confirmatory["ecological_correctness_non_regression_passed"])
    if not all_valid:
        status = "INCONCLUSIVE"
    elif regression:
        status = "REGRESSION"
    elif correctness_acceptance and efficiency_acceptance:
        status = "ENGINEERING ACCEPTANCE — CORRECTNESS + ORIENTATION EFFICIENCY"
    elif correctness_acceptance:
        status = "ENGINEERING ACCEPTANCE — CORRECTNESS"
    elif thresholds and not cost_ok:
        status = "CORRECTNESS SIGNAL / COST NOT ACCEPTED"
    elif efficiency_acceptance:
        status = "ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY"
    elif connector_signal:
        status = "ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY"
    elif pilot["qualifying_positive_reversals"]:
        status = "NOT CONFIRMED"
    else:
        status = "NO INCREMENTAL VALUE SHOWN"
    return {
        "all_primary_pairs_valid": all_valid,
        "combined_qualifying_positive_reversals": positive,
        "combined_reverse_serious_reversals": reverse,
        "engineering_acceptance_correctness": correctness_acceptance,
        "engineering_acceptance_orientation_efficiency": efficiency_acceptance,
        "connector_interaction_signal": connector_signal,
        "inferential_significance_claimed": False,
        "regression": regression,
        "final_status": status,
    }


def validate_run_record(record, p):
    req(record.get("protocol_version") == PROTOCOL_VERSION and record.get("study_id") == p["study_id"], "run record protocol/study mismatch")
    preflight = record.get("execution_preflight")
    req(isinstance(preflight, dict) and preflight.get("eligible_to_start_primary") is True, "run record preflight/eligibility missing")
    for field in PREFLIGHT:
        req(preflight.get(field) is True, f"run record preflight {field} must be true")
    prereg_preflight = p["execution_preflight"]
    req(preflight.get("smoke_evidence_reference") == prereg_preflight["smoke_evidence_reference"], "run record smoke evidence reference mismatch")
    req(preflight.get("smoke_evidence_sha256") == prereg_preflight["smoke_evidence_sha256"], "run record smoke evidence SHA-256 mismatch")


def evaluate(p, record, evidence, score_map):
    validate_prereg(p)
    validate_run_record(record, p)
    treatment = evidence["treatment_surface"]
    pilot = eval_wave("PILOT", record.get("pilot_cases"), evidence["packs"]["pilot"], evidence["keys"]["pilot"], p, treatment, score_map)
    confirmatory = eval_wave("CONFIRMATORY", record.get("confirmatory_cases"), evidence["packs"]["confirmatory"], evidence["keys"]["confirmatory"], p, treatment, score_map)
    return {
        "evaluation_version": 8,
        "protocol_version": PROTOCOL_VERSION,
        "study_id": p["study_id"],
        "repository_ref": p["repository_ref"],
        "evidence_verification": {
            "sampling_frame_bound_to_complete_eligible_pool": True,
            "selection_replayed": True,
            "arm_randomization_replayed": True,
            "pool_materialization_matches_selected_prompts": True,
            "cross_wave_normalized_prompt_overlap_rejected": True,
            "treatment_surface_identity_verified_from_bytes": True,
            "treatment_delivery_completeness_derived_from_byte_ranges": True,
            "source_state_lock_derived_from_branch_tip_events": True,
            "blind_response_scoring_verified": True,
            "protocol_owned_acceptance_floors_enforced": True,
            "strong_scoring_keys_verified": True,
        },
        "pilot": pilot,
        "confirmatory": confirmatory,
        "final_conclusion": final(pilot, confirmatory, p),
    }
