---
title: "External Review Record — Maximiliano Armesto on the Thinking Systems Publication Draft"
artifact_type: research-note
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - terminology
  - control-loop
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/thinking-systems
  - ua/topic/terminology
created: 2026-08-25
updated: 2026-08-25
license: CC-BY-4.0
draft: true
source_basis:
  - thinking-systems-publication-draft.md
  - open-engineering-specification-article-draft.md
related:
  - ../research-register.md
  - ../review-process.md
analysts:
  - "Vitalii Oborskyi"
---

# External Review Record — Maximiliano Armesto on the Thinking Systems Publication Draft

> **Record boundary:** This note preserves the material research effect of a private pre-publication review. It is a maintainer-authored summary, not a verbatim publication of private correspondence. The review is treated as conceptual critique and provenance, not co-authorship, endorsement, framework authority, or empirical validation.

## Review object

**Reviewer:** Maximiliano Armesto, CTO at Taller Technologies  
**Review date:** 2026-08-24  
**Reviewed surface:** the complete standalone publication draft *Uncertainty Architecture: Thinking Systems — When the Controlled Object Changes*, derived from the living long-form manuscript and blueprint.

The review was requested before external publication so that the bounded argument could be challenged while the larger research remained revisable.

## Material findings

### 1. `Linear Software` creates avoidable topology ambiguity

The reviewer observed that the paper repeatedly has to explain that `Linear Software` does not mean sequential or fixed orchestration. The underlying distinction is already expressed more directly in the paper as whether consequential responsibility is explicitly authored before runtime or depends partly on runtime Model Judgment.

**Research effect:** the publication-facing opposite-side label is reopened. This revision tests **Explicitly Authored Software** as a paper-level terminology candidate. The draft-normative glossary entry `Linear Software` is unchanged until a separate framework terminology review deliberately accepts, narrows, rejects, or replaces it.

**Register item:** `TS-TERM-002`.

### 2. The category is not historically LLM-exclusive

The current Thinking-System definition is technology-neutral: a pre-LLM probabilistic system may qualify when a Consequential Runtime Responsibility materially depends on probabilistic Model Judgment. Traditional credit scoring, summarization, or code-completion systems are therefore useful boundary cases depending on how their outputs causally influence downstream responsibility.

**Research effect:** distinguish two claims that must not be collapsed:

- the **definition-level implication** that Thinking-System membership is not restricted to LLMs;
- the **historical/empirical claim** about how common such systems were before general-purpose LLMs.

The first follows from the current definition. The second still requires careful historical framing and evidence. Specific examples remain case-dependent classification tests rather than universal declarations.

**Register item:** `TS-SCOPE-001`.

### 3. Category membership must be separated from control depth

A low-consequence summarizer whose output is reversible and human-mediated may satisfy the category test while requiring much lighter controls than an agent authorized to change financial or operational state.

**Research effect:** make proportionality visible before the full control map appears. Category membership, consequence severity, and implementation depth are separate decisions.

**Register item:** `TS-PROP-001`.

### 4. STAMP/STPA requires explicit positioning

STAMP already models hierarchical socio-technical control structures that can extend into management and regulatory authority. The paper must therefore not imply that extending the control perimeter beyond software is itself a UA invention.

**Research effect:** add a bounded early positioning statement and preserve the full comparison for the later systematic landscape/substitution work. The working question is narrower: whether the four-horizon model provides useful explicit lifecycle decision ownership for model-judgment-dependent software beyond what a competent STAMP/STPA application already supplies.

That question remains unresolved until the planned bidirectional mapping is performed. The comparison must also test what the UA map flattens, renames, duplicates, or fails to preserve.

**Register item:** `TS-COMP-001`.

## Disposition

| Finding | Current disposition | Framework effect |
|---|---|---|
| `Linear Software` publication label | Reopened; test `Explicitly Authored Software` as a research candidate | No canonical rename in this PR |
| Pre-LLM applicability | Accepted as a necessary scope clarification; concrete cases remain under test | No doctrine change implied |
| Proportionality | Accepted; surface earlier in the paper | Consistent with existing separation of consequentiality, severity, and control adequacy |
| STAMP/STPA positioning | Accepted as an early attribution/comparison correction; full verdict deferred | No novelty claim or normative change |

## Remaining questions

1. Is **Explicitly Authored Software** the best durable opposite-side term, or should the paper ultimately use only a descriptive responsibility-level contrast?
2. Which pre-LLM systems satisfy the category test under concrete causal analysis, and which only contain probabilistic components without transferring a Consequential Runtime Responsibility?
3. What does the four-horizon model add, if anything, beyond a competent STAMP/STPA application to the same socio-technical control structure?
4. What does the four-horizon map lose or distort when reverse-mapped from STAMP/STPA, Simplex/runtime assurance, production ML engineering, management systems, and mature internal operating compositions?

## Research-state reconciliation

This review reopens terminology and comparative-contribution questions while clarifying category scope and proportionality. The owning paper surfaces are revised together, the active research register records the open items, and source-to-framework traceability is updated where the review changes the relationship between research wording and canonical framework terminology.
