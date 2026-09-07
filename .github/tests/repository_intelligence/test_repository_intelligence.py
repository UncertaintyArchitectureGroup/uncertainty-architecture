#!/usr/bin/env python3
"""Behavioral tests for deterministic repository intelligence."""

import importlib.util
import json
import os
import subprocess
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


def copy_runtime_files(root: Path) -> None:
    for relative in (
        ".github/scripts/repository_intelligence.py",
        ".github/scripts/validate_metadata.py",
        ".github/policy/repository-intelligence-contract.json",
    ):
        source = REPOSITORY_ROOT / relative
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source.read_bytes())


def materialize_repository(root: Path, duplicate_claim: bool = False) -> None:
    copy_runtime_files(root)
    metadata_contract: Dict[str, object] = {
        "required_frontmatter_paths": [
            "AGENTS.md",
            "DOCUMENT-METADATA.md",
            "00-doctrine/glossary.md",
            "01-patterns/thinking-system-review.md",
            "01-patterns/second-review.md",
            "content/research/research-register.md"
        ],
        "frontmatter_scan_roots": ["00-doctrine", "01-patterns", "content/research"],
        "frontmatter_scan_files": ["AGENTS.md", "DOCUMENT-METADATA.md"],
        "frontmatter_exclude_prefixes": ["content/research/notes/"]
    }
    write(root / ".github/policy/metadata-contract.json", json.dumps(metadata_contract, indent=2) + "\n")
    write(root / ".github/policy/repository-contract.json", "{\"contract_version\": 1}\n")
    write(
        root / "AGENTS.md",
        document(
            "Agent Router", "repository-guide", "repository", "repository-architecture",
            "ai-agent-repository-guide"
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
            "Document Metadata", "repository-process", "repository", "repository-architecture",
            "document-metadata"
        ),
    )
    write(
        root / "00-doctrine/glossary.md",
        document(
            "UA Glossary", "glossary", "doctrine", "thinking-systems", "doctrine-vocabulary",
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
            "Thinking System Review", "pattern", "patterns", "delivery-review", "delivery-release",
            source_path, body="See the [glossary](../00-doctrine/glossary.md) before release."
        ),
    )
    write(
        root / "01-patterns/second-review.md",
        document(
            "Second Review", "pattern", "patterns", "delivery-review", "second-review",
            body="Sibling artifact under the same root contributor scope."
        ),
    )
    if duplicate_claim:
        write(
            root / "01-patterns/duplicate.md",
            document(
                "Duplicate Review", "pattern", "patterns", "delivery-review", "delivery-release"
            ),
        )
    write(
        root / "content/research/research-register.md",
        document(
            "Research State Register", "research-index", "research", "provenance",
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
    write(root / ".github/workflows/repository-contract.yml", "name: Repository contract\n")
    write(root / ".github/workflows/change-coupling.yml", "name: Change coupling\n")
    write(root / ".github/workflows/metadata-integrity.yml", "name: Metadata integrity\n")
    write(root / ".github/workflows/link-integrity.yml", "name: Link integrity\n")
    write(root / ".github/tests/repository_intelligence/test_fixture.py", "# fixture test path\n")
    write(
        root / "package.json",
        json.dumps({"scripts": {"check:types": "tsc --noEmit", "test": "echo test", "build": "echo build"}}, indent=2) + "\n",
    )


def init_git(root: Path) -> str:
    subprocess.run(["git", "init", "-q"], cwd=str(root), check=True)
    subprocess.run(["git", "config", "user.email", "fixture@example.invalid"], cwd=str(root), check=True)
    subprocess.run(["git", "config", "user.name", "Fixture"], cwd=str(root), check=True)
    subprocess.run(["git", "add", "."], cwd=str(root), check=True)
    subprocess.run(["git", "commit", "-qm", "fixture baseline"], cwd=str(root), check=True)
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()


def commit_all(root: Path, message: str) -> str:
    subprocess.run(["git", "add", "-A"], cwd=str(root), check=True)
    subprocess.run(["git", "commit", "-qm", message], cwd=str(root), check=True)
    return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=str(root), text=True).strip()


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_projection_is_deterministic_and_materializations_share_identity() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-deterministic-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        first = RI.build_projection(root)
        second = RI.build_projection(root)
        assert_true(first == second, "repeated builds must be deterministic")
        agent = RI.materialize_agent_surface(first, contract)
        graph = RI.materialize_graph_view(first)
        assert_true(agent["source_identity"] == graph["source_identity"], "views must share source identity")
        assert_true(agent["producer"] == graph["producer"], "views must share producer identity")
        assert_true(
            len(agent["high_value_graph"]["edges"]) < len(graph["graph"]["edges"]),
            "compact view should omit bulk control/navigation graph payload"
        )
        assert_true(
            contract["compact_surface_path"] not in [item["path"] for item in first["source_identity"]["inputs"]],
            "generated compact surface must be non-self-referential"
        )


def test_term_and_artifact_preflight_keep_full_inventory() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-preflight-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        surface = RI.materialize_agent_surface(RI.build_projection(root), contract)
        terms = RI.term_preflight(surface, "Behavioral Software")
        term_inventory = {item["term"]: item for item in terms["inventory"]}
        assert_true("Thinking System" in term_inventory and "Model Judgment" in term_inventory, "full term inventory required")
        assert_true("Behavioral Software" in term_inventory["Thinking System"]["predecessors"], "predecessor must remain visible")
        artifacts = RI.artifact_preflight(surface, "delivery release")
        artifact_paths = {item["path"] for item in artifacts["inventory"]}
        assert_true(".github/REPOSITORY-INTELLIGENCE.md" in artifact_paths, "structural owner must be present")
        assert_true(artifacts["candidates"][0]["path"] == "01-patterns/thinking-system-review.md", "existing owner should rank first")


def test_edges_carry_class_role_direction_and_provenance() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-edge-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        graph = RI.build_projection(root)["graph"]
        assert_true(graph["edges"], "graph edges expected")
        assert_true(
            all(item.get("edge_class") and item.get("impact_role") and item.get("impact_direction") for item in graph["edges"]),
            "every edge must declare class, impact role, and direction"
        )
        assert_true(all(item.get("provenance", {}).get("path") for item in graph["edges"]), "every edge needs provenance")
        by_relation = {item["relation"]: item for item in graph["edges"]}
        assert_true(by_relation["LINKS_TO"]["impact_direction"] == "none", "navigation must not drive impact")
        assert_true(by_relation["SCOPED_BY"]["impact_role"] == "control", "scope must be control")
        assert_true(by_relation["SCOPED_BY"]["impact_direction"] == "both", "scope review relevance must be bidirectional")


def test_structural_control_traversal_is_first_order_and_no_sibling_fanout() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-impact-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        graph_view = RI.materialize_graph_view(RI.build_projection(root))
        result = RI.impact_for_paths(graph_view, ["01-patterns/thinking-system-review.md"])
        impacted = {item["id"] for item in result["impacted"]}
        assert_true("agent-scope:AGENTS.md" in impacted, "direct root scope should be review-relevant")
        assert_true("policy:.github/scripts/validate_metadata.py" in impacted, "direct validator should be review-relevant")
        assert_true(
            "document:01-patterns/second-review.md" not in impacted,
            "shared scope/validator must not connect sibling artifacts transitively"
        )


def test_deterministic_duplicate_signal_and_spaced_relation_path() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-signals-") as temporary:
        root = Path(temporary)
        materialize_repository(root, duplicate_claim=True)
        graph = RI.build_projection(root)["graph"]
        duplicate = [item for item in graph["signals"] if item["class"] == "duplicate-active-canonical-claim"]
        missing = [item for item in graph["signals"] if item["class"] == "missing-explicit-relation-target"]
        assert_true(duplicate and duplicate[0]["disposition"] == "blocking", "duplicate ownership must be blocking")
        assert_true(not missing, "space-containing source_basis path must resolve")
        assert_true(all(item["origin"] == "deterministic" for item in graph["signals"]), "persisted PR2 signals must be deterministic")


def test_compact_surface_verify_rejects_staleness() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-stale-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        surface_path = root / str(contract["compact_surface_path"])
        surface_path.parent.mkdir(parents=True, exist_ok=True)
        surface_path.write_text(
            RI.serialize_json(RI.materialize_agent_surface(RI.build_projection(root), contract)),
            encoding="utf-8"
        )
        assert_true(not RI.verify_surface(root, contract, surface_path), "fresh surface should verify")
        changed = root / "01-patterns/thinking-system-review.md"
        changed.write_text(changed.read_text(encoding="utf-8") + "\nMaterial change.\n", encoding="utf-8")
        errors = RI.verify_surface(root, contract, surface_path)
        assert_true(any("stale" in item.casefold() for item in errors), "material input change must stale surface")


def test_context_pack_routes_scoped_guidance_and_validation_without_full_graph() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-context-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        surface = RI.materialize_agent_surface(RI.build_projection(root), contract)
        result = RI.context_for_task(surface, ".github repository intelligence delivery release change")
        instructions = {item["path"] for item in result["instructions"]}
        assert_true("AGENTS.md" in instructions and ".github/AGENTS.md" in instructions, "scoped instructions should route")
        assert_true(result["graph_context"]["edges"], "compact high-value graph context expected")
        assert_true(
            ".github/scripts/validate_repository_contract.py" in result["validation_plan"]["validators"],
            "repository validator should be discoverable"
        )
        assert_true("CHANGELOG.md" in result["validation_plan"]["companion_candidates"], "companion should be visible")


def test_snapshot_reader_refuses_symlink_and_bounds_candidate_data() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-snapshot-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        baseline = init_git(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        with tempfile.TemporaryDirectory(prefix="ua-ri-materialized-") as out:
            info = RI.materialize_git_snapshot(root, baseline, Path(out), contract)
            assert_true(info["file_count"] > 0, "regular snapshot should materialize")
        os.symlink("00-doctrine/glossary.md", root / "candidate-link")
        symlink_ref = commit_all(root, "add symlink")
        with tempfile.TemporaryDirectory(prefix="ua-ri-materialized-") as out:
            try:
                RI.materialize_git_snapshot(root, symlink_ref, Path(out), contract)
            except RI.SnapshotBoundaryError as exc:
                assert_true("unsupported candidate file kind" in str(exc), "symlink must fail visibly")
            else:
                raise AssertionError("candidate symlink must not be trusted")


def test_trusted_comparison_rejects_self_change_and_head_behind_target() -> None:
    with tempfile.TemporaryDirectory(prefix="ua-ri-compare-") as temporary:
        root = Path(temporary)
        materialize_repository(root)
        accepted = init_git(root)
        contract = RI.load_contract(root / ".github/policy/repository-intelligence-contract.json")
        # Normal content-only descendant can be compared by the accepted producer.
        write(root / "01-patterns/thinking-system-review.md", (root / "01-patterns/thinking-system-review.md").read_text(encoding="utf-8") + "\nChanged.\n")
        proposed = commit_all(root, "content change")
        result = RI.compare_refs(root, accepted, proposed, "tested-merge", contract)
        assert_true(result["comparison_state"] == "complete", "content-only tested-merge comparison should complete")
        # Candidate interpretation self-change must not define its own trusted evidence.
        script = root / ".github/scripts/repository_intelligence.py"
        script.write_text(script.read_text(encoding="utf-8") + "\n# candidate semantic change\n", encoding="utf-8")
        self_change = commit_all(root, "producer change")
        unsupported = RI.compare_refs(root, accepted, self_change, "tested-merge", contract)
        assert_true(unsupported["comparison_state"] == "unsupported", "producer self-change must be unsupported")
        assert_true(".github/scripts/repository_intelligence.py" in unsupported["changed_interpretation_paths"], "changed producer path should be named")

        # Create another target commit from accepted and compare the older content branch as raw head.
        subprocess.run(["git", "checkout", "-q", accepted], cwd=str(root), check=True)
        write(root / "target-only.md", "target only\n")
        target_tip = commit_all(root, "target advance")
        head_only = RI.compare_refs(root, target_tip, proposed, "head", contract)
        assert_true(head_only["comparison_state"] == "unsupported" or head_only["comparison_state"] == "head-only", "behind-target raw head must never masquerade as merge state")
        tested = RI.compare_refs(root, target_tip, proposed, "tested-merge", contract)
        assert_true(tested["comparison_state"] == "incomplete", "behind-target raw head cannot be accepted as tested merge")


def main() -> int:
    tests = [
        test_projection_is_deterministic_and_materializations_share_identity,
        test_term_and_artifact_preflight_keep_full_inventory,
        test_edges_carry_class_role_direction_and_provenance,
        test_structural_control_traversal_is_first_order_and_no_sibling_fanout,
        test_deterministic_duplicate_signal_and_spaced_relation_path,
        test_compact_surface_verify_rejects_staleness,
        test_context_pack_routes_scoped_guidance_and_validation_without_full_graph,
        test_snapshot_reader_refuses_symlink_and_bounds_candidate_data,
        test_trusted_comparison_rejects_self_change_and_head_behind_target,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print("PASS: {}".format(test.__name__))
        except Exception as exc:
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
