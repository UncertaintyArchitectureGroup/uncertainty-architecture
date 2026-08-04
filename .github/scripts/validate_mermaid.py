#!/usr/bin/env python3
"""Extract every maintained Mermaid block and render it with pinned mermaid-cli."""

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONTRACT = ROOT / ".github/policy/supply-chain-contract.json"
BLOCK_RE = re.compile(r"```mermaid\s*\n(.*?)\n```", re.DOTALL)
EXCLUDED_PREFIXES = ("content/raw/", "node_modules/", "public/")


def load_version(path: Path) -> str:
    data: Dict[str, object] = json.loads(path.read_text(encoding="utf-8"))
    if data.get("contract_version") != 1:
        raise ValueError("unsupported contract_version")
    return str(data["tool_versions"]["mermaid_cli"])


def maintained_markdown(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        relative = path.relative_to(root).as_posix()
        if not relative.startswith(EXCLUDED_PREFIXES) and "/node_modules/" not in f"/{relative}":
            yield path


def collect_blocks(root: Path) -> List[Tuple[str, int, str]]:
    blocks: List[Tuple[str, int, str]] = []
    for path in maintained_markdown(root):
        text = path.read_text(encoding="utf-8")
        for index, match in enumerate(BLOCK_RE.finditer(text), start=1):
            blocks.append((path.relative_to(root).as_posix(), index, match.group(1).strip() + "\n"))
    return blocks


def render_blocks(root: Path, version: str, blocks: List[Tuple[str, int, str]]) -> List[str]:
    errors: List[str] = []
    if not blocks:
        return ["no maintained Mermaid blocks were found"]

    with tempfile.TemporaryDirectory(prefix="ua-mermaid-") as temporary:
        temp = Path(temporary)
        puppeteer_config = temp / "puppeteer-config.json"
        puppeteer_config.write_text(
            json.dumps({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}),
            encoding="utf-8",
        )

        for sequence, (relative, block_index, source) in enumerate(blocks, start=1):
            input_path = temp / f"diagram-{sequence}.mmd"
            output_path = temp / f"diagram-{sequence}.svg"
            input_path.write_text(source, encoding="utf-8")
            result = subprocess.run(
                [
                    "npx",
                    "--yes",
                    f"@mermaid-js/mermaid-cli@{version}",
                    "-p",
                    str(puppeteer_config),
                    "-i",
                    str(input_path),
                    "-o",
                    str(output_path),
                    "--quiet",
                ],
                cwd=str(root),
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
            if result.returncode != 0 or not output_path.is_file():
                detail = (result.stderr or result.stdout).strip().replace("\n", " ")
                errors.append(f"{relative}: Mermaid block {block_index} failed to render: {detail}")
    return errors


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--list-only", action="store_true")
    return parser.parse_args(argv)


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    try:
        version = load_version(args.contract.resolve())
        blocks = collect_blocks(root)
        if args.list_only:
            for relative, index, _ in blocks:
                print(f"{relative}#{index}")
            print(f"Found {len(blocks)} maintained Mermaid block(s).")
            return 0 if blocks else 1
        if shutil.which("npx") is None:
            raise ValueError("npx is unavailable")
        errors = render_blocks(root, version, blocks)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Mermaid validation configuration error: {exc}")
        return 2
    if errors:
        print("Mermaid rendering failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Mermaid rendering passed: {len(blocks)} maintained block(s) rendered with mermaid-cli {version}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
