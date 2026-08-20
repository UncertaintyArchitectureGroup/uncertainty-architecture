import test from "node:test"
import assert from "node:assert/strict"
import { readFile } from "node:fs/promises"
import path from "node:path"
import { fileURLToPath } from "node:url"
import {
  buildHeroSvg,
  classifyFigureWidth,
  extractMermaidFigures,
} from "./render-publication-assets.mjs"

test("standalone publication exposes all eight canonical Mermaid figures", async () => {
  const repoRoot = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))
  const markdown = await readFile(
    path.join(repoRoot, "content/research/notes/thinking-systems-publication-draft.md"),
    "utf8",
  )
  const figures = extractMermaidFigures(markdown)
  assert.equal(figures.length, 8)
  assert.deepEqual(figures.map((figure) => figure.number), [1, 2, 3, 4, 5, 6, 7, 8])
  assert.equal(figures[7].title, "Two orthogonal models")
})

test("figure sizing keeps ordinary figures at 1600px and dense figures at 2400–3200px", () => {
  const simple = "flowchart LR\nA[Start] --> B[End]"
  const dense = `flowchart LR\n${Array.from(
    { length: 22 },
    (_, index) => `N${index}[Node ${index}] --> N${index + 1}[Node ${index + 1}]`,
  ).join("\n")}`
  assert.equal(classifyFigureWidth(simple), 1600)
  assert.ok([2400, 3200].includes(classifyFigureWidth(dense)))
})

test("hero renderer emits exact platform dimensions and publication identity", () => {
  const svg = buildHeroSvg(
    { key: "social_preview", filename: "social-preview.png", width: 1200, height: 627 },
    {
      title: "Uncertainty Architecture: Thinking Systems — When the Controlled Object Changes",
      author: "Vitalii Oborskyi",
      date: "2026-08-20",
      license: "CC BY 4.0",
    },
  )
  assert.match(svg, /viewBox="0 0 1200 627"/)
  assert.match(svg, /Vitalii Oborskyi/)
  assert.match(svg, /When the Controlled Object Changes/)
})
