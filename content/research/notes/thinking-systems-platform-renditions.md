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
updated: 2026-08-27
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

The editable content source remains [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) until an actual publication decision freezes an exact content edition under [`../publications/`](../publications/). Medium and LinkedIn outputs may change formatting, image placement, table presentation, cover metadata, platform notes, SEO fields, the launch post, and copy/paste convenience packaging. They must not silently change definitions, decision ownership, maturity caveats, attribution, or the Figure 8 relationships.

The machine profile lives at [`../../../quartz/publication/thinking-systems.platforms.json`](../../../quartz/publication/thinking-systems.platforms.json). Generated files remain under `dist/publication/thinking-systems/` and are not committed.

## Generated package

```text
canonical article Markdown
→ reviewed publication SVG/PNG figures and covers
→ platform-safe table presentation
→ absolute durable links
→ Medium article package
→ LinkedIn article package
→ self-contained copy-ready HTML for each platform
→ LinkedIn launch post
→ provenance and readiness manifest
```

`npm run publication:bundle` generates the reviewed assets, the normal Medium/LinkedIn renditions, and the self-contained copy-ready HTML in one pipeline run.

The generated package contains normal review HTML, copy-ready self-contained HTML, Markdown, and plain-text versions; image upload placeholders; curated alt text; SEO metadata; canonical-link guidance; and platform-specific publishing checklists.

The `copy-ready.html` files are distribution conveniences only. They embed the already reviewed platform PNGs as inline `data:` URIs so the operator can download and open one HTML file without keeping a neighboring image folder. The supported copy path is deliberately manual: **Select All → Copy → Paste**. Scripted local-file copy/select controls are not part of the contract because they are unreliable on iPadOS and can vary by browser.

A second copy/paste compatibility rule applies to linked headings. LinkedIn and Medium may preserve heading formatting but drop a hyperlink attached directly to that heading. An upstream platform transform identifies Markdown heading nodes through the Remark AST and, whenever an HTTP(S) hyperlink occurs inside a heading, emits the same URL as a separate visible linked line immediately below it before normal HTML and copy-ready packaging. The copy-ready renderer preserves that protection rather than owning a second heading parser. This rule applies generically to future platform renditions; it is not a hard-coded fix for the current ISO/IEC TR 29119-11 and NIST AI RMF examples.

The complete-package verifier also enforces a 12 px projected no-zoom label floor across every generated platform figure before the artifact is accepted. The LinkedIn cover remains a separate platform upload. The Medium copy-ready rendition includes the generated hero together with all article figures. Because native editors may sanitize clipboard images, the normal PNG bundle and Markdown image-placement guide remain the fallback path.

Figure 3 uses the current reviewed publication comparison and must preserve the canonical distinction between Explicitly Authored Software and the motivating runtime-judgment class; the broader Thinking-System boundary remains a research question where the canonical article leaves it open. Figure 8A and Figure 8B remain two presentation panels of one logical canonical Figure 8 and must travel together with the complete canonical caption. Copy-ready generation only embeds those reviewed assets; it does not regenerate or reinterpret figure semantics.

## Publication boundary

A generated package is a **candidate distribution package**, not proof that an external publication edition already exists. The publication lifecycle follows [`../review-process.md`](../review-process.md#publication-adaptation-and-external-feedback-cycle):

1. generate the candidate package from the current committed adaptation;
2. review every image, caption, table conversion, link, platform preview, attribution boundary, and copy-ready paste result;
3. publish the first external rendition when the candidate is approved;
4. for LinkedIn, capture the exact native article URL and replace `{{LINKEDIN_ARTICLE_URL}}` before publishing the launch post;
5. immediately preserve the exact externally published content edition under `content/research/publications/`;
6. record the principal `canonical_url`, equivalent `additional_publication_urls`, and immutable published-edition identity;
7. only then begin feedback-driven reconciliation or substantive source revision.

Because this generator intentionally targets the editable note under `content/research/notes/`, it always reports `publication_state: candidate` and `publication_ready: false`. The repository publication record created after release is the durable evidence of what external readers actually received.

## Current platform constraints

The machine profile records the current first-party constraints used by the generator, including:

- LinkedIn posts: 3,000 characters; the launch source also preserves a 120-character machine-enforced reserve for the final native article URL and mention expansion; LinkedIn articles: 125,000 characters.
- LinkedIn article cover: 2,000 × 600 pixels, up to 10 MB, JPG/static GIF/PNG.
- LinkedIn SEO title truncation risk above 60 characters; recommended SEO description: 140–160 characters.
- LinkedIn article editing does not currently provide native tables, so tables are expanded into readable labeled sections in that rendition.
- Medium images: JPG/JPEG/GIF/PNG up to 25 MB; at least 1,192 px wide for all image-placement options.
- Medium canonical URL: use import-from-URL where appropriate or set the canonical link manually.

Reverify these values against the official URLs in the machine profile immediately before publication because platform behavior changes independently of the repository.
