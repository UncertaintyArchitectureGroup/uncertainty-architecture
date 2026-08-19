#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import textwrap
from pathlib import Path

ROOT = Path.cwd()
BASELINE = "fa260c4ab42d13ab7c0593d5ee71b65c4614d541"
BRANCH = "feat/quartz-pdf-export"

INTENDED_PATHS = [
    ".github/policy/repository-contract-change-coupling.json",
    ".github/tests/repository_contract/cases.json",
    ".github/tests/repository_contract/test_repository_contract.py",
    ".github/workflows/build-integrity.yml",
    ".github/workflows/export-research-pdf.yml",
    ".gitignore",
    "CHANGELOG.md",
    "ROADMAP.md",
    "package-lock.json",
    "package.json",
    "quartz.config.ts",
    "quartz/PDF-EXPORT.md",
    "quartz/scripts/export-pdf.mjs",
    "quartz/scripts/export-pdf.test.mjs",
    "quartz/scripts/publication-figure8-fingerprint.mjs",
    "quartz/scripts/publication-figure8.mjs",
    "quartz/scripts/publication-path-safety.mjs",
    "quartz/scripts/publication-rendition.mjs",
    "quartz/scripts/publication-rendition.test.mjs",
    "quartz/scripts/render-publication-assets.mjs",
    "quartz/scripts/render-publication-pdf.mjs",
    "quartz/scripts/run-pdf-export.mjs",
    "quartz/scripts/run-publication-assets.mjs",
    "quartz/scripts/run-publication-verify.mjs",
    "quartz/scripts/verify-publication-pdf.mjs",
    "quartz/styles/custom.scss",
]


def run(*args: str, check: bool = True, capture: bool = False, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        list(args),
        cwd=ROOT,
        check=check,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        env=env,
    )


def git_show(commit: str, path: str) -> bytes:
    proc = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return proc.stdout


def write(path: str, content: str | bytes) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        target.write_bytes(content)
    else:
        target.write_text(textwrap.dedent(content).lstrip("\n"), encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one match, got {text.count(old)}")
    return text.replace(old, new, 1)


print("Fetching current main and clean baseline...")
run("git", "fetch", "origin", "main")
run("git", "fetch", "origin", BASELINE)
saved = {path: git_show(BASELINE, path) for path in INTENDED_PATHS}
run("git", "reset", "--hard", "origin/main")
run("git", "clean", "-fdx")
for path, data in saved.items():
    write(path, data)

# ---------------------------------------------------------------------------
# Shared path safety: trusted repository anchor, no symlinked output roots,
# alias protection, and atomic generated-file writes.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/publication-path-safety.mjs",
    r'''
    import { lstat, mkdir, mkdtemp, realpath, rename, rm, stat, writeFile } from "node:fs/promises"
    import path from "node:path"

    export function isInsidePath(parent, candidate) {
      const relative = path.relative(parent, candidate)
      return relative === "" || (!relative.startsWith(`..${path.sep}`) && relative !== ".." && !path.isAbsolute(relative))
    }

    async function lstatIfExists(candidate) {
      try {
        return await lstat(candidate)
      } catch (error) {
        if (error?.code === "ENOENT") return null
        throw error
      }
    }

    async function assertExistingTrustedDirectory(candidate, label) {
      const info = await lstat(candidate)
      if (info.isSymbolicLink()) throw new Error(`${label} must not be a symbolic link: ${candidate}`)
      if (!info.isDirectory()) throw new Error(`${label} must be a directory: ${candidate}`)
    }

    async function assertNoSymlinkComponents(trustedRoot, candidate) {
      if (!isInsidePath(trustedRoot, candidate)) {
        throw new Error(`Path escapes trusted repository root: ${candidate}`)
      }
      const relative = path.relative(trustedRoot, candidate)
      let cursor = trustedRoot
      for (const part of relative.split(path.sep).filter(Boolean)) {
        cursor = path.join(cursor, part)
        const info = await lstatIfExists(cursor)
        if (!info) break
        if (info.isSymbolicLink()) {
          throw new Error(`Output path contains a symbolic-link component: ${cursor}`)
        }
      }
    }

    async function nearestExistingAncestor(candidate) {
      let cursor = candidate
      while (!(await lstatIfExists(cursor))) {
        const parent = path.dirname(cursor)
        if (parent === cursor) throw new Error(`Unable to find an existing ancestor for ${candidate}`)
        cursor = parent
      }
      return cursor
    }

    export async function assertSafeOutputPath(
      trustedRoot,
      allowedRoot,
      candidate,
      { allowRoot = false, createRoot = true } = {},
    ) {
      const lexicalTrusted = path.resolve(trustedRoot)
      const lexicalAllowed = path.resolve(allowedRoot)
      const lexicalCandidate = path.resolve(candidate)

      await assertExistingTrustedDirectory(lexicalTrusted, "Trusted repository root")
      if (!isInsidePath(lexicalTrusted, lexicalAllowed) || lexicalAllowed === lexicalTrusted) {
        throw new Error(`Allowed output root must be a named directory inside ${lexicalTrusted}`)
      }
      if (!isInsidePath(lexicalAllowed, lexicalCandidate) || (!allowRoot && lexicalCandidate === lexicalAllowed)) {
        throw new Error(`Output must remain inside ${lexicalAllowed}`)
      }

      // Check the path before and after creation to close both pre-existing and
      // newly introduced symlink-root/parent escape paths.
      await assertNoSymlinkComponents(lexicalTrusted, lexicalAllowed)
      if (createRoot) await mkdir(lexicalAllowed, { recursive: true })
      await assertNoSymlinkComponents(lexicalTrusted, lexicalAllowed)
      if (await lstatIfExists(lexicalAllowed)) {
        await assertExistingTrustedDirectory(lexicalAllowed, "Allowed output root")
      }
      await assertNoSymlinkComponents(lexicalTrusted, lexicalCandidate)

      const [realTrusted, realAllowed] = await Promise.all([
        realpath(lexicalTrusted),
        realpath(lexicalAllowed),
      ])
      if (!isInsidePath(realTrusted, realAllowed) || realAllowed === realTrusted) {
        throw new Error(`Allowed output root resolves outside the trusted repository: ${lexicalAllowed}`)
      }
      const ancestor = await nearestExistingAncestor(path.dirname(lexicalCandidate))
      const realAncestor = await realpath(ancestor)
      if (!isInsidePath(realAllowed, realAncestor)) {
        throw new Error(`Output ancestor resolves outside the allowed root: ${ancestor}`)
      }

      return { trustedRoot: realTrusted, allowedRoot: realAllowed, candidate: lexicalCandidate }
    }

    export async function assertNoPathAliases(candidate, forbiddenPaths = []) {
      const candidateInfo = await lstatIfExists(candidate)
      if (!candidateInfo) return
      if (candidateInfo.isSymbolicLink()) {
        throw new Error(`Generated output must not be a symbolic link: ${candidate}`)
      }
      if (!candidateInfo.isFile()) {
        throw new Error(`Generated output must be a regular file: ${candidate}`)
      }
      const resolvedCandidate = await stat(candidate)
      for (const forbidden of forbiddenPaths) {
        let forbiddenInfo
        try {
          forbiddenInfo = await stat(forbidden)
        } catch (error) {
          if (error?.code === "ENOENT") continue
          throw error
        }
        if (resolvedCandidate.dev === forbiddenInfo.dev && resolvedCandidate.ino === forbiddenInfo.ino) {
          throw new Error(`Generated output aliases protected source: ${forbidden}`)
        }
      }
    }

    export async function atomicWriteFile(
      destination,
      data,
      { encoding = undefined, forbiddenPaths = [], renameImpl = rename } = {},
    ) {
      const directory = path.dirname(destination)
      await assertNoPathAliases(destination, forbiddenPaths)
      const stagingDirectory = await mkdtemp(path.join(directory, ".ua-generated-stage-"))
      const staged = path.join(stagingDirectory, path.basename(destination))
      try {
        await writeFile(staged, data, encoding ? { encoding } : undefined)
        const stagedInfo = await stat(staged)
        if (!stagedInfo.isFile() || stagedInfo.size === 0) {
          throw new Error(`Generated staging file is empty or invalid: ${staged}`)
        }
        await renameImpl(staged, destination)
      } finally {
        await rm(stagingDirectory, { recursive: true, force: true })
      }
    }

    export const writeFileAtomically = atomicWriteFile
    ''',
)

write(
    "quartz/scripts/publication-provenance.mjs",
    r'''
    import { spawn } from "node:child_process"

    export function gitOutput(args, { repositoryRoot = process.cwd() } = {}) {
      return new Promise((resolve, reject) => {
        const child = spawn("git", args, { cwd: repositoryRoot, stdio: ["ignore", "pipe", "pipe"] })
        let stdout = ""
        let stderr = ""
        child.stdout.on("data", (chunk) => (stdout += chunk))
        child.stderr.on("data", (chunk) => (stderr += chunk))
        child.once("error", reject)
        child.once("exit", (code) => {
          if (code === 0) return resolve(stdout.trim())
          reject(new Error(`git ${args.join(" ")} failed: ${stderr.trim()}`))
        })
      })
    }

    export async function determineSourceProvenance(
      source,
      declaredCommit,
      { allowDirtyPreview = false, repositoryRoot = process.cwd() } = {},
    ) {
      const workingBlob = await gitOutput(["hash-object", "--", source.absolute], { repositoryRoot })
      let committedBlob = null
      let commitAvailable = true
      try {
        await gitOutput(["rev-parse", "--verify", `${declaredCommit}^{commit}`], { repositoryRoot })
        committedBlob = await gitOutput(["rev-parse", `${declaredCommit}:${source.relative}`], {
          repositoryRoot,
        })
      } catch (error) {
        commitAvailable = false
        if (!allowDirtyPreview) {
          throw new Error(
            `Publication source is not available at declared source commit ${declaredCommit}: ${source.relative}. Ensure the commit is checked out/fetched, commit the source, or use --allow-dirty-preview only for a non-versioned local preview.`,
          )
        }
      }

      const dirty = !commitAvailable || committedBlob !== workingBlob
      if (dirty && !allowDirtyPreview) {
        throw new Error(
          `Publication source bytes do not match declared source commit ${declaredCommit}: ${source.relative}. Commit the source before producing a versioned publication, or use --allow-dirty-preview for an explicitly dirty local preview.`,
        )
      }

      return {
        state: dirty ? "dirty-preview" : "committed",
        declaredCommit,
        workingBlob,
        committedBlob,
      }
    }
    ''',
)

write(
    "quartz/scripts/publication-cover.mjs",
    r'''
    const PROFILES = {
      "LinkedIn article": { maxWidth: 41, maxLines: 3 },
      "social preview": { maxWidth: 33, maxLines: 3 },
      "Medium hero": { maxWidth: 33, maxLines: 3 },
    }

    function glyphUnits(character) {
      if (/\s/.test(character)) return 0.35
      if (/[ilI1|.,:;'`!]/.test(character)) return 0.42
      if (/[MW@#%&]/.test(character)) return 1.25
      if (/[A-Z0-9]/.test(character)) return 0.9
      return 0.72
    }

    function textUnits(value) {
      return [...String(value)].reduce((sum, character) => sum + glyphUnits(character), 0)
    }

    export function layoutCoverTitle(title, profileName) {
      const profile = PROFILES[profileName]
      if (!profile) throw new Error(`Unknown cover profile: ${profileName}`)
      const words = String(title).trim().split(/\s+/).filter(Boolean)
      if (words.length === 0) throw new Error("Publication title is empty")
      for (const word of words) {
        if (textUnits(word) > profile.maxWidth) {
          throw new Error(`${profileName} cover contains an unbreakable token wider than the title area: ${word}`)
        }
      }
      const lines = []
      let current = ""
      for (const word of words) {
        const candidate = current ? `${current} ${word}` : word
        if (current && textUnits(candidate) > profile.maxWidth) {
          lines.push(current)
          current = word
        } else {
          current = candidate
        }
      }
      if (current) lines.push(current)
      if (lines.length > profile.maxLines) {
        throw new Error(
          `${profileName} cover title requires ${lines.length} lines; renderer supports at most ${profile.maxLines} without truncation. Shorten the title or implement an explicit fit strategy.`,
        )
      }
      return { lines, profile }
    }

    export function assertCoverTitleFits(title) {
      return Object.keys(PROFILES).map((profileName) => ({
        profileName,
        ...layoutCoverTitle(title, profileName),
      }))
    }
    ''',
)

# Keep the reviewed exact fingerprint from the clean baseline; overwrite only if absent.
if not (ROOT / "quartz/scripts/publication-figure8-fingerprint.mjs").exists():
    raise RuntimeError("Reviewed Figure 8 fingerprint file missing from baseline")

# ---------------------------------------------------------------------------
# Publication rendition: fail-closed current Figure 8, provenance-aware title.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/publication-rendition.mjs",
    r'''
    import { createHash } from "node:crypto"
    import { mkdtemp, readFile, realpath, rm, stat, writeFile } from "node:fs/promises"
    import os from "node:os"
    import path from "node:path"
    import { spawn } from "node:child_process"
    import { fileURLToPath } from "node:url"
    import matter from "gray-matter"
    import GithubSlugger from "github-slugger"
    import {
      assertFigure8SemanticSource,
      buildFigure8CapabilitySvg,
      buildFigure8DecisionSvg,
    } from "./publication-figure8.mjs"
    import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs"

    export const repoRoot = path.resolve(fileURLToPath(new URL("../..", import.meta.url)))
    export const contentRoot = path.join(repoRoot, "content")
    export const defaultRepository = "UncertaintyArchitectureGroup/uncertainty-architecture"
    export const currentPublicationArticle = "content/research/notes/thinking-systems-publication-draft.md"
    export const currentArticleSource = currentPublicationArticle

    export function isInside(parent, candidate) {
      const relative = path.relative(parent, candidate)
      return relative === "" || (!relative.startsWith(`..${path.sep}`) && relative !== ".." && !path.isAbsolute(relative))
    }

    export function run(command, args, options = {}) {
      return new Promise((resolve, reject) => {
        const child = spawn(command, args, { stdio: "inherit", ...options })
        child.once("error", reject)
        child.once("exit", (code, signal) => {
          if (code === 0) return resolve()
          reject(new Error(`${path.basename(command)} exited with ${signal ? `signal ${signal}` : `code ${code}`}`))
        })
      })
    }

    export function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;")
    }

    export function sha256(buffer) {
      return createHash("sha256").update(buffer).digest("hex")
    }

    export function normalizeDate(value) {
      if (!value) return null
      if (value instanceof Date) return value.toISOString().slice(0, 10)
      const text = String(value).trim()
      const isoPrefix = /^(\d{4}-\d{2}-\d{2})(?:[T\s].*)?$/.exec(text)
      return isoPrefix ? isoPrefix[1] : text
    }

    export function gitOutput(args) {
      return new Promise((resolve, reject) => {
        const child = spawn("git", args, { cwd: repoRoot, stdio: ["ignore", "pipe", "pipe"] })
        let stdout = ""
        let stderr = ""
        child.stdout.on("data", (chunk) => (stdout += chunk))
        child.stderr.on("data", (chunk) => (stderr += chunk))
        child.once("error", reject)
        child.once("exit", (code) => {
          if (code === 0) return resolve(stdout.trim())
          reject(new Error(`git ${args.join(" ")} failed: ${stderr.trim()}`))
        })
      })
    }

    export function normalizeAuthors(value) {
      const entries = Array.isArray(value) ? value : value ? [value] : []
      return entries
        .map((entry) => {
          if (typeof entry === "string") return entry.trim()
          if (!entry || typeof entry !== "object") return ""
          if (typeof entry.name === "string") return entry.name.trim()
          const given = entry["given-names"] ?? entry.givenNames ?? ""
          const family = entry["family-names"] ?? entry.familyNames ?? ""
          return [given, family].filter(Boolean).join(" ").trim()
        })
        .filter(Boolean)
    }

    function extractHeadingTitle(content, fallback) {
      const match = content.match(/^#\s+(.+)$/m)
      return match?.[1]?.trim() || fallback
    }

    function humanLicense(value) {
      if (!value) return "CC BY 4.0"
      return String(value).replace(/^CC-BY-4\.0$/i, "CC BY 4.0")
    }

    function buildTitlePage({ data, content, sourceRelative, sourceCommit, repository, provenance }) {
      const title = data.title || extractHeadingTitle(content, path.basename(sourceRelative, ".md"))
      const authors = normalizeAuthors(data.authors ?? data.author)
      const statusParts = [...new Set([data.status, data.maturity, data.draft === true ? "draft" : undefined].filter(Boolean).map(String))]
      const publicationDate = normalizeDate(data.publication_date)
      const editionDate = publicationDate || normalizeDate(data.updated) || normalizeDate(data.created) || new Date().toISOString().slice(0, 10)
      const dateLabel = publicationDate ? "Publication date" : "Edition date"
      const version = data.edition || data.version || (data.draft === true ? "Draft" : "Unversioned")
      const repoUrl = `https://github.com/${repository}`
      const sourceUrl = `${repoUrl}/blob/${encodeURIComponent(sourceCommit)}/${sourceRelative.split("/").map(encodeURIComponent).join("/")}`
      const canonical = data.canonical_url ? `<br/><a href="${escapeHtml(data.canonical_url)}">Canonical publication</a>` : ""
      const authorLine = authors.length > 0 ? authors.join(" · ") : "Author not declared in source metadata"
      const dirty = provenance?.state === "dirty-preview"
      const stateNotice = dirty
        ? `<p class="ua-pdf-preview-warning"><strong>Uncommitted local preview.</strong> The rendered bytes differ from the declared base commit and are not a versioned publication edition.</p>`
        : ""
      const sourceLabel = dirty ? "Declared base commit" : "Source commit"
      const linkLabel = dirty ? "Declared base source (preview differs)" : "Versioned source"
      const workingBlob = dirty && provenance?.workingBlob
        ? `<div><dt>Working-tree blob</dt><dd><code>${escapeHtml(provenance.workingBlob.slice(0, 12))}</code></dd></div>`
        : ""

      return `<section class="ua-pdf-title-page">
      <div class="ua-pdf-title-kicker">Uncertainty Architecture · Research Publication</div>
      <h1>${escapeHtml(title)}</h1>
      <p class="ua-pdf-title-author">${escapeHtml(authorLine)}</p>
      ${stateNotice}
      <dl class="ua-pdf-title-meta">
        <div><dt>Status</dt><dd>${escapeHtml(statusParts.join(" · ") || "Research")}</dd></div>
        <div><dt>${escapeHtml(dateLabel)}</dt><dd>${escapeHtml(editionDate)}</dd></div>
        <div><dt>Version</dt><dd>${escapeHtml(version)}</dd></div>
        <div><dt>License</dt><dd>${escapeHtml(humanLicense(data.license))}</dd></div>
        <div><dt>${escapeHtml(sourceLabel)}</dt><dd><code>${escapeHtml(sourceCommit.slice(0, 12))}</code></dd></div>
        ${workingBlob}
      </dl>
      <p class="ua-pdf-title-links"><a href="${escapeHtml(repoUrl)}">${escapeHtml(repoUrl)}</a><br/><a href="${escapeHtml(sourceUrl)}">${escapeHtml(linkLabel)}</a>${canonical}</p>
    </section>`
    }

    export function buildToc(content) {
      const slugger = new GithubSlugger()
      const entries = []
      for (const line of content.split(/\r?\n/)) {
        const match = /^(#{2,3})\s+(.+?)\s*$/.exec(line)
        if (!match) continue
        const text = match[2].replace(/\[(.*?)\]\([^)]*\)/g, "$1").replace(/[*_`]/g, "").trim()
        entries.push({ level: match[1].length, text, slug: slugger.slug(text) })
      }
      if (entries.length === 0) return ""
      const items = entries
        .map((entry) => `<li class="ua-pdf-toc-level-${entry.level}"><a href="#${escapeHtml(entry.slug)}">${escapeHtml(entry.text)}</a></li>`)
        .join("\n")
      return `<section class="ua-pdf-toc"><h2>Contents</h2><ul>${items}</ul></section>`
    }

    export function splitFigure8(content, { verifyFingerprint = true } = {}) {
      const pattern = /```mermaid\n((?:(?!\n```)[\s\S])*)\n```\n\n(\*\*Figure 8 —[^\n]*)(?=\n\n|$)/
      const match = content.match(pattern)
      if (!match) return { content, split: false }
      const mermaid = match[1]
      const caption = match[2]
      if (!/\bsubgraph\s+L(?:\[|\s|$)/.test(mermaid) || !/\bsubgraph\s+F(?:\[|\s|$)/.test(mermaid)) {
        return { content, split: false }
      }
      assertFigure8SemanticSource(mermaid)
      if (verifyFingerprint) assertCanonicalFigure8Fingerprint(mermaid, caption)
      const canonicalCaption = caption.replace(/^\*\*Figure 8 —\s*/, "").replace(/\*\*/, "").trim()
      const panelA = `<section class="ua-pdf-static-figure ua-pdf-static-figure--8a">${buildFigure8DecisionSvg()}<p><strong>Figure 8A — Decision-ownership model.</strong> Publication rendition of canonical Figure 8; continue with Figure 8B.</p></section>`
      const panelB = `<section class="ua-pdf-static-figure ua-pdf-static-figure--8b">${buildFigure8CapabilitySvg()}<p><strong>Figure 8B — Capability-family axis and orthogonality relationship.</strong> Publication rendition of canonical Figure 8.</p></section>`
      const shared = `**Together, Figures 8A–8B preserve canonical Figure 8.** ${canonicalCaption}`
      return { content: content.replace(pattern, `${panelA}\n\n${panelB}\n\n${shared}`), split: true }
    }

    export function extractFigureList(content) {
      const figures = []
      const regex = /(?:\*\*|<strong>)Figure\s+(\d+)([AB])?\s+—\s+([^*<\n]+?)(?:\.\*\*|\.<\/strong>)/g
      let match
      while ((match = regex.exec(content)) !== null) {
        figures.push({ number: Number(match[1]), panel: match[2] || null, title: match[3].trim() })
      }
      return figures
    }

    export async function loadPublicationSource(sourcePath) {
      const requested = path.resolve(repoRoot, sourcePath)
      if (path.extname(requested).toLowerCase() !== ".md") throw new Error("Publication source must have a .md extension")
      const absolute = await realpath(requested)
      if (!isInside(contentRoot, absolute)) throw new Error("Publication source must be a Markdown file under content/")
      if (!(await stat(absolute)).isFile()) throw new Error("Publication source must be a regular Markdown file")
      const raw = await readFile(absolute, "utf8")
      const parsed = matter(raw)
      return { absolute, relative: path.relative(repoRoot, absolute).split(path.sep).join("/"), raw, data: parsed.data, content: parsed.content }
    }

    export async function buildPublicationRendition(
      source,
      {
        includeToc = false,
        splitDenseFigures = true,
        sourceCommit = undefined,
        provenance = undefined,
        requireFigure8Split = false,
      } = {},
    ) {
      const repository = process.env.GITHUB_REPOSITORY || defaultRepository
      const resolvedCommit = sourceCommit || process.env.UA_PDF_REPOSITORY_REF || process.env.GITHUB_SHA || (await gitOutput(["rev-parse", "HEAD"]))
      const sourceHash = sha256(Buffer.from(source.raw))
      const transformed = splitDenseFigures ? splitFigure8(source.content) : { content: source.content, split: false }
      if (requireFigure8Split && !transformed.split) {
        throw new Error("Current publication requires the reviewed Figure 8A/8B rendition, but canonical Figure 8 was not recognized. Review the canonical Figure 8 and update the publication fingerprint/rendition deliberately.")
      }
      const titlePage = buildTitlePage({
        data: source.data,
        content: source.content,
        sourceRelative: source.relative,
        sourceCommit: resolvedCommit,
        repository,
        provenance,
      })
      const toc = includeToc ? buildToc(transformed.content) : ""
      const body = [titlePage, toc, transformed.content].filter(Boolean).join("\n\n")
      const rendered = matter.stringify(body, { ...source.data, draft: true })
      return {
        rendered,
        sourceCommit: resolvedCommit,
        sourceHash,
        canonicalFigures: extractFigureList(source.content),
        renditionFigures: extractFigureList(transformed.content),
        figure8Split: transformed.split,
      }
    }

    export async function withTemporaryRendition(source, rendered, action) {
      const directory = path.dirname(source.absolute)
      const scratch = await mkdtemp(path.join(os.tmpdir(), "ua-publication-rendition-"))
      const tempName = `ua-publication-render-${process.pid}-${Date.now()}.md`
      const tempPath = path.join(directory, tempName)
      try {
        await writeFile(tempPath, rendered, "utf8")
        return await action(tempPath, scratch)
      } finally {
        await rm(tempPath, { force: true })
        await rm(scratch, { recursive: true, force: true })
      }
    }
    ''',
)

# ---------------------------------------------------------------------------
# Curated PDF renderer with strict provenance, trusted-root containment,
# fail-closed Figure 8, and rollback-capable PDF+manifest finalization.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/render-publication-pdf.mjs",
    r'''
    #!/usr/bin/env node

    import { mkdtemp, readFile, rename, rm, stat, writeFile } from "node:fs/promises"
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import {
      buildPublicationRendition,
      currentPublicationArticle,
      defaultRepository,
      loadPublicationSource,
      normalizeDate,
      repoRoot,
      run,
      sha256,
      withTemporaryRendition,
    } from "./publication-rendition.mjs"
    import { determineSourceProvenance } from "./publication-provenance.mjs"
    import {
      assertNoPathAliases,
      assertSafeOutputPath,
    } from "./publication-path-safety.mjs"

    export { determineSourceProvenance } from "./publication-provenance.mjs"

    const defaultArticle = currentPublicationArticle
    const defaultOutput = "dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf"
    const tocThresholdPages = 20
    const pdfRoot = path.join(repoRoot, "dist", "pdf")

    function parseArgs(argv) {
      let source = defaultArticle
      let output = defaultOutput
      let splitDenseFigures = true
      let allowDirtyPreview = false
      for (let i = 0; i < argv.length; i += 1) {
        const value = argv[i]
        if (value === "--source") source = argv[++i]
        else if (value === "--output" || value === "-o") output = argv[++i]
        else if (value === "--no-split-dense") splitDenseFigures = false
        else if (value === "--allow-dirty-preview") allowDirtyPreview = true
        else if (value === "--help" || value === "-h") return { help: true }
        else if (!value.startsWith("-") && source === defaultArticle) source = value
        else throw new Error(`Unknown argument: ${value}`)
      }
      if (!source || !output) throw new Error("Source and output paths are required")
      return { source, output, splitDenseFigures, allowDirtyPreview, help: false }
    }

    function usage() {
      console.log("Usage: node quartz/scripts/render-publication-pdf.mjs [source.md] [--output dist/pdf/file.pdf] [--allow-dirty-preview]")
    }

    export function countPdfPages(buffer) {
      const text = buffer.toString("latin1")
      return text.match(/\/Type\s*\/Page\b/g)?.length ?? 0
    }

    function manifestPathFor(pdfPath) {
      return pdfPath.replace(/\.pdf$/i, ".manifest.json")
    }

    async function exists(candidate) {
      try {
        await stat(candidate)
        return true
      } catch (error) {
        if (error?.code === "ENOENT") return false
        throw error
      }
    }

    async function renderWithGenericExporter(tempSourcePath, outputPath) {
      const relativeSource = path.relative(repoRoot, tempSourcePath).split(path.sep).join("/")
      const relativeOutput = path.relative(repoRoot, outputPath).split(path.sep).join("/")
      await run(
        process.execPath,
        [path.join(repoRoot, "quartz", "scripts", "export-pdf.mjs"), relativeSource, "--output", relativeOutput],
        { cwd: repoRoot },
      )
    }

    export async function finalizePublicationPdf(preflightPath, outputPath, renameImpl = rename) {
      await renameImpl(preflightPath, outputPath)
    }

    export async function finalizePublicationPair(
      candidatePdf,
      candidateManifest,
      outputPdf,
      outputManifest,
      { renameImpl = rename } = {},
    ) {
      const backupDirectory = await mkdtemp(path.join(path.dirname(outputPdf), ".ua-publication-backup-"))
      const pdfBackup = path.join(backupDirectory, path.basename(outputPdf))
      const manifestBackup = path.join(backupDirectory, path.basename(outputManifest))
      const hadPdf = await exists(outputPdf)
      const hadManifest = await exists(outputManifest)
      let installedPdf = false
      let installedManifest = false
      try {
        if (hadPdf) await renameImpl(outputPdf, pdfBackup)
        if (hadManifest) await renameImpl(outputManifest, manifestBackup)
        await renameImpl(candidatePdf, outputPdf)
        installedPdf = true
        await renameImpl(candidateManifest, outputManifest)
        installedManifest = true
      } catch (error) {
        if (installedManifest) await rm(outputManifest, { force: true })
        if (installedPdf) await rm(outputPdf, { force: true })
        if (hadManifest && (await exists(manifestBackup))) await rename(manifestBackup, outputManifest)
        if (hadPdf && (await exists(pdfBackup))) await rename(pdfBackup, outputPdf)
        throw error
      } finally {
        await rm(backupDirectory, { recursive: true, force: true })
      }
    }

    async function main() {
      const args = parseArgs(process.argv.slice(2))
      if (args.help) return usage()

      const source = await loadPublicationSource(args.source)
      const outputPath = path.resolve(repoRoot, args.output)
      const manifestPath = manifestPathFor(outputPath)
      if (path.extname(outputPath).toLowerCase() !== ".pdf") {
        throw new Error("Publication output must have a .pdf extension")
      }
      await assertSafeOutputPath(repoRoot, pdfRoot, outputPath)
      await assertSafeOutputPath(repoRoot, pdfRoot, manifestPath)
      await assertNoPathAliases(outputPath, [source.absolute])
      await assertNoPathAliases(manifestPath, [source.absolute])

      const sourceBefore = sha256(Buffer.from(source.raw))
      const declaredSourceCommit = process.env.UA_PDF_REPOSITORY_REF || process.env.GITHUB_SHA || (await new Promise((resolve, reject) => {
        const child = require("node:child_process").spawn("git", ["rev-parse", "HEAD"], { cwd: repoRoot, stdio: ["ignore", "pipe", "pipe"] })
        let stdout = ""; let stderr = ""
        child.stdout.on("data", (chunk) => (stdout += chunk)); child.stderr.on("data", (chunk) => (stderr += chunk))
        child.once("error", reject); child.once("exit", (code) => code === 0 ? resolve(stdout.trim()) : reject(new Error(stderr.trim())))
      }))
      const provenance = await determineSourceProvenance(source, declaredSourceCommit, {
        allowDirtyPreview: args.allowDirtyPreview,
        repositoryRoot: repoRoot,
      })
      const requireFigure8Split = source.relative === currentPublicationArticle && args.splitDenseFigures

      const buildDirectory = await mkdtemp(path.join(pdfRoot, ".ua-publication-build-"))
      const preflightPath = path.join(buildDirectory, "preflight.pdf")
      const finalCandidate = path.join(buildDirectory, "publication.pdf")
      const manifestCandidate = path.join(buildDirectory, "publication.manifest.json")
      let selected
      let pageCount
      let tocIncluded = false
      try {
        const withoutToc = await buildPublicationRendition(source, {
          includeToc: false,
          splitDenseFigures: args.splitDenseFigures,
          sourceCommit: declaredSourceCommit,
          provenance,
          requireFigure8Split,
        })
        selected = withoutToc
        await withTemporaryRendition(source, withoutToc.rendered, async (tempSourcePath) => {
          await renderWithGenericExporter(tempSourcePath, preflightPath)
        })
        pageCount = countPdfPages(await readFile(preflightPath))
        if (pageCount <= 0) throw new Error("Unable to determine publication PDF page count")

        if (pageCount > tocThresholdPages) {
          tocIncluded = true
          selected = await buildPublicationRendition(source, {
            includeToc: true,
            splitDenseFigures: args.splitDenseFigures,
            sourceCommit: declaredSourceCommit,
            provenance,
            requireFigure8Split,
          })
          await withTemporaryRendition(source, selected.rendered, async (tempSourcePath) => {
            await renderWithGenericExporter(tempSourcePath, finalCandidate)
          })
        } else {
          await rename(preflightPath, finalCandidate)
        }

        const pdfBuffer = await readFile(finalCandidate)
        pageCount = countPdfPages(pdfBuffer)
        const sourceAfter = sha256(Buffer.from(await readFile(source.absolute)))
        if (sourceBefore !== sourceAfter) {
          throw new Error("Canonical Markdown source changed during publication rendering")
        }

        const repository = process.env.GITHUB_REPOSITORY || defaultRepository
        const generatedAt = new Date().toISOString()
        const publicationDate = normalizeDate(source.data.publication_date)
        const editionDate = publicationDate || normalizeDate(source.data.updated) || normalizeDate(source.data.created) || generatedAt.slice(0, 10)
        const version = source.data.edition || source.data.version || (source.data.draft === true ? "Draft" : "Unversioned")
        const manifest = {
          schema_version: 1,
          artifact: "publication-pdf",
          title: source.data.title || null,
          source_path: source.relative,
          source_commit: declaredSourceCommit,
          source_state: provenance.state,
          source_git_blob_sha: provenance.committedBlob,
          source_working_blob_sha: provenance.workingBlob,
          source_sha256: sourceBefore,
          pdf_path: path.relative(repoRoot, outputPath).split(path.sep).join("/"),
          pdf_sha256: sha256(pdfBuffer),
          generated_at: generatedAt,
          publication_date: publicationDate,
          edition_date: editionDate,
          version: String(version),
          status: source.data.status || null,
          maturity: source.data.maturity || null,
          draft: source.data.draft === true,
          license: source.data.license || "CC-BY-4.0",
          repository_url: `https://github.com/${repository}`,
          canonical_url: source.data.canonical_url || null,
          additional_publication_urls: Array.isArray(source.data.additional_publication_urls) ? source.data.additional_publication_urls : [],
          page_count: pageCount,
          toc_included: tocIncluded,
          canonical_figures: selected.canonicalFigures,
          rendition_figures: selected.renditionFigures,
          figure_8_split_for_readability: selected.figure8Split,
        }
        await writeFile(manifestCandidate, `${JSON.stringify(manifest, null, 2)}\n`, "utf8")
        await finalizePublicationPair(finalCandidate, manifestCandidate, outputPath, manifestPath)
      } finally {
        await rm(buildDirectory, { recursive: true, force: true })
      }

      const info = await stat(outputPath)
      console.log(`Publication PDF ready: ${path.relative(repoRoot, outputPath)} (${pageCount} pages, ${info.size} bytes; source ${provenance.state})`)
      console.log(`Manifest: ${path.relative(repoRoot, manifestPath)}`)
      if (tocIncluded) console.log(`Clickable contents added because the preflight PDF exceeded ${tocThresholdPages} pages.`)
    }

    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) {
      main().catch((error) => {
        console.error(`Publication PDF failed: ${error instanceof Error ? error.message : String(error)}`)
        process.exitCode = 1
      })
    }
    ''',
)

# Fix the CommonJS require accidentally unsuitable for ESM in the generated renderer.
pdf_renderer = (ROOT / "quartz/scripts/render-publication-pdf.mjs").read_text(encoding="utf-8")
pdf_renderer = pdf_renderer.replace(
    'import { fileURLToPath } from "node:url"\n',
    'import { fileURLToPath } from "node:url"\nimport { spawn } from "node:child_process"\n',
)
pdf_renderer = pdf_renderer.replace(
    'const child = require("node:child_process").spawn("git", ["rev-parse", "HEAD"],',
    'const child = spawn("git", ["rev-parse", "HEAD"],',
)
write("quartz/scripts/render-publication-pdf.mjs", pdf_renderer)

# ---------------------------------------------------------------------------
# Platform assets renderer: core safety + provenance + exact Figure 8 panels.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/render-publication-assets.mjs",
    r'''
    #!/usr/bin/env node

    import { createReadStream } from "node:fs"
    import { mkdir, mkdtemp, readFile, rm, stat, writeFile } from "node:fs/promises"
    import http from "node:http"
    import os from "node:os"
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import { chromium } from "playwright"
    import sharp from "sharp"
    import {
      buildPublicationRendition,
      currentPublicationArticle,
      isInside,
      loadPublicationSource,
      normalizeAuthors,
      repoRoot,
      run,
      sha256,
      withTemporaryRendition,
    } from "./publication-rendition.mjs"
    import { determineSourceProvenance } from "./publication-provenance.mjs"
    import { assertSafeOutputPath, atomicWriteFile } from "./publication-path-safety.mjs"
    import { layoutCoverTitle } from "./publication-cover.mjs"
    import { buildFigure8CapabilitySvg, buildFigure8DecisionSvg } from "./publication-figure8.mjs"

    const defaultSource = currentPublicationArticle
    const defaultOutputRoot = "dist/publication/thinking-systems"
    const publicationOutputRoot = path.join(repoRoot, "dist", "publication")

    function parseArgs(argv) {
      let source = defaultSource
      let outputRoot = defaultOutputRoot
      let allowDirtyPreview = false
      for (let i = 0; i < argv.length; i += 1) {
        const value = argv[i]
        if (value === "--source") source = argv[++i]
        else if (value === "--output-root") outputRoot = argv[++i]
        else if (value === "--allow-dirty-preview") allowDirtyPreview = true
        else if (value === "--help" || value === "-h") return { help: true }
        else if (!value.startsWith("-") && source === defaultSource) source = value
        else throw new Error(`Unknown argument: ${value}`)
      }
      return { source, outputRoot, allowDirtyPreview, help: false }
    }

    function usage() {
      console.log("Usage: node quartz/scripts/render-publication-assets.mjs [source.md] [--output-root dist/publication/name] [--allow-dirty-preview]")
    }

    function contentType(filePath) {
      const ext = path.extname(filePath).toLowerCase()
      return ({ ".css": "text/css; charset=utf-8", ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".json": "application/json; charset=utf-8", ".png": "image/png", ".svg": "image/svg+xml", ".woff": "font/woff", ".woff2": "font/woff2" }[ext] || "application/octet-stream")
    }

    async function existingFile(candidate) {
      try { return (await stat(candidate)).isFile() } catch { return false }
    }

    async function startServer(root) {
      const server = http.createServer(async (request, response) => {
        try {
          const url = new URL(request.url || "/", "http://127.0.0.1")
          const decoded = decodeURIComponent(url.pathname).replace(/^\/+/, "")
          let candidate = path.resolve(root, decoded)
          if (!isInside(root, candidate)) throw new Error("outside publication root")
          try {
            const info = await stat(candidate)
            if (info.isDirectory()) candidate = path.join(candidate, "index.html")
          } catch {
            const html = `${candidate}.html`
            if (await existingFile(html)) candidate = html
          }
          if (!(await existingFile(candidate))) { response.writeHead(404); response.end("Not found"); return }
          response.writeHead(200, { "content-type": contentType(candidate) })
          createReadStream(candidate).pipe(response)
        } catch (error) { response.writeHead(500); response.end(String(error)) }
      })
      await new Promise((resolve, reject) => { server.once("error", reject); server.listen(0, "127.0.0.1", resolve) })
      const address = server.address()
      if (!address || typeof address === "string") throw new Error("Unable to determine asset server port")
      return { origin: `http://127.0.0.1:${address.port}`, close: () => new Promise((resolve, reject) => server.close((error) => error ? reject(error) : resolve())) }
    }

    async function resolveBuiltPage(siteDir, sourcePath) {
      const index = JSON.parse(await readFile(path.join(siteDir, "static", "contentIndex.json"), "utf8"))
      const relative = path.relative(path.join(repoRoot, "content"), sourcePath).split(path.sep).join("/")
      const entry = Object.values(index).find((candidate) => candidate.filePath === relative)
      if (!entry?.slug) throw new Error(`Quartz did not index publication rendition ${relative}`)
      return entry.slug
    }

    function normalizeSvg(svg) { return /xmlns=/.test(svg) ? svg : svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"') }
    function figureId(caption, fallback) {
      if (/Figure\s+8A\b/i.test(caption)) return "08a"
      if (/Figure\s+8B\b/i.test(caption)) return "08b"
      const match = /Figure\s+(\d+)/i.exec(caption)
      return match ? String(match[1]).padStart(2, "0") : String(fallback).padStart(2, "0")
    }

    export function validateFigureAssetIds(figures, { requireFigure8Split = false } = {}) {
      const ids = figures.map((figure) => figure.id)
      const unique = new Set(ids)
      if (unique.size !== ids.length) throw new Error(`Publication figure IDs are not unique: ${ids.join(", ")}`)
      if (requireFigure8Split) {
        if (ids.filter((id) => id === "08a").length !== 1 || ids.filter((id) => id === "08b").length !== 1 || ids.includes("08")) {
          throw new Error("Current publication assets require exactly one Figure 8A and one Figure 8B, with no unsplit Figure 8")
        }
      }
    }

    async function renderSvgToPng(browser, svg, width, outputPath) {
      const page = await browser.newPage({ viewport: { width: width + 80, height: 1200 } })
      try {
        await page.setContent(`<!doctype html><html><body style="margin:0;background:white"><div id="root" style="width:${width}px;padding:24px;box-sizing:border-box">${svg}</div><style>#root svg{display:block;width:100%!important;height:auto!important}</style></body></html>`, { waitUntil: "load" })
        await page.locator("#root").screenshot({ path: outputPath, omitBackground: false })
        const metadata = await sharp(outputPath).metadata()
        if (metadata.width !== width) throw new Error(`Rendered PNG ${path.basename(outputPath)} is ${metadata.width}px wide; expected ${width}px`)
        return metadata
      } finally { await page.close() }
    }

    function escapeXml(value) { return String(value ?? "").replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;").replaceAll('"', "&quot;") }

    async function writeCover(pathname, width, height, title, byline, label, profileName) {
      const { lines } = layoutCoverTitle(title, profileName)
      const titleSize = width >= 1900 ? 76 : 56
      const startY = Math.max(150, (height - lines.length * titleSize * 1.15) / 2)
      const tspans = lines.map((line, index) => `<tspan x="${Math.round(width * 0.08)}" dy="${index === 0 ? 0 : Math.round(titleSize * 1.15)}">${escapeXml(line)}</tspan>`).join("")
      const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${width}" height="${height}"><rect width="100%" height="100%" fill="#faf8f8"/><rect x="0" y="0" width="${Math.round(width * 0.018)}" height="100%" fill="#284b63"/><text x="${Math.round(width * 0.08)}" y="${Math.round(height * 0.16)}" font-family="Arial, sans-serif" font-size="${Math.round(titleSize * 0.34)}" font-weight="700" fill="#54736d" letter-spacing="2">${escapeXml(label.toUpperCase())}</text><text x="${Math.round(width * 0.08)}" y="${Math.round(startY)}" font-family="Arial, sans-serif" font-size="${titleSize}" font-weight="700" fill="#1f1f1f">${tspans}</text><text x="${Math.round(width * 0.08)}" y="${Math.round(height * 0.88)}" font-family="Arial, sans-serif" font-size="${Math.round(titleSize * 0.34)}" fill="#3f3f3f">${escapeXml(byline)}</text></svg>`
      await sharp(Buffer.from(svg)).png().toFile(pathname)
      const metadata = await sharp(pathname).metadata()
      if (metadata.width !== width || metadata.height !== height) throw new Error(`Cover ${path.basename(pathname)} did not render at ${width}×${height}`)
    }

    async function main() {
      const args = parseArgs(process.argv.slice(2))
      if (args.help) return usage()
      const source = await loadPublicationSource(args.source)
      const sourceCommit = process.env.UA_PDF_REPOSITORY_REF || process.env.GITHUB_SHA || (await new Promise((resolve, reject) => {
        const child = require("node:child_process").spawn("git", ["rev-parse", "HEAD"], { cwd: repoRoot, stdio: ["ignore", "pipe", "pipe"] })
        let stdout = ""; let stderr = ""; child.stdout.on("data", (chunk) => (stdout += chunk)); child.stderr.on("data", (chunk) => (stderr += chunk)); child.once("error", reject); child.once("exit", (code) => code === 0 ? resolve(stdout.trim()) : reject(new Error(stderr.trim())))
      }))
      const provenance = await determineSourceProvenance(source, sourceCommit, { allowDirtyPreview: args.allowDirtyPreview, repositoryRoot: repoRoot })
      const outputRoot = path.resolve(repoRoot, args.outputRoot)
      await assertSafeOutputPath(repoRoot, publicationOutputRoot, outputRoot)
      await rm(outputRoot, { recursive: true, force: true })
      const svgDir = path.join(outputRoot, "figures", "svg")
      const pngDir = path.join(outputRoot, "figures", "png")
      await mkdir(svgDir, { recursive: true }); await mkdir(pngDir, { recursive: true })

      const requireFigure8Split = source.relative === currentPublicationArticle
      const rendition = await buildPublicationRendition(source, { includeToc: false, splitDenseFigures: true, sourceCommit, provenance, requireFigure8Split })
      const tempRoot = await mkdtemp(path.join(os.tmpdir(), "ua-publication-assets-"))
      const siteDir = path.join(tempRoot, "site")
      let server; let browser
      try {
        await withTemporaryRendition(source, rendition.rendered, async (tempSourcePath) => {
          await run(process.execPath, [path.join(repoRoot, "quartz", "bootstrap-cli.mjs"), "build", "--output", siteDir], { cwd: repoRoot, env: { ...process.env, UA_INCLUDE_DRAFTS: "1" } })
          const slug = await resolveBuiltPage(siteDir, tempSourcePath)
          server = await startServer(siteDir)
          browser = await chromium.launch({ headless: true, executablePath: process.env.CHROME_PATH || undefined })
          const page = await browser.newPage({ viewport: { width: 1800, height: 1200 } })
          try {
            const url = `${server.origin}/${slug.split("/").map(encodeURIComponent).join("/")}`
            const response = await page.goto(url, { waitUntil: "networkidle" })
            if (!response?.ok()) throw new Error(`Publication asset page returned HTTP ${response?.status()}`)
            await page.waitForFunction(() => Array.from(document.querySelectorAll("code.mermaid")).every((node) => node.getAttribute("data-processed") === "true" && node.querySelector("svg")), undefined, { timeout: 30000 })
            await page.evaluate(async () => { if (document.fonts) await document.fonts.ready })
            const figures = await page.evaluate(() => Array.from(document.querySelectorAll("pre")).filter((pre) => pre.querySelector(":scope > code.mermaid svg")).map((pre, index) => ({ index: index + 1, svg: pre.querySelector(":scope > code.mermaid svg").outerHTML, caption: pre.nextElementSibling?.tagName === "P" ? pre.nextElementSibling.textContent.trim() : "" })))
            if (figures.length === 0) throw new Error("Publication rendition contains no Mermaid figures")
            const manifestFigures = []
            for (const figure of figures) {
              const id = figureId(figure.caption, figure.index)
              const normalized = normalizeSvg(figure.svg)
              const svgPath = path.join(svgDir, `figure-${id}.svg`); const pngPath = path.join(pngDir, `figure-${id}.png`)
              const width = 1800
              await writeFile(svgPath, normalized, "utf8")
              const metadata = await renderSvgToPng(browser, normalized, width, pngPath)
              manifestFigures.push({ id, caption: figure.caption, svg: path.relative(repoRoot, svgPath).split(path.sep).join("/"), png: path.relative(repoRoot, pngPath).split(path.sep).join("/"), width: metadata.width, height: metadata.height })
            }
            if (rendition.figure8Split) {
              for (const figure of [
                { id: "08a", caption: "Figure 8A — Decision-ownership model.", svg: buildFigure8DecisionSvg(), width: 3200 },
                { id: "08b", caption: "Figure 8B — Capability-family axis and orthogonality relationship.", svg: buildFigure8CapabilitySvg(), width: 2400 },
              ]) {
                const svgPath = path.join(svgDir, `figure-${figure.id}.svg`); const pngPath = path.join(pngDir, `figure-${figure.id}.png`)
                await writeFile(svgPath, figure.svg, "utf8")
                const metadata = await renderSvgToPng(browser, figure.svg, figure.width, pngPath)
                manifestFigures.push({ id: figure.id, caption: figure.caption, svg: path.relative(repoRoot, svgPath).split(path.sep).join("/"), png: path.relative(repoRoot, pngPath).split(path.sep).join("/"), width: metadata.width, height: metadata.height })
              }
            }
            validateFigureAssetIds(manifestFigures, { requireFigure8Split })
            const title = source.data.title || "Untitled publication"
            const authors = normalizeAuthors(source.data.authors ?? source.data.author)
            const byline = authors.length > 0 ? `${authors.join(", ")} · Uncertainty Architecture` : "Uncertainty Architecture"
            await writeCover(path.join(outputRoot, "cover-linkedin-article.png"), 2000, 600, title, byline, "LinkedIn article", "LinkedIn article")
            await writeCover(path.join(outputRoot, "social-preview.png"), 1200, 627, title, byline, "Thinking Systems", "social preview")
            await writeCover(path.join(outputRoot, "medium-hero.png"), 1600, 900, title, byline, "Medium", "Medium hero")
            const assetManifest = {
              schema_version: 1, artifact: "publication-assets", source_path: source.relative, source_commit: sourceCommit,
              source_state: provenance.state, source_git_blob_sha: provenance.committedBlob, source_working_blob_sha: provenance.workingBlob,
              source_sha256: sha256(Buffer.from(source.raw)), generated_at: new Date().toISOString(), canonical_url: source.data.canonical_url || null,
              additional_publication_urls: Array.isArray(source.data.additional_publication_urls) ? source.data.additional_publication_urls : [],
              figure_8_split_for_readability: rendition.figure8Split, figures: manifestFigures,
              covers: {
                linkedin_article: { path: path.relative(repoRoot, path.join(outputRoot, "cover-linkedin-article.png")).split(path.sep).join("/"), width: 2000, height: 600 },
                social_preview: { path: path.relative(repoRoot, path.join(outputRoot, "social-preview.png")).split(path.sep).join("/"), width: 1200, height: 627 },
                medium_hero: { path: path.relative(repoRoot, path.join(outputRoot, "medium-hero.png")).split(path.sep).join("/"), width: 1600, height: 900 },
              },
            }
            const manifestPath = path.join(outputRoot, "assets.manifest.json")
            await assertSafeOutputPath(repoRoot, publicationOutputRoot, manifestPath)
            await atomicWriteFile(manifestPath, `${JSON.stringify(assetManifest, null, 2)}\n`, { encoding: "utf8", forbiddenPaths: [source.absolute] })
          } finally { await page.close() }
        })
      } finally {
        if (browser) await browser.close(); if (server) await server.close(); await rm(tempRoot, { recursive: true, force: true })
      }
      console.log(`Publication assets ready: ${path.relative(repoRoot, outputRoot)} (source ${provenance.state})`)
    }

    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) main().catch((error) => { console.error(`Publication asset rendering failed: ${error instanceof Error ? error.message : String(error)}`); process.exitCode = 1 })
    ''',
)
assets = (ROOT / "quartz/scripts/render-publication-assets.mjs").read_text(encoding="utf-8")
assets = assets.replace('import { fileURLToPath } from "node:url"\n', 'import { fileURLToPath } from "node:url"\nimport { spawn } from "node:child_process"\n')
assets = assets.replace('const child = require("node:child_process").spawn("git", ["rev-parse", "HEAD"],', 'const child = spawn("git", ["rev-parse", "HEAD"],')
write("quartz/scripts/render-publication-assets.mjs", assets)

# ---------------------------------------------------------------------------
# Public command wrappers: safety is defense-in-depth, core renderers also check.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/run-pdf-export.mjs",
    r'''
    #!/usr/bin/env node
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import { assertSafeOutputPath } from "./publication-path-safety.mjs"
    import { contentRoot, repoRoot, run } from "./publication-rendition.mjs"

    function parseArgs(argv) {
      let source; let output
      for (let i = 0; i < argv.length; i += 1) {
        const value = argv[i]
        if (value === "--output" || value === "-o") output = argv[++i]
        else if (value === "--help" || value === "-h") return { help: true }
        else if (value.startsWith("-")) throw new Error(`Unknown option: ${value}`)
        else if (!source) source = value
        else throw new Error(`Unexpected argument: ${value}`)
      }
      return { source, output, help: false }
    }

    async function main() {
      const args = parseArgs(process.argv.slice(2))
      if (args.help || !args.source) { console.log("Usage: npm run pdf -- <content/file.md> [--output dist/pdf/file.pdf]"); if (!args.help) process.exitCode = 1; return }
      const source = path.resolve(repoRoot, args.source)
      const pdfRoot = path.join(repoRoot, "dist", "pdf")
      const output = args.output ? path.resolve(repoRoot, args.output) : path.join(pdfRoot, path.relative(contentRoot, source).replace(/\.md$/i, ".pdf"))
      await assertSafeOutputPath(repoRoot, pdfRoot, output)
      await run(process.execPath, [path.join(repoRoot, "quartz", "scripts", "export-pdf.mjs"), ...process.argv.slice(2)], { cwd: repoRoot })
    }
    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) main().catch((error) => { console.error(`PDF export preflight failed: ${error.message}`); process.exitCode = 1 })
    ''',
)

write(
    "quartz/scripts/run-publication-assets.mjs",
    r'''
    #!/usr/bin/env node
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import { assertCoverTitleFits } from "./publication-cover.mjs"
    import { assertSafeOutputPath } from "./publication-path-safety.mjs"
    import { loadPublicationSource, repoRoot, run } from "./publication-rendition.mjs"

    const defaultSource = "content/research/notes/thinking-systems-publication-draft.md"
    const defaultOutputRoot = "dist/publication/thinking-systems"
    function parseArgs(argv) {
      let source = defaultSource; let outputRoot = defaultOutputRoot; let allowDirtyPreview = false
      for (let i = 0; i < argv.length; i += 1) {
        const value = argv[i]
        if (value === "--source") source = argv[++i]
        else if (value === "--output-root") outputRoot = argv[++i]
        else if (value === "--allow-dirty-preview") allowDirtyPreview = true
        else if (value === "--help" || value === "-h") return { help: true }
        else if (!value.startsWith("-") && source === defaultSource) source = value
        else throw new Error(`Unknown argument: ${value}`)
      }
      return { source, outputRoot, allowDirtyPreview, help: false }
    }
    async function main() {
      const args = parseArgs(process.argv.slice(2))
      if (args.help) { console.log("Usage: npm run publication:assets -- [source.md] [--output-root dist/publication/name] [--allow-dirty-preview]"); return }
      const source = await loadPublicationSource(args.source); assertCoverTitleFits(source.data.title || "Untitled publication")
      const publicationRoot = path.join(repoRoot, "dist", "publication"); const outputRoot = path.resolve(repoRoot, args.outputRoot)
      await assertSafeOutputPath(repoRoot, publicationRoot, outputRoot)
      const childArgs = [path.join(repoRoot, "quartz", "scripts", "render-publication-assets.mjs"), args.source, "--output-root", args.outputRoot]
      if (args.allowDirtyPreview) childArgs.push("--allow-dirty-preview")
      await run(process.execPath, childArgs, { cwd: repoRoot })
    }
    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) main().catch((error) => { console.error(`Publication asset preflight failed: ${error.message}`); process.exitCode = 1 })
    ''',
)

write(
    "quartz/scripts/run-publication-verify.mjs",
    r'''
    #!/usr/bin/env node
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import { assertSafeOutputPath } from "./publication-path-safety.mjs"
    import { repoRoot, run } from "./publication-rendition.mjs"
    function parseArgs(argv) {
      if (argv.length === 0 || argv.includes("--help") || argv.includes("-h")) return { help: true }
      const pdf = argv[0]; let outputDir
      for (let i = 1; i < argv.length; i += 1) { if (argv[i] === "--output-dir") outputDir = argv[++i]; else throw new Error(`Unknown argument: ${argv[i]}`) }
      return { pdf, outputDir, help: false }
    }
    async function main() {
      const args = parseArgs(process.argv.slice(2)); if (args.help) { console.log("Usage: npm run pdf:verify -- dist/pdf/file.pdf [--output-dir dist/pdf/visual/file]"); return }
      const pdfRoot = path.join(repoRoot, "dist", "pdf"); const pdfPath = path.resolve(repoRoot, args.pdf)
      const visualRoot = path.join(pdfRoot, "visual"); const stem = path.basename(pdfPath, path.extname(pdfPath)); const outputDir = path.resolve(repoRoot, args.outputDir || path.join(visualRoot, stem))
      await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath); await assertSafeOutputPath(repoRoot, visualRoot, outputDir)
      await run(process.execPath, [path.join(repoRoot, "quartz", "scripts", "verify-publication-pdf.mjs"), ...process.argv.slice(2)], { cwd: repoRoot })
    }
    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) main().catch((error) => { console.error(`PDF verification preflight failed: ${error.message}`); process.exitCode = 1 })
    ''',
)

# ---------------------------------------------------------------------------
# Patch generic exporter and verifier so direct invocation cannot bypass safety.
# ---------------------------------------------------------------------------
exporter_path = ROOT / "quartz/scripts/export-pdf.mjs"
exporter = exporter_path.read_text(encoding="utf-8")
if 'from "./publication-path-safety.mjs"' not in exporter:
    marker = 'import { chromium } from "playwright";\n'
    exporter = replace_once(exporter, marker, marker + 'import { assertSafeOutputPath } from "./publication-path-safety.mjs";\n', "exporter safety import")
needle = '  if (!isInside(allowedOutputRoot, resolvedOutput)) {\n    throw new Error("The PDF output must be under dist/pdf/");\n  }\n\n'
replacement = needle + '  await assertSafeOutputPath(options.trustedRoot ?? repoRoot, allowedOutputRoot, resolvedOutput);\n\n'
if 'await assertSafeOutputPath(options.trustedRoot ?? repoRoot' not in exporter:
    exporter = replace_once(exporter, needle, replacement, "exporter core path safety")
write("quartz/scripts/export-pdf.mjs", exporter)

exporter_test_path = ROOT / "quartz/scripts/export-pdf.test.mjs"
exporter_test = exporter_test_path.read_text(encoding="utf-8")
exporter_test = exporter_test.replace('{ outputRoot: directory }', '{ outputRoot: directory, trustedRoot: directory }')
exporter_test = exporter_test.replace('outputRoot: directory,\n    })', 'outputRoot: directory,\n      trustedRoot: directory,\n    })')
write("quartz/scripts/export-pdf.test.mjs", exporter_test)

verify_path = ROOT / "quartz/scripts/verify-publication-pdf.mjs"
verify = verify_path.read_text(encoding="utf-8")
if 'from "./publication-path-safety.mjs"' not in verify:
    marker = 'import { fileURLToPath } from "node:url"\n'
    verify = replace_once(verify, marker, marker + 'import { assertSafeOutputPath } from "./publication-path-safety.mjs"\n', "verifier safety import")
# Insert after outputDir declaration, before any recursive removal.
if 'await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath)' not in verify:
    main_marker = '  await rm(outputDir, { recursive: true, force: true })'
    if main_marker not in verify:
        raise RuntimeError("verifier output cleanup marker not found")
    declarations = '  const pdfRoot = path.join(repoRoot, "dist", "pdf")\n  const visualRoot = path.join(pdfRoot, "visual")\n  await assertSafeOutputPath(repoRoot, pdfRoot, pdfPath)\n  await assertSafeOutputPath(repoRoot, visualRoot, outputDir)\n'
    verify = verify.replace(main_marker, declarations + main_marker, 1)
write("quartz/scripts/verify-publication-pdf.mjs", verify)

# ---------------------------------------------------------------------------
# Regression tests for the actual blockers.
# ---------------------------------------------------------------------------
write(
    "quartz/scripts/publication-safety.test.mjs",
    r'''
    import assert from "node:assert/strict"
    import { execFile } from "node:child_process"
    import { link, mkdir, mkdtemp, readFile, rm, symlink, writeFile } from "node:fs/promises"
    import os from "node:os"
    import path from "node:path"
    import test from "node:test"
    import { promisify } from "node:util"

    import { assertCoverTitleFits } from "./publication-cover.mjs"
    import { assertSafeOutputPath, atomicWriteFile } from "./publication-path-safety.mjs"
    import { determineSourceProvenance } from "./publication-provenance.mjs"
    import { buildPublicationRendition, currentPublicationArticle } from "./publication-rendition.mjs"
    import { validateFigureAssetIds } from "./render-publication-assets.mjs"

    const exec = promisify(execFile)
    async function temporary(t) { const directory = await mkdtemp(path.join(os.tmpdir(), "ua-publication-safety-")); t.after(() => rm(directory, { recursive: true, force: true })); return directory }

    test("symlinked allowed output root is rejected", async (t) => {
      const trusted = await temporary(t); const outside = await temporary(t)
      await symlink(outside, path.join(trusted, "dist"))
      await assert.rejects(assertSafeOutputPath(trusted, path.join(trusted, "dist", "pdf"), path.join(trusted, "dist", "pdf", "paper.pdf")), /symbolic-link component/)
    })

    test("nested symlink output parent is rejected", async (t) => {
      const trusted = await temporary(t); const outside = await temporary(t); const root = path.join(trusted, "dist", "pdf")
      await mkdir(root, { recursive: true }); await symlink(outside, path.join(root, "alias"))
      await assert.rejects(assertSafeOutputPath(trusted, root, path.join(root, "alias", "paper.pdf")), /symbolic-link component/)
    })

    test("atomic generated write rejects manifest symlink and hardlink aliases to Markdown", async (t) => {
      const directory = await temporary(t); const source = path.join(directory, "source.md"); await writeFile(source, "# Canonical\n")
      const symbolic = path.join(directory, "symbolic.manifest.json"); const hard = path.join(directory, "hard.manifest.json")
      await symlink(source, symbolic); await link(source, hard)
      await assert.rejects(atomicWriteFile(symbolic, "{}", { forbiddenPaths: [source], encoding: "utf8" }), /symbolic link/)
      await assert.rejects(atomicWriteFile(hard, "{}", { forbiddenPaths: [source], encoding: "utf8" }), /aliases protected source/)
      assert.equal(await readFile(source, "utf8"), "# Canonical\n")
    })

    test("atomic manifest failure preserves previous manifest", async (t) => {
      const directory = await temporary(t); const destination = path.join(directory, "paper.manifest.json"); await writeFile(destination, "previous")
      await assert.rejects(atomicWriteFile(destination, "next", { encoding: "utf8", renameImpl: async () => { throw new Error("injected rename failure") } }), /injected rename failure/)
      assert.equal(await readFile(destination, "utf8"), "previous")
    })

    test("strict provenance rejects modified tracked source and explicit preview records both blobs", async (t) => {
      const repository = await temporary(t); await exec("git", ["init"], { cwd: repository }); await exec("git", ["config", "user.email", "test@example.com"], { cwd: repository }); await exec("git", ["config", "user.name", "Test"], { cwd: repository })
      const content = path.join(repository, "content"); await mkdir(content); const sourcePath = path.join(content, "paper.md"); await writeFile(sourcePath, "# committed\n")
      await exec("git", ["add", "."], { cwd: repository }); await exec("git", ["commit", "-m", "source"], { cwd: repository }); const { stdout } = await exec("git", ["rev-parse", "HEAD"], { cwd: repository }); const commit = stdout.trim()
      await writeFile(sourcePath, "# modified\n")
      const source = { absolute: sourcePath, relative: "content/paper.md" }
      await assert.rejects(determineSourceProvenance(source, commit, { repositoryRoot: repository }), /do not match/)
      const preview = await determineSourceProvenance(source, commit, { repositoryRoot: repository, allowDirtyPreview: true })
      assert.equal(preview.state, "dirty-preview"); assert.notEqual(preview.workingBlob, preview.committedBlob)
    })

    test("dirty preview title page is visibly non-versioned", async () => {
      const source = { relative: "content/preview.md", raw: "---\ntitle: Preview\n---\n# Preview\n", data: { title: "Preview" }, content: "# Preview\n" }
      const result = await buildPublicationRendition(source, { sourceCommit: "1234567890abcdef", provenance: { state: "dirty-preview", workingBlob: "abcdef1234567890" } })
      assert.match(result.rendered, /Uncommitted local preview/); assert.match(result.rendered, /Declared base source \(preview differs\)/); assert.doesNotMatch(result.rendered, />Versioned source</)
    })

    test("current publication fails closed when Figure 8 split is not recognized", async () => {
      const source = { relative: currentPublicationArticle, raw: "# Article\n", data: { title: "Article" }, content: "# Article\n" }
      await assert.rejects(buildPublicationRendition(source, { sourceCommit: "abc", provenance: { state: "committed" }, requireFigure8Split: true }), /requires the reviewed Figure 8A\/8B rendition/)
    })

    test("asset Figure 8 contract requires unique 8A and 8B panels", () => {
      assert.doesNotThrow(() => validateFigureAssetIds([{ id: "01" }, { id: "08a" }, { id: "08b" }], { requireFigure8Split: true }))
      assert.throws(() => validateFigureAssetIds([{ id: "08a" }, { id: "08a" }, { id: "08b" }], { requireFigure8Split: true }), /not unique/)
      assert.throws(() => validateFigureAssetIds([{ id: "08" }, { id: "08a" }, { id: "08b" }], { requireFigure8Split: true }), /no unsplit Figure 8/)
    })

    test("cover preflight rejects overflow and unbreakable titles instead of truncating", () => {
      assert.throws(() => assertCoverTitleFits("This deliberately overlong publication title contains far too many words to fit inside three lines across all configured platform cover surfaces without truncation or an explicit redesign"), /cover title requires/)
      assert.throws(() => assertCoverTitleFits("X".repeat(200)), /unbreakable token/)
    })
    ''',
)

# Patch existing rendition tests to import provenance from the owning helper if needed.
rendition_test = (ROOT / "quartz/scripts/publication-rendition.test.mjs").read_text(encoding="utf-8")
rendition_test = rendition_test.replace(
    'import {\n  countPdfPages,\n  determineSourceProvenance,\n  finalizePublicationPdf,\n} from "./render-publication-pdf.mjs"',
    'import { countPdfPages, finalizePublicationPdf } from "./render-publication-pdf.mjs"\nimport { determineSourceProvenance } from "./publication-provenance.mjs"',
)
write("quartz/scripts/publication-rendition.test.mjs", rendition_test)

# ---------------------------------------------------------------------------
# Package scripts, CI, and manual workflow.
# ---------------------------------------------------------------------------
package_path = ROOT / "package.json"
package = json.loads(package_path.read_text(encoding="utf-8"))
package["scripts"]["pdf"] = "node quartz/scripts/run-pdf-export.mjs"
package["scripts"]["pdf:article"] = "node quartz/scripts/render-publication-pdf.mjs content/research/notes/thinking-systems-publication-draft.md --output dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf"
package["scripts"]["pdf:working-paper"] = "node quartz/scripts/render-publication-pdf.mjs content/research/notes/open-engineering-specification-article-draft.md --output dist/pdf/uncertainty-architecture-thinking-systems-working-paper.pdf --no-split-dense"
package["scripts"]["pdf:verify"] = "node quartz/scripts/run-publication-verify.mjs"
package["scripts"]["publication:assets"] = "node quartz/scripts/run-publication-assets.mjs"
package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

write(
    ".github/workflows/build-integrity.yml",
    r'''
    name: Build integrity

    on:
      pull_request:
      push:
        branches:
          - main
      workflow_dispatch:

    permissions:
      contents: read

    concurrency:
      group: build-integrity-${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    jobs:
      quartz-build:
        name: Build / Quartz production site
        runs-on: ubuntu-24.04
        timeout-minutes: 15
        steps:
          - name: Check out repository
            uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
            with:
              persist-credentials: false
          - name: Set up Node.js
            uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
            with:
              node-version: '22'
              cache: npm
              package-manager-cache: false
          - name: Install locked dependencies
            run: npm ci --ignore-scripts
          - name: PDF export / regression tests
            run: node --test quartz/scripts/export-pdf.test.mjs quartz/scripts/publication-rendition.test.mjs quartz/scripts/publication-safety.test.mjs
          - name: Build Quartz site
            run: npm run build

      publication-render:
        name: Publication / current article render
        runs-on: ubuntu-24.04
        timeout-minutes: 35
        steps:
          - name: Check out repository
            uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
            with:
              fetch-depth: 0
              persist-credentials: false
          - name: Set up Node.js
            uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
            with:
              node-version: '22'
              cache: npm
              package-manager-cache: false
          - name: Install locked dependencies
            run: npm ci --ignore-scripts
          - name: Install Chromium and PDF inspection tools
            shell: bash
            run: |
              ./node_modules/.bin/playwright install --with-deps chromium
              sudo apt-get update
              sudo apt-get install -y poppler-utils
          - name: Render current publication PDF
            env:
              UA_PDF_REPOSITORY_REF: ${{ github.sha }}
            run: npm run pdf:article
          - name: Visual verify current publication PDF
            run: npm run pdf:verify -- dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf
          - name: Render current publication assets
            env:
              UA_PDF_REPOSITORY_REF: ${{ github.sha }}
            run: npm run publication:assets
          - name: Render living working paper PDF
            env:
              UA_PDF_REPOSITORY_REF: ${{ github.sha }}
            run: npm run pdf:working-paper
          - name: Visual verify living working paper PDF
            run: npm run pdf:verify -- dist/pdf/uncertainty-architecture-thinking-systems-working-paper.pdf
          - name: Upload publication validation artifact
            uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
            with:
              name: publication-render-validation
              path: |
                dist/pdf/*.pdf
                dist/pdf/*.manifest.json
                dist/pdf/visual/**
                dist/publication/thinking-systems/**
              if-no-files-found: error
              retention-days: 14

      mermaid-render:
        name: Content / render Mermaid diagrams
        runs-on: ubuntu-24.04
        timeout-minutes: 20
        steps:
          - name: Check out repository
            uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
            with:
              persist-credentials: false
          - name: Set up Node.js
            uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
            with:
              node-version: '22'
              package-manager-cache: false
          - name: Render every maintained Mermaid block
            run: python3 .github/scripts/validate_mermaid.py

      workflow-policy:
        name: Supply chain / workflows and pins
        runs-on: ubuntu-24.04
        timeout-minutes: 10
        steps:
          - name: Check out repository
            uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
            with:
              persist-credentials: false
          - name: Validate immutable action and container references
            run: python3 .github/scripts/validate_workflow_supply_chain.py
          - name: Run supply-chain regression fixtures
            run: python3 .github/tests/supply_chain/test_supply_chain.py
          - name: Install actionlint
            env:
              ACTIONLINT_VERSION: '1.7.12'
            run: go install "github.com/rhysd/actionlint/cmd/actionlint@v${ACTIONLINT_VERSION}"
          - name: Run actionlint
            run: '"$(go env GOPATH)/bin/actionlint"'
          - name: Install zizmor
            run: pipx install zizmor==1.26.0
          - name: Run zizmor
            env:
              GH_TOKEN: ${{ github.token }}
            run: zizmor --pedantic .github/workflows
    ''',
)

write(
    ".github/workflows/export-research-pdf.yml",
    r'''
    name: Export research PDF

    on:
      workflow_dispatch:
        inputs:
          source:
            description: Markdown source under content/
            required: true
            default: content/research/notes/thinking-systems-publication-draft.md
            type: string

    permissions:
      contents: read

    concurrency:
      group: export-research-pdf-${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    jobs:
      export:
        name: Render Markdown publication
        runs-on: ubuntu-24.04
        timeout-minutes: 30
        steps:
          - name: Check out repository
            uses: actions/checkout@de0fac2e4500dabe0009e67214ff5f5447ce83dd # v6.0.2
            with:
              fetch-depth: 0
              persist-credentials: false
          - name: Set up Node.js
            uses: actions/setup-node@48b55a011bda9f5d6aeb4c2d9c7362e8dae4041e # v6.4.0
            with:
              node-version: '22'
              cache: npm
              package-manager-cache: false
          - name: Install locked dependencies
            run: npm ci --ignore-scripts
          - name: Install Chromium and PDF inspection tools
            shell: bash
            run: |
              ./node_modules/.bin/playwright install --with-deps chromium
              sudo apt-get update
              sudo apt-get install -y poppler-utils
          - name: Render requested publication
            env:
              UA_PDF_SOURCE: ${{ inputs.source || 'content/research/notes/thinking-systems-publication-draft.md' }}
              UA_PUBLICATION_ARTICLE_SOURCE: content/research/notes/thinking-systems-publication-draft.md
              UA_WORKING_PAPER_SOURCE: content/research/notes/open-engineering-specification-article-draft.md
              UA_PDF_REPOSITORY_REF: ${{ github.sha }}
            shell: bash
            run: |
              set -euo pipefail
              if [[ "$UA_PDF_SOURCE" == "$UA_PUBLICATION_ARTICLE_SOURCE" ]]; then
                npm run pdf:article
                npm run publication:assets
                pdf_path="dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf"
              elif [[ "$UA_PDF_SOURCE" == "$UA_WORKING_PAPER_SOURCE" ]]; then
                npm run pdf:working-paper
                pdf_path="dist/pdf/uncertainty-architecture-thinking-systems-working-paper.pdf"
              else
                stem="$(basename "$UA_PDF_SOURCE" .md)"
                pdf_path="dist/pdf/${stem}.pdf"
                node quartz/scripts/render-publication-pdf.mjs "$UA_PDF_SOURCE" --output "$pdf_path" --no-split-dense
              fi
              npm run pdf:verify -- "$pdf_path"
          - name: Upload publication artifact
            uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
            with:
              name: research-publication
              path: |
                dist/pdf/*.pdf
                dist/pdf/*.manifest.json
                dist/pdf/visual/**
                dist/publication/thinking-systems/**
              if-no-files-found: error
              retention-days: 14
    ''',
)

# ---------------------------------------------------------------------------
# Repository contract: protect every control-bearing helper and the CI ref mode.
# ---------------------------------------------------------------------------
contract_path = ROOT / ".github/policy/repository-contract-change-coupling.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))
required = {entry["path"] for entry in contract["required_paths"]}
for path in [
    "quartz/scripts/publication-path-safety.mjs",
    "quartz/scripts/publication-provenance.mjs",
    "quartz/scripts/publication-cover.mjs",
    "quartz/scripts/publication-figure8-fingerprint.mjs",
    "quartz/scripts/run-pdf-export.mjs",
    "quartz/scripts/run-publication-assets.mjs",
    "quartz/scripts/run-publication-verify.mjs",
    "quartz/scripts/publication-safety.test.mjs",
]:
    if path not in required:
        contract["required_paths"].append({"path": path, "type": "file"})
critical_by_path = {entry["path"]: entry for entry in contract["critical_files"]}
critical_by_path[".github/workflows/build-integrity.yml"]["required_text"].extend(
    text for text in ["fetch-depth: 0", "UA_PDF_REPOSITORY_REF: ${{ github.sha }}", "publication-safety.test.mjs"]
    if text not in critical_by_path[".github/workflows/build-integrity.yml"]["required_text"]
)
for path, texts in {
    "quartz/scripts/publication-path-safety.mjs": ["assertSafeOutputPath", "assertNoPathAliases", "atomicWriteFile", "symbolic-link component"],
    "quartz/scripts/publication-provenance.mjs": ["determineSourceProvenance", "dirty-preview", "source bytes do not match"],
    "quartz/scripts/publication-cover.mjs": ["assertCoverTitleFits", "unbreakable token", "without truncation"],
    "quartz/scripts/publication-figure8-fingerprint.mjs": ["canonicalFigure8Fingerprint", "requires substantive review"],
    "quartz/scripts/run-pdf-export.mjs": ["assertSafeOutputPath", "export-pdf.mjs"],
    "quartz/scripts/run-publication-assets.mjs": ["assertCoverTitleFits", "assertSafeOutputPath", "--allow-dirty-preview"],
    "quartz/scripts/run-publication-verify.mjs": ["assertSafeOutputPath", "verify-publication-pdf.mjs"],
}.items():
    existing = critical_by_path.get(path)
    if existing:
        for text in texts:
            if text not in existing["required_text"]: existing["required_text"].append(text)
    else:
        entry = {"path": path, "required_text": texts}
        contract["critical_files"].append(entry)
        critical_by_path[path] = entry
contract_path.write_text(json.dumps(contract, indent=2) + "\n", encoding="utf-8")

cases_path = ROOT / ".github/tests/repository_contract/cases.json"
manifest = json.loads(cases_path.read_text(encoding="utf-8"))
cases = manifest["cases"] if isinstance(manifest, dict) else manifest
new_cases = [
    {"name": "publication path safety helper deletion is rejected", "mutation": {"type": "delete_path", "path": "quartz/scripts/publication-path-safety.mjs"}, "expected_error": "Missing required file: quartz/scripts/publication-path-safety.mjs"},
    {"name": "publication provenance helper deletion is rejected", "mutation": {"type": "delete_path", "path": "quartz/scripts/publication-provenance.mjs"}, "expected_error": "Missing required file: quartz/scripts/publication-provenance.mjs"},
    {"name": "Figure 8 fingerprint helper deletion is rejected", "mutation": {"type": "delete_path", "path": "quartz/scripts/publication-figure8-fingerprint.mjs"}, "expected_error": "Missing required file: quartz/scripts/publication-figure8-fingerprint.mjs"},
    {"name": "publication full-history checkout deletion is rejected", "mutation": {"type": "remove_text", "path": ".github/workflows/build-integrity.yml", "text": "fetch-depth: 0"}, "expected_error": ".github/workflows/build-integrity.yml: missing protected text 'fetch-depth: 0'"},
    {"name": "publication integration provenance ref deletion is rejected", "mutation": {"type": "remove_text", "path": ".github/workflows/build-integrity.yml", "text": "UA_PDF_REPOSITORY_REF: ${{ github.sha }}"}, "expected_error": ".github/workflows/build-integrity.yml: missing protected text 'UA_PDF_REPOSITORY_REF: ${{ github.sha }}'"},
]
existing_names = {case["name"] for case in cases}
for case in new_cases:
    if case["name"] not in existing_names: cases.append(case)
if isinstance(manifest, dict): manifest["cases"] = cases
else: manifest = cases
cases_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

test_contract_path = ROOT / ".github/tests/repository_contract/test_repository_contract.py"
test_contract = test_contract_path.read_text(encoding="utf-8")
marker = '    "manual publication export workflow deletion is rejected",\n'
if marker not in test_contract:
    raise RuntimeError("repository contract required-case insertion point missing")
insert = "".join(f'    "{case["name"]}",\n' for case in new_cases)
for case in new_cases:
    if f'"{case["name"]}"' in test_contract:
        insert = insert.replace(f'    "{case["name"]}",\n', "")
test_contract = test_contract.replace(marker, marker + insert, 1)
test_contract_path.write_text(test_contract, encoding="utf-8")

# Documentation: record strict provenance and fail-closed safety.
pdf_doc_path = ROOT / "quartz/PDF-EXPORT.md"
pdf_doc = pdf_doc_path.read_text(encoding="utf-8")
if "Strict provenance" not in pdf_doc:
    pdf_doc += textwrap.dedent(r'''

    ## Strict provenance and preview mode

    Curated PDFs and platform assets are versioned outputs by default. The source bytes must match the declared Git commit. A local uncommitted rendition requires the explicit `--allow-dirty-preview` option; its title page and manifest identify it as a non-versioned preview and record both committed and working-tree blob identities.

    Generated PDF, manifest, visual-verification, and platform-asset paths are anchored to the real repository root. Symlinked output roots or parents, aliases to canonical Markdown, and destinations outside the named `dist/` roots are rejected. Current-article publication fails closed when the reviewed Figure 8A/8B rendition cannot be recognized or no longer matches its reviewed fingerprint.
    ''')
pdf_doc_path.write_text(pdf_doc, encoding="utf-8")

# Ensure source Markdown remains byte-identical to main.
for source_path in [
    "content/research/notes/thinking-systems-publication-draft.md",
    "content/research/notes/open-engineering-specification-article-draft.md",
]:
    run("git", "diff", "--exit-code", "origin/main", "--", source_path)

# Locked install and fast validation before publishing the reconstructed branch.
print("Installing locked dependencies and running deterministic validation...")
run("npm", "ci", "--ignore-scripts")
run("node", "--test", "quartz/scripts/export-pdf.test.mjs", "quartz/scripts/publication-rendition.test.mjs", "quartz/scripts/publication-safety.test.mjs")
run("npm", "run", "build")
run("python3", ".github/tests/repository_contract/test_repository_contract.py")
run("python3", ".github/scripts/validate_workflow_supply_chain.py")

# Final clean commit based directly on current main. Temporary reconstruction
# helpers/workflows disappear because they were never reintroduced after reset.
run("git", "add", "-A")
status = run("git", "status", "--short", capture=True).stdout
print(status)
if not status.strip():
    raise RuntimeError("Reconstruction produced no diff")
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "commit", "-m", "Add universal Quartz publication export infrastructure")
run("git", "push", "--force-with-lease", "origin", f"HEAD:{BRANCH}")
print("PR #79 reconstructed cleanly and force-pushed.")
