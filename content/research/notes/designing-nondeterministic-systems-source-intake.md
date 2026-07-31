---
title: Designing Non-Deterministic Systems Source Intake
artifact_type: research-note
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - control-loop
  - sdlc
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/thinking-systems
  - ua/topic/control-loop
source_title: Designing Non-Deterministic Systems — Maintaining Engineering Rigor in the AI Era
source_format: pptx
preserved_format: pdf-export
preserved_file: "content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
updated: 2026-07-31
license: CC-BY-4.0
---

# Designing Non-Deterministic Systems Source Intake

## Purpose

This note records the presentation deck used as a synthesis source for Uncertainty Architecture so that the Research Track distinguishes source evidence, preserved repository material, and explicit framework decisions.

## Source state

The maintainer-supplied original PPTX is the working source used for slide-level review and framework extraction.

The original PPTX is not currently preserved as a repository file. The repository preserves a PDF export under [`content/raw/`](../../raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf). The PDF provides an archival snapshot; it is not a substitute for the original PPTX when slide order, speaker notes, editable content, or presentation-specific detail matters.

Future work may preserve the original PPTX in `content/raw/` when the file and its licensing and attribution state are ready for repository storage. Until then, this intake note is the canonical repository record of the source relationship.

The deck has not been converted into a complete reviewable Markdown transcript or normalized repository edition. Slide content remains research evidence and does not become normative merely because it has been reviewed or preserved.

## Why the source matters

The deck consolidates UA concepts for a practitioner audience, including:

- the shift from deterministic software assumptions to Thinking Systems;
- non-zero runtime variance and probabilistic operating space;
- the AI–code uncertainty boundary;
- control-theory framing for model-mediated systems;
- actuators, sensors, controllers, evidence, and corrective action;
- functional locations where Model Judgment creates value;
- lifecycle and operating-model implications;
- system-level risks that extend beyond model quality;
- the relationship between Requirements, approved business tolerances, Correctness, and Bugs.

Because a presentation compresses arguments and may omit qualifications used in longer publications, its claims must be translated through explicit framework review rather than copied directly.

## Slides 1–6 framework-transfer state

The maintainer-defined slides 1–6 transfer scope has been reviewed against the original PPTX and translated into the following repository components:

- [`00-doctrine/requirements-correctness-and-bugs.md`](../../../00-doctrine/requirements-correctness-and-bugs.md) — mixed Requirements, Operating Envelopes, Correctness, Bugs, and diagnostic sources;
- [`00-doctrine/model-judgment-placement.md`](../../../00-doctrine/model-judgment-placement.md) — Input Interpretation, Decision Logic, and Output Mediation as a functional taxonomy;
- [`01-patterns/judgment-node-boundary.md`](../../../01-patterns/judgment-node-boundary.md) — explicit boundaries around consequential Judgment Nodes;
- [`01-patterns/thinking-system-review.md`](../../../01-patterns/thinking-system-review.md) — one lightweight review flow with full model-mediated DoR and DoD extensions, a distinct Release Gate, responsibility bundles, and reassessment;
- [`01-patterns/thinking-system-review-template.md`](../../../01-patterns/thinking-system-review-template.md) — one living SMB working artifact;
- [`03-reference-architectures/judgment-placement-examples.md`](../../../03-reference-architectures/judgment-placement-examples.md) — isolated and composite placement reference architectures;
- [`content/research/framework-traceability.md`](../framework-traceability.md) — current source-to-framework decisions and resolved presentation shorthand.

The slides 1–6 transfer is complete at the current draft-framework level. Later application evidence may still refine the resulting doctrine, patterns, and template.

## Interpretation decisions

The transfer preserves the deck's engineering concerns while narrowing presentation shorthand:

- a statistical excursion or undesirable tail event is evidence, not automatically a Bug;
- a Bug is a system-level violation of an approved Requirement;
- the Operating Envelope is part of the complete Requirement, not its synonym;
- deterministic verification remains necessary alongside behavioral evidence;
- sample sizes, confidence methods, metrics, tolerances, and thresholds are context-derived rather than universal;
- Input Interpretation, Decision Logic, and Output Mediation are functional placement classes, not a mandatory pipeline;
- responsibility bundles and Human Authority do not imply mandatory job titles;
- reference architectures remain non-prescriptive.

## Remaining follow-up

1. Preserve the original PPTX in `content/raw/` when appropriate and available for repository storage.
2. Create a complete Markdown transcript or normalized repository edition with slide-level provenance only when that work becomes useful.
3. Continue reviewing later deck sections against the broader publication corpus.
4. Record contradictions, superseded claims, and newly extracted entities in the existing research-to-framework traceability matrix.
5. Use worked applications to test whether the current doctrine, patterns, and practical artifact remain sufficiently clear and lightweight for SMB teams.

Research-state changes should be reconciled under the [`Research Review Process`](../review-process.md) rather than tracked through a parallel presentation ledger.
