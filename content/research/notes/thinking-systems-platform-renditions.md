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
updated: 2026-08-28
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

The editable content source remains [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) until an actual publication decision freezes an exact content edition under [`../publications/`](../publications/). Medium and LinkedIn outputs may change formatting, image placement, table presentation, cover metadata, platform notes, SEO fields, the launch post, and copy/paste convenience packaging. They must not silently change definitions, decision ownership, maturity caveats, attribution, or figure semantics.

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

A generated package is a **candidate distribution package**, not proof that an external publication edition already exists. The publication lifecycle follows [`../review-process.md`](../review-process.md#publication-adaptation-and-external-feedback-cycle):

1. generate the candidate package from the current committed adaptation;
2. review the LinkedIn paste result and the Medium text-plus-manual-image workflow;
3. publish the first approved external rendition;
4. for LinkedIn, capture the exact native article URL and replace `{{LINKEDIN_ARTICLE_URL}}` before publishing the launch post;
5. immediately preserve the exact externally published content edition under `content/research/publications/`;
6. record the principal `canonical_url`, equivalent `additional_publication_urls`, and immutable published-edition identity;
7. only then begin feedback-driven reconciliation or substantive source revision.

Because this generator targets the editable note under `content/research/notes/`, it always reports `publication_state: candidate` and `publication_ready: false`. The repository publication record created after release is the durable evidence of what external readers actually received.

## Current platform constraints

The machine profile records the first-party constraints used by the generator, including LinkedIn post/article and cover limits, LinkedIn SEO guidance and table limitations, and Medium image and canonical-URL guidance. Reverify those values against the official references in the profile immediately before publication because platform behavior changes independently of the repository.
