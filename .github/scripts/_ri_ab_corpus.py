#!/usr/bin/env python3
"""Sampling-frame, corpus, prompt-pack, and scoring-key validation for RI A/B."""

from _ri_ab_base import (
    ANCHORS, CORE_SCORE_FIELDS, MANDATORY, OPTIONAL_SCORE_FIELD, arm_order,
    eco_select, load, normalized_prompt, req, s256f, s256t, valid_sha256,
)

def validate_frame(path, p):
    frame_cfg = p["ecological_sampling_frame"]
    req(s256f(path) == frame_cfg["manifest_sha256"], "ecological sampling-frame hash mismatch")
    frame = load(path, "ecological sampling frame")
    items = frame.get("items")
    req(frame.get("schema_version") == 1 and isinstance(items, list) and len(items) >= 24, "invalid ecological sampling frame")
    inclusion = set(frame_cfg["inclusion_rule_ids"])
    exclusion = set(frame_cfg["exclusion_rule_ids"])
    seen = set()
    eligible = {}
    for item in items:
        req(isinstance(item, dict), "invalid ecological sampling-frame item")
        source_id = item.get("source_event_id")
        req(isinstance(source_id, str) and source_id and source_id not in seen, "sampling-frame source_event_id invalid or duplicate")
        seen.add(source_id)
        req(isinstance(item.get("source_event_reference"), str) and item["source_event_reference"], "sampling-frame source_event_reference required")
        req(valid_sha256(item.get("source_event_sha256")), "sampling-frame source_event_sha256 required")
        req(type(item.get("eligible")) is bool, "sampling-frame eligible must be boolean")
        if item["eligible"]:
            rules = item.get("inclusion_rule_ids")
            req(isinstance(rules, list) and rules and set(rules) <= inclusion, "eligible sampling-frame item has invalid inclusion rules")
            req(item.get("exclusion_rule_id") is None, "eligible sampling-frame item cannot have exclusion rule")
            eligible[source_id] = item
        else:
            req(item.get("exclusion_rule_id") in exclusion, "ineligible sampling-frame item needs declared exclusion rule")
    req(len(eligible) >= 24, "ecological sampling frame needs at least 24 eligible source events")
    return eligible


def validate_pool(path, p, seed, eligible_frame):
    req(s256f(path) == p["ecological_source_pool"]["normalized_eligible_pool_sha256"], "ecological pool hash mismatch")
    req(s256t(seed) == p["ecological_source_pool"]["selection_seed_sha256"], "ecological selection seed commitment mismatch")
    pool = load(path, "ecological pool")
    items = pool.get("items")
    req(pool.get("schema_version") == 2 and isinstance(items, list), "invalid ecological pool")
    source_ids, family_ids, prompts = set(), set(), set()
    for item in items:
        req(isinstance(item, dict) and item.get("anchor_type") in {"exact-owner", "legitimate-new-artifact", "none"}, "invalid ecological pool item")
        for field in ("ecological_source_id", "task_family_id", "normalized_prompt", "source_event_reference", "normalization_reference"):
            req(isinstance(item.get(field), str) and item[field], f"ecological pool {field} required")
        req(valid_sha256(item.get("source_event_sha256")), "ecological pool source_event_sha256 required")
        req(item.get("normalized_from_source_only") is True, "ecological normalization must attest source-only normalization")
        source_id = item["ecological_source_id"]
        req(source_id in eligible_frame, "ecological pool contains source outside eligible sampling frame")
        frame_item = eligible_frame[source_id]
        req(item["source_event_reference"] == frame_item["source_event_reference"], "ecological source reference differs from frozen frame")
        req(item["source_event_sha256"] == frame_item["source_event_sha256"], "ecological source hash differs from frozen frame")
        scenarios = item.get("scenario_families")
        req(isinstance(scenarios, list) and all(value in MANDATORY for value in scenarios), "ecological pool scenario_families invalid")
        if item["anchor_type"] == "exact-owner":
            req("exact-owner-recovery" in scenarios, "exact-owner pool anchor must exercise exact-owner-recovery")
        if item["anchor_type"] == "legitimate-new-artifact":
            req("legitimate-new-artifact" in scenarios, "new-artifact pool anchor must exercise legitimate-new-artifact")
        prompt_key = normalized_prompt(item["normalized_prompt"])
        req(source_id not in source_ids, "ecological source IDs must be unique")
        req(item["task_family_id"] not in family_ids, "ecological task families must be unique")
        req(prompt_key not in prompts, "ecological normalized prompts must be unique")
        source_ids.add(source_id)
        family_ids.add(item["task_family_id"])
        prompts.add(prompt_key)
    req(source_ids == set(eligible_frame), "ecological pool must contain every eligible source event in the frozen sampling frame")
    return items, eco_select(items, seed)


def validate_pack(path, expected_hash, wave_name, seed):
    req(s256f(path) == expected_hash, f"{wave_name} prompt-pack hash mismatch")
    pack = load(path, f"{wave_name} prompt pack")
    cases = pack.get("cases")
    req(pack.get("schema_version") == 3 and pack.get("wave") == wave_name and isinstance(cases, list) and len(cases) == 12, f"{wave_name} prompt pack invalid")
    out = {"ids": [], "classes": {}, "prompts": {}, "prompt_text": {}, "normalized_prompts": {}, "families": {}, "sources": {}, "scenarios": {}, "orders": {}}
    seen_normalized = set()
    for case in cases:
        task_id = case.get("task_id")
        corpus = case.get("corpus_class")
        prompt = case.get("prompt")
        family = case.get("task_family_id")
        source = case.get("ecological_source_id")
        scenarios = case.get("scenario_families")
        req(isinstance(task_id, str) and task_id and task_id not in out["ids"], f"{wave_name} task_id invalid")
        req(corpus in {"stress", "ecological"} and isinstance(prompt, str) and prompt.strip() and isinstance(family, str) and family, f"{wave_name} case invalid")
        req(isinstance(scenarios, list) and all(value in MANDATORY for value in scenarios), f"{wave_name} scenarios invalid")
        req((corpus == "ecological" and isinstance(source, str) and source) or (corpus == "stress" and source is None and scenarios), f"{wave_name} source/scenario contract invalid")
        prompt_norm = normalized_prompt(prompt)
        req(prompt_norm not in seen_normalized, f"{wave_name} contains duplicate normalized prompts")
        seen_normalized.add(prompt_norm)
        order = arm_order(seed, task_id)
        req(case.get("planned_order") == order, f"{wave_name} arm order not reproduced by seed")
        out["ids"].append(task_id)
        out["classes"][task_id] = corpus
        out["prompts"][task_id] = s256t(prompt)
        out["prompt_text"][task_id] = prompt
        out["normalized_prompts"][task_id] = prompt_norm
        out["families"][task_id] = family
        out["sources"][task_id] = source
        out["scenarios"][task_id] = scenarios
        out["orders"][task_id] = order
    req(list(out["classes"].values()).count("stress") == 6 and list(out["classes"].values()).count("ecological") == 6, f"{wave_name} must be 6+6")
    return out


def validate_key(path, expected_hash, wave_name, ids):
    req(s256f(path) == expected_hash, f"{wave_name} scoring-key hash mismatch")
    key = load(path, f"{wave_name} scoring key")
    cases = key.get("cases")
    req(key.get("schema_version") == 3 and key.get("wave") == wave_name and isinstance(cases, list), f"{wave_name} scoring key invalid")
    out = {}
    for case in cases:
        task_id = case.get("task_id")
        req(task_id in ids and task_id not in out, f"{wave_name} scoring-key task IDs invalid")
        req(type(case.get("companion_validation_applicable")) is bool, f"{task_id} companion applicability missing")
        for field in ("expected_owner_or_route", "required_authoritative_evidence", "serious_error_conditions", "decision_acceptance_conditions"):
            req(isinstance(case.get(field), list) and case[field], f"{task_id} scoring key {field} must be non-empty")
        req(isinstance(case.get("acceptable_alternatives"), list), f"{task_id} acceptable_alternatives must be list")
        anchors = case.get("dimension_anchors")
        req(isinstance(anchors, dict), f"{task_id} dimension_anchors missing")
        dimensions = set(CORE_SCORE_FIELDS) | ({OPTIONAL_SCORE_FIELD} if case["companion_validation_applicable"] else set())
        req(set(anchors) == dimensions, f"{task_id} dimension anchors mismatch")
        for dimension, levels in anchors.items():
            req(isinstance(levels, dict) and set(levels) == {"0", "1", "2"} and all(isinstance(value, str) and value for value in levels.values()), f"{task_id} {dimension} anchors invalid")
        out[task_id] = case
    req(set(out) == set(ids), f"{wave_name} scoring-key IDs must match prompt pack")
    return out


def verify_evidence(p, paths, seeds):
    eligible = validate_frame(paths["ecological_frame"], p)
    pool_items, selected = validate_pool(paths["ecological_pool"], p, seeds["ecological_selection"], eligible)
    pool_by_id = {item["ecological_source_id"]: item for item in pool_items}
    packs, keys = {}, {}
    for key, wave_name in (("pilot", "PILOT"), ("confirmatory", "CONFIRMATORY")):
        req(s256t(seeds[key + "_arm"]) == p[key]["arm_order_seed_sha256"], f"{wave_name} arm seed commitment mismatch")
        packs[key] = validate_pack(paths[key + "_prompts"], p[key]["prompts_sha256"], wave_name, seeds[key + "_arm"])
        keys[key] = validate_key(paths[key + "_key"], p[key]["scoring_key_sha256"], wave_name, packs[key]["ids"])
        expected_ids = sorted(item["ecological_source_id"] for item in selected[key])
        actual_ids = sorted(source for source in packs[key]["sources"].values() if source)
        req(actual_ids == expected_ids, f"{wave_name} ecological selection not reproduced from pool+seed")
        for task_id in packs[key]["ids"]:
            source_id = packs[key]["sources"][task_id]
            if not source_id:
                continue
            item = pool_by_id[source_id]
            req(packs[key]["families"][task_id] == item["task_family_id"], f"{wave_name} selected task family differs from pool")
            req(packs[key]["prompt_text"][task_id] == item["normalized_prompt"], f"{wave_name} selected prompt differs from frozen normalized pool")
            req(packs[key]["scenarios"][task_id] == item["scenario_families"], f"{wave_name} selected scenarios differ from frozen pool")
        eco_scenarios = {scenario for task_id, scenarios in packs[key]["scenarios"].items() if packs[key]["classes"][task_id] == "ecological" for scenario in scenarios}
        req(ANCHORS <= eco_scenarios, f"{wave_name} ecological half misses required anchors")
    req(not set(packs["pilot"]["families"].values()) & set(packs["confirmatory"]["families"].values()), "task_family_id overlaps across waves")
    pilot_sources = {source for source in packs["pilot"]["sources"].values() if source}
    confirm_sources = {source for source in packs["confirmatory"]["sources"].values() if source}
    req(not pilot_sources & confirm_sources, "ecological_source_id overlaps across waves")
    pilot_prompts = set(packs["pilot"]["normalized_prompts"].values())
    confirm_prompts = set(packs["confirmatory"]["normalized_prompts"].values())
    req(not pilot_prompts & confirm_prompts, "normalized prompt text overlaps across waves")
    all_scenarios = {scenario for pack in packs.values() for scenarios in pack["scenarios"].values() for scenario in scenarios}
    req(MANDATORY <= all_scenarios, "held-out corpora miss mandatory scenarios")
    confirm_scenarios = {scenario for scenarios in packs["confirmatory"]["scenarios"].values() for scenario in scenarios}
    req(set(p["confirmatory_required_scenario_families"]) <= confirm_scenarios, "Confirmatory misses critical scenarios")
    return {"packs": packs, "keys": keys, "selection_replayed": True, "arm_randomization_replayed": True}
