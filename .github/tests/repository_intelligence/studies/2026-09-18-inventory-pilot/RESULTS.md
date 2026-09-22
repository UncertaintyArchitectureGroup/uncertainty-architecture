# Forced RI-inventory pilot: results and adoption decision

**No incremental quality benefit was demonstrated for the supplied inventory in this four-task local pilot.** All four paired quality scores tied, with no serious error in either condition. The inventory also did not reduce the recorded source-reading burden. Neither task family passed its frozen benefit gate, so this iteration leaves production agent guidance unchanged and does not make RI mandatory.

This is a result about one small RI-derived inventory presentation under the conditions below. It is not evidence that every RI capability is useless, proof of equivalence, or a strict v11 benefit/cost verdict. The earlier connector study remains separate and inconclusive about incremental benefit.

## What was compared

All eight sessions used ordinary sources from commit `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`, with the same logged source reader. A received the task without RI. B received the complete 7,126-byte [inventory](ri-inventory.txt) literally in its starting message: all 48 artifact identities with titles, status and declared canonical ownership, plus 46 glossary terms, anchors and explicit predecessors. This task-independent view was prepared before the task author's results; it contains no task-specific answers. It omits graph relations, other metadata, research/instruction inventories and validation routing. The full projection was not injected.

Four new Ukrainian tasks and their expected outcomes were prepared by a separate fresh author using ordinary sources, without the inventory, retrieval rankings or previous answers. [Tasks and scoring expectations](tasks.json), the [protocol](README.md), reader and all eight exact starting messages were frozen before dispatch. Every first answer is retained; no tested agent received a repair message, hint or retry.

Each tested agent started with `fork_turns=none`, the same inherited model/reasoning configuration and no override. This is the configured equality available through the native agent interface; exact backend snapshot identity is unknown. The runs are not the user's former ChatGPT Auto sessions. The reader blocked generated RI and old benchmark evidence. Other-file/tool restrictions were instructional, not an OS sandbox: the available record contains no reported breach, but it cannot independently attest platform-wide isolation or hidden access.

The literal starting messages establish an input contrast: four sessions were supplied the inventory and four were not. They do not prove internal use of every inventory item. All eight sessions returned substantive answers. Recorded source chunks and their hashes were checked against the unchanged pinned snapshot; root instructions and every cited source were fully read through the reader. No reader error, refusal or missing outcome occurred.

## Blind assessment

A separate fresh scorer received exact task wording, frozen expectations, owning sources and shuffled verbatim answers under opaque IDs. It did not receive the arm mapping, inventory, reader logs or dispatch order. Its first finalized scores were hashed and frozen before the organizer applied the mapping. The organizer did not assign semantic scores or revise the key after answers.

The scale was frozen as 0 = materially incorrect or serious error; 1 = partially correct and needs maintainer correction; 2 = meets the substantive expectations with owning evidence. These are ordinal assessments, not percentages of repository understanding.

| Task | Without RI (A) | With inventory (B) | Assessment |
|---|---:|---:|---|
| N1: find the owner for failing human/fallback capacity and control economics | 2 | 2 | Both find the correct project owner and supporting routes |
| N2: preflight a proposed duplicate AI launch passport | 1 | 1 | Both reject duplicate ownership, but leave part of the ownership map unstated |
| C1: apply UA to a human-approved procurement assistant | 2 | 2 | Both distinguish model influence, meaningful human authority and execution |
| C2: assess a change from recommendations to automatic document-access grants | 2 | 2 | Both separate evidence, bounded guarantees, project authorization and release |

There are **0 B wins, 0 B losses and 4 ties**, and **0 serious errors among 8 answers**. Equal coarse scores do not establish semantic identity or statistical equivalence.

The shared N2 gap matters: neither answer explicitly assigns concrete Judgment Nodes and the local Requirement to Thinking System Review. B also leaves delivery-local reassessment ownership unstated. Both correctly preserve project/delivery separation, versioned inheritance and informative-template status, so the scorer assigns partial credit rather than a serious error. The inventory did not remove this omission.

C1 and C2 show successful application of the repository's concepts in both conditions: human approval and absent model API credentials do not eliminate consequential model influence; deterministic execution does not establish semantic correctness; DoD and model scores do not authorize expanded autonomy. This supports the limited observation that agents can produce useful, source-grounded conceptual analyses through ordinary-source reading. It does not establish deeper transfer, reliable future engineering performance, or an RI-caused improvement.

The scorer disclosed residual blinding limits: ordinary `AGENTS.md` reveals generic RI experiment vocabulary, repeated prompts identify pairs, and answer style can provide cues. It reports no inferred arm assignment. Author, tested agents and scorer have separate conversation contexts, but this is agent assessment, not independent human replication; correlated errors remain possible. See the complete [criterion findings](scores.json).

## Recorded reading burden

| Task | Reader operations A / B | Reader-response UTF-8 bytes A / B |
|---|---:|---:|
| N1 | 21 / 22 | 113,118 / 111,404 |
| N2 | 35 / 35 | 199,146 / 203,413 |
| C1 | 35 / 37 | 205,301 / 222,812 |
| C2 | 35 / 36 | 209,215 / 214,697 |
| Total | 126 / 130 | 726,780 / 752,326 |

Initial messages add 12,463 bytes in A and 41,279 in B. Of B's message bytes, 28,504 are the four literal inventory blocks. Thus recorded reader responses plus complete initial messages total **739,243 bytes in A and 793,605 in B: B is 54,362 bytes, about 7.4%, larger**. N1's small reduction in source bytes does not offset its added inventory input. No observed pair has fewer B reader operations.

These are instrumented UTF-8 payload counts, not actual model input tokens, total runtime traffic, elapsed time, billing or economic return. The reader paginates files; operations are not unique files. System instructions, native tool framing, repeated context processing, internal reasoning, preparation and inventory extraction costs are not measured. Runs overlapped, so latency is not compared. Required full-source reading and the short answer budget also limit how this workflow represents other agent tasks. The result establishes no measured savings here and no universal cost penalty.

## Decision and remaining uncertainty

The frozen family gate required two usable pairs, both B answers scoring 2, no B quality loss or new serious error, and at least one B improvement. Navigation fails that gate because N2 scores 1 and neither pair improves. Application has two correct B answers but no improvement over A, so it also fails. No benefit signal justifies the proposed limited adoption trial.

Accordingly, **do not introduce mandatory inventory loading or strengthen the existing RI requirement on this evidence**. Retain the existing optional preflight route, direct reading of known owners, source-authority checks and fallback. No production instruction, retrieval implementation or acceptance threshold changes in this iteration. This is a decision not to impose an unproven extra input cost, not a finding that optional RI never helps.

Uncertainty remains about the full projection, graph/impact queries, source changes, multilingual recovery, reuse across a longer session, weaker configurations, repository edits and the actual connector/iPad workflow. Four convenience tasks, one realization per condition and a coarse scale cannot estimate a general effect or rule out small improvements. No statistical significance or whole-repository acceptance claim is made. More runs are not requested merely to obtain a favorable result; a future experiment would need a distinct decision and a frozen intervention that exercises it.

The [earlier organizer analysis](../2026-09-17-initial/ANALYSIS.md) and its raw attempts remain byte-identical. This new study supplies a verifiable initial-message contrast that the earlier collection lacked, but does not repair its missing exposure/cost evidence, finish its pending independent scoring, or satisfy all [RI-EVAL acceptance prerequisites](../../../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

## Evidence and reproduction boundaries

- [Input freeze](freeze.json) and [frozen-inputs.zip](frozen-inputs.zip): exact pre-dispatch protocol, tasks, author note, inventory, reader and eight-message skeleton. Archiving occurred after collection from the verified original bytes; no pre-run Git publication is claimed.
- [Runs](runs.json): first-answer hashes and paths, model fields, read coverage, errors and payload counts. `sessions.json` remains the unchanged input skeleton. Answers use source-root-relative paths preserved verbatim in `answers/*.txt`.
- [reader-evidence.zip](reader-evidence.zip): original reader journals, source manifest and preparation smoke. The source snapshot can be reconstructed from the pinned Git commit with generated RI output omitted.
- [assessment-evidence.zip](assessment-evidence.zip): exact arm-hidden packet, first finalized scores, score freeze and mapping. Packet SHA-256 is `631c6d846932695280b7d000f68b27b877ff429dfe7cb038424921674ab28caf`; original score SHA-256 is `814bbe444d5bda770c5fbeed0d16817c3efcb4b392ce46f840c35c23b32d2d66`.
- [Score freeze](score-freeze.json), [answer mapping](answer-mapping.json) and [derived results](results.json): the join from opaque assessment IDs to runs, per-pair outcomes, exact totals and family decisions. Archives preserve original serialization even if working JSON is formatted later.

These artifacts support audit and re-scoring. Native platform execution, backend identity and unobserved context cannot be reconstructed from them. Repository CI validates the committed evidence and repository contracts; it does not prove an RI benefit.
