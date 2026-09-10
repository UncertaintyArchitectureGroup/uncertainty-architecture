#!/usr/bin/env python3
"""Mechanically evaluate the preregistered Repository Intelligence A/B study."""

import argparse
import hashlib
import json
import math
import statistics
import sys
from pathlib import Path

PROTOCOL_VERSION = 10
CONTROL = "RI-AB-CONTROL"
TREATMENT = "RI-AB-TREATMENT"
PRIMARY_ARMS = {CONTROL, TREATMENT}
TREATMENT_MODE = "connector_compact_surface"
TREATMENT_IDENTIFIER = "assets/repository-intelligence/agent-context.json"
CORE_SCORE_FIELDS = (
    "owner_routing",
    "evidence_sufficiency",
    "authority_discipline",
    "decision_quality",
)
OPTIONAL_SCORE_FIELD = "companion_validation"
RESOURCE_CLASSES = {
    "ordinary_source",
    "ri_compact_surface",
    "ri_query",
    "ri_full_graph",
    "repository_control_map",
    "other",
}
RI_CLASSES = RESOURCE_CLASSES - {"ordinary_source", "other"}
PROHIBITED_TREATMENT_CLASSES = {"ri_query", "ri_full_graph", "repository_control_map"}
INSTRUMENTATION_SOURCES = {"machine_capture", "exported_transcript"}
MANDATORY = {
    "exact-owner-recovery",
    "canonical-term-synonym-pressure",
    "near-synonym-source-review",
    "overlapping-artifact-refinement",
    "legitimate-new-artifact",
    "impact-validation-routing",
    "accepted-proposed-relation-change",
    "branch-behind-target",
    "producer-schema-self-change",
    "candidate-data-boundary",
    "shared-structural-hub",
    "research-authority-separation",
    "stale-materialization-fallback",
    "ukrainian-or-paraphrased-routing",
}
CRITICAL = {
    "accepted-proposed-relation-change",
    "branch-behind-target",
    "producer-schema-self-change",
    "candidate-data-boundary",
    "shared-structural-hub",
    "stale-materialization-fallback",
}
ANCHORS = {"exact-owner-recovery", "legitimate-new-artifact"}
PREFLIGHT = (
    "smoke_passed",
    "default_branch_tip_checks_verified",
    "ordinary_control_search_verified",
    "exact_ref_direct_reads_verified",
    "treatment_delivery_verified",
    "complete_treatment_payload_verified",
    "truncation_check_passed",
    "instrumentation_capture_verified",
    "connector_permission_parity_verified",
    "memory_disabled_verified",
    "project_context_absent_verified",
    "prior_product_repo_context_absent_verified",
    "repository_mutation_freeze_acknowledged",
)


def req(condition, message):
    if not condition:
        raise ValueError(message)


def exact_fields(value, expected, label):
    req(isinstance(value, dict), f"{label} must be an object")
    actual = set(value)
    req(actual == expected, f"{label} fields mismatch: missing={sorted(expected - actual)}, unexpected={sorted(actual - expected)}")


def load(path, label):
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not readable JSON: {exc}") from exc
    req(isinstance(value, dict), f"{label} must be a JSON object")
    return value


def s256b(payload):
    return hashlib.sha256(payload).hexdigest()


def s256f(path):
    return s256b(Path(path).read_bytes())


def s256t(text):
    return s256b(text.encode("utf-8"))


def cjson(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def csha(value):
    return s256t(cjson(value))


def git_blob_sha(payload):
    header = f"blob {len(payload)}\0".encode("ascii")
    return hashlib.sha1(header + payload).hexdigest()


def normalized_prompt(text):
    return " ".join(text.split()).casefold()


def med(values):
    return statistics.median(values) if values else None


def rat(numerator, denominator):
    if denominator == 0:
        return 1.0 if numerator == 0 else math.inf
    return numerator / denominator


def rank(seed, label, identifier):
    return s256t(f"{seed}\0{label}\0{identifier}")


def arm_order(seed, task_id):
    return (
        [CONTROL, TREATMENT]
        if int(rank(seed, "arm-order", task_id), 16) % 2 == 0
        else [TREATMENT, CONTROL]
    )


def eco_select(items, seed):
    exact = [item for item in items if item["anchor_type"] == "exact-owner"]
    new = [item for item in items if item["anchor_type"] == "legitimate-new-artifact"]
    req(len(exact) >= 2 and len(new) >= 2, "ecological pool needs at least two anchors of each required type")
    exact = sorted(exact, key=lambda item: rank(seed, "exact-owner", item["ecological_source_id"]))[:2]
    new = sorted(new, key=lambda item: rank(seed, "legitimate-new-artifact", item["ecological_source_id"]))[:2]
    used = {item["ecological_source_id"] for item in exact + new}
    rest = sorted(
        [item for item in items if item["ecological_source_id"] not in used],
        key=lambda item: rank(seed, "general", item["ecological_source_id"]),
    )[:8]
    req(len(rest) == 8, "ecological pool needs eight non-reserved selections")
    return {
        "pilot": [exact[0], new[0], *rest[:4]],
        "confirmatory": [exact[1], new[1], *rest[4:]],
    }


def envelope(p, wave, task_id, arm, prompt_sha):
    return {
        "repository": p["repository"],
        "repository_ref": p["repository_ref"],
        "source_state_lock": "stable_default_branch_window",
        "wave": wave,
        "task_id": task_id,
        "arm": arm,
        "treatment_delivery_mode": TREATMENT_MODE if arm == TREATMENT else "not-applicable",
        "task_prompt_sha256": prompt_sha,
    }


def full_message(p, wave, task_id, arm, prompt, prompt_sha):
    env = envelope(p, wave, task_id, arm, prompt_sha)
    return (
        f"Experiment arm: {arm}\n"
        f"Study repository: {env['repository']}\n"
        f"Study ref: {env['repository_ref']}\n"
        f"Wave: {wave}\n"
        f"Task ID: {task_id}\n"
        f"Treatment Delivery Mode: {env['treatment_delivery_mode']}\n"
        "Task:\n"
        f"{prompt}"
    )


def valid_sha256(value):
    return isinstance(value, str) and len(value) == 64 and all(char in "0123456789abcdef" for char in value.lower())


def valid_commit_sha(value):
    return isinstance(value, str) and len(value) == 40 and all(char in "0123456789abcdef" for char in value.lower())


def validate_randomization_provenance(p):
    provenance = p.get("randomization_provenance")
    req(isinstance(provenance, dict), "randomization_provenance required")
    req(provenance.get("method") == "independent_assessor_after_pool_commitment", "randomization provenance method invalid")
    req(isinstance(provenance.get("pool_commitment_reference"), str) and provenance["pool_commitment_reference"], "pool_commitment_reference required")
    req(
        provenance.get("pool_commitment_sha256") == p["ecological_source_pool"]["normalized_eligible_pool_sha256"],
        "pool commitment must bind the frozen ecological pool",
    )
    for name in ("ecological_selection", "pilot_arm_order", "confirmatory_arm_order"):
        entry = provenance.get(name)
        req(isinstance(entry, dict), f"randomization provenance {name} required")
        for field in ("independent_assessor", "generation_reference"):
            req(isinstance(entry.get(field), str) and entry[field], f"randomization provenance {name}.{field} required")
        req(entry.get("generated_after_pool_commitment") is True, f"randomization provenance {name} must postdate pool commitment")
        req(entry.get("single_generation_attested") is True, f"randomization provenance {name} must attest one generation")
