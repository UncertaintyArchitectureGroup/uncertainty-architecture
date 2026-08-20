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

- a title page with the publication title, declared author, publication status, publication or edition date, version, CC BY 4.0 license, visible repository/canonical URLs, versioned source link, and the full immutable source commit SHA;
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

## Figure presentation

Publication pages retain a white background for print fidelity and predictable contrast. Diagram bodies use a restrained off-white panel with a thin neutral border so figures remain visually grouped without turning the paper into a slide deck.

For the standalone article, canonical Figure 3 remains a single Mermaid comparison in Markdown, while the publication rendition presents the same meaning as two side-by-side panels: **Linear Software** on the left and **Thinking System** on the right. The transformation is guarded by semantic markers and does not edit the canonical article source.

Figure 8A is re-authored for publication as three decision bands across **Organization**, **Project / Architecture**, **Delivery**, and **Runtime**, replacing the dense sequence-style presentation while preserving the canonical decision relationships. Figure 8B retains the capability-family and orthogonality view.

## Dense Figure 8

The canonical article keeps **one logical Figure 8**. The PDF renderer does not lower the 5 pt Mermaid-label safety floor. For the standalone article it instead produces two presentation panels:

- **Figure 8A — Decision-ownership model**;
- **Figure 8B — Capability-family axis and orthogonality relationship**.

Together Figures 8A–8B preserve the canonical Figure 8 semantics and full caption. The Markdown source is unchanged. The article fails closed unless the reviewed split produces exactly one 8A and one 8B, no unsplit Figure 8, and the expected fingerprint of the canonical Mermaid plus caption.

The hard floor remains **5 pt**; 6–7 pt or larger is the target where layout permits it. For an unsplit dense diagram in the living working paper or generic publication export, the renderer may use a dedicated A2 landscape foldout rather than reducing the floor.

## Visual verification

After producing a PDF, render every page to images and generate a contact sheet:

```bash
npm run pdf:verify -- dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf --require-manifest
```

Publication verification uses `pdfinfo`, `pdffonts`, `pdftotext`, `pdftohtml`, and `pdftoppm` to:

- compare the adjacent manifest with the actual PDF and canonical Markdown bytes;
- require full source and PDF identities, page-count agreement, figure lists, and publication URL fields;
- confirm the title page contains the declared author, status, date/version, CC BY 4.0 license, visible URLs, and full source commit SHA;
- verify the running footer and correct page counter on every page;
- prove that a TOC required by the 20-page threshold exists and contains internal clickable links;
- rasterize every page, reject likely blank/contentless pages, and create `visual-verification.json` plus a contact sheet under `dist/pdf/visual/<pdf-name>/`.

Omit `--require-manifest` only when visually checking a low-level generic PDF that intentionally has no publication manifest.

Automated verification is not a substitute for editorial review. The contact sheet remains the final visual check for clipping, overlap, awkward pagination, and figure readability.

## Durable links

Same-page anchors remain PDF-local. Cross-document repository links become durable GitHub source links by default. Set `UA_PDF_PUBLICATION_BASE_URL` when a stable Quartz site should become the link target instead. GitHub Actions uses the workflow commit; local exports use the current repository commit unless `UA_PDF_REPOSITORY_REF` overrides it.

## GitHub Actions

Build Integrity runs PDF unit/regression tests and the ordinary draft-filtered Quartz build on every pull request. The Chromium/Poppler end-to-end render is path-aware for pull requests and runs when publication sources or PDF/Quartz rendering surfaces change. Pushes to `main` and manual Build Integrity runs execute the complete article and working-paper PDF path.

Run **Export research PDF** manually when a downloadable review artifact is needed. The workflow defaults to the standalone article, accepts the living working paper or another Markdown source under `content/`, performs visual verification, and uploads PDFs, manifests, and contact sheets for 14 days.

The workflow does not deploy Quartz, publish a website, commit generated PDF binaries, or change research status. Permanent released PDFs should be attached to an explicit GitHub Release after the content edition is frozen.