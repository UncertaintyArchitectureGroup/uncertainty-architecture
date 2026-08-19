#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path.cwd()
BRANCH = "feat/quartz-pdf-export"


def run(*args: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )

required = [
    "quartz/scripts/publication-path-safety.mjs",
    "quartz/scripts/publication-provenance.mjs",
    "quartz/scripts/publication-cover.mjs",
    "quartz/scripts/publication-figure8-fingerprint.mjs",
    "quartz/scripts/publication-safety.test.mjs",
    "quartz/scripts/render-publication-pdf.mjs",
    "quartz/scripts/render-publication-assets.mjs",
]
missing = [path for path in required if not (ROOT / path).is_file()]
if missing:
    raise RuntimeError(
        "Clean reconstruction did not complete; missing final files: " + ", ".join(missing)
    )

# Defensive repair for temporary-root unit tests while retaining repoRoot as the
# production default. Tests should already pass an explicit trustedRoot; this
# additionally gives custom output roots a safe nearest trusted anchor.
exporter_path = ROOT / "quartz/scripts/export-pdf.mjs"
exporter = exporter_path.read_text(encoding="utf-8")
needle = "  await assertSafeOutputPath(options.trustedRoot ?? repoRoot, allowedOutputRoot, resolvedOutput);"
if needle in exporter:
    exporter = exporter.replace(
        needle,
        "  const trustedOutputRoot = options.trustedRoot ?? (allowedOutputRoot === pdfOutputRoot ? repoRoot : path.dirname(allowedOutputRoot));\n  await assertSafeOutputPath(trustedOutputRoot, allowedOutputRoot, resolvedOutput);",
        1,
    )
exporter_path.write_text(exporter, encoding="utf-8")

# Remove every reconstruction/diagnostic artifact. Only the maintained
# publication workflow remains under .github/workflows/.
patterns = [
    ".github/workflows/*pr79*",
    ".github/workflows/*reconstruct*",
    ".github/workflows/*finalize*",
    ".github/workflows/*hardening*",
    ".github/scripts/*pr79*",
    ".github/scripts/*reconstruct*",
    ".github/scripts/*finalize*",
    ".github/scripts/*hardening*",
    ".github/pr79*",
]
for pattern in patterns:
    for path in ROOT.glob(pattern):
        if path.is_file() or path.is_symlink():
            path.unlink()

# No publication infrastructure change may edit the research sources.
run("git", "fetch", "origin", "main")
for source_path in [
    "content/research/notes/thinking-systems-publication-draft.md",
    "content/research/notes/open-engineering-specification-article-draft.md",
]:
    run("git", "diff", "--exit-code", "origin/main", "--", source_path)

# Syntax-check every maintained JS entry/helper before the dependency-heavy run.
for path in sorted((ROOT / "quartz/scripts").glob("*.mjs")):
    if any(token in path.name for token in ["publication", "export-pdf", "run-pdf"]):
        run("node", "--check", str(path.relative_to(ROOT)))

run("npm", "ci", "--ignore-scripts")
run(
    "node",
    "--test",
    "quartz/scripts/export-pdf.test.mjs",
    "quartz/scripts/publication-rendition.test.mjs",
    "quartz/scripts/publication-safety.test.mjs",
)
run("npm", "run", "build")
run("python3", ".github/tests/repository_contract/test_repository_contract.py")
run("python3", ".github/scripts/validate_workflow_supply_chain.py")

# Verify the final diff has only intended infrastructure/documentation paths.
status = run("git", "status", "--short", capture=True).stdout
print(status)
for line in status.splitlines():
    path = line[3:].strip()
    if path.startswith("content/research/notes/"):
        raise RuntimeError(f"Publishing PR unexpectedly changes research source: {path}")
    if "reconstruct" in path or "finalize-pr79" in path or "pr79-" in path:
        raise RuntimeError(f"Temporary repair artifact remains in final diff: {path}")

# One clean commit directly on current main.
run("git", "reset", "--soft", "origin/main")
run("git", "add", "-A")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "commit", "-m", "Add universal Quartz publication export infrastructure")
run("git", "push", "--force-with-lease", "origin", f"HEAD:{BRANCH}")
print("PR #79 finalized and squashed.")
