#!/usr/bin/env python3
"""Measure repository-intelligence retrieval; never score unobserved agent decisions.

The corpus is separate from the producer. Mandatory cases check deterministic
contracts; paraphrase misses remain visible observations rather than hidden
translations or evidence that a new conceptual owner is needed.
"""

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

import repository_intelligence as intelligence

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CASES = ROOT / ".github/tests/repository_intelligence/benchmark_cases.json"
OPERATIONS = {
    "find_owner", "term_preflight", "artifact_preflight",
    "validation_plan", "context_for_task",
}
STANDARD_SUITE = "repository-preflight-v1"
# Coverage is an evaluator contract, not a claim supplied by the input corpus.
# New scenarios can be added; changing these obligations needs an explicit review.
REQUIRED_CASES = {
    "RI-COLD-001": ("find_owner", True),
    "RI-COLD-002": ("term_preflight", True),
    "RI-COLD-003": ("term_preflight", True),
    "RI-COLD-004": ("artifact_preflight", True),
    "RI-COLD-005": ("artifact_preflight", True),
    "RI-COLD-006": ("validation_plan", True),
    "RI-COLD-007": ("context_for_task", True),
    "RI-COLD-008": ("artifact_preflight", True),
    "RI-COLD-009": ("find_owner", False),
    "RI-COLD-010": ("find_owner", False),
    "RI-COLD-011": ("find_owner", False),
    "RI-COLD-012": ("find_owner", False),
}


def load_cases(path, suite=STANDARD_SUITE):
    if suite not in {STANDARD_SUITE, "exploratory"}:
        raise ValueError("Unknown benchmark suite: " + str(suite))
    corpus = intelligence.load_json(path, "Benchmark corpus")
    if corpus.get("version") != 1 or not isinstance(corpus.get("cases"), list) or not corpus["cases"]:
        raise ValueError("Benchmark corpus requires version 1 and nonempty cases")
    seen = set()
    list_fields = ("expected_paths", "expected_terms", "expected_instructions", "expected_validators", "expected_companions", "inventory_paths", "evidence_sources")
    for case in corpus["cases"]:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"] or case["id"] in seen:
            raise ValueError("Benchmark case IDs must be nonempty and unique")
        seen.add(case["id"])
        if not isinstance(case.get("operation"), str) or case["operation"] not in OPERATIONS or not isinstance(case.get("query"), str) or not case["query"]:
            raise ValueError("Invalid benchmark operation/query: " + case["id"])
        if type(case.get("mandatory")) is not bool:
            raise ValueError("Benchmark case must explicitly classify mandatory/advisory: " + case["id"])
        for field in list_fields:
            value = case.get(field, [])
            if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
                raise ValueError("Invalid {} in {}".format(field, case["id"]))
        if case.get("expected_rank") is not None and (type(case["expected_rank"]) is not int or case["expected_rank"] < 1):
            raise ValueError("expected_rank must be a positive integer")
        if case.get("grounded_query") is not None and (not isinstance(case["grounded_query"], str) or not case["grounded_query"]):
            raise ValueError("grounded_query must be nonempty text")
        roles = case.get("expected_roles", {})
        if not isinstance(roles, dict) or any(
            not isinstance(owner, str) or not owner or not isinstance(values, list)
            or not values or not all(isinstance(value, str) and value for value in values)
            for owner, values in roles.items()
        ):
            raise ValueError("Invalid expected_roles in " + case["id"])
        if not any(case.get(field) for field in list_fields[:-1]) and not roles:
            raise ValueError("Benchmark case needs an observable expectation: " + case["id"])
    if suite == STANDARD_SUITE:
        by_id = {case["id"]: case for case in corpus["cases"]}
        for identifier, (operation, mandatory) in REQUIRED_CASES.items():
            case = by_id.get(identifier)
            if case is None or case["operation"] != operation or case["mandatory"] is not mandatory:
                raise ValueError("Standard suite requires {} with operation={} and mandatory={}".format(
                    identifier, operation, mandatory
                ))
    return corpus


def evaluate(surface, case, query):
    # Isolate query side effects from the verified baseline used for all cases.
    result = getattr(intelligence, case["operation"])(copy.deepcopy(surface), query)
    candidates = result.get("candidates", result.get("owner_candidates", []))
    paths = [item["path"] for item in candidates]
    terms = {item.get("term") for item in candidates}
    plan = result.get("validation_plan", result)
    instructions = {item["path"] for item in result.get("instructions", plan.get("instructions", []))}
    inventory = result.get("inventory", [])
    inventory_paths = {item.get("path") for item in inventory}
    missing = {}
    for field, actual in (
        ("expected_paths", set(paths)), ("expected_terms", terms),
        ("expected_instructions", instructions),
        ("expected_validators", set(plan.get("validators", []))),
        ("expected_companions", set(plan.get("companion_candidates", []))),
        ("inventory_paths", inventory_paths),
    ):
        absent = sorted(set(case.get(field, [])) - actual)
        if absent:
            missing[field] = absent
    expected = set(case.get("expected_paths", []))
    rank = next((index for index, path in enumerate(paths, 1) if path in expected), None)
    if case.get("expected_rank") is not None and (rank is None or rank > case["expected_rank"]):
        missing["expected_rank"] = case["expected_rank"]
    inventory_kind = {"term_preflight": "terms", "artifact_preflight": "artifacts"}.get(case["operation"])
    if inventory_kind:
        expected_inventory = surface["inventories"][inventory_kind]
        # Ignore ordering while preserving duplicate multiplicity and all fields.
        expected_records = sorted(intelligence.serialize_json(item) for item in expected_inventory)
        actual_records = sorted(intelligence.serialize_json(item) for item in inventory)
        if actual_records != expected_records:
            missing["full_inventory"] = {
                "kind": inventory_kind,
                "expected_count": len(expected_records), "actual_count": len(actual_records),
                "reason": "Returned inventory differs from verified source records",
            }
    for owner, expected_roles in case.get("expected_roles", {}).items():
        actual_roles = {item.get("role", "") for item in candidates if item["path"] == owner}
        if actual_roles != set(expected_roles):
            missing.setdefault("expected_roles", {})[owner] = {
                "expected": sorted(set(expected_roles)), "actual": sorted(actual_roles),
            }
    return {
        "query": query,
        "passed": not missing,
        "missing": missing,
        "first_expected_path_rank": rank,
        "candidate_count": len(candidates),
        "inventory_count": len(inventory),
        "response_utf8_bytes": len(intelligence.serialize_json(result).encode("utf-8")),
        "top_candidates": candidates[:5],
    }


def run_benchmark(root, cases_path, surface_path, suite=STANDARD_SUITE):
    corpus = load_cases(cases_path, suite)
    contract = intelligence.load_contract(root / ".github/policy/repository-intelligence-contract.json")
    # Regeneration equality, not a copied digest, establishes current input facts.
    surface = intelligence.load_fresh_surface(root, contract, surface_path)
    results = []
    for case in corpus["cases"]:
        result = {
            "id": case["id"], "category": case.get("category", ""),
            "mandatory": case["mandatory"], "operation": case["operation"],
            "evidence_sources": case.get("evidence_sources", []),
            "decision_boundary": case.get("decision_boundary", "Read the owning source before deciding."),
            "raw": evaluate(surface, case, case["query"]),
        }
        if case.get("grounded_query"):
            # A separately reported, source-grounded query never rescues raw recall.
            result["grounded"] = evaluate(surface, case, case["grounded_query"])
        results.append(result)
    failures = [item["id"] for item in results if item["mandatory"] and not item["raw"]["passed"]]
    return {
        "benchmark_version": 2,
        "suite": suite,
        "corpus_sha256": hashlib.sha256(cases_path.read_bytes()).hexdigest(),
        "corpus_authorship": corpus.get("authorship", "unspecified"),
        "producer": surface["producer"], "source_identity": surface["source_identity"],
        "surface_utf8_bytes": surface_path.stat().st_size,
        "mandatory_failures": failures,
        "advisory_misses": [item["id"] for item in results if not item["mandatory"] and not item["raw"]["passed"]],
        "cases": results,
        "unmeasured": [
            "Independent blind cold-start agent assessment",
            "Duplicate owner/file proposals and material decision correctness",
            "Maintainer corrections caused by repository routing",
            "Model input tokens and physical iPad rendering",
        ],
        "connector_measurements": "Recorded separately from live connector calls; local response bytes are not connector reads or model tokens.",
    }


def checkout_record(root, surface_path):
    """Bind a verified clean checkout to the exact committed surface bytes.

    Called only after run_benchmark established freshness. This is local/CI
    provenance; live GitHub still selects the target/head/tested-merge state.
    """
    if Path(intelligence.git_text(root, ["rev-parse", "--show-toplevel"]).strip()).resolve() != root:
        raise ValueError("Checkout evidence requires the repository root")
    if intelligence.git_text(root, ["status", "--porcelain", "--untracked-files=normal"]).strip():
        raise ValueError("Checkout evidence requires a clean committed checkout")
    relative = surface_path.resolve().relative_to(root).as_posix()
    checkout = intelligence.git_text(root, ["rev-parse", "HEAD"]).strip()
    content = surface_path.read_bytes()
    if intelligence.git_bytes(root, ["cat-file", "blob", checkout + ":" + relative]) != content:
        raise ValueError("Surface bytes do not match the committed checkout blob")
    return {
        "checkout_sha": checkout,
        "checkout_tree_sha": intelligence.git_text(root, ["rev-parse", checkout + "^{tree}"]).strip(),
        "surface_path": relative,
        "surface_git_blob_sha": intelligence.git_text(root, ["rev-parse", checkout + ":" + relative]).strip(),
        "surface_sha256": hashlib.sha256(content).hexdigest(),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--surface", type=Path)
    parser.add_argument("--suite", choices=(STANDARD_SUITE, "exploratory"), default=STANDARD_SUITE)
    parser.add_argument("--record-checkout", action="store_true", help="Require a clean Git state and log the verified checkout/blob identity")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        surface = args.surface or root / "assets/repository-intelligence/agent-context.json"
        result = run_benchmark(root, args.cases, surface, args.suite)
        if args.record_checkout:
            result["verified_checkout"] = checkout_record(root, surface)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(intelligence.serialize_json(result), encoding="utf-8")
        if args.record_checkout:
            print("Verified context checkout: " + json.dumps(result["verified_checkout"], sort_keys=True))
        print("Benchmark: {} cases; {} mandatory failure(s); {} advisory miss(es).".format(
            len(result["cases"]), len(result["mandatory_failures"]), len(result["advisory_misses"])
        ))
        return 1 if result["mandatory_failures"] else 0
    except (OSError, ValueError) as exc:
        print("Repository intelligence benchmark error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
