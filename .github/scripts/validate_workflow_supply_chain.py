#!/usr/bin/env python3
"""Validate immutable GitHub Action and container references in workflow YAML."""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/supply-chain-contract.json"
USES_RE = re.compile(r"^\s*-?\s*uses:\s*([^\s#]+)(?:\s+#\s*(.+))?\s*$")
CONTAINER_RE = re.compile(r"^\s*(?:image|container):\s*([^\s#]+)")
FULL_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
DIGEST_RE = re.compile(r"@sha256:[0-9a-f]{64}$")


def load_contract(path: Path) -> Dict[str, object]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("contract_version") != 1:
        raise ValueError("unsupported contract_version")
    return data


def workflow_files(root: Path) -> Iterable[Path]:
    yield from sorted((root / ".github/workflows").glob("*.y*ml"))


def validate(root: Path, contract_path: Path) -> List[str]:
    contract = load_contract(contract_path)
    action_policy = contract["github_action_reference"]
    container_policy = contract["container_reference"]
    errors: List[str] = []

    for path in workflow_files(root):
        relative = path.relative_to(root).as_posix()
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            use_match = USES_RE.match(line)
            if use_match:
                reference, comment = use_match.groups()
                if reference.startswith("./"):
                    continue
                if "@" not in reference:
                    errors.append(f"{relative}:{line_number}: external action lacks @ reference")
                    continue
                _, ref = reference.rsplit("@", 1)
                if action_policy.get("require_full_commit_sha") and not FULL_SHA_RE.fullmatch(ref):
                    errors.append(f"{relative}:{line_number}: action must be pinned to a full 40-character commit SHA: {reference}")
                if action_policy.get("require_version_comment") and not comment:
                    errors.append(f"{relative}:{line_number}: pinned action requires a human-readable version comment")

            container_match = CONTAINER_RE.match(line)
            if container_match:
                image = container_match.group(1)
                if image.startswith("docker://"):
                    image = image[len("docker://"):]
                if container_policy.get("require_digest") and not DIGEST_RE.search(image):
                    errors.append(f"{relative}:{line_number}: container image must be pinned by sha256 digest: {image}")

    return errors


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    try:
        errors = validate(args.root.resolve(), args.contract.resolve())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Supply-chain configuration error: {exc}")
        return 2
    if errors:
        print("Workflow supply-chain validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("Workflow supply-chain validation passed: actions use immutable SHAs and container references use digests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
