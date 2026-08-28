#!/usr/bin/env node

import { mkdtemp, readFile, rm, stat, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import matter from "gray-matter";
import sharp from "sharp";
import { chromium } from "playwright";
import { buildFigure3ControlledObjectSvg } from "./publication-figure3.mjs";
import {
  currentArticleSource,
  loadPublicationSource,
  locateCanonicalFigure8,
  normalizeDate,
  repoRoot,
  sha256,
} from "./publication-rendition.mjs";
import {
  assertFigure8SemanticSource,
  buildFigure8CapabilitySvg,
  buildFigure8DecisionSvg,
} from "./publication-figure8.mjs";
import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs";
import {
  assertIndependentOutputTarget,
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs";

export const publicationAssetsRoot = path.join(
  repoRoot,
  "dist",
  "publication",
  "thinking-systems",
);
export const publicationSvgRoot = path.join(
  publicationAssetsRoot,
  "figures",
  "svg",
);
export const publicationPngRoot = path.join(
  publicationAssetsRoot,
  "figures",
  "png",
);

const manifestPath = path.join(publicationAssetsRoot, "assets.manifest.json");
const minimumFigureWidth = 1600;
const denseFigureWidth = 2400;
const maximumDenseFigureWidth = 3200;
const desktopDisplayWidth = 1600;
const desktopMinimumLabelPx = 14;
const figure8HardFloorPt = 5;

const heroSpecifications = Object.freeze([
  Object.freeze({
    key: "linkedin_article_cover",
    filename: "cover-linkedin-article.png",
    width: 2000,
    height: 600,
  }),
  Object.freeze({
    key: "social_preview",
    filename: "social-preview.png",
    width: 1200,
    height: 627,
  }),
  Object.freeze({
    key: "medium_hero",
    filename: "medium-hero.png",
    width: 1600,
    height: 840,
  }),
]);

function relative(candidate) {
  return path.relative(repoRoot, candidate).split(path.sep).join("/");
}

function escapeXml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function slugify(value) {
  return String(value)
    .toLowerCase()
    .replace(/&/g, " and ")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}

async function writePublicationAsset(target, bytes, sourcePath) {
  await assertSafeOutputPath(repoRoot, publicationAssetsRoot, target);
  await assertIndependentOutputTarget(target, [sourcePath]);
  await writeFileAtomically(target, bytes, {
    trustedRoot: repoRoot,
    allowedRoot: publicationAssetsRoot,
    forbiddenPaths: [sourcePath],
  });
}

async function pinnedMermaidCliVersion() {
  const contractPath = path.join(
    repoRoot,
    ".github",
    "policy",
    "supply-chain-contract.json",
  );
  const contract = JSON.parse(await readFile(contractPath, "utf8"));
  const version = contract?.tool_versions?.mermaid_cli;
  if (!version) throw new Error("Pinned mermaid-cli version is unavailable");
  return String(version);
}

function parseFigureCaption(tail) {
  const match =
    /^\s*(?:<!--[\s\S]*?-->\s*)*\*\*Figure\s+(\d+)([AB])?\s+—\s+([^*\n]+?)\.\*\*/.exec(
      tail,
    );
  if (!match) return null;
  return {
    number: Number(match[1]),
    panel: match[2] || null,
    title: match[3].trim(),
  };
}

export function extractMermaidFigures(markdown) {
  const content = matter(markdown).content;
  const blockPattern = /```mermaid\r?\n([\s\S]*?)\r?\n```/g;
  const figures = [];
  let match;
  let ordinal = 0;
  while ((match = blockPattern.exec(content)) !== null) {
    ordinal += 1;
    const caption = parseFigureCaption(content.slice(blockPattern.lastIndex));
    const number = caption?.number ?? ordinal;
    const panel = caption?.panel ?? null;
    const title = caption?.title ?? `Figure ${number}`;
    figures.push({
      ordinal,
      number,
      panel,
      title,
      mermaid: match[1],
      basename: panel
        ? `figure-${number}${panel.toLowerCase()}-${slugify(title)}`
        : `figure-${number}-${slugify(title)}`,
    });
  }
  return figures;
}

export function classifyFigureWidth(mermaid) {
  const text = String(mermaid);
  const lines = text.split(/\r?\n/).filter((line) => line.trim());
  const edges = (text.match(/-->|==>|-.->/g) || []).length;
  const nodes = (text.match(/\[[^\]]+\]|\{[^}]+\}/g) || []).length;
  const density =
    lines.length + edges + Math.ceil(nodes / 2) + Math.ceil(text.length / 180);
  if (density >= 42 || text.length >= 1400 || lines.length >= 28) {
    return maximumDenseFigureWidth;
  }
  if (density >= 26 || text.length >= 760 || lines.length >= 16) {
    return denseFigureWidth;
  }
  return minimumFigureWidth;
}

function minimumSvgFontPx(svg) {
  const values = [
    ...String(svg).matchAll(/font-size(?:=|:)\s*["']?([0-9.]+)(?:px)?/gi),
  ]
    .map((match) => Number(match[1]))
    .filter((value) => Number.isFinite(value) && value > 0);
  return values.length > 0 ? Math.min(...values) : null;
}

function viewBoxDimensions(svg) {
  const match =
    /viewBox=["']\s*[0-9.-]+\s+[0-9.-]+\s+([0-9.]+)\s+([0-9.]+)\s*["']/i.exec(
      String(svg),
    );
  if (!match) return null;
  const width = Number(match[1]);
  const height = Number(match[2]);
  if (
    !Number.isFinite(width) ||
    !Number.isFinite(height) ||
    width <= 0 ||
    height <= 0
  ) {
    return null;
  }
  return { width, height };
}

function viewBoxWidth(svg) {
  return viewBoxDimensions(svg)?.width ?? null;
}

export function svgRasterizationPlan(svg, pngWidth) {
  const dimensions = viewBoxDimensions(svg);
  if (!dimensions)
    throw new Error("Publication SVG is missing a valid viewBox");
  return {
    renderer: "chromium",
    width: pngWidth,
    height: Math.max(
      1,
      Math.ceil((pngWidth * dimensions.height) / dimensions.width),
    ),
    contains_foreign_object: /<foreignObject\b/i.test(String(svg)),
    background: "#ffffff",
  };
}

async function rasterizeSvgWithChromium(svgBuffer, pngWidth) {
  const svg = svgBuffer.toString("utf8");
  const plan = svgRasterizationPlan(svg, pngWidth);
  const browser = await chromium.launch({
    headless: true,
    args: ["--no-sandbox", "--disable-setuid-sandbox"],
  });
  try {
    const page = await browser.newPage({
      viewport: {
        width: plan.width,
        height: Math.min(Math.max(plan.height, 600), 16384),
      },
      deviceScaleFactor: 1,
    });
    await page.setContent(
      `<!doctype html><html><head><meta charset="utf-8"/><style>html,body{margin:0;padding:0;background:#fff}#ua-frame{display:inline-block;width:${plan.width}px;background:#fff;line-height:0}#ua-frame>svg{display:block!important;width:100%!important;height:auto!important;max-width:none!important;overflow:visible!important}</style></head><body><div id="ua-frame">${svg}</div></body></html>`,
      { waitUntil: "load" },
    );
    await page.evaluate(async () => {
      if (document.fonts?.ready) await document.fonts.ready;
    });

    const frame = page.locator("#ua-frame");
    const box = await frame.boundingBox();
    if (!box || box.width < 1 || box.height < 1) {
      throw new Error("Chromium could not measure the publication SVG");
    }
    if (plan.contains_foreign_object) {
      const labelsVisible = await page
        .locator("#ua-frame foreignObject")
        .evaluateAll((nodes) =>
          nodes.some((node) => {
            const rect = node.getBoundingClientRect();
            const style = getComputedStyle(node);
            return (
              rect.width > 0 &&
              rect.height > 0 &&
              style.display !== "none" &&
              style.visibility !== "hidden"
            );
          }),
        );
      if (!labelsVisible) {
        throw new Error(
          "Chromium did not expose Mermaid foreignObject labels for rasterization",
        );
      }
    }

    const screenshot = await frame.screenshot({ type: "png" });
    const png = await sharp(screenshot)
      .flatten({ background: plan.background })
      .png({ compressionLevel: 9, adaptiveFiltering: true })
      .toBuffer();
    const metadata = await sharp(png).metadata();
    if (metadata.width !== plan.width) {
      throw new Error(
        `Chromium raster width ${metadata.width} does not match requested ${plan.width}`,
      );
    }
    if (metadata.hasAlpha) {
      throw new Error(
        "Platform PNG must be opaque after white-background flattening",
      );
    }
    return { png, plan, metadata };
  } finally {
    await browser.close();
  }
}

function projectedDesktopLabelPx(svg) {
  const font = minimumSvgFontPx(svg);
  const width = viewBoxWidth(svg);
  if (!font || !width) return null;
  return Number(((font * desktopDisplayWidth) / width).toFixed(2));
}

async function renderMermaidSvg(mermaid, version) {
  const temporary = await mkdtemp(
    path.join(os.tmpdir(), "ua-publication-assets-"),
  );
  try {
    const inputPath = path.join(temporary, "figure.mmd");
    const outputPath = path.join(temporary, "figure.svg");
    const puppeteerPath = path.join(temporary, "puppeteer.json");
    await writeFile(inputPath, `${mermaid.trim()}\n`, "utf8");
    await writeFile(
      puppeteerPath,
      JSON.stringify({ args: ["--no-sandbox", "--disable-setuid-sandbox"] }),
      "utf8",
    );

    await new Promise((resolve, reject) => {
      const child = spawn(
        "npx",
        [
          "--yes",
          `@mermaid-js/mermaid-cli@${version}`,
          "-p",
          puppeteerPath,
          "-i",
          inputPath,
          "-o",
          outputPath,
          "-b",
          "transparent",
          "-t",
          "neutral",
          "--quiet",
        ],
        { cwd: repoRoot, stdio: ["ignore", "pipe", "pipe"] },
      );
      let detail = "";
      child.stderr.on("data", (chunk) => {
        detail += chunk.toString();
      });
      child.once("error", reject);
      child.once("exit", (code) => {
        if (code === 0) resolve();
        else
          reject(
            new Error(`mermaid-cli exited with code ${code}: ${detail.trim()}`),
          );
      });
    });
    return await readFile(outputPath);
  } finally {
    await rm(temporary, { recursive: true, force: true });
  }
}

async function emitFigure({
  figure,
  svgBuffer,
  pngWidth,
  sourcePath,
  semanticFingerprint = null,
}) {
  const svgPath = path.join(publicationSvgRoot, `${figure.basename}.svg`);
  const pngPath = path.join(publicationPngRoot, `${figure.basename}.png`);
  const normalizedSvg = Buffer.from(
    `${svgBuffer.toString("utf8").trim()}\n`,
    "utf8",
  );
  const rasterized = await rasterizeSvgWithChromium(normalizedSvg, pngWidth);
  const pngBuffer = rasterized.png;
  const pngMetadata = rasterized.metadata;
  const desktopLabel = projectedDesktopLabelPx(normalizedSvg.toString("utf8"));

  await writePublicationAsset(svgPath, normalizedSvg, sourcePath);
  await writePublicationAsset(pngPath, pngBuffer, sourcePath);

  return {
    number: figure.number,
    panel: figure.panel,
    title: figure.title,
    category: pngWidth >= denseFigureWidth ? "dense" : "standard",
    svg_path: relative(svgPath),
    svg_sha256: sha256(normalizedSvg),
    png_path: relative(pngPath),
    png_sha256: sha256(pngBuffer),
    png_width: pngMetadata.width,
    png_height: pngMetadata.height,
    png_renderer: rasterized.plan.renderer,
    png_background: rasterized.plan.background,
    png_has_alpha: Boolean(pngMetadata.hasAlpha),
    svg_contains_foreign_object: rasterized.plan.contains_foreign_object,
    desktop_display_width_px: desktopDisplayWidth,
    projected_desktop_minimum_label_px: desktopLabel,
    desktop_no_zoom_floor_px: figure.panel ? desktopMinimumLabelPx : null,
    desktop_no_zoom_floor_met:
      figure.panel && desktopLabel !== null
        ? desktopLabel >= desktopMinimumLabelPx
        : null,
    semantic_fingerprint: semanticFingerprint,
  };
}

function wrapText(value, limit) {
  const lines = [];
  let current = "";
  for (const word of String(value).split(/\s+/).filter(Boolean)) {
    const candidate = current ? `${current} ${word}` : word;
    if (candidate.length > limit && current) {
      lines.push(current);
      current = word;
    } else current = candidate;
  }
  if (current) lines.push(current);
  return lines;
}

function svgText(x, y, lines, size, lineHeight, weight, fill) {
  return `<text x="${x}" y="${y}" font-family="Arial, sans-serif" font-size="${size}" font-weight="${weight}" fill="${fill}">${lines
    .map(
      (line, index) =>
        `<tspan x="${x}" dy="${index === 0 ? 0 : lineHeight}">${escapeXml(line)}</tspan>`,
    )
    .join("")}</text>`;
}

export function buildHeroSvg(specification, publication) {
  const [primary, secondary = "When the Controlled Object Changes"] = String(
    publication.title,
  ).split(/\s+—\s+/, 2);
  const titleLines = wrapText(primary, specification.width >= 1800 ? 32 : 25);
  const subtitleLines = wrapText(
    secondary,
    specification.width >= 1800 ? 42 : 31,
  );
  const padX = Math.round(specification.width * 0.075);
  const titleSize =
    specification.width >= 1800 ? 66 : specification.width >= 1500 ? 56 : 47;
  const subtitleSize = specification.width >= 1800 ? 32 : 27;
  const titleY = Math.round(specification.height * 0.3);
  const meta = [publication.author, publication.date, publication.license]
    .filter(Boolean)
    .join(" · ");

  return `<svg xmlns="http://www.w3.org/2000/svg" width="${specification.width}" height="${specification.height}" viewBox="0 0 ${specification.width} ${specification.height}" role="img" aria-label="${escapeXml(publication.title)}">
<defs><linearGradient id="ua-bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#142129"/><stop offset="55%" stop-color="#254659"/><stop offset="100%" stop-color="#54736d"/></linearGradient></defs>
<rect width="100%" height="100%" fill="url(#ua-bg)"/>
<circle cx="${Math.round(specification.width * 0.88)}" cy="${Math.round(specification.height * 0.18)}" r="${Math.round(specification.height * 0.28)}" fill="#ffffff" opacity="0.055"/>
<circle cx="${Math.round(specification.width * 0.93)}" cy="${Math.round(specification.height * 0.82)}" r="${Math.round(specification.height * 0.34)}" fill="#ffffff" opacity="0.045"/>
<path d="M ${Math.round(specification.width * 0.71)} ${Math.round(specification.height * 0.28)} L ${Math.round(specification.width * 0.79)} ${Math.round(specification.height * 0.18)} L ${Math.round(specification.width * 0.87)} ${Math.round(specification.height * 0.34)} L ${Math.round(specification.width * 0.94)} ${Math.round(specification.height * 0.22)}" fill="none" stroke="#d7e7ee" stroke-width="4" opacity="0.45"/>
<rect x="${padX}" y="${Math.round(specification.height * 0.13)}" width="${Math.round(specification.width * 0.31)}" height="6" rx="3" fill="#8fb1bd"/>
${svgText(padX, Math.round(specification.height * 0.19), ["UNCERTAINTY ARCHITECTURE · RESEARCH PUBLICATION"], specification.width >= 1800 ? 21 : 17, 24, 600, "#d7e7ee")}
${svgText(padX, titleY, titleLines, titleSize, Math.round(titleSize * 1.16), 700, "#ffffff")}
${svgText(padX, titleY + titleLines.length * Math.round(titleSize * 1.16) + 30, subtitleLines, subtitleSize, Math.round(subtitleSize * 1.25), 500, "#edf6f8")}
${svgText(padX, specification.height - 72, [meta], specification.width >= 1800 ? 20 : 17, 22, 500, "#d7e7ee")}
</svg>`;
}

async function renderHeroAssets(source) {
  const authors = Array.isArray(source.data.authors)
    ? source.data.authors
    : source.data.author
      ? [source.data.author]
      : ["Vitalii Oborskyi"];
  const publication = {
    title:
      source.data.title ||
      "Uncertainty Architecture: Thinking Systems — When the Controlled Object Changes",
    author: String(authors[0] || "Vitalii Oborskyi"),
    date: normalizeDate(source.data.publication_date),
    license: String(source.data.license || "CC BY 4.0").replace(
      /^CC-BY-4\.0$/i,
      "CC BY 4.0",
    ),
  };
  const assets = [];
  for (const specification of heroSpecifications) {
    const target = path.join(publicationAssetsRoot, specification.filename);
    const svg = buildHeroSvg(specification, publication);
    const png = await sharp(Buffer.from(svg, "utf8"))
      .png({ compressionLevel: 9, adaptiveFiltering: true })
      .toBuffer();
    await writePublicationAsset(target, png, source.absolute);
    const metadata = await sharp(png).metadata();
    assets.push({
      key: specification.key,
      path: relative(target),
      sha256: sha256(png),
      width: metadata.width,
      height: metadata.height,
    });
  }
  return assets;
}

async function renderFigures(source) {
  const version = await pinnedMermaidCliVersion();
  const canonicalFigures = extractMermaidFigures(source.raw);
  const emitted = [];

  for (const figure of canonicalFigures) {
    if (figure.number === 8) continue;
    if (figure.number === 3) {
      emitted.push(
        await emitFigure({
          figure,
          svgBuffer: Buffer.from(buildFigure3ControlledObjectSvg(), "utf8"),
          pngWidth: denseFigureWidth,
          sourcePath: source.absolute,
        }),
      );
      continue;
    }
    const svg = await renderMermaidSvg(figure.mermaid, version);
    emitted.push(
      await emitFigure({
        figure,
        svgBuffer: svg,
        pngWidth: classifyFigureWidth(figure.mermaid),
        sourcePath: source.absolute,
      }),
    );
  }

  const located = locateCanonicalFigure8(source.content);
  if (!located) throw new Error("Canonical Figure 8 was not found");
  assertFigure8SemanticSource(located.mermaid);
  const canonicalFingerprint = assertCanonicalFigure8Fingerprint(
    located.mermaid,
    located.caption,
  );
  const figure8Panels = [
    {
      number: 8,
      panel: "A",
      title: "Decision-ownership model",
      basename: "figure-8a-decision-ownership-model",
      svg: buildFigure8DecisionSvg(),
      width: maximumDenseFigureWidth,
    },
    {
      number: 8,
      panel: "B",
      title: "Capability-family axis and orthogonality relationship",
      basename:
        "figure-8b-capability-family-axis-and-orthogonality-relationship",
      svg: buildFigure8CapabilitySvg(),
      width: denseFigureWidth,
    },
  ];
  for (const panel of figure8Panels) {
    const asset = await emitFigure({
      figure: panel,
      svgBuffer: Buffer.from(panel.svg, "utf8"),
      pngWidth: panel.width,
      sourcePath: source.absolute,
      semanticFingerprint: canonicalFingerprint,
    });
    if (asset.projected_desktop_minimum_label_px === null) {
      throw new Error(
        `Figure 8${panel.panel} SVG has no measurable label size`,
      );
    }
    if (!asset.desktop_no_zoom_floor_met) {
      throw new Error(
        `Figure 8${panel.panel} projected desktop label ${asset.projected_desktop_minimum_label_px}px is below the ${desktopMinimumLabelPx}px no-zoom floor`,
      );
    }
    emitted.push(asset);
  }

  return emitted.sort((left, right) => {
    if (left.number !== right.number) return left.number - right.number;
    return String(left.panel || "").localeCompare(String(right.panel || ""));
  });
}

export async function buildPublicationAssetsManifest(
  source,
  { now = new Date() } = {},
) {
  const figures = await renderFigures(source);
  const heroes = await renderHeroAssets(source);
  const generatedAt = now.toISOString();
  return {
    schema_version: 1,
    artifact: "publication-platform-assets",
    source_path: source.relative,
    source_content_sha256: sha256(Buffer.from(source.raw)),
    generated_at: generatedAt,
    generated_date: generatedAt.slice(0, 10),
    output_root: relative(publicationAssetsRoot),
    platform_targets: {
      linkedin_article_cover: { width: 2000, height: 600 },
      linkedin_social_preview: { width: 1200, height: 627 },
      medium_hero: { width: 1600, height: 840 },
      minimum_figure_width_px: minimumFigureWidth,
      dense_figure_width_range_px: [denseFigureWidth, maximumDenseFigureWidth],
      desktop_display_width_px: desktopDisplayWidth,
      figure8_desktop_minimum_label_px: desktopMinimumLabelPx,
      figure8_print_hard_floor_pt: figure8HardFloorPt,
    },
    figures,
    heroes,
  };
}

async function main() {
  const source = await loadPublicationSource(currentArticleSource);
  const before = await readFile(source.absolute);
  const manifest = await buildPublicationAssetsManifest(source);
  await writePublicationAsset(
    manifestPath,
    Buffer.from(`${JSON.stringify(manifest, null, 2)}\n`, "utf8"),
    source.absolute,
  );
  const after = await readFile(source.absolute);
  if (!before.equals(after)) {
    throw new Error(
      "Canonical Markdown changed while rendering publication assets",
    );
  }
  for (const asset of [...manifest.figures, ...manifest.heroes]) {
    const target = path.join(repoRoot, asset.png_path || asset.path);
    const info = await stat(target);
    if (!info.isFile() || info.size < 1024) {
      throw new Error(
        `Generated publication asset is missing or too small: ${relative(target)}`,
      );
    }
  }
  console.log(
    `Publication platform assets ready: ${relative(publicationAssetsRoot)} ` +
      `(${manifest.figures.length} figure renditions, ${manifest.heroes.length} hero assets)`,
  );
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Publication asset rendering failed: ${error instanceof Error ? error.message : String(error)}`,
    );
    process.exitCode = 1;
  });
}
