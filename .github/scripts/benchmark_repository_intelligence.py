#!/usr/bin/env python3
"""Measure repository-intelligence retrieval; never score unobserved agent decisions.

The corpus is separate from the producer. Mandatory cases check deterministic
contracts; paraphrase misses remain visible observations rather than hidden
translations or evidence that a new conceptual owner is needed.
"""

import argparse
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


def load_cases(path):
    corpus = intelligence.load_json(path, "Benchmark corpus")
    if corpus.get("version") != 1 or not isinstance(corpus.get("cases"), list) or not corpus["cases"]:
        raise ValueError("Benchmark corpus requires version 1 and nonempty cases")
    seen = set()
    list_fields = ("expected_paths", "expected_terms", "expected_instructions", "expected_validators", "expected_companions", "inventory_paths", "evidence_sources")
    for case in corpus["cases"]:
        if not isinstance(case, dict) or not isinstance(case.get("id"), str) or not case["id"] or case["id"] in seen:
            raise ValueError("Benchmark case IDs must be nonempty and unique")
        seen.add(case["id"])
        if case.get("operation") not in OPERATIONS or not isinstance(case.get("query"), str) or not case["query"]:
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
        if not any(case.get(field) for field in list_fields[:-1]):
            raise ValueError("Benchmark case needs an observable expectation: " + case["id"])
    return corpus


def evaluate(surface, case, query):
    result = getattr(intelligence, case["operation"])(surface, query)
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


def run_benchmark(root, cases_path, surface_path):
    corpus = load_cases(cases_path)
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
        "benchmark_version": 1,
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


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--cases", type=Path, default=DEFAULT_CASES)
    parser.add_argument("--surface", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        surface = args.surface or root / "assets/repository-intelligence/agent-context.json"
        result = run_benchmark(root, args.cases, surface)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(intelligence.serialize_json(result), encoding="utf-8")
        print("Benchmark: {} cases; {} mandatory failure(s); {} advisory miss(es).".format(
            len(result["cases"]), len(result["mandatory_failures"]), len(result["advisory_misses"])
        ))
        return 1 if result["mandatory_failures"] else 0
    except (OSError, ValueError) as exc:
        print("Repository intelligence benchmark error: {}".format(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
