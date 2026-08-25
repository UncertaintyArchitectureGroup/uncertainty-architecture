#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

replacements = {
    "quartz/scripts/publication-rendition.mjs": [
        (
            '"Primarily explicitly authored consequential behavior",',
            '"Explicitly Authored Software — consequential mapping authored before release",',
        ),
        (
            '!mermaid.includes("Motivating class — changed responsibility structure")',
            '!mermaid.includes("Motivating runtime-judgment class — part of mapping completed at runtime")',
        ),
    ],
    "quartz/scripts/publication-figure3.test.mjs": [
        (
            'subgraph A["Primarily explicitly authored consequential behavior"]',
            'subgraph A["Explicitly Authored Software — consequential mapping authored before release"]',
        ),
        (
            'subgraph B["Motivating class — changed responsibility structure"]',
            'subgraph B["Motivating runtime-judgment class — part of mapping completed at runtime"]',
        ),
    ],
    "quartz/scripts/publication-rendition.test.mjs": [
        (
            '0d97647ea773cb2e48c5c4394a634e21dab267abad475905347a9d00bda18047',
            '9564729a771d2b0e56ce6600420709efefa032d8b2494159fd05aac6fb19e9a6',
        ),
    ],
}

for rel, pairs in replacements.items():
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    for old, new in pairs:
        count = text.count(old)
        if count != 1:
            raise SystemExit(f"{rel}: expected exactly one {old!r}, got {count}")
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")

print("diagram guards coupled to repaired canonical source")
