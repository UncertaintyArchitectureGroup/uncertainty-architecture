---
title: "Presentation asset provenance"
artifact_type: repository-guide
status: informative
maturity: draft
module: publishing
draft: true
topics:
  - provenance
tags:
  - ua/module/publishing
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/provenance
---

# Presentation asset provenance

- File: [ai-two-roles.png](ai-two-roles.png)
- Created: 2026-09-21, using the built-in OpenAI imagegen tool at the maintainer's request.
- Use: one foreground conceptual illustration on slide 1 only. Two concrete scenes show a developer using an AI coding assistant and an end user asking an AI travel product to make an itinerary; it is not a measured result or an architecture diagram.
- The image contains no slide title, evidence labels or numeric data. All slide text remains editable. The solid slide background is independent of the image.
- The generated asset was copied unchanged into this repository. Slides 2–14 use native editable objects.

## Generation prompt

Use case: illustration-story. Asset type: foreground illustration for a dark technical conference PowerPoint cover. Create a clean, clear editorial illustration with two balanced scenes side by side in a very wide 3:1 horizontal composition, 3072x1024 preferred. Background is uniformly near-black #0B0F14, no visible panels, no border. LEFT SCENE: a human software engineer seated at a desk, using a large desktop code editor. The monitor clearly shows short colored code-like strokes and a cyan AI-assistant sparkle beside proposed code. Human hand on keyboard, human owns the work, AI is a tool helping write software. RIGHT SCENE: a different human end user holding a phone and looking at a large floating software application window. A speech bubble from the user contains a simple suitcase and calendar pictogram; inside the app, a warm amber AI sparkle interprets the request and presents a small travel itinerary with a route and three meaningful icons. This illustrates AI as part of the product's behavior at runtime. These are two independent scenes, no pipeline or connecting tube between them. Style: sophisticated flat editorial illustration with subtle dimensional shading, crisp silhouettes, restrained detail, readable at slide scale. Human figures and recognizable computer/phone objects should carry the meaning. Cyan #28C7F7 accents on the left, amber #F5B61C accents on the right, off-white and slate neutrals. Plenty of clear near-black separation between the scenes. Keep all subjects safely inset. No headings, letters, words, numbers, labels, watermarks, company logos, robots, brains, glowing boxes, industrial machines, or decorative circuitry. All slide copy will be added separately as editable text.

## Roboto font bundle

- File: [roboto-fonts.zip](roboto-fonts.zip), retrieved 2026-09-21 from [Google Fonts’ Roboto source](https://github.com/google/fonts/tree/main/ofl/roboto), version 3.015; 2026. Copyright 2011 The Roboto Project Authors. The original SIL Open Font License 1.1 is included unchanged as `OFL.txt`.
- Includes the untouched variable source, full static Regular/Bold TTF instances (weight 400/700, width 100), uncompressed EOT 2.0001 font data and a per-file SHA-256 provenance record. FontTools produced the static instances; family/style names were normalized for the two styles. No glyph subsetting. Embedding permission `fsType=0`.
- Both styles are embedded in the PPTX via native font relationships. The EOT wrappers follow the [Microsoft EOT format submission](https://www.w3.org/submissions/EOT/); this is a format reference, not a W3C Recommendation. Install the archived TTF files for authoring. The arrow U+2192 remains application font fallback; its source text is unchanged.
- The maintainer explicitly requested this font replacement across all slides after freezing slides 1–8. Only typography and font packaging are authorized by that follow-up; slide wording, numbers, notes and geometry are preserved and the freeze record is refreshed after review.
