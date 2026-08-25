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

### 2. The current definition exposes a non-LLM scope question

The reviewer pointed out that the current wording is not tied to LLMs and therefore appears capable of including earlier probabilistic systems. During reconciliation, that observation exposed a second-order consistency question that remains unresolved: some fixed learned models can produce probabilistic scores or classifications while their deployed input-to-output mapping is fully determined before release, whereas the paper's release-contract thesis emphasizes consequential mapping that remains partly unresolved until runtime and is completed by Model Judgment during operation.

The review therefore establishes that the **current definition is written broadly**, not that historical technology-neutral applicability is already proven.

**Research effect:** preserve separate research items:

- `TS-SCOPE-001` — **Under Validation:** whether the current technology-neutral wording coheres with the release-contract thesis across fixed learned probabilistic functions and runtime judgment processes, or whether the category/thesis needs refinement;
- `TS-HIST-001` — **Under Validation:** which concrete pre-LLM systems, if any, satisfy the resulting category test strongly enough to be treated as Thinking Systems.

The second-order consistency issue is preserved separately in [`thinking-systems-release-contract-scope-review.md`](thinking-systems-release-contract-scope-review.md). No historical prevalence claim follows from the current definition alone.

### 3. Category membership must be separated from control depth

A low-consequence summarizer whose output is reversible and human-mediated may satisfy the category test while requiring much lighter controls than an agent authorized to change financial or operational state.

**Research effect:** make proportionality visible before the full control map appears. Category membership, consequence severity, and implementation depth are separate decisions. The proportionality distinction is resolved at the conceptual level; whether the deliberately low-consequence example actually satisfies the category remains independently under `TS-LOW-001`.

**Register items:** `TS-PROP-001` and `TS-LOW-001`.

### 4. STAMP/STPA requires explicit positioning

STAMP already models hierarchical socio-technical control structures that can extend into management and regulatory authority. The paper must therefore not imply that extending the control perimeter beyond software is itself a UA invention.

**Research effect:** add a bounded early positioning statement and preserve the full comparison for the later systematic landscape/substitution work. The working question is narrower: whether the four-horizon model provides useful explicit lifecycle decision ownership for model-judgment-dependent software beyond what a competent STAMP/STPA application already supplies.

That question remains unresolved until the planned bidirectional mapping is performed. The comparison must also test what the UA map flattens, renames, duplicates, or fails to preserve.

**Register item:** `TS-COMP-001`.

## Disposition

| Finding | Current disposition | Framework effect |
|---|---|---|
| `Linear Software` publication label | Reopened; test `Explicitly Authored Software` as a research candidate | No canonical rename in this PR |
| Definition-level technology scope | Reopened: current wording is broad, but coherence with the release-contract thesis remains under validation | No doctrine change in this PR |
| Concrete pre-LLM classification | Under validation under `TS-HIST-001` | No historical or prevalence claim implied |
| Low-consequence boundary example | Under validation under `TS-LOW-001` | Used only if the case independently satisfies the category test |
| Proportionality | Accepted; surface earlier in the paper | Consistent with existing separation of consequentiality, severity, and control adequacy |
| STAMP/STPA positioning | Accepted as an early attribution/comparison correction; full verdict deferred | No novelty claim or normative change |

## Remaining questions

1. Is **Explicitly Authored Software** the best durable opposite-side term, or should the paper ultimately use only a descriptive responsibility-level contrast?
2. Does the category or release-contract thesis need an additional condition that distinguishes fixed learned probabilistic functions whose deployed mapping is determined before release from runtime judgment processes that leave part of the consequential mapping unresolved until operation?
3. Which concrete pre-LLM systems, if any, satisfy the resulting category test?
4. Which intentionally low-consequence case can demonstrate proportionality without smuggling category membership into the example?
5. What historical or prevalence claims about such systems can be supported independently of the technology-neutral definition itself?
6. What does the four-horizon model add, if anything, beyond a competent STAMP/STPA application to the same socio-technical control structure?
7. What does the four-horizon map lose or distort when reverse-mapped from STAMP/STPA, Simplex/runtime assurance, production ML engineering, management systems, and mature internal operating compositions?

## Research-state reconciliation

This review reopens terminology and comparative-contribution questions and exposes a still-open consistency question between the broad technology wording of the category and the release-contract thesis. Historical pre-LLM classification and the low-consequence proportionality example remain independently under validation. The owning paper surfaces are revised together, the active research register records the distinct lifecycle states, and source-to-framework traceability is updated where the review changes the relationship between research wording and canonical framework terminology.
