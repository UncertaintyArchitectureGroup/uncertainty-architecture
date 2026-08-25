---
title: Research State Register
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
  - research-state-register
created: 2026-08-25
updated: 2026-08-25
license: CC-BY-4.0
---

# Research State Register

## Purpose

This register is the canonical cross-document inventory of **research concerns that require an identity and lifecycle outside any one paper, pull request, or conversation**. It preserves an item's origin separately from later evidence, dialogue, or review that changes its research state.

It exists to preserve the state of important terminology candidates, hypotheses, comparison questions, candidate artifacts/processes, and provenance-bearing external inputs when those items may be discussed or changed across several research records.

This is **not** a second source-to-framework ledger. [`framework-traceability.md`](framework-traceability.md) remains the canonical record of material research-to-framework decisions. The register answers a different question: **which cross-document research concerns need durable identity, where did they come from, what owns the detailed reasoning, what is their research lifecycle state, and what decision remains?**

The register is intentionally selective. It is not required to enumerate every material sentence, subclaim, validation criterion, or open question inside an owning paper or brief.

## Research lifecycle state

Register state describes the **lifecycle of the research item**, not whether the framework has accepted it. Framework disposition remains owned by [`framework-traceability.md`](framework-traceability.md) and by status-bearing specification sources.

- **Open** — the concern is identified and work has not yet reached a stable test or disposition.
- **Under Validation** — a concrete formulation, terminology candidate, comparison, or hypothesis is being tested or challenged.
- **Resolved** — the research question represented by this item has a current disposition or preserved provenance outcome; any framework effect is recorded separately where applicable.
- **Superseded** — a later research item or formulation replaces this one while provenance is retained.
- **Rejected** — the item was deliberately tested or considered and is not being carried forward.

A `Resolved` research item does **not** mean that a term, pattern, doctrine statement, or process has become normative. Likewise, an `Under Validation` item may concern a framework concept that is already active while testing only a narrower paper-level refinement or comparison.

## Identity and granularity rule

Assign a separate stable research-item ID only when the concern needs to change or be referenced independently across records. A separate ID is normally justified when at least one of the following is true:

- it has distinct provenance or attribution that must remain reconstructable;
- it has a different owning record from its parent question;
- it can reach a different lifecycle state or next decision independently of the parent;
- it is a named terminology candidate, comparison, artifact/process proposal, or falsifiable boundary question that will be referenced across workstreams;
- external critique, evidence, or a worked application changes this concern without necessarily changing the larger parent hypothesis.

Do **not** split every subclaim into its own ID. Subclaims that share provenance, owner, lifecycle state, and next decision remain inside the owning parent item and are tracked in that item's blueprint, analysis, brief, validation program, or traceability record. This keeps the register a cross-document epistemic control surface rather than a second backlog.

## Current material items

| ID | Item | Class | Origin | Research state | Detailed owner / provenance | Next decision |
|---|---|---|---|---|---|---|
| `TS-TERM-001` | **Thinking Systems** formulation provenance | Term / provenance | External dialogue with Arkadiy Dobkin | Resolved | [`thinking-systems-formulation-provenance-arkadiy-dobkin.md`](notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md); canonical meaning remains in the glossary | Preserve formulation provenance separately from authorship, endorsement, and definition authority |
| `TS-TERM-002` | **Explicitly Authored Software** | Terminology candidate | Maximiliano Armesto pre-publication review identified topology ambiguity in `Linear Software` | Under Validation | [`thinking-systems-pre-publication-review-maximiliano-armesto.md`](notes/thinking-systems-pre-publication-review-maximiliano-armesto.md); article blueprint owns the current paper-level test | Test whether the label is clearer and durable enough for separate framework terminology review; do not rename the glossary by implication |
| `TS-SCOPE-001` | Technology-neutral scope of the Thinking-System definition versus the release-contract thesis | Category-scope hypothesis | Current repository definition; external review exposed the breadth and a later consistency review exposed a release-contract tension | Under Validation | [`thinking-systems-release-contract-scope-review.md`](notes/thinking-systems-release-contract-scope-review.md) owns the current consistency issue; current glossary supplies the definition; blueprint owns the paper-level test | Test whether fixed learned probabilistic functions and runtime judgment processes belong to one category without weakening the release-contract distinction; narrow or generalize the definition/thesis if necessary |
| `TS-HIST-001` | Concrete pre-LLM Thinking-System boundary cases | Historical/category-boundary test | Maximiliano Armesto review raised earlier probabilistic systems as candidate cases | Under Validation | Same external-review record plus the scope-consistency note and article blueprint | Test concrete pre-LLM systems through causal and release-contract analysis before treating them as established examples or making prevalence claims |
| `TS-LOW-001` | Intentionally low-consequence Thinking-System boundary case | Proportionality/category-boundary test | Maximiliano Armesto review requested a deliberately low-consequence case | Under Validation | Same external-review record and article blueprint | Validate a low-consequence case independently of historical classification so the paper can show category membership ≠ severity ≠ control depth without assuming the example qualifies |
| `TS-PROP-001` | Category membership, consequence severity, and required control depth are distinct | Proportionality finding | Existing UA separation of consequentiality, severity, and control adequacy; sharpened by Maximiliano Armesto review | Resolved | Current glossary/doctrine support the distinction; review record preserves the later sharpening | Keep the resolved distinction visible in publication prose; validation of the illustrative low-consequence case remains under `TS-LOW-001` |
| `TS-LIFE-001` | Four-horizon lifecycle ownership and authorization refinement | Lifecycle / process hypothesis | Internal article synthesis against current Nested Control Lifecycle and project/delivery patterns | Under Validation | [`framework-traceability.md`](framework-traceability.md) conflict/evolution register; article blueprint owns the detailed hypothesis | Validate assessment eligibility, Project technical/design authority, Organization business/research authority, research-only versus production-capable Project Authorization, Business-Authorization coverage, and scoped-authorization semantics before any status-bearing lifecycle change |
| `TS-CARRIER-001` | Material-relationship carrier sufficiency and proportional application | Artifact / process hypothesis | Article §5 blueprint synthesis | Open | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Complete Article §5 mapping and test whether existing records/tools can carry each material relationship without UA-specific duplicate artifacts or semantic loss |
| `TS-COMP-001` | Four-horizon model relative to STAMP/STPA | Comparative hypothesis | Maximiliano Armesto review | Under Validation | Same review record; planned Article §6 landscape/substitution analysis | Perform bidirectional mapping and determine whether the four-horizon model adds useful lifecycle-decision specialization, merely renames existing semantics, or loses material relationships |
| `TS-SUB-001` | Semantic substitution and reverse-mapping test for existing methods/compositions | Comparative method hypothesis | Article §6 blueprint synthesis | Open | [`open-engineering-specification-article-blueprint.md`](notes/open-engineering-specification-article-blueprint.md) | Test whether equivalent-or-stronger semantics can substitute for UA relationships and whether reverse mapping exposes relationships the UA-derived map omitted or distorted |

## Machine-readable register

The block below is validated in CI. Human-readable rows above must express the same items and research lifecycle state; the machine block is the deterministic integrity surface, not a substitute for the explanatory records.

<!-- ua-research-register
{
  "version": 1,
  "items": [
    {
      "id": "TS-TERM-001",
      "title": "Thinking Systems formulation provenance",
      "item_class": "term",
      "status": "resolved",
      "origin_kind": "external-dialogue",
      "provenance_record": "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md",
      "owning_record": "content/research/notes/thinking-systems-formulation-provenance-arkadiy-dobkin.md",
      "framework_destination": "00-doctrine/glossary.md",
      "next_step": "Preserve formulation provenance separately from authorship, endorsement, and definition authority."
    },
    {
      "id": "TS-TERM-002",
      "title": "Explicitly Authored Software",
      "item_class": "term",
      "status": "under-validation",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test the paper-level label and submit any canonical rename to separate framework terminology review."
    },
    {
      "id": "TS-SCOPE-001",
      "title": "Technology-neutral scope of the Thinking-System definition versus the release-contract thesis",
      "item_class": "hypothesis",
      "status": "under-validation",
      "origin_kind": "repository-source",
      "provenance_record": "00-doctrine/glossary.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test whether fixed learned probabilistic functions and runtime judgment processes belong to one category without weakening the release-contract distinction; narrow or generalize the definition/thesis if necessary.",
      "transition_records": [
        "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
        "content/research/notes/thinking-systems-release-contract-scope-review.md"
      ]
    },
    {
      "id": "TS-HIST-001",
      "title": "Concrete pre-LLM Thinking-System boundary cases",
      "item_class": "example",
      "status": "under-validation",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test concrete pre-LLM systems through causal and release-contract analysis before treating them as established examples or making prevalence claims."
    },
    {
      "id": "TS-LOW-001",
      "title": "Intentionally low-consequence Thinking-System boundary case",
      "item_class": "example",
      "status": "under-validation",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Validate a low-consequence case independently of historical classification so the paper can demonstrate proportionality without assuming the example qualifies."
    },
    {
      "id": "TS-PROP-001",
      "title": "Category membership, consequence severity, and required control depth are distinct",
      "item_class": "hypothesis",
      "status": "resolved",
      "origin_kind": "repository-source",
      "provenance_record": "00-doctrine/glossary.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Keep the resolved distinction visible in publication prose; validation of the illustrative low-consequence case remains under TS-LOW-001.",
      "transition_records": [
        "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md"
      ]
    },
    {
      "id": "TS-LIFE-001",
      "title": "Four-horizon lifecycle ownership and authorization refinement",
      "item_class": "process",
      "status": "under-validation",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/framework-traceability.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Validate the lifecycle ownership and authorization refinement before any status-bearing lifecycle change."
    },
    {
      "id": "TS-CARRIER-001",
      "title": "Material-relationship carrier sufficiency and proportional application",
      "item_class": "artifact",
      "status": "open",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Complete Article 5 mapping and test the lightest credible carriers without semantic loss or duplicate UA-specific records."
    },
    {
      "id": "TS-COMP-001",
      "title": "Four-horizon model relative to STAMP/STPA",
      "item_class": "comparison",
      "status": "under-validation",
      "origin_kind": "external-review",
      "provenance_record": "content/research/notes/thinking-systems-pre-publication-review-maximiliano-armesto.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Perform the planned bidirectional STAMP/STPA mapping before making a contribution or substitution verdict."
    },
    {
      "id": "TS-SUB-001",
      "title": "Semantic substitution and reverse-mapping test for existing methods/compositions",
      "item_class": "comparison",
      "status": "open",
      "origin_kind": "internal-synthesis",
      "provenance_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "owning_record": "content/research/notes/open-engineering-specification-article-blueprint.md",
      "next_step": "Test equivalent-or-stronger semantic substitution and reverse mapping against the derived UA map."
    }
  ]
}
-->

## Operating rule

For cross-document research concerns:

```text
source / dialogue / review / observation
→ provenance record when needed
→ decide whether the concern needs independent identity
→ stable research-item ID when the identity/granularity rule is met
→ owning analysis, blueprint, brief, or synthesis
→ explicit research lifecycle state and next decision
→ framework-traceability update only when the source-to-framework relationship materially changes
→ deliberate framework review before normative promotion
```

When an item is resolved, do not delete it merely to make the register look tidy. Mark it **Resolved**, **Superseded**, or **Rejected**, link the decision destination where applicable, and compact old resolved material only when provenance and framework disposition remain reconstructable elsewhere.
