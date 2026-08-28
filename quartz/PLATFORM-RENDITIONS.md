# Medium and LinkedIn rendition export

This publishing layer converts one committed Thinking Systems publication source into platform-ready LinkedIn and Medium distribution packages without making either platform a second conceptual authority.

## Commands

```bash
npm run publication:assets
npm run publication:platforms
npm run publication:protect-links
npm run publication:furniture
npm run publication:copy-ready
npm run publication:verify-package

# Generate the complete platform sequence
npm run publication:bundle
```

For an explicitly dirty local preview only, run the platform-generation step with `publication:platforms -- --allow-dirty-preview`, then run the remaining stages.

Generated outputs remain under `dist/publication/thinking-systems/`. PDF generation and PDF verification are owned by the separate repository PDF pipeline and are not part of this workflow or its artifact.

```text
dist/publication/thinking-systems/
  figures/png/
  cover-linkedin-article.png
  social-preview.png
  medium-hero.png
  assets.manifest.json
  renditions/
    copy-ready-readme.md
    figure-08-shared-caption.md
    linkedin/
      article.html
      copy-ready.html
      article.md
      article.txt
      launch-post.txt
      seo.json
      publishing-checklist.md
    medium/
      article.html
      copy-ready.html
      article.md
      article.txt
      canonical-url.txt
      publishing-checklist.md
      upload/
        00-medium-hero.png
        01-figure-01.png
        ...
        08-figure-08a.png
        09-figure-08b.png
        README.md
    platform-renditions.manifest.json
```

`article.html` is the normal rich review surface with local image references. `article.md` is the exact image-placement and alt-text guide. `article.txt` is the plain-text fallback.

## Copy-ready behavior

The supported interaction is deliberately manual:

```text
open copy-ready.html
→ Select All
→ Copy
→ Paste into the native editor
```

No JavaScript Copy/Select controls are emitted because local-file Clipboard APIs and scripted selection are unreliable across iPadOS and browsers.

Both copy-ready files are self-contained and display their article images through embedded `data:` URIs:

- **LinkedIn:** the tested path preserves the nine embedded article figures during paste. The native LinkedIn article cover remains a separate upload.
- **Medium:** the page displays the generated hero and all nine figures, so it remains a complete local visual-review surface. Practical iPad testing showed, however, that Medium preserves the pasted rich text while dropping clipboard images. The pipeline therefore does not claim one-step Medium image transfer.

The supported Medium publication path is:

```text
open medium/copy-ready.html and verify the complete visual article
→ Select All → Copy → paste the rich text into Medium
→ use medium/article.md for exact positions and alt text
→ upload the ten ordered PNGs from medium/upload/
```

The upload kit contains the hero, Figures 1–7, Figure 8A, Figure 8B, and a short README. It is generated from the same reviewed platform assets as the article rendition; no duplicate image tree is committed under `content/research/`.

## Heading-link preservation contract

LinkedIn and Medium can drop a hyperlink attached directly to a heading during rich-text paste. Protection is applied before copy-ready rendering so every platform Markdown and HTML rendition carries the same recoverable source reference.

For every Markdown heading containing one or more HTTP(S) links, the pipeline inserts a normal body line immediately below the heading:

```markdown
### AI-based system (ISO/IEC TR 29119-11)

**Source:** <https://www.iso.org/standard/79016.html>
```

Multiple distinct URLs are emitted in deterministic encounter order, and duplicates inside one heading are collapsed. Ordinary body links are not duplicated. The transform uses the Remark AST, supports ATX and Setext headings, inline links, reference links, and inline HTML anchors, and does not rewrite fenced-code examples.

## Platform presentation transforms

The platform asset tree keeps SVG masters for reuse, while the downloadable platform package exposes PNG assets. Mermaid figures are rasterized in Chromium so Mermaid `foreignObject` labels survive and the PNGs have an opaque white background.

The LinkedIn rendition expands Markdown tables into labeled sections because the LinkedIn article editor does not provide native tables. Medium receives the same semantic expansion in this review package so both platform copies remain easy to compare against the source. This is a presentation transformation, not a change in claim content.

The platform pipeline does not change the canonical article figure layout:

- Figure 3 keeps its existing reviewed publication rendition.
- Figure 7 remains unchanged from the canonical source.
- Figure 8A and Figure 8B remain two panels of one logical Figure 8, must travel together, and share the complete caption.

## CI package

`Export platform renditions` checks out the exact PR head for candidate provenance and runs:

```text
locked dependency install
→ platform regression tests
→ publication asset generation
→ LinkedIn/Medium rendition generation
→ heading-link protection
→ publication furniture
→ self-contained copy-ready HTML
→ Medium ordered upload-kit generation
→ final platform-package verification
→ one uploaded artifact: thinking-systems-platform-renditions
```

The verifier checks:

- `publication_state: candidate` and `publication_ready: false`;
- exact-head provenance and output digests;
- nine platform figure identities and Figure 8A/B coupling;
- nine embedded LinkedIn images;
- ten embedded Medium review images whose decoded bytes are byte-identical to the ten ordered upload PNGs;
- an ordered Medium upload kit with ten PNGs plus instructions;
- explicit `medium_clipboard_images_supported: false` and `medium_manual_upload_required: true`;
- linked-heading fallbacks, publication furniture, and absence of copy-helper/provenance leakage.

## Publication lifecycle

Generated outputs remain candidate distribution renditions, not frozen publication editions.

```text
generate candidate package
→ human LinkedIn/Medium review
→ publish approved external rendition
→ capture exact publication URLs
→ immediately preserve the exact published edition under content/research/publications/
→ record immutable edition identity
→ only then begin feedback-driven revision
```

The machine profile at `quartz/publication/thinking-systems.platforms.json` records the platform limits and official references used by validation. Recheck those references before release because platform behavior changes independently of the repository.
