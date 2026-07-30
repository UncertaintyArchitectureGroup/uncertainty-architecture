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
source_format: pdf
source_file: "content/raw/Designing Non-Deterministic Systems: Maintaining Engineering Rigor in the AI Era.pdf"
updated: 2026-07-30
license: CC-BY-4.0
---

# Designing Non-Deterministic Systems Source Intake

## Purpose

This note records the presentation deck used as a synthesis source for Uncertainty Architecture so that the Research Track distinguishes a preserved source from a completed repository transcript or normalized edition.

## Source state

The presentation is preserved as a PDF export under [`content/raw/`](../../raw/Designing%20Non-Deterministic%20Systems%3A%20Maintaining%20Engineering%20Rigor%20in%20the%20AI%20Era.pdf).

The raw source remains historical research evidence. It has not yet been converted into a complete reviewable Markdown transcript or normalized repository edition.

Slide content must not be treated as normative merely because the source is now present in the repository.

## Why the source matters

The deck consolidates UA concepts for a practitioner audience, including:

- the shift from deterministic software assumptions to Thinking Systems;
- the AI–code uncertainty boundary;
- control-theory framing for model-mediated systems;
- actuators, sensors, controllers, evidence, and corrective action;
- lifecycle and operating-model implications;
- system-level risks that extend beyond model quality;
- the relationship between requirements, approved business tolerances, correctness, and bugs when stochastic Model Judgment performs business logic.

Because a presentation compresses arguments and may omit qualifications used in longer publications, its claims should be checked against the research corpus before promotion into doctrine or patterns.

## Framework extraction state

One doctrine candidate has been translated through an explicit framework change:

- the requirement–correctness–bug relationship is proposed in [`00-doctrine/requirements-correctness-and-bugs.md`](../../../00-doctrine/requirements-correctness-and-bugs.md);
- the concise canonical definitions are proposed in [`00-doctrine/glossary.md`](../../../00-doctrine/glossary.md);
- traceability is recorded in [`content/research/framework-traceability.md`](../framework-traceability.md).

This does not imply that the rest of the deck has been reviewed or adopted.

## Required follow-up

Before or as part of the cross-publication synthesis:

1. create a Markdown research note or transcript with slide-level provenance;
2. distinguish presentation simplifications from durable framework claims;
3. record concepts introduced in the deck but absent from the publication corpus;
4. classify each extracted entity as doctrine, pattern, artifact, role/responsibility, process, technical reference artifact, failure mode, or reference architecture;
5. update this note when a complete normalized source or transcript supersedes the intake record.
