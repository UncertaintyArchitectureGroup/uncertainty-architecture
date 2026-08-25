---
title: "Internal Consistency Review — Thinking-System Scope and the Release-Contract Thesis"
artifact_type: research-note
status: research
maturity: active
module: research
topics:
  - thinking-systems
  - model-judgment
  - provenance
  - uncertainty-boundary
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/model-judgment
  - ua/topic/provenance
created: 2026-08-25
updated: 2026-08-25
license: CC-BY-4.0
draft: true
related:
  - ../research-register.md
  - open-engineering-specification-article-blueprint.md
  - open-engineering-specification-article-draft.md
  - thinking-systems-pre-publication-review-maximiliano-armesto.md
---

# Internal Consistency Review — Thinking-System Scope and the Release-Contract Thesis

> **Record boundary:** This note records a second-order internal consistency issue discovered while reconciling the Maximiliano Armesto pre-publication review. It is not external evidence and does not resolve the category boundary by itself.

## Research item

**Register item:** `TS-SCOPE-001`.

## Tension exposed

The current Thinking-System definition is written without an LLM-only condition. Maximiliano Armesto's review correctly made that breadth visible by pointing to earlier probabilistic systems as candidate cases.

A subsequent consistency review exposed a harder question: the paper's central release-contract thesis says that a Thinking-System release places into operation a judgment process that completes part of the consequential situation-to-consequence mapping at runtime. Some fixed learned probabilistic models can produce probabilities, scores, or classifications while their deployed input-to-output mapping is nevertheless fully determined before release once parameters and preprocessing are fixed.

That creates a possible mismatch between:

1. the current broad wording of **Model Judgment** and the Thinking-System category; and
2. the narrower release-contract property used to explain why the controlled object has changed.

## Current disposition

The technology-neutral scope is therefore **Under Validation**, not resolved. The research must determine whether:

- fixed learned probabilistic functions and runtime judgment processes genuinely belong to one engineering category because the material uncertainty lies elsewhere than stochastic sampling itself;
- the release-contract thesis needs to be generalized so it correctly describes both; or
- the category definition needs an additional condition that excludes some fixed learned functions from Thinking-System membership.

Concrete pre-LLM cases are tracked separately as `TS-HIST-001`. Low-consequence examples are tracked as `TS-LOW-001` because they test proportionality rather than historical scope.

## Claim boundary

Until this question is resolved, publication prose may state that the current definition is written in technology-neutral terms and that pre-LLM systems are candidate boundary cases. It must not claim that technology-neutral historical applicability has already been established.
