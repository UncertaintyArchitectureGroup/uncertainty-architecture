# Medium and LinkedIn rendition export

This publishing layer converts one committed Thinking Systems publication source into platform-ready distribution packages without making Medium or LinkedIn a second conceptual authority.

## Commands

```bash
npm run publication:assets
npm run publication:platforms
npm run publication:protect-links
npm run publication:furniture
npm run publication:copy-ready

# after the standalone PDF exists, verify the complete distribution package
npm run publication:verify-package

# or generate the complete platform sequence
npm run publication:bundle
```

For an explicitly dirty local preview only, run the same sequence with `publication:platforms -- --allow-dirty-preview`.

Generated outputs remain untracked under `dist/publication/thinking-systems/`. The dedicated GitHub Actions export additionally renders and strictly verifies the standalone research PDF before uploading one complete publication artifact.

```text
dist/
  pdf/
    thinking-systems-when-the-controlled-object-changes.pdf
    thinking-systems-when-the-controlled-object-changes.pdf.manifest.json
    visual/
  publication/thinking-systems/
    figures/svg/
    figures/png/
    cover-linkedin-article.png
    social-preview.png
    medium-hero.png
    assets.manifest.json
    renditions/
      copy-ready-readme.md
      figure-08-shared-caption.md
      medium/
        article.html
        copy-ready.html
        article.md
        article.txt
        canonical-url.txt
        publishing-checklist.md
      linkedin/
        article.html
        copy-ready.html
        article.md
        article.txt
        launch-post.txt
        seo.json
        publishing-checklist.md
      platform-renditions.manifest.json
```

`article.html` is the normal rich review surface with local image references. `article.md` is the explicit image-placement and alt-text guide. `article.txt` is a plain-text fallback.

`copy-ready.html` is a **single self-contained local file** intended for the fastest manual publication path. The generator embeds the article PNGs as `data:` URIs and removes internal upload-file labels and generated provenance. The supported interaction is deliberately simple: open the one HTML file, use **Select All → Copy**, and paste into the native LinkedIn or Medium editor. No JavaScript copy/select controls are emitted because local-file clipboard and scripted-selection behavior is not reliable across iPadOS and other browsers.

## Heading-link preservation contract

LinkedIn and Medium can drop hyperlinks when the hyperlink is attached directly to a heading during rich-text paste. The protection is therefore applied **before** copy-ready rendering so every platform Markdown and HTML rendition carries the same recoverable source reference.

For every `h1`–`h6` / Markdown heading containing one or more HTTP(S) hyperlinks, the pipeline inserts a normal body line immediately below the heading:

```markdown
### AI-based system (ISO/IEC TR 29119-11)

**Source:** <https://www.iso.org/standard/79016.html>
```

For multiple distinct links in one heading, the deterministic representation is:

```markdown
**Sources:** <https://example.com/a> · <https://example.com/b>
```

Links are emitted in encounter order and duplicate URLs inside one heading are collapsed. Ordinary body hyperlinks are never duplicated. The same mechanism runs for LinkedIn and Medium. Markdown headings are identified through the Remark AST rather than line regexes, so ATX and Setext headings, inline links, reference links, and inline HTML anchors are handled without rewriting fenced-code examples; generated HTML receives the equivalent protection. The mechanism is generic for future articles rather than hard-coded to the current ISO/NIST examples. Copy-ready HTML preserves the already-generated fallback instead of creating a second one.

No adjacent image folder is required for the primary path. LinkedIn's article cover remains a separate upload, while the Medium copy-ready file includes the generated hero plus the nine article figures. Clipboard/image sanitization remains platform-dependent, so the generated PNG files and `article.md` placement guide remain the fallback if a platform drops an embedded image during paste.

The local publication asset tree keeps SVG masters for Quartz/PDF/website reuse, but the GitHub **platform rendition artifact intentionally exposes PNG upload assets** for Medium and LinkedIn. Mermaid figures are rasterized in Chromium rather than through librsvg/Sharp because Mermaid HTML labels live in SVG `foreignObject` nodes that non-browser rasterizers may silently drop.

The LinkedIn rendition expands Markdown tables into labeled sections because the current LinkedIn article editor does not provide native tables. Medium receives the same semantic table expansion in this review package so the two platform copies remain easy to compare against one another; this is a presentation transformation, not a change in claim content.

## Complete CI publication package

`Export platform renditions` is the publication-facing review workflow. It checks out the exact PR head for candidate provenance, then runs:

```text
locked dependency install
→ platform/publication regression tests
→ Figure 8 semantic/readability verification
→ strict PDF + manifest verification
→ publication asset generation
→ LinkedIn/Medium rendition generation
→ heading-link protection
→ publication furniture
→ self-contained copy-ready HTML
→ final package verification (PDF, provenance, figures, furniture, fallbacks)
→ one uploaded artifact: thinking-systems-platform-renditions
```

The artifact therefore contains the standalone verified PDF, PDF manifest/visual verification outputs, LinkedIn and Medium renditions, copy-ready HTML, hero/cover/social images, reviewed figure PNGs, launch-post/checklist material, and manifests. The 61-page living working-paper PDF remains a Build Integrity validation object and is intentionally not duplicated into the distribution package.

## Figure contract

The renderer consumes the current `publication:assets` manifest rather than inventing its own figure filenames. The final package verifier rejects any platform figure whose projected minimum label falls below the 12 px no-zoom publication floor; this gate applies to Figures 1–7 as well as the Figure 8 panels.

- Figures 1–7 use the current reviewed publication asset for that logical figure.
- Figure 3 therefore uses the post-PDF-review side-by-side, top-down publication rendition rather than returning to the older Mermaid presentation.
- Figure 8A and Figure 8B remain presentation panels of one logical canonical Figure 8. They must be published together and the complete canonical Figure 8 caption is emitted as `figure-08-shared-caption.md`.

The copy-ready step does not regenerate or reinterpret figures. It only embeds the already reviewed platform PNG assets into generated HTML, so figure semantics continue to be owned by the shared publication asset pipeline.

## Provenance and publication readiness

The package is strict about source provenance. The article source must match the declared Git commit unless `--allow-dirty-preview` is used explicitly. On pull requests, the distribution workflow checks out and records the exact PR head rather than the synthetic GitHub merge-preview SHA; on pushes it falls back to `github.sha`.

The platform manifest records:

- candidate source commit, Git blob identities, and source SHA-256;
- LinkedIn launch-post and machine-profile SHA-256 values;
- the publication-assets manifest digest;
- output-file digests, including copy-ready HTML;
- LinkedIn character counts;
- Figure 8 semantic fingerprint;
- explicit `publication_state: candidate` / `publication_ready: false` semantics for this editable-source generator;
- principal `canonical_url` and `additional_publication_urls` when already recorded;
- the required LinkedIn article-URL binding state for the launch post;
- heading-link protection state and fallback counts;
- copy-ready state, embedded-image counts, and manual select-all/copy behavior.

This generator deliberately targets the editable publication draft under `content/research/notes/`, so it never claims that its output is already a frozen publication edition. Generate and review the candidate package, publish the approved external rendition, then immediately preserve the exact published content under `content/research/publications/`, record the principal canonical URL plus equivalent platform URLs and immutable source identity, and only then begin feedback-driven revision.

## Current platform constraints

The machine profile at `quartz/publication/thinking-systems.platforms.json` records the first-party platform constraints used by validation. Recheck those official references immediately before release because platform limits can change independently of this repository.

Current configured values include:

- LinkedIn post: 3,000 characters, with the launch source required to stay below a stricter 2,900-character review target and to retain a machine-enforced 120-character reserve for the final native article URL and mention expansion;
- LinkedIn article: 125,000 characters;
- LinkedIn article cover: 2,000 × 600, maximum 10 MB;
- LinkedIn social preview: 1,200 × 627;
- LinkedIn SEO title: 60-character truncation boundary used by this package; SEO description: 140–160 characters;
- Medium images: maximum 25 MB and at least 1,192 px wide for full placement options;
- Medium hero generated by the shared asset pipeline: 1,600 × 840.
