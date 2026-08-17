---
title: Research Drafting Protocol for AI Contributors
artifact_type: repository-guide
status: informative
maturity: active
module: research
topics:
  - repository-architecture
  - contribution-workflow
  - provenance
  - thinking-systems
tags:
  - ua/module/research
  - ua/type/repository-guide
  - ua/status/informative
  - ua/topic/repository-architecture
  - ua/topic/thinking-systems
---

# Research Drafting Protocol for AI Contributors

## Scope

This file applies to work inside `content/research/` and supplements the root [`AGENTS.md`](../../AGENTS.md).

It defines the default workflow for long-form research articles, papers, and publication drafts that are developed from a detailed editorial blueprint and a separate target manuscript.

It is operational guidance, not a source of Uncertainty Architecture doctrine or terminology.

## Two-document model

A long-form research publication should normally use two living documents:

1. **Editorial blueprint** — the detailed design document that owns the complete argument, section purposes, required claims, transitions, figures, source plan, exclusions, maturity boundaries, writing notes, and unresolved editorial decisions.
2. **Target manuscript** — the publication-facing article or paper in which prose, diagrams, examples, and the continuous reader experience are developed.

The blueprint is not a temporary checklist and must not be shortened merely because prose has been written. The target manuscript must not contain internal drafting rules, agent instructions, repository workflow notes, or editorial status commentary intended only for contributors.

## Publication adaptation rule

A long-form working paper may intentionally produce a shorter publication-facing adaptation before the complete manuscript is finished when early external review can materially improve the remaining research and the shorter argument can stand on its own.

The detailed lifecycle, feedback classification, publication-state transition, and provenance handling for that surface are owned by [`review-process.md`](review-process.md#publication-adaptation-and-external-feedback-cycle). This file adds only the contributor execution rules needed while editing:

- treat the adaptation as a **distribution surface, not a new source of conceptual authority**;
- keep the blueprint and long-form manuscript as the owning research pair;
- develop an unpublished adaptation under `content/research/notes/` as non-normative research, normally with `draft: true`;
- compare every material adapted claim against the owning long-form sources;
- if adaptation work discovers a conceptual correction rather than a distribution-only wording change, reconcile that correction into the owning long-form pair before release;
- preserve attribution proportionately, distinguishing phrase/framing provenance from authorship, endorsement, and framework authority;
- do not treat external feedback as framework evidence merely because it was public or came from a prominent reviewer; classify it under the Research Review Process first;
- treat equivalent Medium, LinkedIn, website, or other platform copies as **renditions of one content edition** when only formatting, image substitution, or platform mechanics differ; use one principal `canonical_url` and `additional_publication_urls` for equivalent renditions, and preserve a separate repository edition only when the substantive text materially diverges;
- after actual publication, preserve the published content edition under `content/research/publications/` according to the Research Review Process.

## Mandatory drafting iteration

Every substantial drafting iteration MUST follow this sequence:

```text
Read the complete editorial blueprint
→ select the next coherent section block
→ read the complete target manuscript
→ inspect terminology, claims, transitions, examples, and figures already established
→ design the new section as a continuation of the existing argument
→ write and integrate the new prose and diagrams
→ reread the complete target manuscript
→ repair contradictions, repetition, weak transitions, numbering, and premature conclusions
→ return to the editorial blueprint
→ update its section design, figures, writing notes, rejected formulations, source needs, and unresolved risks
```

A drafting iteration is incomplete until both documents are reconciled.

For a publication adaptation, add one bounded distribution pass after the owning pair is coherent:

```text
reread the current long-form manuscript and blueprint
→ select the bounded public argument
→ draft or revise the adaptation
→ compare every material claim against the owning long-form sources
→ reconcile any conceptual change back into the owning pair
→ review provenance, maturity boundary, links, figures, and external-feedback invitation
```

## Cumulative argument rule

A new section must be based on:

- the complete current blueprint;
- all previously accepted manuscript sections;
- terminology and distinctions already introduced;
- the logical need created by the preceding section;
- the repository sources that own the relevant meaning.

Do not treat each chapter as a standalone article. Do not restart the framework explanation from zero. Extend the existing argument.

When new prose exposes a flaw in an earlier section, revise the earlier section in the same iteration when practical, then update the blueprint to preserve the improved design.

## Blueprint integrity

The editorial blueprint should preserve, for every section where relevant:

- purpose;
- core claim;
- detailed required content;
- argument sequence;
- required examples and counterexamples;
- figure requirements;
- repository anchors;
- external-evidence needs;
- transition into the next section;
- closing claim;
- word budget or expected depth;
- known objections, risks, rejected formulations, and unresolved decisions discovered during drafting.

Do not replace detailed section design with one-line summaries after the corresponding prose exists. The blueprint is the recoverable memory of the publication design.

## Manuscript integrity

The target manuscript should read as a publishable continuous work.

Do not include:

- draft-status banners intended for maintainers;
- cumulative drafting rules;
- agent instructions;
- pull-request process;
- internal acceptance checklists;
- repository authority explanations unless they are part of the publication's actual subject;
- placeholders where a requested diagram or argument can already be produced.

Publication-facing maturity caveats remain appropriate where they are part of the paper's claim boundary.

## Diagram protocol

Major architectural arguments and major decision levels should receive a Mermaid diagram, table, or other explicit model when that representation adds information.

Diagrams are first-class reasoning artifacts. They must:

- contribute information rather than merely repeat prose;
- remain consistent with all earlier diagrams;
- preserve current glossary and owning-source terminology;
- avoid implying mandatory products, services, departments, committees, job titles, or execution sequences;
- show upward reassessment where decision levels are shown;
- distinguish authoritative boundaries, evidence, decision authority, and corrective action;
- use captions that state important scope and non-prescriptive limits.

After each iteration, review and renumber the full figure sequence, not only newly added diagrams.

## Framework-introduction discipline

When a paper derives an engineering problem before presenting a named framework, do not introduce the framework as the premise that validates the deduction.

The sequence should remain:

```text
observable engineering change or problem
→ derived responsibilities and architecture
→ worked implications and limits
→ named framework or specification that organizes the result
```

This rule does not prohibit the framework name from appearing in the publication title for attribution and discoverability.

## Research-session completion

Before completing an article-writing session or PR:

1. reread the complete target manuscript;
2. reread and update the complete blueprint;
3. when a publication adaptation changed, compare its material claims and provenance against the owning long-form pair;
4. confirm the target title, H1, abstract, section names, and final framing are consistent;
5. confirm internal drafting notes did not leak into publication prose;
6. confirm figures form one coherent visual sequence;
7. confirm new claims follow repository authority and external evidence rules;
8. confirm attribution distinguishes dialogue/provenance from authorship, endorsement, and framework authority;
9. confirm the PR description names all publication surfaces that materially changed;
10. confirm the machine-readable change contract includes every changed owning path;
11. run the applicable metadata, link, Mermaid, build, and change-coupling checks;
12. report what remains unresolved and whether the PR remains Draft.
