import assert from "node:assert/strict"
import { createHash } from "node:crypto"
import { mkdtemp, readFile, rename, rm, stat, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"

import {
  finalizePublicationPair,
  parseArgs,
  verifyPublicationPair,
} from "./render-publication-pdf.mjs"

async function temporary(t) {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-publication-finalization-"))
  t.after(() => rm(directory, { recursive: true, force: true }))
  return directory
}

function digest(value) {
  return createHash("sha256").update(value).digest("hex")
}

async function writePair(pdfPath, manifestPath, pdfContent, declaredDigest = digest(pdfContent)) {
  await writeFile(pdfPath, pdfContent)
  await writeFile(
    manifestPath,
    `${JSON.stringify({ pdf_sha256: declaredDigest })}\n`,
  )
}

test("custom publication source requires an explicit output path", () => {
  assert.throws(
    () => parseArgs(["content/research/notes/custom.md"]),
    /requires --output/,
  )
  assert.deepEqual(
    parseArgs([
      "content/research/notes/custom.md",
      "--output",
      "dist/pdf/custom.pdf",
    ]),
    {
      source: "content/research/notes/custom.md",
      output: "dist/pdf/custom.pdf",
      splitDenseFigures: true,
      allowDirtyPreview: false,
      help: false,
    },
  )
})

test("candidate checksum mismatch preserves the previous publication pair", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writePair(outputPdf, outputManifest, "old pdf")
  await writePair(candidatePdf, candidateManifest, "new pdf", "wrong")

  await assert.rejects(
    finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest),
    /checksum mismatch/,
  )
  assert.equal(await readFile(outputPdf, "utf8"), "old pdf")
  await verifyPublicationPair(outputPdf, outputManifest)
})

test("incomplete existing publication bundle is rejected before replacement", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writeFile(outputPdf, "orphaned old pdf")
  await writePair(candidatePdf, candidateManifest, "new pdf")

  await assert.rejects(
    finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest),
    /Existing publication bundle is incomplete/,
  )
  assert.equal(await readFile(outputPdf, "utf8"), "orphaned old pdf")
  assert.equal(await readFile(candidatePdf, "utf8"), "new pdf")
})

test("invalid existing publication bundle is rejected before replacement", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writePair(outputPdf, outputManifest, "old pdf", "wrong")
  await writePair(candidatePdf, candidateManifest, "new pdf")
  const previousManifest = await readFile(outputManifest, "utf8")

  await assert.rejects(
    finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest),
    /Existing publication bundle is invalid/,
  )
  assert.equal(await readFile(outputPdf, "utf8"), "old pdf")
  assert.equal(await readFile(outputManifest, "utf8"), previousManifest)
})

test("manifest install failure restores the previous publication pair", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writePair(outputPdf, outputManifest, "old pdf")
  await writePair(candidatePdf, candidateManifest, "new pdf")

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
  await verifyPublicationPair(outputPdf, outputManifest)
})

test("post-install verification failure restores the previous publication pair", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writePair(outputPdf, outputManifest, "old pdf")
  await writePair(candidatePdf, candidateManifest, "new pdf")

  let verifications = 0
  await assert.rejects(
    finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest, {
      verifyImpl: async (pdf, manifest) => {
        verifications += 1
        if (verifications === 3) throw new Error("injected installed-pair verification failure")
        return verifyPublicationPair(pdf, manifest)
      },
    }),
    /injected installed-pair verification failure/,
  )
  assert.equal(await readFile(outputPdf, "utf8"), "old pdf")
  await verifyPublicationPair(outputPdf, outputManifest)
})

test("rollback failure retains recovery files", async (t) => {
  const directory = await temporary(t)
  const outputPdf = path.join(directory, "paper.pdf")
  const outputManifest = path.join(directory, "paper.manifest.json")
  const candidatePdf = path.join(directory, "candidate.pdf")
  const candidateManifest = path.join(directory, "candidate.manifest.json")
  await writePair(outputPdf, outputManifest, "old pdf")
  await writePair(candidatePdf, candidateManifest, "new pdf")

  let calls = 0
  let message = ""
  try {
    await finalizePublicationPair(candidatePdf, candidateManifest, outputPdf, outputManifest, {
      renameImpl: async (source, target) => {
        calls += 1
        if (calls === 4) throw new Error("injected install failure")
        if (calls === 5) throw new Error("injected rollback failure")
        await rename(source, target)
      },
    })
    assert.fail("Expected finalization to fail")
  } catch (error) {
    message = error.message
  }

  assert.match(message, /rollback incomplete, recovery files retained at/)
  const match = /recovery files retained at ([^:]+):/.exec(message)
  assert.ok(match)
  const recoveryDirectory = match[1]
  assert.equal((await stat(recoveryDirectory)).isDirectory(), true)
  assert.equal(await readFile(path.join(recoveryDirectory, "paper.manifest.json"), "utf8"), `${JSON.stringify({ pdf_sha256: digest("old pdf") })}\n`)
})
