---
title: "External Review Record — Thinking Systems Publication Draft (Maximiliano Armesto)"
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - provenance
  - control-loop
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/provenance
  - ua/topic/control-loop
created: 2026-08-24
updated: 2026-08-24
language: en
license: CC-BY-4.0
draft: true
related:
  - open-engineering-specification-article-blueprint.md
  - open-engineering-specification-article-draft.md
  - thinking-systems-publication-draft.md
  - ../framework-traceability.md
---

# External Review Record — Thinking Systems Publication Draft

## Purpose

This note records a material pre-publication review of the Thinking Systems argument and the resulting research/editorial decisions. It preserves critique provenance without reproducing private correspondence verbatim.

## Review provenance and boundary

**Maximiliano Armesto**, Chief Technology Officer at Taller Technologies, reviewed the complete standalone draft before publication at the author's request. The review addressed the category boundary, terminology, proportionality, relationship to STAMP/STPA, and acknowledgment accuracy.

This record attributes the review and its effect on the research. It does **not** imply co-authorship, endorsement of Uncertainty Architecture, agreement with every claim, or authority to change the UA specification. The accepted changes remain research/editorial decisions owned through the repository review process.

## Material feedback and reconciliation

| Review finding | Research/editorial response | Framework status |
|---|---|---|
| **“Linear Software” creates avoidable semantic friction** because the paper must repeatedly explain that it does not mean sequential or fixed orchestration. | Publication-facing prose now describes the opposite side of the boundary through **explicitly authored consequential responsibilities** rather than requiring a named binary category. | The draft-normative glossary is unchanged. A repository-wide terminology decision requires separate framework review. |
| The systems covered by the definition **predate LLMs** and can include earlier probabilistic systems when at least one Consequential Runtime Responsibility depends partly on their Model Judgment. | The paper now states that LLMs did not create the responsibility structure; they made model-mediated judgment more general-purpose, accessible, and widespread. LLM systems remain the primary contemporary focus rather than the historical origin of the category. | Category scope remains a research hypothesis subject to over- and under-classification tests. |
| A broad category makes **proportionality essential**. | The paper separates category membership, consequence severity, and required control depth early and adds an intentionally low-consequence case. | The full map remains diagnostic; implementation depth remains proportionate to consequence, authority, reversibility, evidence, and operating context. |
| The socio-technical control perimeter and organizational decision reach overlap materially with **[STAMP/STPA](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf)**. | The paper now acknowledges that hierarchical socio-technical control extending into management and regulatory authority is established antecedent territory. The narrower candidate contribution is explicit lifecycle decision ownership for model-judgment-dependent software across Organization, Project / Architecture, Delivery / Release, and Runtime. | This contribution claim must be demonstrated, narrowed, or rejected through comparison; it is not assumed as novelty. |
| The comparison should not stop at STAMP/STPA. | The planned analysis remains broad and bidirectional across STAMP/STPA, Simplex/runtime assurance, mathematical and control-theoretic work, production ML/software engineering, risk and AI management systems, and implementation approaches and platforms. | Existing methods may narrow, substitute, or expose loss in the four-horizon map. |
| Jan's acknowledgment should use his full name. | Publication-facing acknowledgments use **Jan Rosen**. | Editorial/provenance confirmation only. |

## Scope decision

The current standalone article receives bounded positioning and proportionality revisions before publication. The direct STAMP/STPA positioning appears only after the four-horizon model has been introduced, so the article does not compare an operating model the reader has not yet seen. It does **not** compress the complete comparative mapping into a token paragraph that would imply research already performed. The systematic, bidirectional comparison remains a substantial later section of the long-form research and may be separated into a companion publication if responsible treatment would otherwise make the manuscript unmanageable.

## Open research questions

1. Does the Consequential Runtime Responsibility boundary classify pre-LLM and LLM-era systems consistently without making the category too broad to guide engineering decisions?
2. Is a named opposite category useful at framework level, or is descriptive language about explicitly authored consequential responsibility more precise?
3. What does the four-horizon model preserve for practitioners beyond a well-applied STAMP/STPA control structure or another credible composition?
4. Which STAMP/STPA, Simplex, control-theoretic, production-ML, management-system, or platform relationships does the derived map flatten, rename, duplicate, or fail to preserve?
5. Can independent practitioners apply proportionality without treating category membership as a mandate for a maximal control stack?

## Owning research surfaces

- [`open-engineering-specification-article-blueprint.md`](open-engineering-specification-article-blueprint.md) owns the revised editorial contract and later comparison design.
- [`open-engineering-specification-article-draft.md`](open-engineering-specification-article-draft.md) owns the long-form argument and systematic research.
- [`thinking-systems-publication-draft.md`](thinking-systems-publication-draft.md) is the bounded public adaptation through which the early argument will be tested.
- [`../framework-traceability.md`](../framework-traceability.md) records the reopened terminology, category-scope, and antecedent-positioning questions without changing status-bearing doctrine by implication.
