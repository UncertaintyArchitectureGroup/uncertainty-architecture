#!/usr/bin/env node

import { createReadStream } from "node:fs";
import {
  lstat,
  mkdir,
  mkdtemp,
  open,
  readFile,
  realpath,
  rename,
  rm,
  stat,
} from "node:fs/promises";
import http from "node:http";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";
import { globby } from "globby";
import matter from "gray-matter";
import { chromium } from "playwright";
import { assertSafeOutputPath } from "./publication-path-safety.mjs";

const repoRoot = path.resolve(fileURLToPath(new URL("../..", import.meta.url)));
const contentRoot = path.join(repoRoot, "content");
const pdfOutputRoot = path.join(repoRoot, "dist", "pdf");
const minimumPdfBytes = 1024;
const minimumDiagramLabelPoints = 5;
const defaultGitHubRepository =
  "UncertaintyArchitectureGroup/uncertainty-architecture";

function usage() {
  console.log(
    [
      "Usage:",
      "  npm run pdf -- <content/file.md> [--output <file.pdf>]",
      "",
      "Examples:",
      "  npm run pdf -- content/research/notes/example.md",
      "  npm run pdf -- content/research/notes/example.md --output dist/pdf/example.pdf",
      "",
    ].join("\n"),
  );
}

function parseArgs(argv) {
  let source;
  let output;

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];
    if (value === "--help" || value === "-h") return { help: true };
    if (value === "--output" || value === "-o") {
      output = argv[index + 1];
      if (!output) throw new Error(value + " requires a path");
      index += 1;
      continue;
    }
    if (value.startsWith("-")) throw new Error("Unknown option: " + value);
    if (source) throw new Error("Unexpected argument: " + value);
    source = value;
  }

  return { source, output, help: false };
}

function normalizePublicationAuthors(value) {
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

function extractPublicationMetadata(markdownSource) {
  const parsed = matter(markdownSource);
  return {
    authors: normalizePublicationAuthors(
      parsed.data.authors ?? parsed.data.author,
    ),
  };
}

function defaultPdfOutputPath(sourcePath, options = {}) {
  const sourceRoot = path.resolve(options.contentRoot ?? contentRoot);
  const outputRoot = path.resolve(options.outputRoot ?? pdfOutputRoot);
  const resolvedSource = path.resolve(sourcePath);
  if (!isInside(sourceRoot, resolvedSource)) {
    throw new Error("The source must be under content/");
  }

  const relative = path.relative(sourceRoot, resolvedSource);
  const extension = path.extname(relative);
  const relativePdf = relative.slice(0, -extension.length) + ".pdf";
  return path.join(outputRoot, relativePdf);
}

function isInside(parent, candidate) {
  const relative = path.relative(parent, candidate);
  return (
    relative === "" ||
    (!relative.startsWith(".." + path.sep) &&
      relative !== ".." &&
      !path.isAbsolute(relative))
  );
}

function run(command, args, options = {}) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { stdio: "inherit", ...options });
    child.once("error", reject);
    child.once("exit", (code, signal) => {
      if (code === 0) return resolve();
      reject(
        new Error(
          path.basename(command) +
            " exited with " +
            (signal ? "signal " + signal : "code " + code),
        ),
      );
    });
  });
}

function contentType(filePath) {
  const extension = path.extname(filePath).toLowerCase();
  return (
    {
      ".css": "text/css; charset=utf-8",
      ".html": "text/html; charset=utf-8",
      ".ico": "image/x-icon",
      ".jpeg": "image/jpeg",
      ".jpg": "image/jpeg",
      ".js": "text/javascript; charset=utf-8",
      ".json": "application/json; charset=utf-8",
      ".map": "application/json; charset=utf-8",
      ".png": "image/png",
      ".svg": "image/svg+xml",
      ".webp": "image/webp",
      ".woff": "font/woff",
      ".woff2": "font/woff2",
    }[extension] ?? "application/octet-stream"
  );
}

async function statIfExists(filePath, operation = stat) {
  try {
    return await operation(filePath);
  } catch (error) {
    if (error?.code === "ENOENT") return undefined;
    throw error;
  }
}

async function existingFile(candidate) {
  const info = await statIfExists(candidate);
  return info?.isFile() ? candidate : undefined;
}

async function validateOutputTarget(sourcePath, outputPath, options = {}) {
  const resolvedSource = path.resolve(sourcePath);
  const resolvedOutput = path.resolve(outputPath);
  const allowedOutputRoot = path.resolve(options.outputRoot ?? pdfOutputRoot);

  if (path.extname(resolvedOutput).toLowerCase() !== ".pdf") {
    throw new Error("The output path must have a .pdf extension");
  }
  if (resolvedOutput === resolvedSource) {
    throw new Error(
      "The PDF output must be different from the Markdown source",
    );
  }
  if (!isInside(allowedOutputRoot, resolvedOutput)) {
    throw new Error("The PDF output must be under dist/pdf/");
  }
  const trustedRoot = options.trustedRoot ??
    (options.outputRoot ? allowedOutputRoot : repoRoot);
  await assertSafeOutputPath(trustedRoot, allowedOutputRoot, resolvedOutput);

  const [sourceInfo, outputInfo, outputLinkInfo] = await Promise.all([
    stat(resolvedSource),
    statIfExists(resolvedOutput),
    statIfExists(resolvedOutput, lstat),
  ]);

  if (
    outputInfo &&
    sourceInfo.dev === outputInfo.dev &&
    sourceInfo.ino === outputInfo.ino
  ) {
    throw new Error("The PDF output resolves to the Markdown source");
  }
  if (outputLinkInfo?.isSymbolicLink()) {
    throw new Error("The PDF output must not be a symbolic link");
  }
  if (outputLinkInfo && !outputLinkInfo.isFile()) {
    throw new Error("The PDF output must be a regular file");
  }
}

async function assertUsablePdf(pdfPath) {
  const info = await stat(pdfPath);
  if (!info.isFile() || info.size < minimumPdfBytes) {
    throw new Error("Chromium did not produce a usable PDF");
  }

  const handle = await open(pdfPath, "r");
  try {
    const header = Buffer.alloc(5);
    await handle.read(header, 0, header.length, 0);
    if (header.toString("ascii") !== "%PDF-") {
      throw new Error("Chromium output is not a PDF file");
    }

    const tailLength = Math.min(info.size, 2048);
    const tail = Buffer.alloc(tailLength);
    await handle.read(tail, 0, tail.length, info.size - tailLength);
    if (!tail.includes(Buffer.from("%%EOF"))) {
      throw new Error("Chromium output is an incomplete PDF file");
    }
  } finally {
    await handle.close();
  }

  return info;
}

async function withAtomicPdfOutput(outputPath, render, options = {}) {
  const outputDirectory = path.dirname(outputPath);
  const allowedOutputRoot = path.resolve(
    options.outputRoot ??
      (isInside(pdfOutputRoot, outputPath) ? pdfOutputRoot : outputDirectory),
  );
  const trustedRoot = path.resolve(
    options.trustedRoot ??
      (isInside(pdfOutputRoot, outputPath) ? repoRoot : allowedOutputRoot),
  );
  await assertSafeOutputPath(trustedRoot, allowedOutputRoot, outputPath);
  await mkdir(outputDirectory, { recursive: true });
  await assertSafeOutputPath(trustedRoot, allowedOutputRoot, outputPath);
  const stagingDirectory = await mkdtemp(
    path.join(outputDirectory, ".ua-pdf-stage-"),
  );
  const stagedPath = path.join(stagingDirectory, path.basename(outputPath));

  try {
    await render(stagedPath);
    const info = await assertUsablePdf(stagedPath);
    await rename(stagedPath, outputPath);
    return info;
  } finally {
    await rm(stagingDirectory, { recursive: true, force: true });
  }
}

async function resolveStaticFile(root, pathname) {
  let decoded;
  try {
    decoded = decodeURIComponent(pathname);
  } catch {
    return undefined;
  }

  const relative = decoded.replace(/^\/+/, "");
  let candidate = path.resolve(root, relative);
  if (!isInside(root, candidate)) return undefined;

  try {
    const info = await stat(candidate);
    if (info.isDirectory()) candidate = path.join(candidate, "index.html");
  } catch {
    const htmlCandidate = candidate + ".html";
    if (await existingFile(htmlCandidate)) return htmlCandidate;
    return undefined;
  }

  return existingFile(candidate);
}

async function startStaticServer(root) {
  const server = http.createServer(async (request, response) => {
    try {
      const requestUrl = new URL(request.url ?? "/", "http://127.0.0.1");
      const filePath = await resolveStaticFile(root, requestUrl.pathname);
      if (!filePath) {
        response.writeHead(404, {
          "content-type": "text/plain; charset=utf-8",
        });
        response.end("Not found");
        return;
      }

      response.writeHead(200, { "content-type": contentType(filePath) });
      createReadStream(filePath).pipe(response);
    } catch (error) {
      response.writeHead(500, { "content-type": "text/plain; charset=utf-8" });
      response.end(error instanceof Error ? error.message : String(error));
    }
  });

  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });

  const address = server.address();
  if (!address || typeof address === "string") {
    server.close();
    throw new Error("Unable to determine the local preview port");
  }

  return {
    origin: "http://127.0.0.1:" + address.port,
    close: () =>
      new Promise((resolve, reject) =>
        server.close((error) => (error ? reject(error) : resolve())),
      ),
  };
}

async function resolveBuiltPage(siteDir, sourcePath) {
  const contentIndexPath = path.join(siteDir, "static", "contentIndex.json");
  const contentIndex = JSON.parse(await readFile(contentIndexPath, "utf8"));
  const sourceRelativeToContent = path
    .relative(contentRoot, sourcePath)
    .split(path.sep)
    .join("/");
  const entry = Object.values(contentIndex).find(
    (candidate) => candidate.filePath === sourceRelativeToContent,
  );

  if (!entry?.slug || typeof entry.slug !== "string") {
    throw new Error(
      "Quartz did not index the requested source: " +
        path.relative(repoRoot, sourcePath),
    );
  }

  const htmlPath = path.resolve(siteDir, ...entry.slug.split("/")) + ".html";
  if (!isInside(siteDir, htmlPath) || !(await existingFile(htmlPath))) {
    throw new Error(
      "Quartz did not emit the expected page: " +
        path.relative(repoRoot, htmlPath),
    );
  }

  return { contentIndex, htmlPath, slug: entry.slug };
}

function encodeRepositoryPath(filePath) {
  return filePath.split("/").map(encodeURIComponent).join("/");
}

function slugifyRepositoryPath(filePath) {
  let relativePath = filePath.replaceAll("\\", "/").replace(/^\/+|\/+$/g, "");
  if (relativePath.startsWith("content/")) {
    relativePath = relativePath.slice("content/".length);
  }

  const extension = path.posix.extname(relativePath).toLowerCase();
  if (extension === ".md" || extension === ".html") {
    relativePath = relativePath.slice(0, -extension.length);
  }

  let slug = relativePath
    .split("/")
    .map((segment) =>
      segment
        .replace(/\s/g, "-")
        .replace(/&/g, "-and-")
        .replace(/%/g, "-percent")
        .replace(/[?#]/g, ""),
    )
    .join("/")
    .replace(/\/$/, "");

  if (slug.endsWith("/_index")) slug = slug.replace(/\/_index$/, "/index");
  if (slug === "_index") slug = "index";
  return slug;
}

function publicationPathForSlug(slug) {
  if (slug === "index") return "";
  if (slug.endsWith("/index")) return slug.slice(0, -"index".length);
  return slug;
}

function buildDurableLinkTargets(contentIndex, repositoryFiles, options = {}) {
  const repository = options.repository ?? defaultGitHubRepository;
  const reference = options.reference ?? "main";
  const repositoryBase =
    "https://github.com/" +
    repository +
    "/blob/" +
    encodeURIComponent(reference) +
    "/";
  const targets = {};

  for (const repositoryPath of repositoryFiles) {
    const slug = slugifyRepositoryPath(repositoryPath);
    if (!slug) continue;
    targets[slug] = repositoryBase + encodeRepositoryPath(repositoryPath);
  }

  for (const entry of Object.values(contentIndex)) {
    if (!entry?.slug || !entry?.filePath) continue;
    if (options.publicationBaseUrl) {
      const base = new URL(
        options.publicationBaseUrl.endsWith("/")
          ? options.publicationBaseUrl
          : options.publicationBaseUrl + "/",
      );
      const publicationPath = publicationPathForSlug(entry.slug)
        .split("/")
        .filter(Boolean)
        .map(encodeURIComponent)
        .join("/");
      targets[entry.slug] = new URL(publicationPath, base).href;
    } else {
      targets[entry.slug] =
        repositoryBase + encodeRepositoryPath("content/" + entry.filePath);
    }
  }

  return targets;
}

function planDurableLinkRewrites(
  links,
  { currentPageUrl, currentSlug, linkTargets },
) {
  const pageUrl = new URL(currentPageUrl);
  const rewrites = [];

  links.forEach((link, index) => {
    const href = link.href ?? "";
    if (href.startsWith("#")) return;

    let resolved;
    try {
      resolved = new URL(href, pageUrl);
    } catch {
      return;
    }

    if (!["http:", "https:"].includes(resolved.protocol)) return;
    if (resolved.origin !== pageUrl.origin) return;

    const dataSlug = link.dataSlug;
    if (dataSlug === currentSlug) {
      rewrites.push({ index, href: resolved.hash || "#" });
      return;
    }

    if (dataSlug) {
      const durableTarget = linkTargets[dataSlug];
      if (!durableTarget) {
        throw new Error(
          "Unable to make internal publication link durable: " +
            href +
            " (slug: " +
            dataSlug +
            ")",
        );
      }
      const target = new URL(durableTarget);
      target.hash = resolved.hash;
      rewrites.push({ index, href: target.href });
      return;
    }

    if (resolved.pathname === pageUrl.pathname && resolved.hash) {
      rewrites.push({ index, href: resolved.hash });
      return;
    }

    throw new Error("Unable to make local publication link durable: " + href);
  });

  return rewrites;
}

function assertMainDocumentResponse(response, requestedUrl) {
  if (!response) {
    throw new Error("Browser received no response for " + requestedUrl);
  }
  if (!response.ok()) {
    throw new Error(
      "Quartz page returned HTTP " +
        response.status() +
        " " +
        response.statusText(),
    );
  }

  const responseContentType = response.headers()["content-type"] ?? "";
  if (!responseContentType.toLowerCase().includes("text/html")) {
    throw new Error(
      "Quartz page returned unexpected content type: " +
        (responseContentType || "unknown"),
    );
  }
}

function isCriticalResource(request, localOrigin) {
  const resourceType = request.resourceType();
  if (["stylesheet", "font", "image"].includes(resourceType)) return true;
  if (resourceType !== "script") return false;

  const requestUrl = new URL(request.url());
  return (
    requestUrl.origin === localOrigin ||
    (requestUrl.hostname === "cdnjs.cloudflare.com" &&
      requestUrl.pathname.includes("/mermaid/"))
  );
}

function monitorCriticalResources(page, localOrigin) {
  const failures = [];

  const onRequestFailed = (request) => {
    if (!isCriticalResource(request, localOrigin)) return;
    failures.push(
      request.resourceType() +
        " " +
        request.url() +
        ": " +
        (request.failure()?.errorText ?? "request failed"),
    );
  };

  const onResponse = (response) => {
    const request = response.request();
    if (isCriticalResource(request, localOrigin) && response.status() >= 400) {
      failures.push(
        request.resourceType() +
          " " +
          response.url() +
          ": HTTP " +
          response.status(),
      );
    }
  };

  page.on("requestfailed", onRequestFailed);
  page.on("response", onResponse);

  return {
    assertClean() {
      if (failures.length > 0) {
        throw new Error(
          "Publication has failed critical resources:\n" +
            [...new Set(failures)].join("\n"),
        );
      }
    },
    dispose() {
      page.off("requestfailed", onRequestFailed);
      page.off("response", onResponse);
    },
  };
}

function assertFontsLoaded({ fontChecks, failedFontFaces }) {
  const unavailable = fontChecks.filter(
    (check) => check.error || check.loadedFaces === 0,
  );
  if (unavailable.length > 0 || failedFontFaces.length > 0) {
    throw new Error(
      "Publication fonts failed to load: " +
        JSON.stringify({ unavailable, failedFontFaces }),
    );
  }
}

async function waitForPublicationRender(page) {
  await page.waitForFunction(
    () => {
      const diagrams = Array.from(document.querySelectorAll("code.mermaid"));
      const diagramsReady = diagrams.every((node) => {
        const svg = node.querySelector("svg");
        if (!svg || node.getAttribute("data-processed") !== "true")
          return false;
        const box = svg.getBoundingClientRect();
        return box.width > 1 && box.height > 1;
      });
      const imagesReady = Array.from(document.images).every(
        (image) => image.complete,
      );
      return document.readyState === "complete" && diagramsReady && imagesReady;
    },
    undefined,
    { timeout: 30_000 },
  );

  const status = await page.evaluate(async () => {
    if (!document.fonts) {
      return {
        diagrams: document.querySelectorAll("code.mermaid").length,
        brokenImages: [],
        fontChecks: [
          { variable: "document.fonts", error: "Font Loading API unavailable" },
        ],
        failedFontFaces: [],
      };
    }

    const rootStyle = getComputedStyle(document.documentElement);
    const fontChecks = [];
    for (const variable of ["--headerFont", "--bodyFont", "--codeFont"]) {
      const specification = rootStyle.getPropertyValue(variable).trim();
      if (!specification) {
        fontChecks.push({ variable, error: "missing CSS font variable" });
        continue;
      }

      try {
        const faces = await document.fonts.load(
          "400 12px " + specification,
          "UA PDF font verification Aa0",
        );
        fontChecks.push({
          variable,
          specification,
          loadedFaces: faces.filter((face) => face.status === "loaded").length,
        });
      } catch (error) {
        fontChecks.push({ variable, specification, error: String(error) });
      }
    }

    await document.fonts.ready;
    await new Promise((resolve) =>
      requestAnimationFrame(() =>
        requestAnimationFrame(() => setTimeout(resolve, 500)),
      ),
    );

    const failedFontFaces = Array.from(document.fonts)
      .filter((face) => face.status === "error")
      .map((face) => face.family + " " + face.weight + " " + face.style);
    const brokenImages = Array.from(document.images)
      .filter((image) => image.naturalWidth === 0)
      .map((image) => image.currentSrc || image.src);

    return {
      diagrams: document.querySelectorAll("code.mermaid").length,
      brokenImages,
      fontChecks,
      failedFontFaces,
    };
  });

  if (status.brokenImages.length > 0) {
    throw new Error(
      "Publication contains unloaded images: " + status.brokenImages.join(", "),
    );
  }
  assertFontsLoaded(status);
  return status;
}

async function rewritePublicationLinks(
  page,
  { currentPageUrl, currentSlug, linkTargets },
) {
  const articleLinks = page.locator("article a[href]");
  const links = await articleLinks.evaluateAll((anchors) =>
    anchors.map((anchor) => ({
      href: anchor.getAttribute("href") ?? "",
      dataSlug: anchor.getAttribute("data-slug") ?? undefined,
    })),
  );
  const rewrites = planDurableLinkRewrites(links, {
    currentPageUrl,
    currentSlug,
    linkTargets,
  });

  await articleLinks.evaluateAll((anchors, plannedRewrites) => {
    for (const rewrite of plannedRewrites) {
      anchors[rewrite.index].setAttribute("href", rewrite.href);
    }
  }, rewrites);

  return rewrites.length;
}

async function injectPublicationMetadata(page, metadata = {}) {
  const authors = Array.isArray(metadata.authors) ? metadata.authors : [];
  if (authors.length === 0) return false;

  return page.evaluate(({ authorNames }) => {
    const heading = document.querySelector("article > h1:first-child");
    if (!heading) return false;
    if (heading.nextElementSibling?.classList.contains("ua-pdf-publication-meta")) {
      return true;
    }

    const byline = document.createElement("p");
    byline.className = "ua-pdf-publication-meta";
    byline.textContent = authorNames.join(", ");
    byline.setAttribute("aria-label", "Authors: " + authorNames.join(", "));
    heading.insertAdjacentElement("afterend", byline);

    let authorMeta = document.head.querySelector('meta[name="author"]');
    if (!authorMeta) {
      authorMeta = document.createElement("meta");
      authorMeta.setAttribute("name", "author");
      document.head.append(authorMeta);
    }
    authorMeta.setAttribute("content", authorNames.join(", "));
    return true;
  }, { authorNames: authors });
}

async function prepareMermaidFigures(page) {
  return page.evaluate(
    ({ minimumLabelPoints }) => {
      const pageMeasurements = {
        portrait: { widthMm: 178, heightMm: 259 },
        landscape: { widthMm: 281, heightMm: 188 },
        foldout: { widthMm: 582, heightMm: 403 },
      };

      const mermaidPreBlocks = Array.from(
        document.querySelectorAll("pre"),
      ).filter((pre) => pre.querySelector(":scope > code.mermaid"));

      const wrappers = mermaidPreBlocks.map((pre, index) => {
        const following = pre.nextElementSibling;
        const caption =
          following?.tagName === "P" &&
          /^Figure\s+\d+(?:[A-Z])?\b/i.test(following.textContent?.trim() ?? "")
            ? following
            : undefined;
        const wrapper = document.createElement("figure");
        wrapper.className = "ua-pdf-mermaid-figure";
        pre.parentNode.insertBefore(wrapper, pre);
        wrapper.append(pre);
        if (caption) wrapper.append(caption);
        const captionText = caption?.textContent?.trim() ?? "";
        const number = captionText.match(/^Figure\s+(\d+)/i)?.[1];
        wrapper.dataset.pdfFigure = number ?? String(index + 1);
        return wrapper;
      });

      function visibleLineHeights(element) {
        if (element.namespaceURI === "http://www.w3.org/2000/svg") {
          const rectangle = element.getBoundingClientRect();
          const tspans = Array.from(element.children).filter(
            (child) => child.tagName.toLowerCase() === "tspan",
          );
          const lines = Math.max(1, tspans.length);
          return rectangle.height > 0 ? [rectangle.height / lines] : [];
        }

        const range = document.createRange();
        range.selectNodeContents(element);
        return Array.from(range.getClientRects())
          .filter((rectangle) => rectangle.width > 0 && rectangle.height > 0)
          .map((rectangle) => rectangle.height);
      }

      function measure(wrapper, orientation) {
        const dimensions = pageMeasurements[orientation];
        const host = document.createElement("div");
        host.className = "ua-pdf-measurement-host";
        host.style.position = "absolute";
        host.style.visibility = "hidden";
        host.style.pointerEvents = "none";
        host.style.left = "-200vw";
        host.style.top = "0";
        host.style.width = dimensions.widthMm + "mm";

        const clone = wrapper.cloneNode(true);
        clone.classList.toggle(
          "ua-pdf-mermaid-figure--landscape",
          orientation === "landscape",
        );
        clone.classList.toggle(
          "ua-pdf-mermaid-figure--foldout",
          orientation === "foldout",
        );
        clone.style.width = "100%";
        host.append(clone);
        document.body.append(host);

        const svg = clone.querySelector("code.mermaid svg");
        const labelElements = svg
          ? Array.from(
              svg.querySelectorAll(
                "text, foreignObject .nodeLabel, foreignObject .edgeLabel",
              ),
            )
          : [];
        const lineHeights = labelElements.flatMap(visibleLineHeights);
        const minimumLabelPt =
          lineHeights.length > 0
            ? Math.min(...lineHeights) * (72 / 96)
            : Number.POSITIVE_INFINITY;
        const heightMm = clone.getBoundingClientRect().height * (25.4 / 96);
        host.remove();

        return {
          heightMm,
          minimumLabelPt,
          fits:
            minimumLabelPt >= minimumLabelPoints &&
            heightMm <= dimensions.heightMm,
        };
      }

      const results = [];
      const failures = [];
      for (const wrapper of wrappers) {
        const portrait = measure(wrapper, "portrait");
        const landscape = measure(wrapper, "landscape");
        const foldout = measure(wrapper, "foldout");
        let orientation;
        let selected;

        if (portrait.fits) {
          orientation = "portrait";
          selected = portrait;
        } else if (landscape.fits) {
          orientation = "landscape";
          selected = landscape;
          wrapper.classList.add("ua-pdf-mermaid-figure--landscape");
        } else if (foldout.fits) {
          orientation = "foldout";
          selected = foldout;
          wrapper.classList.add("ua-pdf-mermaid-figure--foldout");
        } else {
          const label = "Figure " + wrapper.dataset.pdfFigure;
          failures.push(
            label +
              ": portrait " +
              portrait.minimumLabelPt.toFixed(2) +
              " pt / " +
              portrait.heightMm.toFixed(1) +
              " mm; landscape " +
              landscape.minimumLabelPt.toFixed(2) +
              " pt / " +
              landscape.heightMm.toFixed(1) +
              " mm; foldout " +
              foldout.minimumLabelPt.toFixed(2) +
              " pt / " +
              foldout.heightMm.toFixed(1) +
              " mm",
          );
          continue;
        }

        results.push({
          figure: wrapper.dataset.pdfFigure,
          orientation,
          minimumLabelPt: Number(selected.minimumLabelPt.toFixed(2)),
          heightMm: Number(selected.heightMm.toFixed(1)),
        });
      }

      if (failures.length > 0) {
        throw new Error(
          "Mermaid figure is not publication-readable at " +
            minimumLabelPoints +
            " pt:\n" +
            failures.join("\n"),
        );
      }

      return results;
    },
    { minimumLabelPoints: minimumDiagramLabelPoints },
  );
}

async function printWithPlaywright(
  pageUrl,
  outputPath,
  { currentSlug, linkTargets, publicationMetadata },
) {
  const browser = await chromium.launch({
    headless: true,
    executablePath: process.env.CHROME_PATH || undefined,
  });

  try {
    const page = await browser.newPage();
    const resourceMonitor = monitorCriticalResources(
      page,
      new URL(pageUrl).origin,
    );

    try {
      const response = await page.goto(pageUrl, { waitUntil: "networkidle" });
      assertMainDocumentResponse(response, pageUrl);
      const renderStatus = await waitForPublicationRender(page);
      resourceMonitor.assertClean();
      console.log(
        "Browser render ready: " +
          renderStatus.diagrams +
          " Mermaid diagram(s), all images and required fonts loaded",
      );

      const metadataInjected = await injectPublicationMetadata(
        page,
        publicationMetadata,
      );
      if (metadataInjected) {
        console.log(
          "Publication byline ready: " + publicationMetadata.authors.join(", "),
        );
      }

      const rewrittenLinks = await rewritePublicationLinks(page, {
        currentPageUrl: pageUrl,
        currentSlug,
        linkTargets,
      });
      console.log(
        "Publication links ready: " +
          rewrittenLinks +
          " local cross-document link(s) rewritten",
      );

      await page.emulateMedia({ media: "print" });
      const figures = await prepareMermaidFigures(page);
      for (const figure of figures) {
        console.log(
          "Figure " +
            figure.figure +
            ": " +
            figure.orientation +
            ", minimum label " +
            figure.minimumLabelPt +
            " pt, height " +
            figure.heightMm +
            " mm",
        );
      }

      await page.evaluate(
        () =>
          new Promise((resolve) =>
            requestAnimationFrame(() => requestAnimationFrame(resolve)),
          ),
      );
      await page.pdf({
        path: outputPath,
        format: "A4",
        printBackground: true,
        preferCSSPageSize: true,
      });
      resourceMonitor.assertClean();
    } catch (error) {
      resourceMonitor.assertClean();
      throw error;
    } finally {
      resourceMonitor.dispose();
    }
  } finally {
    await browser.close();
  }
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    usage();
    return;
  }
  if (!args.source) {
    usage();
    throw new Error("A Markdown source path is required");
  }

  const requestedSourcePath = path.resolve(repoRoot, args.source);
  if (path.extname(requestedSourcePath).toLowerCase() !== ".md") {
    throw new Error("The source must have a .md extension");
  }
  const sourcePath = await realpath(requestedSourcePath);
  if (!isInside(contentRoot, sourcePath)) {
    throw new Error("The source must be a Markdown file under content/");
  }
  if (!(await stat(sourcePath)).isFile()) {
    throw new Error("The source must be a Markdown file");
  }

  const sourceDocument = await readFile(sourcePath, "utf8");
  const publicationMetadata = extractPublicationMetadata(sourceDocument);
  const outputPath = args.output
    ? path.resolve(repoRoot, args.output)
    : defaultPdfOutputPath(sourcePath);
  await validateOutputTarget(sourcePath, outputPath);

  const tempRoot = await mkdtemp(path.join(os.tmpdir(), "ua-pdf-"));
  const siteDir = path.join(tempRoot, "site");
  let server;

  try {
    console.log(
      "Building Quartz with drafts enabled: " +
        path.relative(repoRoot, sourcePath),
    );
    await run(
      process.execPath,
      [
        path.join(repoRoot, "quartz", "bootstrap-cli.mjs"),
        "build",
        "--output",
        siteDir,
      ],
      {
        cwd: repoRoot,
        env: { ...process.env, UA_INCLUDE_DRAFTS: "1" },
      },
    );

    const { contentIndex, htmlPath, slug } = await resolveBuiltPage(
      siteDir,
      sourcePath,
    );
    console.log("Quartz page ready: " + path.relative(siteDir, htmlPath));

    const repositoryFiles = await globby(["**/*"], {
      cwd: repoRoot,
      onlyFiles: true,
      gitignore: true,
      followSymbolicLinks: false,
      ignore: [
        ".git/**",
        "dist/**",
        "node_modules/**",
        "quartz/.quartz-cache/**",
      ],
    });
    const linkTargets = buildDurableLinkTargets(contentIndex, repositoryFiles, {
      publicationBaseUrl: process.env.UA_PDF_PUBLICATION_BASE_URL,
      repository: process.env.GITHUB_REPOSITORY ?? defaultGitHubRepository,
      reference:
        process.env.UA_PDF_REPOSITORY_REF ?? process.env.GITHUB_SHA ?? "main",
    });

    server = await startStaticServer(siteDir);
    const pagePath =
      "/" +
      slug
        .split("/")
        .map((segment) => encodeURIComponent(segment))
        .join("/");
    const pageUrl = server.origin + pagePath;

    console.log("Rendering and printing " + pageUrl);
    const pdfInfo = await withAtomicPdfOutput(outputPath, (stagedPath) =>
      printWithPlaywright(pageUrl, stagedPath, {
        currentSlug: slug,
        linkTargets,
        publicationMetadata,
      }),
    );

    console.log(
      "PDF created: " +
        path.relative(repoRoot, outputPath) +
        " (" +
        pdfInfo.size +
        " bytes); Markdown source unchanged",
    );
  } finally {
    if (server) await server.close();
    await rm(tempRoot, { recursive: true, force: true });
  }
}

const isEntryPoint =
  process.argv[1] &&
  path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isEntryPoint) {
  main().catch((error) => {
    console.error(
      "PDF export failed: " +
        (error instanceof Error ? error.message : String(error)),
    );
    process.exitCode = 1;
  });
}

export {
  assertFontsLoaded,
  assertMainDocumentResponse,
  assertUsablePdf,
  buildDurableLinkTargets,
  defaultPdfOutputPath,
  extractPublicationMetadata,
  isCriticalResource,
  planDurableLinkRewrites,
  startStaticServer,
  validateOutputTarget,
  withAtomicPdfOutput,
};
