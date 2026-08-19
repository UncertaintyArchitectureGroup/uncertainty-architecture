import assert from "node:assert/strict"
import { link, mkdir, mkdtemp, readFile, rm, symlink, writeFile } from "node:fs/promises"
import os from "node:os"
import path from "node:path"
import test from "node:test"

import {
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs"
import { determineSourceProvenance } from "./publication-provenance.mjs"
import { currentArticleSource } from "./publication-rendition.mjs"

test("output safety rejects a symlinked allowed root", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-output-root-test-"))
  const trusted = path.join(root, "repo")
  const outside = path.join(root, "outside")
  await mkdir(trusted)
  await mkdir(outside)
  await symlink(outside, path.join(trusted, "dist"))
  await assert.rejects(
    assertSafeOutputPath(
      trusted,
      path.join(trusted, "dist", "pdf"),
      path.join(trusted, "dist", "pdf", "paper.pdf"),
    ),
    /symbolic-link component/,
  )
  await rm(root, { recursive: true, force: true })
})

test("output safety rejects a nested symlink parent", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-output-parent-test-"))
  const trusted = path.join(root, "repo")
  const allowed = path.join(trusted, "dist", "pdf")
  const outside = path.join(root, "outside")
  await mkdir(allowed, { recursive: true })
  await mkdir(outside)
  await symlink(outside, path.join(allowed, "alias"))
  await assert.rejects(
    assertSafeOutputPath(
      trusted,
      allowed,
      path.join(allowed, "alias", "paper.pdf"),
    ),
    /symbolic-link component/,
  )
  await rm(root, { recursive: true, force: true })
})

test("atomic manifest writer rejects symlink and hardlink aliases to source", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-output-alias-test-"))
  const trusted = path.join(root, "repo")
  const allowed = path.join(trusted, "dist", "pdf")
  const source = path.join(trusted, "content.md")
  await mkdir(allowed, { recursive: true })
  await writeFile(source, "# Canonical Markdown\n")

  const symlinkTarget = path.join(allowed, "symlink.manifest.json")
  await symlink(source, symlinkTarget)
  await assert.rejects(
    writeFileAtomically(symlinkTarget, "{}\n", {
      trustedRoot: trusted,
      allowedRoot: allowed,
      forbiddenPaths: [source],
    }),
    /symbolic link|symbolic-link component/,
  )
  await rm(symlinkTarget)

  const hardlinkTarget = path.join(allowed, "hardlink.manifest.json")
  await link(source, hardlinkTarget)
  await assert.rejects(
    writeFileAtomically(hardlinkTarget, "{}\n", {
      trustedRoot: trusted,
      allowedRoot: allowed,
      forbiddenPaths: [source],
    }),
    /aliases a protected source/,
  )
  assert.equal(await readFile(source, "utf8"), "# Canonical Markdown\n")
  await rm(root, { recursive: true, force: true })
})

test("atomic manifest writer preserves previous output when final rename fails", async () => {
  const root = await mkdtemp(path.join(os.tmpdir(), "ua-output-atomic-test-"))
  const trusted = path.join(root, "repo")
  const allowed = path.join(trusted, "dist", "pdf")
  const target = path.join(allowed, "paper.manifest.json")
  await mkdir(allowed, { recursive: true })
  await writeFile(target, "previous manifest\n")
  await assert.rejects(
    writeFileAtomically(target, "new manifest\n", {
      trustedRoot: trusted,
      allowedRoot: allowed,
      renameImpl: async () => {
        throw new Error("injected manifest finalization failure")
      },
    }),
    /injected manifest finalization failure/,
  )
  assert.equal(await readFile(target, "utf8"), "previous manifest\n")
  await rm(root, { recursive: true, force: true })
})

test("strict provenance rejects modified bytes for a tracked source", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-provenance-modified-test-"))
  const modified = path.join(directory, "modified.md")
  await writeFile(modified, "# Different working-tree bytes\n")
  const source = { absolute: modified, relative: currentArticleSource }
  await assert.rejects(
    determineSourceProvenance(source, "HEAD"),
    /do not match declared source commit/,
  )
  const preview = await determineSourceProvenance(source, "HEAD", {
    allowDirtyPreview: true,
  })
  assert.equal(preview.state, "dirty-preview")
  assert.notEqual(preview.workingBlob, preview.committedBlob)
  await rm(directory, { recursive: true, force: true })
})
