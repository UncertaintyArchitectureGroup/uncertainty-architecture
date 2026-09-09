#!/usr/bin/env python3
"""Mechanically score the preregistered Repository Intelligence A/B study.

Semantic scores are assessor-entered against frozen keys. This script verifies
commitments, contrast integrity, run validity, paired metrics, and final status.
"""

import argparse
import hashlib
import json
import math
import re
import statistics
import sys
from pathlib import Path

PROTOCOL_VERSION = 7
CONTROL = "RI-AB-CONTROL"
TREATMENT = "RI-AB-TREATMENT"
PRIMARY_ARMS = {CONTROL, TREATMENT}
WAVES = (("pilot", "PILOT"), ("confirmatory", "CONFIRMATORY"))
CORE_SCORE_FIELDS = ("owner_routing", "evidence_sufficiency", "authority_discipline", "decision_quality")
OPTIONAL_SCORE_FIELD = "companion_validation"
CONTEXT_METRICS = {"repository_response_utf8_bytes", "input_tokens", "unavailable"}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
MANDATORY_SCENARIO_FAMILIES = {
    "exact-owner-recovery", "canonical-term-synonym-pressure", "near-synonym-source-review",
    "overlapping-artifact-refinement", "legitimate-new-artifact", "impact-validation-routing",
    "accepted-proposed-relation-change", "branch-behind-target", "producer-schema-self-change",
    "candidate-data-boundary", "shared-structural-hub", "research-authority-separation",
    "stale-materialization-fallback", "ukrainian-or-paraphrased-routing",
}
DEFAULT_CONFIRMATORY_CRITICAL_FAMILIES = {
    "accepted-proposed-relation-change", "branch-behind-target", "producer-schema-self-change",
    "candidate-data-boundary", "shared-structural-hub", "stale-materialization-fallback",
}
PREFLIGHT_TRUE_FIELDS = (
    "smoke_passed", "default_branch_tip_checks_verified", "ordinary_control_search_verified",
    "exact_ref_direct_reads_verified", "treatment_delivery_verified",
    "complete_treatment_payload_verified", "truncation_check_passed",
    "instrumentation_capture_verified", "connector_permission_parity_verified",
    "memory_disabled_verified", "project_context_absent_verified",
    "prior_product_repo_context_absent_verified", "repository_mutation_freeze_acknowledged",
)
CONTROL_PROHIBITED_SURFACE_FIELDS = (
    "ri_prohibited_aid_accessed", "full_graph_view_accessed", "repository_control_map_accessed",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path, label):
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("{} is not readable JSON: {}".format(label, exc)) from exc
    require(isinstance(value, dict), "{} must be a JSON object".format(label))
    return value


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical_sha256(value):
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def require_sha256(value, label):
    require(isinstance(value, str) and SHA256_RE.fullmatch(value), "{} must be a lowercase SHA-256".format(label))


def ratio(numerator, denominator):
    if denominator == 0:
        return 1.0 if numerator == 0 else math.inf
    return numerator / denominator


def median(values):
    return statistics.median(values) if values else None


def normalized_prompt(text):
    return " ".join(text.split())


def expected_treatment_identity(prereg):
    delivery = prereg["treatment_delivery"]
    identity = delivery.get("aid_identity")
    require(isinstance(identity, dict), "treatment_delivery.aid_identity is required")
    require(identity.get("mode") == delivery.get("mode"), "Treatment aid identity mode must match delivery mode")
    require(isinstance(identity.get("identifier"), str) and identity["identifier"], "Treatment aid identifier is required")
    require(isinstance(identity.get("source_identity"), str) and identity["source_identity"], "Treatment aid source_identity is required")
    if delivery["mode"] == "connector_compact_surface":
        require(identity.get("identifier") == "assets/repository-intelligence/agent-context.json", "Connector Treatment must use the committed Agent Context Surface")
        require(isinstance(identity.get("git_blob_sha"), str) and SHA_RE.fullmatch(identity["git_blob_sha"]), "Connector Treatment git_blob_sha is required")
        require_sha256(identity.get("content_sha256"), "Treatment compact-surface content_sha256")
    return identity


def validate_preregistration(prereg):
    require(prereg.get("protocol_version") == PROTOCOL_VERSION, "Unsupported preregistration protocol_version")
    repository_ref = prereg.get("repository_ref")
    require(isinstance(repository_ref, str) and SHA_RE.fullmatch(repository_ref), "repository_ref must be a lowercase 40-character SHA")
    require(prereg.get("execution_policy") == "always_run_pilot_and_confirmatory", "Both primary waves must always run")

    lock = prereg.get("source_state_lock")
    require(isinstance(lock, dict), "source_state_lock is required")
    require(lock.get("mode") == "stable_default_branch_window", "source_state_lock must use stable_default_branch_window")
    require(lock.get("expected_default_branch_tip_sha") == repository_ref, "source-state tip must equal repository_ref")
    for field in ("repository_mutations_prohibited_during_primary", "pre_run_tip_check_required", "post_run_tip_check_required", "ordinary_default_branch_search_allowed"):
        require(lock.get(field) is True, "source-state field {} must be true".format(field))

    preflight = prereg.get("execution_preflight")
    require(isinstance(preflight, dict), "execution_preflight is required")
    for field in PREFLIGHT_TRUE_FIELDS:
        require(preflight.get(field) is True, "execution preflight field {} must be true".format(field))
    require(isinstance(preflight.get("smoke_evidence_reference"), str) and preflight["smoke_evidence_reference"], "smoke evidence reference is required")

    isolation = prereg.get("isolation_requirements")
    expected_isolation = {
        "conversation_fresh": True, "memory_enabled": False, "project_context_present": False,
        "prior_repo_context_available": False, "unavailable_is_acceptable_for_primary": False,
        "previous_arm_output_exposed": False, "corrective_scoring_feedback_before_pair_complete": False,
        "future_wave_material_exposed": False, "hidden_benchmark_material_exposed": False,
    }
    require(isinstance(isolation, dict), "isolation_requirements are required")
    for field, expected in expected_isolation.items():
        require(isolation.get(field) is expected, "isolation requirement {} must be {!r}".format(field, expected))

    for field in ("model_family", "thinking_configuration", "client_environment", "connector"):
        require(isinstance(prereg.get(field), str) and prereg[field], "{} must be preregistered".format(field))

    delivery = prereg.get("treatment_delivery")
    require(isinstance(delivery, dict), "treatment_delivery is required")
    require(delivery.get("mode") in {"connector_compact_surface", "local_cli", "dedicated_adapter"}, "Unknown Treatment Delivery Mode")
    for field in ("must_remain_constant_across_primary_runs", "complete_payload_verified", "truncation_check_passed"):
        require(delivery.get(field) is True, "Treatment field {} must be true".format(field))
    expected_treatment_identity(prereg)

    mandatory = prereg.get("mandatory_scenario_families")
    require(isinstance(mandatory, list) and set(mandatory) == MANDATORY_SCENARIO_FAMILIES, "mandatory_scenario_families must match protocol v7")
    critical = prereg.get("confirmatory_required_scenario_families")
    require(isinstance(critical, list) and set(critical) >= DEFAULT_CONFIRMATORY_CRITICAL_FAMILIES and set(critical) <= MANDATORY_SCENARIO_FAMILIES, "confirmatory critical scenario set is incomplete")

    for key, wave_name in WAVES:
        wave = prereg.get(key)
        require(isinstance(wave, dict), "{} preregistration is required".format(key))
        require(wave.get("case_count") == 12 and wave.get("stress_cases") == 6 and wave.get("ecological_cases") == 6, "{} must be 12 cases: 6 stress + 6 ecological".format(wave_name))
        for field in ("prompts_sha256", "scoring_key_sha256", "arm_order_seed_sha256", "arm_order_plan_sha256", "ecological_selection_seed_sha256", "selected_ecological_ids_sha256"):
            require_sha256(wave.get(field), "{}.{}".format(key, field))

    quality = prereg.get("positive_reversal_quality_gate")
    require(isinstance(quality, dict) and type(quality.get("minimum_each_applicable_dimension")) is int and 0 <= quality["minimum_each_applicable_dimension"] <= 2, "positive-reversal quality gate is invalid")
    cost = prereg.get("connector_cost_gate")
    require(isinstance(cost, dict) and isinstance(cost.get("acceptable_median_ratio_b_over_a"), (int, float)) and isinstance(cost.get("high_overhead_ratio_threshold"), (int, float)) and type(cost.get("acceptable_high_overhead_case_count")) is int, "connector_cost_gate is invalid")
    interaction = prereg.get("connector_interaction_gain_rule")
    require(isinstance(interaction, dict) and isinstance(interaction.get("maximum_median_ratio_b_over_a_per_wave"), (int, float)), "connector interaction rule is invalid")
    context = prereg.get("context_volume")
    require(isinstance(context, dict) and context.get("metric") in CONTEXT_METRICS, "context_volume metric is invalid")
    require(context.get("measurement_must_be_exact_not_estimated") is True and context.get("required_for_orientation_efficiency_go") is True, "context-volume measurement/gating must remain strict")
    rule = prereg.get("final_decision_rule", {}).get("demonstrated_correctness_go")
    require(isinstance(rule, dict) and rule.get("minimum_confirmatory_ecological_positive_reversals", 0) >= 1, "Correctness GO must require confirmatory ecological support")
    return repository_ref


def validate_prompt_pack(path, expected_hash, expected_wave):
    actual_hash = sha256_file(path)
    require(actual_hash == expected_hash, "{} prompt-pack SHA-256 does not match preregistration".format(expected_wave))
    pack = load_json(path, "{} prompt pack".format(expected_wave))
    require(pack.get("schema_version") == 2 and pack.get("wave") == expected_wave, "{} prompt pack schema/wave is invalid".format(expected_wave))
    cases = pack.get("cases")
    require(isinstance(cases, list) and len(cases) == 12, "{} prompt pack must contain 12 cases".format(expected_wave))

    ids, prompts = [], []
    classes, families, source_ids, scenarios, orders = {}, {}, {}, {}, {}
    for case in cases:
        require(isinstance(case, dict), "{} prompt cases must be objects".format(expected_wave))
        task_id, corpus = case.get("task_id"), case.get("corpus_class")
        family, prompt = case.get("task_family_id"), case.get("prompt")
        scenario_list, order = case.get("scenario_families"), case.get("planned_order")
        require(isinstance(task_id, str) and task_id, "{} task_id is required".format(expected_wave))
        require(corpus in {"stress", "ecological"}, "{} corpus_class is invalid".format(expected_wave))
        require(isinstance(family, str) and family, "{} task_family_id is required".format(expected_wave))
        require(isinstance(prompt, str) and prompt.strip(), "{} prompt text is required".format(expected_wave))
        require(isinstance(scenario_list, list) and all(isinstance(item, str) and item in MANDATORY_SCENARIO_FAMILIES for item in scenario_list), "{} scenario_families are invalid".format(expected_wave))
        if corpus == "stress":
            require(scenario_list, "{} stress case {} needs a scenario family".format(expected_wave, task_id))
        source_id = case.get("ecological_source_id")
        if corpus == "ecological":
            require(isinstance(source_id, str) and source_id, "{} ecological case {} needs ecological_source_id".format(expected_wave, task_id))
        else:
            require(source_id is None, "{} stress case {} must not claim ecological_source_id".format(expected_wave, task_id))
        require(isinstance(order, list) and len(order) == 2 and set(order) == PRIMARY_ARMS, "{} case {} planned_order is invalid".format(expected_wave, task_id))
        ids.append(task_id); prompts.append(normalized_prompt(prompt))
        classes[task_id] = corpus; families[task_id] = family; source_ids[task_id] = source_id
        scenarios[task_id] = list(scenario_list); orders[task_id] = list(order)

    require(len(set(ids)) == 12, "{} task IDs must be unique".format(expected_wave))
    require(list(classes.values()).count("stress") == 6 and list(classes.values()).count("ecological") == 6, "{} must be 6 stress + 6 ecological".format(expected_wave))
    require(len(set(families.values())) == 12, "{} task_family_id values must be unique".format(expected_wave))
    eco_ids = sorted(value for value in source_ids.values() if value is not None)
    order_plan = [{"task_id": task_id, "planned_order": orders[task_id]} for task_id in ids]
    return {
        "ids": ids, "prompts": prompts, "classes": classes, "task_families": families,
        "ecological_source_ids": source_ids, "scenario_families": scenarios, "planned_orders": orders,
        "selected_ecological_ids_sha256": canonical_sha256(eco_ids),
        "arm_order_plan_sha256": canonical_sha256(order_plan), "sha256": actual_hash,
    }


def validate_scoring_key(path, expected_hash, expected_wave, expected_ids):
    actual_hash = sha256_file(path)
    require(actual_hash == expected_hash, "{} scoring-key SHA-256 does not match preregistration".format(expected_wave))
    key = load_json(path, "{} scoring key".format(expected_wave))
    require(key.get("schema_version") == 2 and key.get("wave") == expected_wave, "{} scoring-key schema/wave is invalid".format(expected_wave))
    cases = key.get("cases")
    require(isinstance(cases, list), "{} scoring-key cases are required".format(expected_wave))
    ids, applicability = [], {}
    for case in cases:
        require(isinstance(case, dict), "{} scoring-key cases must be objects".format(expected_wave))
        task_id = case.get("task_id")
        require(isinstance(task_id, str) and task_id, "{} scoring-key task_id is required".format(expected_wave))
        require(type(case.get("companion_validation_applicable")) is bool, "{} case {} must freeze companion applicability".format(expected_wave, task_id))
        ids.append(task_id); applicability[task_id] = case["companion_validation_applicable"]
    require(len(ids) == len(cases) and len(set(ids)) == len(ids) and set(ids) == set(expected_ids), "{} scoring-key IDs must match prompt pack".format(expected_wave))
    return {"sha256": actual_hash, "companion_applicability": applicability}


def verify_evidence(prereg, paths):
    packs, keys = {}, {}
    for key, wave_name in WAVES:
        wave = prereg[key]
        packs[key] = validate_prompt_pack(paths[key + "_prompts"], wave["prompts_sha256"], wave_name)
        keys[key] = validate_scoring_key(paths[key + "_key"], wave["scoring_key_sha256"], wave_name, packs[key]["ids"])
        require(packs[key]["selected_ecological_ids_sha256"] == wave["selected_ecological_ids_sha256"], "{} ecological selection commitment mismatch".format(wave_name))
        require(packs[key]["arm_order_plan_sha256"] == wave["arm_order_plan_sha256"], "{} arm-order commitment mismatch".format(wave_name))

    require(not (set(packs["pilot"]["prompts"]) & set(packs["confirmatory"]["prompts"])), "Pilot and confirmatory prompt text overlaps")
    require(not (set(packs["pilot"]["task_families"].values()) & set(packs["confirmatory"]["task_families"].values())), "Pilot and confirmatory task_family_id values overlap")
    pilot_sources = {value for value in packs["pilot"]["ecological_source_ids"].values() if value is not None}
    confirm_sources = {value for value in packs["confirmatory"]["ecological_source_ids"].values() if value is not None}
    require(not (pilot_sources & confirm_sources), "Pilot and confirmatory ecological_source_id values overlap")

    combined = {item for pack in packs.values() for values in pack["scenario_families"].values() for item in values}
    missing = sorted(set(prereg["mandatory_scenario_families"]) - combined)
    require(not missing, "Held-out corpora miss mandatory RI-EVAL scenario families: {}".format(", ".join(missing)))
    confirm = {item for values in packs["confirmatory"]["scenario_families"].values() for item in values}
    missing = sorted(set(prereg["confirmatory_required_scenario_families"]) - confirm)
    require(not missing, "Confirmatory corpus misses critical scenario families: {}".format(", ".join(missing)))
    return {
        "pilot_prompts_sha256": packs["pilot"]["sha256"], "pilot_scoring_key_sha256": keys["pilot"]["sha256"],
        "confirmatory_prompts_sha256": packs["confirmatory"]["sha256"], "confirmatory_scoring_key_sha256": keys["confirmatory"]["sha256"],
        "prompt_overlap_verified_zero": True, "task_family_overlap_verified_zero": True,
        "ecological_source_overlap_verified_zero": True, "mandatory_scenario_coverage_verified": True,
        "confirmatory_critical_coverage_verified": True, "packs": packs, "keys": keys,
    }


def score_total(scores, companion_applicable):
    require(isinstance(scores, dict), "scores object is required for every valid run")
    values = {}
    for field in CORE_SCORE_FIELDS:
        value = scores.get(field)
        require(type(value) is int and 0 <= value <= 2, "{} score must be 0..2".format(field))
        values[field] = value
    companion = scores.get(OPTIONAL_SCORE_FIELD)
    if companion_applicable:
        require(type(companion) is int and 0 <= companion <= 2, "companion_validation must be scored when applicable")
        values[OPTIONAL_SCORE_FIELD] = companion
    else:
        require(companion is None, "companion_validation must be null when not applicable")
    total = sum(values.values())
    if scores.get("total_applicable_correctness") is not None:
        require(scores["total_applicable_correctness"] == total, "total_applicable_correctness does not match dimensions")
    serious = scores.get("serious_routing_error")
    require(type(serious) is bool, "serious_routing_error must be boolean")
    return total, serious, values


def run_validity(run, arm, repository_ref, prereg):
    reasons = []
    checks = {
        "wrong arm": run.get("arm") == arm,
        "conversation not fresh": run.get("conversation_fresh") is True,
        "Memory not disabled": run.get("memory_enabled") is False,
        "Project/workspace context present or unknown": run.get("project_context_present") is False,
        "prior product repository context present or unknown": run.get("prior_repo_context_available") is False,
        "previous-arm output exposed": run.get("previous_arm_output_exposed") is False,
        "corrective scoring feedback exposed before pair completion": run.get("corrective_scoring_feedback_before_pair_complete") is False,
        "future-wave material exposed": run.get("future_wave_material_exposed") is False,
        "hidden benchmark material exposed": run.get("hidden_benchmark_material_exposed") is False,
        "connector state not equal or unknown": run.get("connector_state_equal") is True,
        "pre-run source-state tip mismatch": run.get("source_state_pre_sha") == repository_ref,
        "post-run source-state tip mismatch": run.get("source_state_post_sha") == repository_ref,
        "source-state protocol violation": run.get("source_state_protocol_violation") is False,
        "model family differs from preregistration": run.get("model_family") == prereg["model_family"],
        "thinking configuration differs from preregistration": run.get("thinking_configuration") == prereg["thinking_configuration"],
        "client environment differs from preregistration": run.get("client_environment") == prereg["client_environment"],
        "connector differs from preregistration": run.get("connector") == prereg["connector"],
    }
    reasons.extend(message for message, passed in checks.items() if not passed)
    if run.get("valid") is False:
        reasons.append(run.get("invalid_reason") or "manually marked invalid")
    if not isinstance(run.get("protocol_violations"), list) or run.get("protocol_violations"):
        reasons.append("protocol_violations must be an empty list")
    calls, payload = run.get("total_connector_calls"), run.get("ri_payload_bytes")
    if type(calls) is not int or calls < 0:
        reasons.append("total_connector_calls missing or invalid")
    if type(payload) is not int or payload < 0:
        reasons.append("ri_payload_bytes missing or invalid")
    operations = run.get("ri_logical_operations_or_evidence")
    if not isinstance(operations, list):
        reasons.append("ri_logical_operations_or_evidence must be a list"); operations = []

    if arm == CONTROL:
        if run.get("treatment_delivery_status") not in {None, "not-applicable"}:
            reasons.append("Control unexpectedly records Treatment delivery")
        if run.get("treatment_aid_identity") is not None:
            reasons.append("Control records Treatment aid identity")
        if run.get("treatment_surface_verified") not in {None, False, "not-applicable"}:
            reasons.append("Control unexpectedly verifies Treatment surface")
        if run.get("ri_aid_accessed") is not False or payload != 0 or operations:
            reasons.append("Control RI ablation was contaminated")
        for field in CONTROL_PROHIBITED_SURFACE_FIELDS:
            if run.get(field) is not False:
                reasons.append("Control prohibited surface flag {} is not false".format(field))
    else:
        if run.get("treatment_delivery_status") != "delivered":
            reasons.append("Treatment delivery failed or unknown")
        if run.get("treatment_surface_verified") is not True or run.get("complete_treatment_payload_verified") is not True:
            reasons.append("Treatment aid/payload not completely verified")
        if run.get("ri_aid_accessed") is not True:
            reasons.append("Treatment RI aid was not observably accessed")
        if run.get("treatment_aid_identity") != expected_treatment_identity(prereg):
            reasons.append("Treatment aid identity differs from preregistration")
        if prereg["treatment_delivery"]["mode"] == "connector_compact_surface" and (type(payload) is not int or payload <= 0):
            reasons.append("Connector Treatment must record positive RI payload bytes")
    return reasons


def selected_context_value(run, metric):
    if metric == "unavailable":
        return None
    field = "repository_response_utf8_bytes" if metric == "repository_response_utf8_bytes" else "measured_input_tokens"
    value = run.get(field)
    return value if type(value) is int and value >= 0 else None


def evaluate_case(case, corpus, order, companion_applicable, repository_ref, prereg, context_metric, thresholds):
    require(isinstance(case, dict) and case.get("corpus_class") == corpus, "run-record corpus_class does not match prompt pack")
    require(case.get("order") == order, "run-record pair order does not match frozen prompt-pack order")
    runs = case.get("runs")
    require(isinstance(runs, list) and len(runs) == 2, "each primary task must contain exactly two runs")
    require([run.get("arm") for run in runs if isinstance(run, dict)] == order, "run execution order does not match frozen pair order")
    by_arm = {}
    for run in runs:
        require(isinstance(run, dict) and run.get("arm") in PRIMARY_ARMS and run["arm"] not in by_arm, "primary pair has invalid/duplicate arm")
        by_arm[run["arm"]] = run
    require(set(by_arm) == PRIMARY_ARMS, "each primary pair requires Control and Treatment")
    invalid = {arm: run_validity(by_arm[arm], arm, repository_ref, prereg) for arm in (CONTROL, TREATMENT)}
    valid = not invalid[CONTROL] and not invalid[TREATMENT]
    result = {"task_id": case.get("task_id"), "corpus_class": corpus, "valid": valid, "invalid_reasons": invalid}
    if not valid:
        return result

    a_total, a_serious, _ = score_total(by_arm[CONTROL].get("scores"), companion_applicable)
    b_total, b_serious, b_values = score_total(by_arm[TREATMENT].get("scores"), companion_applicable)
    if a_serious and not b_serious:
        serious = "A-serious/B-no-serious"
    elif not a_serious and b_serious:
        serious = "A-no-serious/B-serious"
    elif a_serious and b_serious:
        serious = "both-serious"
    else:
        serious = "neither-serious"
    quality_min = prereg["positive_reversal_quality_gate"]["minimum_each_applicable_dimension"]
    quality_pass = all(value >= quality_min for value in b_values.values())
    calls_a, calls_b = by_arm[CONTROL]["total_connector_calls"], by_arm[TREATMENT]["total_connector_calls"]
    call_ratio = ratio(calls_b, calls_a)
    volume_a, volume_b = selected_context_value(by_arm[CONTROL], context_metric), selected_context_value(by_arm[TREATMENT], context_metric)
    volume_ratio = None if volume_a is None or volume_b is None else ratio(volume_b, volume_a)
    result.update({
        "correctness_a": a_total, "correctness_b": b_total, "correctness_delta_b_minus_a": b_total - a_total,
        "serious_error_a": a_serious, "serious_error_b": b_serious, "serious_error_outcome": serious,
        "treatment_positive_reversal_quality_passed": quality_pass,
        "qualifying_positive_reversal": serious == "A-serious/B-no-serious" and quality_pass,
        "connector_calls_a": calls_a, "connector_calls_b": calls_b, "connector_ratio_b_over_a": call_ratio,
        "connector_high_overhead": call_ratio > thresholds["connector_high_ratio"],
        "equal_correctness_pair": a_total == b_total and a_serious == b_serious,
        "context_volume_metric": context_metric, "context_volume_a": volume_a, "context_volume_b": volume_b,
        "context_volume_ratio_b_over_a": volume_ratio,
        "context_high_overhead": None if volume_ratio is None else volume_ratio > thresholds["context_high_ratio"],
    })
    return result


def evaluate_wave(name, cases, pack, key, prereg, repository_ref):
    require(isinstance(cases, list) and len(cases) == 12, "{} run record must contain 12 cases".format(name))
    by_id = {}
    for case in cases:
        require(isinstance(case, dict) and isinstance(case.get("task_id"), str) and case["task_id"] not in by_id, "{} run-record task IDs are invalid".format(name))
        by_id[case["task_id"]] = case
    require(set(by_id) == set(pack["ids"]), "{} run-record task IDs must match prompt pack".format(name))

    connector_gate, context_gate = prereg["connector_cost_gate"], prereg["context_volume"]
    thresholds = {"connector_high_ratio": connector_gate["high_overhead_ratio_threshold"], "context_high_ratio": context_gate["high_overhead_ratio_threshold"]}
    evaluated = [evaluate_case(by_id[task_id], pack["classes"][task_id], pack["planned_orders"][task_id], key["companion_applicability"][task_id], repository_ref, prereg, context_gate["metric"], thresholds) for task_id in pack["ids"]]
    valid = [case for case in evaluated if case["valid"]]
    ecological = [case for case in valid if case["corpus_class"] == "ecological"]
    all_valid, eco_complete = len(valid) == 12, len(ecological) == 6
    raw_positive = sum(case.get("serious_error_outcome") == "A-serious/B-no-serious" for case in valid)
    positive = sum(case.get("qualifying_positive_reversal") is True for case in valid)
    eco_positive = sum(case.get("qualifying_positive_reversal") is True for case in ecological)
    reverse = sum(case.get("serious_error_outcome") == "A-no-serious/B-serious" for case in valid)
    neither = sum(case.get("serious_error_outcome") == "neither-serious" for case in valid)
    both = sum(case.get("serious_error_outcome") == "both-serious" for case in valid)
    eco_deltas = [case["correctness_delta_b_minus_a"] for case in ecological]
    eco_reverse = sum(case["serious_error_outcome"] == "A-no-serious/B-serious" for case in ecological)
    nonreg = all_valid and eco_complete and median(eco_deltas) >= prereg["ecological_correctness_non_regression"]["minimum_per_wave"] and eco_reverse <= prereg["ecological_correctness_non_regression"]["maximum_reverse_serious_error_reversals_per_wave"]

    connector_ratios = [case["connector_ratio_b_over_a"] for case in ecological]
    connector_median = median(connector_ratios)
    connector_high = sum(case["connector_high_overhead"] for case in ecological)
    connector_gate_pass = all_valid and eco_complete and connector_median <= connector_gate["acceptable_median_ratio_b_over_a"] and connector_high <= connector_gate["acceptable_high_overhead_case_count"]
    interaction = prereg["connector_interaction_gain_rule"]
    connector_gain = all_valid and nonreg and reverse <= interaction["maximum_reverse_serious_error_reversals"] and connector_median <= interaction["maximum_median_ratio_b_over_a_per_wave"]
    equal_ratios = [case["connector_ratio_b_over_a"] for case in ecological if case["equal_correctness_pair"]]

    context_metric = context_gate["metric"]
    context_ratios = [case["context_volume_ratio_b_over_a"] for case in ecological]
    context_complete = context_metric != "unavailable" and eco_complete and all(value is not None for value in context_ratios)
    if context_metric == "unavailable":
        context_status, context_median, context_high, context_pass = "unavailable", None, None, False
    elif not context_complete:
        context_status, context_median, context_high, context_pass = "incomplete", None, None, False
    else:
        context_median = median(context_ratios); context_high = sum(case["context_high_overhead"] for case in ecological)
        context_pass = context_median <= context_gate["maximum_median_ratio_b_over_a_per_wave"] and context_high <= context_gate["acceptable_high_overhead_case_count"]
        context_status = "pass" if context_pass else "fail"
    return {
        "name": name, "cases": evaluated, "valid_pair_count": len(valid), "all_pairs_valid": all_valid,
        "a_serious_b_no_serious": raw_positive, "qualifying_positive_reversals": positive,
        "qualifying_ecological_positive_reversals": eco_positive, "a_no_serious_b_serious": reverse,
        "neither_serious": neither, "both_serious": both,
        "median_paired_correctness_delta": median([case["correctness_delta_b_minus_a"] for case in valid]),
        "ecological_median_correctness_delta_b_minus_a": median(eco_deltas), "ecological_correctness_non_regression_passed": nonreg,
        "ecological_median_connector_ratio": connector_median, "ecological_connector_high_overhead_count": connector_high,
        "connector_cost_gate_passed": connector_gate_pass, "equal_correctness_ecological_median_connector_ratio": median(equal_ratios),
        "connector_interaction_gain_passed": connector_gain, "context_volume_metric": context_metric,
        "context_volume_status": context_status, "ecological_median_context_volume_ratio": context_median,
        "ecological_context_high_overhead_count": context_high, "context_volume_gate_passed": context_pass,
        "orientation_efficiency_passed": connector_gain and context_pass,
    }


def pilot_classification(pilot):
    if not pilot["all_pairs_valid"]:
        return "PILOT INCONCLUSIVE"
    if pilot["a_no_serious_b_serious"] or not pilot["ecological_correctness_non_regression_passed"]:
        return "PILOT REGRESSION"
    if pilot["qualifying_positive_reversals"] >= 2 and pilot["connector_cost_gate_passed"]:
        return "PROVISIONAL CORRECTNESS SIGNAL"
    if pilot["qualifying_positive_reversals"] == 1:
        return "WEAK CORRECTNESS SIGNAL"
    if pilot["orientation_efficiency_passed"]:
        return "PROVISIONAL ORIENTATION EFFICIENCY SIGNAL"
    if pilot["connector_interaction_gain_passed"]:
        return "PROVISIONAL CONNECTOR-INTERACTION SIGNAL"
    return "NO PILOT SIGNAL"


def final_decision(pilot, confirm, prereg):
    all_valid = pilot["all_pairs_valid"] and confirm["all_pairs_valid"]
    positive = pilot["qualifying_positive_reversals"] + confirm["qualifying_positive_reversals"]
    reverse = pilot["a_no_serious_b_serious"] + confirm["a_no_serious_b_serious"]
    rule = prereg["final_decision_rule"]["demonstrated_correctness_go"]
    thresholds = (
        confirm["qualifying_positive_reversals"] >= rule["minimum_confirmatory_positive_reversals"]
        and confirm["qualifying_ecological_positive_reversals"] >= rule["minimum_confirmatory_ecological_positive_reversals"]
        and confirm["a_no_serious_b_serious"] <= rule["maximum_confirmatory_reverse_reversals"]
        and positive >= rule["minimum_combined_positive_reversals"] and reverse <= rule["maximum_combined_reverse_reversals"]
        and pilot["ecological_correctness_non_regression_passed"] and confirm["ecological_correctness_non_regression_passed"]
    )
    cost_ok = pilot["connector_cost_gate_passed"] and confirm["connector_cost_gate_passed"]
    correctness_go = all_valid and thresholds and cost_ok
    correctness_cost_fail = all_valid and thresholds and not cost_ok
    connector_gain = all_valid and pilot["connector_interaction_gain_passed"] and confirm["connector_interaction_gain_passed"] and reverse == 0
    efficiency_go = connector_gain and pilot["orientation_efficiency_passed"] and confirm["orientation_efficiency_passed"]
    regression = all_valid and (reverse > 0 or not pilot["ecological_correctness_non_regression_passed"] or not confirm["ecological_correctness_non_regression_passed"])
    pilot_signal = pilot["qualifying_positive_reversals"] >= 1 and pilot["a_no_serious_b_serious"] == 0 and pilot["ecological_correctness_non_regression_passed"]
    if not all_valid:
        status = "INCONCLUSIVE"
    elif regression:
        status = "REGRESSION"
    elif correctness_go and efficiency_go:
        status = "DEMONSTRATED CORRECTNESS + ORIENTATION EFFICIENCY GO"
    elif correctness_go:
        status = "DEMONSTRATED CORRECTNESS GO"
    elif efficiency_go:
        status = "DEMONSTRATED ORIENTATION EFFICIENCY GO"
    elif correctness_cost_fail:
        status = "CORRECTNESS GAIN / COST NOT ACCEPTED"
    elif connector_gain:
        status = "DEMONSTRATED CONNECTOR-INTERACTION GAIN ONLY"
    elif pilot_signal:
        status = "NOT CONFIRMED"
    else:
        status = "NO INCREMENTAL VALUE SHOWN"
    return {
        "all_primary_pairs_valid": all_valid, "combined_qualifying_positive_reversals": positive,
        "combined_reverse_serious_reversals": reverse, "demonstrated_correctness_go": correctness_go,
        "demonstrated_orientation_efficiency_go": efficiency_go, "demonstrated_connector_interaction_gain": connector_gain,
        "connector_interaction_gain_only": connector_gain and not efficiency_go,
        "correctness_gain_cost_not_accepted": correctness_cost_fail, "regression": regression, "final_status": status,
    }


def validate_run_record_preflight(record, prereg):
    preflight = record.get("execution_preflight")
    require(isinstance(preflight, dict), "Run record execution_preflight is required")
    for field in PREFLIGHT_TRUE_FIELDS:
        require(preflight.get(field) is True, "Run-record preflight field {} must be true".format(field))
    require(preflight.get("eligible_to_start_primary") is True, "Run record must show primary execution was eligible")
    require(preflight.get("smoke_evidence_reference") == prereg["execution_preflight"]["smoke_evidence_reference"], "Run-record smoke evidence differs from preregistration")


def evaluate(prereg, record, evidence):
    repository_ref = validate_preregistration(prereg)
    validate_run_record_preflight(record, prereg)
    require(record.get("protocol_version") == PROTOCOL_VERSION and record.get("study_id") == prereg.get("study_id"), "Run record protocol/study identity mismatch")
    frozen = record.get("preregistered")
    require(isinstance(frozen, dict), "Run record preregistered snapshot is required")
    expected = {
        "repository_ref": repository_ref, "treatment_delivery_mode": prereg["treatment_delivery"]["mode"],
        "treatment_aid_identity": prereg["treatment_delivery"]["aid_identity"], "context_volume_metric": prereg["context_volume"]["metric"],
        "model_family": prereg["model_family"], "thinking_configuration": prereg["thinking_configuration"],
        "client_environment": prereg["client_environment"], "connector": prereg["connector"],
    }
    for field, value in expected.items():
        require(frozen.get(field) == value, "Run-record preregistered {} mismatch".format(field))
    pilot = evaluate_wave("PILOT", record.get("pilot_cases"), evidence["packs"]["pilot"], evidence["keys"]["pilot"], prereg, repository_ref)
    confirm = evaluate_wave("CONFIRMATORY", record.get("confirmatory_cases"), evidence["packs"]["confirmatory"], evidence["keys"]["confirmatory"], prereg, repository_ref)
    pilot["interim_classification"] = pilot_classification(pilot)
    decision = final_decision(pilot, confirm, prereg)
    ecological = [case for wave in (pilot, confirm) for case in wave["cases"] if case["valid"] and case["corpus_class"] == "ecological"]
    context = [case["context_volume_ratio_b_over_a"] for case in ecological if case["context_volume_ratio_b_over_a"] is not None]
    return {
        "evaluation_version": 2, "protocol_version": PROTOCOL_VERSION, "study_id": prereg["study_id"], "repository_ref": repository_ref,
        "evidence_verification": {key: value for key, value in evidence.items() if key not in {"packs", "keys"}},
        "pilot": pilot, "confirmatory": confirm,
        "combined": {
            "combined_ecological_median_connector_ratio": median([case["connector_ratio_b_over_a"] for case in ecological]),
            "combined_equal_correctness_ecological_median_connector_ratio": median([case["connector_ratio_b_over_a"] for case in ecological if case["equal_correctness_pair"]]),
            "combined_ecological_median_context_volume_ratio": median(context),
        },
        "final_conclusion": decision,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--preregistration", type=Path, required=True); parser.add_argument("--run-record", type=Path, required=True)
    parser.add_argument("--pilot-prompts", type=Path, required=True); parser.add_argument("--pilot-key", type=Path, required=True)
    parser.add_argument("--confirmatory-prompts", type=Path, required=True); parser.add_argument("--confirmatory-key", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        prereg, record = load_json(args.preregistration, "Preregistration"), load_json(args.run_record, "Run record")
        evidence = verify_evidence(prereg, {"pilot_prompts": args.pilot_prompts, "pilot_key": args.pilot_key, "confirmatory_prompts": args.confirmatory_prompts, "confirmatory_key": args.confirmatory_key})
        report = evaluate(prereg, record, evidence)
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print("Repository Intelligence A/B evaluation: " + report["final_conclusion"]["final_status"]); return 0
    except (OSError, ValueError) as exc:
        print("Repository Intelligence A/B evaluation error: {}".format(exc), file=sys.stderr); return 2


if __name__ == "__main__":
    sys.exit(main())
