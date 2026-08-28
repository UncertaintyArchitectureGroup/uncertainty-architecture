#!/usr/bin/env python3
"""One-shot cleanup for PR #93 after the Medium transport experiment."""

import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected one replacement anchor, found {text.count(old)}")
    return text.replace(old, new, 1)


def update_validator() -> None:
    path = ROOT / ".github/scripts/validate_repository_contract.py"
    text = subprocess.check_output(
        ["git", "show", "origin/main:.github/scripts/validate_repository_contract.py"],
        cwd=ROOT,
        text=True,
    )
    helpers = '''\n\n_MISSING = object()\n\n\ndef decode_json_pointer_token(token: str) -> str:\n    return token.replace("~1", "/").replace("~0", "~")\n\n\ndef resolve_json_pointer(document: object, pointer: str) -> object:\n    """Resolve an RFC 6901 JSON Pointer without recursive key matching."""\n    if pointer == "":\n        return document\n    if not pointer.startswith("/"):\n        return _MISSING\n    current = document\n    for raw_token in pointer[1:].split("/"):\n        token = decode_json_pointer_token(raw_token)\n        if isinstance(current, dict):\n            if token not in current:\n                return _MISSING\n            current = current[token]\n            continue\n        if isinstance(current, list):\n            try:\n                index = int(token)\n            except ValueError:\n                return _MISSING\n            if index < 0 or index >= len(current):\n                return _MISSING\n            current = current[index]\n            continue\n        return _MISSING\n    return current\n\n\ndef validate_required_json(\n    relative: str,\n    path: Path,\n    text: str,\n    rules: Iterable[Dict[str, object]],\n    errors: List[str],\n) -> None:\n    checks = list(rules)\n    if not checks:\n        return\n    if path.suffix.lower() != ".json":\n        errors.append("{}: structured contract checks require a JSON file".format(relative))\n        return\n    try:\n        document = json.loads(text)\n    except json.JSONDecodeError as exc:\n        errors.append("{}: invalid JSON for structured contract checks: {}".format(relative, exc))\n        return\n    for check in checks:\n        pointer = check.get("pointer")\n        if not isinstance(pointer, str):\n            errors.append("{}: structured contract entry lacks a JSON pointer".format(relative))\n            continue\n        expected = check.get("equals")\n        actual = resolve_json_pointer(document, pointer)\n        if actual is _MISSING or actual != expected:\n            errors.append("{}: JSON pointer {!r} must equal {!r}".format(relative, pointer, expected))\n'''
    text = replace_once(text, "\n\ndef validate_top_level(", helpers + "\n\ndef validate_top_level(", "validator helpers")
    old = '''        for marker in rule.get("required_text", []):\n            if marker not in text:\n                errors.append("{}: missing protected text {!r}".format(relative, marker))\n        targets = markdown_link_targets(text)\n'''
    new = '''        for marker in rule.get("required_text", []):\n            if marker not in text:\n                errors.append("{}: missing protected text {!r}".format(relative, marker))\n        validate_required_json(relative, path, text, rule.get("required_json", []), errors)\n        targets = markdown_link_targets(text)\n'''
    text = replace_once(text, old, new, "validator hook")
    path.write_text(text, encoding="utf-8")


def update_contract() -> None:
    path = ROOT / ".github/policy/repository-contract-change-coupling.json"
    contract = json.loads(path.read_text(encoding="utf-8"))
    critical = {rule["path"]: rule for rule in contract["critical_files"]}
    scripts = {
        "pdf": "node quartz/scripts/export-pdf.mjs",
        "pdf:article": "node quartz/scripts/render-publication-pdf.mjs content/research/notes/thinking-systems-publication-draft.md --output dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf",
        "pdf:working-paper": "node quartz/scripts/render-publication-pdf.mjs content/research/notes/open-engineering-specification-article-draft.md --output dist/pdf/uncertainty-architecture-thinking-systems-working-paper.pdf --no-split-dense",
        "pdf:verify:figure8": "node quartz/scripts/verify-publication-figure8.mjs",
        "publication:platforms": "node quartz/scripts/render-platform-renditions.mjs",
        "publication:protect-links": "node quartz/scripts/protect-platform-heading-links.mjs",
        "publication:furniture": "node quartz/scripts/render-platform-furniture.mjs",
        "publication:copy-ready": "node quartz/scripts/render-copy-ready.mjs",
        "publication:bundle": "npm run publication:assets && npm run publication:platforms && npm run publication:protect-links && npm run publication:furniture && npm run publication:copy-ready",
        "publication:verify-package": "node quartz/scripts/verify-publication-package.mjs",
    }
    package_rule = critical["package.json"]
    package_rule["required_text"] = [m for m in package_rule.get("required_text", []) if not m.startswith('"pdf') and not m.startswith('"publication:')]
    package_rule["required_json"] = [{"pointer": f"/scripts/{name}", "equals": value} for name, value in scripts.items()]
    critical["quartz/scripts/render-copy-ready.mjs"]["required_text"] = ["embedLocalImages", "buildMediumUploadPlan", "medium_manual_upload_required", "medium_clipboard_images_supported: false", "embedded-data-uri-preview", "medium/upload/README.md", "data:image/png;base64", "manual-select-all-copy", "javascript_copy_controls: false"]
    critical["quartz/scripts/render-copy-ready.test.mjs"]["required_text"] = ["copy-ready HTML embeds local images as data URIs", "copy-ready document exposes one article-only copy surface", "Medium upload plan is hero plus nine figures in deterministic order"]
    critical["quartz/scripts/verify-publication-package.mjs"]["required_text"] = ["assertPlatformFigureInventory", "assertMediumUploadManifest", 'publication_state === "candidate"', "publication_ready === false", "Figure 8A and Figure 8B must travel together", "Medium clipboard image transfer must not be claimed", "medium/upload/00-medium-hero.png", "copy-ready HTML contains obsolete copy controls"]
    critical["quartz/scripts/verify-publication-package.test.mjs"]["required_text"] = ["platform verifier requires nine figures with Figure 8A and 8B coupled", "platform verifier rejects incomplete Figure 8 coupling", "Medium upload manifest requires ten ordered images plus instructions", "Medium upload manifest rejects any claim that clipboard images are supported"]
    path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")


def update_cases() -> None:
    path = ROOT / ".github/tests/repository_contract/cases.json"
    document = json.loads(path.read_text(encoding="utf-8"))
    cases = document["cases"]
    cases[:] = [case for case in cases if case.get("name") not in {"package script JSON formatting is ignored", "package script moved outside scripts is rejected"}]
    by_name = {case["name"]: case for case in cases}
    by_name["explicit generic PDF entrypoint deletion is rejected"].update({"mutation": {"type": "delete_json_pointer", "path": "package.json", "pointer": "/scripts/pdf"}, "expected_error": "package.json: JSON pointer '/scripts/pdf'"})
    by_name["curated working-paper command deletion is rejected"].update({"mutation": {"type": "delete_json_pointer", "path": "package.json", "pointer": "/scripts/pdf:working-paper"}, "expected_error": "package.json: JSON pointer '/scripts/pdf:working-paper'"})
    cases.extend([
        {"name": "package script JSON formatting is ignored", "mutation": {"type": "format_json_compact", "path": "package.json"}, "expected_valid": True},
        {"name": "package script moved outside scripts is rejected", "mutation": {"type": "move_json_pointer", "path": "package.json", "pointer": "/scripts/publication:bundle", "destination": "/publication:bundle"}, "expected_error": "package.json: JSON pointer '/scripts/publication:bundle'"},
    ])
    path.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")


def update_contract_tests() -> None:
    path = ROOT / ".github/tests/repository_contract/test_repository_contract.py"
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, '    "curated working-paper command deletion is rejected",\n', '    "curated working-paper command deletion is rejected",\n    "package script JSON formatting is ignored",\n    "package script moved outside scripts is rejected",\n', "required cases")
    helpers = '''\n\ndef decode_pointer_token(token: str) -> str:\n    return token.replace("~1", "/").replace("~0", "~")\n\n\ndef pointer_tokens(pointer: str) -> List[str]:\n    if not pointer.startswith("/"):\n        raise ValueError("JSON pointer must start with '/': {}".format(pointer))\n    return [decode_pointer_token(token) for token in pointer[1:].split("/")]\n\n\ndef get_json_pointer(document: object, pointer: str) -> object:\n    current = document\n    for token in pointer_tokens(pointer):\n        if isinstance(current, dict):\n            current = current[token]\n        elif isinstance(current, list):\n            current = current[int(token)]\n        else:\n            raise KeyError(pointer)\n    return current\n\n\ndef set_json_pointer(document: object, pointer: str, value: object) -> object:\n    tokens = pointer_tokens(pointer)\n    if not isinstance(document, dict):\n        document = {}\n    current = document\n    for token in tokens[:-1]:\n        next_value = current.get(token)\n        if not isinstance(next_value, dict):\n            next_value = {}\n            current[token] = next_value\n        current = next_value\n    current[tokens[-1]] = value\n    return document\n\n\ndef delete_json_pointer(document: object, pointer: str) -> object:\n    tokens = pointer_tokens(pointer)\n    current = document\n    for token in tokens[:-1]:\n        if not isinstance(current, dict) or token not in current:\n            return document\n        current = current[token]\n    if isinstance(current, dict):\n        current.pop(tokens[-1], None)\n    return document\n'''
    text = replace_once(text, "\n\ndef materialize_rules(", helpers + "\n\ndef materialize_rules(", "test helpers")
    old_materialize = '''    for rule in rules.get("critical_files", []):\n        path = root / rule["path"]\n        existing = path.read_text(encoding="utf-8") if path.exists() else ""\n        parts: List[str] = []\n        parts.extend(rule.get("required_headings", []))\n        parts.extend(rule.get("required_text", []))\n        parts.extend("[fixture]({})".format(target) for target in rule.get("required_links", []))\n        addition = "\\n\\n".join(parts) + "\\n"\n        write_text(path, existing + addition)\n'''
    new_materialize = '''    for rule in rules.get("critical_files", []):\n        path = root / rule["path"]\n        required_json = rule.get("required_json", [])\n        if required_json:\n            document: object = {}\n            if path.exists():\n                try:\n                    document = json.loads(path.read_text(encoding="utf-8"))\n                except json.JSONDecodeError:\n                    document = {}\n            for check in required_json:\n                document = set_json_pointer(document, str(check["pointer"]), check.get("equals"))\n            write_text(path, json.dumps(document, indent=2) + "\\n")\n        existing = path.read_text(encoding="utf-8") if path.exists() else ""\n        parts: List[str] = []\n        parts.extend(rule.get("required_headings", []))\n        parts.extend(rule.get("required_text", []))\n        parts.extend("[fixture]({})".format(target) for target in rule.get("required_links", []))\n        if parts:\n            write_text(path, existing + "\\n\\n".join(parts) + "\\n")\n'''
    text = replace_once(text, old_materialize, new_materialize, "materialization")
    old_tail = '''    if mutation_type == "add_file":\n        write_text(path)\n        return\n    raise ValueError("Unsupported fixture mutation: {}".format(mutation_type))\n'''
    new_tail = '''    if mutation_type == "add_file":\n        write_text(path)\n        return\n    if mutation_type == "format_json_compact":\n        document = json.loads(path.read_text(encoding="utf-8"))\n        path.write_text(json.dumps(document, separators=(",", ":")) + "\\n", encoding="utf-8")\n        return\n    if mutation_type == "delete_json_pointer":\n        document = json.loads(path.read_text(encoding="utf-8"))\n        document = delete_json_pointer(document, mutation["pointer"])\n        path.write_text(json.dumps(document, indent=2) + "\\n", encoding="utf-8")\n        return\n    if mutation_type == "move_json_pointer":\n        document = json.loads(path.read_text(encoding="utf-8"))\n        value = get_json_pointer(document, mutation["pointer"])\n        document = delete_json_pointer(document, mutation["pointer"])\n        document = set_json_pointer(document, mutation["destination"], value)\n        path.write_text(json.dumps(document, indent=2) + "\\n", encoding="utf-8")\n        return\n    raise ValueError("Unsupported fixture mutation: {}".format(mutation_type))\n'''
    text = replace_once(text, old_tail, new_tail, "test mutations")
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    update_validator()
    update_contract()
    update_cases()
    update_contract_tests()
    shutil.rmtree(ROOT / "content/research/notes/thinking-systems-platform-assets", ignore_errors=True)
