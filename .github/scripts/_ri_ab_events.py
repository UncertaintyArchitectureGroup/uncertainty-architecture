#!/usr/bin/env python3
"""Per-run input, source-lock, Treatment, and instrumentation validation for RI A/B."""

from _ri_ab_base import (
    CONTROL, CORE_SCORE_FIELDS, INSTRUMENTATION_SOURCES, OPTIONAL_SCORE_FIELD,
    PROHIBITED_TREATMENT_CLASSES, RESOURCE_CLASSES, RI_CLASSES, TREATMENT,
    csha, envelope, full_message, req, s256b, s256t, valid_sha256,
)

def score_total(scores, key):
    req(isinstance(scores, dict), "blind scores required")
    values = {}
    for field in CORE_SCORE_FIELDS:
        req(type(scores.get(field)) is int and 0 <= scores[field] <= 2, f"{field} score invalid")
        values[field] = scores[field]
    companion = scores.get(OPTIONAL_SCORE_FIELD)
    if key["companion_validation_applicable"]:
        req(type(companion) is int and 0 <= companion <= 2, "companion_validation must be scored")
        values[OPTIONAL_SCORE_FIELD] = companion
    else:
        req(companion is None, "companion_validation must be null")
    total = sum(values.values())
    req(scores.get("total_applicable_correctness") == total, "total_applicable_correctness mismatch")
    req(type(scores.get("serious_routing_error")) is bool, "serious_routing_error must be boolean")
    return total, scores["serious_routing_error"], values


def validate_event(event, index, p):
    req(isinstance(event, dict) and event.get("sequence") == index and event.get("phase") in {"study_infrastructure", "task_orientation"} and event.get("resource_class") in RESOURCE_CLASSES and event.get("repository") == p["repository"], "invalid tool event")
    for field in ("tool_family", "operation", "resource"):
        req(isinstance(event.get(field), str) and event[field], f"tool event {field} required")
    req(event.get("response_bytes") is None or type(event["response_bytes"]) is int and event["response_bytes"] >= 0, "invalid response_bytes")
    if event["operation"] in {"branch_tip_pre", "branch_tip_post"}:
        req(event["phase"] == "study_infrastructure", "branch-tip evidence must be study infrastructure")
        req(event.get("observed_ref_sha") == p["repository_ref"], "branch-tip event does not prove study SHA")


def compact_surface_coverage(events, p, treatment):
    payload = treatment["payload"]
    size = len(payload)
    ranges = []
    for event in events:
        req(event.get("content_identity") == p["treatment_delivery"]["aid_identity"], "Treatment compact-surface event has wrong identity")
        start = event.get("payload_byte_start")
        end = event.get("payload_byte_end")
        chunk_sha = event.get("payload_chunk_sha256")
        req(type(start) is int and type(end) is int and 0 <= start < end <= size, "Treatment compact-surface byte range invalid")
        req(valid_sha256(chunk_sha), "Treatment compact-surface chunk SHA-256 required")
        req(event.get("response_bytes") == end - start, "Treatment compact-surface response_bytes must equal byte range length")
        req(s256b(payload[start:end]) == chunk_sha, "Treatment compact-surface chunk bytes do not match exact surface")
        ranges.append((start, end))
    if not ranges:
        return False
    ranges.sort()
    cursor = 0
    for start, end in ranges:
        if start != cursor:
            return False
        cursor = end
    return cursor == size


def derive(run, p, treatment):
    events = run.get("tool_events")
    req(isinstance(events, list) and events, "tool_events must be non-empty list")
    req(run.get("instrumentation_source") in INSTRUMENTATION_SOURCES, "instrumentation_source must be machine_capture or exported_transcript")
    req(isinstance(run.get("raw_evidence_reference"), str) and run["raw_evidence_reference"], "raw_evidence_reference required")
    req(valid_sha256(run.get("raw_evidence_sha256")), "raw_evidence_sha256 required")
    req(isinstance(run.get("event_extractor_version"), str) and run["event_extractor_version"], "event_extractor_version required")
    req(run.get("event_log_sha256") == csha(events), "event_log_sha256 does not match structured events")
    for index, event in enumerate(events, 1):
        validate_event(event, index, p)
    task = [event for event in events if event["phase"] == "task_orientation"]
    req(task, "at least one task_orientation event required")
    pre = [event for event in events if event.get("operation") == "branch_tip_pre"]
    post = [event for event in events if event.get("operation") == "branch_tip_post"]
    req(len(pre) == 1 and len(post) == 1, "exactly one branch_tip_pre and branch_tip_post event required")
    req(pre[0]["sequence"] < min(event["sequence"] for event in task), "branch_tip_pre must precede task orientation")
    req(post[0]["sequence"] > max(event["sequence"] for event in task), "branch_tip_post must follow task orientation")
    ri = [event for event in task if event["resource_class"] in RI_CLASSES]
    compact = [event for event in task if event["resource_class"] == "ri_compact_surface"]
    repo_bytes = None if any(event.get("response_bytes") is None for event in task) else sum(event["response_bytes"] for event in task)
    ri_bytes = None if any(event.get("response_bytes") is None for event in ri) else sum(event["response_bytes"] for event in ri)
    exact_identity = [event for event in compact if event.get("content_identity") == p["treatment_delivery"]["aid_identity"]]
    complete = compact_surface_coverage(compact, p, treatment)
    return {
        "calls": len(task),
        "infrastructure_calls": len(events) - len(task),
        "searches": sum(event.get("operation") in {"search", "code_search"} for event in task),
        "ri": bool(ri),
        "ri_bytes": 0 if not ri else ri_bytes,
        "repo_bytes": repo_bytes,
        "bad_control": bool(ri),
        "prohibited_treatment": any(event["resource_class"] in PROHIBITED_TREATMENT_CLASSES for event in task),
        "identity": bool(exact_identity),
        "complete_treatment_delivery": complete,
        "source_pre_sha": pre[0]["observed_ref_sha"],
        "source_post_sha": post[0]["observed_ref_sha"],
    }


def run_valid(run, arm, wave, task_id, prompt_text, prompt_hash, order, p, treatment):
    reasons = []
    expected_env = envelope(p, wave, task_id, arm, prompt_hash)
    expected_message = full_message(p, wave, task_id, arm, prompt_text, prompt_hash)
    checks = {
        "wrong arm": run.get("arm") == arm,
        "submitted task prompt mismatch": run.get("submitted_task_prompt") == prompt_text,
        "task prompt hash mismatch": run.get("task_prompt_sha256") == prompt_hash,
        "run envelope object mismatch": run.get("submitted_run_envelope") == expected_env,
        "run envelope hash mismatch": run.get("run_envelope_sha256") == csha(expected_env),
        "submitted full message mismatch": run.get("submitted_full_message") == expected_message,
        "submitted full message hash mismatch": run.get("submitted_full_message_sha256") == s256t(expected_message),
        "conversation not fresh": run.get("conversation_fresh") is True,
        "Memory not disabled": run.get("memory_enabled") is False,
        "Project context present": run.get("project_context_present") is False,
        "prior repo context present": run.get("prior_repo_context_available") is False,
        "previous arm exposed": run.get("previous_arm_output_exposed") is False,
        "corrective feedback exposed": run.get("corrective_scoring_feedback_before_pair_complete") is False,
        "future wave exposed": run.get("future_wave_material_exposed") is False,
        "hidden benchmark exposed": run.get("hidden_benchmark_material_exposed") is False,
        "connector state mismatch": run.get("connector_state_equal") is True,
        "source protocol violation": run.get("source_state_protocol_violation") is False,
        "model mismatch": run.get("model_family") == p["model_family"],
        "thinking mismatch": run.get("thinking_configuration") == p["thinking_configuration"],
        "client mismatch": run.get("client_environment") == p["client_environment"],
        "connector mismatch": run.get("connector") == p["connector"],
    }
    reasons.extend(message for message, passed in checks.items() if not passed)
    req(run.get("pair_order") == order, "pair_order mismatch")
    req(isinstance(run.get("protocol_violations"), list), "protocol_violations must be list")
    if run["protocol_violations"]:
        reasons.append("protocol violations")
    if "scores" in run:
        reasons.append("arm-labelled inline scores are prohibited")
    response = run.get("model_response")
    req(isinstance(response, str) and response, "model_response required")
    if run.get("model_response_sha256") != s256t(response):
        reasons.append("model_response_sha256 mismatch")
    req(isinstance(run.get("blind_response_id"), str) and run["blind_response_id"], "blind_response_id required")
    derived = derive(run, p, treatment)
    for summary_field, derived_field in (
        ("total_connector_calls", "calls"),
        ("default_branch_search_calls", "searches"),
        ("ri_payload_bytes", "ri_bytes"),
        ("repository_response_utf8_bytes", "repo_bytes"),
        ("source_state_pre_sha", "source_pre_sha"),
        ("source_state_post_sha", "source_post_sha"),
    ):
        if run.get(summary_field) != derived[derived_field]:
            reasons.append(f"{summary_field} does not match structured events")
    if arm == CONTROL:
        if derived["bad_control"]:
            reasons.append("Control RI ablation contaminated by structured events")
        if run.get("treatment_delivery_status") not in {None, "not-applicable"}:
            reasons.append("Control records Treatment delivery")
    else:
        if run.get("treatment_delivery_status") != "delivered":
            reasons.append("Treatment delivery failed")
        if derived["prohibited_treatment"]:
            reasons.append("Treatment used RI aid outside compact-surface-only boundary")
        if not derived["ri"] or not derived["identity"]:
            reasons.append("Treatment events do not prove exact compact aid access")
        if not derived["complete_treatment_delivery"]:
            reasons.append("Treatment events do not prove complete aid delivery")
        if run.get("complete_treatment_payload_verified") != derived["complete_treatment_delivery"]:
            reasons.append("complete_treatment_payload_verified does not match derived delivery")
    return reasons, derived
