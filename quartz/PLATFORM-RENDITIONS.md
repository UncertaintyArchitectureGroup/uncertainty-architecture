# Medium and LinkedIn rendition export

This publishing layer converts one committed Thinking Systems publication source into platform-ready Medium and LinkedIn distribution packages without making either platform a second conceptual authority.

## Commands

```bash
npm run publication:assets
npm run publication:platforms
npm run publication:protect-links
npm run publication:furniture
npm run publication:copy-ready
npm run publication:verify-package

# or generate the complete platform sequence
npm run publication:bundle
```

For an explicitly dirty local preview only, run the platform generation step with `publication:platforms -- --allow-dirty-preview`.

Generated rendition outputs remain under `dist/publication/thinking-systems/`. A bounded set of PNGs is also committed under `content/research/notes/thinking-systems-platform-assets/` solely to provide Medium with ordinary immutable HTTPS image sources during copy/paste.

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

content/research/notes/thinking-systems-platform-assets/
  medium-hero.png
  figures/*.png
```

`article.html` is the normal rich review surface with local image references. `article.md` is the explicit image-placement and alt-text guide. `article.txt` is a plain-text fallback.

## Copy-ready image transport

The supported interaction is deliberately simple: open the platform-specific `copy-ready.html`, use **Select All → Copy**, and paste into the native editor. No JavaScript copy/select controls are emitted because local-file clipboard behavior varies across browsers and iPadOS.

The two platforms use different image transport because their paste sanitizers behave differently:

- **LinkedIn**: the nine article figures are embedded as `data:` URIs. The LinkedIn article cover remains a separate native upload.
- **Medium**: `data:` images are not used. The hero and nine article figures are referenced through ordinary `https://raw.githubusercontent.com/...` URLs pinned to the immutable Git commit that contains the matching materialized PNG assets.

Before emitting the Medium copy-ready file, the generator byte-compares every current generated PNG against its committed materialized counterpart. Generation fails if the repository asset is stale. The materialized PNGs therefore serve only as transport for Medium; they do not become a content or semantic authority.

The CI artifact still carries normal PNG files and `article.md` as a manual-upload fallback if either platform changes its clipboard behavior.

## Heading-link preservation contract

LinkedIn and Medium can drop hyperlinks when the hyperlink is attached directly to a heading during rich-text paste. The protection is applied before copy-ready rendering so every platform Markdown and HTML rendition carries the same recoverable source reference.

For every Markdown heading containing one or more HTTP(S) hyperlinks, the pipeline inserts a normal body line immediately below the heading:

```markdown
### AI-based system (ISO/IEC TR 29119-11)

**Source:** <https://www.iso.org/standard/79016.html>
```

For multiple distinct links in one heading:

```markdown
**Sources:** <https://example.com/a> · <https://example.com/b>
```

Links are emitted in encounter order and duplicate URLs inside one heading are collapsed. Ordinary body hyperlinks are not duplicated. Markdown headings are identified through the Remark AST, so ATX and Setext headings, inline links, reference links, and inline HTML anchors are handled without rewriting fenced-code examples. The mechanism is generic rather than hard-coded to the current ISO/NIST examples.

## Platform presentation transforms

The platform asset tree keeps SVG masters for reuse, while the platform rendition artifact exposes PNG assets for Medium and LinkedIn. Mermaid figures are rasterized in Chromium because Mermaid HTML labels live in SVG `foreignObject` nodes that non-browser rasterizers can silently drop.

The LinkedIn rendition expands Markdown tables into labeled sections because the current LinkedIn article editor does not provide native tables. Medium receives the same semantic table expansion in this review package so both platform copies remain easy to compare against the source. This is a presentation transformation, not a change in claim content.

The platform pipeline does **not** change the canonical article figure layout. Figures 1–7 use the current source-defined layout. Figure 8A and Figure 8B remain two presentation panels of one logical canonical Figure 8, must travel together, and share the complete canonical caption.

## CI package

`Export platform renditions` is the platform-facing review workflow. It checks out the exact PR head for candidate provenance and runs:

```text
locked dependency install
→ platform regression tests
→ publication asset generation
→ LinkedIn/Medium rendition generation
→ heading-link protection
→ publication furniture
→ platform-specific copy-ready HTML
→ final platform-package verification
→ one uploaded artifact: thinking-systems-platform-renditions
```

The uploaded artifact contains LinkedIn and Medium renditions, copy-ready HTML, hero/cover/social images, figure PNGs, launch-post/checklist material, and manifests. PDF generation and PDF verification are intentionally outside this workflow and outside this PR's distribution scope.

The final verifier checks candidate state and exact-head provenance, output digests, nine platform figure identities with Figure 8A/B coupling, heading-link fallbacks, publication furniture, absence of copy-helper leakage, and the platform-specific image transport: nine embedded LinkedIn figures versus ten immutable HTTPS Medium images.

## Provenance and publication readiness

The article source must match the declared Git commit unless `--allow-dirty-preview` is used explicitly. On pull requests, the distribution workflow checks out and records the exact PR head rather than GitHub's synthetic merge-preview SHA.

The platform manifest records, among other things:

- candidate source commit, Git blob identities, and source SHA-256;
- LinkedIn launch-post and machine-profile SHA-256 values;
- publication-assets manifest digest;
- output-file digests, including copy-ready HTML;
- LinkedIn character counts;
- Figure 8 semantic fingerprint and coupling state;
- explicit `publication_state: candidate` / `publication_ready: false` semantics;
- heading-link protection state and fallback counts;
- LinkedIn `embedded-data-uri` image strategy;
- Medium `immutable-raw-github-url` image strategy, materialized-asset path, and immutable asset commit;
- manual select-all/copy behavior.

This generator targets the editable publication draft under `content/research/notes/`, so it never claims that its output is already a frozen publication edition. Generate and review the candidate package, publish the approved external rendition, immediately preserve the exact published content under `content/research/publications/`, record its URLs and immutable identity, and only then begin feedback-driven revision.

## Current platform constraints

The machine profile at `quartz/publication/thinking-systems.platforms.json` records the first-party platform constraints used by validation. Recheck those references immediately before release because platform limits can change independently of this repository.

Current configured values include:

- LinkedIn post: 3,000 characters, with a stricter review target and reserve for the final native article URL and mentions;
- LinkedIn article: 125,000 characters;
- LinkedIn article cover: 2,000 × 600, maximum 10 MB;
- LinkedIn social preview: 1,200 × 627;
- LinkedIn SEO title/description guidance encoded by the profile;
- Medium images: maximum 25 MB and at least 1,192 px wide for full placement options;
- Medium hero: 1,600 × 840.
