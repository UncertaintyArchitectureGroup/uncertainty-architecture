#!/usr/bin/env node

import { mkdir, rm } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";
import {
  buildFigure8RenditionAssets,
  figure8ReadabilityPolicy,
} from "./publication-figure8.mjs";
import {
  currentArticleSource,
  loadPublicationSource,
  repoRoot,
  splitFigure8,
} from "./publication-rendition.mjs";
import {
  assertSafeOutputPath,
  writeFileAtomically,
} from "./publication-path-safety.mjs";

const visualRoot = path.join(repoRoot, "dist", "pdf", "visual");
const outputDir = path.join(visualRoot, "figure-8");

export const figure8AssetFileNames = Object.freeze({
  A: Object.freeze({
    svg: "figure-8a-decision-ownership.svg",
    png: "figure-8a-decision-ownership.png",
  }),
  B: Object.freeze({
    svg: "figure-8b-capability-orthogonality.svg",
    png: "figure-8b-capability-orthogonality.png",
  }),
});

async function writePanel(panel, asset) {
  const names = figure8AssetFileNames[panel];
  if (!names) throw new Error(`Unsupported Figure 8 panel: ${panel}`);
  const svgPath = path.join(outputDir, names.svg);
  const pngPath = path.join(outputDir, names.png);
  const svgBuffer = Buffer.from(asset.svg);
  const pngBuffer = await sharp(svgBuffer)
    .resize({ width: asset.pngOutputWidthPx })
    .png({ compressionLevel: 9 })
    .toBuffer();
  const metadata = await sharp(pngBuffer).metadata();
  if (metadata.width !== asset.pngOutputWidthPx || !metadata.height) {
    throw new Error(
      `Figure 8${panel} PNG dimensions are invalid: ${metadata.width}x${metadata.height}`,
    );
  }
  await writeFileAtomically(svgPath, svgBuffer, {
    trustedRoot: repoRoot,
    allowedRoot: visualRoot,
  });
  await writeFileAtomically(pngPath, pngBuffer, {
    trustedRoot: repoRoot,
    allowedRoot: visualRoot,
  });
  return {
    svg: path.relative(repoRoot, svgPath).split(path.sep).join("/"),
    png: path.relative(repoRoot, pngPath).split(path.sep).join("/"),
    png_width_px: metadata.width,
    png_height_px: metadata.height,
    png_bytes: pngBuffer.length,
  };
}

async function main() {
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir);
  await rm(outputDir, { recursive: true, force: true });
  await mkdir(outputDir, { recursive: true });
  await assertSafeOutputPath(repoRoot, visualRoot, outputDir);

  const source = await loadPublicationSource(currentArticleSource);
  const split = splitFigure8(source.content);
  if (!split.split || !split.fingerprint || !split.readability) {
    throw new Error(
      "Canonical Figure 8 could not produce the reviewed 8A/8B publication rendition",
    );
  }
  const assets = buildFigure8RenditionAssets();
  const panelA = await writePanel("A", assets.decision);
  const panelB = await writePanel("B", assets.capability);
  const report = {
    schema_version: 1,
    artifact: "figure-8-publication-verification",
    canonical_source: currentArticleSource,
    canonical_fingerprint: split.fingerprint,
    semantics_verified: true,
    policy: figure8ReadabilityPolicy,
    readability: assets.readability,
    panels: {
      A: panelA,
      B: panelB,
    },
    generated_at: new Date().toISOString(),
  };
  const reportPath = path.join(outputDir, "figure-8-verification.json");
  await writeFileAtomically(
    reportPath,
    `${JSON.stringify(report, null, 2)}\n`,
    {
      trustedRoot: repoRoot,
      allowedRoot: visualRoot,
    },
  );
  console.log(
    `Figure 8 publication assets verified: ${path.relative(repoRoot, outputDir)} (8A ${assets.readability.panels.A.effective_pdf_label_pt} pt; 8B ${assets.readability.panels.B.effective_pdf_label_pt} pt)`,
  );
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);
if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      `Figure 8 publication verification failed: ${
        error instanceof Error ? error.message : String(error)
      }`,
    );
    process.exitCode = 1;
  });
}
