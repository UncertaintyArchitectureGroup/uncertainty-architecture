#!/usr/bin/env python3
"""Preregistration and Treatment identity validation for RI A/B."""

from pathlib import Path

from _ri_ab_base import (
    CRITICAL, MANDATORY, PREFLIGHT, PROTOCOL_VERSION, TREATMENT_IDENTIFIER,
    TREATMENT_MODE, git_blob_sha, req, s256b, valid_sha256,
    validate_randomization_provenance,
)
import json

def validate_protocol_floors(p):
    gate = p.get("positive_reversal_quality_gate", {})
    req(type(gate.get("minimum_each_applicable_dimension")) is int and gate["minimum_each_applicable_dimension"] >= 1, "positive reversal quality floor may not be weakened below 1")

    nonreg = p.get("ecological_correctness_non_regression", {})
    req(nonreg.get("metric") == "median paired total correctness delta B-A", "ecological non-regression metric invalid")
    req(type(nonreg.get("minimum_per_wave")) in {int, float} and nonreg["minimum_per_wave"] >= 0, "ecological correctness floor may not be weakened below 0")
    req(nonreg.get("maximum_reverse_serious_error_reversals_per_wave") == 0, "ecological reverse-serious floor must remain zero")

    connector = p.get("connector_cost_gate", {})
    req(type(connector.get("acceptable_median_ratio_b_over_a")) in {int, float} and 0 <= connector["acceptable_median_ratio_b_over_a"] <= 1.5, "connector median cost gate may not exceed 1.5")
    req(type(connector.get("high_overhead_ratio_threshold")) in {int, float} and 0 <= connector["high_overhead_ratio_threshold"] <= 2.0, "connector high-overhead threshold may not exceed 2.0")
    req(type(connector.get("acceptable_high_overhead_case_count")) is int and 0 <= connector["acceptable_high_overhead_case_count"] <= 2, "connector high-overhead case allowance may not exceed 2")

    interaction = p.get("connector_interaction_gain_rule", {})
    req(type(interaction.get("maximum_median_ratio_b_over_a_per_wave")) in {int, float} and 0 <= interaction["maximum_median_ratio_b_over_a_per_wave"] <= 0.8, "connector interaction gain threshold may not exceed 0.8")

    volume = p.get("context_volume", {})
    req(volume.get("metric") in {"repository_response_utf8_bytes", "input_tokens", "unavailable"}, "context volume metric invalid")
    if volume["metric"] != "unavailable":
        req(type(volume.get("maximum_median_ratio_b_over_a_per_wave")) in {int, float} and 0 <= volume["maximum_median_ratio_b_over_a_per_wave"] <= 1.0, "context-volume median gate may not exceed 1.0")
        req(type(volume.get("high_overhead_ratio_threshold")) in {int, float} and 0 <= volume["high_overhead_ratio_threshold"] <= 2.0, "context-volume high-overhead threshold may not exceed 2.0")
        req(type(volume.get("acceptable_high_overhead_case_count")) is int and 0 <= volume["acceptable_high_overhead_case_count"] <= 2, "context-volume high-overhead case allowance may not exceed 2")

    rule = p.get("final_decision_rule", {}).get("engineering_acceptance_correctness", {})
    req(type(rule.get("minimum_confirmatory_positive_reversals")) is int and rule["minimum_confirmatory_positive_reversals"] >= 1, "correctness acceptance requires at least one confirmatory positive reversal")
    req(type(rule.get("minimum_confirmatory_ecological_positive_reversals")) is int and rule["minimum_confirmatory_ecological_positive_reversals"] >= 1, "correctness acceptance requires at least one confirmatory ecological positive reversal")
    req(type(rule.get("minimum_combined_positive_reversals")) is int and rule["minimum_combined_positive_reversals"] >= 3, "correctness acceptance requires at least three combined positive reversals")
    req(rule.get("maximum_combined_reverse_serious_reversals") == 0, "correctness acceptance reverse-serious ceiling must remain zero")
    for field in ("ecological_non_regression_must_pass_both_waves", "connector_cost_gate_must_pass_both_waves", "all_primary_pairs_must_be_valid"):
        req(rule.get(field) is True, f"correctness acceptance field {field} must remain true")


def validate_prereg(p):
    req(p.get("protocol_version") == PROTOCOL_VERSION, "unsupported protocol_version")
    for field in ("study_id", "repository", "repository_ref", "model_family", "thinking_configuration", "client_environment", "connector"):
        req(isinstance(p.get(field), str) and p[field], f"{field} must be preregistered")
    req(p.get("execution_policy") == "always_run_pilot_and_confirmatory", "both primary waves must run")
    lock = p.get("source_state_lock")
    req(isinstance(lock, dict) and lock.get("mode") == "stable_default_branch_window" and lock.get("expected_default_branch_tip_sha") == p["repository_ref"], "invalid source_state_lock")
    for field in ("repository_mutations_prohibited_during_primary", "pre_run_tip_check_required", "post_run_tip_check_required", "ordinary_default_branch_search_allowed"):
        req(lock.get(field) is True, f"source-state field {field} must be true")
    preflight = p.get("execution_preflight")
    req(isinstance(preflight, dict), "execution_preflight required")
    for field in PREFLIGHT:
        req(preflight.get(field) is True, f"execution preflight field {field} must be true")
    req(isinstance(preflight.get("smoke_evidence_reference"), str) and preflight["smoke_evidence_reference"], "smoke_evidence_reference required")
    req(valid_sha256(preflight.get("smoke_evidence_sha256")), "smoke_evidence_sha256 required")
    isolation = p.get("isolation_requirements")
    req(isinstance(isolation, dict), "isolation_requirements required")
    for field, expected in {
        "conversation_fresh": True,
        "memory_enabled": False,
        "project_context_present": False,
        "prior_repo_context_available": False,
        "previous_arm_output_exposed": False,
        "corrective_scoring_feedback_before_pair_complete": False,
        "future_wave_material_exposed": False,
        "hidden_benchmark_material_exposed": False,
    }.items():
        req(isolation.get(field) is expected, f"isolation {field} must be {expected}")
    delivery = p.get("treatment_delivery")
    req(isinstance(delivery, dict) and delivery.get("mode") == TREATMENT_MODE, "v10 primary study supports connector_compact_surface only")
    identity = delivery.get("aid_identity")
    req(isinstance(identity, dict) and identity.get("mode") == TREATMENT_MODE, "Treatment aid identity required")
    req(identity.get("identifier") == TREATMENT_IDENTIFIER, "Treatment aid identifier must be the compact Agent Context Surface")
    for field in ("git_blob_sha", "content_sha256", "source_identity"):
        req(isinstance(identity.get(field), str) and identity[field], f"Treatment aid identity {field} required")
    req(set(p.get("mandatory_scenario_families", [])) == MANDATORY, "mandatory scenario family set mismatch")
    req(set(p.get("confirmatory_required_scenario_families", [])) >= CRITICAL, "confirmatory critical coverage set incomplete")
    for key in ("pilot", "confirmatory"):
        wave = p.get(key)
        req(isinstance(wave, dict) and wave.get("case_count") == 12 and wave.get("stress_cases") == 6 and wave.get("ecological_cases") == 6, f"{key} must be 6+6")
        for field in ("prompts_sha256", "scoring_key_sha256", "arm_order_seed_sha256"):
            req(valid_sha256(wave.get(field)), f"{key}.{field} must be SHA-256")
    frame = p.get("ecological_sampling_frame")
    req(isinstance(frame, dict), "ecological_sampling_frame required")
    for field in ("manifest_sha256", "commitment_reference", "source_window", "cutoff"):
        req(isinstance(frame.get(field), str) and frame[field], f"ecological_sampling_frame.{field} required")
    req(valid_sha256(frame["manifest_sha256"]), "ecological_sampling_frame.manifest_sha256 invalid")
    for field in ("inclusion_rule_ids", "exclusion_rule_ids"):
        req(isinstance(frame.get(field), list) and frame[field] and all(isinstance(x, str) and x for x in frame[field]), f"ecological_sampling_frame.{field} required")
    eco = p.get("ecological_source_pool")
    req(isinstance(eco, dict) and eco.get("mode") == "complete_eligible_frame", "v10 requires complete eligible ecological frame")
    for field in ("normalized_eligible_pool_sha256", "selection_seed_sha256"):
        req(valid_sha256(eco.get(field)), f"ecological_source_pool.{field} must be SHA-256")
    validate_randomization_provenance(p)
    req(p.get("prompt_pack_schema_version") == 3 and p.get("scoring_key_schema_version") == 3, "v10 requires prompt/key schema version 3")
    req(p.get("blind_scoring_schema_version") == 1, "v10 requires blind scoring schema version 1")
    req(p.get("orientation_cost_boundary") == "task_orientation_events_only", "orientation cost boundary invalid")
    req(p.get("claim_boundary") == "engineering acceptance; not statistical significance or universal productivity proof", "claim boundary invalid")
    validate_protocol_floors(p)


def validate_treatment_surface(path, p):
    identity = p["treatment_delivery"]["aid_identity"]
    payload = Path(path).read_bytes()
    req(s256b(payload) == identity["content_sha256"], "Treatment surface content SHA-256 mismatch")
    req(git_blob_sha(payload) == identity["git_blob_sha"], "Treatment surface Git blob SHA mismatch")
    try:
        parsed = json.loads(payload.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"Treatment surface is not valid UTF-8 JSON: {exc}") from exc
    source = parsed.get("source_identity") if isinstance(parsed, dict) else None
    req(isinstance(source, dict) and source.get("digest") == identity["source_identity"], "Treatment surface source_identity mismatch")
    return {"content_sha256": s256b(payload), "git_blob_sha": git_blob_sha(payload), "source_identity": source["digest"], "utf8_bytes": len(payload), "payload": payload}
