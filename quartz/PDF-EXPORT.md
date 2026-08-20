# PDF export

The repository keeps Markdown under `content/` as the canonical editable source. PDF commands build temporary Quartz renditions and write generated files only under `dist/pdf/`.

```text
canonical Markdown
→ temporary publication rendition when needed
→ Quartz render
→ headless Chromium
→ PDF + provenance manifest
```

The exporter does **not** move, rename, replace, or rewrite the canonical Markdown source. Normal Quartz builds continue to remove `draft: true` content; PDF commands set `UA_INCLUDE_DRAFTS=1` only for their temporary build.

## Local setup

```bash
npm ci
npm run pdf:setup
```

`pdf:setup` installs the Playwright Chromium binary. On a fresh Linux machine that also needs browser system packages, use:

```bash
npx playwright install --with-deps chromium
```

Visual verification additionally requires Poppler (`poppler-utils` on Ubuntu):

```bash
sudo apt-get install poppler-utils
```

## Commands

Current standalone publication article:

```bash
npm run pdf:article
```

Output:

```text
dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf
dist/pdf/thinking-systems-when-the-controlled-object-changes.manifest.json
```

Living long-form working paper:

```bash
npm run pdf:working-paper
```

Output:

```text
dist/pdf/uncertainty-architecture-thinking-systems-working-paper.pdf
dist/pdf/uncertainty-architecture-thinking-systems-working-paper.manifest.json
```

The article and the working paper are **different publication objects**, not short and long versions of one document. `pdf:article` is the default external publication surface. `pdf:working-paper` is an explicit export of the living long-form research manuscript; it keeps its own source identity, filename, provenance manifest, and publication state.

The generic `pdf` command maps directly to `quartz/scripts/export-pdf.mjs` and always requires an explicit Markdown source under `content/`.

Generic low-level exporter for any Markdown file under `content/`:

```bash
npm run pdf -- content/research/notes/example.md
npm run pdf -- content/research/notes/example.md --output dist/pdf/example.pdf
```

The generic exporter enforces source/output containment, rejects symlink or hard-link aliases and source collisions, renders through a staging file, validates the resulting PDF, and only then replaces the target. Missing critical stylesheets, fonts, images, local scripts, unresolved temporary links, or unreadable Mermaid labels fail the export rather than silently degrading it.

## Exporter non-regression contract

Later publication work may add title pages, manifests, visual verification, or platform renditions, but it must not weaken the low-level exporter. The following properties are release invariants:

- source real paths resolve to regular `.md` files under `content/`;
- generated PDF outputs remain under `dist/pdf/`;
- canonical Markdown is never moved, renamed, replaced, rewritten, or used as an output target;
- symlink, hardlink, and source-collision protections remain active;
- rendering occurs through a staging file and the destination is replaced only after validation succeeds;
- PDF size, `%PDF-` header, and `%%EOF` trailer validation remain mandatory;
- Quartz renders into an operating-system temporary directory instead of the repository `public/` tree;
- `UA_INCLUDE_DRAFTS=1` is scoped to the temporary PDF build while ordinary Quartz builds continue to remove drafts;
- failed stylesheets, images, fonts, local scripts, or Mermaid resources fail the export;
- same-page anchors remain local and cross-document links become durable GitHub or configured site URLs before printing;
- Mermaid figures are measured automatically, preferring portrait, then landscape, with a foldout only as the final readability-preserving fallback;
- the 5 pt minimum effective Mermaid-label floor remains enforced rather than lowered to make a dense page fit;
- exporter regressions remain part of ordinary Build Integrity;
- the manual `Export research PDF` workflow continues to upload review artifacts.

`quartz/scripts/export-pdf.test.mjs` provides behavioral regression coverage for containment, alias rejection, atomic replacement, PDF validation, critical-resource classification, font loading, durable links, and server failure behavior. The machine-readable repository contract protects the exporter, its regression suite, the ordinary Build Integrity step, and the manual artifact workflow so a later refactor must update the contract explicitly rather than silently deleting a safeguard. This is intentionally more than a browser `print()` call followed by prayer.

## Publication-grade rendition

`pdf:article` and `pdf:working-paper` use `render-publication-pdf.mjs` around the generic exporter. The wrapper adds:

- a title page with the publication title, author, publication status, publication or edition date, version, CC BY 4.0 license, visible repository/canonical URLs, versioned source link, and the full immutable source commit SHA;
- `Vitalii Oborskyi` as the curated author fallback for the standalone article and living working paper when their source metadata does not declare an author; an explicitly declared source author remains authoritative;
- page numbers and a short running footer on every page;
- a clickable contents page when the preflight PDF exceeds 20 pages;
- an adjacent machine-readable provenance manifest;
- source hashing before, after, and during final bundle acceptance;
- rollback-capable installation of the PDF and manifest as one coherent pair.

The schema-version-2 manifest records:

- `source_path`, the full `source_commit_sha`, committed and working Git blob identities, and `source_content_sha256`;
- `pdf_path`, `pdf_sha256`, `generated_at`, `generated_date`, and `page_count`;
- title, authors, publication/edition date, status, maturity, version, draft state, and license;
- `repository_url`, immutable `source_url`, `canonical_url`, `additional_publication_urls`, and combined `external_publication_urls`;
- the TOC threshold and decision;
- canonical and rendered figure lists, including publication-only panel splits.

Before installation and again after installation, the renderer verifies that the manifest checksum matches the actual PDF. An existing destination bundle must also contain both files and pass the same checksum verification before it can become the rollback baseline. If either new file cannot be installed or the installed pair fails verification, the previous matching PDF and manifest are restored together. If rollback itself cannot complete, recovery files are retained and their directory is reported instead of being deleted.

## Strict provenance and preview mode

Versioned PDF builds are strict by default: the working-tree source bytes must match the declared Git commit. Any ref supplied through `UA_PDF_REPOSITORY_REF` or `GITHUB_SHA` is resolved to an immutable full commit SHA before title-page links, source checks, and manifest metadata are produced. A local uncommitted rendition requires `--allow-dirty-preview`; its title page and manifest identify it as a non-versioned preview and record both committed and working-tree blob identities.

Generated PDF, manifest, and verification paths are anchored to the real repository root. Symlinked output roots or parents, aliases to canonical Markdown, and destinations outside `dist/pdf/` are rejected.

## Dense Figure 8

The canonical article keeps **one logical Figure 8**. The PDF renderer does not lower the 5 pt Mermaid-label safety floor. For the standalone article it instead produces two presentation panels:

- **Figure 8A — Decision-ownership model**;
- **Figure 8B — Capability-family axis and orthogonality relationship**.

Together Figures 8A–8B preserve the canonical Figure 8 semantics and full caption. The Markdown source is unchanged. Figure 8A occupies its own A4 landscape page; Figure 8B occupies its own following A4 page and carries the shared canonical-caption continuation note. The article fails closed unless the reviewed split produces exactly one 8A and one 8B, no unsplit Figure 8, and the expected fingerprint of the canonical Mermaid plus caption.

The hard floor remains **5 pt**. The current measured panel geometry is also required to meet the preferred **6 pt** publication minimum, with 6–7 pt as the intended range for the densest panel. Desktop-image verification assumes a 1440 px no-zoom display width and requires an effective minimum label size of at least 12 px. Generate the reviewed SVG/PNG pair and machine-readable measurements with:

```bash
npm run pdf:verify:figure8
```

Outputs are written under `dist/pdf/visual/figure-8/` and included in the CI publication-validation artifact. For an unsplit dense diagram in the living working paper or generic publication export, the renderer may still use a dedicated A2 landscape foldout rather than reducing the floor.

## Platform assets

Generate all standalone-article figures and platform imagery with:

```bash
npm run publication:assets
```

The renderer reads the canonical standalone article and writes only under:

```text
dist/publication/thinking-systems/
├── assets.manifest.json
├── cover-linkedin-article.png
├── social-preview.png
├── medium-hero.png
└── figures/
    ├── svg/
    └── png/
```

Every canonical Mermaid figure is exported as SVG for website/PDF reuse and as PNG for Medium or LinkedIn distribution. Standard figures are rendered at no less than **1600 px** wide; denser figures use **2400–3200 px**. Figure 8 is not reinterpreted: the renderer reuses the reviewed, fingerprint-coupled 8A/8B panel builders. At a declared 1600 px desktop display width, each Figure 8 panel must retain a projected minimum label size of at least 14 px, so the platform image does not depend on browser zoom.

The generated platform sizes are:

- `cover-linkedin-article.png` — **2000 × 600**;
- `social-preview.png` — **1200 × 627**;
- `medium-hero.png` — **1600 × 840**.

`assets.manifest.json` records the canonical source path and digest, generated date, output checksums and dimensions, the figure-density classification, platform target sizes, and the Figure 8 semantic fingerprint/readability result. Canonical Markdown is hashed before and after rendering and must remain byte-identical.

## Visual verification

After producing a PDF, render every page to images and generate a contact sheet:

```bash
npm run pdf:verify -- dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf --require-manifest
```

Publication verification uses `pdfinfo`, `pdffonts`, `pdftotext`, `pdftohtml`, and `pdftoppm` to:

- compare the adjacent manifest with the actual PDF and canonical Markdown bytes;
- require full source and PDF identities, page-count agreement, figure lists, and publication URL fields;
- confirm the title page contains the resolved author, status, date/version, CC BY 4.0 license, visible URLs, and full source commit SHA;
- verify the running footer and correct page counter on every page;
- prove that a TOC required by the 20-page threshold exists and contains internal clickable links;
- rasterize every page, reject likely blank/contentless pages, and create `visual-verification.json` plus a contact sheet under `dist/pdf/visual/<pdf-name>/`.

Omit `--require-manifest` only when visually checking a low-level generic PDF that intentionally has no publication manifest.

Automated verification is not a substitute for editorial review. The contact sheet remains the final visual check for clipping, overlap, awkward pagination, and figure readability.

## Durable links

Same-page anchors remain PDF-local. Cross-document repository links become durable GitHub source links by default. Set `UA_PDF_PUBLICATION_BASE_URL` when a stable Quartz site should become the link target instead. GitHub Actions uses the workflow commit; local exports use the current repository commit unless `UA_PDF_REPOSITORY_REF` overrides it.

## GitHub Actions

Build Integrity runs PDF unit/regression tests and the ordinary draft-filtered Quartz build on every pull request. The Chromium/Poppler end-to-end render is path-aware for pull requests and runs when publication sources or PDF/Quartz rendering surfaces change. Pushes to `main` and manual Build Integrity runs execute the complete article and working-paper PDF path plus the standalone article platform-asset renderer.

Run **Export research PDF** manually when a downloadable review artifact is needed. The workflow defaults to the standalone article, accepts the living working paper or another Markdown source under `content/`, performs visual verification, and uploads PDFs, manifests, contact sheets, and the complete `dist/publication/thinking-systems/` asset bundle for 14 days when the standalone article is selected.

The workflow does not deploy Quartz, publish a website, commit generated PDF or image binaries, or change research status. Permanent released artifacts should be attached to an explicit GitHub Release after the content edition is frozen.
