#!/usr/bin/env python3
"""Regression tests for publication-impact detection."""

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/detect_publication_impact.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("detect_publication_impact", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load publication-impact detector")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(root: Path, *arguments: str) -> str:
    completed = subprocess.run(
        ["git", *arguments], cwd=str(root), check=True,
        stdout=subprocess.PIPE, text=True,
    )
    return completed.stdout.strip()


class PublicationImpactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()

    def test_renderer_configuration_types_and_publication_sources_are_impacting(self) -> None:
        impacting = [
            "quartz/plugins/transformers/ofm.ts",
            "quartz/components/renderPage.tsx",
            "quartz/processors/parse.ts",
            "quartz/styles/base.scss",
            "quartz/build.ts",
            "quartz.config.ts",
            "quartz.layout.ts",
            "quartz/types/global.d.ts",
            "quartz/types/events.d.ts",
            "assets/publication/figure.svg",
            "content/research/publications/article.md",
        ]
        for path in impacting:
            with self.subTest(path=path):
                self.assertTrue(self.validator.is_publication_impact_path(path))

    def test_scoped_guidance_and_unrelated_repository_docs_are_not_impacting(self) -> None:
        for path in [
            "quartz/AGENTS.md",
            "quartz/README.md",
            "quartz/PDF-EXPORT.md",
            "quartz/PLATFORM-RENDITIONS.md",
            "CONTRIBUTING.md",
        ]:
            with self.subTest(path=path):
                self.assertFalse(self.validator.is_publication_impact_path(path))

    def test_invalid_revision_fails_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")
            (root / "README.md").write_text("base\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            with self.assertRaisesRegex(ValueError, "git merge-base"):
                self.validator.publication_render_required(root, "missing-revision", "HEAD")

    def test_changed_paths_preserve_unicode_newlines_and_both_rename_sides(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")
            original = root / "quartz/plugins/original.ts"
            original.parent.mkdir(parents=True)
            original.write_text("export const value = 1\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            renamed = root / "notes/renamed\nтест.txt"
            renamed.parent.mkdir(parents=True)
            original.rename(renamed)
            git(root, "add", "-A")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")
            paths = self.validator.changed_paths(root, base, head)
            self.assertEqual(paths, ["notes/renamed\nтест.txt", "quartz/plugins/original.ts"])
            self.assertTrue(self.validator.publication_render_required(root, base, head))

    def test_unrelated_diff_does_not_require_publication_render(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            git(root, "init", "--initial-branch=main")
            git(root, "config", "user.email", "fixture@example.invalid")
            git(root, "config", "user.name", "Fixture")
            contributing = root / "CONTRIBUTING.md"
            contributing.write_text("base\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "base")
            base = git(root, "rev-parse", "HEAD")
            contributing.write_text("changed\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "head")
            head = git(root, "rev-parse", "HEAD")
            self.assertFalse(self.validator.publication_render_required(root, base, head))


if __name__ == "__main__":
    unittest.main()
