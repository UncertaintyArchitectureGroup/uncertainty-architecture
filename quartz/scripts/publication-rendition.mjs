import { createHash } from "node:crypto";
import {
  mkdtemp,
  readFile,
  realpath,
  rm,
  stat,
  writeFile,
} from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";
import GithubSlugger from "github-slugger";
import {
  assertFigure3SemanticSource,
  buildFigure3ControlledObjectSvg,
} from "./publication-figure3.mjs";
import {
  assertFigure8SemanticSource,
  buildFigure8RenditionAssets,
} from "./publication-figure8.mjs";
import {
  assertCanonicalFigure8Fingerprint,
  canonicalFigure8Fingerprint,
} from "./publication-figure8-fingerprint.mjs";
import { gitOutput } from "./publication-provenance.mjs";

export const repoRoot = path.resolve(
  fileURLToPath(new URL("../..", import.meta.url)),
);
export const contentRoot = path.join(repoRoot, "content");
export const defaultRepository =
  "UncertaintyArchitectureGroup/uncertainty-architecture";
export const currentArticleSource =
  "content/research/notes/thinking-systems-publication-draft.md";
export const workingPaperSource =
  "content/research/notes/open-engineering-specification-article-draft.md";

const curatedPublicationAuthors = new Map([
  [currentArticleSource, ["Vitalii Oborskyi"]],
  [workingPaperSource, ["Vitalii Oborskyi"]],
]);

export { gitOutput };

export function isInside(parent, candidate) {
  const relative = path.relative(parent, candidate);
  return (
    relative === "" ||
    (!relative.startsWith(`..${path.sep}`) &&
      relative !== ".." &&
      !path.isAbsolute(relative))
  );
}

export function run(command, args, options = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: "inherit", ...options });
    child.once("error", reject);
    child.once("exit", (code, signal) => {
      if (code === 0) return resolve();
      reject(
        new Error(
          `${path.basename(command)} exited with ${signal ? `signal ${signal}` : `code ${code}`}`,
        ),
      );
    });
  });
}

export function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

export function sha256(buffer) {
  return createHash("sha256").update(buffer).digest("hex");
}

export function normalizeDate(value) {
  if (!value) return null;
  if (value instanceof Date) return value.toISOString().slice(0, 10);
  const text = String(value).trim();
  const isoPrefix = /^(\d{4}-\d{2}-\d{2})(?:[T\s].*)?$/.exec(text);
  return isoPrefix ? isoPrefix[1] : text;
}

export function normalizeAuthors(value) {
  const entries = Array.isArray(value) ? value : value ? [value] : [];
  return entries
    .map((entry) => {
      if (typeof entry === "string") return entry.trim();
      if (!entry || typeof entry !== "object") return "";
      if (typeof entry.name === "string") return entry.name.trim();
      const given = entry["given-names"] ?? entry.givenNames ?? "";
      const family = entry["family-names"] ?? entry.familyNames ?? "";
      return [given, family].filter(Boolean).join(" ").trim();
    })
    .filter(Boolean);
}

export function resolvePublicationAuthors(data, sourceRelative) {
  const declared = normalizeAuthors(data.authors ?? data.author);
  if (declared.length > 0) return declared;
  return [...(curatedPublicationAuthors.get(sourceRelative) ?? [])];
}

function extractHeadingTitle(content, fallback) {
  const match = content.match(/^#\s+(.+)$/m);
  return match?.[1]?.trim() || fallback;
}

export function humanLicense(value) {
  if (!value) return "CC BY 4.0";
  return String(value).replace(/^CC-BY-4\.0$/i, "CC BY 4.0");
}

export function buildTitlePage({
  data,
  content,
  sourceRelative,
  sourceCommit,
  repository,
  provenance,
}) {
  const title =
    data.title ||
    extractHeadingTitle(content, path.basename(sourceRelative, ".md"));
  const authors = resolvePublicationAuthors(data, sourceRelative);
  const statusParts = [
    ...new Set(
      [data.status, data.maturity, data.draft === true ? "draft" : undefined]
        .filter(Boolean)
        .map(String),
    ),
  ];
  const publicationDate = normalizeDate(data.publication_date);
  const editionDate =
    publicationDate ||
    normalizeDate(data.updated) ||
    normalizeDate(data.created) ||
    new Date().toISOString().slice(0, 10);
  const dateLabel = publicationDate ? "Publication date" : "Edition date";
  const version =
    data.edition ||
    data.version ||
    (data.draft === true ? "Draft" : "Unversioned");
  const repoUrl = `https://github.com/${repository}`;
  const sourceUrl = `${repoUrl}/blob/${encodeURIComponent(sourceCommit)}/${sourceRelative
    .split("/")
    .map(encodeURIComponent)
    .join("/")}`;
  const canonical = data.canonical_url
    ? `<br/><a href="${escapeHtml(data.canonical_url)}">${escapeHtml(data.canonical_url)}</a>`
    : "";
  const authorLine =
    authors.length > 0
      ? authors.join(" · ")
      : "Author not declared in source metadata";
  const dirty = provenance?.state === "dirty-preview";
  const sourceRows = dirty
    ? `<div><dt>Source state</dt><dd>Uncommitted local preview</dd></div>
    <div><dt>Committed baseline SHA</dt><dd><code>${escapeHtml(sourceCommit)}</code></dd></div>
    <div><dt>Working-tree blob SHA</dt><dd><code>${escapeHtml(provenance.workingBlob)}</code></dd></div>`
    : `<div><dt>Source commit SHA</dt><dd><code>${escapeHtml(sourceCommit)}</code></dd></div>`;
  const sourceLinkLabel = dirty
    ? "Committed baseline source — preview differs"
    : "Versioned source";

  return `<section class="ua-pdf-title-page${dirty ? " ua-pdf-title-page--dirty" : ""}">
  <div class="ua-pdf-title-kicker">Uncertainty Architecture · Research Publication</div>
  <h1>${escapeHtml(title)}</h1>
  <p class="ua-pdf-title-author">${escapeHtml(authorLine)}</p>
  ${dirty ? '<p class="ua-pdf-preview-warning"><strong>Uncommitted local preview.</strong> This PDF is not a versioned publication artifact.</p>' : ""}
  <dl class="ua-pdf-title-meta">
    <div><dt>Status</dt><dd>${escapeHtml(statusParts.join(" · ") || "Research")}</dd></div>
    <div><dt>${escapeHtml(dateLabel)}</dt><dd>${escapeHtml(editionDate)}</dd></div>
    <div><dt>Version</dt><dd>${escapeHtml(version)}</dd></div>
    <div><dt>License</dt><dd>${escapeHtml(humanLicense(data.license))}</dd></div>
    ${sourceRows}
  </dl>
  <p class="ua-pdf-title-links"><a href="${escapeHtml(repoUrl)}">${escapeHtml(repoUrl)}</a><br/><a href="${escapeHtml(sourceUrl)}">${escapeHtml(sourceLinkLabel)}</a>${canonical}</p>
</section>`;
}

export function buildToc(content) {
  const slugger = new GithubSlugger();
  const entries = [];
  for (const line of content.split(/\r?\n/)) {
    const match = /^(#{2,3})\s+(.+?)\s*$/.exec(line);
    if (!match) continue;
    const text = match[2]
      .replace(/\[(.*?)\]\([^)]*\)/g, "$1")
      .replace(/[*_`]/g, "")
      .trim();
    entries.push({ level: match[1].length, text, slug: slugger.slug(text) });
  }
  if (entries.length === 0) return "";
  const items = entries
    .map(
      (entry) =>
        `<li class="ua-pdf-toc-level-${entry.level}"><a href="#${escapeHtml(entry.slug)}">${escapeHtml(entry.text)}</a></li>`,
    )
    .join("\n");
  return `<section class="ua-pdf-toc">
  <h2>Contents</h2>
  <ul>
${items}
  </ul>
</section>`;
}

export function compactInlineSvg(svg) {
  return String(svg ?? "")
    .replace(/\r\n/g, "\n")
    .replace(/\r?\n[ \t]*\r?\n/g, "\n")
    .trim();
}

export function locateCanonicalFigure3(content) {
  const blockPattern = /```mermaid\r?\n([\s\S]*?)\r?\n```/g;
  let match;
  while ((match = blockPattern.exec(content)) !== null) {
    const mermaid = match[1];
    if (
      !mermaid.includes(
        "Primarily explicitly authored consequential behavior",
      ) ||
      !mermaid.includes("Motivating class — changed responsibility structure")
    ) {
      continue;
    }
    const tail = content.slice(blockPattern.lastIndex);
    const captionMatch = /^\s*(\*\*Figure 3 —[^\n]*)(?=\n\n|$)/.exec(tail);
    if (!captionMatch) return null;
    const captionStart =
      blockPattern.lastIndex +
      captionMatch.index +
      captionMatch[0].indexOf(captionMatch[1]);
    return {
      start: match.index,
      end: captionStart + captionMatch[1].length,
      mermaid,
      caption: captionMatch[1],
    };
  }
  return null;
}

export function renderFigure3(content) {
  const located = locateCanonicalFigure3(content);
  if (!located) return { content, rendered: false };
  assertFigure3SemanticSource(located.mermaid);
  const svg = compactInlineSvg(buildFigure3ControlledObjectSvg());
  const caption = located.caption.replace(
    /^\*\*(Figure 3 — ?.*?\.)\*\*/,
    "<strong>$1</strong>",
  );
  const panel = `<section class="ua-pdf-static-figure ua-pdf-static-figure--3" data-ua-figure3-rendition="side-by-side">
${svg}
<p>${caption}</p>
</section>`;
  return {
    content: `${content.slice(0, located.start)}${panel}${content.slice(located.end)}`,
    rendered: true,
  };
}

export function assertCurrentArticleFigure3Rendition(rendition) {
  if (!rendition.figure3Rendition) {
    throw new Error(
      "Current Thinking Systems publication requires the reviewed side-by-side Figure 3 rendition.",
    );
  }
  const canonical = rendition.canonicalFigures.filter(
    (figure) => figure.number === 3,
  );
  const rendered = rendition.renditionFigures.filter(
    (figure) => figure.number === 3,
  );
  if (
    canonical.length !== 1 ||
    canonical[0].panel !== null ||
    rendered.length !== 1 ||
    rendered[0].panel !== null
  ) {
    throw new Error(
      "Current publication must preserve exactly one canonical Figure 3 and one rendered Figure 3.",
    );
  }
}

export function locateCanonicalFigure8(content) {
  const blockPattern = /```mermaid\r?\n([\s\S]*?)\r?\n```/g;
  let match;
  while ((match = blockPattern.exec(content)) !== null) {
    const mermaid = match[1];
    if (
      !/\bsubgraph\s+L(?:\[|\s|$)/.test(mermaid) ||
      !/\bsubgraph\s+F(?:\[|\s|$)/.test(mermaid)
    ) {
      continue;
    }
    const tail = content.slice(blockPattern.lastIndex);
    const captionMatch =
      /^\s*(?:<!--[\s\S]*?-->\s*)*(\*\*Figure 8 —[^\n]*)(?=\n\n|$)/.exec(tail);
    if (!captionMatch) return null;
    const captionStart =
      blockPattern.lastIndex +
      captionMatch.index +
      captionMatch[0].indexOf(captionMatch[1]);
    return {
      start: match.index,
      end: captionStart + captionMatch[1].length,
      mermaid,
      caption: captionMatch[1],
    };
  }
  return null;
}

export function splitFigure8(content, { verifyFingerprint = true } = {}) {
  const located = locateCanonicalFigure8(content);
  if (!located) {
    return {
      content,
      split: false,
      fingerprint: null,
      readability: null,
    };
  }
  const { start, end, mermaid, caption } = located;
  assertFigure8SemanticSource(mermaid);
  const fingerprint = verifyFingerprint
    ? assertCanonicalFigure8Fingerprint(mermaid, caption)
    : null;
  const assets = buildFigure8RenditionAssets();

  const canonicalCaption = caption
    .replace(/^\*\*Figure 8 —\s*/, "")
    .replace(/\*\*/, "")
    .trim();
  const panelA = `<section class="ua-pdf-static-figure ua-pdf-static-figure--8a" data-ua-figure8-panel="A">
${compactInlineSvg(assets.decision.svg)}
<p><strong>Figure 8A — Decision-ownership model.</strong> Publication rendition of canonical Figure 8; continue with Figure 8B.</p>
</section>`;
  const panelB = `<section class="ua-pdf-static-figure ua-pdf-static-figure--8b" data-ua-figure8-panel="B">
${compactInlineSvg(assets.capability.svg)}
<p><strong>Figure 8B — Capability-family axis and orthogonality relationship.</strong> Publication rendition of canonical Figure 8.</p>
<p class="ua-pdf-figure8-shared-caption"><strong>Together, Figures 8A–8B preserve canonical Figure 8.</strong> ${escapeHtml(canonicalCaption)}</p>
</section>`;
  return {
    content: `${content.slice(0, start)}${panelA}\n\n${panelB}${content.slice(end)}`,
    split: true,
    fingerprint,
    readability: assets.readability,
  };
}

export function extractFigureList(content) {
  const figures = [];
  const regex =
    /(?:\*\*|<strong>)Figure\s+(\d+)([AB])?\s+—\s+([^*<\n]+?)(?:\.\*\*|\.<\/strong>)/g;
  let match;
  while ((match = regex.exec(content)) !== null) {
    figures.push({
      number: Number(match[1]),
      panel: match[2] || null,
      title: match[3].trim(),
    });
  }
  return figures;
}

export function assertCurrentArticleFigure8Rendition(rendition) {
  if (!rendition.figure8Split) {
    throw new Error(
      "Current Thinking Systems publication requires the reviewed Figure 8A/8B rendition, but canonical Figure 8 was not recognized.",
    );
  }
  const canonicalEight = rendition.canonicalFigures.filter(
    (figure) => figure.number === 8,
  );
  const renderedEight = rendition.renditionFigures.filter(
    (figure) => figure.number === 8,
  );
  const panels = renderedEight.map((figure) => figure.panel).sort();
  if (
    canonicalEight.length !== 1 ||
    canonicalEight[0].panel !== null ||
    renderedEight.length !== 2 ||
    panels[0] !== "A" ||
    panels[1] !== "B"
  ) {
    throw new Error(
      "Current publication must contain exactly one canonical Figure 8 and exactly one reviewed Figure 8A plus one Figure 8B rendition.",
    );
  }
  if (rendition.figure8Fingerprint !== canonicalFigure8Fingerprint) {
    throw new Error(
      "Current publication Figure 8A/8B is not coupled to the reviewed canonical Figure 8 fingerprint.",
    );
  }
  const readability = rendition.figure8Readability;
  if (!readability || !readability.panels?.A || !readability.panels?.B) {
    throw new Error(
      "Current publication Figure 8 readability evidence is missing",
    );
  }
  for (const panel of ["A", "B"]) {
    const result = readability.panels[panel];
    if (
      !result.pdf_hard_floor_met ||
      !result.pdf_preferred_target_met ||
      !result.desktop_readable
    ) {
      throw new Error(
        `Current publication Figure 8${panel} does not meet PDF and desktop readability acceptance`,
      );
    }
  }
}

export async function loadPublicationSource(sourcePath) {
  const requested = path.resolve(repoRoot, sourcePath);
  if (path.extname(requested).toLowerCase() !== ".md") {
    throw new Error("Publication source must have a .md extension");
  }
  const absolute = await realpath(requested);
  if (!isInside(contentRoot, absolute)) {
    throw new Error(
      "Publication source must be a Markdown file under content/",
    );
  }
  if (!(await stat(absolute)).isFile()) {
    throw new Error("Publication source must be a regular Markdown file");
  }
  const raw = await readFile(absolute, "utf8");
  const parsed = matter(raw);
  return {
    absolute,
    relative: path.relative(repoRoot, absolute).split(path.sep).join("/"),
    raw,
    data: parsed.data,
    content: parsed.content,
  };
}

export async function buildPublicationRendition(
  source,
  {
    includeToc = false,
    splitDenseFigures = true,
    sourceCommit: explicitSourceCommit,
    provenance,
    requireFigure8Split = false,
  } = {},
) {
  const repository = process.env.GITHUB_REPOSITORY || defaultRepository;
  const sourceCommit =
    explicitSourceCommit ||
    process.env.UA_PDF_REPOSITORY_REF ||
    process.env.GITHUB_SHA ||
    (await gitOutput(["rev-parse", "HEAD"]));
  const sourceHash = sha256(Buffer.from(source.raw));
  const figure3 = renderFigure3(source.content);
  const transformed = splitDenseFigures
    ? splitFigure8(figure3.content)
    : { content: figure3.content, split: false };
  const titlePage = buildTitlePage({
    data: source.data,
    content: source.content,
    sourceRelative: source.relative,
    sourceCommit,
    repository,
    provenance,
  });
  const toc = includeToc ? buildToc(transformed.content) : "";
  const body = [titlePage, toc, transformed.content]
    .filter(Boolean)
    .join("\n\n");
  const rendered = matter.stringify(body, { ...source.data, draft: true });
  const result = {
    rendered,
    sourceCommit,
    sourceHash,
    authors: resolvePublicationAuthors(source.data, source.relative),
    canonicalFigures: extractFigureList(source.content),
    renditionFigures: extractFigureList(transformed.content),
    figure3Rendition: figure3.rendered,
    figure8Split: transformed.split,
    figure8Fingerprint: transformed.fingerprint,
    figure8Readability: transformed.readability,
  };
  if (requireFigure8Split) {
    assertCurrentArticleFigure3Rendition(result);
    assertCurrentArticleFigure8Rendition(result);
  }
  return result;
}

export async function withTemporaryRendition(source, rendered, action) {
  const directory = path.dirname(source.absolute);
  const scratch = await mkdtemp(
    path.join(os.tmpdir(), "ua-publication-rendition-"),
  );
  const tempName = `ua-publication-render-${process.pid}-${Date.now()}.md`;
  const tempPath = path.join(directory, tempName);
  try {
    await writeFile(tempPath, rendered, "utf8");
    return await action(tempPath, scratch);
  } finally {
    await rm(tempPath, { force: true });
    await rm(scratch, { recursive: true, force: true });
  }
}
