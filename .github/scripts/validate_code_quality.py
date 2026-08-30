#!/usr/bin/env python3
"""Validate changed repository-owned code without normalizing the legacy tree.

The repository contains a maintained Quartz fork and preserved documents whose
full-tree formatting baseline is intentionally not rewritten in one mechanical
change. This validator applies the current code-format contract incrementally to
the PR-owned diff and validates Python syntax without adding a runtime dependency.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Callable, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parents[2]
PRETTIER_SUFFIXES = {
    ".cjs",
    ".css",
    ".js",
    ".json",
    ".jsx",
    ".mjs",
    ".scss",
    ".ts",
    ".tsx",
    ".yaml",
    ".yml",
}
ROOT_CODE_FILES = {
    "package.json",
    "quartz.config.ts",
    "quartz.layout.ts",
    "tsconfig.json",
    "vercel.json",
}
PRETTIER_PREFIXES = (".github/", "quartz/")
PYTHON_PREFIXES = (".github/scripts/", ".github/tests/")
# These files are generated or tool-owned; reformatting them would create noisy,
# non-semantic diffs instead of improving maintained source.
EXCLUDED_PATHS = {"package-lock.json", "quartz/util/emojimap.json"}

Runner = Callable[..., subprocess.CompletedProcess]


def git_output_bytes(root: Path, arguments: Sequence[str]) -> bytes:
    """Run one read-only git query without lossy path decoding or line splitting."""
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


def git_output(root: Path, arguments: Sequence[str]) -> str:
    """Run one read-only git query whose output is not a collection of paths."""
    return os.fsdecode(git_output_bytes(root, arguments))


def changed_paths(root: Path, base: str, head: str) -> List[str]:
    """Return added, copied, modified, or renamed paths owned by base..head."""
    merge_base = git_output(root, ["merge-base", base, head]).strip()
    if not merge_base:
        raise ValueError("git merge-base returned no commit")
    output = git_output_bytes(
        root,
        [
            "diff",
            "--name-only",
            "-z",
            "--diff-filter=ACMR",
            "--find-renames",
            merge_base,
            head,
        ],
    )
    return sorted({os.fsdecode(raw_path) for raw_path in output.split(b"\0") if raw_path})


def is_prettier_candidate(relative: str) -> bool:
    """Select maintained web/config source that uses the repository Prettier baseline."""
    if relative in EXCLUDED_PATHS:
        return False
    path = Path(relative)
    if path.suffix.lower() not in PRETTIER_SUFFIXES:
        return False
    return relative in ROOT_CODE_FILES or relative.startswith(PRETTIER_PREFIXES)


def is_python_candidate(relative: str) -> bool:
    """Select repository-policy Python source rather than arbitrary preserved files."""
    return relative.endswith(".py") and relative.startswith(PYTHON_PREFIXES)


def existing_paths(root: Path, paths: Iterable[str]) -> List[str]:
    """Drop deleted or non-file paths after resolving them inside the repository."""
    selected: List[str] = []
    resolved_root = root.resolve()
    for relative in paths:
        candidate = (resolved_root / relative).resolve()
        try:
            candidate.relative_to(resolved_root)
        except ValueError:
            raise ValueError("Changed path escapes repository: {}".format(relative))
        if candidate.is_file():
            selected.append(relative)
    return selected


def validate_python_syntax(root: Path, paths: Iterable[str]) -> List[str]:
    """Compile changed Python source in memory and report every syntax failure."""
    errors: List[str] = []
    for relative in paths:
        path = root / relative
        try:
            source = path.read_text(encoding="utf-8")
            compile(source, relative, "exec")
        except (OSError, UnicodeError, SyntaxError) as exc:
            errors.append("{}: {}".format(relative, exc))
    return errors


def run_prettier(
    root: Path,
    paths: Sequence[str],
    runner: Runner = subprocess.run,
    write: bool = False,
) -> int:
    """Run the locked local Prettier binary for the selected changed files."""
    if not paths:
        return 0
    executable = root / "node_modules/.bin/prettier"
    if not executable.is_file():
        print(
            "Local Prettier is unavailable; run npm ci --ignore-scripts first.",
            file=sys.stderr,
        )
        return 2
    mode = "--write" if write else "--check"
    completed = runner(
        [str(executable), mode, "--ignore-unknown", *paths],
        cwd=str(root),
        check=False,
    )
    return int(completed.returncode)


def validate(root: Path, base: str, head: str, write: bool = False) -> int:
    """Validate the incremental code-quality contract for one git diff."""
    try:
        paths = existing_paths(root, changed_paths(root, base, head))
    except ValueError as exc:
        print("Code-quality validation failed: {}".format(exc), file=sys.stderr)
        return 2

    prettier_paths = [path for path in paths if is_prettier_candidate(path)]
    python_paths = [path for path in paths if is_python_candidate(path)]

    python_errors = validate_python_syntax(root, python_paths)
    for error in python_errors:
        print("Python syntax error: {}".format(error), file=sys.stderr)

    prettier_status = run_prettier(root, prettier_paths, write=write)
    if python_errors or prettier_status:
        return 1

    print(
        "Changed-code {} passed "
        "({} formatted files, {} Python files).".format(
            "formatting" if write else "quality validation",
            len(prettier_paths), len(python_paths)
        )
    )
    return 0


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="Current target tip or other base ref")
    parser.add_argument("--head", required=True, help="Candidate head ref")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Format selected changed files instead of checking them",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="Repository root (defaults to the script's repository)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] = sys.argv[1:]) -> int:
    args = parse_args(argv)
    return validate(args.root.resolve(), args.base, args.head, write=args.write)


if __name__ == "__main__":
    raise SystemExit(main())
