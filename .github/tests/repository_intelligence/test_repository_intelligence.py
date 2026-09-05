#!/usr/bin/env python3
"""Behavioral tests for the deterministic repository-intelligence projection."""

import importlib.util
import json
import sys
import tempfile
from pathlib import Path
from typing import Dict

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
SCRIPT_PATH = REPOSITORY_ROOT / ".github/scripts/repository_intelligence.py"


def load_module():
    spec = importlib.util.spec_from_file_location("repository_intelligence", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load repository intelligence producer")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RI = load_module()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def document(
    title: str,
    artifact_type: str,
    module: str,
    topic: str,
    canonical_for: str = "",
    source_basis: str = "",
    body: str = "Fixture body.",
) -> str:
    canonical = ""
    if canonical_for:
        canonical = "canonical_for:\n  - {}\n".format(canonical_for)
    source = ""
    if source_basis:
        source = 'source_basis:\n  - "{}"\n'.format(source_basis)
    return """---
title: {title}
artifact_type: {artifact_type}
status: informative
maturity: active
module: {module}
topics:
  - {topic}
tags:
  - ua/module/{module}
  - ua/type/{artifact_type}
  - ua/status/informative
  - ua/topic/{topic}
{canonical}{source}---

# {title}

{body}
""".format(
        title=title,
        artifact_type=artifact_type,
        module=module,
        topic=topic,
        canonical=canonical,
        source=source,
        body=body,
    )


def materialize_repository(root: Path, duplicate_claim: bool = False) -> None:
    contract: Dict[str, object] = {
        "required_frontmatter_paths": [
            "AGENTS.md",
            "DOCUMENT-METADATA.md",
            "00-doctrine/glossary.md",
            "01-patterns/thinking-system-review.md",
            "content/research/research-register.md",
        ],
        "frontmatter_scan_roots": ["00-doctrine", "01-patterns", "content/research"],
        "frontmatter_scan_files": ["AGENTS.md", "DOCUMENT-METADATA.md"],
        "frontmatter_exclude_prefixes": ["content/research/notes/"],
    }
    write(root / ".github/policy/metadata-contract.json", json.dumps(contract, indent=2) + "\n")
    write(root / ".github/policy/repository-contract.json", "{\"contract_version\": 1}\n")
    write(
        root / "AGENTS.md",
        document(
            "Agent Router",
            "repository-guide",
            "repository",
            "repository-architecture",
            "ai-agent-repository-guide",
        ),
    )
    write(root / ".github/AGENTS.md", "# Scoped GitHub agent instructions\n")
    write(
        root / ".github/REPOSITORY-INTELLIGENCE.md",
        "# Repository Intelligence\n\nFrontmatter-free structural owner fixture.\n",
    )
    write(
        root / "DOCUMENT-METADATA.md",
        document(
            "Document Metadata",
            "repository-process",
            "repository",
            "repository-architecture",
            "document-metadata",
        ),
    )
    write(
        root / "00-doctrine/glossary.md",
        document(
            "UA Glossary",
            "glossary",
            "doctrine",
            "thinking-systems",
            "doctrine-vocabulary",
            body="""### Thinking System

Current category. Earlier UA publications used **Behavioral Software** and **Behavioral Applications**; those names remain historical predecessors.

### Model Judgment

Probabilistic judgment used by the system.
""",
        ),
    )
    source_path = "../content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
    write(
        root / "content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf",
        "fixture-binary-placeholder\n",
    )
    write(
        root / "01-patterns/thinking-system-review.md",
        document(
            "Thinking System Review",
            "pattern",
            "patterns",
            "delivery-review",
            "delivery-release",
            source_path,
            body="See the [glossary](../00-doctrine/glossary.md) before release.",
        ),
    )
    if duplicate_claim:
        write(
            root / "01-patterns/duplicate.md",
            document(
                "Duplicate Review",
                "pattern",
                "patterns",
                "delivery-review",
                "delivery-release",
            ),
        )
    write(
        root / "content/research/research-register.md",
        document(
            "Research State Register",
            "research-index",
            "research",
            "provenance",
            "research-state-register",
            body="""<!-- ua-research-register
{
  "version": 1,
  "items": [
    {
      "id": "TS-TEST-001",
      "title": "Fixture hypothesis",
      "item_class": "hypothesis",
      "status": "open",
      "origin_kind": "repository-source",
      "provenance_record": "00-doctrine/glossary.md",
      "owning_record": "01-patterns/thinking-system-review.md",
      "framework_destination": "00-doctrine/glossary.md",
      "next_step": "Test the fixture."
    }
  ]
}
-->
""",
        ),
    )
    write(root / ".github/scripts/validate_repository_contract.py", "# fixture validator\n")
    write(root / ".github/scripts/validate_change_coupling.py", "# fixture validator\n")
    write(root / ".github/scripts/validate_code_quality.py", "# fixture validator\n")
    write(root / ".github/scripts/validate_metadata.py", "# fixture validator\n")
    write(root / ".github/workflows/repository-contract.yml", "name: Repository contract\n")
    write(root / ".github/workflows/change-coupling.yml", "name: Change coupling\n")
    write(root / ".github/workflows/metadata-integrity.yml", "name: Metadata integrity\n")
    write(root / ".github/workflows/link-integrity.yml", "name: Link integrity\n")
    write(
        root / ".github/tests/repository_intelligence/test_fixture.py",
        "# fixture test path\n",
    )
    write(
        root / "package.json",
        json.dumps(
            {"scripts": {"check:types": "tsc --noEmit", "test": "echo test", "build": "echo build"}},
            indent=2,
        )
        + "\n",
    )


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_surface_is_deterministic_and_non_self_referential() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-deterministic-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        first = RI.build_surface(root)
        second = RI.build_surface(root)
        assert_true(first == second, "repeated builds must be deterministic")
        inputs = first["source_identity"]["inputs"]
        assert_true(
            ".github/agent-context.json" not in inputs,
            "generated surface must not participate in its own source digest",
        )
        write(root / ".github/agent-context.json", "{\"ignored\": true}\n")
        third = RI.build_surface(root)
        assert_true(first == third, "changing only generated output must not change the projection")


def test_term_preflight_keeps_full_inventory_and_historical_predecessors() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-terms-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        result = RI.term_preflight(RI.build_surface(root), "Behavioral Software")
        inventory = {item["term"]: item for item in result["inventory"]}
        assert_true("Thinking System" in inventory, "canonical term inventory must be complete")
        assert_true("Model Judgment" in inventory, "full inventory must precede ranking")
        assert_true(
            "Behavioral Software" in inventory["Thinking System"]["predecessors"],
            "explicit historical predecessor must remain visible",
        )
        assert_true(
            result["candidates"] and result["candidates"][0]["term"] == "Thinking System",
            "historical predecessor query should route to the current canonical term",
        )


def test_artifact_preflight_keeps_structural_owner_and_existing_claim() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-artifacts-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        surface = RI.build_surface(root)
        artifact_paths = {item["path"] for item in surface["inventories"]["artifacts"]}
        assert_true(
            ".github/REPOSITORY-INTELLIGENCE.md" in artifact_paths,
            "frontmatter-free structural repository owner must remain in the shared inventory",
        )
        result = RI.artifact_preflight(surface, "delivery release")
        assert_true(result["inventory"], "full maintained-artifact inventory is required")
        assert_true(
            result["candidates"]
            and result["candidates"][0]["path"] == "01-patterns/thinking-system-review.md",
            "exact canonical_for evidence should surface the existing owner candidate",
        )


def test_find_owner_preserves_machine_and_semantic_evidence_roles() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-owner-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        result = RI.find_owner(RI.build_surface(root), "delivery release")
        roles = {item["role"] for item in result["candidates"]}
        assert_true(
            "machine_responsibility_claim" in roles,
            "explicit canonical_for evidence must stay distinct from semantic ownership",
        )
        assert_true(
            "semantic_owner_candidate" in roles,
            "semantic owner candidate must not be collapsed into metadata authority",
        )


def test_graph_has_typed_edges_and_provenance_for_shared_consumers() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-graph-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        graph = RI.build_surface(root)["graph"]
        families = {node["family"] for node in graph["nodes"]}
        assert_true(
            {"Document", "Term", "AgentScope", "ResearchItem", "PolicyOrValidator"}.issubset(families),
            "shared projection must expose the baseline node families",
        )
        relation_types = {item["relation"] for item in graph["edges"]}
        for required in (
            "DEFINES",
            "CANONICAL_FOR",
            "SCOPED_BY",
            "SOURCE_BASIS",
            "RESEARCH_OWNER",
            "FRAMEWORK_DESTINATION",
        ):
            assert_true(required in relation_types, "missing typed edge {}".format(required))
        assert_true(
            all(item.get("provenance", {}).get("path") for item in graph["edges"]),
            "every explicit edge must expose deterministic provenance",
        )
        missing_relation_signals = [
            item for item in graph["signals"] if item["class"] == "missing-explicit-relation-target"
        ]
        assert_true(
            not missing_relation_signals,
            "space-containing repository-local source_basis must resolve without a false defect",
        )


def test_duplicate_canonical_claim_becomes_deterministic_blocking_signal() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-signals-") as temporary:
        root = Path(temporary)
        materialize_repository(root, duplicate_claim=True)
        signals = RI.build_surface(root)["graph"]["signals"]
        matches = [item for item in signals if item["class"] == "duplicate-active-canonical-claim"]
        assert_true(matches, "duplicate explicit ownership must create a deterministic signal")
        assert_true(matches[0]["origin"] == "deterministic", "signal origin must remain explicit")
        assert_true(matches[0]["disposition"] == "blocking", "objective duplicate ownership is blocking")


def test_verify_rejects_stale_committed_surface() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-stale-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        surface_path = root / ".github/agent-context.json"
        surface_path.write_text(RI.serialize_surface(RI.build_surface(root)), encoding="utf-8")
        assert_true(not RI.verify_surface(root, surface_path), "fresh surface should verify")
        changed = root / "01-patterns/thinking-system-review.md"
        changed.write_text(changed.read_text(encoding="utf-8") + "\nMaterial change.\n", encoding="utf-8")
        errors = RI.verify_surface(root, surface_path)
        assert_true(errors, "material input change must stale the committed surface")
        assert_true(any("stale" in item.casefold() for item in errors), "failure should explain staleness")


def test_context_pack_routes_scoped_guidance_graph_and_validation() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-context-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        surface = RI.build_surface(root)
        result = RI.context_for_task(surface, ".github repository intelligence delivery release change")
        instruction_paths = {item["path"] for item in result["instructions"]}
        assert_true("AGENTS.md" in instruction_paths, "root guidance must always be routed")
        assert_true(".github/AGENTS.md" in instruction_paths, "scoped GitHub guidance must be routed")
        assert_true(result["graph_context"]["nodes"], "context pack should include local graph evidence")
        plan = result["validation_plan"]
        assert_true(
            ".github/scripts/validate_repository_contract.py" in plan["validators"],
            "repository-policy validator should be discoverable",
        )
        assert_true(
            ".github/workflows/metadata-integrity.yml" in plan["workflows"],
            "context-surface validation workflow should be discoverable",
        )
        assert_true("CHANGELOG.md" in plan["companion_candidates"], "notable policy companion should be visible")


def main() -> int:
    tests = [
        test_surface_is_deterministic_and_non_self_referential,
        test_term_preflight_keeps_full_inventory_and_historical_predecessors,
        test_artifact_preflight_keeps_structural_owner_and_existing_claim,
        test_find_owner_preserves_machine_and_semantic_evidence_roles,
        test_graph_has_typed_edges_and_provenance_for_shared_consumers,
        test_duplicate_canonical_claim_becomes_deterministic_blocking_signal,
        test_verify_rejects_stale_committed_surface,
        test_context_pack_routes_scoped_guidance_graph_and_validation,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print("PASS: {}".format(test.__name__))
        except Exception as exc:  # standalone regression harness needs aggregate reporting
            failures.append("{}: {}".format(test.__name__, exc))
    if failures:
        print("Repository intelligence tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Repository intelligence tests passed: {} behavioral cases.".format(len(tests)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
