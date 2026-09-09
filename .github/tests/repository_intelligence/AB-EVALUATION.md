# Repository Intelligence A/B Evaluation Protocol

## Purpose and estimand

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the normal Repository Intelligence route** over the repository's ordinary live-GitHub fallback route. It does not isolate the projection data from the workflow that verifies, queries, and interprets that data. Both primary arms use the same accepted repository state, the same model/configuration, the same root and scoped `AGENTS.md` instructions, the same GitHub connector, and the same task prompt.

The primary question is:

> Given the repository's normal contributor instructions and authority model, does the operational RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions, compared with the ordinary live-GitHub route?

A small optional diagnostic arm may later separate projection value from workflow value, but it is not part of the primary A/B acceptance claim.

The existing 12-case deterministic corpus remains a regression suite. It is not the independent held-out corpus because it was authored after exploratory work by an agent that already knew the implementation.

## 1. Why `AGENTS.md` does not invalidate the experiment

The normal root protocol tells an agent to use RI for owner discovery and preflight. Removing `AGENTS.md` from Control would create a different repository contract and would confound the comparison.

The experiment therefore uses a controlled benchmark ablation:

- both primary arms read the same root and applicable nested `AGENTS.md` files;
- Control treats RI as deliberately unavailable and follows the already-defined live-repository fallback;
- Treatment follows the normal operational RI route;
- semantic authority, provenance, safety, scoped-instruction, and repository-policy rules remain identical.

The root `AGENTS.md` already names some owners. That is shared production baseline information, not a treatment advantage. Exact-owner tasks are therefore ceiling/negative-control cases: both arms should often succeed, and RI must justify itself through observable cost or robustness rather than an artificial accuracy advantage.

The benchmark marker itself is an observer intervention because it exists in the tested instruction surface. Keep that intervention minimal, identical across arms except for the arm value, and report it as part of the experimental environment. Do not treat the benchmark marker as evidence for RI's usefulness.

## 2. Experimental design

The experimental unit is one **task × arm** run in a fresh isolated agent session.

Use a **paired randomized crossover design**:

- each held-out task is run once in Control (A) and once in Treatment (B);
- the pair uses the identical task prompt and pinned repository state;
- each run occurs in a separate fresh session so one arm cannot teach the other;
- arm order is randomized per task before execution;
- pairs are interleaved over time rather than running all A then all B;
- model family, selectable thinking configuration, connector permissions, client class, and repository commit are held equal within each pair;
- scoring uses a frozen evidence key and is locked before arm labels are revealed where practical.

Recommended first acceptance run: **12 paired tasks = 24 isolated sessions**.

Do not selectively rerun failures. If the pilot is ambiguous or shows high variance, repeat the complete preregistered paired set with a second frozen randomization seed.

### 2.1 Optional diagnostic C arm

The primary experiment answers whether the **operational RI route** is useful. It does not by itself determine whether any gain comes from the projection data or the prescribed RI workflow.

After the primary A/B outputs and scores are frozen, an optional **C — RI data-only diagnostic** may be run on 4–6 preregistered or separately frozen cases:

- provide the verified compact Agent Context Surface for the pinned state;
- do not provide RI query-operation output or task-specific RI routing suggestions;
- keep ordinary repository authority and source-reading rules unchanged;
- require the agent to decide how to use the compact data itself.

Interpret C only diagnostically:

- B > A and C ≈ B suggests the projection/data carries most of the gain;
- B > C and C ≈ A suggests the operational query/routing workflow carries most of the gain;
- B ≈ C ≈ A suggests no incremental agent value on those cases.

C must not be used post hoc to rewrite the primary A/B conclusion.

## 3. Isolation and validity

A primary-analysis run is invalid when prior benchmark/repository knowledge can materially leak into the tested session in a way that is not shared and controlled.

For every run record these fields explicitly:

- `conversation_fresh`;
- `memory_enabled`;
- `project_context_present`;
- `prior_repo_context_available`;
- `connector_state_equal` within the pair;
- exact displayed `model_family`;
- exact selectable `thinking_configuration`, or `unavailable`;
- client/environment class.

Required execution conditions:

1. Start a fresh conversation for every run.
2. Do not run inside a project/workspace that injects the held-out pack, prior arm output, or earlier benchmark design discussion.
3. Do not expose the answer key, expected owners, validators, companion files, or previous arm output.
4. Do not reuse a conversation across arms.
5. Do not give corrective scoring feedback until both runs in the pair are complete.
6. Keep repository/connector access equivalent within the pair.

For the primary analysis, mark a run invalid if `conversation_fresh` is false, the held-out key or previous-arm output was available, project context contains benchmark answers, connector access differs materially within the pair, or known prior repository context supplies the answer independently of the tested route.

If the product cannot establish whether cross-chat memory or prior repo context was available, record `unavailable` and treat the pair as an **isolation limitation**. Do not silently call it blind. If that uncertainty is material to the outcome, classify the experiment as inconclusive or repeat in a cleaner environment.

## 4. Held-out corpus and answer-key secrecy

### 4.1 Independence

The final held-out prompts and scoring key must be frozen before the first run and must not be adapted after observing RI rankings or A/B outputs. The assessor may inspect accepted repository sources to create objectively scoreable expectations, but should not tune prompts to known retrieval rankings.

### 4.2 Corpus composition: stress plus ecological tasks

The first 12-task corpus must be split into two declared halves:

**Six designed stress cases** test claimed RI failure surfaces. Across those six, cover a balanced subset of:

- canonical term / synonym pressure;
- overlapping artifact ownership;
- validation/companion routing;
- research-state versus framework-authority separation;
- impact reasoning where navigation or shared control hubs must not inflate blast radius;
- stale/unverifiable RI fallback;
- Ukrainian or paraphrased maintainer wording.

**Six ecological cases** must come from realistic UA maintainer work patterns rather than being selected because RI is expected to win. They should resemble tasks such as:

- review or modify an existing repository artifact;
- decide where a new concern belongs;
- assess whether glossary/roadmap/changelog/traceability companions are needed;
- inspect a realistic PR or publishing change;
- answer a repository-structure question;
- plan a bounded implementation change.

At least one ecological case should be an easy exact-owner/negative-control case. At least one should be a legitimate new-artifact case where the correct conclusion is that no existing owner fully covers the need.

The ecological set must be selected before arm execution from a frozen source pool or by an assessor who does not filter cases based on expected RI advantage.

### 4.3 Do not commit hidden prompts or answers before execution

The repository is the tested information environment. Committing the held-out prompts or scoring key before execution would contaminate the experiment.

Before the run, keep the complete held-out pack outside the repository view available to tested sessions. Preregister only non-revealing metadata and cryptographic commitments:

- corpus version and case count;
- six stress / six ecological classification;
- SHA-256 of exact serialized prompt pack;
- SHA-256 of exact serialized scoring key;
- repository source commit;
- model/configuration target;
- SHA-256 commitment to the randomization seed;
- primary/secondary endpoints and decision rule.

After all primary outputs and scores are frozen, the prompts, key, transcripts/measurement extracts where appropriate, and scoring record may be published and verified against the preregistered hashes.

## 5. Primary arm definitions

### A — Control: live GitHub orientation without RI

Control follows all normal repository authority and contributor rules, including root/nested `AGENTS.md`, but activates the benchmark-only ablation marker.

Allowed:

- GitHub tree/directory reads;
- GitHub code/file search;
- direct repository file reads;
- PR/diff/review/check/branch/commit reads when the task requires them;
- maintained source cross-links and navigation documents.

Disallowed for orientation:

- `assets/repository-intelligence/agent-context.json`;
- generated/full Graph View data;
- RI query operations such as `context-for-task`, `find-owner`, `term-preflight`, `artifact-preflight`, or `validation-plan`;
- Repository Control Map;
- copied RI output from another session.

Control may read `.github/REPOSITORY-INTELLIGENCE.md` only when the task itself is specifically about RI architecture. Reading it solely to reconstruct RI-derived routing defeats the ablation.

### B — Treatment: normal operational RI route

Treatment follows the production route:

- establish/verify compact-surface freshness for the pinned state;
- use the narrowest appropriate RI operation for orientation/preflight;
- read owning sources before making material decisions;
- fall back to live GitHub when RI is stale, missing, truncated, ambiguous, or unsupported;
- never infer authority from ranking or graph structure alone;
- do not load the full graph when the compact surface is sufficient.

The A/B result therefore supports or rejects the **operational RI route**, not the projection in isolation.

## 6. Neutral run envelope

Every primary run receives the same envelope except for the arm value:

```text
Repository: UncertaintyArchitectureGroup/uncertainty-architecture
Pinned source state: <commit SHA>
Experiment arm: RI-AB-CONTROL | RI-AB-TREATMENT
Task ID: <opaque ID>

Follow the repository's applicable contributor instructions and complete the task below. Do not ask for or search for benchmark answer keys, prior experiment outputs, or hidden scoring material. Report the repository sources you relied on and distinguish verified facts from inference.

Task:
<held-out prompt>
```

Opaque IDs must not reveal task category or expected owner. Do not tell either arm what RI is expected to improve.

## 7. Observable instrumentation

Do not use hidden model reasoning or infer when the model internally "knew" the answer.

Record, where observable:

- ordered connector/tool calls;
- number of connector calls before the **first explicit owner/route assertion in the visible response or tool-visible working output**, when such an assertion occurs before the final answer;
- total connector calls to final answer;
- broad search calls to final answer;
- ordered source files opened;
- total distinct source files opened;
- RI operations and returned payload bytes for Treatment;
- measured input/context/token volume when the product exposes it;
- elapsed time only when reliably observable;
- tool errors, truncation, stale-context events, and fallbacks;
- final response/transcript reference.

Do **not** use "files opened before the first materially correct decision" as a primary cost measure when the decision point is not externally observable. Do not estimate unavailable token counts or latency from prose length.

## 8. Scoring

Each case has a frozen repository-verifiable scoring key. Score arm-hidden responses where practical.

Dimensions:

- **Owner/routing correctness (0–2):** wrong/missing; partially correct; correct canonical owner/route.
- **Evidence sufficiency (0–2):** unsupported/material evidence gap; correct direction but material uncertainty remains; decision sufficiently supported by authoritative evidence.
- **Authority discipline (0–2):** authority incorrectly inferred/promoted; minor ambiguity; correct source-of-truth distinctions.
- **Companion/validation completeness (0–2)** when applicable: material validator/scope/companion missed; partial; complete.
- **Decision quality (0–2):** wrong repository action/proposal; directionally right with material gap; correct bounded decision.

`Evidence sufficiency` rewards support for the decision, **not the number of files read**. File/read volume is a cost metric only.

Mark genuinely inapplicable dimensions `NA`; do not award free points.

A **serious routing error** is any of:

- wrong canonical owner asserted as authoritative;
- duplicate canonical term/artifact proposed despite an existing owner that should be refined;
- research/history/example material promoted to framework authority;
- required scoped `AGENTS.md` missed in a way that changes permissible workflow;
- material validator/companion omitted such that the proposed action would violate an existing repository contract;
- candidate/proposed state presented as accepted state.

### Blind scoring

Preferred order:

1. remove arm labels and route-specific metadata from response copies used for correctness scoring;
2. randomize the two responses within each task;
3. score against the frozen key;
4. lock scores;
5. reveal arm labels and combine with cost measurements.

If blind scoring is impractical, record the limitation and keep the key frozen.

## 9. Endpoints

### Primary endpoint

Report the paired serious-error matrix across valid pairs:

- A wrong / B correct;
- A correct / B wrong;
- both correct;
- both wrong.

Do not convert 12 cases into a spurious precise population estimate.

### Secondary correctness endpoint

Report per-case total applicable correctness score and B−A delta, plus median paired delta.

### Cost endpoints

Report paired differences for observable measures:

- total connector calls to final answer;
- broad searches to final answer;
- distinct source files opened;
- calls before first explicit visible owner/route assertion, when observable;
- measured context/token volume when available;
- RI payload bytes;
- elapsed time when reliably available.

Report stress and ecological halves separately as well as together. A gain confined to designed stress cases must not be presented as demonstrated broad routine productivity improvement.

## 10. Preregistered stop/go decision rule

The first run is a decision experiment, not a leaderboard.

Use the following rule for the 12-pair pilot:

- **GO / retain operational RI:** at least **2** valid `A wrong / B correct` serious-error reversals, **0** `A correct / B wrong` reversals, no systematic correctness regression on ecological cases, and no clearly disproportionate routine orientation-cost regression.
- **WEAK POSITIVE / REPLICATE:** exactly **1** `A wrong / B correct`, **0** reverse serious errors, with otherwise non-worse correctness. Treat this as a signal, not acceptance; repeat the full paired study before claiming agent benefit.
- **GO, OPTIMIZE COST:** the correctness criterion for GO is met, but exact-owner/routine ecological cases show repeated avoidable RI cost. Preserve semantics and optimize retrieval/materialization before adding new retrieval technology.
- **NO INCREMENTAL VALUE SHOWN:** serious-error outcomes and material correctness are equivalent and RI does not reduce observable orientation cost. Keep the projection for other demonstrated consumers, but do not claim agent productivity benefit.
- **REGRESSION:** RI introduces any serious error on a case Control handled correctly, or systematically increases cost without compensating correctness. Fix the measured failure before expansion.
- **INCONCLUSIVE:** invalid pairs, isolation uncertainty, source-state mismatch, tool availability, scoring ambiguity, or other protocol defects prevent a defensible comparison.

The cost phrase "clearly disproportionate" must be interpreted from the preregistered paired metrics and case context; do not invent a post hoc percentage threshold after unblinding. If a numeric threshold is desired, preregister it before execution.

No embeddings, vector database, MCP service, graph database, inferred semantic edges, or additional retrieval layer is justified unless a measured failure identifies a concrete need that the simpler route cannot address.

## 11. Randomization and execution

Before any primary run:

1. freeze repository source commit;
2. freeze the six stress and six ecological prompts plus scoring key;
3. record their SHA-256 commitments;
4. freeze model/client/configuration target;
5. generate randomized A/B order per task from a committed seed hash;
6. assign opaque run IDs;
7. verify equivalent connector/repository access;
8. verify the isolation fields required by Section 3 can be recorded.

Execute pairs in randomized, interleaved order. Do not stop early because one arm appears to win.

Do not run optional C until primary A/B outputs and scores are frozen unless C was itself fully preregistered as a co-primary design.

## 12. Result report

The final report must include:

- preregistered hashes and source commit;
- exact model/client/configuration and isolation limitations;
- case provenance classification: stress or ecological;
- all valid paired outcomes and all invalidated runs with reasons;
- serious-error matrix overall and by corpus half;
- correctness-score deltas;
- observable connector/search/file/context cost deltas;
- stale/fallback behavior;
- deviations made before unblinding;
- post-unblinding exploratory changes, clearly labelled;
- stop/go conclusion tied exactly to Section 10;
- optional C results separately from primary evidence;
- follow-up only for measured failures.

Publish hidden prompts and the scoring key only after primary outputs and scoring are frozen, then verify them against the preregistered commitments.

## 13. What this experiment does not prove

A successful primary result supports the claim that the **operational RI route** improves repository orientation for the tested model/client/source state and task distribution. It does not prove:

- that the projection alone caused the gain;
- universal productivity improvement for all repositories or models;
- semantic understanding by the graph itself;
- that rankings establish authority;
- that the visual Control Map improves agent behavior;
- that future repository states have the same cost/benefit;
- that connector bytes equal model tokens;
- that deterministic regression tests substitute for independent agent evaluation.

Rerun the experiment after material changes to RI retrieval semantics, agent routing policy, model/client behavior, or repository scale when the old evidence no longer represents the operational system.
