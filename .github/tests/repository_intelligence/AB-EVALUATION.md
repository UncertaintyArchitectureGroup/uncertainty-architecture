# Repository Intelligence A/B Evaluation Protocol

> Protocol version: 10

## Purpose

This protocol defines the independent comparative evaluation required by [`REPOSITORY-INTELLIGENCE.md`](../../REPOSITORY-INTELLIGENCE.md#14-evaluation-and-acceptance).

The primary estimand is the **incremental operational value of the connector-delivered compact Repository Intelligence (RI) route** over the repository's ordinary live-GitHub orientation route under one stable repository state.

Primary question:

> Given the same repository instructions, model/client configuration, source state, and task prompt, does the compact RI route reduce serious routing mistakes or observable orientation cost without degrading material decisions compared with ordinary live-GitHub bootstrap/search?

The primary A/B does **not** isolate relational graph value, graph visualization, the Repository Control Map, local CLI behavior, or another adapter. Those require separate diagnostics.

## 1. Shared baseline and arms

Both arms read the same root and scoped `AGENTS.md` files and use the same repository authority model.

- `RI-AB-CONTROL`: ordinary live-GitHub orientation with RI deliberately unavailable.
- `RI-AB-TREATMENT`: the same baseline plus the exact committed compact Agent Context Surface delivered through the connector.
- `RI-AB-DATA-ONLY`: optional post-primary diagnostic only.

Protocol v10 primary evidence is **connector-compact-surface only**. `local_cli`, `dedicated_adapter`, RI query helpers, the full Graph View, and the Repository Control Map are outside the primary Treatment boundary. A later study may define another delivery mode explicitly.

The benchmark marker is an unavoidable observer intervention. The model is arm-aware, which can create demand-characteristic effects; report this limitation explicitly.

## 2. Study design

The unit is one **task × arm** run in a fresh isolated session.

The primary study uses two independently held-out waves frozen before Pilot:

- Pilot: 12 tasks = 6 stress + 6 ecological.
- Confirmatory: 12 different tasks = 6 stress + 6 ecological.

Each task runs once in each arm, yielding **48 primary sessions across 24 distinct tasks**. Both waves run regardless of Pilot performance unless experiment infrastructure validity fails. Do not selectively rerun unfavorable valid results.

## 3. Stable source state and evidence-derived lock

Use a preregistered `stable_default_branch_window`:

1. select the exact study commit and require the default-branch tip to equal it;
2. freeze repository mutations through all primary sessions;
3. preserve ordinary default-branch GitHub search in both arms while the lock is valid;
4. use exact-ref direct reads where supported;
5. record exactly one structured `branch_tip_pre` event before task orientation and one `branch_tip_post` event after task orientation in every run;
6. each branch-tip event must carry the observed default-branch SHA and it must equal the study ref;
7. stop the study on lock failure and invalidate affected runs.

Run-level `source_state_pre_sha` and `source_state_post_sha` are summaries only. The evaluator derives the authoritative lock evidence from the ordered branch-tip events and requires the summaries to match.

The branch-tip events must identify the preregistered default branch in both `ref` and `resource`. Each other repository event must also establish its permitted source route; marking a read as study infrastructure does not exempt it:

- Direct reads use `ref` equal to the exact study SHA. If a connector cannot pin a read, only an omitted/null ref or the preregistered default branch is allowed, and that read must carry `observed_ref_sha` equal to the study SHA from its own source evidence. Do not copy the surrounding branch-tip checks into this field as a substitute for read-level evidence.
- Ordinary `search` / `code_search` events may use an omitted/null ref, the preregistered default branch, or the exact study SHA under the required pre/post lock. This exception applies only to `ordinary_source` events, not Treatment-surface acquisition.
- Any supplied `observed_ref_sha` must agree with the study SHA. Another explicit SHA, branch, tag, or contradictory resolved SHA is rejected even when the surrounding tip checks pass.

Search-index lag is baseline behavior and is not silently corrected out of Control. If the default branch cannot remain stable, do not silently weaken the lock; preregister a separate immutable evaluation repository in a future protocol revision.

## 4. Treatment delivery and identity

Protocol v10 fixes primary Treatment to `connector_compact_surface` and the exact path `assets/repository-intelligence/agent-context.json`.

Freeze:

- repository path;
- Git blob SHA;
- full-content SHA-256;
- RI source identity/digest.

The evaluator receives the exact Treatment surface as evidence and recomputes those identities from its bytes.

Every compact-surface delivery event records `payload_byte_start`, `payload_byte_end`, and `payload_chunk_sha256`. The evaluator requires all chunks to belong to the exact frozen identity and to cover byte interval `[0, surface_size)` exactly once with no gaps, overlap, duplicate range, or hash mismatch.

A different blob, digest, source identity, truncated payload, invented byte range, or unverifiable payload is **Treatment delivery failure**. The primary Treatment may use the compact surface plus ordinary authoritative repository sources only. Any task-orientation `ri_query`, `ri_full_graph`, or `repository_control_map` event invalidates the Treatment run.

Task-level fallback to ordinary authoritative sources after successful compact-surface delivery remains valid Treatment behavior.

## 5. Execution eligibility and isolation

Before Pilot, run a non-scored smoke test in the actual client. Freeze an immutable smoke-evidence reference and SHA-256. It must establish:

- source-state pre/post checks;
- ordinary Control search;
- exact-ref reads where supported;
- complete Treatment delivery for the same state;
- truncation verification;
- instrumentation capture;
- connector-permission parity;
- Memory disabled;
- Project/workspace context absent;
- prior product-supplied repository context absent;
- repository-mutation freeze acknowledged.

If exact connector bytes/ranges cannot be observed strongly enough to verify complete compact-surface delivery, the v10 primary study is **ineligible**. Do not invent offsets or downgrade the requirement after seeing results.

Primary runs require a fresh conversation, Memory disabled, no Project/workspace context, no prior product-supplied repository context, no previous-arm output, no corrective scoring feedback before pair completion, no future-wave or hidden benchmark material, the same displayed model family/thinking configuration/client/connector/source state, and no protocol violation.

## 6. Held-out corpora

### 6.1 Mandatory scenario coverage

Across the 24 tasks cover every mandatory scenario family inherited from `RI-EVAL-001`:

- `exact-owner-recovery`;
- `canonical-term-synonym-pressure`;
- `near-synonym-source-review`;
- `overlapping-artifact-refinement`;
- `legitimate-new-artifact`;
- `impact-validation-routing`;
- `accepted-proposed-relation-change`;
- `branch-behind-target`;
- `producer-schema-self-change`;
- `candidate-data-boundary`;
- `shared-structural-hub`;
- `research-authority-separation`;
- `stale-materialization-fallback`;
- `ukrainian-or-paraphrased-routing`.

Confirmatory must itself cover `accepted-proposed-relation-change`, `branch-behind-target`, `producer-schema-self-change`, `candidate-data-boundary`, `shared-structural-hub`, and `stale-materialization-fallback`.

The evaluator verifies declared coverage; human review of revealed prompts still confirms that the cases genuinely exercise those scenarios.

### 6.2 Ecological sampling frame: freeze before normalization

Ecological validity starts from a **sampling frame**, not from a handpicked normalized pool.

Before writing normalized ecological prompts:

1. freeze a source window and cutoff;
2. freeze explicit inclusion-rule IDs and exclusion-rule IDs;
3. create a manifest containing every candidate maintainer event in that source window;
4. for each candidate record `source_event_id`, immutable source reference, source-event SHA-256, eligibility, and the applicable inclusion or exclusion rule;
5. commit the manifest hash and immutable reference.

The frame must yield at least 24 eligible source events. A later normalized pool is valid only when it contains **every eligible source event** from this frozen frame. This prevents selection bias from moving upstream into pool construction.

### 6.3 Neutral normalization and complete eligible pool

For every eligible frame event, create exactly one normalized pool item. It carries:

- `ecological_source_id` equal to the frozen `source_event_id`;
- original source reference and source-event SHA-256;
- `normalization_reference`;
- `normalized_from_source_only: true`;
- `task_family_id`;
- exact normalized prompt;
- `anchor_type` (`exact-owner`, `legitimate-new-artifact`, or `none`);
- declared scenario families.

Normalization may add only facts explicitly present in the source event/context that are necessary to make the task self-contained. It must not add expected owners, paths, validators, canonical terms, RI vocabulary, answer-key facts, or later repository findings.

`ecological_source_id`, `task_family_id`, and whitespace-normalized/case-folded prompt text must each be unique. The evaluator rejects any pool that omits an eligible frame event, adds an ineligible event, or changes the source reference/hash.

### 6.4 Seed-shopping control and replayable ecological sampling

Only after the complete eligible pool is frozen and hash-committed does an independent assessor generate exactly one ecological-selection seed and one arm-order seed per wave. Record immutable generation references and attest single generation. Commit seed hashes before primary execution and reveal the seeds only after primary evidence is frozen.

The evaluator can verify commitment/replay and declared provenance. It cannot prove an assessor privately generated an unreported alternative seed; that remains an externally auditable limitation.

Ecological selection algorithm:

1. rank exact-owner anchors by `SHA256(seed + NUL + "exact-owner" + NUL + ecological_source_id)` and choose the first two;
2. rank legitimate-new-artifact anchors similarly and choose the first two;
3. remove those four IDs, rank remaining eligible items by `SHA256(seed + NUL + "general" + NUL + ecological_source_id)`, and choose the first eight;
4. Pilot receives the first selected anchor of each type plus the first four general selections;
5. Confirmatory receives the second selected anchor of each type plus the remaining four general selections.

### 6.5 Replayable arm randomization and wave independence

For task ID `t`, compute `h = SHA256(seed + NUL + "arm-order" + NUL + t)`. If the integer value is even, order is Control→Treatment; otherwise Treatment→Control.

Prompt packs use schema version 3. Pilot and Confirmatory must have no overlap in `task_family_id`, ecological `ecological_source_id`, or whitespace-normalized/case-folded exact prompt text.

## 7. Frozen scoring key and blind scoring

Scoring keys use schema version 3 and every case freezes:

- accepted owner/route outcomes;
- acceptable alternatives;
- required authoritative evidence;
- serious-error conditions;
- decision-acceptance conditions;
- companion-validation applicability;
- concrete `0`/`1`/`2` anchors for every applicable dimension.

The judgment boundary must exist before any run.

Every primary run then records the exact `model_response`, its SHA-256, and an opaque `blind_response_id`. **Primary run records must not contain correctness scores.**

After all primary responses for scoring are frozen, prepare a separate blind scoring bundle:

- schema version 1;
- no arm labels and no tool/cost/Treatment metadata;
- opaque response ID, task ID, response SHA-256, and scores only;
- scorer identity and immutable scoring-evidence reference;
- Pilot and Confirmatory scoring-key hashes;
- `scoring_completed_before_arm_reveal: true`;
- `arm_labels_present: false`.

Freeze the blind scoring bundle hash before revealing arm mapping to the scorer. The evaluator maps blind scores back to the run only through the opaque ID, task ID, and exact response SHA-256, keeping the structured scoring packet separate from arm-labelled run evidence.

The bundle, each response entry, and each `scores` object must contain exactly the fields shown in [`ab_blind_scoring.example.json`](ab_blind_scoring.example.json), including explicit `companion_validation: null` when inapplicable. Unknown fields are rejected at every level; an `arm` blacklist alone would still permit tool events, costs, delivery status, or nested metadata to reveal the arm. Opaque identifiers and arm-hidden evidence references remain an assessor/process obligation; field validation cannot prove that allowed strings conceal no arm information or that the scorer saw no outside material.

## 8. Exact input identity per run

Every run records the exact held-out prompt text and SHA-256, the canonical run envelope and SHA-256, and the exact deterministic full message plus SHA-256.

The full message contains only experiment arm, study repository, study ref, wave, task ID, Treatment Delivery Mode, and exact task prompt. No extra hint, owner guess, explanation, or arm-specific prose may be appended.

## 9. Structured instrumentation and provenance

Every run contains a canonical `tool_events` list with contiguous sequence numbers, phase (`study_infrastructure` or `task_orientation`), tool family, operation, repository, ref when available, resource, `resource_class`, response bytes when measurable, and RI content identity where applicable.

Each run also records:

- `instrumentation_source` = `machine_capture` or `exported_transcript`;
- immutable `raw_evidence_reference`;
- `raw_evidence_sha256`;
- `event_extractor_version`;
- `event_log_sha256` over canonical JSON for `tool_events`.

The evaluator mechanically verifies the structured event-log digest and reconstructs connector calls, search calls, source-lock evidence, RI access, RI bytes, repository-response bytes, Control contamination, and Treatment completeness from that event list. Raw transcript/capture evidence is **separately hash-committed and auditable**; v10 does not claim that the local evaluator mechanically re-extracts `tool_events` from the raw transcript.

Primary connector-cost metrics count only `task_orientation` events. `branch_tip_pre`, `branch_tip_post`, smoke checks, and recorder bookkeeping are study infrastructure and excluded. Compact-surface acquisition is Treatment orientation cost and remains included.

## 10. Correctness and cost

Dimensions are Owner/routing correctness (0–2), Evidence sufficiency (0–2), Authority discipline (0–2), Companion/validation completeness (0–2) when applicable, and Decision quality (0–2).

Serious-error matrix labels are `A-serious/B-no-serious`, `A-no-serious/B-serious`, `both-serious`, and `neither-serious`.

An `A-serious/B-no-serious` pair is qualifying only when every applicable Treatment dimension meets the preregistered quality floor.

For each ecological pair define connector ratio `r_i = B_i/A_i` from task-orientation calls only; `0/0 -> 1.0`, `A=0, B>0 -> infinity`.

Context-volume efficiency uses exactly one preregistered metric: reconstructed repository-response UTF-8 bytes, exact client-exposed input tokens, or `unavailable`.

## 11. Protocol-owned acceptance floors

Study preregistration may make acceptance **stricter**, never weaker than protocol v10. The evaluator rejects a preregistration that weakens these floors:

- positive-reversal minimum each applicable dimension: `>=1`;
- ecological median correctness delta B−A per wave: `>=0` and zero ecological reverse serious-error reversals;
- correctness-route connector median B/A: `<=1.50`, high-overhead threshold `<=2.00`, at most 2 high-overhead ecological cases;
- connector-interaction signal median B/A: `<=0.80` in each wave;
- measured context-volume median B/A: `<=1.00`, high-overhead threshold `<=2.00`, at most 2 high-overhead ecological cases;
- correctness acceptance: at least 1 Confirmatory positive reversal, at least 1 Confirmatory ecological positive reversal, at least 3 qualifying positives combined, zero reverse serious-error reversals, ecological non-regression in both waves, connector cost gate in both waves, and all 24 pairs valid.

The correctness route is an **engineering acceptance criterion**, not a statistical-significance claim.

Possible outcomes remain `ENGINEERING ACCEPTANCE — CORRECTNESS + ORIENTATION EFFICIENCY`, `ENGINEERING ACCEPTANCE — CORRECTNESS`, `ENGINEERING ACCEPTANCE — ORIENTATION EFFICIENCY`, `ENGINEERING SIGNAL — CONNECTOR INTERACTION ONLY`, `CORRECTNESS SIGNAL / COST NOT ACCEPTED`, `NOT CONFIRMED`, `NO INCREMENTAL VALUE SHOWN`, `REGRESSION`, and `INCONCLUSIVE`.

When run-validity failures leave no valid ecological pairs in a wave, the evaluator still writes the report with `INCONCLUSIVE`, the individual invalidity reasons, null ecological medians, and failed cost/efficiency gates. A partial valid sample may retain descriptive medians, but cannot pass an acceptance gate. Missing or contradictory required evidence is a validation error, reported by the CLI with exit code 2 rather than an acceptance report.

## 12. Deterministic evaluator

`.github/scripts/score_repository_intelligence_ab.py` plus its small `_ri_ab_*` helper modules verify:

- preregistration, protocol-owned floors, and smoke eligibility;
- sampling-frame manifest and complete eligible pool;
- independent-after-pool randomization provenance and seed replay;
- prompt/key hashes, scenario coverage, ecological anchors, and cross-wave independence;
- strong scoring keys;
- exact per-run prompt/envelope/full-message and model-response identity;
- blind scoring-bundle identity and response mapping;
- model/client/isolation parity;
- event-derived source lock and event-log-derived cost/RI evidence;
- Control ablation;
- compact-surface-only Treatment boundary;
- exact Treatment-surface identity and complete byte coverage;
- paired correctness/cost/context metrics and final engineering classification.

Example invocation after primary evidence and blind scoring are frozen:

```bash
python3 .github/scripts/score_repository_intelligence_ab.py \
  --preregistration /secure/ab-preregistration.json \
  --run-record /secure/ab-run-record.json \
  --ecological-frame /secure/ecological-sampling-frame.json \
  --ecological-pool /secure/ecological-normalized-pool.json \
  --ecological-selection-seed "$ECO_SELECTION_SEED" \
  --pilot-arm-seed "$PILOT_ARM_SEED" \
  --confirmatory-arm-seed "$CONFIRM_ARM_SEED" \
  --pilot-prompts /secure/pilot-prompts.json \
  --pilot-key /secure/pilot-scoring-key.json \
  --confirmatory-prompts /secure/confirmatory-prompts.json \
  --confirmatory-key /secure/confirmatory-scoring-key.json \
  --blind-scores /secure/blind-scoring.json \
  --treatment-surface /secure/agent-context.json \
  --output /secure/ab-evaluation-report.json
```

## 13. Lifecycle

1. Merge this protocol/infrastructure PR after generated RI surface freshness, tests, companions, and checkpoint are green.
2. Select the exact study commit and establish the repository-mutation freeze.
3. Smoke-test the actual client and freeze smoke evidence.
4. Freeze the ecological sampling frame manifest, source window/cutoff, and inclusion/exclusion rules.
5. Normalize **all** eligible frame events and freeze the complete eligible pool.
6. Only then have the independent assessor generate exactly one ecological-selection seed and one arm-order seed per wave; freeze provenance and seed hashes.
7. Freeze both prompt packs and both strong scoring keys outside the tested Git tree.
8. Preregister model/client, exact compact Treatment identity, protocol-compatible stricter-or-equal thresholds, and decision rules.
9. Run Pilot A/B in replayed order and freeze outputs; do not change Confirmatory material.
10. Run Confirmatory A/B in replayed order and freeze all primary outputs.
11. Build the arm-hidden response bundle, complete blind scoring against frozen keys, and freeze its hash **before arm reveal**.
12. Reveal seeds/arm mapping and run the deterministic evaluator.
13. Optionally run data-only C or a separate flat-inventory-vs-relational diagnostic.
14. Publish a separate evidence/results PR with revealed evidence, evaluator output, limitations, and conclusion; merge it whether positive, null, regression, or inconclusive.
15. Release the repository-mutation freeze after primary evidence is safely frozen.

The protocol, templates, evaluator, and benchmark markers remain durable test infrastructure after the study.

## 14. What the experiment does not prove

A successful result supports only the tested connector compact-surface RI route for the tested repository state, model/client, and task distribution. It does not prove universal productivity gain, relational graph value, graph visualization value, Control Map value to agents, local CLI value, another adapter, or future-state equivalence.

If relational graph value matters after primary evidence, run a separate flat-owner/inventory versus relational-evidence decomposition diagnostic rather than inferring graph value from this A/B.
