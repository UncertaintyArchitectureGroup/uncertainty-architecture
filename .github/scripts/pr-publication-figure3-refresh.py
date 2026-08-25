from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_once(rel, old, new):
    path = ROOT / rel
    text = path.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{rel}: expected exactly one match, got {count}: {old!r}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")

# Recognize the post-review canonical Figure 3 source.
replace_once(
    "quartz/scripts/publication-rendition.mjs",
    '!mermaid.includes("Thinking System — changed responsibility structure")',
    '!mermaid.includes("Motivating class — changed responsibility structure")',
)

# Update semantic guard and static reviewed SVG to the narrowed Figure 3 meaning.
fig = "quartz/scripts/publication-figure3.mjs"
replace_once(fig, '"Thinking System — changed responsibility structure",', '"Motivating class — changed responsibility structure",')
replace_once(fig, 'aria-label="Side-by-side top-down comparison of Linear Software and a Thinking System"', 'aria-label="Side-by-side top-down comparison of Explicitly Authored Software and the motivating runtime-judgment class"')
replace_once(fig, '["Linear Software"]', '["Explicitly Authored Software"]')
replace_once(fig, '["Thinking System"]', '["Motivating runtime-judgment class"]')
replace_once(
    fig,
    '["Model Judgment changes the responsibility structure at a bounded node;", "the surrounding system still contains explicitly authored responsibilities."]',
    '["Model Judgment leaves part of a consequential responsibility unresolved until operation;", "the surrounding system still contains explicitly authored responsibilities."]',
)

# Keep regression fixtures coupled to the reviewed semantic source and rendition labels.
test = "quartz/scripts/publication-figure3.test.mjs"
replace_once(test, 'subgraph B["Thinking System — changed responsibility structure"]', 'subgraph B["Motivating class — changed responsibility structure"]')
replace_once(test, '**Figure 3 — The controlled-object shift.** Canonical caption.', '**Figure 3 — The controlled-object shift for the motivating class.** Canonical caption.')
replace_once(test, 'test("Figure 3 publication rendition is a side-by-side Linear Software comparison", () => {', 'test("Figure 3 publication rendition is a side-by-side motivating-class comparison", () => {')
replace_once(test, 'assert.match(result.content, /Linear Software/);', 'assert.match(result.content, /Explicitly Authored Software/);')
replace_once(test, 'assert.match(result.content, /Thinking System/);', 'assert.match(result.content, /Motivating runtime-judgment class/);')
replace_once(test, 'assert.match(svg, /Linear Software/);', 'assert.match(svg, /Explicitly Authored Software/);')
replace_once(test, 'assert.match(svg, /Thinking System/);', 'assert.match(svg, /Motivating runtime-judgment class/);')
replace_once(
    test,
    '/<strong>Figure 3 — The controlled-object shift\\.<\\/strong>/',
    '/<strong>Figure 3 — The controlled-object shift for the motivating class\\.<\\/strong>/',
)

print("Figure 3 publication renderer, locator, and tests refreshed")
