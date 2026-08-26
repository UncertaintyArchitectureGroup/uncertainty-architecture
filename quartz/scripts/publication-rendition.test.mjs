import assert from "node:assert/strict";
import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import {
  buildPublicationRendition,
  compactInlineSvg,
  buildToc,
  extractFigureList,
  normalizeDate,
  repoRoot,
  resolvePublicationAuthors,
  sha256,
  splitFigure8,
  workingPaperSource,
} from "./publication-rendition.mjs";
import {
  countPdfPages,
  determineSourceProvenance,
  finalizePublicationPdf,
} from "./render-publication-pdf.mjs";
import {
  findContentlessTextPages,
  verifyClickableContents,
  verifyFigure8PublicationRendition,
  verifyPageFurniture,
  verifyPublicationManifest,
  verifyTitlePage,
} from "./verify-publication-pdf.mjs";
import { assertCanonicalFigure8Fingerprint } from "./publication-figure8-fingerprint.mjs";

test("inline publication SVG remains one raw HTML block", () => {
  const svg = `<svg>\n<text>top</text>\n\n<rect/>\n\n<text>bottom</text>\n</svg>`;
  const compacted = compactInlineSvg(svg);
  assert.doesNotMatch(compacted, /\n[ \t]*\n/);
  assert.match(compacted, /<text>bottom<\/text>/);
});

test("Figure 8 publication rendition preserves decision and capability semantics", () => {
  const source = `Before\n\n\`\`\`mermaid\nflowchart LR\n    subgraph L["Decision ownership"]\n        O["Organization"] -->|initial admissibility + assessment eligibility| P["Project"]\n        P --> CAT{"Selected technical design still a Thinking System?"}\n        CAT -->|No| EXIT["Exit Thinking-System-specific lifecycle"]\n        P --> RQ["specific Bounded Research Authorization"]\n        P --> VB["viable production basis"]\n        P --> PA["research-only and/or production-capable"]\n        D["Delivery"] --> E["Delivery / Runtime reassessment evidence"]\n        X["Exogenous Organizational change"] --> O\n    end\n    subgraph F["Capability functions"]\n        A["Actuators and corrective action"]\n        K["Constraints and realizations"]\n        S["Sensors and evidence"]\n        C["Controllers / decision functions"]\n    end\n    L -. "all four capability families may appear at every decision horizon" .- F\n\`\`\`\n\n**Figure 8 — Two orthogonal models.** Canonical caption.\n\nAfter`;
  const result = splitFigure8(source, { verifyFingerprint: false });
  assert.equal(result.split, true);
  assert.match(result.content, /Figure 8A — Decision-ownership model/);
  assert.match(result.content, /Figure 8B — Capability-family axis/);
  assert.match(
    result.content,
    /Together, Figures 8A–8B preserve canonical Figure 8/,
  );
  assert.match(
    result.content,
    /initial admissibility \+ assessment eligibility/,
  );
  assert.match(result.content, /specific Bounded Research Authorization/);
  assert.match(result.content, /research-only and\/or production-capable/);
  assert.match(result.content, /Exogenous Organizational change/);
  assert.match(
    result.content,
    /All four capability families may appear at every decision horizon/,
  );
  assert.match(result.content, /not an execution pipeline/);
});

test("strict Figure 8 fingerprint rejects topology changes even when semantic marker text remains", () => {
  const mermaid = `flowchart LR\nsubgraph L["Decision ownership"]\nO["initial admissibility + assessment eligibility"] --> P["specific Bounded Research Authorization"]\nP --> X["Selected technical design still a Thinking System?"]\nX --> E["Exit Thinking-System-specific lifecycle"]\nV["viable production basis"]\nA["research-only and/or production-capable"]\nD["Delivery / Runtime reassessment evidence"]\nG["Exogenous Organizational change"]\nend\nsubgraph F["Capability"]\nC["all four capability families may appear at every decision horizon"]\nend`;
  assert.throws(
    () =>
      assertCanonicalFigure8Fingerprint(
        mermaid,
        "**Figure 8 — Two orthogonal models.** changed",
      ),
    /requires substantive review/,
  );
});

test("Figure 8 without both orthogonal subgraphs is left unchanged", () => {
  const source = `\`\`\`mermaid\nflowchart TB\n    O["Organization"] --> P["Project"]\n\`\`\`\n\n**Figure 8 — Decision model.** No capability model here.`;
  const result = splitFigure8(source);
  assert.equal(result.split, false);
  assert.equal(result.content, source);
});

test("clickable contents renders stable second and third level links", () => {
  const toc = buildToc(
    `# Title\n\n## First Section\n\n### Detail Here\n\n## First Section`,
  );
  assert.match(toc, /<a href="#first-section">First Section<\/a>/);
  assert.match(toc, /<a href="#detail-here">Detail Here<\/a>/);
  assert.match(toc, /<a href="#first-section-1">First Section<\/a>/);
});

test("curated UA publication objects retain Vitalii Oborskyi attribution without editing research Markdown", async () => {
  assert.deepEqual(resolvePublicationAuthors({}, workingPaperSource), [
    "Vitalii Oborskyi",
  ]);
  assert.deepEqual(
    resolvePublicationAuthors(
      { authors: ["Declared Author"] },
      workingPaperSource,
    ),
    ["Declared Author"],
  );

  const sourceCommit = "f".repeat(40);
  const source = {
    relative: workingPaperSource,
    raw: "---\ntitle: Working paper\n---\n# Working paper\n",
    data: {
      title: "Working paper",
      status: "research",
      maturity: "draft",
      updated: "2026-08-20",
      license: "CC-BY-4.0",
      draft: true,
    },
    content: "# Working paper\n",
  };
  const rendition = await buildPublicationRendition(source, {
    sourceCommit,
    provenance: {
      state: "committed",
      workingBlob: "a".repeat(40),
      committedBlob: "a".repeat(40),
    },
    splitDenseFigures: false,
  });
  assert.deepEqual(rendition.authors, ["Vitalii Oborskyi"]);
  assert.match(rendition.rendered, /Vitalii Oborskyi/);
});

test("publication title page carries full author, status, license, URLs, and source commit SHA", async () => {
  const sourceCommit = "0123456789abcdef0123456789abcdef01234567";
  const source = {
    relative: "content/research/notes/publication.md",
    raw: "---\ntitle: Publication title\n---\n# Publication title\n\n## Section\n",
    data: {
      title: "Publication title",
      authors: ["Vitalii Oborskyi"],
      status: "research",
      maturity: "draft",
      publication_date: "2026-08-20",
      version: "v1.0",
      license: "CC-BY-4.0",
      canonical_url: "https://example.org/publication",
      draft: true,
    },
    content: "# Publication title\n\n## Section\n",
  };
  const rendition = await buildPublicationRendition(source, {
    sourceCommit,
    provenance: {
      state: "committed",
      workingBlob: "a".repeat(40),
      committedBlob: "a".repeat(40),
    },
    splitDenseFigures: false,
  });
  assert.match(rendition.rendered, /Vitalii Oborskyi/);
  assert.match(rendition.rendered, /research · draft/);
  assert.match(rendition.rendered, /CC BY 4\.0/);
  assert.match(rendition.rendered, /https:\/\/example\.org\/publication/);
  assert.match(rendition.rendered, new RegExp(sourceCommit));
  assert.doesNotMatch(rendition.rendered, /0123456789ab<\/code>/);
});

test("publication manifest verifies explicit source and PDF identities", async () => {
  const pdfBuffer = Buffer.from("publication pdf bytes");
  const sourceBuffer = Buffer.from("# Canonical source\n");
  const pdfPath = path.join(repoRoot, "dist", "pdf", "publication.pdf");
  const commit = "1".repeat(40);
  const manifest = {
    schema_version: 2,
    artifact: "publication-pdf",
    title: "Publication title",
    authors: ["Vitalii Oborskyi"],
    source_path: "content/research/notes/publication.md",
    source_sha: commit,
    source_commit: commit,
    source_commit_sha: commit,
    source_state: "committed",
    source_git_blob_sha: "2".repeat(40),
    source_working_blob_sha: "2".repeat(40),
    source_content_digest: {
      algorithm: "sha256",
      value: sha256(sourceBuffer),
    },
    source_sha256: sha256(sourceBuffer),
    source_content_sha256: sha256(sourceBuffer),
    pdf_path: "dist/pdf/publication.pdf",
    pdf_sha256: sha256(pdfBuffer),
    generated_at: "2026-08-20T10:00:00.000Z",
    generated_date: "2026-08-20",
    publication_date: "2026-08-20",
    edition_date: "2026-08-20",
    version: "v1.0",
    status: "research",
    maturity: "draft",
    draft: true,
    license: "CC-BY-4.0",
    repository_url: "https://github.com/Example/Repository",
    source_url: `https://github.com/Example/Repository/blob/${commit}/content/research/notes/publication.md`,
    canonical_url: "https://example.org/publication",
    additional_publication_urls: ["https://example.org/copy"],
    external_publication_urls: [
      "https://example.org/publication",
      "https://example.org/copy",
    ],
    number_of_pages: 21,
    page_count: 21,
    toc_included: true,
    toc_threshold_pages: 20,
    figures: {
      canonical: [{ number: 1, panel: null, title: "Canonical" }],
      rendered: [{ number: 1, panel: null, title: "Canonical" }],
    },
    canonical_figures: [{ number: 1, panel: null, title: "Canonical" }],
    rendition_figures: [{ number: 1, panel: null, title: "Canonical" }],
    figure_8_split_for_readability: false,
  };
  const result = await verifyPublicationManifest(manifest, {
    pdfPath,
    pdfBuffer,
    expectedPages: 21,
    sourceBuffer,
  });
  assert.equal(result.valid, true, result.errors.join("; "));

  const truncated = {
    ...manifest,
    source_commit_sha: commit.slice(0, 12),
  };
  const invalid = await verifyPublicationManifest(truncated, {
    pdfPath,
    pdfBuffer,
    expectedPages: 21,
    sourceBuffer,
  });
  assert.equal(invalid.valid, false);
  assert.match(invalid.errors.join("; "), /full 40-character Git commit SHA/);
});

test("title-page and clickable-contents verification reject incomplete publication furniture", () => {
  const commit = "3".repeat(40);
  const manifest = {
    title: "Publication title",
    authors: ["Vitalii Oborskyi"],
    status: "research",
    maturity: "draft",
    version: "v1.0",
    license: "CC-BY-4.0",
    publication_date: "2026-08-20",
    edition_date: "2026-08-20",
    source_commit_sha: commit,
    repository_url: "https://github.com/Example/Repository",
    canonical_url: "https://example.org/publication",
    toc_included: true,
    toc_threshold_pages: 20,
  };
  const titleText = [
    "Publication title",
    "Vitalii Oborskyi",
    "research · draft",
    "v1.0",
    "CC BY 4.0",
    "2026-08-20",
    commit,
    "https://github.com/Example/Repository",
    "https://example.org/publication",
  ].join("\n");
  assert.equal(verifyTitlePage(titleText, manifest).valid, true);
  assert.equal(
    verifyTitlePage(titleText.replace(commit, commit.slice(0, 12)), manifest)
      .valid,
    false,
  );

  const pdfText = `${titleText}\fContents\nFirst Section\fBody`;
  const xml = '<text><a href="publication.html#3">First Section</a></text>';
  assert.equal(verifyClickableContents(pdfText, xml, manifest, 21).valid, true);
  assert.equal(
    verifyClickableContents(pdfText, "<text>First Section</text>", manifest, 21)
      .valid,
    false,
  );
});

test("Figure 8 PDF verification tolerates Poppler glyph spacing and wrapped captions", () => {
  const manifest = {
    source_path: "content/research/notes/thinking-systems-publication-draft.md",
    figure_8_split_for_readability: true,
    figure_8_source_fingerprint:
      "54c622e1404e7ee760934f231bc81f9e9a5ce2dde30a7c85422316ecc138626a",
    figure_8_readability: {
      panels: {
        A: {
          effective_pdf_label_pt: 6.11,
          pdf_hard_floor_met: true,
          pdf_preferred_target_met: true,
          effective_desktop_label_px: 14.63,
          desktop_readable: true,
        },
        B: {
          effective_pdf_label_pt: 8.07,
          pdf_hard_floor_met: true,
          pdf_preferred_target_met: true,
          effective_desktop_label_px: 25.6,
          desktop_readable: true,
        },
      },
    },
    figures: {
      canonical: [{ number: 8, panel: null, title: "Two orthogonal models" }],
      rendered: [
        { number: 8, panel: "A", title: "Decision-ownership model" },
        {
          number: 8,
          panel: "B",
          title: "Capability-family axis and orthogonality relationship",
        },
      ],
    },
  };
  const pdfText = [
    "Figure 8A — Decision-ownership model.",
    [
      "Figure 8B — Capabilit y-family axis and ort hogonalit y relat ionship.",
      "Toget her, Figures 8A–8B preserve canonical Figure 8.",
    ].join("\n"),
  ].join("\f");

  const result = verifyFigure8PublicationRendition(pdfText, manifest);
  assert.equal(result.valid, true, JSON.stringify(result.checks));
  assert.equal(result.panel_a_page, 1);
  assert.equal(result.panel_b_page, 2);
});

test("publication dates remain stable YYYY-MM-DD values", () => {
  assert.equal(
    normalizeDate(new Date("2026-08-17T00:00:00.000Z")),
    "2026-08-17",
  );
  assert.equal(normalizeDate("2026-08-17T18:20:00Z"), "2026-08-17");
  assert.equal(normalizeDate("2026-08-17"), "2026-08-17");
  assert.equal(normalizeDate(null), null);
});

test("PDF page furniture requires a running footer and counter on every page", () => {
  const complete = Array.from(
    { length: 3 },
    (_, index) =>
      `Page body ${index + 1}\nUncertainty Architecture · Research Publication\nPage ${index + 1} / 3`,
  ).join("\f");
  assert.equal(verifyPageFurniture(complete, 3).valid, true);

  const incomplete = complete.replace(
    "Uncertainty Architecture · Research Publication\nPage 2 / 3",
    "Page 2 / 3",
  );
  const result = verifyPageFurniture(incomplete, 3);
  assert.equal(result.valid, false);
  assert.deepEqual(result.missing_running_footer_pages, [2]);
});

test("PDF verification rejects pages that contain only page furniture", () => {
  const text = [
    "Article title\nUncertainty Architecture · Research Publication\nPage 1 / 3",
    "Uncertainty Architecture · Research Publication\nPage 2 / 3",
    "Closing section\nUncertainty Architecture · Research Publication\nPage 3 / 3",
  ].join("\f");
  assert.deepEqual(findContentlessTextPages(text, 3), [2]);
});

test("figure list distinguishes publication 8A and 8B renditions", () => {
  const figures = extractFigureList(
    `**Figure 7 — Complete bounded control architecture.** Text\n\n**Figure 8A — Decision-ownership model.** Text\n\n**Figure 8B — Capability-family axis.** Text`,
  );
  assert.deepEqual(
    figures.map(({ number, panel }) => [number, panel]),
    [
      [7, null],
      [8, "A"],
      [8, "B"],
    ],
  );
});

test("PDF page counting ignores Pages objects", () => {
  assert.equal(
    countPdfPages(
      Buffer.from(
        "/Type /Pages /Count 2 /Kids [] /Type /Page /Type /Page",
        "latin1",
      ),
    ),
    2,
  );
});

test("publication finalization preserves the previous PDF when rename fails", async () => {
  const directory = await mkdtemp(
    path.join(os.tmpdir(), "ua-publication-finalize-test-"),
  );
  try {
    const preflight = path.join(directory, "preflight.pdf");
    const output = path.join(directory, "publication.pdf");
    await writeFile(preflight, "new publication");
    await writeFile(output, "previous publication");
    await assert.rejects(
      finalizePublicationPdf(preflight, output, async () => {
        throw new Error("injected finalization failure");
      }),
      /injected finalization failure/,
    );
    assert.equal(await readFile(output, "utf8"), "previous publication");
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test("strict provenance rejects a source missing from the declared commit", async () => {
  const directory = await mkdtemp(
    path.join(os.tmpdir(), "ua-publication-provenance-test-"),
  );
  try {
    const sourcePath = path.join(directory, "uncommitted.md");
    await writeFile(sourcePath, "# Uncommitted publication\n");
    const source = { absolute: sourcePath, relative: "content/uncommitted.md" };
    await assert.rejects(
      determineSourceProvenance(source, "HEAD"),
      /not present at declared source commit/,
    );
    const preview = await determineSourceProvenance(source, "HEAD", {
      allowDirtyPreview: true,
    });
    assert.equal(preview.state, "dirty-preview");
    assert.equal(preview.committedBlob, null);
    assert.match(preview.workingBlob, /^[0-9a-f]{40}$/);
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});
