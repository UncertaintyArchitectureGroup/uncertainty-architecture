#!/usr/bin/env python3
"""Regression tests for incremental repository code-quality validation."""

import importlib.util
import os
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
        ["git", *arguments], cwd=str(root), check=True,
        stdout=subprocess.PIPE, text=True,
    )
    return completed.stdout.strip()


def materialize_prettier_fixture(root: Path) -> Path:
    executable = root / "node_modules/.bin/prettier"
    executable.parent.mkdir(parents=True)
    executable.write_text("fixture\n", encoding="utf-8")
    config = root / ".github/config/prettier.json"
    ignore = root / ".github/config/prettierignore"
    config.parent.mkdir(parents=True)
    config.write_text("{}\n", encoding="utf-8")
    ignore.write_text("node_modules\n", encoding="utf-8")
    return executable


class CodeQualityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()

    def test_scope_selects_repository_code_without_preserved_or_prose_files(self) -> None:
        self.assertTrue(self.validator.is_prettier_candidate("quartz/scripts/export.mjs"))
        self.assertTrue(self.validator.is_prettier_candidate(".github/workflows/build-integrity.yml"))
        self.assertTrue(self.validator.is_prettier_candidate(".github/config/prettier.json"))
        self.assertTrue(self.validator.is_prettier_candidate("package.json"))
        self.assertFalse(self.validator.is_prettier_candidate("package-lock.json"))
        self.assertFalse(self.validator.is_prettier_candidate("content/research/note.md"))
        self.assertTrue(self.validator.is_python_candidate(".github/scripts/validate_example.py"))
        self.assertFalse(self.validator.is_python_candidate("content/raw/example.py"))
        self.assertEqual(
            self.validator.selected_code_paths(
                ["content/research/note.md", "quartz/scripts/export.mjs", ".github/tests/test.py"]
            ),
            [".github/tests/test.py", "quartz/scripts/export.mjs"],
        )

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
                root, [".github/scripts/valid.py", ".github/tests/invalid.py"]
            )
            self.assertEqual(len(errors), 1)
            self.assertIn(".github/tests/invalid.py", errors[0])

    def test_prettier_failure_is_blocking_and_write_mode_is_forwarded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            materialize_prettier_fixture(root)
            calls = []

            def runner(arguments, **options):
                calls.append((arguments, options))
                return subprocess.CompletedProcess(arguments, 1)

            status = self.validator.run_prettier(root, ["package.json"], runner=runner, write=True)
            self.assertEqual(status, 1)
            self.assertEqual(calls[0][0][1], "--write")
            self.assertIn("--config", calls[0][0])
            self.assertIn("--ignore-path", calls[0][0])

    def test_missing_or_aliased_prettier_configuration_is_configuration_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            executable = root / "node_modules/.bin/prettier"
            executable.parent.mkdir(parents=True)
            executable.write_text("fixture\n", encoding="utf-8")
            self.assertEqual(self.validator.run_prettier(root, ["package.json"]), 2)
            config = root / ".github/config/prettier.json"
            ignore = root / ".github/config/prettierignore"
            config.parent.mkdir(parents=True)
            target = root / "config-target.json"
            target.write_text("{}\n", encoding="utf-8")
            config.symlink_to(target)
            ignore.write_text("node_modules\n", encoding="utf-8")
            self.assertEqual(self.validator.run_prettier(root, ["package.json"]), 2)

    def test_existing_paths_reject_symbolic_hard_and_parent_aliases(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "quartz/source.ts"
            source.parent.mkdir(parents=True)
            source.write_text("export const value = 1\n", encoding="utf-8")
            symbolic_alias = root / "quartz/symbolic.ts"
            symbolic_alias.symlink_to(source.name)
            with self.assertRaisesRegex(ValueError, "symbolic-link alias"):
                self.validator.existing_paths(root, ["quartz/symbolic.ts"])
            hard_alias = root / "quartz/hard.ts"
            os.link(source, hard_alias)
            with self.assertRaisesRegex(ValueError, "hard-link alias"):
                self.validator.existing_paths(root, ["quartz/hard.ts"])
            parent_target = root / "real"
            parent_target.mkdir()
            parent_alias = root / "alias"
            parent_alias.symlink_to(parent_target, target_is_directory=True)
            (parent_target / "nested.ts").write_text("export {}\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "symbolic-link alias"):
                self.validator.existing_paths(root, ["alias/nested.ts"])

    def test_unrelated_prose_symlink_is_outside_code_quality_scope(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")
            target = root / "note-target.md"
            target.write_text("base\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            prose = root / "content/research/note.md"
            prose.parent.mkdir(parents=True)
            prose.symlink_to(Path("../../note-target.md"))
            git(root, "add", "-A")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")
            self.assertEqual(self.validator.validate(root, base, head), 0)

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
            git(root, "add", "-A")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")
            paths = self.validator.changed_paths(root, base, head)
            self.assertEqual(paths, [".github/tests/example.py", "quartz/scripts/example.mjs"])

    def test_changed_paths_are_nul_safe_for_unicode_newline_and_rename(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")
            original = root / "quartz/original.ts"
            original.parent.mkdir(parents=True)
            original.write_text("export const value = 1\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            renamed = root / "quartz/renamed\nтест.ts"
            original.rename(renamed)
            spaced = root / "quartz/space name.ts"
            spaced.write_text("export const value = 2\n", encoding="utf-8")
            git(root, "add", "-A")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")
            self.assertEqual(
                self.validator.changed_paths(root, base, head),
                ["quartz/renamed\nтест.ts", "quartz/space name.ts"],
            )


if __name__ == "__main__":
    unittest.main()
