---
title: Active Research Register
artifact_type: research-index
status: research
maturity: active
module: research
topics:
  - provenance
  - thinking-systems
  - terminology
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-index
  - ua/status/research
  - ua/topic/provenance
  - ua/topic/thinking-systems
  - ua/topic/terminology
canonical_for:
  - active-research-register
created: 2026-08-25
updated: 2026-08-25
license: CC-BY-4.0
---

# Active Research Register

## Purpose

This register is the canonical cross-document inventory of **material research items that are still being tested, clarified, compared, or deliberately carried forward with provenance**.

It exists to prevent important terms, hypotheses, comparison questions, candidate artifacts, and externally introduced ideas from living only inside one paper, pull request, or conversation.

This is **not** a second source-to-framework ledger. [`framework-traceability.md`](framework-traceability.md) remains the canonical record of material research-to-framework decisions. The register answers a different question: **what material research items are currently in play, where did they come from, what owns the detailed work, and what is their current epistemic status?**

Do not register every noun, paragraph, or editing task. Register an item when losing its provenance or state would make later research, comparison, or framework review materially harder.

## Status vocabulary

The register reuses the Research Track vocabulary:

- **Research Finding** — a preserved finding that matters to current work but is not by itself a framework decision;
- **Candidate** — a term, hypothesis, artifact, process, example, or comparison proposition worth testing;
- **Needs Resolution** — evidence, terminology, scope, contradiction, or comparative adequacy is unresolved;
- **Proposed for Framework Review** — mature enough for a deliberate framework decision;
- **Active** — accepted into the current framework boundary, subject to the owning document's status;
- **Superseded** — replaced by a later formulation;
- **Rejected** — considered and intentionally not adopted.

## Current material items

| ID | Item | Class | Origin | Status | Detailed owner / provenance | Next decision |
|---|---|---|---|---|---|---|
| `TS-TERM-001` | **Thinking Systems** formulation provenance | Term / provenance | External dialogue with Arkadiy Dobkin | Active | [`thinking-systems-formulation-provenance-arkadiy-dobkin.md`](notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md); canonical meaning remains in the glossary | Preserve formulation provenance separately from authorship, endorsement, and definition authority |
| `TS-TERM-002` | **Explicitly Authored Software** | Terminology candidate | Maximiliano Armesto pre-publication review identified topology ambiguity in `Linear Software` | Needs Resolution | [`thinking-systems-pre-publication-review-maximiliano-armesto.md`](notes/thinking-systems-pre-publication-review-maximiliano-armesto.md); article blueprint owns the current paper-level test | Test whether the label is clearer and durable enough for separate framework terminology review; do not rename the glossary by implication |
| `TS-SCOPE-001` | Pre-LLM applicability of the Thinking-System definition | Category-boundary hypothesis / classification test | Maximiliano Armesto review plus current technology-neutral definition | Needs Resolution | Same review record and article blueprint | Preserve the definition-level implication, but test concrete pre-LLM and low-consequence cases and separate applicability from historical prevalence claims |
| `TS-PROP-001` | Category membership, consequence severity, and required control depth are distinct | Proportionality finding | Maximiliano Armesto review sharpened an existing UA distinction | Active | Same review record; current glossary/doctrine already separate consequentiality from severity and control adequacy | Keep the distinction visible early and validate whether low-consequence examples communicate it without scope expansion |
| `TS-LIFE-001` | Four-horizon lifecycle ownership and authorization refinement | Lifecycle / process hypothesis | Internal article synthesis against current Nested Control Lifecycle and project/delivery patterns | Needs Resolution | [`framework-traceability.md`](framework-traceability.md) conflict/evolution register; article blueprint owns the detailed hypothesis | Validate assessment eligibility, Project technical/design authority, Organization business/research authority, research-only versus production-capable Project Authorization, Business-Authorization coverage, and scoped-authorization semantics before any status-bearing lifecycle change |
| `TS-CARRIER-001` | Material-relationship carrier sufficiency and proportional application | Artifact / process hypothesis | Article §5 blueprint synthesis | Candidate | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Complete Article §5 mapping and test whether existing records/tools can carry each material relationship without UA-specific duplicate artifacts or semantic loss |
| `TS-COMP-001` | Four-horizon model relative to STAMP/STPA | Comparative hypothesis | Maximiliano Armesto review | Needs Resolution | Same review record; planned Article §6 landscape/substitution analysis | Perform bidirectional mapping and determine whether the four-horizon model adds useful lifecycle-decision specialization, merely renames existing semantics, or loses material relationships |
| `TS-SUB-001` | Semantic substitution and reverse-mapping test for existing methods/compositions | Comparative method hypothesis | Article §6 blueprint synthesis | Candidate | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Test whether equivalent-or-stronger semantics can substitute for UA relationships and whether reverse mapping exposes relationships the UA-derived map omitted or distorted |

## Machine-readable register

The block below is validated in CI. Human-readable rows above must express the same items and status; the machine block is the deterministic integrity surface, not a substitute for the explanatory records.

<!-- ua-research-register
{
  "version": 1,
  "items": [
    {
      "id": "TS-TERM-001",
      "title": "Thinking Systems formulation provenance",
      "item_class": "term",
      "status": "active",
      "origin_kind": "external-dialogue",
      "provenance_record": "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md",
      "owning_record": "00-doctrine/glossary.md",
      "next_step": "Preserve formulation provenance separately from authorship, endorsement, and definition authority."
    },
    {
      "id": "TS-TERM-002",
      "title": "Explicitly Authored Software",
      "item_class": "term",
      "status": "needs-resolution",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test the paper-level label and submit any canonical rename to separate framework terminology review."
    },
    {
      "id": "TS-SCOPE-001",
      "title": "Pre-LLM applicability of the Thinking-System definition",
      "item_class": "hypothesis",
      "status": "needs-resolution",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Preserve the definition-level implication, test concrete pre-LLM and low-consequence cases, and separate category applicability from historical prevalence."
    },
    {
      "id": "TS-PROP-001",
      "title": "Category membership, consequence severity, and required control depth are distinct",
      "item_class": "hypothesis",
      "status": "active",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Keep proportionality visible early and validate the low-consequence example during publication review."
    },
    {
      "id": "TS-LIFE-001",
      "title": "Four-horizon lifecycle ownership and authorization refinement",
      "item_class": "process",
      "status": "needs-resolution",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/framework-traceability.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Validate the lifecycle ownership and authorization refinement before any status-bearing lifecycle change."
    },
    {
      "id": "TS-CARRIER-001",
      "title": "Material-relationship carrier sufficiency and proportional application",
      "item_class": "artifact",
      "status": "candidate",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Complete Article 5 mapping and test the lightest credible carriers without semantic loss or duplicate UA-specific records."
    },
    {
      "id": "TS-COMP-001",
      "title": "Four-horizon model relative to STAMP/STPA",
      "item_class": "comparison",
      "status": "needs-resolution",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Perform the planned bidirectional STAMP/STPA mapping before making a contribution or substitution verdict."
    },
    {
      "id": "TS-SUB-001",
      "title": "Semantic substitution and reverse-mapping test for existing methods/compositions",
      "item_class": "comparison",
      "status": "candidate",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test equivalent-or-stronger semantic substitution and reverse mapping against the derived UA map."
    }
  ]
}
-->

## Operating rule

For material research work:

```text
source / dialogue / review / observation
→ provenance record when needed
→ stable research-item ID
→ owning analysis, blueprint, brief, or synthesis
→ explicit status and next decision
→ framework-traceability update only when the source-to-framework relationship materially changes
→ deliberate framework review before normative promotion
```

When an item is resolved, do not delete it merely to make the register look tidy. Mark it **Active**, **Superseded**, or **Rejected**, link the decision destination, and compact old resolved material only when provenance remains reconstructable elsewhere.
