#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[2]
source_path = root / ".github/scripts/apply_pr99_semantic_fixes.py"
source = source_path.read_text(encoding="utf-8")
marker = "# Restore Metadata integrity workflow to normal read-only operation and"
if marker not in source:
    raise SystemExit("semantic patch cleanup marker missing")
prefix = source.split(marker, 1)[0]
exec(compile(prefix, str(source_path), "exec"), {"__name__": "__main__", "__file__": str(source_path)})

# Script files are safe to remove in the pushed commit; workflow files are
# restored separately through the repository connector after semantic changes land.
source_path.unlink()
Path(__file__).unlink()
