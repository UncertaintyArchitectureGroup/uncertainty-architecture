#!/usr/bin/env python3
from __future__ import annotations

import json
import textwrap
from pathlib import Path

ROOT = Path.cwd()


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(textwrap.dedent(content).lstrip("\n"), encoding="utf-8")


def write_json(path: str, value: object) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


profile = {
    "schema_version": 1,
    "publication_id": "thinking-systems",
    "source": "content/research/notes/thinking-systems-publication-draft.md",
    "output_root": "dist/publication/thinking-systems",
    "launch_post_source": "content/research/notes/thinking-systems-linkedin-launch-post.md",
    "repository": "UncertaintyArchitectureGroup/uncertainty-architecture",
    "medium": {
        "title": "Thinking Systems: When the Controlled Object Changes",
        "subtitle": "Why probabilistic Model Judgment changes the engineering object — and why software architecture alone may no longer be enough.",
        "publication_note": "This is a publication-facing adaptation of a living Uncertainty Architecture working paper. The long-form manuscript remains under development, and criticism of this bounded argument may still change the larger research.",
        "closing_note": "The complete Uncertainty Architecture repository, the living working paper, and the open validation agenda are linked below. Contradictory cases and simpler competing approaches are welcome.",
        "image_min_width": 1192,
        "image_max_bytes": 26214400,
        "hero": {"file": "medium-hero.png", "width": 1600, "height": 900},
        "canonical_required_before_publish": True,
    },
    "linkedin": {
        "title": "Thinking Systems: When the Controlled Object Changes",
        "subtitle": "Why probabilistic Model Judgment changes the engineering object — and why control becomes socio-technical.",
        "publication_note": "This article is a bounded publication adaptation of a living Uncertainty Architecture working paper. It preserves the current argument while the larger manuscript remains open to criticism and revision.",
        "closing_note": "Uncertainty Architecture is open source and under validation. Apply the map to a real system, show where it breaks, or point to an existing approach that solves the problem more simply.",
        "article_max_characters": 125000,
        "post_max_characters": 3000,
        "post_target_max_characters": 2900,
        "seo_title": "Thinking Systems: When the Controlled Object Changes",
        "seo_title_max_characters": 60,
        "seo_description": "Why probabilistic Model Judgment changes the engineering object—and why bounded control must span software, delivery, humans, and organizational authority.",
        "seo_description_min_characters": 140,
        "seo_description_max_characters": 160,
        "cover": {"file": "cover-linkedin-article.png", "width": 2000, "height": 600, "max_bytes": 10485760},
        "social_preview": {"file": "social-preview.png", "width": 1200, "height": 627},
        "mentions": ["Arkadiy Dobkin", "Christophe Kolb", "Maxi Armesto", "Jan"],
    },
    "resources": [
        {"label": "Uncertainty Architecture repository", "path": ""},
        {"label": "Standalone repository article source", "path": "content/research/notes/thinking-systems-publication-draft.md"},
        {"label": "Living long-form working paper", "path": "content/research/notes/open-engineering-specification-article-draft.md"},
    ],
    "figures": {
        "01": {"alt": "Four connected boxes show plan-driven engineering, iterative delivery, modern operations, and Thinking-System engineering as responses to uncertainty moving closer to runtime and into the controlled object."},
        "02": {"alt": "A decision tree asks whether any Consequential Runtime Responsibility depends partly on probabilistic Model Judgment; orchestration topology, autonomy, and delegated authority are shown as independent dimensions."},
        "03": {"alt": "Side-by-side responsibility structures compare explicitly authored consequential behavior with a Thinking System that combines deterministic responsibilities and one or more probabilistic Judgment Nodes."},
        "04": {"alt": "Model Judgment branches into three non-sequential functional placements: Input Interpretation, Decision Logic, and Output Mediation."},
        "05": {"alt": "Product and requirement uncertainty, environment and operational uncertainty, and runtime-judgment uncertainty converge on one controlled system."},
        "06": {"alt": "A closed feedback loop connects the controlled process to Sensors, a Controller or decision function, an authorized Actuator, and changed operation."},
        "07": {"alt": "A complete bounded control architecture adds authoritative Constraints and realizations to Sensors, Controllers, Actuators, and the controlled process."},
        "08a": {"alt": "The decision-ownership model connects Organization, Project or Architecture, Delivery, Runtime, category confirmation, authorization flows, and reassessment evidence."},
        "08b": {"alt": "The capability-family model lists Actuators, Constraints and realizations, Sensors and evidence, and Controllers or decision functions as orthogonal to every decision horizon."},
    },
    "official_sources": {
        "linkedin_article_limits": "https://www.linkedin.com/help/linkedin/answer/a522483",
        "linkedin_article_images": "https://www.linkedin.com/help/linkedin/answer/a522463",
        "linkedin_rich_media": "https://www.linkedin.com/help/linkedin/answer/a518895",
        "linkedin_seo": "https://www.linkedin.com/help/linkedin/answer/a6244140",
        "linkedin_link_preview": "https://www.linkedin.com/help/linkedin/answer/a566445/customizing-an-image-and-title-when-posting-a-url-on-your-linkedin-page?lang=en",
        "medium_images": "https://help.medium.com/hc/en-us/articles/215679797-Using-images",
        "medium_import": "https://help.medium.com/hc/en-us/articles/214550207-Importing-a-post-to-Medium",
        "medium_canonical": "https://help.medium.com/hc/en-us/articles/360033930293-Set-a-canonical-link",
    },
}
write_json("quartz/publication/thinking-systems.platforms.json", profile)

write(
    "content/research/notes/thinking-systems-linkedin-launch-post.md",
    r'''
    ---
    title: "LinkedIn Launch Post — Thinking Systems"
    artifact_type: research-note
    status: research
    maturity: draft
    module: research
    topics:
      - thinking-systems
      - provenance
      - repository-architecture
    tags:
      - ua/module/research
      - ua/type/research-note
      - ua/status/research
      - ua/topic/thinking-systems
      - ua/topic/provenance
      - ua/topic/repository-architecture
    created: 2026-08-19
    updated: 2026-08-19
    language: en
    license: CC-BY-4.0
    draft: true
    authors:
      - "Vitalii Oborskyi"
    source_basis:
      - thinking-systems-publication-draft.md
    related:
      - thinking-systems-platform-renditions.md
    ---

    # LinkedIn Launch Post — Thinking Systems

    This is the copy source for the LinkedIn launch post accompanying the native LinkedIn article. It is a distribution artifact, not a source of UA doctrine. Convert the named people into LinkedIn mentions in the editor before publishing; do not alter the substantive attribution boundary.

    <!-- platform-copy:start -->
    There is an idea I first encountered at university that has stayed with me ever since.

    In the sociology of science, one related concept is multiple discovery: important ideas rarely appear as isolated flashes of genius. They emerge when previous work and conversations bring people close enough to the same problem.

    The lone genius makes a good movie poster. Real innovation often looks more like a complicated Git history.

    AI is giving us an unusually visible example. We have LLMs, but we still do not know where their diffusion will stop or which applications will ultimately matter most.

    And in engineering, before we can search seriously for a solution, we first need to frame the problem correctly.

    That is part of the story behind my new working paper:

    Thinking Systems: When the Controlled Object Changes

    One important step came from my exchange with Arkadiy Dobkin following his post about AI and the enterprise “last mile.”

    I want to thank Arkadiy specifically for the formulation “Thinking Systems.” It gave a name to an engineering object I had already been circling around in my work on Uncertainty Architecture — and pushed me to make the boundary more precise.

    In the paper, a Thinking System means software in which one or more consequential runtime responsibilities depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.

    That leads to the central question:

    What if the important change is not simply that software contains an AI component, but that the engineering object itself has changed?

    From there, I examine why the whole socio-technical control system — not merely the model call — may need explicit boundaries, evidence, authority, corrective action, and reassessment.

    Another important influence has been my dialogue with the Taller team about the socio-technical architecture surrounding AI.

    Christophe Kolb, Maxi Armesto, Jan — thank you for the thoughtful discussions. Let’s keep them going.

    There is also a recursive part.

    The article and UA repository are increasingly being developed through agentic workflows. I use UA to structure the human–agent system producing the research: authority sources, constraints, evidence, review boundaries, decision ownership, revision loops, and escalation back to human judgment.

    That does not validate the framework. But it gives me another place to test it.

    I do not need people to agree with UA. I need people to try to break it.

    Apply the map to a real system. Show me where the category fails, where an existing approach already solves the problem better — or what can simply be removed.

    Uncertainty Architecture is open source and under validation. Critiques, contradictory cases, issues, PRs, and serious collaboration are welcome.
    <!-- platform-copy:end -->
    ''',
)

write(
    "content/research/notes/thinking-systems-platform-renditions.md",
    r'''
    ---
    title: "Platform Rendition Profile — Thinking Systems"
    artifact_type: research-note
    status: research
    maturity: draft
    module: research
    topics:
      - thinking-systems
      - provenance
      - repository-architecture
    tags:
      - ua/module/research
      - ua/type/research-note
      - ua/status/research
      - ua/topic/thinking-systems
      - ua/topic/provenance
      - ua/topic/repository-architecture
    created: 2026-08-19
    updated: 2026-08-19
    language: en
    license: CC-BY-4.0
    draft: true
    source_basis:
      - thinking-systems-publication-draft.md
      - thinking-systems-linkedin-launch-post.md
    related:
      - ../review-process.md
      - thinking-systems-publication-draft.md
    ---

    # Platform Rendition Profile — Thinking Systems

    This note defines the distribution boundary for Medium and LinkedIn renditions of *Thinking Systems: When the Controlled Object Changes*. It is non-normative research and does not create a second conceptual version of the article.

    ## Source relationship

    The canonical editable source remains [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) until an actual publication decision freezes an exact content edition under [`../publications/`](../publications/). Medium and LinkedIn outputs may change formatting, image placement, table presentation, cover metadata, platform notes, SEO fields, and the launch post. They must not silently change definitions, decision ownership, maturity caveats, attribution, or the Figure 8 relationships.

    The machine profile lives at [`../../../quartz/publication/thinking-systems.platforms.json`](../../../quartz/publication/thinking-systems.platforms.json). Generated files remain under `dist/publication/thinking-systems/` and are not committed.

    ## Generated package

    ```text
    canonical article Markdown
    → reviewed SVG/PNG figures and covers
    → table-to-readable-section conversion
    → absolute durable links
    → Medium article package
    → LinkedIn article package
    → LinkedIn launch post
    → provenance and readiness manifest
    ```

    The generated package contains copy-ready HTML, Markdown, and plain-text versions; image upload placeholders; alt text; captions; SEO metadata; canonical-link guidance; and platform-specific publishing checklists.

    ## Publication boundary

    A generated package is not automatically publication-ready. Before external release:

    1. freeze the exact content edition under `content/research/publications/`;
    2. set one principal canonical URL;
    3. regenerate the package from that committed source;
    4. review every image, caption, table conversion, link, and platform preview;
    5. convert the named people in the launch post into actual LinkedIn mentions;
    6. publish equivalent platform copies as renditions of the same edition;
    7. record final URLs and immutable source identity before feedback-driven revision.

    ## Current official constraints

    The profile records current first-party constraints used by the generator:

    - LinkedIn posts: 3,000 characters; LinkedIn articles: 125,000 characters.
    - LinkedIn article cover: 2,000 × 600 pixels, up to 10 MB, JPG/static GIF/PNG.
    - LinkedIn SEO title: truncate risk above 60 characters; recommended SEO description: 140–160 characters.
    - LinkedIn article editor: tables are not currently supported, so article tables are expanded into readable labeled sections.
    - Medium images: JPG/JPEG/GIF/PNG up to 25 MB; at least 1,192 px wide for all placement options.
    - Medium canonical URL: use import-from-URL where possible or set the canonical link manually.

    Reverify these values against the official URLs in the machine profile immediately before publication because platform behavior changes independently of the repository.
    ''',
)

write(
    "quartz/scripts/render-platform-renditions.mjs",
    r'''
    #!/usr/bin/env node

    import { readFile, mkdtemp, mkdir, rm, stat } from "node:fs/promises"
    import path from "node:path"
    import { fileURLToPath } from "node:url"
    import matter from "gray-matter"
    import { unified } from "unified"
    import remarkParse from "remark-parse"
    import remarkGfm from "remark-gfm"
    import remarkRehype from "remark-rehype"
    import rehypeRaw from "rehype-raw"
    import { toHtml } from "hast-util-to-html"
    import {
      assertSafeOutputPath,
      writeFileAtomically,
    } from "./publication-path-safety.mjs"
    import { determineSourceProvenance } from "./publication-provenance.mjs"
    import {
      currentArticleSource,
      defaultRepository,
      gitOutput,
      loadPublicationSource,
      repoRoot,
      sha256,
    } from "./publication-rendition.mjs"
    import {
      assertFigure8SemanticSource,
    } from "./publication-figure8.mjs"
    import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs"
    import { finalizePublicationDirectory } from "./run-publication-assets.mjs"

    const defaultProfile = "quartz/publication/thinking-systems.platforms.json"
    const publicationRoot = path.join(repoRoot, "dist", "publication")

    function parseArgs(argv) {
      let profile = defaultProfile
      let allowDirtyPreview = false
      for (let index = 0; index < argv.length; index += 1) {
        const value = argv[index]
        if (value === "--profile") profile = argv[++index]
        else if (value === "--allow-dirty-preview") allowDirtyPreview = true
        else if (value === "--help" || value === "-h") return { help: true }
        else throw new Error(`Unknown argument: ${value}`)
      }
      return { profile, allowDirtyPreview, help: false }
    }

    function usage() {
      console.log("Usage: node quartz/scripts/render-platform-renditions.mjs [--profile quartz/publication/file.json] [--allow-dirty-preview]")
    }

    function countCharacters(value) {
      return [...String(value ?? "")].length
    }

    function parseTableRow(line) {
      return line.trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map((cell) => cell.trim())
    }

    function isSeparatorRow(line) {
      const cells = parseTableRow(line)
      return cells.length > 0 && cells.every((cell) => /^:?-{3,}:?$/.test(cell))
    }

    export function convertMarkdownTables(markdown) {
      const lines = markdown.split(/\r?\n/)
      const output = []
      let index = 0
      while (index < lines.length) {
        if (
          lines[index]?.trim().startsWith("|") &&
          lines[index + 1]?.trim().startsWith("|") &&
          isSeparatorRow(lines[index + 1])
        ) {
          const headers = parseTableRow(lines[index])
          index += 2
          const rows = []
          while (index < lines.length && lines[index].trim().startsWith("|")) {
            rows.push(parseTableRow(lines[index]))
            index += 1
          }
          for (const row of rows) {
            const label = row[0] || "Item"
            output.push(`### ${label}`, "")
            for (let column = 1; column < headers.length; column += 1) {
              if (!row[column]) continue
              output.push(`**${headers[column]}:** ${row[column]}`, "")
            }
          }
          continue
        }
        output.push(lines[index])
        index += 1
      }
      return output.join("\n")
    }

    function encodeRepositoryPath(value) {
      return value.split("/").map(encodeURIComponent).join("/")
    }

    export function rewriteRelativeLinks(markdown, sourceRelative, repository, sourceCommit) {
      const sourceDirectory = path.posix.dirname(sourceRelative)
      return markdown.replace(/\[([^\]]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g, (full, label, target) => {
        if (/^(?:https?:|mailto:|tel:|#)/i.test(target)) return full
        const [pathname, fragment = ""] = target.split("#", 2)
        const resolved = path.posix.normalize(path.posix.join(sourceDirectory, pathname))
        if (resolved.startsWith("../")) {
          throw new Error(`Platform rendition link escapes the repository root: ${target}`)
        }
        const suffix = fragment ? `#${encodeURIComponent(fragment)}` : ""
        return `[${label}](https://github.com/${repository}/blob/${encodeURIComponent(sourceCommit)}/${encodeRepositoryPath(resolved)}${suffix})`
      })
    }

    export function extractLaunchPost(raw) {
      const parsed = matter(raw)
      const match = /<!-- platform-copy:start -->\s*([\s\S]*?)\s*<!-- platform-copy:end -->/.exec(parsed.content)
      if (!match) throw new Error("LinkedIn launch-post source is missing platform-copy markers")
      return match[1].trim()
    }

    function stripCanonicalHeadingAndNote(content) {
      let value = content.replace(/^#\s+[^\n]+\n+/, "")
      value = value.replace(/^>\s+\*\*Publication note\.\*\*[^\n]*(?:\n>[^\n]*)*\n+/m, "")
      return value
    }

    export function replaceMermaidWithFigureTokens(markdown, { verifyFigure8 = true } = {}) {
      const seen = []
      const pattern = /```mermaid\r?\n([\s\S]*?)\r?\n```\r?\n\r?\n(\*\*Figure\s+(\d+)\s+—[^\n]*)/g
      const replaced = markdown.replace(pattern, (full, mermaid, caption, numberText) => {
        const number = Number(numberText)
        seen.push(number)
        if (number === 8) {
          assertFigure8SemanticSource(mermaid)
          if (verifyFigure8) assertCanonicalFigure8Fingerprint(mermaid, caption)
          return `@@UA_FIGURE_08A@@\n\n@@UA_FIGURE_08B@@\n\n${caption}`
        }
        const id = String(number).padStart(2, "0")
        return `@@UA_FIGURE_${id.toUpperCase()}@@\n\n${caption}`
      })
      if (/```mermaid/.test(replaced)) {
        throw new Error("A Mermaid block without a publication caption remains in the platform rendition")
      }
      const expected = [1, 2, 3, 4, 5, 6, 7, 8]
      if (JSON.stringify(seen) !== JSON.stringify(expected)) {
        throw new Error(`Expected canonical Figures 1–8 in order; received ${seen.join(", ")}`)
      }
      return replaced
    }

    function escapeHtml(value) {
      return String(value ?? "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;")
    }

    function figureToken(id) {
      return `@@UA_FIGURE_${id.toUpperCase()}@@`
    }

    function imagePathFor(id) {
      return `../../figures/png/figure-${id}.png`
    }

    function buildFigureHtml(id, profile) {
      const alt = profile.figures[id]?.alt
      if (!alt) throw new Error(`Missing curated alt text for figure ${id}`)
      return `<figure class="platform-figure" data-figure-id="${id}"><img src="${imagePathFor(id)}" alt="${escapeHtml(alt)}"/><figcaption><strong>Upload file:</strong> figure-${id}.png</figcaption></figure>`
    }

    function buildFigureMarkdown(id, profile) {
      const alt = profile.figures[id]?.alt
      if (!alt) throw new Error(`Missing curated alt text for figure ${id}`)
      return `> **UPLOAD IMAGE:** \`${imagePathFor(id)}\`\n>\n> **Alt text:** ${alt}`
    }

    async function markdownToHtml(markdown) {
      const mdast = unified().use(remarkParse).use(remarkGfm).parse(markdown)
      const hast = await unified()
        .use(remarkRehype, { allowDangerousHtml: true })
        .use(rehypeRaw)
        .run(mdast)
      return toHtml(hast, { allowDangerousHtml: true })
    }

    function applyFigureHtml(html, profile) {
      for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
        const paragraph = `<p>${figureToken(id)}</p>`
        if (!html.includes(paragraph)) throw new Error(`Platform HTML is missing figure token ${id}`)
        html = html.replace(paragraph, buildFigureHtml(id, profile))
      }
      return html
    }

    function applyFigureMarkdown(markdown, profile) {
      for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
        const token = figureToken(id)
        if (!markdown.includes(token)) throw new Error(`Platform Markdown is missing figure token ${id}`)
        markdown = markdown.replace(token, buildFigureMarkdown(id, profile))
      }
      return markdown
    }

    function decodeEntities(value) {
      return value
        .replaceAll("&amp;", "&")
        .replaceAll("&lt;", "<")
        .replaceAll("&gt;", ">")
        .replaceAll("&quot;", '"')
        .replaceAll("&#39;", "'")
        .replaceAll("&nbsp;", " ")
    }

    export function htmlToPlainText(html) {
      return decodeEntities(
        html
          .replace(/<figure[^>]*data-figure-id="([^"]+)"[^>]*>[\s\S]*?<\/figure>/g, "\n\n[UPLOAD IMAGE: figure-$1.png]\n\n")
          .replace(/<a\s+href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g, "$2 ($1)")
          .replace(/<li[^>]*>/g, "\n- ")
          .replace(/<\/(?:p|h1|h2|h3|h4|blockquote|li|ul|ol|section|div|figure)>/g, "\n\n")
          .replace(/<br\s*\/?\s*>/g, "\n")
          .replace(/<[^>]+>/g, "")
          .replace(/[ \t]+\n/g, "\n")
          .replace(/\n{3,}/g, "\n\n")
          .trim(),
      )
    }

    function standaloneHtml({ title, subtitle, hero, body, sourceCommit, sourceState }) {
      const heroHtml = hero ? `<img class="platform-hero" src="../../${escapeHtml(hero)}" alt=""/>` : ""
      return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>${escapeHtml(title)}</title>
<style>
body{font-family:Arial,sans-serif;line-height:1.55;color:#202124;margin:0;background:#f3f4f5}main{max-width:820px;margin:0 auto;background:white;padding:48px 56px}h1{font-size:42px;line-height:1.12}h2{margin-top:2.2em}h3{margin-top:1.5em}.deck{font-size:21px;color:#51606a}.platform-hero,.platform-figure img{display:block;max-width:100%;height:auto;margin:24px auto}.platform-figure{margin:36px 0}.platform-figure figcaption{font-size:13px;color:#667}.platform-note{border-left:4px solid #54736d;padding-left:16px;color:#42545f}blockquote{margin-left:0;border-left:4px solid #d3d8dc;padding-left:16px}code{white-space:pre-wrap}.provenance{margin-top:48px;font-size:12px;color:#778}</style>
</head>
<body><main>${heroHtml}<h1>${escapeHtml(title)}</h1><p class="deck">${escapeHtml(subtitle)}</p>${body}<p class="provenance">Generated from source commit ${escapeHtml(sourceCommit)} · source state ${escapeHtml(sourceState)}</p></main></body>
</html>`
    }

    function repositoryUrl(repository, sourceCommit, targetPath = "") {
      if (!targetPath) return `https://github.com/${repository}`
      return `https://github.com/${repository}/blob/${encodeURIComponent(sourceCommit)}/${targetPath.split("/").map(encodeURIComponent).join("/")}`
    }

    function buildResourceBlock(profile, sourceCommit) {
      const lines = ["## Resources", ""]
      for (const resource of profile.resources ?? []) {
        lines.push(`- [${resource.label}](${repositoryUrl(profile.repository, sourceCommit, resource.path)})`)
      }
      return lines.join("\n")
    }

    function buildPlatformMarkdown(base, platform, profile, sourceCommit) {
      return [
        `# ${platform.title}`,
        "",
        `> ${platform.subtitle}`,
        "",
        `> **Publication note.** ${platform.publication_note}`,
        "",
        base,
        "",
        platform.closing_note,
        "",
        buildResourceBlock(profile, sourceCommit),
        "",
      ].join("\n")
    }

    function validateProfile(profile) {
      if (profile.schema_version !== 1) throw new Error("Unsupported platform-profile schema")
      if (profile.source !== currentArticleSource) throw new Error("Current profile must target the standalone Thinking Systems article")
      if (countCharacters(profile.linkedin.seo_title) > profile.linkedin.seo_title_max_characters) {
        throw new Error("LinkedIn SEO title exceeds the configured limit")
      }
      const seoDescription = countCharacters(profile.linkedin.seo_description)
      if (seoDescription < profile.linkedin.seo_description_min_characters || seoDescription > profile.linkedin.seo_description_max_characters) {
        throw new Error("LinkedIn SEO description is outside the configured 140–160 character range")
      }
      for (const id of ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]) {
        if (!profile.figures[id]?.alt) throw new Error(`Missing alt text for figure ${id}`)
      }
      return profile
    }

    async function assertFileDimensions(filePath, width, height, maxBytes = null) {
      const info = await stat(filePath)
      if (!info.isFile() || info.size === 0) throw new Error(`Missing generated image: ${filePath}`)
      if (maxBytes && info.size > maxBytes) throw new Error(`Generated image exceeds platform byte limit: ${filePath}`)
      const sharp = (await import("sharp")).default
      const metadata = await sharp(filePath).metadata()
      if (metadata.width !== width || metadata.height !== height) {
        throw new Error(`${path.basename(filePath)} is ${metadata.width}×${metadata.height}; expected ${width}×${height}`)
      }
    }

    function verifyAssetManifest(manifest, profile, provenance, sourceCommit) {
      if (manifest.source_path !== profile.source) throw new Error("Asset manifest source does not match platform profile")
      if (manifest.source_commit !== sourceCommit) throw new Error("Asset manifest commit does not match platform rendition commit")
      if (manifest.source_state !== provenance.state) throw new Error("Asset manifest source state does not match platform rendition state")
      if (manifest.source_working_blob_sha !== provenance.workingBlob) throw new Error("Asset manifest working blob does not match platform source")
      const ids = (manifest.figures ?? []).map((figure) => figure.id)
      const expected = ["01", "02", "03", "04", "05", "06", "07", "08a", "08b"]
      if (JSON.stringify(ids.sort()) !== JSON.stringify(expected.sort())) {
        throw new Error(`Asset manifest figure set is incomplete: ${ids.join(", ")}`)
      }
      if (!manifest.figure_8_panels_must_travel_together || !manifest.figure_8_canonical_caption) {
        throw new Error("Figure 8 platform assets must preserve the shared canonical-caption contract")
      }
    }

    function buildChecklist(platformName, profile, source, sourceCommit, publicationReady) {
      const platform = profile[platformName]
      const official = profile.official_sources
      const lines = [
        `# ${platformName === "linkedin" ? "LinkedIn" : "Medium"} Publishing Checklist`,
        "",
        `- Source: \`${source.relative}\``,
        `- Source commit: \`${sourceCommit}\``,
        `- Publication status: ${publicationReady ? "frozen/canonical metadata present" : "DRAFT — freeze a repository edition and set canonical_url before publication"}`,
        "- Open `article.html` in a desktop browser for rich-text review/copying.",
        "- Use `article.md` as the authoritative placement guide for images, captions, and alt text.",
        "- Upload every image named by an `UPLOAD IMAGE` marker; do not paste Mermaid source.",
        "- Recheck every link, caption, table-to-section conversion, and Figure 8A/8B sequence in the platform preview.",
      ]
      if (platformName === "linkedin") {
        lines.push(
          "- Upload `../../cover-linkedin-article.png` as the article cover.",
          "- Apply `seo.json` in LinkedIn SEO settings.",
          "- Convert the names in `launch-post.txt` into actual LinkedIn mentions before publishing.",
          `- Keep the launch post at or below ${profile.linkedin.post_max_characters} characters; current count is recorded in the manifest.`,
          "- LinkedIn does not currently support tables in article editing; verify the generated labeled-section conversion.",
          "",
          `Official references: ${official.linkedin_article_limits} · ${official.linkedin_article_images} · ${official.linkedin_rich_media} · ${official.linkedin_seo}`,
        )
      } else {
        lines.push(
          "- Upload `../../medium-hero.png` as the story hero.",
          "- Prefer Medium’s Import a story flow from the final canonical URL; otherwise set the canonical URL manually.",
          "- Confirm each uploaded figure is at least 1,192 px wide when full placement options are needed.",
          "",
          `Official references: ${official.medium_images} · ${official.medium_import} · ${official.medium_canonical}`,
        )
      }
      return `${lines.join("\n")}\n`
    }

    async function main() {
      const args = parseArgs(process.argv.slice(2))
      if (args.help) return usage()

      const profilePath = path.resolve(repoRoot, args.profile)
      const profile = validateProfile(JSON.parse(await readFile(profilePath, "utf8")))
      const source = await loadPublicationSource(profile.source)
      const sourceCommit =
        process.env.UA_PDF_REPOSITORY_REF ||
        process.env.GITHUB_SHA ||
        (await gitOutput(["rev-parse", "HEAD"]))
      const provenance = await determineSourceProvenance(source, sourceCommit, {
        allowDirtyPreview: args.allowDirtyPreview,
      })
      const repository = process.env.GITHUB_REPOSITORY || profile.repository || defaultRepository
      profile.repository = repository

      const outputRoot = path.resolve(repoRoot, profile.output_root)
      await assertSafeOutputPath(repoRoot, publicationRoot, outputRoot)
      const assetsManifestPath = path.join(outputRoot, "assets.manifest.json")
      const assetsManifestRaw = await readFile(assetsManifestPath, "utf8").catch(() => null)
      if (!assetsManifestRaw) throw new Error("Platform assets are missing. Run npm run publication:assets first.")
      const assetsManifest = JSON.parse(assetsManifestRaw)
      verifyAssetManifest(assetsManifest, profile, provenance, sourceCommit)

      await assertFileDimensions(path.join(outputRoot, profile.linkedin.cover.file), profile.linkedin.cover.width, profile.linkedin.cover.height, profile.linkedin.cover.max_bytes)
      await assertFileDimensions(path.join(outputRoot, profile.linkedin.social_preview.file), profile.linkedin.social_preview.width, profile.linkedin.social_preview.height)
      await assertFileDimensions(path.join(outputRoot, profile.medium.hero.file), profile.medium.hero.width, profile.medium.hero.height, profile.medium.image_max_bytes)
      for (const figure of assetsManifest.figures) {
        const filePath = path.join(repoRoot, ...figure.png.split("/"))
        const info = await stat(filePath)
        if (info.size > profile.medium.image_max_bytes) throw new Error(`Figure exceeds Medium image limit: ${figure.png}`)
        if (figure.width < profile.medium.image_min_width) throw new Error(`Figure is too narrow for Medium full placement: ${figure.png}`)
      }

      let baseMarkdown = stripCanonicalHeadingAndNote(source.content)
      baseMarkdown = replaceMermaidWithFigureTokens(baseMarkdown)
      baseMarkdown = convertMarkdownTables(baseMarkdown)
      baseMarkdown = rewriteRelativeLinks(baseMarkdown, source.relative, repository, sourceCommit)

      const launchRaw = await readFile(path.resolve(repoRoot, profile.launch_post_source), "utf8")
      const launchPost = extractLaunchPost(launchRaw)
      const launchCharacters = countCharacters(launchPost)
      if (launchCharacters > profile.linkedin.post_max_characters) {
        throw new Error(`LinkedIn launch post is ${launchCharacters} characters; limit is ${profile.linkedin.post_max_characters}`)
      }
      if (launchCharacters > profile.linkedin.post_target_max_characters) {
        throw new Error(`LinkedIn launch post leaves insufficient mention/link headroom: ${launchCharacters} characters`)
      }

      const mediumMarkdown = applyFigureMarkdown(buildPlatformMarkdown(baseMarkdown, profile.medium, profile, sourceCommit), profile)
      const linkedinMarkdown = applyFigureMarkdown(buildPlatformMarkdown(baseMarkdown, profile.linkedin, profile, sourceCommit), profile)
      const mediumBody = applyFigureHtml(await markdownToHtml(mediumMarkdown), profile)
      const linkedinBody = applyFigureHtml(await markdownToHtml(linkedinMarkdown), profile)
      const mediumHtml = standaloneHtml({ title: profile.medium.title, subtitle: profile.medium.subtitle, hero: profile.medium.hero.file, body: mediumBody, sourceCommit, sourceState: provenance.state })
      const linkedinHtml = standaloneHtml({ title: profile.linkedin.title, subtitle: profile.linkedin.subtitle, hero: null, body: linkedinBody, sourceCommit, sourceState: provenance.state })
      const linkedinText = htmlToPlainText(linkedinBody)
      const mediumText = htmlToPlainText(mediumBody)
      const linkedinArticleCharacters = countCharacters(linkedinText)
      if (linkedinArticleCharacters > profile.linkedin.article_max_characters) {
        throw new Error(`LinkedIn article is ${linkedinArticleCharacters} characters; limit is ${profile.linkedin.article_max_characters}`)
      }
      if (/<table\b/i.test(linkedinHtml) || /```mermaid/.test(linkedinMarkdown)) {
        throw new Error("LinkedIn rendition still contains a table or Mermaid source")
      }

      const publicationReady = source.data.draft !== true && Boolean(source.data.canonical_url)
      const canonicalText = source.data.canonical_url
        ? `${source.data.canonical_url}\n`
        : `PENDING — freeze the exact edition under content/research/publications/ and set canonical_url before publishing.\nCurrent versioned source: ${repositoryUrl(repository, sourceCommit, source.relative)}\n`

      const stagingRoot = await mkdtemp(path.join(publicationRoot, ".ua-platform-stage-"))
      const renditionRoot = path.join(outputRoot, "renditions")
      try {
        const mediumDir = path.join(stagingRoot, "medium")
        const linkedinDir = path.join(stagingRoot, "linkedin")
        await mkdir(mediumDir, { recursive: true })
        await mkdir(linkedinDir, { recursive: true })

        const writes = [
          [path.join(mediumDir, "article.md"), mediumMarkdown + "\n"],
          [path.join(mediumDir, "article.html"), mediumHtml + "\n"],
          [path.join(mediumDir, "article.txt"), mediumText + "\n"],
          [path.join(mediumDir, "canonical-url.txt"), canonicalText],
          [path.join(mediumDir, "publishing-checklist.md"), buildChecklist("medium", profile, source, sourceCommit, publicationReady)],
          [path.join(linkedinDir, "article.md"), linkedinMarkdown + "\n"],
          [path.join(linkedinDir, "article.html"), linkedinHtml + "\n"],
          [path.join(linkedinDir, "article.txt"), linkedinText + "\n"],
          [path.join(linkedinDir, "launch-post.txt"), launchPost + "\n"],
          [path.join(linkedinDir, "seo.json"), JSON.stringify({ title: profile.linkedin.seo_title, description: profile.linkedin.seo_description }, null, 2) + "\n"],
          [path.join(linkedinDir, "publishing-checklist.md"), buildChecklist("linkedin", profile, source, sourceCommit, publicationReady)],
        ]
        for (const [target, value] of writes) {
          await writeFileAtomically(target, value, { trustedRoot: repoRoot, allowedRoot: publicationRoot, forbiddenPaths: [source.absolute, path.resolve(repoRoot, profile.launch_post_source)] })
        }

        const outputFiles = {}
        for (const [target, value] of writes) {
          const relative = path.relative(stagingRoot, target).split(path.sep).join("/")
          outputFiles[relative] = sha256(Buffer.from(value))
        }
        const manifest = {
          schema_version: 1,
          artifact: "platform-renditions",
          publication_id: profile.publication_id,
          source_path: source.relative,
          source_commit: sourceCommit,
          source_state: provenance.state,
          source_git_blob_sha: provenance.committedBlob,
          source_working_blob_sha: provenance.workingBlob,
          source_sha256: sha256(Buffer.from(source.raw)),
          assets_manifest_sha256: sha256(Buffer.from(assetsManifestRaw)),
          generated_at: new Date().toISOString(),
          publication_ready: publicationReady,
          canonical_url: source.data.canonical_url || null,
          linkedin_article_characters: linkedinArticleCharacters,
          linkedin_launch_post_characters: launchCharacters,
          linkedin_post_limit: profile.linkedin.post_max_characters,
          linkedin_article_limit: profile.linkedin.article_max_characters,
          figure_8_panels_must_travel_together: true,
          outputs: outputFiles,
        }
        await writeFileAtomically(path.join(stagingRoot, "platform-renditions.manifest.json"), JSON.stringify(manifest, null, 2) + "\n", { trustedRoot: repoRoot, allowedRoot: publicationRoot, forbiddenPaths: [source.absolute] })
        await finalizePublicationDirectory(stagingRoot, renditionRoot)
      } finally {
        await rm(stagingRoot, { recursive: true, force: true })
      }

      console.log(`Platform renditions ready: ${path.relative(repoRoot, renditionRoot)}`)
      console.log(`LinkedIn article: ${linkedinArticleCharacters}/${profile.linkedin.article_max_characters} characters`)
      console.log(`LinkedIn launch post: ${launchCharacters}/${profile.linkedin.post_max_characters} characters`)
      if (!publicationReady) console.log("Publication readiness: draft package; canonical freeze still required")
    }

    const isEntryPoint = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)
    if (isEntryPoint) {
      main().catch((error) => {
        console.error(`Platform rendition failed: ${error instanceof Error ? error.message : String(error)}`)
        process.exitCode = 1
      })
    }
    ''',
)

write(
    "quartz/scripts/platform-rendition.test.mjs",
    r'''
    import assert from "node:assert/strict"
    import { readFile } from "node:fs/promises"
    import path from "node:path"
    import test from "node:test"

    import {
      convertMarkdownTables,
      extractLaunchPost,
      htmlToPlainText,
      replaceMermaidWithFigureTokens,
      rewriteRelativeLinks,
    } from "./render-platform-renditions.mjs"
    import { repoRoot } from "./publication-rendition.mjs"

    test("platform table conversion expands rows into labeled readable sections", () => {
      const input = "| Term | Meaning |\n|---|---|\n| Thinking System | A responsibility boundary |\n| Model Judgment | Probabilistic selection |"
      const output = convertMarkdownTables(input)
      assert.match(output, /### Thinking System/)
      assert.match(output, /\*\*Meaning:\*\* A responsibility boundary/)
      assert.doesNotMatch(output, /^\|/m)
    })

    test("platform links become immutable GitHub source links", () => {
      const output = rewriteRelativeLinks(
        "[Working paper](open-engineering-specification-article-draft.md#section)",
        "content/research/notes/thinking-systems-publication-draft.md",
        "Example/Repo",
        "abc123",
      )
      assert.equal(
        output,
        "[Working paper](https://github.com/Example/Repo/blob/abc123/content/research/notes/open-engineering-specification-article-draft.md#section)",
      )
    })

    test("launch post markers produce copy under the LinkedIn hard limit", async () => {
      const source = await readFile(
        path.join(repoRoot, "content/research/notes/thinking-systems-linkedin-launch-post.md"),
        "utf8",
      )
      const post = extractLaunchPost(source)
      assert.ok([...post].length <= 3000)
      assert.ok([...post].length <= 2900)
      assert.match(post, /thank Arkadiy specifically for the formulation “Thinking Systems”/)
      assert.match(post, /Christophe Kolb, Maxi Armesto, Jan/)
      assert.match(post, /I need people to try to break it/)
    })

    test("plain-text conversion keeps image upload markers and link targets", () => {
      const text = htmlToPlainText('<p>Read <a href="https://example.com">this</a>.</p><figure data-figure-id="01"><img/></figure>')
      assert.match(text, /this \(https:\/\/example.com\)/)
      assert.match(text, /UPLOAD IMAGE: figure-01.png/)
    })

    test("unreviewed Mermaid remains a hard failure", () => {
      assert.throws(
        () => replaceMermaidWithFigureTokens("```mermaid\nflowchart LR\nA-->B\n```\n\nNo caption"),
        /without a publication caption remains/,
      )
    })

    test("platform profile records current official LinkedIn and Medium constraints", async () => {
      const profile = JSON.parse(
        await readFile(path.join(repoRoot, "quartz/publication/thinking-systems.platforms.json"), "utf8"),
      )
      assert.equal(profile.linkedin.post_max_characters, 3000)
      assert.equal(profile.linkedin.article_max_characters, 125000)
      assert.deepEqual([profile.linkedin.cover.width, profile.linkedin.cover.height], [2000, 600])
      assert.equal(profile.medium.image_min_width, 1192)
      assert.equal(profile.medium.image_max_bytes, 25 * 1024 * 1024)
      assert.ok([...profile.linkedin.seo_title].length <= 60)
      assert.ok([...profile.linkedin.seo_description].length >= 140)
      assert.ok([...profile.linkedin.seo_description].length <= 160)
    })
    ''',
)

write(
    "quartz/PLATFORM-RENDITIONS.md",
    r'''
    # Medium and LinkedIn rendition export

    This layer converts one committed publication source into platform-ready distribution packages without making Medium or LinkedIn a second conceptual authority.

    ## Commands

    ```bash
    npm run publication:assets
    npm run publication:platforms
    # or both in one command
    npm run publication:bundle
    ```

    Generated outputs remain untracked:

    ```text
    dist/publication/thinking-systems/
      figures/svg/
      figures/png/
      cover-linkedin-article.png
      social-preview.png
      medium-hero.png
      assets.manifest.json
      figure-08-shared-caption.md
      renditions/
        medium/
          article.html
          article.md
          article.txt
          canonical-url.txt
          publishing-checklist.md
        linkedin/
          article.html
          article.md
          article.txt
          launch-post.txt
          seo.json
          publishing-checklist.md
        platform-renditions.manifest.json
    ```

    `article.html` is the rich-text review/copy surface. `article.md` is the placement authority for images, captions, and alt text. `article.txt` is a plain-text fallback. The generator expands Markdown tables into labeled sections because LinkedIn’s article editor does not currently support tables.

    The package is strict about source provenance. It must match the declared commit unless `--allow-dirty-preview` is used explicitly. A draft source without `canonical_url` can generate a review package, but the manifest records `publication_ready: false`; external publication still requires an immutable repository edition and canonical URL.

    Figure 8A and Figure 8B are presentation panels of one logical Figure 8. They must be published together with `figure-08-shared-caption.md`.

    ## Current first-party constraints

    - LinkedIn: 3,000-character posts, 125,000-character articles, 2,000 × 600 article cover, 10 MB image limit, SEO title truncation above 60 characters, and recommended 140–160-character SEO description.
    - Medium: JPG/JPEG/GIF/PNG up to 25 MB and at least 1,192 px width for all image-placement options; canonical URLs can be set through import or Advanced Settings.

    The exact official references are stored in `quartz/publication/thinking-systems.platforms.json` and must be rechecked before release.
    ''',
)

write(
    ".github/workflows/export-platform-renditions.yml",
    r'''
    name: Export platform renditions

    on:
      pull_request:
        paths:
          - '.github/workflows/export-platform-renditions.yml'
          - 'package.json'
          - 'package-lock.json'
          - 'quartz/publication/**'
          - 'quartz/scripts/render-publication-assets.mjs'
          - 'quartz/scripts/run-publication-assets.mjs'
          - 'quartz/scripts/render-platform-renditions.mjs'
          - 'quartz/scripts/platform-rendition.test.mjs'
          - 'quartz/PLATFORM-RENDITIONS.md'
          - 'content/research/notes/thinking-systems-publication-draft.md'
          - 'content/research/notes/thinking-systems-linkedin-launch-post.md'
          - 'content/research/notes/thinking-systems-platform-renditions.md'
      push:
        branches:
          - main
        paths:
          - '.github/workflows/export-platform-renditions.yml'
          - 'package.json'
          - 'package-lock.json'
          - 'quartz/publication/**'
          - 'quartz/scripts/render-publication-assets.mjs'
          - 'quartz/scripts/run-publication-assets.mjs'
          - 'quartz/scripts/render-platform-renditions.mjs'
          - 'quartz/scripts/platform-rendition.test.mjs'
          - 'quartz/PLATFORM-RENDITIONS.md'
          - 'content/research/notes/thinking-systems-publication-draft.md'
          - 'content/research/notes/thinking-systems-linkedin-launch-post.md'
          - 'content/research/notes/thinking-systems-platform-renditions.md'
      workflow_dispatch:

    permissions:
      contents: read

    concurrency:
      group: platform-renditions-${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    jobs:
      render:
        name: Render / Medium and LinkedIn packages
        runs-on: ubuntu-24.04
        timeout-minutes: 25
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
          - name: Install Chromium
            run: ./node_modules/.bin/playwright install --with-deps chromium
          - name: Render platform bundle
            env:
              UA_PDF_REPOSITORY_REF: ${{ github.sha }}
            run: npm run publication:bundle
          - name: Upload platform bundle
            uses: actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02 # v4.6.2
            with:
              name: thinking-systems-platform-renditions
              path: dist/publication/thinking-systems/**
              if-no-files-found: error
              retention-days: 14
    ''',
)

# package.json scripts
package_path = ROOT / "package.json"
package = json.loads(package_path.read_text(encoding="utf-8"))
scripts = package["scripts"]
ordered = {}
for key, value in scripts.items():
    ordered[key] = value
    if key == "publication:assets":
        ordered["publication:platforms"] = "node quartz/scripts/render-platform-renditions.mjs"
        ordered["publication:bundle"] = "npm run publication:assets && npm run publication:platforms"
package["scripts"] = ordered
write_json("package.json", package)

# Research notes index
notes_path = ROOT / "content/research/notes/README.md"
notes = notes_path.read_text(encoding="utf-8")
anchor = "- [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) — publication-facing adaptation titled *Thinking Systems: When the Controlled Object Changes*."
index = notes.find(anchor)
if index < 0:
    raise SystemExit("Thinking Systems publication entry not found in research-notes index")
line_end = notes.find("\n", index)
insert = (
    "\n- [`thinking-systems-platform-renditions.md`](thinking-systems-platform-renditions.md) — distribution profile for equivalent Medium and LinkedIn renditions of the Thinking Systems content edition, including platform constraints, canonical-link handling, image/alt-text rules, and the boundary between formatting adaptation and conceptual change."
    "\n- [`thinking-systems-linkedin-launch-post.md`](thinking-systems-linkedin-launch-post.md) — copy source for the LinkedIn launch post, preserving the Arkadiy Dobkin formulation credit, Taller dialogue acknowledgement, agentic-workflow reflection, and explicit invitation to challenge or simplify the framework."
)
notes_path.write_text(notes[:line_end] + insert + notes[line_end:], encoding="utf-8")

# Changelog and roadmap
changelog_path = ROOT / "CHANGELOG.md"
changelog = changelog_path.read_text(encoding="utf-8")
entry = "- Added reproducible Medium and LinkedIn rendition packaging for the Thinking Systems article: copy-ready HTML/Markdown/text, deterministic table expansion, durable links, reviewed figure PNG/SVG assets and alt text, LinkedIn cover/SEO/launch-post checks, Medium hero/canonical guidance, and provenance/readiness manifests without creating a second conceptual source.\n"
heading = "### Added\n\n"
if entry not in changelog:
    changelog = changelog.replace(heading, heading + entry, 1)
changelog_path.write_text(changelog, encoding="utf-8")

roadmap_path = ROOT / "ROADMAP.md"
roadmap = roadmap_path.read_text(encoding="utf-8")
roadmap_entry = "- reproducible Medium and LinkedIn rendition packages generated from one committed content edition, with platform-ready figures, covers, alt text, canonical-link guidance, SEO metadata, and launch-post validation;\n"
needle = "- deployment-independent publication rendering from canonical Markdown to PDF and reusable platform assets, with draft-only temporary builds, provenance manifests, visual verification, and explicit standalone-publication versus working-paper outputs;\n"
if roadmap_entry not in roadmap:
    if needle not in roadmap:
        raise SystemExit("Publishing roadmap anchor not found")
    roadmap = roadmap.replace(needle, needle + roadmap_entry, 1)
roadmap_path.write_text(roadmap, encoding="utf-8")

# Repository contract and regression fixture
contract_path = ROOT / ".github/policy/repository-contract-change-coupling.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))
required = [
    ".github/workflows/export-platform-renditions.yml",
    "quartz/PLATFORM-RENDITIONS.md",
    "quartz/publication/thinking-systems.platforms.json",
    "quartz/scripts/render-platform-renditions.mjs",
    "quartz/scripts/platform-rendition.test.mjs",
    "content/research/notes/thinking-systems-linkedin-launch-post.md",
    "content/research/notes/thinking-systems-platform-renditions.md",
]
existing_required = {item["path"] for item in contract["required_paths"]}
for value in required:
    if value not in existing_required:
        contract["required_paths"].append({"path": value, "type": "file"})
critical_by_path = {item["path"]: item for item in contract["critical_files"]}
critical_by_path.setdefault(
    ".github/workflows/export-platform-renditions.yml",
    {"path": ".github/workflows/export-platform-renditions.yml", "required_text": []},
)["required_text"] = [
    "name: Export platform renditions",
    "workflow_dispatch:",
    "npm run publication:bundle",
    "thinking-systems-platform-renditions",
    "fetch-depth: 0",
    "UA_PDF_REPOSITORY_REF: ${{ github.sha }}",
]
critical_by_path.setdefault(
    "quartz/scripts/render-platform-renditions.mjs",
    {"path": "quartz/scripts/render-platform-renditions.mjs", "required_text": []},
)["required_text"] = [
    "convertMarkdownTables",
    "replaceMermaidWithFigureTokens",
    "LinkedIn launch post",
    "publication_ready",
    "platform-renditions.manifest.json",
]
critical_by_path.setdefault(
    "quartz/publication/thinking-systems.platforms.json",
    {"path": "quartz/publication/thinking-systems.platforms.json", "required_text": []},
)["required_text"] = [
    "\"post_max_characters\": 3000",
    "\"article_max_characters\": 125000",
    "\"width\": 2000",
    "\"image_min_width\": 1192",
]
contract["critical_files"] = list(critical_by_path.values())
write_json(".github/policy/repository-contract-change-coupling.json", contract)

cases_path = ROOT / ".github/tests/repository_contract/cases.json"
cases_manifest = json.loads(cases_path.read_text(encoding="utf-8"))
case_name = "platform rendition workflow deletion is rejected"
if not any(case.get("name") == case_name for case in cases_manifest["cases"]):
    cases_manifest["cases"].append({
        "name": case_name,
        "mutation": {"type": "delete_path", "path": ".github/workflows/export-platform-renditions.yml"},
        "expected_error": "Missing required file: .github/workflows/export-platform-renditions.yml",
    })
write_json(".github/tests/repository_contract/cases.json", cases_manifest)

test_contract_path = ROOT / ".github/tests/repository_contract/test_repository_contract.py"
test_contract = test_contract_path.read_text(encoding="utf-8")
required_case = '    "platform rendition workflow deletion is rejected",\n'
if required_case not in test_contract:
    marker = '    "manual publication export workflow deletion is rejected",\n'
    if marker not in test_contract:
        raise SystemExit("Repository-contract required-case anchor not found")
    test_contract = test_contract.replace(marker, marker + required_case, 1)
test_contract_path.write_text(test_contract, encoding="utf-8")

# Remove the temporary implementation mechanism from the final branch.
for relative in (
    ".github/scripts/build_platform_renditions_pr.py",
    ".github/workflows/build-platform-renditions-pr.yml",
):
    candidate = ROOT / relative
    if candidate.exists():
        candidate.unlink()
