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

## Publication adaptation cycle

A long-form working paper may intentionally produce a shorter publication-facing adaptation before the complete target manuscript is finished. Use this only when early external review can materially improve the remaining research and when the shorter article can stand on its own without pretending to be the completed working paper.

The adaptation is a **third publication surface, not a third source of conceptual authority**:

```text
Editorial blueprint
↔ living long-form target manuscript
→ bounded publication adaptation under content/research/notes/
→ external review and contradictory evidence
→ reconcile material findings back into the blueprint / long-form manuscript
→ continue, narrow, reorder, or revise the research
→ after actual publication, preserve the published edition under content/research/publications/
```

Rules for a publication adaptation:

1. Keep the living blueprint and long-form target manuscript as the owning research pair. The adaptation may compress, reorder, omit later sections, or change rhetorical sequence for a different audience, but it must not silently create a competing framework definition.
2. Develop the adaptation as `status: research`, `maturity: draft`, `artifact_type: research-note`, normally with Quartz `draft: true`, and identify the source manuscript/blueprint through provenance or relationship metadata.
3. State the publication boundary honestly. If the long-form paper is incomplete, the adaptation may say that it intentionally stops at the current defensible argument and is being exposed to criticism before the next research phase.
4. When adaptation work discovers a material conceptual correction rather than a distribution-only wording change, reconcile that correction into the owning long-form manuscript and blueprint before treating the adaptation as ready for publication.
5. External feedback is evidence, not authority by itself. Record only feedback that materially changes a research question, claim boundary, source interpretation, or framework candidate; do not turn the adaptation or Research Track into a comment log.
6. After external publication, preserve the exact or normalized repository edition under `content/research/publications/` with `artifact_type: research-publication`, publication date, canonical URL, edition/provenance data, and any material transformations. The prior adaptation draft may be retained, superseded, or removed according to whether it still carries distinct research value; Git history remains the drafting record.
7. A shorter adaptation must link back to the fuller living work when that helps readers inspect omitted reasoning, evidence, diagrams, or unresolved sections.

### Attribution and dialogue provenance

When external dialogue materially contributes a phrase, framing, distinction, example, challenge, or research direction, publication-facing material should preserve that provenance proportionately.

- Distinguish **source of a phrase or framing** from authorship of the paper's specific engineering definition, model, or conclusion.
- Do not claim coinage when the work only adopts or sharpens an existing formulation.
- Do not imply endorsement, co-authorship, or agreement merely because a person is acknowledged, cited, tagged, or thanked for dialogue.
- Link a public source when it materially anchors the provenance and can be cited accurately; otherwise describe the contribution as dialogue or correspondence without inventing a public record.
- Keep acknowledgments concise enough that they explain intellectual provenance rather than functioning as promotional name lists.

For the current Thinking Systems research, the repository already states that UA does not claim coinage of the phrase **Thinking Systems**. Publication adaptations should preserve the more specific provenance when relevant: the formulation entered this research through Vitalii Oborskyi's exchange with Arkadiy Dobkin, while the UA-specific engineering definition and responsibility boundary remain claims developed and tested in the UA research track.

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

For a publication adaptation, add one more loop after the owning pair is coherent:

```text
reread the current long-form manuscript and blueprint
→ select the bounded public argument
→ draft or revise the adaptation
→ compare every material claim against the owning long-form sources
→ reconcile any conceptual change back into the owning pair
→ review provenance, maturity boundary, links, and the external-feedback invitation
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
