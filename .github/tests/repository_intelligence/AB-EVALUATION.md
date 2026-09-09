# Repository Intelligence A/B Evaluation Protocol

## Purpose

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The experiment measures the **incremental value of Repository Intelligence (RI)** for AI-assisted repository work. It does not ask whether an agent can navigate the repository at all. Both arms use the same accepted repository state, the same model/configuration, the same root and scoped `AGENTS.md` instructions, the same GitHub connector, and the same task prompt. The only experimental difference is whether the agent may use the RI projection/preflight surface.

The primary question is:

> Given the repository's normal contributor instructions and authority model, does RI reduce routing mistakes or orientation cost without degrading material decisions?

The existing 12-case deterministic corpus remains a regression suite. It is not the independent held-out corpus for this experiment because it was authored after exploratory work by an agent that already knew the implementation.

## 1. Why `AGENTS.md` does not invalidate the experiment

The normal root protocol tells an agent to use the RI route for owner discovery and preflight. Removing `AGENTS.md` from one arm would therefore create a different repository contract and would confound the result.

The experiment instead uses a **controlled ablation mode** defined in root `AGENTS.md`:

- both arms read the same `AGENTS.md` and all applicable nested instructions;
- the **control arm** is explicitly authorized, only for a frozen benchmark run, to use the documented live-repository fallback and to avoid RI generated surfaces/operations;
- the **treatment arm** follows the normal RI route;
- all semantic authority, provenance, safety, scoped-instruction, and repository-policy rules remain identical in both arms.

This tests RI as an additional orientation instrument rather than testing two different instruction systems.

The fact that `AGENTS.md` already names some canonical owners is **shared baseline information**, not contamination. It creates a useful ceiling condition: on easy exact-owner tasks both arms should often be correct, and RI should justify itself through lower orientation cost rather than an artificial accuracy advantage. Harder tasks must therefore require relationship recovery, scoped routing, overlap detection, validation planning, authority separation, fallback, or impact reasoning that is not answered by one explicit root-table row.

## 2. Experimental unit and design

The experimental unit is one **task × arm** run in a fresh isolated agent session.

Use a **paired A/B crossover design**:

- each held-out task is run once in Control (A) and once in RI (B);
- A and B runs for the same task use the identical prompt and repository source state;
- each run occurs in a separate fresh session so one arm cannot teach the other;
- arm order is randomized per task before execution;
- the same model family, model setting/thinking level, connector permissions, client class, and source commit are used for the pair;
- task scoring is performed against a frozen evidence key, not against which arm produced the answer.

Recommended first acceptance run: **12 paired tasks = 24 isolated sessions**. If variance is high or several results are ambiguous, repeat the complete paired set with a second randomization seed rather than selectively rerunning failures.

## 3. Isolation requirements

A run is invalid if prior experiment knowledge can materially leak into the tested session.

For every run:

1. Start a fresh chat/session with no prior benchmark conversation loaded.
2. Do not place the session in a project/workspace that injects earlier repository-test conversations or the held-out answer key.
3. Keep personal memory or cross-chat context unavailable to the tested session where the product supports that isolation mode.
4. Supply only the task prompt, the arm marker, the pinned repository ref, and any task-specific live PR/commit identifiers required by the case.
5. Do not expose the held-out case file, scoring key, expected owner, expected validators, expected companion files, or previous arm output to the tested session.
6. Do not reuse the same conversation for A and B.
7. Do not let the scorer give corrective feedback until both arms for that task are complete.

If the product cannot guarantee a particular isolation control, record it as a limitation instead of pretending the run is blind.

## 4. Held-out corpus and answer-key secrecy

### 4.1 Corpus authorship

The held-out corpus must be authored or selected by an assessor who does not adapt tasks after seeing RI rankings or A/B outputs. The assessor may use accepted repository sources to define objectively scoreable expectations.

A model or maintainer that already knows the repository may help define the **strata and protocol**, but the final held-out prompts and answer key must be frozen before the first experimental run.

### 4.2 Do not commit the answer key before the experiment

The repository is itself the tested information environment. Committing held-out prompts and expected answers into the accessible repository before execution would contaminate the experiment.

Before the run, keep the complete held-out pack outside the repository view available to tested sessions. Commit only a **cryptographic commitment** and non-revealing study metadata if a durable pre-registration record is desired:

- corpus version;
- case count and strata;
- SHA-256 of the exact serialized held-out prompt pack;
- SHA-256 of the exact serialized scoring key;
- repository source commit;
- model/configuration target;
- randomization seed or SHA-256 commitment to it;
- planned primary and secondary metrics.

After all runs are complete and frozen, the corpus, answer key, raw transcripts/measurement extracts where appropriate, and scoring record may be published into the repository or a review artifact and checked against the pre-registered hashes.

### 4.3 Required task strata

The 12-task first run should cover at least these distinct failure surfaces, with no two tasks differing only by wording:

1. exact canonical owner recovery (**negative-control / ceiling case**);
2. existing canonical term / synonym temptation;
3. ambiguous near-synonyms requiring source reading;
4. apparent new artifact that should refine an existing owner;
5. legitimate new artifact where no existing owner is sufficient;
6. validation/companion routing for a repository-policy or publishing change;
7. research-state versus framework-authority boundary;
8. impact query where navigation links must not inflate blast radius;
9. shared scope/validator hub where traversal must remain first-order/terminal;
10. stale or unverifiable RI materialization requiring live-source fallback;
11. Ukrainian maintainer wording with no guaranteed lexical match;
12. paraphrased task whose correct route is not named directly in the prompt.

PR-state-specific trusted-comparison/security cases remain deterministic regression requirements and may be included in the human/agent A/B corpus only when they can be run identically in both arms without exposing the answer key.

## 5. Arm definitions

### A — Control: live GitHub orientation without RI

The control arm follows all normal repository authority and contributor rules, including root/nested `AGENTS.md`, but activates the benchmark-only ablation marker defined by that protocol.

The agent may use:

- GitHub repository tree/directory reads;
- GitHub code/file search;
- direct file reads;
- PR, diff, review, check, branch, and commit reads when the task requires them;
- ordinary source cross-links and maintained navigation documents.

The agent must not use:

- `assets/repository-intelligence/agent-context.json`;
- generated/full Graph View data;
- `repository_intelligence.py` query operations (`context-for-task`, `find-owner`, `term-preflight`, `artifact-preflight`, `validation-plan`, or equivalent);
- Repository Control Map as an orientation source;
- copied RI query results supplied by another session.

The control arm may read `.github/REPOSITORY-INTELLIGENCE.md` only if the task itself is specifically about changing RI architecture. For ordinary repository-orientation tasks, reading that architecture solely to recover RI-derived routing would defeat the ablation and is disallowed.

### B — Treatment: normal RI-assisted orientation

The treatment arm follows the ordinary operational route:

- verify or establish freshness of the compact surface for the pinned state;
- use the narrowest appropriate RI operation for orientation/preflight;
- read the owning source before making a material decision;
- fall back to live GitHub when RI is stale, missing, truncated, ambiguous, or unsupported;
- never infer authority from ranking or graph structure alone.

The treatment arm must not load the full graph merely because it exists when the compact surface is sufficient.

## 6. Standard run prompt envelope

Every run receives the same neutral envelope except for the arm marker:

```text
Repository: UncertaintyArchitectureGroup/uncertainty-architecture
Pinned source state: <commit SHA>
Experiment arm: RI-AB-CONTROL | RI-AB-TREATMENT
Task ID: <opaque ID>

Follow the repository's applicable contributor instructions and complete the task below. Do not ask for or search for benchmark answer keys, prior experiment outputs, or hidden scoring material. Report the repository sources you relied on and distinguish verified facts from inference.

Task:
<held-out prompt>
```

The opaque task ID must not encode the expected owner/category.

Do not tell either arm what the experiment expects RI to improve.

## 7. Instrumentation

For each run record, as available:

- run ID, task ID, arm, source commit, date/time;
- model family and selectable model/thinking configuration;
- client/environment class (for example ChatGPT iPad, web, Work/connector session);
- whether memory/project-history isolation was available and enabled;
- every GitHub connector read/search/action used for orientation;
- ordered list of files opened before the first materially correct owner/route decision;
- RI operations used and RI response bytes for Treatment;
- broad searches before correct owner recovery;
- connector call count;
- source files opened;
- measured input/token/context volume when the product exposes it; otherwise mark unavailable;
- time-to-final-answer when reliably observable; otherwise mark unavailable;
- final answer/transcript reference;
- tool errors, truncation, stale-context events, and fallbacks.

Do not estimate missing token counts or latency from prose length.

## 8. Scoring

### 8.1 Scoring key

Each held-out case has a frozen answer key containing only repository-verifiable criteria. The scorer must evaluate outputs without changing the key after seeing either arm.

For each case score these dimensions:

- **Owner/routing correctness (0–2)**: wrong/missing; partially correct; correct canonical owner/route.
- **Required source reading (0–2)**: material owner/dependency omitted; incomplete; sufficient source set read before decision.
- **Authority discipline (0–2)**: authority incorrectly inferred/promoted; minor ambiguity; correct source-of-truth distinctions.
- **Companion/validation completeness (0–2)** when applicable: material validator/scope/companion missed; partial; complete.
- **Decision quality (0–2)**: wrong repository action/proposal; directionally right with material gap; correct bounded decision.

Cases where a dimension is genuinely inapplicable mark it `NA`; do not award free points.

A **serious routing error** is any of:

- wrong canonical owner asserted as authoritative;
- duplicate canonical term/artifact proposed despite an existing owner that should be refined;
- research/history/example material promoted to framework authority;
- required scoped `AGENTS.md` missed in a way that changes the permissible workflow;
- material validator/companion omitted such that the proposed change would violate an existing repository contract;
- candidate/proposed state presented as accepted state.

### 8.2 Blind scoring

Preferred scoring order:

1. strip arm labels from the final responses and measurement summaries;
2. randomize A/B response order within each task;
3. scorer evaluates correctness against the frozen key;
4. reveal arm labels only after scoring is locked.

If true blind scoring is not practical, record that limitation and keep the answer key frozen.

## 9. Primary and secondary endpoints

### Primary endpoint

**Paired serious-routing-error difference** across the held-out tasks.

RI passes the primary usefulness test if it reduces serious routing errors without creating a new serious error on a case the control arm handled correctly.

For a 12-case pilot, report raw paired outcomes instead of pretending the sample supports a precise population estimate:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

### Secondary correctness endpoint

Compare paired total correctness scores across applicable dimensions. Report the per-case delta and median paired delta.

### Cost endpoints

Compare paired:

- connector calls before material decision;
- broad searches before material decision;
- files opened before material decision;
- measured context/token volume when available;
- RI payload bytes read;
- time when reliably available.

RI should not be declared useful merely because it is more correct if the orientation cost becomes clearly disproportionate for routine tasks. Conversely, a small cost increase may be acceptable when it prevents serious repository errors. Report the trade-off rather than hiding it in one aggregate score.

## 10. Stop/go interpretation

The first independent run is a **decision experiment**, not a benchmark leaderboard.

Use these outcomes:

- **GO / retain and use RI**: RI prevents at least one serious routing error, introduces none, and does not show a clearly disproportionate orientation-cost regression across routine cases.
- **GO, optimize retrieval cost**: RI materially improves correctness but repeatedly adds avoidable reads/context on exact-owner tasks; preserve RI semantics and optimize routing/materialization before adding retrieval technology.
- **NO INCREMENTAL VALUE SHOWN**: both arms are materially equivalent in correctness and RI does not reduce orientation cost. Keep deterministic projection only for Control Map/other demonstrated consumers; do not claim agent productivity benefit.
- **REGRESSION**: RI creates serious errors or systematically increases cost without compensating correctness. Fix the named failure before expanding RI.
- **INCONCLUSIVE**: isolation, scoring, source-state parity, tool availability, or sample ambiguity prevents a defensible comparison. Repeat with the defect fixed; do not cherry-pick successful cases.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified by this experiment unless the measured failure identifies a concrete need that the simpler route cannot address.

## 11. Randomization and execution plan

Before any run:

1. freeze repository source commit;
2. freeze held-out prompt pack and answer key;
3. record their SHA-256 commitments;
4. choose/freeze model and configuration;
5. generate a random A/B order per task from a recorded seed;
6. assign opaque run IDs;
7. verify both arms have identical repository/connector access.

Execute task pairs in randomized order. Do not run all A sessions first and all B sessions second if model/service behavior may change over time. Interleave them while keeping every individual run isolated.

Do not stop early because one arm appears to be winning.

## 12. Result report

The final report must include:

- pre-registered hashes and source commit;
- environment/model limitations;
- all 12 paired task outcomes;
- serious-error matrix;
- correctness-score deltas;
- connector/search/file/context cost deltas;
- stale/fallback behavior;
- invalidated runs and why;
- deviations from this protocol made before unblinding;
- deviations made after unblinding, clearly labelled exploratory;
- stop/go conclusion tied to the observed data;
- concrete follow-up only for measured failures.

Publish raw case prompts and answer key only after the experimental outputs and scoring are frozen, then verify them against the pre-registered commitments.

## 13. What this experiment does not prove

A successful result would support the claim that RI improves repository orientation for the tested model/client/source state and task distribution. It does not prove:

- universal productivity improvement for all repositories or models;
- semantic understanding by the graph itself;
- that rankings establish authority;
- that the visual Control Map improves agent behavior;
- that future repository states will have the same cost/benefit;
- that measured connector bytes equal model tokens;
- that a green deterministic regression suite substitutes for independent agent evaluation.

The experiment should be rerun after a material change to RI retrieval semantics, agent routing policy, or repository scale if the old evidence no longer represents the operational system.
