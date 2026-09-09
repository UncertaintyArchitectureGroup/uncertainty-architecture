#!/usr/bin/env python3
"""Mechanically evaluate the preregistered Repository Intelligence A/B study.

The evaluator never scores model reasoning or free-form answer quality. A human
assessor enters repository-verifiable dimension scores and serious-error labels
against the frozen key. This script then verifies commitments and recomputes run
validity, paired outcomes, cost/volume gates, and the final classification.
"""

import argparse
import hashlib
import json
import math
import re
import statistics
import sys
from pathlib import Path

PROTOCOL_VERSION = 6
CONTROL = "RI-AB-CONTROL"
TREATMENT = "RI-AB-TREATMENT"
PRIMARY_ARMS = {CONTROL, TREATMENT}
WAVES = (("pilot", "PILOT"), ("confirmatory", "CONFIRMATORY"))
SCORE_FIELDS = (
    "owner_routing",
    "evidence_sufficiency",
    "authority_discipline",
    "decision_quality",
)
OPTIONAL_SCORE_FIELD = "companion_validation"
CONTEXT_METRICS = {"repository_response_utf8_bytes", "input_tokens", "unavailable"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def load_json(path, label):
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("{} is not readable JSON: {}".format(label, exc)) from exc
    if not isinstance(value, dict):
        raise ValueError("{} must be a JSON object".format(label))
    return value


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def ratio(numerator, denominator):
    if denominator == 0:
        return 1.0 if numerator == 0 else math.inf
    return numerator / denominator


def median(values):
    return statistics.median(values) if values else None


def normalized_prompt(text):
    return " ".join(text.split())


def validate_preregistration(preregistration):
    require(preregistration.get("protocol_version") == PROTOCOL_VERSION, "Unsupported preregistration protocol_version")
    repository_ref = preregistration.get("repository_ref")
    require(isinstance(repository_ref, str) and SHA_RE.fullmatch(repository_ref), "repository_ref must be a 40-character lowercase commit SHA")
    require(preregistration.get("execution_policy") == "always_run_pilot_and_confirmatory", "execution_policy must keep both primary waves")

    lock = preregistration.get("source_state_lock")
    require(isinstance(lock, dict), "source_state_lock is required")
    require(lock.get("mode") == "stable_default_branch_window", "source_state_lock mode must be stable_default_branch_window")
    require(lock.get("expected_default_branch_tip_sha") == repository_ref, "source_state_lock tip must equal repository_ref")
    require(lock.get("repository_mutations_prohibited_during_primary") is True, "primary study must freeze repository mutations")
    require(lock.get("pre_run_tip_check_required") is True and lock.get("post_run_tip_check_required") is True, "source-state pre/post checks are required")
    require(lock.get("ordinary_default_branch_search_allowed") is True, "Control must preserve ordinary live-GitHub search")

    isolation = preregistration.get("isolation_requirements")
    require(isinstance(isolation, dict), "isolation_requirements are required")
    expected_isolation = {
        "conversation_fresh": True,
        "memory_enabled": False,
        "project_context_present": False,
        "prior_repo_context_available": False,
        "unavailable_is_acceptable_for_primary": False,
        "previous_arm_output_exposed": False,
    }
    for field, expected in expected_isolation.items():
        require(isolation.get(field) is expected, "isolation requirement {} must be {!r}".format(field, expected))

    delivery = preregistration.get("treatment_delivery")
    require(isinstance(delivery, dict), "treatment_delivery is required")
    require(delivery.get("mode") in {"connector_compact_surface", "local_cli", "dedicated_adapter"}, "Unknown Treatment Delivery Mode")
    require(delivery.get("must_remain_constant_across_primary_runs") is True, "Treatment Delivery Mode must remain constant")

    for key, wave_name in WAVES:
        wave = preregistration.get(key)
        require(isinstance(wave, dict), "{} preregistration is required".format(key))
        require(wave.get("case_count") == 12, "{} must have 12 cases".format(wave_name))
        require(wave.get("stress_cases") == 6 and wave.get("ecological_cases") == 6, "{} must have 6 stress and 6 ecological cases".format(wave_name))
        for field in ("prompts_sha256", "scoring_key_sha256"):
            value = wave.get(field)
            require(isinstance(value, str) and SHA256_RE.fullmatch(value), "{}.{} must be a SHA-256".format(key, field))

    cost = preregistration.get("connector_cost_gate")
    require(isinstance(cost, dict), "connector_cost_gate is required")
    require(isinstance(cost.get("acceptable_median_ratio_b_over_a"), (int, float)), "connector cost median threshold is required")
    require(isinstance(cost.get("high_overhead_ratio_threshold"), (int, float)), "connector high-overhead threshold is required")
    require(type(cost.get("acceptable_high_overhead_case_count")) is int, "connector high-overhead count is required")

    interaction = preregistration.get("connector_interaction_gain_rule")
    require(isinstance(interaction, dict), "connector_interaction_gain_rule is required")
    require(isinstance(interaction.get("maximum_median_ratio_b_over_a_per_wave"), (int, float)), "connector interaction threshold is required")

    context = preregistration.get("context_volume")
    require(isinstance(context, dict), "context_volume is required")
    require(context.get("metric") in CONTEXT_METRICS, "Unknown context-volume metric")
    require(context.get("measurement_must_be_exact_not_estimated") is True, "Context-volume measurement must be exact")
    require(context.get("required_for_orientation_efficiency_go") is True, "Context volume must gate orientation-efficiency GO")
    return repository_ref


def validate_prompt_pack(path, expected_hash, expected_wave, expected_count=12):
    actual_hash = sha256_file(path)
    require(actual_hash == expected_hash, "{} prompt-pack SHA-256 does not match preregistration".format(expected_wave))
    pack = load_json(path, "{} prompt pack".format(expected_wave))
    require(pack.get("schema_version") == 1, "{} prompt pack must use schema_version 1".format(expected_wave))
    require(pack.get("wave") == expected_wave, "{} prompt pack has wrong wave".format(expected_wave))
    cases = pack.get("cases")
    require(isinstance(cases, list) and len(cases) == expected_count, "{} prompt pack must contain {} cases".format(expected_wave, expected_count))
    ids = []
    prompts = []
    classes = []
    for case in cases:
        require(isinstance(case, dict), "{} prompt cases must be objects".format(expected_wave))
        task_id = case.get("task_id")
        corpus_class = case.get("corpus_class")
        prompt = case.get("prompt")
        require(isinstance(task_id, str) and task_id, "{} prompt task_id is required".format(expected_wave))
        require(corpus_class in {"stress", "ecological"}, "{} corpus_class must be stress or ecological".format(expected_wave))
        require(isinstance(prompt, str) and prompt.strip(), "{} prompt text is required".format(expected_wave))
        ids.append(task_id)
        classes.append(corpus_class)
        prompts.append(normalized_prompt(prompt))
    require(len(set(ids)) == len(ids), "{} prompt task IDs must be unique".format(expected_wave))
    require(classes.count("stress") == 6 and classes.count("ecological") == 6, "{} prompt pack must be 6 stress + 6 ecological".format(expected_wave))
    return {"ids": ids, "classes": dict(zip(ids, classes)), "prompts": prompts, "sha256": actual_hash}


def validate_scoring_key(path, expected_hash, expected_wave, expected_ids):
    actual_hash = sha256_file(path)
    require(actual_hash == expected_hash, "{} scoring-key SHA-256 does not match preregistration".format(expected_wave))
    key = load_json(path, "{} scoring key".format(expected_wave))
    require(key.get("schema_version") == 1, "{} scoring key must use schema_version 1".format(expected_wave))
    require(key.get("wave") == expected_wave, "{} scoring key has wrong wave".format(expected_wave))
    cases = key.get("cases")
    require(isinstance(cases, list), "{} scoring key cases are required".format(expected_wave))
    ids = [case.get("task_id") for case in cases if isinstance(case, dict)]
    require(len(ids) == len(cases) and len(set(ids)) == len(ids), "{} scoring-key task IDs must be unique".format(expected_wave))
    require(set(ids) == set(expected_ids), "{} scoring-key task IDs must match prompt pack".format(expected_wave))
    return actual_hash


def verify_evidence(preregistration, paths):
    packs = {}
    key_hashes = {}
    for key, wave_name in WAVES:
        prereg_wave = preregistration[key]
        prompt_path = paths[key + "_prompts"]
        key_path = paths[key + "_key"]
        packs[key] = validate_prompt_pack(prompt_path, prereg_wave["prompts_sha256"], wave_name)
        key_hashes[key] = validate_scoring_key(key_path, prereg_wave["scoring_key_sha256"], wave_name, packs[key]["ids"])
    overlap = set(packs["pilot"]["prompts"]) & set(packs["confirmatory"]["prompts"])
    require(not overlap, "Pilot and confirmatory prompt text overlaps")
    return {
        "pilot_prompts_sha256": packs["pilot"]["sha256"],
        "pilot_scoring_key_sha256": key_hashes["pilot"],
        "confirmatory_prompts_sha256": packs["confirmatory"]["sha256"],
        "confirmatory_scoring_key_sha256": key_hashes["confirmatory"],
        "prompt_overlap_verified_zero": True,
        "packs": packs,
    }


def score_total(scores):
    require(isinstance(scores, dict), "scores object is required for every valid run")
    values = []
    for field in SCORE_FIELDS:
        value = scores.get(field)
        require(type(value) is int and 0 <= value <= 2, "{} score must be an integer 0..2".format(field))
        values.append(value)
    optional = scores.get(OPTIONAL_SCORE_FIELD)
    if optional is not None:
        require(type(optional) is int and 0 <= optional <= 2, "{} score must be null or an integer 0..2".format(OPTIONAL_SCORE_FIELD))
        values.append(optional)
    total = sum(values)
    supplied = scores.get("total_applicable_correctness")
    if supplied is not None:
        require(supplied == total, "total_applicable_correctness does not match dimension scores")
    serious = scores.get("serious_routing_error")
    require(type(serious) is bool, "serious_routing_error must be true or false")
    return total, serious


def run_validity(run, arm, repository_ref):
    reasons = []
    checks = (
        (run.get("arm") == arm, "wrong arm"),
        (run.get("conversation_fresh") is True, "conversation not fresh"),
        (run.get("memory_enabled") is False, "Memory not disabled"),
        (run.get("project_context_present") is False, "Project/workspace context present or unknown"),
        (run.get("prior_repo_context_available") is False, "prior product repository context present or unknown"),
        (run.get("previous_arm_output_exposed") is False, "previous-arm output exposed or unknown"),
        (run.get("connector_state_equal") is True, "connector state not equal or unknown"),
        (run.get("source_state_pre_sha") == repository_ref, "pre-run source-state tip mismatch"),
        (run.get("source_state_post_sha") == repository_ref, "post-run source-state tip mismatch"),
        (run.get("source_state_protocol_violation") is False, "source-state protocol violation"),
    )
    reasons.extend(message for passed, message in checks if not passed)
    if run.get("valid") is False:
        reasons.append(run.get("invalid_reason") or "manually marked invalid")
    if arm == TREATMENT:
        if run.get("treatment_delivery_status") != "delivered":
            reasons.append("Treatment delivery failed or unknown")
        if run.get("treatment_surface_verified") is not True:
            reasons.append("Treatment aid not verified")
    else:
        if run.get("treatment_delivery_status") not in {None, "not-applicable"}:
            reasons.append("Control unexpectedly records Treatment delivery")
    calls = run.get("total_connector_calls")
    if type(calls) is not int or calls < 0:
        reasons.append("total_connector_calls missing or invalid")
    return reasons


def selected_context_value(run, metric):
    if metric == "unavailable":
        return None
    field = "repository_response_utf8_bytes" if metric == "repository_response_utf8_bytes" else "measured_input_tokens"
    value = run.get(field)
    return value if type(value) is int and value >= 0 else None


def evaluate_case(case, expected_class, repository_ref, context_metric, thresholds):
    require(isinstance(case, dict), "run-record case must be an object")
    require(case.get("corpus_class") == expected_class, "run-record corpus_class does not match prompt pack")
    runs = case.get("runs")
    require(isinstance(runs, list) and len(runs) == 2, "each primary task must contain exactly two runs")
    by_arm = {}
    for run in runs:
        require(isinstance(run, dict) and run.get("arm") in PRIMARY_ARMS, "primary run has invalid arm")
        require(run["arm"] not in by_arm, "duplicate arm in primary pair")
        by_arm[run["arm"]] = run
    require(set(by_arm) == PRIMARY_ARMS, "each primary pair requires Control and Treatment")

    invalid_reasons = {
        arm: run_validity(by_arm[arm], arm, repository_ref) for arm in (CONTROL, TREATMENT)
    }
    pair_valid = not invalid_reasons[CONTROL] and not invalid_reasons[TREATMENT]
    result = {
        "task_id": case.get("task_id"),
        "corpus_class": expected_class,
        "valid": pair_valid,
        "invalid_reasons": invalid_reasons,
    }
    if not pair_valid:
        return result

    a_total, a_serious = score_total(by_arm[CONTROL].get("scores"))
    b_total, b_serious = score_total(by_arm[TREATMENT].get("scores"))
    calls_a = by_arm[CONTROL]["total_connector_calls"]
    calls_b = by_arm[TREATMENT]["total_connector_calls"]
    call_ratio = ratio(calls_b, calls_a)
    if a_serious and not b_serious:
        serious_outcome = "A-wrong/B-correct"
    elif not a_serious and b_serious:
        serious_outcome = "A-correct/B-wrong"
    elif a_serious and b_serious:
        serious_outcome = "both-wrong"
    else:
        serious_outcome = "both-correct"

    volume_a = selected_context_value(by_arm[CONTROL], context_metric)
    volume_b = selected_context_value(by_arm[TREATMENT], context_metric)
    volume_ratio = None if volume_a is None or volume_b is None else ratio(volume_b, volume_a)
    result.update(
        {
            "correctness_a": a_total,
            "correctness_b": b_total,
            "correctness_delta_b_minus_a": b_total - a_total,
            "serious_error_a": a_serious,
            "serious_error_b": b_serious,
            "serious_error_outcome": serious_outcome,
            "connector_calls_a": calls_a,
            "connector_calls_b": calls_b,
            "connector_ratio_b_over_a": call_ratio,
            "connector_high_overhead": call_ratio > thresholds["connector_high_ratio"],
            "equal_correctness_pair": a_total == b_total and a_serious == b_serious,
            "context_volume_metric": context_metric,
            "context_volume_a": volume_a,
            "context_volume_b": volume_b,
            "context_volume_ratio_b_over_a": volume_ratio,
            "context_high_overhead": None if volume_ratio is None else volume_ratio > thresholds["context_high_ratio"],
        }
    )
    return result


def evaluate_wave(name, cases, pack, preregistration, repository_ref):
    require(isinstance(cases, list) and len(cases) == 12, "{} run record must contain exactly 12 cases".format(name))
    by_id = {}
    for case in cases:
        require(isinstance(case, dict) and isinstance(case.get("task_id"), str), "{} run-record task_id is required".format(name))
        require(case["task_id"] not in by_id, "{} run-record task IDs must be unique".format(name))
        by_id[case["task_id"]] = case
    require(set(by_id) == set(pack["ids"]), "{} run-record task IDs must match prompt pack".format(name))

    connector_gate = preregistration["connector_cost_gate"]
    context_gate = preregistration["context_volume"]
    thresholds = {
        "connector_high_ratio": connector_gate["high_overhead_ratio_threshold"],
        "context_high_ratio": context_gate["high_overhead_ratio_threshold"],
    }
    evaluated = [
        evaluate_case(by_id[task_id], pack["classes"][task_id], repository_ref, context_gate["metric"], thresholds)
        for task_id in pack["ids"]
    ]
    valid = [case for case in evaluated if case["valid"]]
    ecological = [case for case in valid if case["corpus_class"] == "ecological"]
    positive = sum(case.get("serious_error_outcome") == "A-wrong/B-correct" for case in valid)
    reverse = sum(case.get("serious_error_outcome") == "A-correct/B-wrong" for case in valid)
    both_correct = sum(case.get("serious_error_outcome") == "both-correct" for case in valid)
    both_wrong = sum(case.get("serious_error_outcome") == "both-wrong" for case in valid)
    eco_deltas = [case["correctness_delta_b_minus_a"] for case in ecological]
    eco_reverse = sum(case["serious_error_outcome"] == "A-correct/B-wrong" for case in ecological)
    all_pairs_valid = len(valid) == 12
    ecological_complete = len(ecological) == 6
    ecological_non_regression = (
        all_pairs_valid
        and ecological_complete
        and median(eco_deltas) >= preregistration["ecological_correctness_non_regression"]["minimum_per_wave"]
        and eco_reverse <= preregistration["ecological_correctness_non_regression"]["maximum_reverse_serious_error_reversals_per_wave"]
    )

    connector_ratios = [case["connector_ratio_b_over_a"] for case in ecological]
    connector_median = median(connector_ratios)
    connector_high_count = sum(case["connector_high_overhead"] for case in ecological)
    connector_cost_gate_passed = (
        all_pairs_valid
        and ecological_complete
        and connector_median <= connector_gate["acceptable_median_ratio_b_over_a"]
        and connector_high_count <= connector_gate["acceptable_high_overhead_case_count"]
    )
    interaction_rule = preregistration["connector_interaction_gain_rule"]
    connector_interaction_gain_passed = (
        all_pairs_valid
        and ecological_non_regression
        and reverse <= interaction_rule["maximum_reverse_serious_error_reversals"]
        and connector_median <= interaction_rule["maximum_median_ratio_b_over_a_per_wave"]
    )

    equal_ratios = [
        case["connector_ratio_b_over_a"] for case in ecological if case["equal_correctness_pair"]
    ]
    context_metric = context_gate["metric"]
    context_ratios = [case["context_volume_ratio_b_over_a"] for case in ecological]
    context_complete = context_metric != "unavailable" and ecological_complete and all(value is not None for value in context_ratios)
    if context_metric == "unavailable":
        context_status = "unavailable"
        context_median = None
        context_high_count = None
        context_gate_passed = False
    elif not context_complete:
        context_status = "incomplete"
        context_median = None
        context_high_count = None
        context_gate_passed = False
    else:
        context_median = median(context_ratios)
        context_high_count = sum(case["context_high_overhead"] for case in ecological)
        context_gate_passed = (
            context_median <= context_gate["maximum_median_ratio_b_over_a_per_wave"]
            and context_high_count <= context_gate["acceptable_high_overhead_case_count"]
        )
        context_status = "pass" if context_gate_passed else "fail"
    orientation_efficiency_passed = connector_interaction_gain_passed and context_gate_passed

    return {
        "name": name,
        "cases": evaluated,
        "valid_pair_count": len(valid),
        "all_pairs_valid": all_pairs_valid,
        "control_wrong_treatment_correct": positive,
        "control_correct_treatment_wrong": reverse,
        "both_correct": both_correct,
        "both_wrong": both_wrong,
        "median_paired_correctness_delta": median([case["correctness_delta_b_minus_a"] for case in valid]),
        "ecological_median_correctness_delta_b_minus_a": median(eco_deltas),
        "ecological_correctness_non_regression_passed": ecological_non_regression,
        "ecological_median_connector_ratio": connector_median,
        "ecological_connector_high_overhead_count": connector_high_count,
        "connector_cost_gate_passed": connector_cost_gate_passed,
        "equal_correctness_ecological_median_connector_ratio": median(equal_ratios),
        "connector_interaction_gain_passed": connector_interaction_gain_passed,
        "context_volume_metric": context_metric,
        "context_volume_status": context_status,
        "ecological_median_context_volume_ratio": context_median,
        "ecological_context_high_overhead_count": context_high_count,
        "context_volume_gate_passed": context_gate_passed,
        "orientation_efficiency_passed": orientation_efficiency_passed,
    }


def pilot_classification(pilot):
    if not pilot["all_pairs_valid"]:
        return "PILOT INCONCLUSIVE"
    if pilot["control_correct_treatment_wrong"] or not pilot["ecological_correctness_non_regression_passed"]:
        return "PILOT REGRESSION"
    if (
        pilot["control_wrong_treatment_correct"] >= 2
        and pilot["connector_cost_gate_passed"]
    ):
        return "PROVISIONAL CORRECTNESS SIGNAL"
    if pilot["control_wrong_treatment_correct"] == 1:
        return "WEAK CORRECTNESS SIGNAL"
    if pilot["orientation_efficiency_passed"]:
        return "PROVISIONAL ORIENTATION EFFICIENCY SIGNAL"
    if pilot["connector_interaction_gain_passed"]:
        return "PROVISIONAL CONNECTOR-INTERACTION SIGNAL"
    return "NO PILOT SIGNAL"


def final_decision(pilot, confirmatory, preregistration):
    all_valid = pilot["all_pairs_valid"] and confirmatory["all_pairs_valid"]
    combined_positive = pilot["control_wrong_treatment_correct"] + confirmatory["control_wrong_treatment_correct"]
    combined_reverse = pilot["control_correct_treatment_wrong"] + confirmatory["control_correct_treatment_wrong"]
    rules = preregistration["final_decision_rule"]["demonstrated_correctness_go"]
    correctness_thresholds = (
        confirmatory["control_wrong_treatment_correct"] >= rules["minimum_confirmatory_positive_reversals"]
        and confirmatory["control_correct_treatment_wrong"] <= rules["maximum_confirmatory_reverse_reversals"]
        and combined_positive >= rules["minimum_combined_positive_reversals"]
        and combined_reverse <= rules["maximum_combined_reverse_reversals"]
        and pilot["ecological_correctness_non_regression_passed"]
        and confirmatory["ecological_correctness_non_regression_passed"]
    )
    correctness_go = (
        all_valid
        and correctness_thresholds
        and pilot["connector_cost_gate_passed"]
        and confirmatory["connector_cost_gate_passed"]
    )
    correctness_gain_cost_not_accepted = (
        all_valid
        and correctness_thresholds
        and not (pilot["connector_cost_gate_passed"] and confirmatory["connector_cost_gate_passed"])
    )
    connector_interaction_gain = (
        all_valid
        and pilot["connector_interaction_gain_passed"]
        and confirmatory["connector_interaction_gain_passed"]
        and combined_reverse == 0
    )
    orientation_efficiency_go = (
        connector_interaction_gain
        and pilot["orientation_efficiency_passed"]
        and confirmatory["orientation_efficiency_passed"]
    )
    regression = (
        all_valid
        and (
            combined_reverse > 0
            or not pilot["ecological_correctness_non_regression_passed"]
            or not confirmatory["ecological_correctness_non_regression_passed"]
        )
    )
    pilot_signal = pilot_classification(pilot) == "PROVISIONAL CORRECTNESS SIGNAL"

    if not all_valid:
        status = "INCONCLUSIVE"
    elif regression:
        status = "REGRESSION"
    elif correctness_go and orientation_efficiency_go:
        status = "DEMONSTRATED CORRECTNESS + ORIENTATION EFFICIENCY GO"
    elif correctness_go:
        status = "DEMONSTRATED CORRECTNESS GO"
    elif orientation_efficiency_go:
        status = "DEMONSTRATED ORIENTATION EFFICIENCY GO"
    elif correctness_gain_cost_not_accepted:
        status = "CORRECTNESS GAIN / COST NOT ACCEPTED"
    elif connector_interaction_gain:
        status = "DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY"
    elif pilot_signal:
        status = "NOT CONFIRMED"
    else:
        status = "NO INCREMENTAL VALUE SHOWN"

    return {
        "all_primary_pairs_valid": all_valid,
        "combined_positive_reversals": combined_positive,
        "combined_reverse_reversals": combined_reverse,
        "demonstrated_correctness_go": correctness_go,
        "demonstrated_orientation_efficiency_go": orientation_efficiency_go,
        "demonstrated_connector_interaction_gain": connector_interaction_gain,
        "connector_interaction_gain_only": connector_interaction_gain and not orientation_efficiency_go,
        "correctness_gain_cost_not_accepted": correctness_gain_cost_not_accepted,
        "regression": regression,
        "final_status": status,
    }


def evaluate(preregistration, run_record, evidence):
    repository_ref = validate_preregistration(preregistration)
    require(run_record.get("protocol_version") == PROTOCOL_VERSION, "Run record protocol_version does not match evaluator")
    require(run_record.get("study_id") == preregistration.get("study_id"), "Run record study_id does not match preregistration")
    recorded = run_record.get("preregistered")
    require(isinstance(recorded, dict), "Run record preregistered snapshot is required")
    require(recorded.get("repository_ref") == repository_ref, "Run record repository_ref does not match preregistration")
    require(recorded.get("treatment_delivery_mode") == preregistration["treatment_delivery"]["mode"], "Run record Treatment Delivery Mode does not match preregistration")
    require(recorded.get("context_volume_metric") == preregistration["context_volume"]["metric"], "Run record context-volume metric does not match preregistration")

    pilot = evaluate_wave("PILOT", run_record.get("pilot_cases"), evidence["packs"]["pilot"], preregistration, repository_ref)
    confirmatory = evaluate_wave("CONFIRMATORY", run_record.get("confirmatory_cases"), evidence["packs"]["confirmatory"], preregistration, repository_ref)
    pilot["interim_classification"] = pilot_classification(pilot)
    decision = final_decision(pilot, confirmatory, preregistration)

    valid_ecological = [
        case
        for wave in (pilot, confirmatory)
        for case in wave["cases"]
        if case["valid"] and case["corpus_class"] == "ecological"
    ]
    combined_connector = median([case["connector_ratio_b_over_a"] for case in valid_ecological])
    combined_equal = median([
        case["connector_ratio_b_over_a"] for case in valid_ecological if case["equal_correctness_pair"]
    ])
    combined_context_values = [
        case["context_volume_ratio_b_over_a"]
        for case in valid_ecological
        if case["context_volume_ratio_b_over_a"] is not None
    ]
    return {
        "evaluation_version": 1,
        "protocol_version": PROTOCOL_VERSION,
        "study_id": preregistration["study_id"],
        "repository_ref": repository_ref,
        "evidence_verification": {key: value for key, value in evidence.items() if key != "packs"},
        "pilot": pilot,
        "confirmatory": confirmatory,
        "combined": {
            "combined_ecological_median_connector_ratio": combined_connector,
            "combined_equal_correctness_ecological_median_connector_ratio": combined_equal,
            "combined_ecological_median_context_volume_ratio": median(combined_context_values),
        },
        "final_conclusion": decision,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preregistration", type=Path, required=True)
    parser.add_argument("--run-record", type=Path, required=True)
    parser.add_argument("--pilot-prompts", type=Path, required=True)
    parser.add_argument("--pilot-key", type=Path, required=True)
    parser.add_argument("--confirmatory-prompts", type=Path, required=True)
    parser.add_argument("--confirmatory-key", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        preregistration = load_json(args.preregistration, "Preregistration")
        run_record = load_json(args.run_record, "Run record")
        evidence = verify_evidence(
            preregistration,
            {
                "pilot_prompts": args.pilot_prompts,
                "pilot_key": args.pilot_key,
                "confirmatory_prompts": args.confirmatory_prompts,
                "confirmatory_key": args.confirmatory_key,
            },
        )
        report = evaluate(preregistration, run_record, evidence)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("Repository Intelligence A/B evaluation: " + report["final_conclusion"]["final_status"])
        return 0
    except (OSError, ValueError) as exc:
        print("Repository Intelligence A/B evaluation error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
