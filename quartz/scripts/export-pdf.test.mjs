import assert from "node:assert/strict";
import {
  link,
  mkdir,
  mkdtemp,
  readFile,
  readdir,
  rm,
  symlink,
  writeFile,
} from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
  assertFontsLoaded,
  assertMainDocumentResponse,
  buildDurableLinkTargets,
  defaultPdfOutputPath,
  extractPublicationMetadata,
  isCriticalResource,
  planDurableLinkRewrites,
  startStaticServer,
  validateOutputTarget,
  withAtomicPdfOutput,
} from "./export-pdf.mjs";

async function temporaryDirectory(t) {
  const directory = await mkdtemp(path.join(os.tmpdir(), "ua-pdf-test-"));
  t.after(() => rm(directory, { recursive: true, force: true }));
  return directory;
}

function syntheticPdf(marker = "publication") {
  return Buffer.concat([
    Buffer.from("%PDF-1.7\n"),
    Buffer.from(marker),
    Buffer.alloc(2048),
    Buffer.from("\n%%EOF\n"),
  ]);
}

function responseFixture({
  contentType = "text/html; charset=utf-8",
  ok = true,
  status = 200,
  statusText = "OK",
} = {}) {
  return {
    headers: () => ({ "content-type": contentType }),
    ok: () => ok,
    status: () => status,
    statusText: () => statusText,
  };
}

function requestFixture(resourceType, url) {
  return {
    resourceType: () => resourceType,
    url: () => url,
  };
}

test("output must be a separate PDF path", async (t) => {
  const directory = await temporaryDirectory(t);
  const source = path.join(directory, "paper.md");
  await writeFile(source, "# Source\n");

  await assert.rejects(
    validateOutputTarget(source, source, { outputRoot: directory }),
    /output path must have a \.pdf extension/,
  );
  await assert.rejects(
    validateOutputTarget(source, path.join(directory, "package.json"), {
      outputRoot: directory,
    }),
    /output path must have a \.pdf extension/,
  );
  await assert.doesNotReject(
    validateOutputTarget(source, path.join(directory, "paper.pdf"), {
      outputRoot: directory,
    }),
  );
  await assert.rejects(
    validateOutputTarget(source, path.join(directory, "..", "paper.pdf"), {
      outputRoot: directory,
    }),
    /must be under dist\/pdf\//,
  );
});


test("default output mirrors the content-relative source path", async (t) => {
  const directory = await temporaryDirectory(t);
  const content = path.join(directory, "content");
  const output = path.join(directory, "dist", "pdf");
  const source = path.join(content, "research", "notes", "paper.md");
  await mkdir(path.dirname(source), { recursive: true });
  await writeFile(source, "# Source\n");

  assert.equal(
    defaultPdfOutputPath(source, { contentRoot: content, outputRoot: output }),
    path.join(output, "research", "notes", "paper.pdf"),
  );
});


test("publication metadata normalizes frontmatter authors", () => {
  assert.deepEqual(
    extractPublicationMetadata(`---
authors:
  - Vitalii Oborskyi
  - name: Sam Walker
---
# Paper
`),
    { authors: ["Vitalii Oborskyi", "Sam Walker"] },
  );
  assert.deepEqual(
    extractPublicationMetadata(`---
author: Vitalii Oborskyi
---
# Paper
`),
    { authors: ["Vitalii Oborskyi"] },
  );
});

test("output cannot reach Markdown through a symlink or hardlink", async (t) => {
  const directory = await temporaryDirectory(t);
  const source = path.join(directory, "paper.md");
  const symbolicOutput = path.join(directory, "symbolic.pdf");
  const hardOutput = path.join(directory, "hard.pdf");
  await writeFile(source, "# Canonical Markdown\n");
  await symlink(source, symbolicOutput);
  await link(source, hardOutput);

  await assert.rejects(
    validateOutputTarget(source, symbolicOutput, { outputRoot: directory }),
    /resolves to the Markdown source|must not be a symbolic link|symbolic-link component/,
  );
  await assert.rejects(
    validateOutputTarget(source, hardOutput, { outputRoot: directory }),
    /resolves to the Markdown source/,
  );
  assert.equal(await readFile(source, "utf8"), "# Canonical Markdown\n");
});

test("atomic export replaces only the PDF after validation", async (t) => {
  const directory = await temporaryDirectory(t);
  const output = path.join(directory, "publication.pdf");
  const expected = syntheticPdf("new");
  await writeFile(output, "previous PDF placeholder");

  const info = await withAtomicPdfOutput(output, (stagedPath) =>
    writeFile(stagedPath, expected),
  );

  assert.equal(info.size, expected.length);
  assert.deepEqual(await readFile(output), expected);
  assert.deepEqual(
    (await readdir(directory)).filter((name) =>
      name.startsWith(".ua-pdf-stage-"),
    ),
    [],
  );
});

test("failed rendering preserves the previous PDF", async (t) => {
  const directory = await temporaryDirectory(t);
  const output = path.join(directory, "publication.pdf");
  await writeFile(output, "previous PDF");

  await assert.rejects(
    withAtomicPdfOutput(output, async () => {
      throw new Error("browser failed");
    }),
    /browser failed/,
  );

  assert.equal(await readFile(output, "utf8"), "previous PDF");
  assert.deepEqual(
    (await readdir(directory)).filter((name) =>
      name.startsWith(".ua-pdf-stage-"),
    ),
    [],
  );
});

test("invalid staged output preserves the previous PDF", async (t) => {
  const directory = await temporaryDirectory(t);
  const output = path.join(directory, "publication.pdf");
  await writeFile(output, "previous PDF");

  await assert.rejects(
    withAtomicPdfOutput(output, (stagedPath) =>
      writeFile(stagedPath, Buffer.alloc(2048)),
    ),
    /not a PDF file/,
  );

  assert.equal(await readFile(output, "utf8"), "previous PDF");
  assert.deepEqual(
    (await readdir(directory)).filter((name) =>
      name.startsWith(".ua-pdf-stage-"),
    ),
    [],
  );
});

test("main document must be successful HTML", () => {
  assert.doesNotThrow(() =>
    assertMainDocumentResponse(
      responseFixture(),
      "http://127.0.0.1/publication",
    ),
  );
  assert.throws(
    () =>
      assertMainDocumentResponse(
        responseFixture({ ok: false, status: 404, statusText: "Not Found" }),
        "http://127.0.0.1/missing",
      ),
    /HTTP 404 Not Found/,
  );
  assert.throws(
    () =>
      assertMainDocumentResponse(
        responseFixture({ contentType: "application/pdf" }),
        "http://127.0.0.1/not-html",
      ),
    /unexpected content type/,
  );
  assert.throws(
    () => assertMainDocumentResponse(null, "http://127.0.0.1/no-response"),
    /received no response/,
  );
});

test("publication-critical resources are classified narrowly", () => {
  const origin = "http://127.0.0.1:4321";
  assert.equal(
    isCriticalResource(
      requestFixture("stylesheet", "https://fonts.googleapis.com/css2"),
      origin,
    ),
    true,
  );
  assert.equal(
    isCriticalResource(
      requestFixture("font", "https://fonts.gstatic.com/font.woff2"),
      origin,
    ),
    true,
  );
  assert.equal(
    isCriticalResource(
      requestFixture("script", origin + "/prescript.js"),
      origin,
    ),
    true,
  );
  assert.equal(
    isCriticalResource(
      requestFixture(
        "script",
        "https://cdnjs.cloudflare.com/ajax/libs/mermaid/11.4.1/mermaid.min.js",
      ),
      origin,
    ),
    true,
  );
  assert.equal(
    isCriticalResource(
      requestFixture("script", "https://plausible.io/js/script.manual.js"),
      origin,
    ),
    false,
  );
});

test("required publication fonts must really load", () => {
  assert.doesNotThrow(() =>
    assertFontsLoaded({
      fontChecks: [
        { variable: "--headerFont", loadedFaces: 1 },
        { variable: "--bodyFont", loadedFaces: 1 },
        { variable: "--codeFont", loadedFaces: 1 },
      ],
      failedFontFaces: [],
    }),
  );
  assert.throws(
    () =>
      assertFontsLoaded({
        fontChecks: [{ variable: "--bodyFont", loadedFaces: 0 }],
        failedFontFaces: [],
      }),
    /fonts failed to load/,
  );
  assert.throws(
    () =>
      assertFontsLoaded({
        fontChecks: [{ variable: "--bodyFont", loadedFaces: 1 }],
        failedFontFaces: ["Source Sans Pro 400 normal"],
      }),
    /fonts failed to load/,
  );
});

test("durable targets cover Quartz slugs, root docs, and encoded paths", () => {
  const targets = buildDurableLinkTargets(
    {
      paper: {
        slug: "research/custom-paper",
        filePath: "research/notes/Paper Name.md",
      },
    },
    ["CONTRIBUTING.md", "content/research/notes/Paper Name.md"],
    {
      repository: "Example/Repository",
      reference: "abc123",
    },
  );

  assert.equal(
    targets["research/custom-paper"],
    "https://github.com/Example/Repository/blob/abc123/content/research/notes/Paper%20Name.md",
  );
  assert.equal(
    targets.CONTRIBUTING,
    "https://github.com/Example/Repository/blob/abc123/CONTRIBUTING.md",
  );
});

test("cross-document links become durable and preserve fragments", () => {
  const rewrites = planDurableLinkRewrites(
    [
      {
        href: "../other#decision-boundary",
        dataSlug: "research/other",
      },
      {
        href: "./current#local",
        dataSlug: "research/current",
      },
      { href: "#already-local" },
      { href: "https://example.com/reference" },
      { href: "mailto:review@example.com" },
    ],
    {
      currentPageUrl: "http://127.0.0.1:4321/research/current",
      currentSlug: "research/current",
      linkTargets: {
        "research/other":
          "https://github.com/Example/Repository/blob/abc123/content/research/other.md",
      },
    },
  );

  assert.deepEqual(rewrites, [
    {
      index: 0,
      href: "https://github.com/Example/Repository/blob/abc123/content/research/other.md#decision-boundary",
    },
    { index: 1, href: "#local" },
  ]);
});

test("unresolved localhost links fail instead of entering the PDF", () => {
  assert.throws(
    () =>
      planDurableLinkRewrites(
        [{ href: "../missing", dataSlug: "research/missing" }],
        {
          currentPageUrl: "http://127.0.0.1:4321/research/current",
          currentSlug: "research/current",
          linkTargets: {},
        },
      ),
    /Unable to make internal publication link durable/,
  );
});

test("static server returns a real 404 for missing output", async (t) => {
  const directory = await temporaryDirectory(t);
  await writeFile(path.join(directory, "index.html"), "<h1>Ready</h1>");
  const server = await startStaticServer(directory);
  t.after(() => server.close());

  const found = await fetch(server.origin + "/");
  const missing = await fetch(server.origin + "/missing");
  assert.equal(found.status, 200);
  assert.match(found.headers.get("content-type"), /text\/html/);
  assert.equal(missing.status, 404);
});
