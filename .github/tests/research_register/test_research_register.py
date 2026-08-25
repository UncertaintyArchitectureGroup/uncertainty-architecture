#!/usr/bin/env python3
"""Regression tests for the Active Research Register validator."""

import importlib.util
import json
import tempfile
from pathlib import Path
from typing import Dict, List

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_research_register.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_research_register", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load research-register validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def block(items: List[Dict[str, object]]) -> str:
    return "# Active Research Register\n\n<!-- ua-research-register\n{}\n-->\n".format(
        json.dumps({"version": 1, "items": items}, indent=2)
    )


def valid_item() -> Dict[str, object]:
    return {
        "id": "TS-TERM-001",
        "title": "Thinking Systems formulation provenance",
        "item_class": "term",
        "status": "active",
        "origin_kind": "external-dialogue",
        "provenance_record": "content/research/notes/provenance.md",
        "owning_record": "00-doctrine/glossary.md",
        "next_step": "Preserve the provenance boundary.",
    }


def run_case(name: str, mutate, expected_fragment: str = "") -> str:
    validator = load_validator()
    with tempfile.TemporaryDirectory(prefix="ua-research-register-") as temporary:
        root = Path(temporary)
        item = valid_item()
        items = [item]
        register_text = block(items)
        write(root / "content/research/research-register.md", register_text)
        write(root / "content/research/notes/provenance.md", "# Provenance\n")
        write(root / "content/research/notes/README.md", "- [provenance.md](provenance.md)\n")
        write(root / "00-doctrine/glossary.md", "# Glossary\n")

        mutate(root, items)
        if items != [item] or (root / "content/research/research-register.md").read_text(encoding="utf-8") == register_text:
            write(root / "content/research/research-register.md", block(items))

        findings = validator.validate(
            root,
            root / "content/research/research-register.md",
            root / "content/research/notes/README.md",
        )
        messages = "\n".join(f.message for f in findings)
        if expected_fragment:
            if expected_fragment not in messages:
                return "{}: expected {!r}, got {!r}".format(name, expected_fragment, messages)
        elif any(f.severity == "error" for f in findings):
            return "{}: expected valid register, got {!r}".format(name, messages)
        print("PASS: {}".format(name))
        return ""


def main() -> int:
    failures: List[str] = []

    failures.append(run_case("valid register passes", lambda root, items: None))

    def duplicate(root: Path, items: List[Dict[str, object]]) -> None:
        items.append(dict(items[0]))
    failures.append(run_case("duplicate ID rejected", duplicate, "duplicate research-item ID"))

    def bad_status(root: Path, items: List[Dict[str, object]]) -> None:
        items[0]["status"] = "maybe"
    failures.append(run_case("uncontrolled status rejected", bad_status, "uncontrolled status"))

    def missing_provenance(root: Path, items: List[Dict[str, object]]) -> None:
        (root / "content/research/notes/provenance.md").unlink()
    failures.append(run_case("missing provenance record rejected", missing_provenance, "provenance_record does not exist"))

    def unindexed(root: Path, items: List[Dict[str, object]]) -> None:
        write(root / "content/research/notes/README.md", "# Notes\n")
    failures.append(run_case("external provenance must be indexed", unindexed, "provenance record is not indexed"))

    def outside_notes(root: Path, items: List[Dict[str, object]]) -> None:
        write(root / "content/research/provenance.md", "# Provenance\n")
        items[0]["provenance_record"] = "content/research/provenance.md"
    failures.append(run_case("external provenance must use notes", outside_notes, "external origin must use a bounded provenance record"))

    failures = [failure for failure in failures if failure]
    if failures:
        print("Research-register self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1

    print("Research-register self-tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
