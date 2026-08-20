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
      ? authors.join(" Â· ")
      : "Author not declared in source metadata";
  const dirty = provenance?.state === "dirty-preview";
  const sourceRows = dirty
    ? `<div><dt>Source state</dt><dd>Uncommitted local preview</dd></div>
    <div><dt>Committed baseline SHA</dt><dd><code>${escapeHtml(sourceCommit)}</code></dd></div>
    <div><dt>Working-tree blob SHA</dt><dd><code>${escapeHtml(provenance.workingBlob)}</code></dd></div>`
    : `<div><dt>Source commit SHA</dt><dd><code>${escapeHtml(sourceCommit)}</code></dd></div>`;
  const sourceLinkLabel = dirty
    ? "Committed baseline source â€” preview differs"
    : "Versioned source";

  return `<section class="ua-pdf-title-page${dirty ? " ua-pdf-title-page--dirty" : ""}">
  <div class="ua-pdf-title-kicker">Uncertainty Architecture Â· Research Publication</div>
  <h1>${escapeHtml(title)}</h1>
  <p class="ua-pdf-title-author">${escapeHtml(authorLine)}</p>
  ${dirty ? '<p class="ua-pdf-preview-warning"><strong>Uncommitted local preview.</strong> This PDF is not a versioned publication artifact.</p>' : ""}
  <dl class="ua-pdf-title-meta">
    <div><dt>Status</dt><dd>${escapeHtml(statusParts.join(" Â· ") || "Research")}</dd></div>
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

export function locateCanonicalFigur²È="25•ÑÕÉ¸MÑÉ¥¹œ¡ÍÙœ¤¹É•Á±…” ½q¹lqÑt©q¸½œ°€‰q¸ˆ¤ì)ô()•áÁ½ÉÐ™Õ¹Ñ¥½¸ÍÁ±¥Ñ¥ÕÉ”à¡½¹Ñ•¹Ð°ìÙ•É¥™å¥¹•ÉÁÉ¥¹Ð€ôÑÉÕ”ô€ôíô¤ì(€½¹ÍÐ±½…Ñ•€ô±½…Ñ•…¹½¹¥…±¥ÕÉ”à¡½¹Ñ•¹Ð¤ì(€¥˜€ …±½…Ñ•¤ì(€€€É•ÑÕÉ¸ì(€€€€€½¹Ñ•¹Ð°(€€€€€ÍÁ±¥Ðè™…±Í”°(€€€€€™¥¹•ÉÁÉ¥¹Ðè¹Õ±°°(€€€€€É•…‘…‰¥±¥Ñäè¹Õ±°°(€€€ôì(€ô(€½¹ÍÐìÍÑ…ÉÐ°•¹°µ•Éµ…¥°…ÁÑ¥½¸ô€ô±½…Ñ•ì(€…ÍÍ•ÉÑ¥ÕÉ”áM•µ…¹Ñ¥M½ÕÉ”¡µ•Éµ…¥¤ì(€½¹ÍÐ™¥¹•ÉÁÉ¥¹Ð€ôÙ•É¥™å¥¹•ÉÁÉ¥¹Ð(€€€€ü…ÍÍ•ÉÑ…¹½¹¥…±¥ÕÉ”á¥¹•ÉÁÉ¥¹Ð¡µ•Éµ…¥°…ÁÑ¥½¸¤(€€€€è¹Õ±°ì(€½¹ÍÐ…ÍÍ•ÑÌ€ô‰Õ¥±‘¥ÕÉ”áI•¹‘¥Ñ¥½¹ÍÍ•ÑÌ ¤ì((€½¹ÍÐ…¹½¹¥…±…ÁÑ¥½¸€ô…ÁÑ¥½¸(€€€€¹É•Á±…” ½yp©p©¥ÕÉ”€àƒŠQqÌ¨¼°€ˆˆ¤(€€€€¹É•Á±…” ½p©p¨¼°€ˆˆ¤(€€€€¹ÑÉ¥´ ¤ì(€½¹ÍÐÁ…¹•±€ô€ñÍ•Ñ¥½¸±…ÍÌô‰Õ„µÁ‘˜µÍÑ…Ñ¥Œµ™¥ÕÉ”Õ„µÁ‘˜µÍÑ…Ñ¥Œµ™¥ÕÉ”´´á„ˆ‘…Ñ„µÕ„µ™¥ÕÉ”àµÁ…¹•°ô‰ˆø(‘í½µÁ…Ñ%¹±¥¹•MÙœ¡…ÍÍ•ÑÌ¹‘•¥Í¥½¸¹ÍÙœ¥ô(ñÀøñÍÑÉ½¹œù¥ÕÉ”€áƒŠP•¥Í¥½¸µ½Ý¹•ÉÍ¡¥Àµ½‘•°¸ð½ÍÑÉ½¹œøAÕ‰±¥…Ñ¥½¸É•¹‘¥Ñ¥½¸½˜…¹½¹¥…°¥ÕÉ”€àì½¹Ñ¥¹Õ”Ý¥Ñ ¥ÕÉ”€á¸ð½Àø(ð½Í•Ñ¥½¸ù€ì(€½¹ÍÐÁ…¹•±€ô€ñÍ•Ñ¥½¸±…ÍÌô‰Õ„µÁ‘˜µÍÑ…Ñ¥Œµ™¥ÕÉ”Õ„µÁ‘˜µÍÑ…Ñ¥Œµ™¥ÕÉ”´´áˆˆ‘…Ñ„µÕ„µ™¥ÕÉ”àµÁ…¹•°ô‰ˆø(‘í½µÁ…Ñ%¹±¥¹•MÙœ¡…ÍÍ•ÑÌ¹…Á…‰¥±¥Ñä¹ÍÙœ¥ô(ñÀøñÍÑÉ½¹œù¥ÕÉ”€áƒŠP…Á…‰¥±¥Ñäµ™…µ¥±ä…á¥Ì…¹½ÉÑ¡½½¹…±¥ÑäÉ•±…Ñ¥½¹Í¡¥À¸ð½ÍÑÉ½¹œøAÕ‰±¥…Ñ¥½¸É•¹‘¥Ñ¥½¸½˜…¹½¹¥…°¥ÕÉ”€à¸ð½Àø(ñÀ±…ÍÌô‰Õ„µÁ‘˜µ™¥ÕÉ”àµÍ¡…É•µ…ÁÑ¥½¸ˆøñÍÑÉ½¹œùQ½•Ñ¡•È°¥ÕÉ•Ì€áŠLáÁÉ•Í•ÉÙ”…¹½¹¥…°¥ÕÉ”€à¸ð½ÍÑÉ½¹œø€‘í•Í…Á•!Ñµ°¡…¹½¹¥…±…ÁÑ¥½¸¥ôð½Àø(ð½Í•Ñ¥½¸ù€ì(€É•ÑÕÉ¸ì(€€€½¹Ñ•¹Ðè€‘í½¹Ñ•¹Ð¹Í±¥” À°ÍÑ…ÉÐ¥ô‘íÁ…¹•±õq¹q¸‘íÁ…¹•±	ô‘í½¹Ñ•¹Ð¹Í±¥”¡•¹¥õ€°(€€€ÍÁ±¥ÐèÑÉÕ”°(€€€™¥¹•ÉÁÉ¥¹Ð°(€€€É•…‘…‰¥±¥Ñäè…ÍÍ•ÑÌ¹É•…‘…‰¥±¥Ñä°(€ôì)ô()•áÁ½ÉÐ™Õ¹Ñ¥½¸•áÑÉ…Ñ¥ÕÉ•1¥ÍÐ¡½¹Ñ•¹Ð¤ì(€½¹ÍÐ™¥ÕÉ•Ì€ômtì(€½¹ÍÐÉ••à€ô(€€€€¼ üép©p©ðñÍÑÉ½¹œø¥¥ÕÉ•qÌ¬¡q¬¤¡m	t¤ýqÌ¯ŠQqÌ¬¡mx¨ñq¹t¬ü¤ üép¹p©p©ñp¸ñp½ÍÑÉ½¹œø¤½œì(€±•Ðµ…Ñ ì(€Ý¡¥±”€ ¡µ…Ñ €ôÉ••à¹•á•Œ¡½¹Ñ•¹Ð¤¤€„ôô¹Õ±°¤ì(€€€™¥ÕÉ•Ì¹ÁÕÍ ¡ì(€€€€€¹Õµ‰•Èè9Õµ‰•È¡µ…Ñ¡lÅt¤°(€€€€€Á…¹•°èµ…Ñ¡lÉtñð¹Õ±°°(€€€€€Ñ¥Ñ±”èµ…Ñ¡lÍt¹ÑÉ¥´ ¤°(€€€ô¤ì(€ô(€É•ÑÕÉ¸™¥ÕÉ•Ìì)ô()•áÁ½ÉÐ™Õ¹Ñ¥½¸…ÍÍ•ÉÑÕÉÉ•¹ÑÉÑ¥±•¥ÕÉ”ÍI•¹‘¥Ñ¥½¸¡É•¹‘¥Ñ¥½¸¤ì(€¥˜€ …É•¹‘¥Ñ¥½¸¹™¥ÕÉ”ÍI•¹‘¥Ñ¥½¸¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐQ¡¥¹­¥¹œMåÍÑ•µÌÁÕ‰±¥…Ñ¥½¸É•ÅÕ¥É•ÌÑ¡”É•Ù¥•Ý•Í¥‘”µ‰äµÍ¥‘”¥ÕÉ”€ÌÉ•¹‘¥Ñ¥½¸¸ˆ°(€€€€¤ì(€ô(€½¹ÍÐ…¹½¹¥…±Q¡É•”€ôÉ•¹‘¥Ñ¥½¸¹…¹½¹¥…±¥ÕÉ•Ì¹™¥±Ñ•È (€€€€¡™¥ÕÉ”¤€ôø™¥ÕÉ”¹¹Õµ‰•È€ôôô€Ì°(€€¤ì(€½¹ÍÐÉ•¹‘•É•‘Q¡É•”€ôÉ•¹‘¥Ñ¥½¸¹É•¹‘¥Ñ¥½¹¥ÕÉ•Ì¹™¥±Ñ•È (€€€€¡™¥ÕÉ”¤€ôø™¥ÕÉ”¹¹Õµ‰•È€ôôô€Ì°(€€¤ì(€¥˜€ (€€€…¹½¹¥…±Q¡É•”¹±•¹Ñ €„ôô€Äñð(€€€É•¹‘•É•‘Q¡É•”¹±•¹Ñ €„ôô€Äñð(€€€É•¹‘•É•‘Q¡É••lÁt¹Ñ¥Ñ±”€„ôô€‰Q¡”½¹ÑÉ½±±•µ½‰©•ÐÍ¡¥™Ðˆ(€€¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐÁÕ‰±¥…Ñ¥½¸µÕÍÐÁÉ•Í•ÉÙ”½¹”…¹½¹¥…°¥ÕÉ”€Ì…¹½¹”Í¥‘”µ‰äµÍ¥‘”ÁÕ‰±¥…Ñ¥½¸É•¹‘¥Ñ¥½¸¸ˆ°(€€€€¤ì(€ô)ô()•áÁ½ÉÐ™Õ¹Ñ¥½¸…ÍÍ•ÉÑÕÉÉ•¹ÑÉÑ¥±•¥ÕÉ”áI•¹‘¥Ñ¥½¸¡É•¹‘¥Ñ¥½¸¤ì(€¥˜€ …É•¹‘¥Ñ¥½¸¹™¥ÕÉ”áMÁ±¥Ð¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐQ¡¥¹­¥¹œMåÍÑ•µÌÁÕ‰±¥…Ñ¥½¸É•ÅÕ¥É•ÌÑ¡”É•Ù¥•Ý•¥ÕÉ”€á¼áÉ•¹‘¥Ñ¥½¸°‰ÕÐ…¹½¹¥…°¥ÕÉ”€àÝ…Ì¹½ÐÉ•½¹¥é•¸ˆ°(€€€¤ì(€ô(€½¹ÍÐ…¹½¹¥…±¥¡Ð€ôÉ•¹‘¥Ñ¥½¸¹…¹½¹¥…±¥ÕÉ•Ì¹™¥±Ñ•È (€€€€¡™¥ÕÉ”¤€ôø™¥ÕÉ”¹¹Õµ‰•È€ôôô€à°(€€¤ì(€½¹ÍÐÉ•¹‘•É•‘¥¡Ð€ôÉ•¹‘¥Ñ¥½¸¹É•¹‘¥Ñ¥½¹¥ÕÉ•Ì¹™¥±Ñ•È (€€€€¡™¥ÕÉ”¤€ôø™¥ÕÉ”¹¹Õµ‰•È€ôôô€à°(€€¤ì(€½¹ÍÐÁ…¹•±Ì€ôÉ•¹‘•É•‘¥¡Ð¹µ…À ¡™¥ÕÉ”¤€ôø™¥ÕÉ”¹Á…¹•°¤¹Í½ÉÐ ¤ì(€¥˜€ (€€€…¹½¹¥…±¥¡Ð¹±•¹Ñ €„ôô€Äñð(€€€…¹½¹¥…±¥¡ÑlÁt¹Á…¹•°€„ôô¹Õ±°ñð(€€€É•¹‘•É•‘¥¡Ð¹±•¹Ñ €„ôô€Èñð(€€€Á…¹•±ÍlÁt€„ôô€‰ˆñð(€€€Á…¹•±ÍlÅt€„ôô€‰ˆ(€€¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐÁÕ‰±¥…Ñ¥½¸µÕÍÐ½¹Ñ…¥¸•á…Ñ±ä½¹”…¹½¹¥…°¥ÕÉ”€à…¹•á…Ñ±ä½¹”É•Ù¥•Ý•¥ÕÉ”€áÁ±ÕÌ½¹”¥ÕÉ”€áÉ•¹‘¥Ñ¥½¸¸ˆ°(€€€€¤ì(€ô(€¥˜€¡É•¹‘¥Ñ¥½¸¹™¥ÕÉ”á¥¹•ÉÁÉ¥¹Ð€„ôô…¹½¹¥…±¥ÕÉ”á¥¹•ÉÁÉ¥¹Ð¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐÁÕ‰±¥…Ñ¥½¸¥ÕÉ”€á¼á¥Ì¹½Ð½ÕÁ±•Ñ¼Ñ¡”É•Ù¥•Ý•…¹½¹¥…°¥ÕÉ”€à™¥¹•ÉÁÉ¥¹Ð¸ˆ°(€€€€¤ì(€ô(€½¹ÍÐÉ•…‘…‰¥±¥Ñä€ôÉ•¹‘¥Ñ¥½¸¹™¥ÕÉ”áI•…‘…‰¥±¥Ñäì(€¥˜€ …É•…‘…‰¥±¥Ñäñð€…É•…‘…‰¥±¥Ñä¹Á…¹•±Ìü¹ñð€…É•…‘…‰¥±¥Ñä¹Á…¹•±Ìü¹¤ì(€€€Ñ¡É½Ü¹•ÜÉÉ½È (€€€€€€‰ÕÉÉ•¹ÐÁÕ‰±¥…Ñ¥½¸¥ÕÉ”€àÉ•…‘…‰¥±¥Ñä•Ù¥‘•¹”¥Ìµ¥ÍÍ¥¹œˆ°(€€€€¤ì(€ô(€™½È€¡½¹ÍÐÁ…¹•°½˜l‰ˆ°€‰‰t¤ì(€€€½¹ÍÐÉ•ÍÕ±Ð€ôÉ•…‘…‰¥±¥Ñä¹Á…¹•±ÍmÁ…¹•±tì(€€€¥˜€ (€€€€€€…É•ÍÕ±Ð¹Á‘™}¡…É‘}™±½½É}µ•Ðñð(€€€€€€…É•ÍÕ±Ð¹Á‘™}ÁÉ•™•ÉÉ•‘}Ñ…É•Ñ}µ•ÒÇÀ¢&W7VÇBæFW6·F÷÷&VF&ÆP¢’°¢F‡&÷ræWrW'&÷"€¢7W'&VçBV&Æ–6F–öâf–wW&R‚G·æVÇÒFöW2æ÷BÖVWBDbæBFW6·F÷&VF&–Æ—G’66WFæ6VÀ¢“°¢Ð¢Ð§Ð ¦W‡÷'B7–æ2gVæ7F–öâÆöEV&Æ–6F–öå6÷W&6R‡6÷W&6UF‚’°¢6öç7B&WVW7FVBÒF‚ç&W6öÇfR‡&Wõ&ö÷BÂ6÷W&6UF‚“°¢–b‡F‚æW‡FæÖR‡&WVW7FVB’çFôÆ÷vW$66R‚’ÓÒ"æÖB"’°¢F‡&÷ræWrW'&÷"‚%V&Æ–6F–öâ6÷W&6R×W7B†fRæÖBW‡FVç6–öâ"“°¢Ð¢6öç7B'6öÇWFRÒv—B&VÇF‚‡&WVW7FVB“°¢–b‚—4–ç6–FR†6öçFVçE&ö÷BÂ'6öÇWFR’’°¢F‡&÷ræWrW'&÷"€¢%V&Æ–6F–öâ6÷W&6R×W7B&RÖ&¶F÷vâf–ÆRVæFW"6öçFVçBò"À¢“°¢Ð¢–b‚†v—B7FB†'6öÇWFR’’æ—4f–ÆR‚’’°¢F‡&÷ræWrW'&÷"‚%V&Æ–6F–öâ6÷W&6R×W7B&R&VwVÆ"Ö&¶F÷vâf–ÆR"“°¢Ð¢6öç7B&rÒv—B&VDf–ÆR†'6öÇWFRÂ'WFc‚"“°¢6öç7B'6VBÒÖGFW"‡&r“°¢&WGW&â°¢'6öÇWFRÀ¢&VÆF—fS¢F‚ç&VÆF—fR‡&Wõ&ö÷BÂ'6öÇWFR’ç7Æ—B‡F‚ç6W’æ¦ö–â‚"ò"’À¢&rÀ¢FF¢'6VBæFFÀ¢6öçFVçC¢'6VBæ6öçFVçBÀ¢Ó°§Ð ¦W‡÷'B7–æ2gVæ7F–öâ'V–ÆEV&Æ–6F–öå&VæF—F–öâ€¢6÷W&6RÀ¢°¢–æ6ÇVFUFö2ÒfÇ6RÀ¢7Æ—DFVç6Tf–wW&W2ÒG'VRÀ¢6÷W&6T6öÖÖ—C¢W‡Æ–6—E6÷W&6T6öÖÖ—BÀ¢&÷fVææ6RÀ¢&WV—&Tf–wW&S…7Æ—BÒfÇ6RÀ¢ÒÒ·ÒÀ¢’°¢6öç7B&W÷6—F÷'’Ò&ö6W72æVçbät•D…T%õ$Uõ4•Dõ%’ÇÂFVfVÇE&W÷6—F÷'“°¢6öç7B6÷W&6T6öÖÖ—BÐ¢W‡Æ–6—E6÷W&6T6öÖÖ—BÇÀ¢&ö6W72æVçbåTõDeõ$Uõ4•Dõ%•õ$TbÇÀ¢&ö6W72æVçbät•D…T%õ4„ÇÀ¢†v—Bv—D÷WGWB…²'&Wb×'6R"Â$„TB%Ò’“°¢6öç7B6÷W&6T†6‚Ò6†#Sb„'VffW"æg&öÒ‡6÷W&6Rç&r’“°¢6öç7Bf–wW&S2Ò7Æ—DFVç6Tf–wW&W0¢ò&VæFW$f–wW&S2‡6÷W&6Ræ6öçFVçB¢¢²6öçFVçC¢6÷W&6Ræ6öçFVçBÂ&VæFW&VC¢fÇ6RÓ°¢6öç7BG&ç6f÷&ÖVBÒ7Æ—DFVç6Tf–wW&W2(€€€€üÍÁ±¥Ñ¥ÕÉ”à¡™¥ÕÉ”Ì¹½¹Ñ•¹Ð¤(€€€€èì½¹Ñ•¹Ðè™¥ÕÉ”Ì¹½¹Ñ•¹Ð°ÍÁ±¥Ðè™…±Í”ôì(€½¹ÍÐÑ¥Ñ±•A…”€ô‰Õ¥±‘Q¥Ñ±•A…”¡ì(€€€‘…Ñ„èÍ½ÕÉ”¹‘…Ñ„°(€€€½¹Ñ•¹ÐèÍ½ÕÉ”¹½¹Ñ•¹Ð°(€€€Í½ÕÉ•I•±…Ñ¥Ù”èÍ½ÕÉ”¹É•±…Ñ¥Ù”°(€€€Í½ÕÉ•½µµ¥Ð°(€€€É•Á½Í¥Ñ½Éä°(€€€ÁÉ½Ù•¹…¹”°(€ô¤ì(€½¹ÍÐÑ½Œ€ô¥¹±Õ‘•Q½Œ€ü‰Õ¥±‘Q½Œ¡ÑÉ…¹Í™½Éµ•¹½¹Ñ•¹Ð¤€è€ˆˆì(€½¹ÍÐ‰½‘ä€ômÑ¥Ñ±•A…”°Ñ½Œ°ÑÉ…¹Í™½Éµ•¹½¹Ñ•¹Ñt(€€€€¹™¥±Ñ•È¡	½½±•…¸¤(€€€€¹©½¥¸ ‰q¹q¸ˆ¤ì(€½¹ÍÐÉ•¹‘•É•€ôµ…ÑÑ•È¹ÍÑÉ¥¹¥™ä¡‰½‘ä°ì€¸¸¹Í½ÕÉ”¹‘…Ñ„°‘É…™ÐèÑÉÕ”ô¤ì(€½¹ÍÐÉ•ÍÕ±Ð€ôì(€€€É•¹‘•É•°(€€€Í½ÕÉ•½µµ¥Ð°(€€€Í½ÕÉ•!…Í °(€€€…ÕÑ¡½ÉÌèÉ•Í½±Ù•AÕ‰±¥…Ñ¥½¹ÕÑ¡½ÉÌ¡Í½ÕÉ”¹‘…Ñ„°Í½ÕÉ”¹É•±…Ñ¥Ù”¤°(€€€…¹½¹¥…±¥ÕÉ•Ìè•áÑÉ…Ñ¥ÕÉ•1¥ÍÐ¡Í½ÕÉ”¹½¹Ñ•¹Ð¤°(€€€É•¹‘¥Ñ¥½¹¥ÕÉ•Ìè•áÑÉ…Ñ¥ÕÉ•1¥ÍÐ¡ÑÉ…¹Í™½Éµ•¹½¹Ñ•¹Ð¤°(€€€™¥ÕÉ”ÍI•¹‘¥Ñ¥½¸è™¥ÕÉ”Ì¹É•¹‘•É•°(€€€™¥ÕÉ”áMÁ±¥ÐèÑÉ…¹Í™½Éµ•¹ÍÁ±¥Ð°(€€€™¥ÕÉ”á¥¹•ÉÁÉ¥¹ÐèÑÉ…¹Í™½Éµ•¹™¥¹•ÉÁÉ¥¹Ð°(€€€™¥ÕÉ”áI•…‘…‰¥±¥ÑäèÑÉ…¹Í™½Éµ•¹É•…‘…‰¥±¥Ñä°(€ôì(€¥˜€¡É•ÅÕ¥É•¥ÕÉ”áMÁ±¥Ð¤ì(€€€…ÍÍ•ÉÑÕÉÉ•¹ÑÉÑ¥±•¥ÕÉ”ÍI•¹‘¥Ñ¥½¸¡É•ÍÕ±Ð¤ì(€€€…ÍÍ•ÉÑÕÉÉ•¹ÑÉÑ¥±•¥ÕÉ”áI•¹‘¥Ñ¥½¸¡É•ÍÕ±Ð¤ì(€ô(€É•ÑÕÉ¸É•ÍÕ±Ðì)ô()•áÁ½ÉÐ…Íå¹Œ™Õ¹Ñ¥½¸Ý¥Ñ¡Q•µÁ½É…ÉåI•¹‘¥Ñ¥½¸¡Í½ÕÉ”°É•¹‘•É•°…Ñ¥½¸¤ì(€½¹ÍÐ‘¥É•Ñ½Éä€ôÁ…Ñ ¹‘¥É¹…µ”¡Í½ÕÉ”¹…‰Í½±ÕÑ”¤ì(€½¹ÍÐÍÉ…Ñ €ô…Ý…¥Ðµ­‘Ñ•µÀ (€€€Á…Ñ ¹©½¥¸¡½Ì¹ÑµÁ‘¥È ¤°€‰Õ„µÁÕ‰±¥…Ñ¥½¸µÉ•¹‘¥Ñ¥½¸´ˆ¤°(€€¤ì(€½¹ÍÐÑ•µÁ9…µ”€ôÕ„µÁÕ‰±¥…Ñ¥½¸µÉ•¹‘•È´‘íÁÉ½•ÍÌ¹Á¥‘ô´‘í…Ñ”¹¹½Ü ¥ô¹µ‘€ì(€½¹ÍÐÑ•µÁA…Ñ €ôÁ…Ñ ¹©½¥¸¡‘¥É•Ñ½Éä°Ñ•µÁ9…µ”¤ì(€ÑÉäì(€€€…Ý…¥ÐÝÉ¥Ñ•¥±”¡Ñ•µÁA…Ñ °É•¹‘•É•°€‰ÕÑ˜àˆ¤ì(€€€É•ÑÕÉ¸…Ý…¥Ð…Ñ¥½¸¡Ñ•µÁA…Ñ °ÍÉ…Ñ ¤ì(€ô™¥¹…±±äì(€€€…Ý…¥ÐÉ´¡Ñ•µÁA…Ñ °ì™½É”èÑÉÕ”ô¤ì(€€€…Ý…¥ÐÉ´¡ÍÉ…Ñ °ìÉ•ÕÉÍ¥Ù”èÑÉÕ”°™½É”èÑÉÕ”ô¤ì(€ô)ô(