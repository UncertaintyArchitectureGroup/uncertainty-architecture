---
title: "Analysis: [Source title]"
artifact_type: research-analysis
status: draft
draft: true
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_record: "[Relative path to publication or research note]"
source_date: YYYY-MM-DD
analysts:
  - "[Name]"
license: CC-BY-4.0
---

# Analysis: [Source title]

## Analysis purpose

Explain why this source is being reviewed and which methodological or architectural questions the analysis must resolve.

## Source summary

Provide a concise, neutral summary of the source without converting its claims into normative UA requirements.

## Research question and assumptions

- What question did the source ask?
- What assumptions did it make about software, models, users, organizations, risk, and scale?
- Which assumptions were explicit and which were implicit?

## Findings that remain strong

| Finding | Why it remains useful | Evidence or later support |
|---|---|---|
| [Finding] | [Reason] | [Source or observation] |

## Findings refined by later work

| Original finding | Later refinement | Impact on UA |
|---|---|---|
| [Original formulation] | [Refined formulation] | [Keep / narrow / rename / supersede] |

## Contradictions and tensions

### Internal tensions

Identify claims within the source that do not fit together cleanly.

### Tensions with earlier UA work

Identify where the source rejects, narrows, or changes an earlier position.

### Tensions with later UA work

Identify where later sources or current thinking modify this source.

## Over-strong or ambiguous claims

For each claim:

- quote or paraphrase the claim;
- explain the problem;
- propose a more defensible interpretation;
- state whether the archived text should remain unchanged.

## Terminology review

| Source term | Meaning in the source | Current interpretation | Decision candidate |
|---|---|---|---|
| [Term] | [Meaning] | [Current meaning] | [Retain / narrow / rename / supersede / unresolved] |

Explicitly review legacy terms such as Behavioral Software and Behavioral Applications against the current **Thinking Systems** category whenever they appear. Also review Model Control Plane, AI Control Plane, actuators, constraints, sensors, controller, and specialized role names where relevant.

## Methodology impact

### What this source adds

List genuinely new contributions.

### What this source changes

List earlier methodological assumptions that should be reconsidered.

### What this source does not justify

List conclusions that should not be promoted into the normative framework.

## Framework candidates

| Research finding | Candidate destination | Proposed status | Work required before adoption |
|---|---|---|---|
| [Finding] | [Doctrine / Lifecycle / Pattern / Operating Model / Reference Architecture / Artifact] | Candidate | [Validation, definition, conflict resolution, RFC] |

## SMB surface vs technical depth

### Surface guidance

What would an SMB team need to understand or use directly?

### Deeper framework material

What should remain in advanced patterns, rationale, research, or reference architecture?

## Unresolved questions

1. [Question]

## Recommended traceability delta

List the exact rows proposed for `framework-traceability.md`.

## Review outcome

- **Research record:** [Accepted / changes requested]
- **Framework candidates:** [List]
- **Superseded concepts:** [List]
- **Separate RFC or methodology work required:** [List]
- **Terminology decisions deferred:** [List]
