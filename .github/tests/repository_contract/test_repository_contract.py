#!/usr/bin/env python3
"""Regression tests for the machine-readable repository contract."""

import importlib.util
import json
import shutil
import sys
import tempfile
from pathlib import Path
from typing import Dict, List, Set

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_repository_contract.py"
CONTRACT_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract.json"
EXTENSION_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract-change-coupling.json"
CASES_PATH = Path(__file__).with_name("cases.json")

REQUIRED_CASE_NAMES: Set[str] = {
    "valid synthetic repository passes",
    "critical file deletion is rejected",
    "critical README section deletion is rejected",
    "protected attribution text deletion is rejected",
    "required canonical link deletion is rejected",
    "unexpected top-level directory is rejected",
    "unexpected top-level file is rejected",
    "legacy runtime anchor deletion is rejected",
    "compatibility path deletion is rejected",
    "immutable documentation license modification is rejected",
    "CODEOWNERS default ownership deletion is rejected",
    "PR contract marker deletion is rejected",
    "AI contributor coupling protocol deletion is rejected",
    "code contribution contract deletion is rejected",
    "Quartz architecture map deletion is rejected",
    "changed code quality validator deletion is rejected",
    "code quality regression suite deletion is rejected",
    "NUL-safe changed path parsing deletion is rejected",
    "code quality workflow step deletion is rejected",
    "TypeScript static-analysis workflow step deletion is rejected",
    "Quartz TypeScript regression command deletion is rejected",
    "TypeScript static-analysis command deletion is rejected",
    "bounded format command deletion is rejected",
    "Quartz global type declarations deletion is rejected",
    "Quartz SCSS and event declarations deletion is rejected",
    "Quartz upstream provenance baseline deletion is rejected",
    "CITATION author deletion is rejected",
    "link-integrity citation step deletion is rejected",
    "metadata workflow job deletion is rejected",
    "PDF export regression step deletion is rejected",
    "manual publication export workflow deletion is rejected",
    "platform rendition workflow deletion is rejected",
    "explicit generic PDF entrypoint deletion is rejected",
    "curated working-paper command deletion is rejected",
    "package script JSON formatting is ignored",
    "package script moved outside scripts is rejected",
    "manual PDF workflow default article deletion is rejected",
    "manual PDF workflow working-paper route deletion is rejected",
    "publication path safety helper deletion is rejected",
    "publication provenance helper deletion is rejected",
    "Figure 8 fingerprint helper deletion is rejected",
    "Figure 8 readability policy deletion is rejected",
    "Figure 8 desktop asset verifier deletion is rejected",
    "Figure 8 separate-page PDF verification deletion is rejected",
    "publication integration provenance ref deletion is rejected",
    "publication pair verification deletion is rejected",
    "publication finalization regression file deletion is rejected",
    "publication manifest source commit field deletion is rejected",
    "publication strict manifest verification deletion is rejected",
    "publication-grade regression test deletion is rejected",
    "curated publication author fallback deletion is rejected",
    "change coupling workflow deletion is rejected",
    "navigation routing declaration deletion is rejected",
    "self-test manifest deletion is rejected",
    "preferred citation author deletion is rejected",
    "README evidence boundary deletion is rejected",
    "README BibTeX author deletion is rejected",
    "README advisor attribution deletion is rejected",
}


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_repository_contract", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load repository contract validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def write_text(path: Path, text: str = "fixture\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def decode_pointer_token(token: str) -> str:
    return token.replace("~1", "/").replace("~0", "~")


def pointer_tokens(pointer: str) -> List[str]:
    if not pointer.startswith("/"):
        raise ValueError("JSON pointer must start with '/': {}".format(pointer))
    return [decode_pointer_token(token) for token in pointer[1:].split("/")]


def get_json_pointer(document: object, pointer: str) -> object:
    current = document
    for token in pointer_tokens(pointer):
        if isinstance(current, dict):
            current = current[token]
        elif isinstance(current, list):
            current = current[int(token)]
        else:
            raise KeyError(pointer)
    return current


def set_json_pointer(document: object, pointer: str, value: object) -> object:
    tokens = pointer_tokens(pointer)
    if not isinstance(document, dict):
        document = {}
    current = document
    for token in tokens[:-1]:
        next_value = current.get(token)
        if not isinstance(next_value, dict):
            next_value = {}
            current[token] = next_value
        current = next_value
    current[tokens[-1]] = value
    return document


def delete_json_pointer(document: object, pointer: str) -> object:
    tokens = pointer_tokens(pointer)
    current = document
    for token in tokens[:-1]:
        if not isinstance(current, dict) or token not in current:
            return document
        current = current[token]
    if isinstance(current, dict):
        current.pop(tokens[-1], None)
    return document


def materialize_rules(root: Path, rules: Dict[str, object]) -> None:
    for required in rules.get("required_paths", []):
        path = root / required["path"]
        if required["type"] == "directory":
            path.mkdir(parents=True, exist_ok=True)
        elif not path.exists():
            write_text(path)
    for rule in rules.get("critical_files", []):
        path = root / rule["path"]
        required_json = rule.get("required_json", [])
        if required_json:
            document: object = {}
            if path.exists():
                try:
                    document = json.loads(path.read_text(encoding="utf-8"))
                except json.JSONDecodeError:
                    document = {}
            for check in required_json:
                document = set_json_pointer(
                    document, str(check["pointer"]), check.get("equals")
                )
            write_text(path, json.dumps(document, indent=2) + "\n")

        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        parts: List[str] = []
        parts.extend(rule.get("required_headings", []))
        parts.extend(rule.get("required_text", []))
        parts.extend("[fixture]({})".format(target) for target in rule.get("required_links", []))
        if parts:
            addition = "\n\n".join(parts) + "\n"
            write_text(path, existing + addition)


def materialize_valid_repository(root: Path, contract: Dict[str, object], extension: Dict[str, object]) -> None:
    allowed = contract["allowed_top_level"]
    for directory in allowed["directories"]:
        (root / directory).mkdir(parents=True, exist_ok=True)
    for filename in allowed["files"]:
        write_text(root / filename)

    materialize_rules(root, contract)
    materialize_rules(root, extension)

    for immutable in contract["immutable_files"]:
        source = REPOSITORY_ROOT / immutable["path"]
        destination = root / immutable["path"]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(str(source), str(destination))

    for marker in contract["protected_markers"]:
        path = root / marker["path"]
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        write_text(path, existing + marker["text"] + "\n")


def apply_mutation(root: Path, mutation: Dict[str, str]) -> None:
    mutation_type = mutation["type"]
    if mutation_type == "none":
        return
    path = root / mutation["path"]
    if mutation_type == "delete_path":
        if path.is_dir():
            shutil.rmtree(str(path))
        elif path.exists():
            path.unlink()
        return
    if mutation_type == "remove_text":
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(mutation["text"], "", 1), encoding="utf-8")
        return
    if mutation_type == "append_text":
        with path.open("a", encoding="utf-8") as handle:
            handle.write(mutation["text"])
        return
    if mutation_type == "add_directory":
        path.mkdir(parents=True, exist_ok=True)
        return
    if mutation_type == "add_file":
        write_text(path)
        return
    if mutation_type == "format_json_compact":
        document = json.loads(path.read_text(encoding="utf-8"))
        path.write_text(
            json.dumps(document, separators=(",", ":")) + "\n",
            encoding="utf-8",
        )
        return
    if mutation_type == "delete_json_pointer":
        document = json.loads(path.read_text(encoding="utf-8"))
        document = delete_json_pointer(document, mutation["pointer"])
        path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
        return
    if mutation_type == "move_json_pointer":
        document = json.loads(path.read_text(encoding="utf-8"))
        value = get_json_pointer(document, mutation["pointer"])
        document = delete_json_pointer(document, mutation["pointer"])
        document = set_json_pointer(document, mutation["destination"], value)
        path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
        return
    raise ValueError("Unsupported fixture mutation: {}".format(mutation_type))


def validate_case_manifest(cases: List[Dict[str, object]]) -> List[str]:
    names = [str(case.get("name", "")) for case in cases]
    errors: List[str] = []
    missing = sorted(REQUIRED_CASE_NAMES - set(names))
    if missing:
        errors.append("missing required cases: {}".format(", ".join(missing)))
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append("duplicate case names: {}".format(", ".join(duplicates)))
    unnamed = [str(index) for index, name in enumerate(names, start=1) if not name]
    if unnamed:
        errors.append("unnamed cases at positions: {}".format(", ".join(unnamed)))
    return errors


def main() -> int:
    validator = load_validator()
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    extension = json.loads(EXTENSION_PATH.read_text(encoding="utf-8"))
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))["cases"]
    failures = validate_case_manifest(cases)

    for case in cases:
        with tempfile.TemporaryDirectory(prefix="ua-contract-") as temporary:
            root = Path(temporary)
            materialize_valid_repository(root, contract, extension)
            apply_mutation(root, case["mutation"])
            errors = validator.validate(root, CONTRACT_PATH, (EXTENSION_PATH,))

        if case.get("expected_valid"):
            if errors:
                failures.append("{}: expected success, got {}".format(case["name"], errors))
            else:
                print("PASS: {}".format(case["name"]))
            continue
        expected = case["expected_error"]
        if not any(expected in error for error in errors):
            failures.append("{}: expected error containing {!r}, got {}".format(case["name"], expected, errors))
        else:
            print("PASS: {}".format(case["name"]))

    if failures:
        print("Repository contract self-tests failed:")
        for failure in failures:
            print("- {}".format(failure))
        return 1
    print("Repository contract self-tests passed: {} regression fixtures.".format(len(cases)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
