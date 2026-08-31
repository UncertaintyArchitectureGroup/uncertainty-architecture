#!/usr/bin/env python3
"""Mutation checks for the code-quality repository-contract extension."""

import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPOSITORY_ROOT / ".github/scripts/validate_repository_contract.py"
EXTENSION_PATH = REPOSITORY_ROOT / ".github/policy/repository-contract-code-quality.json"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_repository_contract", VALIDATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load repository-contract validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CodeQualityRepositoryContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = load_validator()
        cls.extension = json.loads(EXTENSION_PATH.read_text(encoding="utf-8"))

    def validate_extension(self, root: Path):
        errors = []
        self.validator.validate_required_paths(root, self.extension, errors)
        self.validator.validate_critical_files(root, self.extension, errors)
        return errors

    def materialize(self, root: Path) -> None:
        for item in self.extension["required_paths"]:
            relative = item["path"]
            source = REPOSITORY_ROOT / relative
            target = root / relative
            if item["type"] == "directory":
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)

    def test_live_surface_satisfies_extension(self) -> None:
        self.assertEqual(self.validate_extension(REPOSITORY_ROOT), [])

    def test_contributor_contract_mutation_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.materialize(root)
            path = root / "CONTRIBUTING.md"
            path.write_text(path.read_text(encoding="utf-8").replace("Every defect fix requires a regression test that would fail without the fix.", ""), encoding="utf-8")
            self.assertTrue(any("CONTRIBUTING.md: missing protected text" in error for error in self.validate_extension(root)))

    def test_quartz_upstream_baseline_mutation_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.materialize(root)
            path = root / "quartz/README.md"
            path.write_text(path.read_text(encoding="utf-8").replace("4923affa7722dfc751f1074348e6dad214fe0c08", "changed"), encoding="utf-8")
            self.assertTrue(any("quartz/README.md: missing protected text" in error for error in self.validate_extension(root)))

    def test_package_script_mutation_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.materialize(root)
            path = root / "package.json"
            package = json.loads(path.read_text(encoding="utf-8"))
            del package["scripts"]["format:check"]
            path.write_text(json.dumps(package), encoding="utf-8")
            self.assertTrue(any("package.json: JSON pointer '/scripts/format:check'" in error for error in self.validate_extension(root)))

    def test_required_type_declaration_deletion_is_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.materialize(root)
            (root / "quartz/types/events.d.ts").unlink()
            self.assertTrue(any("Missing required file: quartz/types/events.d.ts" in error for error in self.validate_extension(root)))


if __name__ == "__main__":
    unittest.main()
