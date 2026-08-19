#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path.cwd()
helper = ROOT / ".github/scripts/reconstruct_pr79_final_clean_v2.py"


def run(*args: str) -> None:
    subprocess.run(list(args), cwd=ROOT, check=True)


if helper.exists():
    text = helper.read_text(encoding="utf-8")
    text = text.replace(
        "Publication source is not available at declared source commit",
        "Publication source is not present at declared source commit",
    )
    start = text.find('print("Installing locked dependencies and running deterministic validation...")')
    end = text.find('# Final clean commit based directly on current main.', start)
    if start < 0 or end < 0:
        raise RuntimeError("Unable to locate reconstruction validation block")
    text = text[:start] + 'print("Deferring dependency-heavy validation to exact-head PR CI.")\n\n' + text[end:]
    temp = Path("/tmp/reconstruct_pr79_recovery.py")
    temp.write_text(text, encoding="utf-8")
    run("python3", str(temp))
else:
    # Reconstruction already landed. Apply the compatibility wording patch,
    # remove this temporary runner/workflow, validate, and resquash.
    provenance = ROOT / "quartz/scripts/publication-provenance.mjs"
    if not provenance.exists():
        raise RuntimeError("Neither reconstruction helper nor reconstructed publication files are present")
    text = provenance.read_text(encoding="utf-8").replace(
        "Publication source is not available at declared source commit",
        "Publication source is not present at declared source commit",
    )
    provenance.write_text(text, encoding="utf-8")
    for path in [
        ROOT / ".github/scripts/pr79_recovery_runner.py",
        ROOT / ".github/workflows/pr79-recovery-runner.yml",
    ]:
        path.unlink(missing_ok=True)
    run("npm", "ci", "--ignore-scripts")
    run("node", "--test", "quartz/scripts/export-pdf.test.mjs", "quartz/scripts/publication-rendition.test.mjs", "quartz/scripts/publication-safety.test.mjs")
    run("npm", "run", "build")
    run("git", "fetch", "origin", "main")
    run("git", "reset", "--soft", "origin/main")
    run("git", "add", "-A")
    run("git", "config", "user.name", "github-actions[bot]")
    run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
    run("git", "commit", "-m", "Add universal Quartz publication export infrastructure")
    run("git", "push", "--force-with-lease", "origin", "HEAD:feat/quartz-pdf-export")
