#!/usr/bin/env python3
"""Regression tests for incremental repository code-quality validation."""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_code_quality.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_code_quality", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load code-quality validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", *arguments],
        cwd=str(root),
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return completed.stdout.strip()


class CodeQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()

    def test_scope_selects_repository_code_without_preserved_or_prose_files(self) -> None:
        self.assertTrue(self.validator.is_prettier_candidate("quartz/scripts/export.mjs"))
        self.assertTrue(
            self.validator.is_prettier_candidate(".github/workflows/build-integrity.yml")
        )
        self.assertTrue(self.validator.is_prettier_candidate("package.json"))
        self.assertFalse(self.validator.is_prettier_candidate("package-lock.json"))
        self.assertFalse(self.validator.is_prettier_candidate("quartz/util/emojimap.json"))
        self.assertFalse(self.validator.is_prettier_candidate("content/research/note.md"))
        self.assertTrue(
            self.validator.is_python_candidate(".github/scripts/validate_example.py")
        )
        self.assertFalse(self.validator.is_python_candidate("content/raw/example.py"))

    def test_python_syntax_reports_invalid_changed_source(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / ".github/scripts/valid.py"
            invalid = root / ".github/tests/invalid.py"
            valid.parent.mkdir(parents=True)
            invalid.parent.mkdir(parents=True)
            valid.write_text("value = 1\n", encoding="utf-8")
            invalid.write_text("if True print('broken')\n", encoding="utf-8")

            errors = self.validator.validate_python_syntax(
                root,
                [".github/scripts/valid.py", ".github/tests/invalid.py"],
            )

            self.assertEqual(len(errors), 1)
            self.assertIn(".github/tests/invalid.py", errors[0])

    def test_prettier_uses_locked_binary_and_selected_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "node_modules/.bin/prettier"
            executable.parent.mkdir(parents=True)
            executable.write_text("fixture\n", encoding="utf-8")
            calls = []

            def runner(arguments, **options):
                calls.append((arguments, options))
                return subprocess.CompletedProcess(arguments, 0)

            status = self.validator.run_prettier(
                root,
                ["package.json", "quartz/scripts/example.mjs"],
                runner=runner,
            )

            self.assertEqual(status, 0)
            self.assertEqual(calls[0][0][0], str(executable))
            self.assertEqual(calls[0][0][-2:], ["package.json", "quartz/scripts/example.mjs"])
            self.assertEqual(calls[0][1]["cwd"], str(root))

    def test_changed_paths_use_merge_base_and_ignore_deletions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")

            script = root / "quartz/scripts/example.mjs"
            removed = root / ".github/scripts/removed.py"
            script.parent.mkdir(parents=True)
            removed.parent.mkdir(parents=True)
            script.write_text("export const value = 1\n", encoding="utf-8")
            removed.write_text("value = 1\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            base = git(root, "rev-parse", "HEAD")

            script.write_text("export const value = 2\n", encoding="utf-8")
            removed.unlink()
            added = root / ".github/tests/example.py"
            added.parent.mkdir(parents=True)
            added.write_text("value = 2\n", encoding="utf-8")
            prose = root / "content/note.md"
            prose.parent.mkdir(parents=True)
            prose.write_text("# Note\n", encoding="utf-8")
            git(root, "add", "-A")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")

            paths = self.validator.changed_paths(root, base, head)

            self.assertEqual(
                paths,
                [
                    ".github/tests/example.py",
                    "content/note.md",
                    "quartz/scripts/example.mjs",
                ],
            )


if __name__ == "__main__":
    unittest.main()
