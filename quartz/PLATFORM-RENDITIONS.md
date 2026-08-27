# Medium and LinkedIn rendition export

This publishing layer converts one committed Thinking Systems publication source into platform-ready distribution packages without making Medium or LinkedIn a second conceptual authority.

## Commands

```bash
npm run publication:assets
npm run publication:platforms
npm run publication:copy-ready

# or all three
npm run publication:bundle
```

For an explicitly dirty local preview only:

```bash
npm run publication:assets
npm run publication:platforms -- --allow-dirty-preview
npm run publication:copy-ready
```

Generated outputs remain untracked:

```text
dist/publication/thinking-systems/
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

`copy-ready.html` is a **single self-contained local file** intended for the fastest manual publication path. The generator embeds the article PNGs as `data:` URIs and removes the internal upload-file labels and generated provenance. The supported interaction is deliberately simple: open the one HTML file, use **Select All → Copy**, and paste into the native LinkedIn or Medium editor. No JavaScript copy/select controls are emitted because local-file clipboard and scripted-selection behavior is not reliable across iPadOS and other browsers.

LinkedIn and Medium can also drop hyperlinks when the hyperlink is attached directly to a heading during rich-text paste. To make this failure visible and recoverable, the copy-ready postprocessor scans every `h1`–`h6`; when a heading contains an HTTP(S) hyperlink, it emits the same URL as a separate visible linked line immediately below that heading. This is a generic copy/paste compatibility transform and is not specific to the current ISO/NIST examples or to this article.

No adjacent image folder is required for the primary path. LinkedIn's article cover remains a separate upload, while the Medium copy-ready file includes the generated hero plus the nine article figures. Clipboard/image sanitization remains platform-dependent, so the generated PNG files and `article.md` placement guide remain the fallback if a platform drops an embedded image during paste.

The local publication asset tree keeps SVG masters for Quartz/PDF/website reuse, but the GitHub **platform rendition artifact intentionally excludes SVG**. Medium and LinkedIn upload packages contain opaque white-background PNG figures only. Mermaid figures are rasterized in Chromium rather than through librsvg/Sharp because Mermaid HTML labels live in SVG `foreignObject` nodes that non-browser rasterizers may silently drop.

The LinkedIn rendition expands Markdown tables into labeled sections because the current LinkedIn article editor does not provide native tables. Medium receives the same semantic table expansion in this review package so the two platform copies remain easy to compare against one another; this is a presentation transformation, not a change in claim content.

## Figure contract

The renderer consumes the current `publication:assets` manifest rather than inventing its own figure filenames.

- Figures 1–7 use the current reviewed publication asset for that logical figure.
- Figure 3 therefore uses the post-PDF-review side-by-side, top-down publication rendition rather than returning to the older Mermaid presentation.
- Figure 8A and Figure 8B remain presentation panels of one logical canonical Figure 8. They must be published together and the complete canonical Figure 8 caption is emitted as `figure-08-shared-caption.md`.

The copy-ready post-processing step does not regenerate or reinterpret figures. It only embeds the already reviewed platform PNG assets into the generated HTML, so figure semantics continue to be owned by the shared publication asset pipeline.

## Provenance and publication readiness

The package is strict about source provenance. The article source must match the declared Git commit unless `--allow-dirty-preview` is used explicitly. The platform manifest records:

- candidate source commit, Git blob identities, and source SHA-256;
- LinkedIn launch-post and machine-profile SHA-256 values;
- the publication-assets manifest digest;
- output-file digests, including the copy-ready HTML files;
- LinkedIn character counts;
- Figure 8 semantic fingerprint;
- explicit `publication_state: candidate` / `publication_ready: false` semantics for this editable-source generator;
- principal `canonical_url` and `additional_publication_urls` when already recorded;
- the required LinkedIn article-URL binding state for the launch post;
- copy-ready state, embedded-image counts, manual select-all/copy behavior, and heading-link fallback counts.

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
