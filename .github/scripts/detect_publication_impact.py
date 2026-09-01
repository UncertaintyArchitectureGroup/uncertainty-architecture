#!/usr/bin/env python3
"""Detect whether a PR-owned diff requires publication integration rendering."""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Sequence

ROOT = Path(__file__).resolve().parents[2]
PUBLICATION_EXACT_PATHS = {
    ".github/policy/repository-contract-code-quality.json",
    ".github/scripts/detect_publication_impact.py",
    ".github/workflows/build-integrity.yml",
    ".github/workflows/export-research-pdf.yml",
    "package-lock.json",
    "package.json",
    "quartz.config.ts",
    "quartz.layout.ts",
    "tsconfig.json",
    "content/research/notes/open-engineering-specification-article-draft.md",
    "content/research/notes/thinking-systems-publication-draft.md",
}
PUBLICATION_PREFIXES = (
    "assets/",
    "content/research/publications/",
    "quartz/",
)
PUBLICATION_NON_EXECUTABLE_PATHS = {
    "quartz/AGENTS.md",
    "quartz/README.md",
    "quartz/PDF-EXPORT.md",
    "quartz/PLATFORM-RENDITIONS.md",
}


def git_output_bytes(root: Path, arguments: Sequence[str]) -> bytes:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=str(root),
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise ValueError(
            "git {} failed: {}".format(
                " ".join(arguments),
                os.fsdecode(completed.stderr).strip() or "unknown error",
            )
        )
    return completed.stdout


def changed_paths(root: Path, base: str, head: str) -> List[str]:
    """Return both sides of PR-owned renames using a NUL-delimited diff."""
    merge_base = os.fsdecode(git_output_bytes(root, ["merge-base", base, head])).strip()
    if not merge_base:
        raise ValueError("git merge-base returned no commit")
    output = git_output_bytes(
        root,
        ["diff", "--name-only", "-z", "--no-renames", merge_base, head],
    )
    return sorted({os.fsdecode(path) for path in output.split(b"\0") if path})


def is_publication_impact_path(relative: str) -> bool:
    """Classify sources whose changes can alter publication render or verification."""
    if relative in PUBLICATION_NON_EXECUTABLE_PATHS:
        return False
    return relative in PUBLICATION_EXACT_PATHS or relative.startswith(PUBLICATION_PREFIXES)


def publication_render_required(root: Path, base: str, head: str) -> bool:
    return any(is_publication_impact_path(path) for path in changed_paths(root, base, head))


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Current target tip or other base ref")
    parser.add_argument("--head", required=True, help="Candidate head ref")
    parser.add_argument("--root", type=Path, default=ROOT)
    return parser.parse_args(argv)


def main(argv: Sequence[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    try:
        required = publication_render_required(args.root.resolve(), args.base, args.head)
    except ValueError as exc:
        print("Publication-impact detection failed: {}".format(exc), file=sys.stderr)
        return 2
    print("true" if required else "false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
