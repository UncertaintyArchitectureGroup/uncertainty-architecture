# RI usefulness: organizer analysis of the interrupted comparison

Date: 2026-09-18. Evidence cutoff: collection commit `3aadb1fdea1b0a0385b18fd15d090b83932cc892`. Repository claims are checked against study commit `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`, not subsequent experiment-record changes.

## Finding and decision

**The recorded answers demonstrate useful repository navigation and explanation in both instruction conditions. They do not demonstrate an incremental improvement from RI in the model's understanding of the repository or its concepts. That improvement remains inconclusive, rather than disproved.**

RI has an implemented navigation mechanism: a deterministic projection of terms, documents, responsibilities, instruction scopes and related evidence can route an agent to owning sources. That mechanism is a plausible aid when the owner is unknown. In this collection, however, the substantive paired answers mostly describe direct source reading, and no received tool payload independently verifies compact-RI exposure. The comparison therefore gives considerably more evidence about answering from the repository's existing documentation than about learning from its generated RI surface.

The practical decision is to retain the existing optional RI route and direct-owner fallback, without expanding RI infrastructure or making RI retrieval mandatory on the strength of this study. The evidence also does not justify removing RI as useless. Prioritize clear owning documents and reliable delivery of those documents; decide further RI investment only against a concrete unresolved task and measurable benefit. Development and maintenance return on investment is unmeasured.

## Method and evidence boundary

This is an **unblinded qualitative analysis by the organizer**, who knows the instruction assignments and prepared the tasks. It is not the independent blind scoring required by the [frozen study record](README.md#assessment-and-stopping-rule). No 0/1/2 quality scores, scored wins/losses/ties, significance claims or strict v11 acceptance result are issued. Independent scoring remains pending; this report does not change or substitute for that protocol step.

The analysis reads the original answers in [sessions.json](sessions.json), both supplemental captures, and the unchanged [task expectations](TASK-CANDIDATES.md). It checks material claims against the frozen owning files. Agreement with source text is evidence about the answer's content; it does not prove the tested model actually retrieved that source. Answer length, citation count and self-reported usefulness are not quality or benefit measurements.

Condition A received ordinary-source instructions. Condition B received optional-RI instructions and could legitimately take a direct-owner route. Both received the same repository address, study ref and instruction bootstrap. **A was not an undocumented repository or an agent without guidance.** The study does not isolate the value of the repository's curated instructions, conceptual owners, metadata or authority hierarchy as a whole. It asks about adding the optional RI route to that already structured baseline.

| Available evidence | Count and disposition |
|---|---|
| Frozen design | 12 tasks / 24 original slots |
| Received originals | 20 attempts: 18 substantive answers and 2 refusals |
| Original pairs with two substantive answers and matching reported model labels | 8 pairs: T01, T02, T04, T05, T06, T07, T08, T09; all report `gpt-5-6` |
| Other original pairs | T03 and T10 each have one substantive answer and one refusal; the refusal reports `gpt-5-6-mini` |
| Supplemental T03-B-R1 | One later substantive answer; reuses T03/A for any comparison, not a replacement or new independent pair |
| Supplemental T10-A-R1 | Initial refusal and later user-assisted substantive continuation in one conversation; both report `gpt-5-6-mini` |
| Missing originals | T11/A, T11/B, T12/B, T12/A; no outcomes inferred |
| Independent quality scores | 0 |

Matching Share labels do not verify identical backends or settings. The 8-pair subset is a transparent descriptive subset, not an unbiased estimate of overall success. All original refusals, missing slots and supplements remain visible below. Collection stopped after observed access/model problems and operator burden, not at a statistical stopping boundary.

## What the answers show about understanding

Several repeated distinctions are consistent with the owning sources:

- **Authority and representation:** both T01 answers separate canonical Markdown and specification owners from generated navigation data. Neither treats a graph edge as semantic authority or deterministic projection tests as proof of agent usefulness.
- **Existing implementation and ownership:** T04 locates current code conventions and separates formatter/type checks from behavior and human review. T05/T06 identify the existing article exporter, preserve canonical Markdown and distinguish a temporary local Quartz render from publishing a website. T08 keeps PDF and platform renditions as derived outputs and recognizes Medium's manual image-upload boundary.
- **Research workflow:** both T09 answers identify the living blueprint and long-form manuscript, keep the next-section plan in the blueprint and distinguish that manuscript from the standalone publication article. They do not create a competing planning artifact.
- **UA concepts:** T07 answers reproduce important boundaries: Thinking Systems concern consequential runtime responsibilities partly dependent on probabilistic Model Judgment; the control capabilities are logical families, not four required physical services. This is useful source-consistent explanation.

These are observable answer properties, not a measurement of the model's internal representation. Most tasks ask the model to locate, summarize or distinguish documented material. They do not test applying UA concepts to an unfamiliar architecture, resolving a difficult doctrinal contradiction, preserving invariants through a code change or producing a reviewed new research section. Consequently, **deep conceptual transfer and reliable implementation behavior remain untested**.

There are also concrete limitations in the answers. In T02, both explain source-driven freshness and fallback but omit the complete actionable freshness procedure: the explicit regeneration/verification commands and the connector's checkout-plus-surface-identity verification. T07 has an ambiguous subject, “Це”: A explains UA and then the RI implementation; B concentrates on UA and provides much less of the deterministic projection explanation required by the frozen key. Correct surrounding concepts do not eliminate that task-scope gap.

## Case-level comparison under the frozen expectations

The following observations are qualitative and unblinded. Each row links the preserved primary captures; exact submitted messages and answers are also in `sessions.json`. “Reports” describes an answer's claim, not verified tool execution.

| Task and original evidence | Observation against the frozen task | Implication for RI attribution |
|---|---|---|
| T01 — [A](T01-A-share.json), [B](T01-B-share.json): architecture and proportionality | Both correctly describe a derived navigation layer, source authority and conditional proportionality. B supplies more implementation detail about producer/schema and input bounds; A clearly distinguishes plausible value from measured value. | More detail in B is not proof of better understanding or RI causation. B reports a truncated compact request and ordinary-source fallback. |
| T02 — [A](T02-A-share.json), [B](T02-B-share.json): freshness | Both explain regeneration after relevant changes, optional adoption and fallback. Neither gives the full local command sequence and connector identity-check procedure expected by the key. | A shared operational omission; RI-assigned instructions did not visibly resolve it. Compact delivery in B is not established. |
| T03 — [A](T03-A-share.json), [B](T03-B-share.json): code-style owner | A finds the existing contribution/scoped owners and explains comments as intent/invariants rather than syntax. B refuses source access. | The original pair cannot compare substantive understanding. The refusal has a different reported model label and an altered SHA in its text. |
| T04 — [A](T04-A-share.json), [B](T04-B-share.json): enforcement | Both identify actual formatter settings, TypeScript/Python checks, scoped rules and the boundary between automatic checks and semantic review. Differences are mainly emphasis and coverage detail. | Both provide useful source-grounded explanations. B reports direct known-owner reads without compact RI. |
| T05 — [A](T05-A-share.json), [B](T05-B-share.json): article PDF | Both identify the existing workflow and standalone-article commands/output, provenance/manifest and visual checks, preserving Markdown and respecting the no-execution request. A emphasizes the operator route; B adds rendering/provenance detail. | Successful discovery of the existing route appears in both conditions. The task already gives the article source path; B reports ordinary-source fallback. |
| T06 — [A](T06-A-share.json), [B](T06-B-share.json): no deployed Pages | Both correctly explain temporary local Quartz plus browser rendering and its dependencies, independently of Pages deployment. | Both demonstrate the relevant dependency boundary. This overlaps T05 and is not an independent broad test of conceptual transfer. B reports direct reads. |
| T07 — [A](T07-A-share.json), [B](T07-B-share.json): graph versus SDD | Both distinguish UA from a runtime SDK and reproduce conceptual boundaries. A also directly explains the RI producer and two materializations; B mostly explains UA, with limited RI implementation coverage. | A addresses the frozen RI-specific key more directly. The ambiguous task subject and unverified exposure prevent attributing this difference to an RI benefit or regression. |
| T08 — [A](T08-A-share.json), [B](T08-B-share.json): publication routes | Both reuse the PDF and LinkedIn/Medium owners, preserve canonical-source authority and explain Medium's manual image handling. Neither proposes an unnecessary competing pipeline. A is longer, which is not itself a quality advantage. | Both show useful workflow understanding; B reports known-owner reads without compact RI. |
| T09 — [A](T09-A-share.json), [B](T09-B-share.json): next-section owner | Both find the correct blueprint/manuscript, locate future planning in the blueprint and route drafting through prior material and research state. A gives more detailed research-register/carrier mapping; B emphasizes cumulative rereading and synchronization. | Owner selection works in both conditions. No section was written or reviewed, so conceptual synthesis is not tested. B reports direct reads without compact RI. |
| T10 — [A](T10-A-share.json), [B](T10-B-share.json): implementation versus benefit | B distinguishes deterministic capabilities/tests from unmeasured agent benefit and proposes bounded follow-up. A refuses access while quoting an altered ref. | B is the substantive answer that explicitly reports compact use, but payloads are redacted and there is no unassisted substantive original A counterpart. |
| T11 — dependency validation | Neither original response received. | No finding about dependency/compatibility reasoning. |
| T12 — extraction boundary | Neither original response received. | No finding about RI portability, packaging or product potential. |

Across the 8 original substantive pairs, this reading finds no clear, consistent additional advantage from the assigned RI instructions. That is a bounded qualitative observation, not a scored tie, an equivalence result or proof of zero effect. Detailed answers in both conditions can still omit required operational steps or answer an adjacent question.

## Supplements and the incorrect-ref failures

[T03-B-R1](T03-B-R1-share.json) returns a useful answer after the reported availability pause and again reports direct-source reading without compact RI. Its recommendation for a compact rule in agent instructions is less explicit than T03/A about first proving a gap in the existing contribution owner. That is a duplication risk to review, not evidence that a duplicate rule was actually introduced. This later answer cannot replace the original refusal or add another independent pair.

[T10-A-R1](T10-A-R1-share.json) first refuses, then answers substantively after the user repeats the correct ref. The original prompt already contained the correct 40-character SHA. The original T03/B and T10/A refusals and this retry's initial refusal instead quote the same 39-character variant, missing the penultimate `b`. The captures do not expose actual call arguments or errors. The safe diagnosis is therefore an observed ref/access failure in the answer, followed in T10-A-R1 by assisted recovery; its precise tool/model cause remains unknown.

The assisted answer correctly separates implementation checks from usefulness evidence. It shows that a substantive answer was possible in that later interaction. It does not establish that RI, a model switch or a quota reset caused either the failures or recovery. Both retry phases still report `gpt-5-6-mini`, and the continuation has extra user assistance. Preserve all phases without converting the continuation into a clean A/B result.

## Implemented mechanism versus demonstrated benefit

The [RI producer][producer] actually builds inventories and typed graph relations, materializes a compact agent view and provides owner/term/artifact/validation routing. The [architecture and operational route][ri] preserve source authority, allow direct reads when the owner is known and require fallback when projection delivery or freshness cannot be established. [Contribution guidance][contributing] and the [projection workflow][workflow] specify rebuilding, verifying and identifying the accepted source/surface. These are implemented affordances, not merely proposals.

They support a reasonable hypothesis: RI can reduce owner-discovery effort and help avoid terminology or ownership mistakes when the model lacks an initial path. The observed task mix often supplies or quickly exposes the owner; both arms also benefit from the existing curated bootstrap. In that setting the optional route may appropriately be bypassed. A lack of visible incremental benefit here neither invalidates the mechanism nor demonstrates that maintaining it pays off.

RI is also not an alternative conceptual authority. The model still needs the owning doctrine, patterns and research context to understand a concept's qualifications and apply it. A correct term-to-document association is a navigation result; it is not proof of a correct architectural judgment. The conceptual explanations in these answers are consistent with [SPECIFICATION.md][specification] and [control-loop anatomy][anatomy], but this collection cannot isolate whether the projection improves that understanding.

## Why stronger conclusions remain unavailable

1. **Exposure:** every exposed tool payload is redacted. T01/B reports compact truncation; T02/B does not establish compact delivery; T04/B–T09/B report direct-source routes. T10/B's reported compact use has no clean substantive primary counterpart. No actual RI exposure is independently verified.
2. **Comparability:** Auto routing changes reported labels on the two original refusals. Matching labels elsewhere are weaker than controlled model identity. Isolation and Memory-disabled compliance are unconfirmed; this is not proof of contamination. Organizer observations that main remained at the study commit do not prove tested-session source reads.
3. **Coverage and selection:** the organizer prepared the convenience corpus, some tasks overlap, and collection stopped at 20/24 original attempts after observed outcomes. Missing dependency and extraction tasks cannot be treated as successful. Eight substantive pairs do not establish statistical power or broad generality.
4. **Judgment independence:** this report is organizer interpretation with known arms. Independent blind scores remain absent, and answers themselves may reveal routes even in a future blinded packet.
5. **Cost:** measured input tokens, bytes, repository reads, latency and maintenance effort are absent. Exposed tool-message counts are not verified calls or traffic. Answer verbosity and repository file sizes cannot supply the missing cost denominator.

| Decision question | Supported conclusion |
|---|---|
| Can the tested client produce useful repository explanations? | Yes, the received substantive answers contain multiple source-consistent navigation and conceptual distinctions, alongside the identified omissions. This is not a general reliability estimate. |
| Do ordinary owning documents suffice for these tasks? | The A answers provide useful results across the 8 substantive paired tasks, and B often reports the same direct route. Actual reads remain unverified. |
| Does adding RI improve model understanding? | **Inconclusive; incremental benefit is not demonstrated in this collection.** |
| Does RI save context, time or money? | Unmeasured. |
| Is RI useless, harmful or worth expanding? | None of those general claims is established. T07 alone is not evidence of harm; implemented properties alone do not justify expansion. |
| Should collection continue under the same conditions now? | No further sessions are needed for this bounded report. More of the same redacted, unstable-routing evidence would not by itself resolve attribution or cost. |

A later study is justified only if a concrete decision requires it: for example, whether a reliably delivered compact surface improves unknown-owner discovery or application of a specific UA distinction to a new case. It would need stable model conditions, observable source/RI delivery, a frozen appropriate task and independent assessment. This report does not initiate that study or request more work from the maintainer.

## Source audit and preservation

Material answer checks used the study-state [contribution rules][contributing], [formatter configuration][formatter], [TypeScript configuration][typescript], [PDF contract][pdf], [export workflow][export], [platform contract][platform], [article blueprint][blueprint], [manuscript][manuscript], and RI/specification owners linked above. These sources are unchanged between the study commit and the collection cutoff. Links are pinned to the study commit so subsequent maintenance cannot silently change the comparison basis.

All original prompts, expectations, response fields, Share captures and supplemental phases remain unchanged. The collection record retains 24 original slots and the interruption. This report completes the requested organizer analysis; it does not mark independent scoring, full RI-EVAL acceptance, or Draft PR readiness as complete.

[ri]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/.github/REPOSITORY-INTELLIGENCE.md
[producer]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/.github/scripts/repository_intelligence.py
[contributing]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/CONTRIBUTING.md
[workflow]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/.github/workflows/metadata-integrity.yml
[specification]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/SPECIFICATION.md
[anatomy]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/00-doctrine/control-loop-anatomy.md
[formatter]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/.github/config/prettier.json
[typescript]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/tsconfig.json
[pdf]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/quartz/PDF-EXPORT.md
[export]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/.github/workflows/export-research-pdf.yml
[platform]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/quartz/PLATFORM-RENDITIONS.md
[blueprint]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/content/research/notes/open-engineering-specification-article-blueprint.md
[manuscript]: https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture/blob/989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3/content/research/notes/open-engineering-specification-article-draft.md
