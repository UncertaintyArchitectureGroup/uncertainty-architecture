import assert from "node:assert/strict"
import { mkdtemp, readFile, rename, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"

import { buildToc, extractFigureList, normalizeDate, splitFigure8 } from "./publication-rendition.mjs"
import {
  countPdfPages,
  determineSourceProvenance,
  finalizePublicationBundle,
} from "./render-publication-pdf.mjs"
import { findContentlessTextPages, verifyPageFurniture } from "./verify-publication-pdf.mjs"
import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs"

test("Figure 8 publication rendition preserves decision and capability semantics", () => {
  const source = `Before\n\n\`\`\`mermaid\nflowchart LR\n    subgraph L["Decision ownership"]\n        O["Organization"] -->|initial admissibility + assessment eligibility| P["Project"]\n        P --> CAT{"Selected technical design still a Thinking System?"}\n        CAT -->|No| EXIT["Exit Thinking-System-specific lifecycle"]\n        P --> RQ["specific Bounded Research Authorization"]\n        P --> VB["viable production basis"]\n        P --> PA["research-only and/or production-capable"]\n        D["Delivery"] --> E["Delivery / Runtime reassessment evidence"]\n        X["Exogenous Organizational change"] --> O\n    end\n    subgraph F["Capability functions"]\n        A["Actuators and corrective action"]\n        K["Constraints and realizations"]\n        S["Sensors and evidence"]\n        C["Controllers / decision functions"]\n    end\n    L -. "all four capability families may appear at every decision horizon" .- F\n\`\`\`\n\n**Figure 8 — Two orthogonal models.** Canonical caption.\n\nAfter`
  const result = splitFigure8(source, { verifyFingerprint: false })
  assert.equal(result.split, true)
  assert.match(result.content, /Figure 8A — Decision-ownership model/)
  assert.match(result.content, /Figure 8B — Capability-family axis/)
  assert.match(result.content, /Together, Figures 8A–8B preserve canonical Figure 8/)
  assert.match(result.content, /initial admissibility \+ assessment eligibility/)
  assert.match(result.content, /specific Bounded Research Authorization/)
  assert.match(result.content, /research-only and\/or production-capable/)
  assert.match(result.content, /Exogenous Organizational change/)
  assert.match(result.content, /All four capability families may appear at every decision horizon/)
  assert.match(result.content, /not an execution pipeline/)
})

test("strict Figure 8 fingerprint rejects topology changes even when semantic marker text remains", () => {
  const mermaid = `flowchart LR\nsubgraph L["Decision ownership"]\nO["initial admissibility + assessment eligibility"] --> P["specific Bounded Research Authorization"]\nP --> X["Selected technical design still a Thinking System?"]\nX --> E["Exit Thinking-System-specific lifecycle"]\nV["viable production basis"]\nA["research-only and/or production-capable"]\nD["Delivery / Runtime reassessment evidence"]\nG["Exogenous Organizational change"]\nend\nsubgraph F["Capability"]\nC["all four capability families may appear at every decision horizon"]\nend`
  assert.throws(
    () => assertCanonicalFigure8Fingerprint(mermaid, "**Figure 8 — Two orthogonal models.** changed"),
    /requires substantive review/,
  )
})

test("Figure 8 without both orthogonal subgraphs is left unchanged", () => {
  const source = `\`\`\`mermaid\nflowchart TB\n    O["Organization"] --> P["Project"]\n\`\`\`\n\n**Figure 8 — Decision model.** No capability model here.`
  const result = splitFigure8(source)
  assert.equal(result.split, false)
  assert.equal(result.content, source)
})

test("clickable contents renders stable second and third level links", () => {
  const toc = buildToc(`# Title\n\n## First Section\n\n### Detail Here\n\n## First Section`)
  assert.match(toc, /<a href="#first-section">First Section<\/a>/)
  assert.match(toc, /<a href="#detail-here">Detail Here<\/a>/)
  assert.match(toc, /<a href="#first-section-1">First Section<\/a>/)
})

test("publication dates remain stable YYYY-MM-DD values", () => {
  assert.equal(normalizeDate(new Date("2026-08-17T00:00:00.000Z")), "2026-08-17")
  assert.equal(normalizeDate("2026-08-17T18:20:00Z"), "2026-08-17")
  assert.equal(normalizeDate("2026-08-17"), "2026-08-17")
  assert.equal(normalizeDate(null), null)
})

test("PDF page furniture requires running footer and boundary counters", () => {
  assert.equal(verifyPageFurniture("Uncertainty Architecture · Research Publication   Page 1 / 23\n...\nPage 23 / 23", 23).valid, true)
  assert.equal(verifyPageFurniture("Uncertainty Architecture · Research Publication   Page 1 / 23", 23).valid, false)
})

test("PDF verification rejects pages that contain only page furniture", () => {
  const text = ["Article title\nUncertainty Architecture · Research Publication\nPage 1 / 3", "Uncertainty Architecture · Research Publication\nPage 2 / 3", "Closing section\nUncertainty Architecture · Research Publication\nPage 3 / 3"].join("\f")
  assert.deepEqual(findContentlessTextPages(text, 3), [2])
})

test("figure list distinguishes publication 8A and 8B renditions", () => {
  const figures = extractFigureList(`**Figure 7 — Complete bounded control architecture.** Text\n\n**Figure 8A — Decision-ownership model.** Text\n\n**Figure 8B — Capability-family axis.** Text`)
  assert.deepEqual(figures.map(({ number, panel }) => [number, panel]), [[7, null], [8, "A"], [8, "B"]])
})

test("PDF page counting ignores Pages objects", () => {
  assert.equal(countPdfPages(Buffer.from("/Type /Pages /Count 2 /Kids [] /Type /Page /Type /Page", "latin1")), 2)
})

test("publication bundle finalization restores the previous PDF and manifest when manifest installation fails", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-publication-bundle-test-"))
  try {
    const stagedPdf = path.join(directory, "staged.pdf")
    const stagedManifest = path.join(directory, "staged.manifest.json")
    const output = path.join(directory, "publication.pdf")
    const manifest = path.join(directory, "publication.manifest.json")
    await writeFile(stagedPdf, "new publication")
    await writeFile(stagedManifest, "new manifest")
    await writeFile(output, "previous publication")
    await writeFile(manifest, "previous manifest")

    let injected = false
    const renameImpl = async (source, target) => {
      if (!injected && source === stagedManifest && target === manifest) {
        injected = true
        throw new Error("injected bundle finalization failure")
      }
      await rename(source, target)
    }

    await assert.rejects(
      finalizePublicationBundle(
        {
          stagedPdfPath: stagedPdf,
          stagedManifestPath: stagedManifest,
          outputPath: output,
          manifestPath: manifest,
        },
        {
          trustedRoot: directory,
          allowedRoot: directory,
          renameImpl,
        },
      ),
      /injected bundle finalization failure/,
    )
    assert.equal(await readFile(output, "utf8"), "previous publication")
    assert.equal(await readFile(manifest, "utf8"), "previous manifest")
  } finally {
    await rm(directory, { recursive: true, force: true })
  }
})

test("strict provenance rejects a source missing from the declared commit", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-publication-provenance-test-"))
  try {
    const sourcePath = path.join(directory, "uncommitted.md")
    await writeFile(sourcePath, "# Uncommitted publication\n")
    const source = { absolute: sourcePath, relative: "content/uncommitted.md" }
    await assert.rejects(determineSourceProvenance(source, "HEAD"), /not present at declared source commit/)
    const preview = await determineSourceProvenance(source, "HEAD", { allowDirtyPreview: true })
    assert.equal(preview.state, "dirty-preview")
    assert.equal(preview.committedBlob, null)
    assert.match(preview.workingBlob, /^[0-9a-f]{40}$/)
  } finally {
    await rm(directory, { recursive: true, force: true })
  }
})
