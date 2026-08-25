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

### 2. The definition is not LLM-exclusive

The current Thinking-System definition is technology-neutral. That establishes a definition-level scope point: membership is not restricted to LLM-based systems. It does **not** by itself establish that any particular pre-LLM system qualifies, nor how prevalent such systems were historically.

Traditional credit scoring, summarization, or code-completion systems are therefore useful boundary cases only when their outputs causally influence a Consequential Runtime Responsibility strongly enough to satisfy the category test.

**Research effect:** preserve two distinct research items rather than collapsing them:

- `TS-SCOPE-001` — **Resolved:** the definition-level implication that Thinking-System membership is not restricted to LLMs;
- `TS-CASE-001` — **Under Validation:** which concrete pre-LLM and low-consequence systems actually satisfy the category test, and what historical/prevalence claims are supportable.

The split is intentional under the Active Research Register's identity/granularity rule: the definition-level scope point and the concrete classification/evidence question now have different lifecycle states and different next decisions. The first follows from the current definition. The second still requires case-specific causal analysis and, for historical/prevalence claims, supporting evidence.

### 3. Category membership must be separated from control depth

A low-consequence summarizer whose output is reversible and human-mediated may satisfy the category test while requiring much lighter controls than an agent authorized to change financial or operational state.

**Research effect:** make proportionality visible before the full control map appears. Category membership, consequence severity, and implementation depth are separate decisions. The proportionality distinction is resolved at the conceptual level; whether a particular low-consequence example satisfies the category remains under `TS-CASE-001`.

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
| Definition-level LLM scope | Resolved: the definition is technology-neutral and not LLM-exclusive | No doctrine change implied |
| Concrete pre-LLM / low-consequence classification | Under validation; treat examples case by case | No historical or prevalence claim implied |
| Proportionality | Accepted; surface earlier in the paper | Consistent with existing separation of consequentiality, severity, and control adequacy |
| STAMP/STPA positioning | Accepted as an early attribution/comparison correction; full verdict deferred | No novelty claim or normative change |

## Remaining questions

1. Is **Explicitly Authored Software** the best durable opposite-side term, or should the paper ultimately use only a descriptive responsibility-level contrast?
2. Which pre-LLM and intentionally low-consequence systems satisfy the category test under concrete causal analysis, and which only contain probabilistic components without transferring a Consequential Runtime Responsibility?
3. What historical or prevalence claims about such systems can be supported independently of the technology-neutral definition itself?
4. What does the four-horizon model add, if anything, beyond a competent STAMP/STPA application to the same socio-technical control structure?
5. What does the four-horizon map lose or distort when reverse-mapped from STAMP/STPA, Simplex/runtime assurance, production ML engineering, management systems, and mature internal operating compositions?

## Research-state reconciliation

This review reopens terminology and comparative-contribution questions, resolves the definition-level non-LLM-exclusivity point, and leaves concrete historical/low-consequence classification under validation. The owning paper surfaces are revised together, the active research register records the distinct lifecycle states, and source-to-framework traceability is updated where the review changes the relationship between research wording and canonical framework terminology.
