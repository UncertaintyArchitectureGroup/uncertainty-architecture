# PDF export

The repository keeps Markdown under `content/` as the canonical editable source. PDF commands build temporary Quartz renditions and write generated artifacts only under `dist/pdf/`.

```text
canonical Markdown
→ temporary publication rendition (when needed)
→ Quartz render
→ headless Chromium
→ PDF + provenance manifest
```

The publishing layer does **not** move, rename, replace, or rewrite the canonical Markdown source. Normal Quartz builds continue to remove `draft: true` content; PDF commands set `UA_INCLUDE_DRAFTS=1` only for temporary rendering.

## One-time local setup

Install the locked Node dependencies and Playwright Chromium before the first local PDF render:

```bash
npm ci
npm run pdf:setup
```

On Linux systems that also need Chromium system packages, use:

```bash
npx playwright install --with-deps chromium
```

Visual verification additionally requires Poppler (`poppler-utils` on Ubuntu). The GitHub Actions workflows install Chromium, its Linux dependencies, and Poppler automatically.

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

Generic low-level exporter for any Markdown file under `content/`:

```bash
npm run pdf -- content/research/notes/example.md
npm run pdf -- content/research/notes/example.md --output dist/pdf/example.pdf
```

The generic exporter enforces source/output containment, rejects symlink or hard-link aliases and source collisions, renders through a staging file, validates the resulting PDF, and only then atomically replaces the target PDF. Missing critical stylesheets, fonts, images, local scripts, unresolved temporary links, or unreadable Mermaid labels fail the export rather than silently degrading it.

## Publication-grade rendition

`pdf:article` and `pdf:working-paper` use `render-publication-pdf.mjs` around the generic exporter. The wrapper adds a publication title page, status/date/version/license/source-commit metadata, repository and canonical-publication links when available, a running footer with page numbers, a clickable contents page when a preflight PDF exceeds 20 pages, and a machine-readable manifest. YAML date values are normalized to stable `YYYY-MM-DD` publication or edition dates rather than serializer-specific date strings.

Before and after rendering, the wrapper hashes the canonical Markdown. A source change during rendering is a hard failure. Versioned PDF builds are strict by default: the working-tree bytes must match the declared source commit. `--allow-dirty-preview` is an explicit local-preview escape hatch; those outputs are visibly marked as uncommitted and record both committed and working blob identities.

The final PDF and its manifest are installed as one rollback-protected publication bundle. If manifest finalization fails after the PDF has been staged, the previous PDF/manifest pair is restored rather than leaving a new PDF beside stale provenance.

The manifest records:

- canonical source path;
- source commit and Git blob SHA;
- source SHA-256;
- PDF SHA-256;
- generated timestamp;
- publication date when explicitly present, otherwise an edition date;
- version/status/maturity/draft/license;
- repository URL, `canonical_url`, and `additional_publication_urls` when present;
- page count and TOC decision;
- canonical and rendered figure lists;
- whether Figure 8 was split in the rendition for readability.

## Dense Figure 8

The canonical article keeps **one logical Figure 8**. PDF renditions do not lower the 5 pt Mermaid-label safety floor. Instead, the renderer produces two presentation renditions only for PDF output:

- **Figure 8A — Decision-ownership model**;
- **Figure 8B — Capability-family axis and orthogonality relationship**.

Together Figures 8A–8B preserve the canonical Figure 8 semantics and original caption. The Markdown source is never changed. The current standalone article fails closed unless the reviewed split produces exactly one Figure 8A and one Figure 8B and no unsplit Figure 8; a fingerprint change requires substantive review. This split is recorded in the manifest. Figure 8A begins on its own A4 landscape page; Figure 8B begins on a new page and keeps automatic orientation selection.

The hard technical floor remains **5 pt**. The publication target is **6–7 pt or larger** where the layout allows it.

For unsplit dense diagrams in the living working paper or generic publication export, the renderer may use a dedicated **A2 landscape foldout page** rather than lowering the 5 pt guard. The shorter publication article still prefers the Figure 8A/8B rendition split, so its dense Figure 8 does not depend on the foldout fallback.

## Visual verification

After producing a PDF, render every page to images and generate a contact sheet:

```bash
npm run pdf:verify -- dist/pdf/thinking-systems-when-the-controlled-object-changes.pdf
```

Verification uses `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm` to confirm the reported/rasterized page count, inspect fonts, prove that the running footer and first/last page counters are present, rasterize every page, detect likely blank pages, and generate a contact sheet. It writes page PNGs, the contact sheet, and `visual-verification.json` under `dist/pdf/visual/<pdf-name>/`.

Automated verification is deliberately not a substitute for editorial eyes: human review of the contact sheet remains the final visual acceptance step for clipping, overlap, awkward pagination, and figure readability.

## Durable links

Same-page anchors remain PDF-local. Cross-document repository links are rewritten to durable GitHub source links by default. Set `UA_PDF_PUBLICATION_BASE_URL` when a stable Quartz site should become the publication-link target instead. In GitHub Actions, links use the workflow commit; local exports use the current repository commit unless `UA_PDF_REPOSITORY_REF` overrides it.

## GitHub Actions

**Build integrity** runs the fast PDF unit/regression suite on every pull request together with the normal Quartz build and repository workflow checks.

The separate **Publication render** workflow performs the expensive end-to-end article and working-paper render only when publication sources, Quartz rendering code/styles/configuration, package dependencies, or the publication workflows change. It also supports manual dispatch. The workflow installs Chromium and Poppler, renders both PDFs and manifests, runs visual verification, and uploads the validation bundle for 14 days.

Run **Export research PDF** manually from the Actions tab when a downloadable artifact bundle is needed. The default source is the standalone Thinking Systems publication article. The long-form working paper or another Markdown source under `content/` can be supplied explicitly. The workflow creates the publication-grade PDF and manifest, runs visual verification, and uploads the generated files for 14 days.

The workflows do not deploy Quartz, publish a website, create Medium/LinkedIn renditions, or change research status. Platform-specific images and prose adaptations belong to a separate publication-rendition change.
