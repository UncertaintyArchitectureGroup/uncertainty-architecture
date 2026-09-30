---
title: "Platform Rendition Profile — Thinking Systems"
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - provenance
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/provenance
  - ua/topic/repository-architecture
created: 2026-08-21
updated: 2026-09-18
language: en
license: CC-BY-4.0
draft: true
source_basis:
  - thinking-systems-publication-draft.md
  - thinking-systems-linkedin-launch-post.md
related:
  - ../review-process.md
  - thinking-systems-publication-draft.md
---

# Platform Rendition Profile — Thinking Systems

This note defines the distribution boundary for Medium and LinkedIn renditions of _Thinking Systems: When the Controlled Object Changes_. It is non-normative research and does not create a second conceptual version of the article.

## Source relationship

External publication has occurred on LinkedIn and Medium, with a PDF rendition also published. The publication Markdown in [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) is now a **frozen authoring source**: the maintainer confirmed on September 18, 2026 that it did not change after publication and does not intend to develop it further. Its preserved repository edition is [`../publications/thinking-systems-when-the-controlled-object-changes.md`](../publications/thinking-systems-when-the-controlled-object-changes.md). Future substantive research development belongs in the living long-form manuscript, not in this frozen publication source.

Medium and LinkedIn outputs may differ only in formatting, image placement, table presentation, cover metadata, platform notes, SEO fields, the launch post, and copy/paste packaging unless a later publication is explicitly recorded as a new content edition. Exact platform URLs and remaining publication metadata are pending maintainer reconciliation.

The machine profile lives at [`../../../quartz/publication/thinking-systems.platforms.json`](../../../quartz/publication/thinking-systems.platforms.json). Generated rendition files remain under `dist/publication/thinking-systems/` and are not conceptual authorities.

## Generated platform package

```text
canonical article Markdown
→ reviewed platform figures and hero/cover assets
→ platform-safe table presentation and durable links
→ structural linked-heading URL protection
→ publication furniture
→ LinkedIn and Medium candidate renditions
→ self-contained copy-ready HTML
→ Medium ordered manual-upload kit
→ platform manifest and final verification
```

`npm run publication:bundle` generates the platform assets and renditions. `npm run publication:verify-package` validates the completed package. PDF generation is outside this PR and remains owned by the separate repository PDF pipeline.

The package contains normal review HTML, copy-ready HTML, Markdown, plain text, curated alt text, SEO metadata, canonical-link guidance, the LinkedIn launch post and checklists, and the platform assets needed for publication.

## Copy and image transport

The supported local interaction is manual **Select All → Copy → Paste**. Scripted local-file Copy/Select controls are not part of the contract because they are unreliable on iPadOS and vary by browser.

Both `copy-ready.html` files are self-contained and display their article images through embedded `data:` URIs. This keeps the local review surface visually complete without a neighboring folder or network access.

Practical testing produced different platform behavior:

- **LinkedIn** preserved the nine embedded article figures during paste. The LinkedIn cover remains a separate native upload.
- **Medium** preserved the pasted rich text but dropped the clipboard images. A later attempt to replace embedded images with remote repository URLs also made the local review page lose its pictures and did not establish a reliable image-transfer path. That experiment was removed.

The supported Medium path therefore separates text transfer from image upload:

1. open `medium/copy-ready.html` and verify the complete article with the hero and all nine figures visible;
2. use **Select All → Copy → Paste** for the rich text;
3. use `medium/article.md` for the exact image positions and alt text;
4. upload the ten ordered PNGs from `medium/upload/`.

The upload kit contains the hero, Figures 1–7, Figure 8A, Figure 8B, and a short README. It is generated from the same reviewed platform assets as the rendition and remains inside the CI artifact. No duplicate transport-image tree is committed under `content/research/`.

## Heading-link preservation

LinkedIn and Medium may preserve heading formatting while dropping a hyperlink attached directly to a heading. An upstream transform identifies Markdown heading nodes through the Remark AST and emits every HTTP(S) heading URL as a separate visible linked line immediately below the heading before normal HTML and copy-ready packaging.

The mechanism supports ATX and Setext headings, inline links, reference links, and inline HTML anchors; does not rewrite fenced-code examples; does not duplicate ordinary body links; deduplicates repeated URLs inside one heading; and is idempotent. The current adaptation has two such headings after table expansion: the ISO/IEC TR 29119-11 and NIST AI RMF references.

## Figure boundary

Platform packaging consumes reviewed assets without changing the canonical article argument or source layout.

- Figure 3 keeps its existing reviewed publication comparison.
- Figure 7 remains unchanged from the canonical source.
- Figure 8A and Figure 8B remain two presentation panels of one logical Figure 8, must travel together, and share the complete canonical caption.

## Publication boundary

A generated package remains a reproducible distribution artifact; external publication is now independently recorded by the frozen repository edition rather than inferred from package generation. The publication lifecycle follows [`../review-process.md`](../review-process.md#publication-adaptation-and-external-feedback-cycle):

1. preserve the frozen publication source and repository edition;
2. retain generated packages as reproducible rendition artifacts rather than conceptual authorities;
3. add the exact LinkedIn and Medium URLs and remaining platform metadata when supplied by the maintainer;
4. treat any later substantive change to the publication text as a new content edition rather than silently rewriting this one;
5. continue feedback-driven research in the living long-form manuscript.

The generator still targets the historical path under `content/research/notes/` for compatibility, but that source is now frozen. Generator fields such as `publication_state: candidate` describe a generated package, not the publication status of the content edition. The repository publication record is the durable publication-provenance surface.

## Current platform constraints

The machine profile records the first-party constraints used by the generator, including LinkedIn post/article and cover limits, LinkedIn SEO guidance and table limitations, and Medium image and canonical-URL guidance. Reverify those values against the official references in the profile immediately before publication because platform behavior changes independently of the repository.
