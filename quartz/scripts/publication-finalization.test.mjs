import assert from "node:assert/strict"
import { mkdir, mkdtemp, readFile, rename, rm, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"

import { finalizePublicationPair } from "./render-publication-pdf.mjs"
import {
  buildFigure8CaptionDocument,
  finalizePublicationDirectory,
  remapAssetManifestPaths,
} from "./run-publication-assets.mjs"

async function temporary(t) {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-publication-finalization-"))
  t.after(() => rm(directory, { recursive: true, force: true }))
  return directory
}

test("PDF and manifest publication pair rolls back together when manifest install fails", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writeFile(outputPdf, "old pdf")
  await writeFile(outputManifest, "old manifest")
  await writeFile(candidatePdf, "new pdf")
  await writeFile(candidateManifest, "new manifest")

  let calls = 0
  await assert.rejects(
    finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest, {
      renameImpl: async (source, target) => {
        calls += 1
        if (calls === 4) throw new Error("injected manifest install failure")
        await rename(source, target)
      },
    }),
    /injected manifest install failure/,
  )

  assert.equal(await readFile(outputPdf, "utf8"), "old pdf")
  assert.equal(await readFile(outputManifest, "utf8"), "old manifest")
})

test("asset directory transaction preserves the previous complete bundle on install failure", async (t) => {
  const directory = await temporary(t)
  const output = path.join(directory, "thinking-systems")
  const staging = path.join(directory, "staging")
  await mkdir(output)
  await mkdir(staging)
  await writeFile(path.join(output, "marker.txt"), "old bundle")
  await writeFile(path.join(staging, "marker.txt"), "new bundle")

  let calls = 0
  await assert.rejects(
    finalizePublicationDirectory(staging, output, {
      renameImpl: async (source, target) => {
        calls += 1
        if (calls === 2) throw new Error("injected bundle install failure")
        await rename(source, target)
      },
    }),
    /injected bundle install failure/,
  )

  assert.equal(await readFile(path.join(output, "marker.txt"), "utf8"), "old bundle")
})

test("asset manifest paths are rewritten from staging to the durable bundle root", () => {
  const manifest = {
    figures: [
      {
        svg: "dist/publication/.ua-assets-stage-123/figures/svg/figure-01.svg",
        png: "dist/publication/.ua-assets-stage-123/figures/png/figure-01.png",
      },
    ],
    covers: {
      linkedin: {
        path: "dist/publication/.ua-assets-stage-123/cover-linkedin-article.png",
      },
    },
  }
  remapAssetManifestPaths(
    manifest,
    "dist/publication/.ua-assets-stage-123",
    "dist/publication/thinking-systems",
  )
  assert.equal(
    manifest.figures[0].svg,
    "dist/publication/thinking-systems/figures/svg/figure-01.svg",
  )
  assert.equal(
    manifest.covers.linkedin.path,
    "dist/publication/thinking-systems/cover-linkedin-article.png",
  )
})

test("Figure 8 platform caption requires both panels and the complete canonical caption", () => {
  const caption =
    "**Figure 8 — Two orthogonal models.** Full decision, authority, reassessment, and capability semantics."
  const document = buildFigure8CaptionDocument(caption)
  assert.match(document, /Full decision, authority, reassessment, and capability semantics/)
  assert.match(document, /Publish them together with this complete canonical caption/)
  assert.match(document, /neither panel is a standalone replacement/)
})
