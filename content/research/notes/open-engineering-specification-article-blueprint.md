---
title: "Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities"
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - control-loop
  - constraints
  - sdlc
  - repository-architecture
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/control-loop
  - ua/topic/constraints
  - ua/topic/sdlc
  - ua/topic/repository-architecture
created: 2026-07-31
updated: 2026-08-15
language: en
license: CC-BY-4.0
draft: true
---

# Article Blueprint — Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities

> **Status:** Living editorial design document for the article. This is a non-normative research note, not article prose and not a specification source. It preserves the complete argument, section responsibilities, claim boundaries, figures, transitions, source plan, writing notes, and unresolved editorial decisions. It must evolve after every drafting iteration and must not be compressed into a checklist merely because publication prose exists.

## 1. Editorial decision

The public article uses **Thinking Systems** as the engineering category through which the problem is developed. It does not begin by presenting Uncertainty Architecture as the premise that validates the argument.

The article first:

1. defines Thinking Systems;
2. distinguishes them from agentic applications;
3. explains why making a Consequential Runtime Responsibility depend partly on probabilistic Model Judgment changes the controlled object;
4. derives the control capabilities and lifecycle decision responsibilities that the paper argues must be made explicit, then organizes them using the current UA four-family × four-horizon model;
5. develops the four decision levels as an operating model with explicit triggers, inputs, decisions, capability obligations, outputs, evidence routes, escalation, and learning;
6. applies the complete map to concrete implementation carriers and contrasting authority scopes so proportionality becomes an operational sufficiency test rather than a repeated framework explanation;
7. challenges the derived operating map against systems/safety/runtime-assurance methods, control-theoretic research, orchestration, guardrail, observability, managed-platform, governance, standards, and regulation, including what those approaches already solve and what the derived map loses when translating them;
8. situates and delimits the paper-level synthesis in relation to the existing **Uncertainty Architecture** draft specification whose boundary is defined and indexed by `SPECIFICATION.md`, then closes with a falsifiable validation agenda for community review.

The connected argument is:

```text
engineering expands around consequential uncertainty it can no longer leave outside its operating model
→ Thinking Systems place probabilistic Model Judgment inside the controlled object
→ Thinking Systems are not synonymous with agentic applications
→ runtime Model Judgment resolves situations whose relevant interpretation or decision space cannot be exhaustively specified in advance; useful behavioral variance may be part of that capability but is not the objective itself
→ model quality and observability are necessary but insufficient
→ the paper derives four control-capability families
→ governance becomes operational through the active socio-technical control architecture, not through a post-hoc review or document
→ the paper derives lifecycle decision ownership through four connected decision horizons
→ each level must have explicit triggers, inputs, decision rights, evidence needs, downward outputs, and reassessment routes
→ if a material control responsibility remains unowned, unrealized, unevidenced, or without a credible corrective or reassessment path, the application is not ready for production at that intended scope
→ authoritative Constraints flow downward by reference while realization becomes concrete
→ runtime and delivery evidence returns to the decision level whose basis it invalidates
→ material evidence remains attributable to the active authorization and behavioral/control baseline well enough to reconstruct which source, decision, realization, model/configuration, evaluator, deployment, and fallback state actually governed the event
→ fallback, containment, and recovery are control claims to evidence rather than safety properties inferred from the existence of a secondary path
→ negative cases can feed structured learning back into Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and authorization
→ the complete map is inspected before implementation depth is reduced proportionally
→ material obligations are carried through the lightest credible composition of existing records and operating mechanisms, with new UA-specific surfaces added only where a material relationship would otherwise be lost
→ the ecosystem already contains many strong pieces and alternative framings of this control problem: systems/safety/runtime-assurance methods, orchestration runtimes, guardrails, evaluation and observability, managed AI platforms, governance suites, standards, regulation, and control-theoretic research
→ those approaches are compared against the derived map by controlled object, capability coverage, decision horizon, authority semantics, guarantee strength, evidence routing, reassessment, Human Authority, and viability-decision semantics—and reverse-mapped to identify what the derived map itself loses or distorts
→ semantic substitution is established when an existing method or composition preserves all material relationships with equivalent or stronger semantics under the same relevant scope and assumptions; where a relationship concerns economics, semantic equivalence preserves the viability-decision semantics rather than matching the actual cost burden; material control overhead then determines practical preference among semantically adequate operating compositions rather than whether the semantic integration gap exists
→ the tested paper-level synthesis is formally situated and delimited in relation to the existing open draft Uncertainty Architecture specification: SPECIFICATION.md defines and indexes that specification boundary, each indexed document contributes only according to its declared status and scope, and paper-only carrier, substitution, reverse-mapping, integration-gap, and validation claims remain research unless separately accepted through framework review and a corresponding status-bearing change
→ the paper ends with falsifiable programs specifying what practical evidence should simplify, split, demote, contradict, or refine
```

The article uses one unnumbered abstract and eight numbered sections.

Two models remain orthogonal throughout:

- **decision levels** identify where a decision is owned;
- **capability families** identify how boundaries, evidence, decisions, and actions become operational.

The article must not map the four levels one-to-one onto the four families, present either model as a mandatory physical stack, or turn the lifecycle into a one-way waterfall.

The four decision levels must be explained as an **operating model through time**, not merely as four static ownership descriptions. Each level must therefore answer a common set of questions:

```text
What activates this level?
→ What inputs and authoritative sources arrive here?
→ Which questions and decisions are owned here?
→ Which Constraints, Sensors, Controllers, and Actuators must exist or be required because of those decisions?
→ What outputs, boundaries, delegated authority, evidence obligations, and artifacts flow downward?
→ What evidence, exceptions, change requests, or invalidated assumptions flow upward?
→ Which decisions can be taken locally and which require reassessment or reauthorization?
→ How do negative cases improve the control architecture over time?
```

This common frame is an editorial rule for **Article §4**. It is not a claim that all four levels use identical processes, teams, cadence, documents, or automation.

**Full-map and proportionality rule.** The article intentionally presents the full decision-and-capability map needed to reason about a complex, high-consequence Thinking System. It must state explicitly that this does **not** mean every system requires every mechanism, role, artifact, approval path, Sensor, or Actuator shown in the complete map. Simpler, lower-consequence systems should use a proportionate subset justified by consequence, authority, exposure, reversibility, uncertainty, feedback latency, realization difficulty, Human Authority load, operating capacity, and control economics. The purpose of teaching the complete map is diagnostic: even when implementation is intentionally lightweight, teams should inspect the whole map first so they do not accidentally build a system with broad authority, slow feedback, hidden cross-level dependencies, or expensive control requirements while treating it as a simple LLM feature. Proportionality may simplify implementation; it must not hide complexity that is actually present.

**Artifact-neutral publication rule.** The repository contains concrete project and delivery reviews, canonical Constraint artifacts, templates, and illustrative reference material. These remain important UA implementation patterns, but this paper should not make one artifact set the proof, centerpiece, or mandatory operating surface of the conceptual map. In particular, the publication should not devote standalone sections to the two-living-review SMB pattern or the illustrative `K-SEND-01` lifecycle trace at the current evidence maturity. They may be linked as repository examples after the operating map is understood. The paper's durable contribution is the problem definition, capability anatomy, decision-horizon operating map, evidence/authority routing, proportionality logic, landscape mapping, and validation questions—not one form, checklist, worked support scenario, or product stack.

**Landscape and non-duplication rule.** The article already uses adjacent standards and research in earlier sections for specific local purposes. Preserve those roles instead of reintroducing the same source from zero later. In particular, **Article §2** may use ISO/IEC TR 29119-11 and NIST AI RMF to compare broad `AI-based system` / `AI system` labels with the narrower Thinking-System category boundary. That early comparison is about **category scope**, not a verdict on the adequacy of NIST, ISO, governance practice, or compliance. **Article §6** must perform the separate **functional landscape mapping**: what each approach actually contributes, where it fits across the capability families and decision horizons already derived in the paper, which authority or lifecycle semantics it carries, and what remains outside its normal scope. The later landscape section may refer back to the earlier NIST/ISO mention but must not repeat the category-definition discussion. ISO/IEC 42001 and the EU AI Act belong primarily in the later organizational/landscape analysis unless an earlier argument specifically needs them.

The opening may use **plan-driven development**, **iterative delivery**, and **modern operations** as a narrow explanatory lens, with **Waterfall**, **Agile and related approaches**, and **DevOps** named as familiar but non-equivalent examples. The broader engineering categories must remain primary in the prose, Figure 1, and the comparison table. The comparison must not claim that one methodology replaced another, reduce any movement to one purpose, or use the comparison as evidence of a universal historical law. Its role is to show how engineering expands when an important location of uncertainty can no longer remain outside the engineering model.

## 2. Two-document drafting model

This article is developed through two living documents with different responsibilities.

### 2.1 Editorial blueprint

This file is the design document for the article. It owns:

- the end-to-end argument;
- detailed section purpose and sequence;
- stable and provisional claims;
- required distinctions, examples, anti-examples, and counterarguments;
- figure contracts;
- transitions and closing claims;
- repository anchors and external-evidence expectations;
- exclusions, maturity boundaries, rejected formulations, and known risks;
- durable reasoning discovered during drafting.

The blueprint is not replaced by prose. Drafting should make it more precise. Detailed section content must not be replaced with one-line reminders after the section has been written.

Blueprint-owned working analyses needed to draft later sections—including the complete Article §5 material-relationship mapping—remain inside this living blueprint as working sections or appendices. Creating another living article-planning research note is not the default escape hatch; if a future analysis genuinely warrants an independent research artifact, that requires a separate explicit repository/editorial decision rather than silently expanding the two-document drafting model.

### 2.2 Target manuscript

The publication-facing manuscript lives at:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

It owns article prose, figures, examples, and the continuous reader experience. Internal drafting rules, contributor instructions, PR workflow, and editorial acceptance checklists do not belong in the article body.

### 2.3 Mandatory iteration loop

Every substantial drafting iteration follows this order:

```text
read the complete blueprint
→ select the next coherent section block
→ read the complete target manuscript
→ inspect terminology, claims, transitions, examples, and figures already established
→ design the new sections as a continuation of the existing argument
→ write and integrate prose, Mermaid diagrams, tables, and examples
→ reread the complete manuscript, not only the new diff
→ repair contradictions, repetition, weak transitions, title drift, figure numbering, and premature framework promotion
→ return to the blueprint
→ update its section design, writing notes, rejected formulations, figures, source needs, and unresolved risks
```

An iteration is incomplete until both documents are reconciled.

### 2.4 Cumulative argument rule

Every new section must be written from:

1. this complete blueprint;
2. every previously accepted article section;
3. terminology and distinctions already introduced;
4. the logical need created by the preceding section;
5. the repository sources that own the relevant meaning.

Later prose must extend the argument rather than restart the framework explanation. When drafting reveals a weakness in an earlier section, revise the earlier manuscript prose and then update this blueprint accordingly.

**Future-section ownership rule after Article §4.** **Article §§1–4** now own the category boundary, whole-system controlled object, capability anatomy, Hard/Soft semantics, substantive Human Authority, four decision horizons, invalidated-decision-basis routing, full-map-before-depth proportionality, operational governance framing, evidence-instrument validity, material active-baseline reconstructability, fallback/recovery credibility as an evidenced control property, and the proposed negative-case learning/stabilization discipline. Later sections must refer back and apply those results rather than re-derive them:

- **Article §5 owns application** — extracting material obligations, selecting and testing implementation carriers, comparing proportionate authority scopes, and closing only material gaps.
- **Article §6 owns functional landscape and substitution** — testing the derived map against adjacent methods, standards, platforms, tools, and organizational compositions, including reverse mapping.
- **Article §7 owns identity and boundary delimitation** — the existing UA specification boundary, the paper's separate synthesis claim, provenance, repository relationship, maturity boundary, and what neither surface is.
- **Article §8 owns falsification** — the evidence programs that could revise, split, simplify, demote, substitute, or reject parts of the map.

Do not re-define Thinking System, the controlled object, the four capability families, the four horizons, Hard/Soft, Human Authority, or reassessment routing in **Article §§5–8** unless a real contradiction discovered during drafting requires an earlier manuscript revision.

### 2.5 Diagram rule

Every major argument and every decision level should have an architectural or process representation when a diagram adds information.

Diagrams are part of the reasoning, not decoration. They must:

- make the controlled object, boundary, evidence, authority, action, or reassessment path clearer;
- introduce no doctrine absent from owning repository sources;
- state non-prescriptive boundaries in captions;
- avoid implying mandatory products, services, teams, departments, committees, roles, or execution pipelines;
- remain consistent with all earlier figures;
- be reviewed and renumbered as one visual system after every iteration.

**Figure 3 — Controlled-object shift** and **Figure 9 — Two orthogonal models** are established as the primary architectural anchors. A third UA boundary/composition representation is planned only if it adds a relationship not already carried by Figure 9; a compact table may replace it. Supporting figures are not capped, but every new visual must materially strengthen the deduction rather than satisfy a count.

Visual emphasis may be used when it carries architectural meaning. In particular, a distinct red treatment may identify where a Consequential Runtime Responsibility depends partly on probabilistic Model Judgment inside the controlled object, but it must not imply that the entire Thinking System is probabilistic or unsafe.

### 2.6 Running-example contract — bounded customer-support resolution

The manuscript should use one **canonical running educational trace** to make the abstract model concrete across **Article §§1–8**. The canonical trace is the bounded action-capable customer-support resolution system established through **Article §4**. **Article §5** may add only the explicitly marked counterfactual sibling defined below. Both are pedagogical devices, not repository reference architectures, empirical case studies, or validation evidence for UA.

The canonical trace must remain stable enough that the reader can recognize the **same action-capable controlled object** as it moves from business proposal through organizational authorization, Project / Architecture viability, Delivery realization, Runtime operation, and reassessment. Do not replace it with unrelated examples at each level. The **Article §5** sibling starts from the same business proposal but is a different candidate Project design and scope whose reachable authority and effects differ. Its category must be retested; for this defined sibling, that retest remains positive. Do not presuppose Project Authorization or collapse that project alternative into a Delivery realization. Short counterexamples from other domains may be used to prevent overfitting, but they must remain secondary.

**Variant-branch rule after Article §4.** **Article §4** establishes the canonical action-capable trace: the support system may communicate directly and execute refunds up to the illustrative delegated threshold, with Human Authority above it and three distinct reassessment routes. **Article §5** may branch back to a draft-only/human-execution alternative from the same business proposal to test proportionality. In that defined sibling, the human has real authority and executes the consequential response, but the decision remains materially informed by and dependent on the model's draft or recommendation; the category retest therefore still identifies a Thinking System. Treat the branch as a counterfactual candidate Project / Architecture design and scope with different reachable authority and effects—not as a later chronological state, not as another Delivery realization inside the canonical Project Authorization, and not as a replacement for the canonical trace. **Article §6** returns to the canonical action-capable case for composition/substitution analysis. **Article §§7–8** use only brief callbacks unless new case detail is necessary.

**Progressive-disclosure rule.** Introduce the canonical running trace explicitly in **Article §1** as a named pedagogical spine and define the business goal and whole controlled object there, but reveal implementation detail only when the corresponding concept is introduced. For **Article §§1–4**, prefer the sequence `generic model → application to the canonical trace → optional secondary counterexample or transfer check`. **Article §5** instead uses `generic carrier logic → explicit comparison with the counterfactual sibling`; **Article §6** returns to the canonical trace. Do not let a new domain example silently replace the support-resolution system as the primary explanatory object.

**Running-example visual contract.** Primary returns in **Article §§1–5** should be visibly separated from generic exposition using portable Markdown rather than platform-specific callout syntax. Use a horizontal rule, a `### Running Example | <lens-specific title>` heading, a bold `Lens in this section:` line, the case material itself, a short bold `What this adds to the case:` progression statement, and a closing horizontal rule. Keep tables, diagrams, lists, and prose inside the callout as ordinary Markdown so the structure survives GitHub, static-site, and publication export. The title after the pipe and the lens must change with the section; the business context and system identity must remain recognizable. **Article §6** may use one compact composition table instead of retelling the scenario; **Article §7** should use only a brief continuity callback; **Article §8** should explicitly end the fictional example's evidentiary role and ask for independent cases. This visual contract is editorial, not UA doctrine.

#### Section-by-section running-example progression

The canonical running example is a **cumulative architectural trace**, not a recurring anecdote. **Article §§1–4** should expose one additional property of the same action-capable support-resolution system; **Article §5**'s explicitly marked sibling is a comparative alternative, not another chronological stage; **Article §6** returns to the canonical case. Keep every use visibly separated from generic exposition with a consistent `Running Example` heading or equivalent callout.

- **Article §1** — establish the business goal, whole controlled object, Model-Judgment-dependent Consequential Runtime Responsibilities, and the fact that control/evidence/authority paths are intentionally unresolved.
- **Article §2** — show that a fixed workflow can already be a Thinking System; then make the engineering consequence explicit: once Model Judgment participates in consequential responsibility, the control perimeter follows the whole object and may become a socio-technical architecture crossing technical, delivery, architectural, human-authority, and organizational decision boundaries. Show only the **reach of the perimeter**, without introducing the canonical horizon sequence, horizon ownership, detailed responsibilities, or reassessment semantics. Reserve the canonical four-horizon model and its names as an operating structure for **Article §4**.
- **Article §3** — take one stable refund-authority boundary and expose the four capability families as parallel control functions around that boundary: Constraint + Constraint Realization, Sensors, Controller / decision functions operating within delegated authority, and Actuators. Do not treat the Controller as creating its own authority: define it as a decision function that may select or authorize action only within delegated authority, and where substantive judgment is reserved, show Human Authority or another authorized decision process as the holder of that authority or escalation destination. Show why a policy sentence is not yet a complete control path without implying an execution pipeline.
- **Article §4** — establish the standing decision basis and illustrative owner at each of the four horizons, then apply one concrete runtime event and vary what fails. Show that one event does not automatically traverse all horizons: local response and escalation follow the **invalidated decision basis**, not the component or team where the signal first appeared. Preserve enough correlated baseline identity to diagnose which authorization, realization, model/configuration, evaluator, deployment, or fallback state was active for material evidence; treat fallback independence, capacity, and restoration as properties to evidence rather than assumptions.
- **Article §4 figure sequence** — first show the four decision-ownership horizons as a standalone model, including downward inheritance and direct reassessment from realization or operation evidence to the horizon whose decision basis is invalidated. Do not imply that reassessment originates only at Runtime. Only then combine that model with the **Article §3** capability anatomy to produce the orthogonal horizons × capability-families map. Preserve the pedagogical order: capability model → decision-ownership model → combined model.
- **Article §5** — branch from the same business proposal to compare a draft-only/human-execution Project alternative with the canonical bounded autonomous-refund scope. Hold lifecycle maturity constant when attributing differences to authority/scope: compare both variants at the same Project / Architecture candidate point before Delivery approval, then discuss later realization maturity separately. Show the material-obligation delta, test whether existing carriers preserve each relationship, and demonstrate why implementation depth differs. Do not present the lower-authority branch as a chronological upgrade/downgrade or claim that human mediation automatically makes the control problem lightweight.
- **Article §6** — return to the canonical action-capable case and use it as one compact substitution/composition test for existing methods, tooling, integrated stacks, and organizational practice. Ask which parts of the support-system control relationship they already preserve and which relationships, if any, remain residual. Treat law, binding contracts, and adopted policy as pure authority/obligation inputs rather than substitutes by themselves; keep adopted and operated risk/management methods, including standards-based management systems, eligible for the same composition/substitution test as other methods.
- **Article §7** — use only a brief callback showing how the paper-level synthesis relates to the existing open draft Uncertainty Architecture specification. `SPECIFICATION.md` defines and indexes the specification boundary; each indexed document contributes only within its declared status and scope. Do not turn paper-only hypotheses into a new architectural layer or implicit specification expansion. The example remains evidence of explanatory continuity, not validation evidence.
- **Article §8** — state explicitly that the constructed support case cannot validate the map. Convert its remaining questions into prompts for independent applications: can another team find an otherwise-missed responsibility, remove unnecessary control, route evidence correctly, reconstruct the active baseline after a material event, demonstrate credible fallback under realistic/common-mode failure, or show that an existing stack already preserves the material relationships without additional UA artifacts?

The canonical trace should accumulate detail rather than restart. Later sections may refer back to earlier disclosed facts (`€50` delegated refund authority, Human Authority above the threshold, approved identity/data paths, the realized transaction guard, evidence and escalation routes) instead of re-explaining the business context. The **Article §5** sibling must retain its own lower-authority facts and must not silently overwrite the canonical trace.

#### Business context

Use a fictional company that wants to reduce the cost and latency of customer-support resolution. The proposed system may:

- interpret a customer's support request;
- retrieve authorized account, order, product, and support-policy context;
- classify the issue and select an applicable resolution path;
- synthesize or draft consequential customer communication;
- recommend a credit, refund, replacement, escalation, or another bounded remedy;
- for explicitly authorized low-impact cases, invoke a tool/API that changes downstream business state;
- route cases requiring reserved judgment or authority to Human Authority.

The example should be realistic enough to contain meaningful authority, side effects, Human Authority, evidence, and economics, but deliberately avoid domain-specific complexity such as medical diagnosis, criminal justice, or regulated lending that would allow regulation to dominate the engineering argument.

#### Controlled object and category test

Treat the controlled object as the **whole support-resolution system**, not the model invocation:

> A support-resolution system that interprets customer requests and determines or executes bounded remediation using authorized customer/account context, company policy, deterministic software, and probabilistic Model Judgment.

Representative Consequential Runtime Responsibilities include:

- interpreting the customer's actual support intent;
- deciding which support policy or resolution path applies;
- selecting or recommending a consequential remedy;
- communicating information that materially affects the customer outcome;
- deciding whether a transaction may be proposed or routed for execution;
- in the more autonomous variant, initiating a bounded refund/credit or another downstream action.

The example should demonstrate that a **fixed workflow can still be a Thinking System**. The workflow may be predefined and deterministic while one or more Consequential Runtime Responsibilities inside it depend partly on Model Judgment. Dynamic routing, multiple agents, memory, planning, or high autonomy are not required for the category.

#### Initial organizational authority context

Use a small set of plausible organizational sources and decision owners. They are illustrative responsibilities, not mandatory UA departments or roles.

Possible organizational boundaries:

- customer/account data may be accessed only through approved identity, data, and deployment paths;
- some customer or contractual case classes must always remain under Human Authority;
- organizational policy may permit a project to delegate bounded low-value refund or credit authority, while higher-value transactions remain reserved to Human Authority;
- billing-plan changes, account closure, or other higher-authority operations remain outside the automated support scope;
- consequential customer communication and transaction decisions must remain traceable enough for the owning decision process;
- material privacy/security boundary violations, abnormal financial behavior, repeated complaints, and shared-capability degradation must produce evidence usable by the relevant organizational owners.

Use **Finance**, **Support/Product**, **Security/Privacy**, and equivalent functions only when they make decision ownership concrete. Do not imply that every company needs those exact departments. In an SMB, the same person may hold several responsibility bundles.

A key organizational lesson to preserve is:

```text
legitimate organizational authority
→ downstream Constraint / assumption
→ realization requirement
→ Sensor / evidence obligation
→ Controller / decision owner
→ available Actuator / escalation / reauthorization path
```

For example, if the organization reserves higher-value refunds to Human Authority, that decision must eventually become a realizable transaction boundary and an evidence path—not merely a RACI entry saying that Finance is consulted.

#### Project / Architecture alternatives and AI-necessity test

At Project / Architecture, compare at least three plausible designs before presuming that the broadest Thinking-System design is justified:

```text
A. deterministic rules / decision tree for supported case classes
B. model-assisted interpretation or recommendation with human execution
C. bounded Thinking System that can resolve and execute selected low-impact cases autonomously
```

The Project / Architecture discussion should ask:

- where Model Judgment adds value that deterministic/manual alternatives do not;
- which Consequential Runtime Responsibilities actually need Model Judgment;
- what authority and downstream consequences become reachable in each variant;
- what Human Authority remains necessary;
- what control perimeter each variant creates;
- whether the business case still works after model/platform cost **and** the complete control-perimeter cost are included.

Do not predetermine that variant C wins. A legitimate project result may be variant A, variant B, narrower variant C, bounded research, redesign, defer, or No-Go.

#### Representative Judgment Nodes

Candidate Judgment Nodes may include:

- interpreting ambiguous customer intent;
- mapping a case to policy meaning when policy application is semantic rather than purely syntactic;
- ranking candidate remedies;
- deciding whether a case fits a low-impact autonomous-resolution class;
- generating consequential customer communication.

Do not require all of these Judgment Nodes. Use only those needed by the prose and keep deterministic responsibilities visible before, between, and after them.

#### Representative Hard / Soft distinction

Use a deliberately concrete pair because this example should make the realized-path distinction intuitive.

**Illustrative Soft claim:**

> Approved boundary: customer communication and refund recommendations must remain consistent with the applicable support policy. The current semantic realization can provide only a Soft guarantee for that semantic property.

The business intent may be categorical while the realized guarantee remains Soft. A prompt, policy instruction, classifier, or LLM-as-judge may influence or estimate compliance with the boundary, but does not make an inappropriate semantic outcome unreachable.

**Illustrative Hard claim for one action path:**

> An automated refund transaction above an illustrative threshold (for example, €50) must not reach the payment API unless a deterministic gateway verifies an approval credential issued through the designated approval path for an authenticated authorized human identity and the matching transaction scope.

A credible Hard realization might therefore require a deterministic transaction gateway that checks amount, authenticated execution identity, approval credential, transaction scope, and relevant bypass paths before the payment action is reachable. **This Hard claim establishes deterministic transaction gating; it does not by itself prove that the Human Authority process is substantively effective.** Information quality, competence, capacity, latency, fallback, and real power to change the outcome remain separate Project / Runtime obligations.

The **€50 value is purely illustrative**. It is not a UA recommendation, universal risk threshold, or proposed business policy. The article may change the number or describe it as `T` if that avoids accidental normative interpretation.

Use this example to show that:

- the authoritative business decision is the Constraint;
- the transaction/identity/approval path is the Constraint Realization;
- denied attempts, approvals, transaction outcomes, bypass/health evidence, and version/configuration state are Sensors/evidence;
- deterministic or human decision logic can perform Controller functions within delegated authority;
- execute, reject, route for approval, narrow, disable, compensate, or roll back can be Actuator functions;
- a product marketed as a “guardrail” could implement several of these functions without becoming the authoritative source of the business boundary.

Do not claim a Hard semantic guarantee such as “the system will never recommend an inappropriate refund” merely because the transaction amount is hard-limited.

#### Human Authority in the example

Human Authority must be substantive, not a decorative approval box. The example should expose:

- who has the legitimate decision right for the reserved case;
- what evidence/context the reviewer receives;
- required expertise;
- expected approval volume;
- acceptable decision latency;
- what happens when the reviewer is unavailable or overloaded;
- whether the reviewer can actually change the outcome;
- fallback behavior;
- the lifecycle cost of maintaining that path.

This is also the bridge to control economics: a technically safe design may still be economically non-viable if too much traffic is routed to expensive or slow Human Authority.

#### Representative Delivery realizations

Delivery may realize the authorized design through combinations of:

- scoped IAM and service identities;
- typed tool interfaces;
- transaction guards and amount/authority checks;
- model/prompt/context/retrieval configuration;
- deterministic schema and state validation;
- Human Authority approval workflow;
- evaluator and telemetry pipelines;
- denied-action logging;
- correlated source/project/delivery/configuration/version records sufficient to reconstruct the active behavioral and control baseline for material evidence;
- fallback and compensation paths whose relevant dependency independence, capacity, transition behavior, and restorability can be evidenced rather than presumed;
- rollback, disable, or exposure-narrowing mechanisms;
- release-specific checks and evidence.

Use these as examples of **realizations**, not as a mandatory product stack. The manuscript should be able to substitute equivalent existing platform capabilities without changing the conceptual map.

#### Representative Runtime evidence

Potential runtime evidence includes:

- customer outcomes and complaints;
- resolution categories and downstream transaction outcomes;
- attempted and blocked high-value refunds;
- Human Authority requests, approvals, rejects, queue size, overload, and latency;
- fallback volume, availability, saturation, dependency/common-mode failure evidence, transition success, and restoration result;
- evaluator outputs, active evaluator/version identity, calibration or validation basis where applicable, and evaluator health/validity state;
- authorization or identity failures;
- realization bypass/degradation signals;
- correlated authoritative-source / Project / Delivery / realization / model / prompt-instruction / context-retrieval / tool-routing / evaluator-policy / deployment-scope / fallback identity sufficient to reconstruct the material active baseline;
- cost and latency by resolution path;
- Actuator execution and post-action verification.

The example should repeatedly reinforce that **evidence is useful only relative to a decision path**. A dashboard showing these metrics is not by itself a Controller.

#### Three canonical reassessment cases

Preserve at least three distinct runtime/change cases so the article can demonstrate routing by **invalidated decision basis** rather than routing everything to one governance layer.

**Case A — Delivery reassessment: realization/configuration defect.**

A legacy transaction endpoint or deployment configuration causes the refund-limit realization to be unavailable, degraded, or potentially bypassable for one path.

```text
Runtime Sensor evidence
→ affected path narrowed/disabled inside delegated authority
→ Delivery reassessment
→ realization/configuration repaired
→ complete path retested
→ evidence verifies that the intended Hard boundary is restored
→ bounded re-release
```

The point: the Project Authorization may remain valid if the architecture and assumptions are still sound and Delivery can restore the released realization to its previously authorized operating state.

**Case B — Project Reauthorization: viability/economics assumption invalidated.**

Suppose the project assumed that only a small percentage of cases would require Human Authority. Production evidence instead shows, for example, that 30–40% of cases require approval, approval latency is hours rather than minutes, fallback load rises, and cost per resolved case approaches or exceeds the human-only process.

```text
Runtime evidence
→ Project Reauthorization
→ reassess Model Judgment placement, autonomous scope, Human Authority capacity, fallback, latency, and control economics
→ narrow / redesign / return to model-assisted mode / research / defer / No-Go
```

The point: the system may be respecting every Hard Constraint and still become non-viable. This is not automatically a Delivery bug and not something Runtime can solve by silently widening authority.

**Case C — Organizational review: authoritative basis changes.**

An external contractual, legal, customer, or organizational policy change requires a particular customer segment or case class to receive explicit Human Authority regardless of transaction amount.

```text
external / organizational evidence
→ Organizational review
→ authoritative boundary / reserved decision updated
→ Project Reauthorization if the existing design is affected
→ Delivery updates the realization and evidence path
→ Runtime operates against the new authorized baseline
```

The point: this evidence did not originate as a model failure. Organization changes the authoritative context; lower levels make the new decision operable.

These three cases should remain mutually distinguishable throughout the manuscript. Do not collapse them into one generic “incident escalation” story.

#### Proportionality variant

Use the same business context to show why implementation depth is based on authority/consequence rather than feature size.

**Lower-authority variant:** the model drafts a suggested response or remedy for a human support agent; it cannot execute refunds, change account state, or communicate directly. The agent is adequately informed and empowered to reject or replace the suggestion and personally decides and executes the consequential response, but that decision remains materially informed by and dependent on Model Judgment. State the category test and its positive result: this defined sibling remains a Thinking System even though the human path reduces reachable system authority. Inspect its full map before reducing explicit runtime Actuators, deterministic transaction boundaries, or organizational evidence obligations; they may be lighter **only where the human path genuinely reduces reachable authority, consequence, irreversibility, or automation dependence**. A different process in which no Consequential Runtime Responsibility remains materially dependent on Model Judgment would fall outside the category, but that is not the sibling used for this comparison. Rubber-stamping, poor information, overload, or lack of intervention power would also fail to establish substantive Human Authority.

**Higher-authority variant:** the system can communicate directly with customers and execute bounded refunds/credits. The same visible UI may now require stronger identity/transaction realizations, richer Sensors, substantive Human Authority, fallback, incident paths, more explicit decision rights, and a larger control perimeter.

**Comparison-control rule:** when the article attributes a difference to authority/scope, compare both variants at the **same lifecycle maturity point**. The authority delta is evaluated at Project / Architecture candidate design before Delivery approval, using proposed required operating-contract properties for both alternatives. The canonical system's later active Delivery-approved Requirement, Operating Envelope, realizations, runtime carriers, and release evidence may be recalled separately as a **lifecycle-maturity callback**, but those artifacts are not evidence that broader authority alone caused the difference. If the lower-authority candidate were authorized and delivered, it too would acquire delivery/runtime carriers appropriate to its scope.

The lesson is not that the higher-authority version is “bad.” It is that **one model call or one feature is not a reliable proxy for control complexity**.

#### Landscape use of the same example

**Article §6** should map adjacent approaches onto this **same support-resolution system** rather than presenting only abstract vendor categories.

Illustrative mapping questions:

- an orchestration runtime may carry state, tool calls, durable execution, routing, and Human Authority workflow;
- a guardrail product may realize checks, Sensors, local Controller logic, or Actuators around input/output/tool boundaries;
- an evaluation/observability system may provide traces, online/offline evaluators, alerts, version comparison, and evidence;
- a managed AI platform may implement identity, deployment, tool permissions, guardrails, tracing, evaluation, and delegated workflow mechanics;
- an enterprise governance platform may carry use-case records, authoritative references, approvals, evidence, risk/control mappings, and lifecycle state;
- applicable regulation and binding obligations provide authoritative source obligations; Organization identifies applicable authoritative sources and legitimately adopts internal or voluntary sources where appropriate, Project interprets them into scoped project Constraints, authorization conditions, required operating-contract properties, authority, and evidence obligations, and Delivery translates that inherited baseline into an approved Requirement and Operating Envelope for the bounded scope. NIST/ISO and other voluntary frameworks may structure risk-management or evidence obligations and become authoritative only through explicit adoption, contractual incorporation, certification/procurement commitment, policy, or another legitimate authority decision.

Then ask what remains: who authorizes the refund boundary, whether Model Judgment is justified, whether the `Hard` claim is actually deterministic across the complete path, which evidence invalidates which decision, whether Human Authority capacity is viable, and whether the resulting control perimeter makes economic sense.

Do not hard-code named products into the example's architecture. Product names belong to the landscape analysis and must be reverified against current first-party documentation at drafting/publication time.

#### Chapter-by-chapter usage contract

Use the running example differently in each article section; do not retell the full scenario eight times.

**Article §1 — Engineering Evolves Around Dominant Uncertainty**

- Introduce only the business motivation and credible initial team state: model/tooling, traces/evaluations, policy, Human Authority, pilot.
- Define the whole support-resolution system as the running controlled object, but deliberately leave the evidence, decision, and corrective paths unresolved so later sections derive them rather than assume them.
- Use the support-resolution proposal to ask the unanswered cross-boundary questions: why Model Judgment, what authority, what evidence, who can act, and whether control cost preserves the business case.
- Do not introduce the full refund Constraint or four-horizon machinery yet.

**Article §2 — The Controlled Object Has Changed**

- Classify the support-resolution system as a Thinking System when consequential interpretation/resolution depends partly on Model Judgment, even if orchestration is fixed.
- Show the whole mixed deterministic/probabilistic controlled object rather than reducing the example to the LLM call.
- Use the example to separate category membership from autonomy and control adequacy.

**Article §3 — From Model Quality to Bounded Control**

- Introduce the illustrative refund boundary to distinguish authoritative Constraint from realization and Hard from Soft.
- Map Sensor, Controller, and Actuator functions on the same case.
- Use Human Authority to show why an approval UI alone is not a complete control path.

**Article §4 — Four Decision Levels**

- Make this the main narrative spine of the example.
- Organization establishes admissibility, reserved authority, shared-capability/evidence obligations.
- Project / Architecture compares deterministic/manual/model-assisted/autonomous alternatives, places Judgment, designs the complete control architecture, and tests economics.
- Delivery realizes the bounded design and release evidence, including enough correlated baseline identity to reconstruct material releases/incidents and evidence that fallback/recovery paths are credible under the failures they are intended to contain.
- Runtime operates the loop, generates evidence, verifies corrective outcomes, and treats fallback/common-mode failure and inability to restore an authorized state as control evidence rather than as an automatic safe state.
- Use Cases A, B, and C to demonstrate Delivery reassessment, Project Reauthorization, and Organizational review respectively.

**Article §5 — Applying the Map Without Overbuilding**

- Treat the draft-only/human-execution design as a counterfactual Project / Architecture alternative from the same business proposal, not as the next chronological state of the canonical action-capable trace.
- Compare it with the canonical direct-communication and bounded-refund scope through material obligations, credible carriers, reachable authority, Human Authority, evidence, Actuators, reassessment, and economics.
- Hold lifecycle maturity constant for the authority/scope comparison: use proposed required operating-contract properties for both candidate Project designs before Delivery approval. Discuss the canonical system's later active Delivery/Runtime realization only as a separate maturity callback.
- State that **Article §4** inspected the canonical action-capable case. **Article §5** category-retests the defined sibling, records that its human decision still materially depends on the model recommendation and therefore remains a Thinking System, inspects its own full map, and then demonstrates how implementation depth and carrier composition differ.
- Do not turn the example into a recommendation that every support system needs the full illustrated control stack.

**Article §6 — Existing Landscape**

- Return to the canonical action-capable controlled object as the anchoring composition test for what orchestration, guardrails, observability, managed platforms, governance suites, standards, and regulation can contribute.
- Import the same versioned complete material-relationship map produced in **Article §5**; do not let a publication excerpt define the substitution universe.
- Use one compact table or worked mapping rather than retelling the complete scenario.
- Separate the semantic substitution verdict from practical preference: relationship-level semantic equivalence under the same relevant scope and assumptions, applied across every material relationship, decides whether a semantic integration gap remains; economic/viability relationships compare decision semantics rather than numerical burden, and material control overhead is compared only after semantic adequacy to choose among concrete operating compositions.
- Do not distort current tools to make the example favor the derived map.

**Article §7 — Situating and Delimiting the Research Synthesis Relative to Uncertainty Architecture**

- Use only a brief callback to show how the example connects relationships already carried within the specification boundary defined and indexed by `SPECIFICATION.md` with the paper-only carrier, substitution, and validation synthesis, while keeping the boundary explicit.
- Do not present the support example as proof that UA works; the contribution is the synthesis and its explicit boundary, not the anecdote.

**Article §8 — Validation Agenda**

- Explicitly state that the support-resolution case is editorially constructed and therefore cannot validate the framework.
- Ask external reviewers to apply the map independently in other domains and identify where the support example overfits the proposed distinctions.
- Welcome examples where existing tools/processes make parts of the illustrated mapping unnecessary.

#### Anti-overfitting and claim-safety rules

The manuscript must not:

- present the running example as empirical validation, a customer case study, or evidence that UA improves outcomes;
- imply that customer support is the canonical domain for UA;
- turn Finance, Support, Security, Privacy, or any illustrative participant into a mandatory UA role or department;
- present the illustrative refund threshold as a recommended, safe, legal, or generally applicable amount;
- make every Constraint financial, transactional, or tool-based merely because the example uses a refund path;
- imply that all Hard Constraints are transaction limits or all Soft Constraints are model-output quality policies;
- infer that successful blocking of one transaction path proves the whole system is controlled;
- reuse `K-SEND-01` as if the running example were evidence from a validated repository implementation; the running example and repository reference artifacts have different purposes;
- change UA definitions, capability-family boundaries, decision-horizon ownership, or Hard/Soft semantics merely to make the example narratively convenient;
- assume that repeated negative cases always route upward; route according to the invalidated decision basis;
- assume the system should maximize autonomous resolution. The correct Project decision may be narrower Model Judgment, model-assisted human work, deterministic redesign, or No-Go;
- treat a fallback as safe merely because it exists or ignore common dependencies, capacity, transition failure, and restorability where those properties are material;
- let product/vendor capabilities become permanent facts in the example; current platform claims belong to **Article §6** source verification.

When the example does not fit a general claim cleanly, **change or qualify the example rather than changing the doctrine to fit the story**.

#### Running-example acceptance checks

Every manuscript iteration that touches **Article §§1–8** should verify:

- [ ] The canonical action-capable controlled object and business context remain recognizable across the article; the **Article §5** lower-authority sibling is explicitly marked as a different candidate Project design and scope, not a second Delivery realization, and does not overwrite the canonical trace.
- [ ] The example is explicitly fictional/editorial and not presented as validation evidence.
- [ ] Consequential Runtime Responsibilities and Judgment Nodes remain consistent with the Thinking-System definition.
- [ ] Organization does not absorb the Project-owned AI-necessity/viability decision.
- [ ] The illustrative Hard refund boundary remains a **scoped complete-path transaction-gating claim**, not a semantic guarantee about all model behavior and not proof that the Human Authority process is substantively effective.
- [ ] The illustrative threshold is clearly non-normative.
- [ ] Human Authority includes authority, information, capacity, latency, fallback, and power to change the outcome.
- [ ] Delivery realizations remain examples rather than a mandatory stack.
- [ ] Runtime evidence is tied to decision consumers rather than presented as telemetry for its own sake.
- [ ] Material release/runtime evidence can be correlated to the active source/authorization/delivery/realization/model-config/evaluator/deployment/fallback baseline without requiring one universal registry.
- [ ] Fallback/recovery is not treated as inherently safe: relevant dependency independence/common-mode coupling, capacity/latency, transition behavior, and restorability are evidenced where material.
- [ ] Case A routes to Delivery because realization/configuration is invalidated.
- [ ] Case B routes to Project Reauthorization because capacity/economics/architecture assumptions are invalidated.
- [ ] Case C routes to Organization because the authoritative basis changes.
- [ ] Proportionality compares both authority variants at the same Project / Architecture candidate maturity point, isolates **scope/authority delta** from later **lifecycle-maturity delta**, and does not attribute Delivery/Runtime artifacts to authority alone.
- [ ] Landscape discussion returns to the canonical action-capable case and uses it to clarify substitution and residual responsibility, not to manufacture vendor weaknesses.
- [ ] **Article §§7–8** do not restart the case narrative or treat it as validation evidence.
- [ ] No example-specific role, threshold, artifact, or implementation mechanism is promoted into UA doctrine.
- [ ] Counterexamples from other domains are used where necessary to demonstrate that a claim is general rather than support-specific.

## 3. Stable thesis and claim boundary

### Stable thesis paragraph

Thinking Systems are software systems in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance. The category names the changed engineering object; it does not certify that the object is adequately controlled. Because useful runtime judgment places consequential uncertainty inside that object, evaluation, observability, policies, human approval, and agent orchestration remain insufficient as system control when disconnected from approved boundaries, concrete realizations, decision authority, corrective action, and reassessment. For production use, the socio-technical control architecture around the application must be engineered with it rather than added as a governance layer after implementation: governance becomes operational through that architecture, and the application is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path. The article derives this engineering model first, maps adjacent approaches against it, and situates its research synthesis alongside the existing open draft, tool-neutral Uncertainty Architecture specification whose boundary is defined and indexed by `SPECIFICATION.md`; each indexed document contributes only within its declared status and scope. The paper's additional carrier, substitution, reverse-mapping, integration-gap, and validation claims remain subject to practical testing and do not alter the specification without explicit framework review and a corresponding status-bearing change.

### Thinking Systems definition

Use the canonical glossary definition:

> A software system in which one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment rather than being fully specified through explicitly encoded logic in advance.

Use **Consequential Runtime Responsibility** as an implementation-neutral classification term: a runtime responsibility is consequential when its output, decision, path, action, or downstream state can materially affect an intended outcome, satisfaction of an applicable Requirement or Constraint, the exercise of delegated authority, resource use, or a person or system downstream. State explicitly that **consequential describes material causal relevance, not implementation mechanism or risk severity**. A Consequential Runtime Responsibility may be fulfilled entirely through explicitly encoded logic or may depend partly on probabilistic Model Judgment; Thinking-System classification changes only in the latter case. Harm, severity, likelihood, reversibility, residual exposure, autonomy, regulation, control strength, and release decisions remain separate. A model invocation with no material influence on any Consequential Runtime Responsibility is not sufficient by itself to establish Thinking-System classification.

Preserve the following category boundary:

- fixed, linear, iterative, adaptive, or dynamically selected orchestration does not determine whether software is Linear Software or a Thinking System;
- a fixed or explicitly orchestrated sequence is a Thinking System when one or more **Consequential Runtime Responsibilities** depend partly on probabilistic Model Judgment;
- category membership and control adequacy are separate: missing Constraints, evidence, decision rights, or corrective mechanisms may make a Thinking System inadequately controlled or not production-ready without changing its category;
- the category may begin in a first simple model-enabled iteration and does not require agents, dynamic routing, multiple models, or high autonomy;
- deterministic code before, between, or after Judgment Nodes does not make delegated Model Judgment deterministic;
- autonomy and delegated authority are additional dimensions separate from both Model Judgment and orchestration topology;
- systems described as agentic may use fixed or dynamic orchestration, while an agent label alone neither establishes nor excludes Thinking-System classification;
- the precise boundary of agentic terminology remains an open research topic and must not be presented as settled doctrine;
- a non-agentic feature may be a Thinking System when probabilistic judgment materially affects interpretation, routing, decisions, outputs, or downstream action;
- a Thinking System remains a mixed deterministic and probabilistic system.

### Defensible public claim

The paper proposes a coherent engineering model for reasoning about and operating Thinking Systems from organizational authority and project viability through delivery release and runtime reassessment, examines that model through structured carrier, substitution, and reverse-mapping analysis against the adjacent tool/framework landscape, and situates the research synthesis alongside the open draft Uncertainty Architecture specification whose boundary is defined and indexed by `SPECIFICATION.md`. Paper-only claims do not enlarge that specification without explicit framework review and a corresponding status-bearing change.

### Claims the article must not make

The article must not describe UA as:

- an accepted industry standard;
- a complete scientific theory;
- independently validated across multiple teams or domains;
- a universal governance or compliance framework;
- a replacement for Agile, DevOps, QA, security, change management, incident response, legal review, organizational policy, agent frameworks, guardrails, observability, evaluation tooling, governance platforms, or standards;
- a mandatory four-service AI Control Plane;
- a universal risk score, maturity ladder, threshold method, role model, or artifact package;
- a finished product or SDK;
- supported by a complete repository-level project-to-runtime worked application that does not yet exist.

The article must not present the early engineering deduction as proof that UA is uniquely correct. `SPECIFICATION.md` defines and indexes the existing open draft specification boundary; each indexed document contributes only according to its declared status and scope. The paper's broader carrier, substitution, reverse-mapping, integration-gap, and validation synthesis remains research alongside it, not evidence for the specification's own claims or an implicit expansion of its scope. The landscape comparison must not be written as a superiority chart. Its purpose is to locate responsibilities and substitution boundaries, including cases where an existing platform, standard, or internal process already carries part of the map better than a new UA-specific artifact would.

## 4. Audience, tone, and reader promise

### Primary readers

- software and enterprise architects placing Model Judgment inside production systems;
- engineering, delivery, product, and project leaders deciding whether an AI path is viable beyond a prototype;
- AI platform and agent-framework builders implementing control capabilities;
- security, risk, legal, compliance, and governance practitioners connecting authoritative sources to technical operation;
- practitioners and researchers able to test the specification through application evidence.

### Tone

- architectural rather than promotional;
- direct and skeptical of hype without dismissing adjacent disciplines or products;
- precise about evidence, authority, failure, and maturity;
- practical for SMB teams without assuming enterprise governance structure;
- open to contradiction and revision.

### Reader promise

The reader should leave able to explain:

1. what a Thinking System is and why the category is not equivalent to agentic software;
2. why making a Consequential Runtime Responsibility depend partly on probabilistic Model Judgment changes the controlled object;
3. the difference between measurement, a closed feedback loop, and bounded acceptable operation;
4. why governance for a Thinking System becomes operational through an active socio-technical control architecture rather than through a post-hoc review or document;
5. why a Thinking System intended for production use is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path;
6. the four capability families and their boundaries;
7. the four decision levels and the question owned by each;
8. what activates each decision level, what arrives there, what it decides, what it sends downward, what evidence returns upward, and when reassessment is required;
9. how authoritative boundaries become scoped Constraints and realization/evidence obligations while invalidating evidence routes back to the decision owner;
10. why Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization are different decisions;
11. how control economics affects the decision to use Model Judgment at all, not only the choice of model;
12. how negative cases may be used to improve Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and authorization rather than becoming isolated incident closure;
13. why a Controller is a decision function that may combine legitimate human authority with automation rather than being synonymous with either a team or an algorithm;
14. why the complete map is a diagnostic reference rather than a requirement to instantiate every element for every system, and how proportionality is applied without hiding real complexity;
15. how to extract material obligations from the already inspected map, test existing implementation carriers, and build the lightest credible many-to-many composition without assuming one mandatory UA document set;
16. how systems/safety/runtime-assurance methods, control-theoretic research, orchestration runtimes, guardrails, evaluation/observability tools, managed AI platforms, governance suites, standards, regulation, and ordinary organizational practice contribute to or substitute for the same decision-and-capability relationships;
17. what those approaches genuinely provide, which responsibilities may remain outside their normal scope, and what the derived reference model itself loses or distorts when the mapping is reversed;
18. how to separate **semantic substitution** from **practical preference**: an existing method or stack semantically substitutes when, for the same relevant scope and assumptions, it preserves every material semantic property required by each material relationship—source/authority, scope/assumptions, guarantee semantics where applicable, evidence and consumer, decision right, effective action and verification, lifecycle/change control, reassessment, and the semantics of any material viability/economic decision—even if it uses different vocabulary or structure. For economic relationships, that means preserving who decides viability, which input categories matter, which decisions are available, and what triggers reassessment; it does not mean matching the actual cost, latency, staffing, or operational burden. Material control overhead then determines which semantically adequate operating composition is practically preferable; conceptual overhead remains a separate explanatory-economy question;
19. that `SPECIFICATION.md` defines and indexes the current draft Uncertainty Architecture specification boundary, each indexed document acts only within its declared status/scope, which additions remain paper-level research hypotheses, and what evidence should simplify, split, demote, substitute, or reject those hypotheses.

## 5. Article structure

### Unnumbered abstract

**Purpose:** Introduce Thinking Systems, establish the controlled-object shift, and summarize the production-release condition without narrating the article's internal reveal sequence.

**Required content:**

- software engineering expands when important uncertainty can no longer remain outside its operating model;
- use **plan-driven development**, **iterative delivery**, and **modern operations** as the primary categories, with **Waterfall**, **Agile and related approaches**, and **DevOps** named as familiar examples;
- the canonical Thinking Systems definition;
- explicit distinction from agentic software;
- a Consequential Runtime Responsibility depends partly on probabilistic Model Judgment inside the controlled object;
- model quality and observability are insufficient when disconnected from boundaries, authority, corrective action, and reassessment;
- for production use of a Thinking System, the application is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path, even if model and code tests pass locally;
- governance becomes operational through the socio-technical control architecture spanning organizational, project / architecture, delivery, and runtime decision levels, not through a post-hoc review, compliance document, or approval ceremony;
- the paper derives a control-capability and decision-horizon model for reasoning about the architecture, explains proportional application, maps the adjacent ecosystem against the resulting structure through substitution analysis, situates that research synthesis in relation to the existing open draft Uncertainty Architecture specification whose boundary is defined and indexed by `SPECIFICATION.md`, and preserves an explicit validation agenda without implying that paper-only claims already belong to the specification.

**Exclude:** internal manuscript-draft status and workflow metadata, drafting rules, repository workflow, statements narrating when the paper will reveal UA such as “Only after the problem...”, the complete taxonomy, detailed repository templates, `K-SEND-01`, long vendor catalogs, market statistics, and promotional calls to action. This exclusion does not permit omitting the specification's declared draft maturity from reader-facing claims.

**Word budget:** 240–330

---

### Article §1 — Engineering Evolves Around Dominant Uncertainty

**Purpose:** Establish the path to Thinking Systems, define the category, distinguish it from agentic software, expose the missing engineering connection, and make the production-release condition explicit.

**Core claim:** **Plan-driven development**, **iterative delivery**, and **modern operations** can be read as cumulative responses to requirement, product-learning, and production-condition uncertainty, with Waterfall, Agile and related approaches, and DevOps serving as familiar but non-equivalent examples. Thinking Systems add runtime-judgment uncertainty when Consequential Runtime Responsibilities depend partly on probabilistic Model Judgment inside the controlled object. Existing policies, evaluations, traces, approval steps, and orchestration tools do not become a governable or production-release-ready system unless connected to authorization, bounded authority, decision ownership, corrective action, and reassessment.

**Required content:**

- Explain the methodology comparison narrowly and cumulatively rather than as replacement history.
- Keep the broader engineering responses primary and name Waterfall, Agile and related approaches, and DevOps in parentheses or explanatory prose as familiar examples.
- Do not describe iterative approaches as derivatives of Agile or imply historical equivalence among Waterfall, Agile, and DevOps.
- Show how feedback moves closer to runtime as uncertainty becomes harder to contain before implementation.
- Preserve why plan-driven engineering, including Waterfall, remains rational where uncertainty can be reduced sufficiently in advance and late change is expensive.
- Preserve why iterative delivery, including Agile and related approaches, does not abandon planning; it shortens the cycle between assumption, delivery, use, and revision.
- Preserve why modern operations, commonly associated with DevOps, extends engineering into runtime because production combinations cannot be reproduced exhaustively before release.
- State explicitly that Thinking Systems retain earlier uncertainty classes while adding consequential uncertainty produced through runtime Model Judgment.
- Keep this transition framework-neutral in the publication prose: state the engineering problem directly—how to build and operate systems once consequential behavior is partly produced through probabilistic Model Judgment—without using Uncertainty Architecture as the premise that validates the deduction. The publication title may retain the framework name for attribution and discoverability.
- Introduce the canonical Thinking Systems definition in publication-facing prose and give the operational meaning of **consequential** used by the category test.
- Define Model Judgment through interpretation, synthesis, classification, generation, planning, ranking, routing, or action selection under uncertainty.
- Explain that the category describes responsibility structure, not product marketing. Keep the full justification for why a distinct name is needed, and the comparison with broader AI-system labels, in **Article §2** after the controlled-object shift is introduced.
- Show a simple classification boundary: ask whether any **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment. Route **No** to Linear Software and **Yes** to Thinking System. Show orchestration topology, autonomy, and delegated authority as independent dimensions that affect architecture, risk, and control demand but do not decide category membership.
- State that autonomy and probabilistic judgment are separate dimensions.
- Introduce the bounded customer-support-resolution running example at intentionally low detail: a team seeking lower resolution cost and latency has a capable model, retrieval and tool access, traces, evaluations, policy guidance, a human-review path, and a pilot that interprets requests and proposes resolutions. Make clear that the same controlled object will return as the argument develops, without presenting it as validation evidence or a reference architecture.
- Define the whole support-resolution controlled object at this stage, but leave the required evidence, decision, authority, and corrective paths explicitly unresolved so **Article §§2–4** derive them rather than smuggle the solution into the premise. **Article §1** may name problem domains such as authorization, architectural viability, realization, operation, and reassessment, but it must not yet present `Organization`, `Project / Architecture`, `Delivery`, and `Runtime` as the canonical decision-horizon model.
- Ask the connected questions those components do not answer:
  - Was Model Judgment necessary?
  - What authority was delegated?
  - Which consequences are prohibited or unacceptable?
  - Which Constraints are authoritative?
  - How are they realized?
  - Which evidence informs which decision?
  - Who may narrow, roll back, disable, redesign, or stop operation?
  - When does runtime evidence invalidate Project Authorization?
  - Does the business case survive the complete control cost?
- State fragmentation as practitioner observation unless current authoritative evidence supports a broader market claim.
- Explain that observability may describe behavior without authority to act; evaluation may estimate quality without defining an approved boundary; policy may express intent without realization; nominal human approval may lack information, time, power, or capacity; and orchestration may execute a workflow without authorizing it.
- Preserve the anti-substitution argument: evaluation score is not release authorization; prompt is not policy; policy is not a realized control; a human-in-the-loop label is not substantive Human Authority; a rollback button is not evidence that recovery is credible.
- State explicitly that these gaps are not governance debt that can be closed after release: for production use of a Thinking System, the application is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path. Define **complete control architecture** here as materially complete for the authorized scope, not maximal control implementation. Do not introduce the four-horizon × four-capability terminology in this callout before those models are explained later.
- Present this release-readiness consequence as a visually distinct publication-facing callout so the reader can identify it as a central engineering thesis without repeating the argument elsewhere.
- State that governance becomes operational through the socio-technical control architecture rather than through a policy document or post-release review. Preserve boundedness, evidence, corrective action, and reassessment as the substance of that claim without implying a mandatory physical stack.
- Support factual claims about current industry practice with current primary or authoritative sources. When evidence is unavailable, label the point as practitioner observation.
- Do not claim that no governance, safety, systems, or control practice exists.

**Accepted drafting decisions from the 2026-08-12 Abstract / Article §1 iteration:**

- Keep **Article §1** publication prose UA-neutral until the engineering problem and category have been derived; avoid formulations such as `UA expects` or `UA is designed to address` as premises.
- Introduce the customer-support running example explicitly as the article's named pedagogical spine, define the whole controlled object, and leave evidence/decision/corrective paths unresolved until the corresponding engineering argument derives them.
- Defer thresholds, Hard/Soft mechanics, explicit horizon routing, and detailed control-loop implementation to later sections.
- Use the material-control-responsibility release-readiness criterion here, but defer canonical decision-horizon labels and explicit `four horizons × four capability families` language until those models have been introduced. **Article §1** may foreshadow the underlying problem domains without presenting them as the operating model.
- In the Abstract, distinguish the existing open-specification UA boundary from the paper's proposed research synthesis and its falsifiable maturity boundary rather than narrating when the framework name appears in the paper or implying that paper-only claims already belong to the specification.

**Supporting figures:**

1. engineering responses around dominant uncertainty, with nodes labeled **Plan-driven engineering (Waterfall)**, **Iterative delivery (Agile and related approaches)**, **Modern operations (DevOps)**, and **Thinking-System engineering**; keep the Figure 1 caption framework-neutral and describe the final transition as the engineering problem created when consequential behavior is partly produced through probabilistic Model Judgment;
2. classification boundary showing the single category question—whether any **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment—while orchestration topology, autonomy, and delegated authority remain visibly independent dimensions.

**Supporting table:** Location of uncertainty, primary engineering mechanism, and where decisive feedback appears. The first column must use the broader categories first: plan-driven development (including Waterfall), iterative delivery (including Agile and related approaches), modern operations (commonly associated with DevOps), and **Thinking-System engineering**. Keep the table framework-neutral at this stage. It must state that earlier uncertainty classes persist and describe the Thinking-System engineering response as bounded control architecture rather than using Uncertainty Architecture as the category definition or explanatory premise.

**Repository anchors:**

- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)
- [`Designing Non-Deterministic Systems source intake`](designing-nondeterministic-systems-source-intake.md)

**Transition:** The missing connection exists because the system is often treated as conventional software with an additional AI component rather than as a changed controlled object.

**Closing claims:**

> Previous engineering methods learned to manage uncertainty surrounding software. Thinking Systems require engineering to manage consequential uncertainty produced by the software itself.

> The missing layer is not another AI component. It is the engineering connection between delegated judgment, authorized boundaries, evidence, decision authority, corrective action, and reassessment.

> A Thinking System intended for production use is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path.

**Working word budget:** 1,800–2,250  <!-- reconciled against current Article §1 (~2,016 words) -->

---

### Article §2 — The Controlled Object Has Changed

**Purpose:** Explain why probabilistic Model Judgment changes the controlled object and why consequential responsibility can require an expanded socio-technical control perimeter around that object, without yet allocating that perimeter to the canonical decision horizons.

**Core claim:** A Thinking System produces part of its consequential uncertainty inside the engineered object because runtime behavior depends partly on probabilistic Model Judgment. Once that happens, the engineering perimeter must follow the authority, evidence, effects, realizations, and corrective paths of the **whole controlled object** rather than stop at the model invocation or runtime component.

**Required content:**

- Begin **Article §2** by defining the **controlled object** as the thing whose behavior engineering seeks to keep within acceptable conditions. For this paper's category, state that it is not only source code or a model invocation but the whole software Thinking System within its declared boundary: deployed components, data, configuration, dependencies, infrastructure, and software-operated processes and interfaces. State separately that the behavior being controlled must be assessed through the downstream effects the system can produce; those effects do not become additional software components. Relevant human roles and interactions may belong to the socio-technical control perimeter around that object; they do not become part of the controlled process merely because they observe, authorize, or change it. A software component may implement a control function while remaining physically inside the system boundary, but the controlled-process and control-function relationships remain conceptually distinct.
- Treat the article-level exclusions already established in the Abstract and **Article §1**—**Thinking System** is not a maturity stage, architecture style, or synonym for an agentic system—as inherited framing rather than mandatory verbatim repetition. In this section, explain the need for a distinct name through the controlled-object boundary and state explicitly that **Thinking System** is not a replacement for the broader term **AI system**.
- Explain why the broader category is insufficient for this paper: ISO/IEC TR 29119-11 defines an AI-based system by the presence of at least one AI component, while this paper's narrower boundary asks whether a **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment.
- Include a compact publication-facing comparison that keeps neighboring labels distinct rather than joining them as synonyms: at minimum separate ISO/IEC **AI-based system**, NIST **AI system**, **LLM application**, **agentic system**, and **autonomous system**. Present the table as an analytical comparison, not universal definitions of those neighboring labels.
- State explicitly that this early ISO/NIST comparison has one narrow purpose: **category boundary**. It must not imply that NIST AI RMF, ISO standards, or broader AI-system concepts are technically shallow, operationally incomplete, or competitors that **Article §2** is evaluating. Reserve capability/authority/lifecycle comparison of NIST, ISO/IEC 42001, regulation, governance platforms, and tooling for **Article §6**.
- State explicitly that application topology does not determine the category: a single model call, a predefined workflow, dynamic routing, or agentic orchestration can all host a Thinking System, but neither the presence of a probabilistic model nor any of these topologies is sufficient by itself. The category begins only when at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment.
- Use the same bounded customer-support-resolution system to demonstrate predefined stages and permitted transitions such as receive request → retrieve authorized context → interpret issue → select or recommend resolution → prepare consequential communication → check authority → execute a bounded action or route to Human Authority. Keep that concrete sequence inside the dedicated **Running Example** block rather than generic prose. The point is that fixed orchestration topology neither creates nor prevents the category; the system crosses the boundary when a **Consequential Runtime Responsibility** within that workflow depends partly on Model Judgment.
- Explain that later tools, memory, dynamic routing, multiple models, cooperating agents, or greater autonomy increase complexity and control demand but do not create the category.
- Explain why the object needs a distinct name using the canonical category boundary: in Linear Software, no **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment; its **Consequential Runtime Responsibilities**, if any, are fulfilled entirely through explicitly encoded logic. In a Thinking System, part of a consequential responsibility depends on runtime Model Judgment. Do not imply perfect physical repeatability or exhaustive specification of every system behavior.
- State explicitly that the **whole Thinking System—not the model invocation—is the controlled object**. Keep this as a framework-neutral deduction; do not use UA as the premise that validates the boundary.
- Keep the controlled process conceptually distinct from the control architecture around it: the engineering perimeter connects the consequential path to people, permissions, evidence, decision authority, and corrective mechanisms; do not redefine those control functions as part of the controlled object merely because they operate around it.
- Keep category identity separate from control adequacy: Constraints, evidence, decision authority, corrective mechanisms, and cross-level control architecture determine governability and production readiness rather than whether the object belongs to the category.
- Use determinism as a design-contract distinction over the relevant input, context, configuration, and state, not as a claim of perfect physical repeatability:

  ```text
  y = f(x, context, configuration, system state)
  ```

- Compare like with like: describe model-mediated responsibility over the same classes of relevant conditions as selection from plausible outcomes:

  ```text
  y ~ P(y | x, context, configuration, system state)
  ```

- Explain Model Judgment through interpretation, classification, ranking, planning, generation, routing, or action selection.
- Explain Input Interpretation, Decision Logic, and Output Mediation without presenting them as a mandatory pipeline.
- State that the reason to introduce Model Judgment is its ability to resolve consequential situations whose relevant interpretation or decision space cannot be exhaustively specified in advance. Useful behavioral variance may be part of that capability, but variance is not itself the engineering objective; bounded useful judgment is.
- Distinguish product and requirement uncertainty, environment and operational uncertainty, and runtime-judgment uncertainty.
- Preserve the mixed-system claim: deterministic responsibilities may remain before, between, and after Judgment Nodes.
- Explain why model quality alone cannot define prohibited states, allocate residual-risk authority, restrict reachable actions, execute correction, or determine Project Reauthorization.
- Explain why the changed object creates connected control questions that can cross technical, delivery, architectural, human-authority, and organizational decision boundaries. Show the **reach of the control perimeter** without introducing the canonical `Organization → Project / Architecture → Delivery → Runtime` sequence, horizon ownership, or detailed reassessment routing; those belong to **Article §4**.
- Make explicit that where authority, exposure, reversibility, or downstream effects make the control problem material, a Thinking System may require a socio-technical control architecture designed around the **whole controlled object**, rather than treating governance as an attachment to the model, application, or runtime architecture. Preserve proportionality: this is a perimeter claim, not a requirement for separate departments, committees, or a maximal stack.
- Introduce the recurring control questions:

  ```text
  What outcome or condition is intended?
  → What operating space is acceptable?
  → What uncertainty or disturbance can move the object outside it?
  → What evidence reveals behavior, outcome, conditions, and control state?
  → Who or what may decide that action is required?
  → Which mechanism can change operation?
  → When does new evidence require reassessment at this or an earlier level?
  ```

- State explicitly that these recurring questions expose the control structure that reappears across the expanded perimeter; they do **not** yet allocate those questions to canonical decision horizons.
- Explain that the transfer from control theory is structural, not a claim that organizations, projects, delivery teams, and runtime services are equivalent to one mathematical Controller or reducible to one scalar error signal.
- State that existing disciplines remain necessary and are connected rather than replaced.

**Primary architectural anchor — Figure 3: Controlled-object shift**

Use two vertical top-to-bottom responsibility diagrams placed side by side. The comparison must read as two parallel columns, not as two horizontal execution pipelines and not as one mandatory topology. Because disconnected Mermaid subgraphs may otherwise stack vertically, use an invisible alignment link between the columns to force the side-by-side GitHub rendering.

```text
Left — Primarily explicitly authored consequential behavior
situation and operating conditions
→ explicitly authored consequential decision mechanisms
→ consequential output, action, or downstream state

Right — Thinking System — changed responsibility structure
situation and operating conditions
├→ explicitly authored responsibilities before, between, and after Judgment Nodes
└→ one or more Judgment Nodes using probabilistic Model Judgment
   both responsibility paths converge on
→ consequential output, action, or downstream state
```

The two right-hand paths are schematic responsibility relationships, not a prescribed execution topology. The figure is **descriptive of the category boundary**, not a target control architecture. Use restrained red treatment only on the Judgment Node or Judgment Nodes where probabilistic Model Judgment changes the responsibility structure. Keep explicitly authored responsibilities, external/input conditions, outputs, and the Thinking-System boundary neutral. Do not preload deterministic validation, authority, evidence, correction, Constraints, Sensors, Controllers, or Actuators into this figure merely because those mechanisms are required later for controlled production use; **Article §§3–4** derive those responsibilities.

The caption must state that the figure is **descriptive of the controlled-object change, not a prescribed control architecture** and explicitly defer deterministic boundaries, evidence, authority, and corrective mechanisms for controlled production use to the sections that follow.

The figure must not imply that:

- traditional software has no uncertainty;
- a Thinking System is wholly probabilistic;
- every system has one Judgment Node;
- Judgment placement follows one fixed order;
- the right-hand structure is a prescribed production architecture;
- every realization acts before a model call;
- capability families form a vertical execution sequence;
- red denotes an error state rather than the structural addition being explained.

**Supporting figures:**

- functional placement of Model Judgment, with **Model Judgment** above and **Input Interpretation**, **Decision Logic**, and **Output Mediation** aligned horizontally beneath it;
- connected locations of **product / requirement uncertainty**, **environment / operational uncertainty**, and **runtime-judgment uncertainty**.

The Model Judgment placement figure is a taxonomy, not a sequence. It must not connect the three placement categories laterally in a way that implies a mandatory pipeline. The canonical four-horizon decision-ownership figure belongs to **Article §4**, not **Article §2**.

**Repository anchors:**

- [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
- [`Glossary`](../../../00-doctrine/glossary.md)
- [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)

**Transition:** Once consequential uncertainty is produced inside execution, measurement is necessary but no longer the complete engineering contract.

**Closing claim:**

> The problem is not merely that AI is harder to test. Part of the controlled object's behavior is now produced through runtime judgment, and every decision that controls that object must account for the change.

**Accepted drafting decisions from the 2026-08-12 Article §2 iteration:**

- Keep **Article §2** framework-neutral while deriving the changed controlled object; use UA later as the specification that organizes the resulting model rather than as the premise that validates the category.
- In the neighboring-label comparison, use `Thinking System (this paper)` and a controlled-object-boundary comparison rather than `UA boundary` language. Keep the ISO/NIST use narrow and non-competitive here.
- Treat the deterministic and model-mediated equations as design-contract abstractions, not claims of perfect repeatability or complete probabilistic specification.
- Define Linear Software using the canonical responsibility boundary: no Consequential Runtime Responsibility depends partly on probabilistic Model Judgment; consequential responsibilities, if any, are fulfilled entirely through explicitly encoded logic.
- Use the customer-support running example to show the mixed deterministic / Model-Judgment structure, but defer refund thresholds, Hard/Soft realization details, and full control-loop mechanics to later sections.
- Use the same support-resolution system, rather than a separate project-planning scenario, to demonstrate inside the dedicated **Running Example** block that the workflow may remain predefined while the category boundary still depends only on whether a **Consequential Runtime Responsibility** depends partly on Model Judgment.
- Keep Figure 3 descriptive of the category boundary rather than a UA target architecture: highlight the Judgment Node structural change only and defer validation, authority, evidence, and corrective mechanisms to the bounded-control deduction.
- Frame Model Judgment around situations whose relevant interpretation or decision space cannot be exhaustively specified in advance; useful variance may be part of that capability but is not the objective itself.
- Keep **Article §2** focused on the **reach of the expanded socio-technical control perimeter**. It may foreshadow technical, delivery, architectural, human-authority, and organizational decision boundaries, but it must not teach the canonical horizon sequence or ownership model before **Article §4**.
- Reserve the standalone decision-horizon figure, downward inheritance, invalidated-decision-basis routing, and explicit `Organization → Project / Architecture → Delivery → Runtime` ownership semantics for **Article §4**.

**Working word budget:** 2,050–2,550  <!-- reconciled against current Article §2 (~2,350 words) -->

---

### Article §3 — From Model Quality to Bounded Control

**Purpose:** Introduce the current status-bearing draft-normative Control-Loop Capability Anatomy, distinguish measurement, feedback closure, and bounded acceptable operation, and explain how governance becomes operational through the complete socio-technical control architecture.

**Core claim:** A measured system is not necessarily controlled, a closed feedback loop is not necessarily operating inside an approved boundary, and a Thinking System intended for production use is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path. In this paper, **complete control architecture** means materially complete for the authorized scope, not maximal implementation of every possible control mechanism or every cell in the later operating map.

**Required content:**

- Use the canonical feedback path:

  ```text
  Thinking System
  → Sensors and evidence
  → Controller and decision authority
  → Actuators and corrective action
  → changed Thinking System operation
  ```

- Explain why a loop may remain closed while unsafe, over-authorized, too slow, operationally fragile, or economically unacceptable.
- Introduce the four logical capability families in the publication-facing pedagogical order **Actuators → Constraints and realizations → Sensors → Controllers**. State explicitly that this is a reading traversal of the closed control loop, not a mandatory execution order or physical stack:
  1. **Actuators and corrective action** execute authorized changes to operation or a Constraint Realization.
  2. **Constraints and their realizations** define and operationalize approved boundaries around those changes and the operating space.
  3. **Sensors and evidence** observe behavior, outcomes, conditions, realization state, Actuator execution, and control health. Material evidence instruments must also have an identifiable active version, a validation/calibration basis where applicable, known coverage/uncertainty/latency/blind spots, and conditions under which model, population, policy, or operating-condition change can invalidate their use for a decision.
  4. **Controllers and decision authority** compare or interpret evidence relative to approved Requirements, Constraints, and assumptions, then select or authorize the next action.
- Close the four-family explanation by making the loop explicit: Controller authorizes Actuator; Actuator changes operation or realization; Constraints bound legitimate change; Sensors expose resulting state and effects; evidence returns to Controller.
- Preserve the functional distinctions:
  - Constraint is the authoritative boundary object.
  - Constraint Realization implements, enforces, or influences it.
  - Constraint Realization is not a fifth family.
  - Controller decides or authorizes; Actuator executes.
  - evaluator and metrics normally perform Sensor functions;
  - logic selecting `block`, `canary`, or `release` performs a Controller function;
  - deployment, blocking, exposure change, or rollback performs an Actuator function.
- Explain scoped Hard and Soft claims:
  - a Hard Constraint's complete realized path deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundaries;
  - where an organizationally or project-level prohibited state can feasibly be made unreachable through deterministic enforcement, prefer deterministic realization over probabilistic influence;
  - when deterministic prevention is not feasible, do not label the boundary Hard merely because the intent is important; record the remaining uncertainty and evidence obligations explicitly;
  - prompts, natural-language policies, probabilistic evaluators, and model preferences are not hard by themselves;
  - different guarantee strengths require separate Constraint records.
- Use short anti-examples: telemetry without authority is observation; a Controller without an effective Actuator cannot correct; a declared policy without realization is not an operable boundary; nominal human review is not substantive Human Authority.
- Define **Controller** as a decision function rather than as a team, person, dashboard, or algorithm. A Controller may be human, automated, or socio-technical: legitimate decision authority may be combined with automated evidence collection, invariant checks, routing, decision support, and bounded automated decisions where delegation permits them. The proportion of automation may vary, but automation does not create authority that was never delegated. State explicitly that the Controller selects or authorizes a bounded response, while the Actuator executes the authorized change.
- State that automation should remove repetitive sensing, checking, routing, evidence aggregation, and safe bounded response **where evidence quality, failure behavior, reversibility, consequence, and delegated authority make the automated path credible**. Automation is itself part of the control architecture: its decisions, failures, latency, configuration, and Actuator effects must remain observable and correctable. Do not present “maximum automation” as an independent goal.
- State explicitly that AI governance is not a fifth capability family, a post-hoc checkpoint, or a document layered over the implementation.
- Explain that governance becomes operational through the complete socio-technical control architecture formed by the capability families across the expanded control perimeter. Defer the canonical decision-level labels, sequence, and ownership model to **Article §4**.
- State the release-readiness condition: until credible boundaries, evidence, authority, effective Actuators, Human Authority and fallback where needed, and reassessment paths exist, the application may be demonstrable or testable but is not ready for production release at the intended scope.
- Avoid UA-first formulations such as “UA asks” in this section; the capability anatomy must follow from the problem itself.

**Figures:**

- supporting figure — closed feedback loop;
- supporting figure — complete bounded control architecture showing the four capability families as logical functions, not services, layers, or one execution order. The figure may show the true relationship topology even though the prose introduces the families in Actuator-first pedagogical order.

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
- [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
- [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
- [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

**Transition:** Capability functions explain what bounded control requires, but not where project, release, runtime, and organizational decisions are owned or how those decision horizons interact through time.

**Closing claims:**

> A closed loop can still be unacceptable when it operates outside an approved, credibly realized, observable, and correctable boundary.

> Capability without legitimate decision ownership is not a complete control architecture.

> Governance becomes operational through the active socio-technical control architecture; a Thinking System is not ready for production at the intended scope while any material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path.

**Accepted drafting decisions from the 2026-08-12 Article §3 rewrite:**

- Preserve the deduction sequence `measurement → closed feedback → bounded control`; do not present evaluation or observability as control by themselves.
- Reuse the bounded customer-support system as the primary explanatory object and introduce the refund-above-delegated-authority boundary here as the first concrete Constraint example.
- Use that same boundary to distinguish authoritative Constraint from Constraint Realization, Hard from Soft guarantee strength, Sensor evidence from Controller decision authority, and Controller authorization from Actuator execution.
- Prefer deterministic realization where a prohibited consequential state can feasibly be made unreachable; when prevention remains probabilistic, keep the residual uncertainty explicit rather than overstating the guarantee.
- Treat Human Authority as an architectural capability with information, time, competence, capacity, independence, and power requirements rather than as an approval UI.
- Make automation conditional on evidence quality, failure behavior, reversibility, consequence, and delegated authority; automated control remains part of the controlled architecture and must itself be observable and correctable.
- Keep the four-family order Actuators → Constraints and realizations → Sensors → Controllers as a pedagogical traversal only; Figure 7 expresses the actual relationship topology without implying one execution sequence.
- Close by separating the two models explicitly: capability anatomy explains how bounded control becomes operational; **Article §4** explains where the relevant decisions are owned.

**Working word budget:** 1,650–2,050  <!-- reconciled against current Article §3 (~1,850 words) -->

---

### Article §4 — Four Decision Levels for Thinking Systems — the operating map

**Purpose:** Present the connected organizational, project / architecture, delivery, and runtime horizons as the conceptual and operational center of the paper. The section must explain not only where decisions are owned, but how each level becomes active, what enters it, what it decides, which control capabilities its decisions require, what it sends downward, what evidence returns upward, and how negative cases trigger reassessment and learning.

**Core claim:** Different control decisions require different evidence, authority, time horizons, automation, and corrective actions. Together, the four levels describe how one Thinking System is authorized, made viable, realized, released, operated, corrected, and reauthorized. They are not four documents or four meetings; they are connected decision horizons in one socio-technical control system.

#### Common operating-frame rule for all four levels

Each level subsection must use the same publication-facing logic while preserving level-specific meaning:

1. **Activation triggers** — what event, proposal, evidence, or change causes this level to act.
2. **Inputs and authoritative basis** — what information, Constraints, assumptions, dependencies, prior decisions, and evidence arrive here.
3. **Questions and decisions owned** — what this level may legitimately decide and what it may not decide.
4. **Capability obligations** — what Constraints, Sensors, Controllers, Actuators, Human Authority, fallback, and automation must exist or be required because of the decisions owned here.
5. **Outputs and artifacts** — what authorization, boundaries, delegated decision rights, evidence obligations, realization requirements, records, and versioned artifacts flow downward or become active.
6. **Evidence and change received** — what lower-level evidence, incidents, changed assumptions, capacity or economic findings, and authority-expansion requests return here.
7. **Local action versus escalation** — what may be repaired, narrowed, accepted, or rejected locally and what requires reassessment or reauthorization at another level.
8. **Learning and stabilization** — how negative cases may improve the relevant Sensors, Constraints and realizations, Controllers, Actuators, assumptions, and decision rules rather than closing as isolated incidents.

The manuscript should make this common rhythm visible without mechanically repeating eight labels in every paragraph. A compact table may summarize the frame after the four detailed subsections if it improves navigation.

**Required proportionality framing before the level subsections:**

The full map is a **reference architecture for reasoning**, not a requirement to instantiate every element at maximum depth. The manuscript must make the following distinction explicit:

```text
full map = inspect every decision horizon and capability family
implementation depth = proportionate to the actual system
```

A simple low-consequence Thinking System may legitimately need few explicit controls, lightweight evidence, and the same people carrying several responsibilities. A high-authority, high-consequence, weakly reversible, slowly observable, or economically fragile system may require much more of the map to be explicit and operational. The map should therefore be used twice: first to detect hidden complexity, then to justify which parts can safely remain lightweight. A team must not infer “simple system” merely from a simple UI, one model call, or one feature boundary; broad authority, downstream side effects, poor observability, Human Authority load, or expensive fallback can make an apparently small feature a complex controlled object.

**Required framing before the level subsections:**

- State that the four levels are not four governance documents, four mandatory teams, or four approval meetings.
- Explain that they are the decision-ownership horizons through which governance becomes operational.
- State that production release at the intended scope requires the relevant capability functions and decisions to be connected across all four levels, **at a depth proportionate to the actual consequence and control problem**.
- Preserve the distinction that combining responsibilities in one person does not collapse the decisions.
- Explain that the same organization may implement Controllers at different levels using different mixtures of people and automation.
- Use **Article §2**'s expanded-perimeter conclusion and recurring control questions as orientation. Introduce the canonical four decision levels here for the first time; **Article §2** intentionally does not define their labels, ownership, or reassessment semantics.

**Primary architectural anchor — Figure 9: Two orthogonal models**

Show two adjacent views. The **decision-ownership side must present the canonical four-horizon model defined in this section**: use the four horizon questions, the shared reassessment-evidence node fed by Delivery realization evidence and Runtime operation evidence, the downward labels, and the three direct reassessment routes with the invalidated-decision-basis wording specified below. Keep the same decision-ownership model consistent between the standalone four-horizon Figure 8 and Figure 9 rather than creating a second competing representation.

```text
Decision ownership — canonical four-horizon model
Organization — What may be authorized?
→ Project / Architecture — Is the controlled system viable and authorizable?
→ Delivery — Is this bounded realization complete and releasable?
→ Runtime — Does active operation remain inside the authorized boundary?

Delivery realization evidence ─┐
Runtime operation evidence ────┴→ Reassessment evidence — behavior · outcomes · control state · changed assumptions

Reassessment evidence → Delivery: implementation / realization / evidence issue
Reassessment evidence → Project / Architecture: risk / authority / feasibility / capacity / economics invalidated
Reassessment evidence → Organization: authoritative source / decision right / shared capability changed

Capability functions at every level — visually distinct control dimension
Actuators and corrective action
Constraints and realizations
Sensors and evidence
Controllers and decision authority
```

Use one restrained green semantic class for the capability-family side so the additional control-theory dimension is immediately distinguishable from the decision-horizon model. The green treatment identifies the orthogonal capability model, not a maturity state, safety claim, or execution sequence. The capability-family ordering is a reading aid consistent with **Article §3**; it must not be rendered as a directional pipeline. Use a neutral undirected structural rail or equivalent grouping to show that the four capability families form one control-capability model without implying causal sequence. The figure must show that all four capability families may appear at every decision horizon and must not imply one-to-one mapping, four mandatory services, or a one-way waterfall.

#### Organizational authorization and control context

**Primary question owned:** Within which authoritative boundaries, shared capabilities, and decision rights may a proposed project explore or operate, and which decisions remain reserved to the organization?

The manuscript may preserve the shorter orientation question **“What may be authorized?”** in figures. The detailed subsection must make clear that Organization decides admissibility, authoritative boundaries, shared capabilities, reserved authority, evidence obligations, and exceptions. It may prohibit a use category or permit only bounded research. **It does not own the project-level decision that Model Judgment is necessary for a specific business outcome or that the complete Thinking-System architecture is economically viable; those decisions belong to Project / Architecture.**

**Activation triggers:**

- a new business capability, process problem, customer need, or product opportunity for which a Thinking-System path is proposed;
- a proposed expansion of autonomy, delegated authority, deployment population, geography, data access, tool access, vendor/deployment mode, or downstream action capability that would cross or change an organizational boundary, reserved decision right, shared capability, approved basis, or exception;
- a new or changed legal, contractual, privacy, security, safety, procurement, vendor, geography, prohibited-use, incident, or shared-capability source;
- a Project Reauthorization request that cannot be resolved inside existing organizational authority;
- repeated delivery or runtime evidence showing that an organizational assumption, shared capability, decision right, or business rationale may no longer be valid;
- cross-project incidents, audits, external regulatory or contractual changes, vendor changes, or organizational capability-health evidence even when no single runtime event triggered the review.

**Inputs and authoritative basis:**

- the proposed business capability and project rationale;
- existing policies, contracts, legal obligations, security/privacy boundaries, procurement rules, customer commitments, geography and deployment restrictions, prohibited uses, incident obligations, and vendor constraints;
- existing shared organizational capabilities such as identity, authorization, audit, secrets management, logging, incident response, rollback/shutdown, data governance, model/vendor approval, and Human Authority capacity;
- existing exception authority and decision-right structures;
- external or organizational evidence such as audits, regulatory change, contractual change, vendor notices, cross-project incidents, portfolio evidence, and shared-capability health;
- project, delivery, or runtime evidence when the level is reactivated after initial authorization.

**Questions and decisions owned:**

- Is the proposed use category admissible for the organization at all?
- Which outcomes, actions, data uses, geographies, populations, vendors, deployment modes, or authority expansions are prohibited, conditionally allowed, or explicitly reserved to Human Authority?
- Which existing organizational sources are authoritative for this system and which take precedence when they conflict?
- Which organizational functions legitimately own decisions that may be affected by system behavior—for example product, engineering, architecture, operations, security, privacy, legal, compliance, procurement, finance, customer support, domain specialists, or executive authority?
- Which decisions may be delegated to Project, Delivery, or Runtime Controllers, and which remain reserved at organizational level?
- Which exceptions may be granted, by whom, using what evidence, for what scope and duration?
- Which shared capabilities are mandatory dependencies before Project Authorization can be credible?
- Which material evidence must lower levels be able to produce so organizational decision owners can know when a boundary or assumption they own is threatened or invalidated?
- Which external or cross-project evidence must be monitored because it can invalidate the organizational basis even when the Thinking System itself appears locally healthy?

Organization may express that a class of activity must remain deterministic where an authoritative source genuinely requires that property, but the ordinary engineering choice between deterministic, manual, narrower model-assisted, and broader Thinking-System designs remains a Project / Architecture viability decision.

**Capability obligations created by organizational authority:**

The organization does not merely name participating departments. If an organizational function has legitimate authority over a boundary or outcome, the downstream architecture must provide that decision owner with an operable control relationship.

For every material organizational boundary or reserved decision right, the article should establish the chain:

```text
authoritative source or organizational decision
→ scoped project Constraint or explicit project assumption
→ required Constraint Realization properties
→ Sensor / evidence obligation
→ Controller / decision owner and expected decision latency
→ available Actuator, escalation, exception, or reauthorization path
```

This does **not** mean Organization designs every technical Sensor or realization. It means Organization creates evidence and decision obligations that Project / Architecture must make realizable.

Where a prohibited state can feasibly be made unreachable through deterministic enforcement, Project / Architecture should prefer deterministic realization rather than probabilistic influence. An organizational statement is not a Hard Constraint merely because its source is authoritative. If deterministic prevention cannot be credibly realized for the relevant path, the system must not hide that uncertainty behind a Hard label.

**Controller composition at Organization level:**

- The organizational Controller is the legitimate decision function, not a committee by definition.
- It may be one accountable person, several existing functions, or an existing governance/management process.
- Human authority will usually dominate consequential organizational decisions, but sensing and decision support may be automated where useful and credible: source/version tracking, policy checks, evidence aggregation, threshold detection, notification, routing, dependency-health signals, and preparation of exception or reauthorization context.
- Automation may help apply explicit delegated rules, but it must not invent authority, change a prohibited-use boundary, or silently accept residual risk outside delegation.
- Automated organizational checks are themselves control mechanisms whose data sources, configuration, failures, and blind spots require evidence when material.

**Organizational Actuators:**

The organizational horizon must show that it can do more than observe and approve. Depending on legitimate authority, organizational Actuators may:

- publish or revise an authoritative source or interpretation;
- approve, deny, narrow, suspend, or revoke project permission;
- grant or reject a scoped exception;
- change approved vendor, deployment, geography, or data-use permission;
- fund, provide, restrict, or withdraw a shared capability;
- require additional evidence or a new Project Reauthorization;
- reserve a decision to Human Authority;
- stop or suspend a project when the organizational basis is no longer valid.

The article must distinguish these actions from Project or Runtime Actuators. Organization changes the authoritative context or permission boundary; it does not directly perform a runtime rollback unless the same person or mechanism separately holds runtime authority.

**Outputs and artifacts flowing downward:**

The level should produce or make explicit, by reference where possible:

- organizational status: prohibited, eligible only for bounded research, or eligible for Project / Architecture assessment inside stated conditions;
- authoritative source references and organizational assumptions relevant to the use case;
- prohibited or conditionally allowed outcomes, actions, authority, data use, populations, geographies, vendors, or deployment modes;
- reserved Human Authority and exception authority;
- delegated decision rights for Project, Delivery, and Runtime;
- mandatory shared-capability dependencies;
- organizational evidence obligations and escalation expectations;
- conditions that require return to organizational review.

Do **not** require a new standalone “UA Organization Document.” Existing sources and decision records should be linked rather than copied. In an SMB, several responsibility bundles may be held by the same people. These outputs may be represented inside existing project or architecture records, including the repository's Project Control Architecture and Viability Review pattern, when that preserves clarity and ownership.

**Evidence and change received:**

From lower levels:

- Project finding that a required control cannot be realized credibly under the current organizational boundary;
- Project finding that control economics, latency, Human Authority capacity, vendor constraints, or shared-capability cost destroy the expected business case;
- requests to expand authority, autonomy, geography, data access, vendor choice, deployment mode, or reachable downstream actions;
- repeated or material runtime violations of an organizationally owned boundary;
- evidence that lower levels cannot produce the information required for the organizational decision owner to act credibly.

From outside the local project/runtime path:

- legal, contractual, regulatory, procurement, customer, or policy change;
- vendor or model-provider change affecting an approved dependency;
- audit findings;
- cross-project incident or recurring organizational failure mechanism;
- degradation, unavailability, or changed assumptions in a shared organizational capability;
- portfolio evidence showing that an exception, permission model, or control expectation is systematically inadequate.

**Local action versus escalation:**

Organization may prohibit, authorize eligibility for project assessment, condition, narrow, suspend, change a shared capability, redefine delegated authority, approve or reject an exception, or require Project Reauthorization. Runtime and Delivery may trigger organizational review; they do not perform it automatically. A lower-level workaround cannot normalize an organizationally prohibited state.

**Learning and stabilization:**

Negative cases affecting organizational decisions must not end with “incident closed.” They should ask whether:

- the authoritative source was ambiguous or inaccessible;
- decision rights were unclear;
- required evidence was missing, late, or too aggregated;
- a shared capability failed or was incorrectly assumed;
- an exception path encouraged authority drift;
- organizational Constraints were too broad, too vague, internally conflicting, or impossible to realize at the claimed strength;
- the organization repeatedly authorized project classes whose control perimeter later proved unattractive.

The resulting change may improve source clarity, delegated authority, evidence obligations, shared capabilities, exception handling, project-entry criteria, or organizational admissibility rules. The manuscript must present this systematic learning treatment as a **proposed operating discipline under validation**, not as already-established normative UA doctrine.

**Supporting figure — Figure 10: Organizational control process across the lifecycle:** Replace the current department-centric influence map with a process-oriented organizational control loop showing both endogenous and exogenous evidence as **converging inputs**, not as a sequential evidence pipeline:

```text
external / organizational evidence
legal · contractual · audit · vendor · cross-project incident · shared-capability health ───────┐
                                                                                               │
authoritative organizational sources + shared capabilities + decision rights ─────────────────┼→ Organizational Controller / legitimate decision owners
                                                                                               │
project / runtime evidence or authority-change request ────────────────────────────────────────┘
                                                                                               ↓
                                                                                  organizational decision
                                                                                               ↓
                                                                                  Organizational Actuators:
                                                    change permission · exception · shared capability ·
                                                    vendor/deployment approval · suspend/narrow
                                                                                               ↓
                                                         updated authoritative context and evidence obligations
                                                                                               ↓
                                                                                  Project / Architecture
```

Examples within the lower-level evidence lane include a Project viability or authority request and Runtime evidence that invalidates an organizational basis. They are examples of that lane, not additional independent inputs that should be drawn a second time.

The three upper inputs must remain visually parallel or convergent in the manuscript figure. Authoritative sources are the reference basis, while external/organizational evidence and project/runtime evidence are evidence streams; none should be drawn as if it is generated by the preceding input. The caption must state that the figure represents a decision horizon and control relationship, not a required department structure, sequential stage gate, or claim that Organization directly performs all downstream technical actions.

#### Project / architecture control and viability

**Primary question owned:** Does a credible, operable, and economically viable control architecture exist for this proposed Thinking System within the organizationally authorized boundary?

This is the level at which organizational admissibility becomes a concrete system authorization decision. A successful prototype is not Project Authorization. **Project / Architecture owns business outcome and AI necessity for the specific system.**

**Activation triggers:**

- organizational eligibility or bounded research authorization for a proposed use;
- a material new use of Model Judgment inside an existing project;
- a new Judgment Node, changed authority path, model/tool/retrieval architecture, vendor, deployment mode, or material population expansion;
- delivery or runtime evidence that invalidates project risk, authority, feasibility, evidence, Human Authority capacity, control latency, shared-capability assumptions, or economics;
- a proposed authority expansion that remains within organizational policy but exceeds current Project Authorization.

**Inputs and authoritative basis:**

- intended business outcome and the **proposed rationale or hypothesis** for using Model Judgment, not a presumption that its value has already been proven;
- organizational admissibility, authoritative source references, prohibited states, reserved decisions, shared-capability dependencies, evidence obligations, and reassessment triggers;
- proposed deterministic, manual, narrower model-assisted, and broader Thinking-System alternatives where relevant;
- proposed system boundary, user population, data, models, tools, dependencies, downstream effects, and reachable authority;
- material scenarios, expected operating conditions, business assumptions, cost assumptions, and available Human Authority;
- relevant prior evidence, incidents, platform limitations, and known failure modes.

**Questions and decisions owned:**

- Is Model Judgment genuinely required for the intended outcome, or should the design use a deterministic, manual, or narrower judgment-dependent path?
- What value is expected specifically from Model Judgment, and what value is lost when Constraints narrow autonomy, data, tools, population, or speed?
- Where is Model Judgment placed and which Consequential Runtime Responsibilities depend on it?
- What authority and downstream consequences are reachable from each Judgment Node?
- Which material scenarios could move the system outside acceptable operation?
- What intended outcome and required operating-contract properties must Delivery translate into an approved Requirement and Operating Envelope for a bounded realization?
- Which organizational boundaries become scoped project Constraints?
- Which complete Constraint Realization paths are credible, and at what guarantee strength?
- What evidence can detect loss of acceptable operation early enough for the consequence?
- Who or what owns each project-level decision and which authority can be delegated downward?
- Which Actuator can change operation when evidence requires action?
- Where is substantive Human Authority required, and is the required information, expertise, time, volume, and fallback capacity realistic?
- What happens when Sensors, realizations, models, tools, automation, Human Authority, or fallback are unavailable or degraded?
- If fallback/recovery is material to viability, is there evidence that it is sufficiently independent from the relevant primary failure/common dependency, available at required capacity and latency, and capable of restoring an authorized state?
- Can at least one **credible complete bounded control path through the required capability functions** be described for every material scenario?
- Does the full control perimeter preserve technical, operational, and economic viability?
- Which assumptions or evidence changes require Project Reauthorization?

**Capability obligations:**

Project / Architecture translates risks and organizational decisions into a realizable control architecture. For each material scenario it must derive or identify:

- scoped Constraints and intended guarantee strength;
- candidate Constraint Realizations and complete paths;
- Sensors and evidence, including active instrument/version identity, validation or calibration basis where applicable, coverage, uncertainty, latency, blind spots, and validity-loss triggers when model, population, policy, or operating conditions change materially;
- Controller decisions, authority, and escalation boundaries;
- effective Actuator paths;
- Human Authority, fallback, containment, recovery, and fail-safe behavior where required, including the failure modes, dependency/common-mode assumptions, capacity/latency, and restoration conditions of fallback paths when material;
- versioning and correlation sufficient to reconstruct the material active authorization and behavioral/control baseline when later evidence challenges a decision, without requiring one universal registry or manifest;
- evidence obligations needed by organizational decision owners.

**Control economics and viability:**

The business case must include the complete control perimeter rather than treating control as post-launch overhead. To avoid double counting, the article must distinguish non-overlapping cost buckets conceptually rather than subtracting Human Authority and fallback twice.

Use this decision structure:

```text
expected value attributable to Model Judgment
compared with
solution lifecycle cost
+ complete control-perimeter lifecycle cost
+ residual exposure / uncertainty that remains after control
→ authorize / narrow / bounded research / redesign / defer / No-Go
```

Where useful, explain that **solution lifecycle cost** may include model, platform, data, integration, and ordinary operation, while **control-perimeter lifecycle cost** may include Constraint design/realization, evaluation and evidence, Human Authority, fallback, observability, incident response, false blocks, control maintenance, reassessment, additional latency, and control-specific operational friction. The categories are a reasoning aid, not a universal accounting standard.

The point is architectural: if adequate control destroys the economics, the correct engineering outcome may be deterministic redesign, narrower scope, research, deferral, or No-Go. A hard prohibition or missing authority/capability cannot be averaged away by favorable expected value.

**Controller composition at Project / Architecture level:**

The project Controller is commonly socio-technical. Architecture, product, engineering, risk/security/domain owners, finance or operations may contribute evidence and authority according to the decision. Automated tooling may gather model/evaluator evidence, verify invariants, compare versions, estimate capacity/cost, detect missing dependencies, and route deviations where those mechanisms are sufficiently trustworthy and observable. Human decision owners remain accountable for decisions that require legitimate business, architectural, residual-risk, or authority judgment. Automation should be evaluated as part of the architecture rather than assumed to reduce control cost without creating new failure modes.

**Outputs and artifacts flowing downward:**

- Project Authorization status and authorized scope;
- one versioned **Project Constraint Architecture** containing the scoped Project Constraints and assumptions it owns;
- project boundary and intended Judgment landscape;
- **separate required operating-contract properties and evidence obligations** that Delivery must translate into its approved Requirement and Operating Envelope for the bounded scope; these are a Project output but are not part of the Project Constraint Architecture merely because they travel downward with it;
- material scenarios and assumptions;
- required Constraint Realization properties and claimed strength;
- required Sensors/evidence and expected decision latency;
- Controller ownership and delegated authority;
- required Actuator paths;
- Human Authority, fallback, containment, and recovery requirements, including material independence/common-mode, capacity/latency, transition, and restoration expectations for fallback where applicable;
- required shared capabilities and dependencies;
- baseline-correlation obligations needed to reconstruct material active authorization/configuration later;
- control economics baseline;
- reauthorization triggers;
- conditions under which Delivery may narrow, repair, or experiment without returning to Project.

The repository's **Project Control Architecture and Viability Review** is one canonical pattern that can carry this baseline. The article should not imply that every implementation must use that exact form; existing architecture, product, risk, or decision records may carry the same decisions when ownership, versioning, and evidence remain explicit.

**Evidence and change received from Delivery / Runtime:**

- inability to realize a required Hard Constraint or evidence path;
- evidence coverage weaker than assumed or evidence-instrument validity/calibration no longer fit for the decision basis;
- inability to reconstruct which material authorization/configuration baseline produced the evidence;
- new reachable tool/action/data paths;
- drift or incidents that change scenario likelihood or consequence;
- Human Authority overload or unavailability;
- fallback saturation, common-mode failure, loss of independence, or inability to restore the authorized state;
- control latency incompatible with the consequence;
- material model/vendor/platform changes;
- changed capacity or unit economics;
- repeated local defects indicating the architecture rather than one implementation is wrong;
- requested authority or scope expansion.

**Local action versus escalation:**

Project may authorize, narrow, condition, redesign, require more research, defer, or issue No-Go. Project may change its architecture within organizational authority. If the proposed change requires a new organizational boundary, reserved decision right, vendor/deployment permission, or shared capability outside existing authorization, Project must escalate to Organization.

**Learning and stabilization:**

Negative cases should test whether the project model of the controlled object was wrong: missing scenario, incorrect assumption, insufficient Constraint, non-credible Hard claim, poor Sensor coverage or validity, wrong Controller authority, ineffective Actuator, unrealistic Human Authority capacity, fallback/common-mode failure, automation failure, non-reconstructable active baseline, or invalid economics. Repeated delivery/runtime workarounds are evidence that Project Authorization may need revision rather than more local tuning. This systematic negative-case learning loop is a publication-facing proposal under validation; the article must distinguish it from already-established normative lifecycle rules.

**Supporting figure — Figure 11: Project control architecture and viability:** Show:

```text
organizational admissibility + intended outcome
→ Model Judgment necessity / deterministic or narrower alternative check
→ material scenarios and reachable consequences
→ Project Constraint Architecture: scoped Project Constraints + assumptions
→ separate required operating-contract properties + evidence obligations for Delivery
→ credible complete bounded control paths through required capability functions
→ Human Authority / fallback / recovery
+ control economics and capacity
→ authorize / narrow / bounded research / redesign / defer / No-Go

Delivery/runtime invalidating evidence → Project Reauthorization
Project need for wider authority → Organizational review
```

The figure must not place the required operating-contract properties inside the Project Constraint Architecture. They are a separate Project output that Delivery translates into its approved Requirement and Operating Envelope.

#### Designing the control architecture

This remains inside the Project / Architecture decision horizon and must not be presented as a fifth level.

**Required argument:**

- Translate material business and operational risks into a realizable control structure.
- Identify where Model Judgment is placed, what authority and consequences are reachable from each Judgment Node, which deterministic responsibilities must surround it, and which scenarios could produce unacceptable outcomes.
- Derive the required Constraints, candidate Constraint Realizations, Sensors, Controller decisions, Actuator paths, Human Authority, fallback, containment, recovery, and reassessment mechanisms.
- Distinguish machine-checkable or syntactic evidence from semantic or probabilistic evidence without creating new capability families.
- Machine-checkable evidence may verify schema, type, structure, permissions, tool arguments, state transitions, resource limits, and other deterministic conditions.
- Semantic evidence may estimate grounding, relevance, harmfulness, intent alignment, factual support, policy meaning, or downstream business acceptability.
- Semantic evidence must expose the active instrument/version, validation or calibration basis where applicable, coverage, uncertainty, latency, blind spots, and validity-loss triggers when the model, population, policy, data distribution, or operating conditions change materially rather than being treated as an oracle.
- Treat Human Authority as part of the architecture where required, including information, decision right, time, expected volume, expertise, fatigue, escalation rights, unavailability, and overload.
- Treat fallback/recovery as an evidenced control path: test the relevant failure behavior, shared dependencies/common-mode coupling, capacity/latency, transition behavior, and restoration assumptions instead of assuming a secondary path is safer.
- Prefer deterministic realization for prohibited states where technically feasible and do not upgrade a Soft guarantee to Hard because the business intent is important.
- Drive the design from the risks, authority, and consequences of the system rather than a generic control-component checklist.

#### Delivery realization and release

**Primary question owned:** Is this bounded realization complete, evidence-bearing, operationally supportable, and acceptable for a specific deployment context under Project Authorization?

**Activation triggers:**

- Project Authorization of a bounded implementation or experiment;
- a new feature, Judgment Node, model/prompt/context/retrieval/tool change, Constraint Realization change, evaluator change, or material configuration change;
- a new deployment population or environment inside existing Project Authorization;
- local runtime defect, realization degradation, or evidence issue that Delivery is authorized to repair;
- Project Reauthorization that changes the delivery baseline.

**Inputs and authoritative basis:**

- Project Authorization and current Project Constraint Architecture;
- inherited Constraints, assumptions, intended Judgment landscape and placement assumptions, **separate required operating-contract properties**, evidence obligations, shared-capability dependencies, delegated authority, reauthorization triggers, baseline-correlation obligations where material, and control economics baseline;
- implementation scope and deployment context;
- relevant historical defects, incidents, runtime evidence, and known failure modes.

**Questions and decisions owned:**

- What approved Requirement and Operating Envelope define successful and acceptable operation for this bounded delivery scope?
- Is the bounded work ready to begin under known authority and evidence conditions?
- Are all Judgment Nodes and deterministic responsibilities in scope explicit?
- Does every inherited and local Constraint have a concrete realization path or an explicit unresolved gap?
- Are claimed Hard paths complete and bypass-tested for the reviewed scope?
- Are Sensors/evaluators/telemetry operational and versioned, with evidence quality, coverage/uncertainty/latency, validation or calibration basis where applicable, and validity-loss triggers sufficient for the decisions they feed?
- Can material release, incident, and correction evidence be correlated to the active authoritative-source, Project, Delivery, realization, model/configuration, evaluator, deployment, and fallback baseline rather than to an ambiguous list of independent versions?
- Are Controller decision boundaries and delegated authority explicit?
- Are Actuators, fallback, rollback, containment, and Human Authority paths operational and tested?
- Where fallback is material, has its relevant dependency/common-mode coupling, capacity/latency, transition behavior, and ability to restore an authorized state been tested?
- Are failure/unavailable/degraded states explicit?
- Is implementation and evidence complete for the reviewed scope?
- Is release acceptable for the specific population, environment, model/configuration versions, residual exposure, capacity, and economics?
- Does any new evidence invalidate Project Authorization rather than only a local realization?

**Capability obligations:**

Delivery owns and maintains the approved Requirement and Operating Envelope for the bounded scope and makes the inherited project control architecture concrete. It must implement, configure, verify, and operate the required realizations, Sensors, bounded Controllers, Actuators, Human Authority interfaces, fallback, version records, and evidence paths. It must also ensure that material evidence can travel upward in a form usable by Project and Organization decision owners and can be attributed to the material active baseline sufficiently to diagnose which decision or realization was actually in force.

**Controller composition at Delivery level:**

Delivery Controllers combine explicit human release/engineering authority with automation. Automation may handle repeatable invariant checks, build/test/evaluation execution, evidence aggregation, traceability, drift/version detection, policy-as-code checks, blocked-action verification, release-condition checks, routing, and safe bounded actions **when evidence quality, failure behavior, reversibility, consequence, and delegated authority make the automated path credible**. The automated path must itself remain observable and correctable. Human decision owners retain contextual release acceptance, bounded engineering judgment, and residual-risk acceptance within delegated release authority; changes to project architecture or authority must be escalated to Project / Architecture or Organization as appropriate.

**Outputs and artifacts:**

- a bounded delivery decision record using the repository's **Thinking System Review** pattern or an equivalent existing workflow that preserves the same decision boundaries;
- an approved Requirement and Operating Envelope for the bounded delivery scope;
- one canonical **Constraint Realization Map** for the bounded scope, whether represented in the UA template or in an equivalent owned engineering record;
- Definition of Ready decision and evidence;
- implementation and bounded experiments inside delegated authority;
- Definition of Done decision and evidence completeness;
- deployment-specific Release Gate decision;
- active model, prompt/instruction, context/retrieval, tool/routing, policy, evaluator, realization, deployment-scope, and fallback versions where material, correlated with relevant source/Project/Delivery baselines enough to reconstruct the material active behavioral/control state;
- runtime Sensor/Actuator configuration and expected decision latency;
- fallback/recovery evidence where material, including relevant common dependencies, capacity/latency, transition behavior, and restoration result;
- known gaps and reauthorization/escalation triggers.

**Evidence and change received from Runtime:**

- local implementation or configuration defects;
- realization unavailable/degraded/bypassed signals;
- evaluator or telemetry gaps, calibration/validation loss, or evidence-instrument mismatch to the active model, population, policy, or operating conditions;
- drift or version mismatch, including inability to correlate evidence to the active baseline;
- denied-action or failed-Actuator evidence;
- Human Authority overload;
- fallback saturation, failed transition/restoration, or common-mode failure with the primary path;
- incidents and complaints;
- unexpected cost/latency/capacity behavior;
- repeated local corrections indicating a project-level assumption is invalid.

**Local action versus escalation:**

Delivery may repair, reconfigure, roll back, narrow exposure, disable, or re-release within delegated authority. It may not silently expand project authority, weaken an inherited Hard Constraint, change an organizational prohibition, or normalize evidence that project viability has failed. Delivery evidence that challenges Project Authorization routes to Project Reauthorization. If that Project decision requires a changed organizational boundary, reserved decision right, or exception, Project escalates to Organization. An exogenous change to the organizational basis may activate Organization directly; the affected Project Authorization must then be reassessed before Delivery proceeds under a new baseline.

**Learning and stabilization:**

Every material negative case should ask which part of the delivery control architecture failed or was insufficient:

- missing or late Sensor, or an evidence instrument that lost validity for the decision it was meant to support;
- ambiguous or incomplete Constraint;
- incorrect, degraded, or bypassable Constraint Realization;
- Controller rule/authority/latency problem;
- ineffective or unavailable Actuator;
- weak Human Authority path;
- fallback that shared the failed dependency, lacked capacity, failed to transition, or could not restore an authorized state;
- failed or misleading automation;
- missing deterministic validation around Model Judgment;
- inadequate test/evaluation coverage or invalid evaluator/Golden Set/rubric/threshold basis;
- untracked or non-correlatable version/configuration drift.

The fix should improve the weakest control element and the evidence that verifies it. For evidence instruments that may mean recalibration, replacement, changed coverage, threshold/rubric revision, or a new validity-loss trigger; incident evidence must not be ingested automatically into a new baseline merely because it exists. Do not default to prompt tuning because the model produced the visible symptom. Treat this systematic learning practice as a proposed operating discipline to be validated through application evidence.

**Supporting figure — Figure 12: Delivery translation and release loop:** Extend the current translation figure so it shows:

```text
Project Authorization + Constraints + evidence obligations
→ Delivery-approved Requirement + Operating Envelope for the bounded scope
→ Definition of Ready
   → ready: delivery implementation / realization → evaluation / verification → Definition of Done
   → not ready: revise the bounded operating contract or evidence plan → Definition of Ready
   → project contradiction: Project Reauthorization
Definition of Done
   → complete: deployment-specific Release Gate
   → incomplete: return to delivery implementation / realization
   → project basis invalidated: Project Reauthorization
deployment-specific Release Gate
   → approved or limited: runtime deployment and evidence
   → rework required: return to delivery implementation / realization
   → stop / defer / reject: terminal for this release attempt
   → project decision required: Project Reauthorization
   → organizational-boundary / reserved-authority issue discovered through Delivery evidence: Project Reauthorization
runtime evidence
   → local implementation / realization / evidence issue: contain / roll back / narrow / disable → delivery implementation / realization
   → authorization basis invalidated: Project Reauthorization
Project Reauthorization
   → organizational boundary must change / organizational exception required: Organizational review

Exogenous authoritative-source / organizational-decision-right / shared-capability change
   → Organizational review
   → Project Reauthorization when the project baseline is affected
   → Delivery proceeds only from the resulting authorized baseline
```

Preserve the existing two-way business ↔ engineering translation claim inside this process. The figure should show technical evidence being interpreted as changed exposure / decision consequences and feeding back into engineering/release reasoning without implying an additional lifecycle gate. DoR, DoD, and Release Gate must remain decisions with explicit **rework**, **terminal stop/defer/reject**, and **Project Reauthorization for delivery-discovered authorization/boundary issues** rather than appearing as an unconditional forward pipeline or allowing Delivery to bypass the Project decision surface. Organizational review is direct only when the organizational basis itself changes or when Project Reauthorization determines that organizational authority/exception is required.

#### Runtime operation, correction, and reassessment

**Primary question owned:** Does active operation remain inside the authorized Requirement, Constraint baseline, authority, capacity, and economics with required realizations active and healthy, and what response is authorized when it does not?

**Activation trigger:** Runtime is continuously active while the Thinking System operates. Specific Controller decisions are triggered by Sensor evidence, violations, drift, incidents, degraded control state, capacity/economic thresholds, authority failures, or scheduled reassessment conditions.

**Inputs and authoritative basis:**

- active authorized Project and Delivery baselines;
- deployment scope and active versions;
- delegated runtime authority;
- active Constraints and Constraint Realizations;
- Sensor/evidence definitions, active instrument versions, interpretation/validation/calibration basis where applicable, and validity-loss conditions;
- Controller rules and Human Authority responsibilities;
- available Actuators, fallback, containment, rollback, disable, and stop paths, including material fallback dependency/capacity/restoration assumptions;
- enough correlated baseline identity to reconstruct relevant authoritative-source, Project, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state for material evidence;
- expected decision latency and escalation routing.

**Questions and decisions owned:**

- Is the active controlled system operating inside the authorized boundary?
- Are required realizations active, healthy, and non-bypassed?
- Are model behavior, downstream outcomes, cost, latency, capacity, Human Authority, fallback, and control health inside acceptable conditions?
- Can the material evidence be attributed to the actual authorization and behavioral/control baseline active when the event occurred?
- Is the current evidence sufficient to make the runtime decision, or has Sensor/evaluator validity degraded because the model, population, policy, data distribution, or operating condition no longer matches the instrument's basis?
- Which local corrective action is authorized now?
- Did the Actuator actually produce the intended state?
- If fallback was invoked, did it avoid the relevant primary/common-mode failure, carry the required load, and restore a known authorized state?
- Has operation returned to a known authorized state, or has the basis of Project or organizational authorization been invalidated?
- What must be escalated, to whom, and with what evidence?

**Capability obligations:**

Runtime must operate the complete feedback path:

```text
active Thinking System / realizations
→ Sensors and evidence
→ Runtime Controller / Human Authority within delegated authority
→ Actuator / fallback
→ changed operation
→ Sensor verification of the resulting state
```

Monitoring must cover the whole software controlled object and its socio-technical control perimeter rather than only model output. Evidence may include model behavior, downstream outcomes, active source/Project/Delivery baseline identity, model/prompt/context/retrieval/tool/routing versions, authorization failures, realization activation and bypass, evaluator results and evaluator validity state, policy/configuration and deployment scope, fallback configuration/health/capacity/common dependencies, drift, complaints, overrides, Human Authority capacity, cost, latency, incidents, Actuator execution, and post-action verification. The objective is not a universal manifest; it is sufficient correlation to reconstruct the material active baseline when evidence or an incident must be interpreted.

**Controller composition at Runtime:**

Runtime may automate the control path as far as consequence, evidence quality, failure behavior, reversibility, and delegated authority make credible. Deterministic checks, rate/permission boundaries, circuit breakers, routing, rollback, exposure narrowing, fallback selection, and well-defined invariant responses need not require humans merely for ceremony. Human Authority is required where interpretation, accountability, residual-risk acceptance, or reserved authority cannot be credibly automated. Automated runtime control remains bounded by delegated authority and may not reauthorize the project. The automated Controller and Actuator path itself must expose health, configuration, failures, latency, and resulting state so that automation does not become an unobserved control dependency.

**Outputs and records:**

- active evidence, evidence-instrument version/validity state where material, and control-health state;
- runtime decisions and decision basis where material;
- Actuator execution and verification evidence;
- incidents, overrides, Human Authority decisions, fallback use/failure/capacity/restoration, denied actions, and relevant outcomes;
- correlated active source/project/delivery/configuration/version traceability sufficient to reconstruct the material behavioral/control baseline;
- routed evidence packages for Delivery, Project, or Organization when the relevant basis is invalidated.

These are operational records, not necessarily a new standalone UA document or universal registry.

**Evidence routing by invalidated decision basis:**

```text
local implementation, realization, configuration, or evidence issue
→ Delivery reassessment

project risk, authority, feasibility, evidence, Human Authority capacity, control latency, fallback credibility, baseline reconstructability, or economics changed
→ Project Reauthorization

authoritative source, decision right, prohibited-use boundary, approved vendor/deployment mode, or shared capability changed
→ Organizational review

proposed authority expansion
→ Project Reauthorization
→ Organizational review where the organizational boundary must change
```

**Local action versus escalation:**

Runtime may reject, contain, compensate, route to fallback, narrow exposure, roll back, disable, or stop within delegated authority. These actions may restore a previously authorized state. They do not authorize redesign, new authority, or a new business boundary. A fallback is not presumed safe merely because it is configured; failed/common-mode fallback, saturation, or inability to restore an authorized state is evidence for reassessment. Persistent or repeated local recovery is evidence for reassessment when the underlying basis remains invalid.

**Learning and stabilization:**

Runtime negative cases are not only operational noise. Their analysis may improve the control system at the correct level. The review asks whether the case exposed:

- a missing Sensor, blind spot, or evidence instrument that lost validity for the active decision;
- a weak or mis-scoped Constraint;
- a degraded/bypassable realization;
- a Controller threshold, authority, or decision-latency problem;
- an ineffective Actuator;
- a Human Authority capacity problem;
- fallback/common-mode coupling, capacity failure, failed transition, or failed restoration;
- failed or misleading automation;
- inability to reconstruct the material active baseline;
- a project scenario or assumption that was wrong;
- an organizational boundary or shared capability that needs revision.

Repeated cases should become less frequent, earlier detectable, less consequential, cheaper to correct, or structurally impossible where deterministic prevention is feasible. The paper must present this as an **operating hypothesis to validate**, not as established empirical evidence that the loop necessarily stabilizes real systems.

**Supporting figures:**

- Figure 13 — runtime control and reassessment;
- Figure 14 — evidence and change routing.

Keep Figure 13's escalation exit generic (`authorization basis invalidated → route by decision ownership`) and let Figure 14 own the concrete Delivery / Project / Organization destinations. Ensure Figure 12 and Figure 14 agree: a Delivery-discovered issue that challenges Project Authorization routes first to Project Reauthorization; Organization is reached directly only when the organizational basis itself changed, or from Project when wider organizational authority/exception is required.

#### Cross-level operating discipline — measurement, negative-case learning, automation, and stabilization

This subsection is required after the four level descriptions. Its purpose is to state a **publication-facing operating proposal under validation** that builds on the current status-bearing reassessment structure of the draft-normative Nested Control Lifecycle without silently promoting new research prose into doctrine. It is not a fifth decision level.

**Epistemic-status rule:** Existing authority-bearing UA sources already establish downward inheritance, runtime evidence, local reassessment, Project Reauthorization, organizational review, and capability relationships. This paper proposes making systematic negative-case analysis and control-improvement feedback more explicit across those levels. Until separately reconciled into doctrine/patterns through framework review and application evidence, describe that learning/stabilization discipline as a proposed operating hypothesis rather than as settled normative UA behavior.

**1. Measure for decisions, not for dashboards.**

Do not use “measure everything” literally. Every **material control claim and decision basis** should be observable enough for the Controller that owns it to decide within the consequence-relevant time horizon. Evidence should have a known consumer, decision boundary, expected latency, coverage, uncertainty, blind spots, active instrument version, validation/calibration basis where applicable, explicit conditions under which the instrument may lose validity, and enough active-baseline identity to reconstruct the material configuration/authorization context when the decision depends on it. Telemetry with no decision path remains observation.

**2. Every material negative case gets triaged to an owning decision level.**

A **negative case is evidence requiring diagnosis, not a diagnosis by itself**. It may later be classified as a Requirement violation, Constraint violation, realization defect, accepted residual behavior, false positive, near miss, changed assumption, capacity/economic break, Human Authority failure, fallback/common-mode failure, or other condition. Do not turn every deviation or undesirable output into a Bug by definition.

A negative case may include a violation, near miss, denied action, bad output, downstream harm, failed realization, Sensor blind spot or validity loss, Actuator failure, Human Authority overload, fallback saturation or common-mode failure, capacity/economic break, non-reconstructable baseline, or evidence that an authorization assumption is false. It should route to the level that owns the affected decision basis rather than to the team that happened to observe it first.

**3. Analyze control failure, not only model failure.**

For each material negative case ask:

```text
Did the Sensor fail to observe, observe in time, or remain valid for the decision it was meant to support?
Did the Constraint fail to express the required boundary?
Did the Constraint Realization fail, degrade, or permit bypass?
Did the Controller have the wrong rule, evidence, authority, or latency?
Did the Actuator fail to execute or verify correction?
Did Human Authority lack information, time, capacity, or power?
Did fallback share the failed dependency, lack required capacity, fail to transition, or fail to restore an authorized state?
Did automation introduce a hidden failure, latency, coupling, or false-confidence path?
Can the material event be attributed to the actual authorization/configuration baseline that was active?
Was the project scenario, assumption, or economics wrong?
Was the organizational source, decision right, or shared capability wrong or changed?
```

The visible model output is only one possible failure location.

**4. Improve the weakest control element and its evidence.**

Corrective learning may improve Sensors, Constraints, realizations, Controller logic, Actuators, Human Authority, fallback, baseline correlation, assumptions, tests/evaluators, organizational sources, delegated authority, or project economics. Where an evaluator, Golden Set, rubric, threshold, or structured human-review signal is implicated, improvement may require recalibration, replacement, revised coverage, a new validity-loss trigger, or changed interpretation—not automatic ingestion of every incident into a new baseline. The system should not treat repeated prompt adjustment as the default response to every negative case.

**5. Prefer deterministic prevention for prohibited states where feasible.**

When a prohibited state can credibly be made unreachable at an identity, permission, type, transaction, resource, tool, or execution boundary, prefer that deterministic enforcement and verify the full path. Do not claim Hard control where only probabilistic influence exists.

**6. Automate control work where the automated path is itself controllable.**

Across all levels, automation may reduce repetitive sensing, evidence collection, invariant checking, routing, version comparison, alerting, decision support, and safe bounded Actuation. Use it when evidence quality, failure behavior, reversibility, consequence, and delegated authority make the automated path credible. Higher-level Controllers may remain predominantly human because decisions involve business authority, ambiguity, residual exposure, or exceptions. Runtime Controllers may be predominantly automated. In every case, authority must be explicitly delegated before automation exercises it, and the automated path must itself expose health, decision basis where material, configuration, failures, and resulting state.

**7. Stabilization means reducing uncontrolled recurrence, not eliminating probabilistic variance.**

The proposed objective is not zero variance from Model Judgment. It is progressive reduction of uncontrolled or poorly understood failure modes. Over time, important negative cases should ideally become one or more of:

- structurally prevented;
- detected earlier;
- routed to the correct Controller faster;
- corrected by a more reliable Actuator;
- cheaper to recover from;
- less consequential because exposure or authority is narrower;
- better represented in project scenarios and evidence obligations;
- reflected in revised organizational or project authorization where required.

The article must not claim that this stabilization effect is already empirically validated across real systems. It is a concrete hypothesis for worked applications and external review.

**Supporting figure — Figure 15: Cross-level learning and stabilization loop:** Show negative case/evidence → triage to owning decision level → diagnose Sensor/Constraint/Realization/Controller/Actuator/Human Authority/fallback/automation/baseline/assumption weakness → change within authority or reauthorize upward → improved control architecture → runtime verification. The figure must not imply that every case escalates to Organization or that every negative case is a Bug.

#### Known risks, rejected formulations, and unresolved decisions for Article §4

Preserve these explicitly for future drafting and external review:

- **Organization / Project boundary:** Organization owns admissibility, authoritative boundaries, shared capabilities, reserved decisions, evidence obligations, and exceptions; Project / Architecture owns business outcome, AI necessity, concrete control architecture, control economics, and Project Authorization. Do not drift back into an organizational “AI necessity gate” unless authority-bearing doctrine is deliberately changed.
- **Full map versus proportional implementation:** The article must show the complete map clearly enough to expose hidden complexity while avoiding the implication that every low-consequence system needs the maximal process, automation, artifacts, or roles.
- **Negative-case learning status:** Systematic cross-level learning/stabilization is a proposed operating discipline under validation. Do not describe it as mature empirical evidence or normative doctrine until application evidence and framework review justify that change.
- **Automation boundary:** The useful degree of automation differs by horizon and case. Avoid “automate as much as possible” as a universal rule; automation may introduce hidden coupling, common-mode failure, latency, false confidence, or new evidence obligations.
- **Behavioral/control baseline correlation:** Material evidence, incidents, release decisions, and Actuator actions need enough correlation across authoritative-source, Project, Delivery, realization, model/prompt/context/retrieval/tool/routing/evaluator/policy/deployment/fallback state to reconstruct what was actually active. The paper must not turn this need into a mandatory universal registry or invent a canonical “Behavioral Configuration Baseline” artifact before application evidence shows one is warranted.
- **Fallback independence and restoration:** A fallback is not safer merely because it exists. Application evidence must test whether fallback/recovery paths are sufficiently independent from the relevant primary/common-mode failure, available at required capacity/latency, transition correctly, and can restore a known authorized state. Do not promote one universal fallback pattern before such evidence exists.
- **Evidence overload:** More Sensors are not automatically better. Future application should test how much evidence is sufficient for each decision without creating alert fatigue, unusable dashboards, or control cost that destroys viability.
- **Evidence-instrument lifecycle:** Evaluators, Golden Sets, rubrics, thresholds, and human-review signals can lose validity when the model, population, policy, data distribution, or operating environment changes. Future application must test practical versioning, calibration/validation, validity-loss detection, incident ingestion, recalibration, and replacement rather than assuming a stable Sensor once deployed.
- **Repeated local defect threshold:** It remains unresolved when repeated delivery/runtime defects should be treated as evidence of a project-architecture problem rather than independent local defects. Do not invent a universal count or frequency threshold.
- **Organizational Actuator taxonomy:** The paper may show functional examples such as changing permission, exception, vendor approval, shared capability, or project eligibility. Do not create a mandatory exhaustive taxonomy unless future doctrine requires one.
- **Constraint precedence/conflict:** Multiple organizational Constraints may conflict or have different authority sources. The article should acknowledge precedence and conflict resolution as a required decision problem without pretending the current paper provides a universal resolver.
- **Stabilization measurement:** The paper may use qualitative directions—prevention, earlier detection, faster routing, cheaper recovery, narrower exposure—but should not invent one universal stability score.
- **Artifact/form neutrality:** The repository's two-living-review SMB pattern and Constraint templates are plausible implementation surfaces, not the conceptual map itself and not yet evidence that every team should carry the map through exactly those forms. The publication should keep them in the repository layer rather than making them central article sections.
- **External validation goal:** These unresolved points are appropriate prompts for community review and worked applications rather than defects to hide before publication.

**Repository anchors for Article §4:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)
- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md)

**Transition:** Once the full operating map is visible, the next practical question is not “which UA form must I fill in?” but “how much of this map must be made explicit for this controlled object, and where can existing engineering and organizational mechanisms carry the required decisions?”

**Closing claims:**

> Lower levels may refine and narrow a higher-level decision. They may not silently expand its authority or normalize evidence that invalidates it.

> A decision owner that receives no fit-for-purpose evidence is authority on paper, not an operational Controller.

> The complete map should be inspected even when implementation is deliberately lightweight; proportionality is justified reduction, not permission to ignore complexity that is actually present.

> Material evidence must be attributable to the active authorization and behavioral/control baseline well enough to diagnose what actually governed the event; this need does not imply one mandatory registry or artifact.

> Fallback and recovery are credible only to the extent that their failure behavior, relevant independence/common-mode assumptions, capacity, transition, and restoration are evidenced for the intended consequence profile.

> Systematic negative-case learning is a proposed way to improve the control architecture at the level that owns the failed decision basis; it remains to be validated through worked applications and external review.

**Accepted drafting decisions from the 2026-08-12 Article §4 rewrite and the 2026-08-15 operational-transfer review:**

- Make proportionality explicit before the level subsections: inspect the full four-horizon × four-capability map first, then justify implementation depth from the actual controlled object rather than superficial feature size.
- Preserve Figure 9 as the literal orthogonal-model bridge: decision horizons answer where decisions belong; capability families answer how control becomes operational; no one-to-one mapping is permitted.
- Use one visible operating rhythm across all four horizons without mechanically repeating eight labels: activation, authoritative basis, owned decision, capability obligations, outputs, returned evidence, local action versus escalation, and learning.
- Replace the department-centric Organization figure with a process-oriented organizational control relationship in which authoritative sources, external/organizational evidence, and lower-level evidence converge on legitimate decision owners.
- Keep the Organization / Project boundary strict: Organization owns admissibility, reserved authority, shared capabilities, evidence obligations, and exceptions; Project / Architecture owns AI necessity, concrete control architecture, control economics, and Project Authorization.
- Make the Project / Architecture horizon explicitly compare deterministic, manual, narrower model-assisted, and broader Thinking-System alternatives before authorizing Model Judgment for the intended outcome.
- Include the complete control perimeter in project viability rather than treating evaluation, Human Authority, fallback, observability, and control friction as post-launch overhead; keep attributable value, non-negotiable Project Constraint Architecture boundaries, separate required operating-contract properties, and residual exposure / uncertainty after proposed control visibly connected to the final Project decision rather than collapsing them into tradeable economics.
- Preserve DoR, DoD, and Release Gate as distinct Delivery decisions even when one lightweight workflow carries them; Release Gate outcomes must distinguish rework, terminal stop/defer/reject, and escalation to Project Reauthorization when Delivery evidence challenges the project/authority basis. Organizational review is reached directly only for an exogenous organizational-basis change, or from Project when wider authority/exception is required.
- Keep Runtime restoration distinct from redesign and route evidence according to the decision basis invalidated rather than the team that first observed the signal.
- Preserve enough correlated source/project/delivery/realization/model-config/evaluator/deployment/fallback identity to reconstruct the material active behavioral/control baseline for release, incident, and corrective evidence; do not create a mandatory universal registry by implication.
- Treat fallback/recovery as an evidenced control path rather than an automatic safe state; test relevant independence/common-mode coupling, capacity/latency, transition behavior, and restoration where material.
- Add a cross-level negative-case learning and stabilization loop as a publication-facing operating hypothesis under validation, not a fifth horizon or already-established normative doctrine.
- Define stabilization as reducing uncontrolled recurrence, not eliminating probabilistic variance; prefer deterministic prevention where prohibited states can feasibly be made unreachable.

**Working word budget:** 3,400–4,600 before final compression. Do not optimize this section back to the previous 1,800–2,300-word target until the operating model is fully expressed and reviewed.

---

#### State established by the end of Article §4

**Article §§1–4** now establish the conceptual operating map. Future drafting must treat the following as inherited results rather than material to teach again:

- Thinking-System classification through Consequential Runtime Responsibility + probabilistic Model Judgment;
- the whole software Thinking System as controlled object and the socio-technical control perimeter around it;
- the four capability families and the distinctions among Constraint, realization, Sensor, Controller, Actuator, and substantive Human Authority;
- Hard/Soft semantics at the complete realized-path level;
- Organization, Project / Architecture, Delivery, and Runtime as four decision-ownership horizons;
- authority, decision rights, and Constraints flow downward by reference while scoped realizations become concrete; changed authoritative sources and Delivery realization or Runtime operation evidence return to the horizon whose decision basis they affect or invalidate;
- the complete-map-before-depth proportionality rule and its consequence/authority/evidence/Human-Authority/economics dimensions;
- governance as operational through the active socio-technical control architecture;
- evidence-instrument validity as part of Sensor sufficiency where material;
- material active-baseline reconstructability as an evidence/traceability requirement without a mandatory universal registry;
- fallback/recovery credibility as an evidenced property—including relevant independence/common-mode coupling, capacity/latency, transition behavior, and restoration—not a property inferred from mere existence;
- cross-level negative-case learning/stabilization as a proposed discipline under validation.

**Article §5** applies these results. It must not reproduce the four-horizon pressure test, baseline-correlation argument, fallback-credibility argument, or implementation-depth argument from **Article §4** unless a newly discovered contradiction requires revising the earlier manuscript.

### Article §5 — Applying the Map Without Overbuilding

**Purpose:** Show how a team turns material relationships discovered through the complete map into the lightest credible composition of existing records and operating mechanisms, without making one repository artifact set, team structure, platform, or ceremony mandatory.

**Epistemic status — proposed paper-level application test.** The carrier-sufficiency test, complete material-relationship working mapping, materiality rule, and substitution handoff developed in **Article §§5–6** are research hypotheses under validation. They are not new UA conformance requirements, do not enlarge the `SPECIFICATION.md`-defined specification boundary, and do not require a new mandatory artifact. Existing records and operating mechanisms may carry the same relationships. **Article §7** formally delimits this paper-level synthesis from the existing draft specification.

**Core claim:** The paper proposes that proportionality is credible when every material relationship remains operable and traceable somewhere. Reuse existing carriers when they preserve the intended outcome, the applicable operating-contract basis—proposed properties for an unapproved candidate or the active Delivery-approved Requirement and Operating Envelope for an authorized bounded scope—and the authority, scope, evidence, decision, action, verification, and reassessment semantics. Add a new record, automation, or operating mechanism only where a material relationship would otherwise be lost. This is an application/sufficiency hypothesis to test, not an already-established universal conformance rule.

**Inherited premise from Article §4:**

**Article §4** has already taught and applied the complete-map-before-depth rule to the canonical action-capable case. Do not prove or narrate that rule again. This section answers the next question: **where do the material operating-contract, boundary, decision, and control relationships live, and how do we know the chosen carriers are sufficient?** The **Article §5** counterfactual sibling is a different candidate Project design and scope. Reapply the category test and record its defined positive result: the human makes and executes the consequential decision, but that decision remains materially dependent on the model's draft or recommendation, so the sibling remains a Thinking System and receives its own compact full-map inspection. Publication prose should show only the material delta rather than reteaching the map.

**Controlled comparison rule — separate authority/scope delta from lifecycle-maturity delta:**

The lower-authority sibling and the canonical action-capable case must be compared at the **same lifecycle point** when the paper attributes differences to authority or scope. Use the Project / Architecture candidate-design point before Delivery approval for both alternatives. At that point, both sides carry proposed required operating-contract properties, proposed boundaries, expected evidence, Human Authority, Actuation, reassessment, dependencies, and economics appropriate to their candidate scope. The comparison may then identify which additional obligations arise because the canonical candidate can communicate or transact directly.

The canonical system's later active Delivery-approved Requirement and Operating Envelope, realized transaction guard, active Runtime Sensors/Actuators, release evidence, and operational version carriers are a **separate lifecycle-maturity delta**. They may be recalled after the like-for-like comparison because **Article §4** has already followed the canonical system into Delivery and Runtime. They must not be used as evidence that the authority difference itself caused those artifacts. A lower-authority candidate that is later authorized and delivered would also acquire Delivery/Runtime carriers appropriate to its own scope.

**Why this section remains artifact-neutral:**

The repository contains a Project Control Architecture and Viability Review, a Thinking System Review, Constraint templates, a Constraint Realization Map pattern, and illustrative reference material. They remain useful implementation patterns. The article must not make “two living reviews,” `K-SEND-01`, or any one toolchain the central proof of the map. The durable publication contribution is the carrier-selection and sufficiency logic; repository artifacts may be linked as optional starting points.

**Blueprint-only drafting workflow:**

Use this to organize the section; do not reproduce it as a second numbered method in publication prose. The publication-facing output and required mappings below carry the result.

```text
1. inherit the canonical full-map reasoning, category-test the counterfactual candidate Project design and scope, record why its consequential human decision still materially depends on Model Judgment, and apply the map to that distinct Thinking System
→ 2. compare authority/scope at the same Project / Architecture candidate maturity point using proposed required operating-contract properties for both alternatives
→ 3. extract the intended outcome and material authority, boundary, evidence, decision, action, verification, and reassessment relationships; use the active Delivery-approved Requirement and Operating Envelope only when analyzing an already authorized bounded realization, not as part of the authority-delta comparison
→ 4. locate the existing records and operating mechanisms that already carry each relationship
→ 5. test whether those carriers preserve the required semantics and lifecycle
→ 6. add or strengthen only the uncovered material pieces
→ 7. verify the connected path across carriers
→ 8. revisit depth, scope, carrier choice, or evidence-instrument validity when an authoritative source, authorization, scope, Project assumption, model/population/policy/operating condition, Delivery realization, or Runtime operation changes the materiality judgment
```

Do not turn this into a second explanation of all four horizons. **Article §4** owns the map; **Article §5** owns its application to each materially different candidate Project design and scope and, where Project Authorization permits implementation, its projection into a concrete Delivery composition.

**Blueprint-only relationship patterns:**

Use these as internal inputs to the required relationship-to-carrier mapping. Do not reproduce all three chains as a second publication-facing method; the mapping should carry their representative semantics.

Do not force the approved operating contract or every standing decision basis through a Constraint path. Preserve the appropriate end-to-end relationship.

For the positive operating contract of an authorized bounded scope:

```text
Project Authorization, intended outcome, and required operating-contract properties
→ Delivery-approved Requirement and Operating Envelope for the bounded scope
→ deterministic obligations, model-mediated expectations, evidence expectations, and required failure handling
→ active scope, version, and accountable owner
→ observed behavior and fit-for-decision evidence
→ authorized correctness diagnosis or lifecycle decision
→ action, verification, and reassessment when the operating contract is violated or invalidated
```

For a material boundary or control obligation:

```text
legitimate source / authorized decision
→ scoped Constraint and assumptions
→ active realization
→ fit-for-decision evidence
→ legitimate Controller
→ effective Actuator
→ verified resulting state
→ local reassessment or return to the owning horizon
```

For a standing decision or assumption such as AI necessity, viability, authorization rationale, scope, economics, or Human Authority capacity:

```text
legitimate source / decision authority
→ recorded rationale, alternatives, and assumptions
→ authorized scope and active version
→ downstream obligations and accountable owner
→ fit-for-decision evidence
→ continue, narrow, redesign, stop, or reauthorize
→ reassessment when the decision basis changes or is invalidated
```

These patterns may be distributed across several tools, records, people, and automated paths. They do not require one document or one product.

**Credible-carrier test:**

An existing architecture record, product requirement, ADR, issue, CI check, evaluation store, release workflow, access-control system, runtime monitor, incident process, audit record, or governance platform is a credible carrier only where the material relationship remains clear enough to operate. Test:

1. **Owner and authority** — who owns the decision, and what legitimate decision right does the carrier represent or execute?
2. **Operating contract** — where are the intended outcome and, as applicable, the proposed operating-contract properties of an unapproved candidate or the active Delivery-approved Requirement, Operating Envelope, correctness criteria, and required failure handling carried?
3. **Source, scope, assumptions, guarantee, and version** — which authoritative source, bounded subject/path/scope, assumptions, guarantee strength where applicable, and active version are represented?
4. **Lifecycle and change control** — who may change the carrier, how does the change become active, and what requires reassessment?
5. **Evidence and consumer** — what evidence is produced, with what active instrument/version, validation/calibration basis where applicable, coverage/uncertainty/latency and validity-loss triggers, and which Controller uses it for correctness, continuation, release, correction, or reassessment?
6. **Decision and action** — which bounded decision follows, which Actuator can execute it, and what happens when action is unavailable or fails?
7. **Post-action verification** — what evidence confirms that the requested change produced the intended state?
8. **Failure and reassessment route** — which defects remain local, and which evidence invalidates Delivery, Project / Architecture, or Organization?
9. **Access, retention, and auditability** — where material, can the relevant owner retrieve and trust the active decision/evidence history?

A carrier may be lightweight. It may not be semantically empty.

**Record versus operating mechanism:**

The section must apply distinctions already derived in **Article §§3–4**:

- a Requirement record may preserve the approved operating contract but does not by itself realize a Constraint, produce evidence, diagnose Correctness, or execute correction;
- an ADR may preserve a decision but does not realize a Constraint;
- a test or evaluator may produce evidence but does not itself make the Release decision;
- an approval workflow may execute routing but does not create the authority to approve;
- a dashboard may expose evidence but is not a Controller unless a legitimate decision function actually consumes that evidence;
- a feature flag or API may provide Actuation but does not authorize its own use.

One surface may carry several functions, and one material obligation may span several surfaces. Describe the mapping as a **many-to-many composition with end-to-end traceability**, not as one tool or document “containing the map.”

**Gap-closing rule:**

- Reuse and reference a credible existing carrier rather than duplicate it in a UA-specific form.
- Add a new record only when ownership, lifecycle, scope/version, access, retention, or auditability would otherwise be unclear.
- Add automation only where a repeatable sensing, evidence, checking, routing, bounded-decision, or Actuation function is credibly automatable. Judge evidence quality, failure behavior, reversibility, consequence, and delegated authority as applicable, and keep whichever automated path is chosen observable and correctable.
- Add an operating practice only when a material decision or reassessment path would otherwise remain absent.
- Do not confuse fewer artifacts with fewer decisions; do not confuse more artifacts with stronger control.
- Revisit depth bidirectionally: evidence may require stronger control, narrower authority, a different carrier, evidence-instrument recalibration/replacement, consolidation of duplication, or removal of control work that proves immaterial.

---

#### Running-example application — same business proposal, different candidate Project scope

Use the manuscript callout heading `### Running Example | Same Business Proposal, Different Candidate Project Scope`.

**Lens in this section:** how material obligations and credible carriers change between a counterfactual lower-authority design and the canonical action-capable support system.

Use two Project / Architecture alternatives from the same business proposal:

- **Counterfactual lower-authority scope:** Model Judgment drafts or recommends; an adequately informed and empowered human may reject or replace the recommendation, makes the consequential decision, and executes customer communication or transactions. The human decision nevertheless remains materially informed by and dependent on the model's recommendation. The system cannot communicate directly, execute refunds, or change account state.
- **Canonical action-capable scope:** the system may communicate directly and execute bounded refunds/credits up to the illustrative delegated threshold; higher-value transactions remain under Human Authority.

The lower-authority branch is not the next chronological state of the canonical case and not another Delivery realization inside the canonical Project Authorization. It is a separate candidate Project design and scope. Its system identity and business context remain recognizable, while reachable authority, effects, and control perimeter differ.

Reapply the category test and state the answer rather than leaving the decisive causal fact implicit. In this defined sibling, the human's consequential decision remains materially dependent on the model recommendation, so the sibling remains a Thinking System. The human's real authority reduces reachable system authority and may reduce control depth; it does not remove Model Judgment from the consequential responsibility. A design in which no Consequential Runtime Responsibility remains materially dependent on Model Judgment would fall outside the category, but that is a different design and is not the sibling used in the comparison.

After recording that positive category result, inspect the counterfactual against all four decision horizons and all four capability families as a distinct candidate controlled object and Project scope before calling it lighter; do not imply that the comparison itself grants Project Authorization. Publication prose should show the material differences while **holding lifecycle maturity constant for the authority/scope comparison**. Compare proposed operating-contract properties, reachable authority, boundaries, evidence obligations, Human Authority, candidate Actuation, reassessment, dependencies, and economics for both Project / Architecture candidates. Only afterward may the article recall the canonical system's active Delivery-approved Requirement/Operating Envelope and Runtime realization as a separate maturity callback.

Include one compact comparison table covering:

| Comparison dimension | Draft/recommendation + human execution | Direct communication + bounded refund execution |
|---|---|---|
| Lifecycle point used for the authority/scope comparison | candidate Project / Architecture design before Delivery approval | candidate Project / Architecture design before Delivery approval |
| Intended outcome and proposed operating-contract basis | proposed required properties that a later Delivery-approved Requirement and Operating Envelope would need to carry if this candidate scope were authorized | proposed required properties that a later Delivery-approved Requirement and Operating Envelope would need to carry if this action-capable candidate scope were authorized |
| Model-Judgment-dependent consequential responsibility | what remains consequential despite human mediation | what would reach customers or business state directly if authorized |
| Reachable authority and effects | what the candidate system cannot execute | proposed delegated transaction and communication authority |
| Material boundaries and claimed guarantee strength | which deterministic boundaries or other Hard/Soft claims remain necessary after the positive category retest | transaction gating plus explicit Hard/Soft distinction for semantic uncertainty |
| Human / decision authority | information, time, competence, capacity, independence, and real power in the human decision path | substantive Human Authority for reserved decisions above threshold and overload/fallback obligations |
| Evidence, corrective mechanisms, and Actuation | proposed evidence needed for the human decision and correction | proposed transaction, guard, Human Authority, fallback, rollback/disable, and post-action evidence obligations |
| Carrier composition at the candidate point | which existing Project-level records/workflows could carry the candidate obligations | which additional Project-level realization/evidence obligations become material before Delivery designs concrete carriers |
| Economics | expected cost and latency of substantive human execution | expected control-perimeter cost of bounded autonomous operation |
| Reassessment | what would invalidate the lower-authority Project design | what would require Delivery reassessment, Project Reauthorization, or Organizational review once realized |

**Lifecycle-maturity callback — not part of the authority-delta test:** After the table, briefly reconnect the canonical action-capable design to the already drafted Delivery/Runtime state from **Article §4**: its active Requirement and Operating Envelope, transaction guard, active evidence instruments, release decision, and runtime carriers are consequences of having matured an authorized design into operation. They must be presented as the canonical case's **maturity delta**, not as proof that broader authority alone requires “more documents.” A delivered lower-authority design would likewise have active carriers, just for a narrower material relationship set.

Human mediation reduces control demand only where it genuinely reduces reachable authority, consequence, irreversibility, or automation dependence. Rubber-stamping, poor information, overload, or lack of power to change the outcome can leave the consequential responsibility substantially Model-Judgment-dependent.

**Required canonical material-relationship-to-carrier mapping:** After the variant comparison, complete the mapping for every material relationship in the canonical action-capable case; this full working mapping is the handoff consumed by **Article §6**. Retain it **inside this living blueprint** as a blueprint-owned working section or appendix during drafting. Do not create a third living article-planning note merely to host the mapping; a standalone research artifact would require a separate explicit repository/editorial decision. **The map is a controlled research object, not an unversioned table whose contents define their own completeness universe.**

**Materiality invariant for this paper-level test.** Under the stated scope and assumptions, treat a candidate relationship as material when its absence, misrepresentation, or change could materially alter at least one of: the intended outcome; satisfaction of an applicable Requirement or Constraint; delegated authority or reachable consequence; a correctness, release, continuation, or stop decision; the ability to correct, contain, verify, or reassess operation; or technical/operational/control-economic viability. Apply this rule **before** evaluating a particular carrier or substitute so materiality cannot be defined post hoc to favor either the derived map or the competing composition. Reverse mapping may expose a missing candidate relationship and therefore expand, narrow, or challenge the material set; it does not permit silent retroactive redefinition of materiality.

Before any relationship rows, record a mapping header containing:

- **Mapping ID and version** — a stable identifier plus explicit version, e.g. `support-resolution-canonical-material-map / vN`;
- **controlled object and lifecycle baseline** — exactly which canonical system state is being mapped;
- **source/authorization baseline** — Project Authorization, authoritative source references, and other standing decisions used by the mapping;
- **scope boundaries** — subjects, paths, populations, environments, authority, and excluded scope relevant to materiality;
- **assumptions** — the assumptions under which carrier and guarantee claims are made;
- **materiality decision rule** — apply the invariant above independently of whether the derived UA categories or the candidate substitute already contain the relationship, and name the accountable owner of the judgment;
- **change log / supersedes** — what changed from the previous mapping version and why.

Do **not** embed a self-referential repository commit SHA in the mapping header. The logical mapping version belongs to the blueprint; the immutable source snapshot used for a substitution run is captured by the run/verdict record **after the mapping is frozen**. Prefer a deterministic digest of the canonical mapping content when the working map remains inside the living blueprint, because that digest survives branch rebases or squashes. A preserved Git blob/commit/tag may also serve as the immutable snapshot reference when its history is intentionally retained. Any material change to the mapping's relationship set, source/scope/assumptions, materiality rationale, guarantee semantics, or frozen equivalence basis requires a mapping-version increment and a new snapshot reference.

Every candidate relationship considered for inclusion or exclusion must retain a **materiality rationale**. A relationship cannot be excluded merely because it is awkward to classify in the four-horizon × four-capability partition.

The full working mapping is the canonical handoff to **Article §6**. Every semantic property that §6 freezes for substitution must therefore be recoverable from the mapping itself rather than reconstructed ad hoc from surrounding prose.

Use this schema for the retained full working mapping:

| Relationship ID | Material relationship | Source / scope / assumptions | Guarantee strength where applicable | Materiality rationale | Active carrier or carrier composition | Owner / authority | Decision / reference semantics | Evidence / intended consumer / action / verification | Lifecycle / change control / reassessment |
|---|---|---|---|---|---|---|---|---|---|

For a standing viability/economic relationship, **Decision / reference semantics** must preserve the accountable viability owner, relevant input categories, legitimate decision right, available outcomes such as continue/narrow/redesign/defer/No-Go, and the decision basis whose change triggers reassessment. The actual cost, latency, capacity, staffing, Human Authority burden, maintenance burden, operational friction, and failure surface remain separate observations for the later practical-preference comparison.

The manuscript may render only three or four representative rows—including the active Requirement/Operating Envelope, the deterministic transaction boundary, the Soft semantic communication/policy expectation, and Human Authority or Project Authorization—provided that it labels them illustrative and does not imply that the visible sample is the complete analysis. Render the publication-facing sample as a table, a clearly separated block, or a replacement figure if that is clearer; do not require both a mapping table and a mapping figure.

The retained full working mapping need not enumerate immaterial implementation detail, but it must cover every material operating-contract, boundary, authority, decision/reference, evidence/consumer, action/verification, lifecycle/change-control, and reassessment relationship and preserve its active version, source/scope/assumptions, guarantee semantics where applicable, and materiality decisions. Representative publication rows support only relationship-level illustration; they cannot by themselves support a whole-controlled-object substitution conclusion.

**Reverse-mapping closure rule:** The mapping is provisional until **Article §6** has reverse-mapped at least one serious substitute or adjacent method against it. If reverse mapping identifies a potentially material native relationship, guarantee, responsibility structure, or lifecycle semantic that is **absent from the imported canonical mapping**, the whole-controlled-object semantic-substitution verdict must stop. Do not force-fit the discovery into an existing row simply to preserve the map. Instead:

```text
reverse mapping identifies an absent potentially material relationship
→ record the native relationship and provenance in its own terms
→ apply the documented materiality rule independently of “is it already in the derived map?”
→ if immaterial: retain the exclusion and rationale
→ if material or still uncertain: increment the mapping version
→ add the relationship, or record the reference-model gap / unresolved classification explicitly
→ rerun the substitution test across every material relationship against the new mapping version
→ only then issue or restore a whole-controlled-object semantic-substitution verdict
```

Every whole-controlled-object semantic-substitution verdict must record the **mapping ID, mapping version, and immutable snapshot reference actually tested**. The snapshot reference is recorded in the verdict/test record after freeze; it is not required to be embedded in the mapping itself. If the mapping version changes, an earlier verdict becomes stale for the new mapping until the full substitution test is rerun; it remains a valid historical result only for the exact mapping version/snapshot against which it was issued.

If the repeated result shows that the four-horizon × four-capability partition itself loses important relationships, route that evidence to **Validation Program 2 — Structural sufficiency and reverse-mapping lossiness** rather than endlessly expanding carrier rows. **The UA-derived mapping must not define the universe against which UA's own completeness is tested.**

**What this adds to the case:** the full map is no longer another diagram to reproduce; it becomes a versioned material-obligation source whose credible implementation composition changes with the authorized scope and can itself be revised by reverse mapping.

---

**Minimum publication-facing output:**

The output is not a named template. The authority-variant comparison, canonical relationship-to-carrier mapping, and surrounding prose must together make the active operating contract, authorization/source/scope, Model-Judgment rationale, material Constraints and assumptions, realization/evidence path, legitimate Controller and effective Actuation, post-action verification, failure handling, and local/Project/Organizational reassessment routes traceable and operable. If these answers already live credibly across existing engineering and organizational systems, duplicating them into an additional UA form may reduce rather than improve control.

**Supporting representation — Material relationships to credible carriers:** The running-example comparison and a clearly labeled publication-facing excerpt from the complete canonical working mapping are required. Render the excerpt once—as a table/block by default or as a replacement figure if that makes the many-to-many carrier composition or changed-decision-basis trigger clearer. Do not add both forms, a third representation, or a redraw of the complete four-horizon × four-capability map. Any implementation surfaces shown are carriers of derived relationships, not new decision levels or capability families.

**Repository anchors:**

- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
- [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md)
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md)

**Transition:** Once carrier sufficiency is explicit, the next question is whether current engineering methods, safety/runtime-assurance approaches, standards, platforms, tools, governance systems, and ordinary organizational practice already carry the material relationships well enough that any additional operating augmentation or replacement composition is unnecessary.

**Closing claim:**

> The paper proposes the following application test: a proportionate implementation is sufficiently represented when every relationship that is material under the stated pre-substitution materiality rule has a credible carrier, and when a changed decision basis or reverse-mapping discovery triggers renewed inspection. This remains a paper-level hypothesis under validation rather than a new UA conformance requirement.

**Working word budget:** 950–1,200

---

### Article §6 — The Existing Landscape: What Current Approaches Solve — and Whether Anything Material Remains to Be Connected

**Purpose:** Test the derived operating map against serious conceptual, implementation, and organizational substitutes while treating pure authority and obligation sources as inputs rather than substitutes by themselves. Risk and management methods, including operated management systems, still receive the same composition/substitution test as other methods. The section asks whether existing methods and compositions already preserve the material relationships, and separately which semantically adequate operating composition is practically preferable, rather than whether the ecosystem lacks controls or whether one framework “covers more.”

**Core hypothesis to examine:** Existing approaches cover substantial parts of the Thinking-System control problem, often with more concrete implementation or deeper domain semantics than the derived map. The first open question is **semantic**: whether a material burden remains in connecting controlled-object scope, intended outcome and approved operating contract, capability, legitimate authority, guarantee strength, evidence routing, correctness and corrective action, reassessment, Human Authority, and **viability-decision semantics** around one system—or whether established methods and ordinary engineering practice already preserve equivalent or stronger semantics across every material relationship. For a material viability/economic relationship, semantic equivalence means preserving the accountable owner, relevant input categories, decision authority, available viability outcomes, and reassessment triggers—not matching the actual lifecycle cost, latency, staffing demand, or operational burden. If every material relationship is semantically preserved, the semantic integration gap is absent for that tested scope regardless of comparative overhead. A second, separate question is **practical preference**: among semantically adequate concrete operating compositions, which option preserves those relationships with the acceptable lifecycle cost, latency, capacity demand, operational friction, Human Authority burden, maintenance burden, and failure surface? Compare the actual existing composition with any proposed augmentation or replacement needed to close a residual gap; do not assume that use of the derived map itself constitutes an additional runtime or document layer. A third explanatory question asks whether the derived model adds useful conceptual clarity; conceptual overhead does not decide either semantic equivalence or practical control overhead.

**Epistemic boundary:**

> The preceding deduction argues, under the paper's stated premises, why these relationships are required for the controlled object it describes. It does not establish that current methods, organizations, standards, or platforms fail to preserve them.

The proposed integration gap remains a falsifiable landscape hypothesis. “Outside scope” identifies a responsibility that must be supplied elsewhere when material; it is not an inferiority score. Coverage is not maturity. A narrow research method, runtime architecture, standard, or implementation tool may be excellent precisely because it does not attempt to own the entire lifecycle.

**Naming discipline before Article §7:**

Use **the derived operating map**, **the reference model developed in Article §§2–5**, or **the paper's derived map** in publication prose. Do not repeatedly call it the “UA map,” “UA operating map,” or “UA-shaped architecture” before **Article §7** formally delimits the research synthesis in relation to the UA specification boundary defined and indexed by `SPECIFICATION.md`. The article title and abstract may identify UA for attribution; the comparison itself must not use the named framework as the premise that validates its own categories.

Use this publication-facing thesis or a close equivalent:

> **The ecosystem does not lack controls. The question is whether existing approaches or their composition already connect the material control relationships for this controlled object—and what the derived map itself fails to capture from those approaches.**

A second useful sentence to preserve:

> A team can assemble orchestration, guardrails, evaluation, observability, governance workflows, and compliance controls and still need an explicit answer to who owns the consequential decision, what guarantee is actually claimed, which evidence can invalidate authorization, and whether the resulting control perimeter makes the system worth building. The landscape analysis must determine whether that answer is already present before proposing anything additional.

Do **not** frame the section as a market contest or vendor scorecard.

#### Article §6.1 — Research comparison worksheet

Keep the detailed lens below in the blueprint and research notes. It ensures bidirectional, non-strawman analysis; it is **not** a fifteen-paragraph manuscript template to repeat for every approach family.

1. **Controlled object and normal scope** — model, prompt, trace, workflow/agent run, application, socio-technical system, AI use case, organizational estate, management system, hazard/loss structure, or another object?
2. **Primary function** — analysis, orchestration, evaluation, observability, enforcement, runtime assurance, governance, risk management, compliance, management-system control, or mathematical control research?
3. **Operating-contract semantics** — how does it preserve or help establish the intended outcome, active Requirement, Operating Envelope, deterministic and model-mediated obligations, correctness criteria, and required failure handling?
4. **Capability contribution** — which Constraint/realization, Sensor/evidence, Controller/decision, and Actuator functions can it perform, host, or inform?
5. **Decision-horizon contribution** — where does it materially contribute across Organization, Project / Architecture, Delivery, and Runtime?
6. **Authority semantics** — does it create an authoritative source obligation, record/delegate a legitimate decision, provide a workflow for one, or only execute configured logic?
7. **Guarantee semantics** — does it distinguish deterministic enforcement from probabilistic influence, and can it substantiate a Hard claim across the complete realized path?
8. **Evidence and action routing** — what evidence is produced, who consumes it, with what active instrument/version and validation/calibration basis where applicable, at what latency/coverage, under which validity-loss conditions, and what correctness, continuation, corrective, or reassessment path follows?
9. **Lifecycle reassessment** — how does it represent changed assumptions, invalidated authorization or Requirement, redesign, authority expansion, No-Go, continual improvement, or equivalent lifecycle change?
10. **Human Authority** — does it establish authority, information, competence, capacity, latency, fallback, and real power, or only provide an approval primitive?
11. **Viability-decision semantics and control economics** — does it preserve who owns the viability decision, which cost/capacity/latency/burden categories inform it, which outcomes can follow, and what triggers reassessment? Record actual lifecycle cost, Human Authority burden, fallback cost, false blocks, latency, incidents, maintenance, and operational friction separately for the later practical-preference comparison; numerical burden is not itself the semantic-equivalence test.
12. **Implementation versus source of authority** — can it implement a decision without being the legitimate source of that decision?
13. **Semantic substitution** — for each material relationship, which required semantic properties are preserved with equivalent or stronger meaning under the same relevant scope and assumptions?
14. **Practical preference / residual responsibility** — which material relationship remains unsupplied, if any, and if no semantic residual remains, what material control overhead differentiates the concrete operating compositions being compared?
15. **Reverse mapping / lossiness** — which native concepts, guarantees, responsibility structures, lifecycle semantics, or useful distinctions are lost, distorted, or forced unnaturally when translated into the paper's four horizons × four capability families?

Apply the same criteria consistently. Translate questions into the adjacent method's native concepts before judging it; do not require one-to-one vocabulary, lifecycle stages, or reproduction of the paper's partition.

#### Article §6.2 — Publication structure: three substitution classes plus authority inputs

The manuscript should group true substitutes into three compact analytical classes rather than thirteen mini product reviews, then assess sources of obligation and authority as a separate input class.

**A. Conceptual and engineering substitutes**

Treat established methods as serious alternatives capable of narrowing or disproving the synthesis claim:

- **STAMP/STPA** — socio-technical hierarchical control structures, safety constraints, unsafe control actions, feedback, process models, hazards/losses, and responsibility across organizational and technical boundaries. Its coverage may span all four horizons depending on application. Do not demote it to historical inspiration or a runtime monitor.
- **Simplex and related runtime-assurance architectures** — trusted assurance/safety paths, switching logic, fallback/recovery, and bounded operation around complex or untrusted components. Do not attribute STAMP's organizational semantics merely because both are safety-related.
- **Control-theoretic research around LLMs and AI systems** — distinguish research that treats a generative model as the controlled stochastic object from work that uses an LLM inside or as a Controller for another system. Preserve state, reachability, controllability, trajectories, stability, observer, intervention, and formal-boundary contributions where supported.
- **Production ML and software/systems engineering for AI** — use where these traditions materially contribute lifecycle, technical-debt, testing, assurance, change, maintenance, or responsibility semantics not already captured by the other approaches above.
- **Risk- and management-system methods** — treat NIST AI RMF, an operated ISO/IEC 42001-style AI management system, and comparable methods as possible lifecycle/organizational substitutes when they are adopted and composed with ordinary engineering practice. Test their actual decision, monitoring, corrective-action, and continual-improvement semantics rather than preclassifying them as mere obligation sources.

Required challenge:

```text
Could an established method
+ ordinary architecture, delivery, operations, and business-governance records
already preserve every material decision and relationship
with equivalent or stronger semantics under the same relevant scope and assumptions?

If yes, compare the concrete operating compositions:
existing composition unchanged
vs any proposed augmentation or replacement needed to close a residual gap.
Which has the acceptable material control overhead for the intended operating context?
```

A positive answer to the first question narrows or rejects the semantic integration-gap claim for the tested scope **regardless of comparative overhead**. The second question is a practical operating decision among semantically adequate compositions. Higher overhead may make a semantic substitute less attractive in practice; it does not recreate a semantic gap that the substitute already closed. The derived map may still be used as an analytical or review lens without becoming a runtime, workflow, or document layer. Reverse mapping must identify where the paper loses useful native structure—such as hierarchical control, hazards/losses, unsafe control actions, process models, trusted assurance separation, switching logic, or formal safety invariants—instead of treating every mismatch as a deficiency in the adjacent method.

**B. Implementation and integrated-stack substitutes**

Analyze implementation surfaces as a composition, not as five repeated tutorials:

- agent/orchestration runtimes may carry state, durable execution, routing, tool invocation, retries, checkpoints, human interruption, trace hooks, and portions of Controller/Actuator realization;
- guardrail/runtime-enforcement systems may perform Constraint Realization, Sensor, local Controller, and Actuator functions across input, output, retrieval, or tool boundaries;
- evaluation/observability systems may provide Delivery/Runtime evidence, datasets, experiments, evaluators, traces, alerts, version comparison, and sometimes automated response;
- managed AI/agent platforms may combine identity, deployment, orchestration, tool permissions, guardrails, evaluation, observability, policy/configuration, and approval mechanisms;
- enterprise governance/assurance platforms may carry AI-use-case records, policy/control mappings, risk and compliance workflows, factsheets, evaluation, monitoring, thresholds, approvals, lifecycle state, and integrations with lower-level controls.

Classify concrete functions rather than market labels. One integrated platform may implement substantial portions of all four capability families and several decision horizons. Preserve these distinctions:

- execution of a configured decision does not by itself establish legitimate authority;
- a probabilistic classifier does not create a Hard claim merely because it is sold as a guardrail;
- rich evidence does not by itself define the Controller, decision latency, or Actuator path;
- an approval primitive does not by itself establish substantive Human Authority;
- strong platform integration may eliminate many separate implementation surfaces and should be reused;
- the stronger a platform becomes at implementing control mechanics, the more important it becomes to distinguish delegated implementation authority from the source that legitimizes the decision.

Named products belong in the external-evidence/source plan and should appear in publication prose only as a small, freshly verified representative set.

**C. Organizational-practice substitutes**

Treat mature internal practice as a serious substitute where ordinary architecture, delivery, operations, security, legal, governance, operated management systems, and decision records already preserve the material relationships coherently. Judge the operated composition rather than the presence of framework-specific labels. If it preserves equivalent or stronger semantics across every material relationship under the same relevant scope and assumptions, treat it as a semantic substitute for the tested scope. Then compare material control overhead only among the actual candidate operating compositions; higher overhead affects preference, not semantic equivalence.

**Separate input class — Pure sources of obligation and authority**

These sources constrain or authorize a control architecture; they are not control-architecture substitutes by themselves. Keep source authority distinct from the risk/management method or operated composition that may implement it:

- applicable law and binding contractual obligations may directly create authoritative source obligations within scope; Organization identifies applicable authoritative sources and legitimately adopts internal or voluntary sources where appropriate, Project interprets them into scoped project Constraints, authorization conditions, required operating-contract properties, assumptions, authority, and evidence obligations, and Delivery translates the inherited baseline into an approved Requirement and Operating Envelope for the bounded scope;
- an adopted organizational policy may create an authoritative basis through legitimate organizational decision;
- a voluntary framework or standard does not become authoritative merely by existing; authority for a specific system may arise through adoption, contractual incorporation, certification/procurement commitment, policy, or another legitimate decision;
- the standard or source alone does not instantiate the application-specific control architecture, but an adopted and operated risk/management method composed with engineering practice must remain eligible for the same substitution test as other methods.

Preserve both directions:

- **Compliance is not identical to operational control:** an obligation may be documented while its application-specific realization/evidence/action path remains weak.
- **Operational control is not identical to compliance:** a locally controlled system may still violate an authoritative source obligation or an approved Requirement derived from it.

Do not repeat **Article §2**'s NIST/ISO category-label comparison. The lens here is functional contribution, authority, lifecycle, and substitution.

#### Article §6.3 — Compact landscape matrix

Use one required representation: either the compact matrix below or a coverage-band figure, not both unless integrated manuscript review shows that each adds a distinct relationship. Prefer approach classes and representative tendencies over product-level rows.

| Approach class | Typical controlled object / scope | What it may contribute substantially | What may require composition outside its normal scope | Mandatory reverse-mapping question |
|---|---|---|---|---|
| Systems/safety methods such as STAMP/STPA | socio-technical control structure, hazards, losses | constraints, hierarchical responsibility, unsafe control actions, feedback, lifecycle control analysis | Thinking-System category boundary or paper-specific terminology may be unnecessary or supplied separately | What hierarchical, hazard, loss, process-model, or responsibility structure does the four-by-four map flatten? |
| Runtime-assurance architectures such as Simplex | assured runtime architecture around a complex or untrusted component | trusted assurance separation, switching logic, bounded operation, fallback/recovery, runtime evidence and Actuation | organizational authority, intended outcome, broader lifecycle ownership, and viability-decision semantics may come from surrounding practice | What trusted-path, switching, fallback, or formal-assurance structure does the derived map fail to preserve? |
| Mathematical/control-theoretic research | generative model, stochastic state/process, LLM-mediated Controller, or physical/cyber-physical process | state, trajectories, observers, reachability, controllability, stability, optimization, intervention, and formal boundaries | socio-technical authorization, Requirement ownership, and lifecycle/viability-decision semantics may be outside the scoped research question | What dynamic, quantitative, or formal structure cannot be expressed precisely in the derived map? |
| Production ML and software/systems engineering for AI | production ML/AI system and its development/operation lifecycle | technical-debt, testing, assurance, maintenance, change, data/dependency, and responsibility semantics | paper-specific category, authority routing, or control-economics distinctions may be supplied separately | Which established lifecycle or technical-debt relationship is lost or merely renamed by the derived map? |
| Risk/management methods and operated AI management systems | organization, AI use case/estate, management system, risk and continual-improvement process | policy/risk decisions, lifecycle governance, evidence expectations, monitoring, corrective action, continual improvement, and management review | concrete application-specific realizations and Runtime Actuation may require engineering/platform composition | When does the operated method already preserve the cross-horizon relationships, and which management-system semantics does the derived map understate? |
| Implementation tools and integrated platforms | trace, workflow, agent run, application, platform estate | potentially all four capability functions, especially Delivery and Runtime; sometimes lifecycle/governance records | source of legitimate authority, AI-necessity/viability, or higher-level reassessment may be application/organization decisions | Which supposedly residual relationships are already implemented by current platform composition? |
| Pure authority/obligation sources—not substitutes by themselves | regulated/contract-bound system, adopted organizational policy, authorized scope | applicable law, binding contract, policy, adoption/authorization decision, and resulting source obligations | project Constraints and Project Authorization conditions, a Delivery-approved Requirement and Operating Envelope, and concrete realization/evidence/action depend on legitimate decisions at their owning horizons and an operated composition | Which source authority or obligation does the derived map understate or misclassify? |
| Mature internal organizational composition | the organization's actual socio-technical system | any or all material relationships through ordinary architecture, delivery, operations, security, legal, and decision records | nothing, if the composition is coherent and operable | Does the derived map add any decision value, or merely rename what already works? |

Cells describe common tendencies observed in the cited representative set, not universal properties. Product coverage is configuration-dependent; method coverage depends on application and surrounding lifecycle practice.

Required disclaimer:

> **The derived map is the reference frame for this comparison, not a scored implementation row. Adjacent approaches may carry important concepts more precisely and implement capabilities far more concretely. “Outside scope” identifies where composition may be required, not inferiority.**

#### Article §6.4 — Running-example composition test

Return to the canonical action-capable support system from **Article §4**. Import the **same mapping ID/version and immutable snapshot reference recorded after freeze** for the complete canonical material-relationship-to-carrier map produced in **Article §5**, including its mapping header, materiality decisions, source/scope/assumptions, guarantee semantics, decision/reference semantics, evidence/consumer/action/verification, lifecycle/change-control/reassessment, and intended outcome, Requirement, Operating Envelope, boundaries, authority, and viability-decision relationships. Do not rerun its credible-carrier test or reproduce its operational checklist, and do not substitute a visible manuscript excerpt for the full mapping.

Before examining any substitute, freeze the **required semantic properties for each material relationship** from that mapping. At minimum, where applicable, the equivalence basis includes:

```text
legitimate source / authority
+ relevant scope and assumptions
+ guarantee semantics
+ evidence and intended consumer
+ decision right
+ effective action and post-action verification
+ lifecycle / change control
+ reassessment route
+ viability-decision semantics: accountable owner, input categories, decision options, and reassessment trigger
```

The final viability-decision item applies only where economics/viability is material to the relationship. It preserves the meaning of the viability decision, not the numerical burden of one implementation. Actual lifecycle cost, latency, Human Authority load, capacity demand, maintenance burden, operational friction, and failure surface are recorded separately and compared only during **practical preference**.

A substitute may use different vocabulary, partitions, artifacts, stages, or technical mechanisms. **Semantic equivalence** exists only when those material properties are preserved for the same relevant scope and assumptions. Call a substitute **stronger** only when it preserves every required material property and adds a demonstrably stronger guarantee, coverage, assurance, or failure handling for the same purpose. If dimensions trade off, the scopes differ materially, or the evidence cannot support a dominance claim, record the relationship as **unresolved/non-comparable** rather than labeling the substitute stronger or weaker by intuition.

Test a representative conceptual method, implementation stack, or mature organizational practice against that exact mapping ID/version/snapshot. The manuscript may display a representative relationship-level excerpt for readability, but it must label that result partial.

Use one compact table or worked paragraph with only these results:

```text
imported material relationship + frozen equivalence basis
→ equivalent / stronger / residual / unresolved against the substitute composition
→ native concept or guarantee lost when translated into the derived map
```

The tested composition may include orchestration, deterministic platform controls, evaluation/observability, managed AI platforms, governance or organizational record systems, with authority/obligation inputs supplying legitimate sources. Mention them only to identify the tested composition, not to reteach what each tool class does.

The point is relationship-level semantic equivalence, residual relationships, unresolved comparisons, and reverse-mapping loss—not proof that every stack has gaps.

A representative excerpt supports only conclusions about the relationships actually tested. Claim whole-controlled-object **semantic substitution** only after the analysis covers every material relationship in the full **Article §5** mapping and every relationship is equivalent or stronger under its frozen basis; any residual, unresolved, non-comparable, or untested material relationship keeps the whole-object verdict open. Compare material control overhead only after semantic adequacy is established.

Every whole-controlled-object verdict must record the **mapping ID, mapping version, and immutable snapshot reference** actually tested. The reference is captured after freeze—preferably as a deterministic digest of the canonical mapping content for this blueprint-owned workflow—and need not be embedded in the mapping header. A later mapping-version increment makes the earlier verdict stale for the new mapping until the whole test is rerun; the earlier result remains a valid historical statement only about the exact mapping version/snapshot that was tested.

**Mandatory reverse-mapping closure:** If the adjacent method/composition reveals a potentially material native relationship, guarantee, responsibility structure, or lifecycle semantic that is absent from the imported mapping, **stop the whole-controlled-object semantic-substitution verdict**. Record the native concept in its own terms and provenance, apply the mapping's documented materiality rule independently of the current UA-derived rows, and then:

- if the relationship is immaterial, retain the explicit exclusion and rationale;
- if it is material or still uncertain, increment the mapping version, add the relationship or record the reference-model gap/unresolved classification, and rerun the substitution test across the full material set;
- only after the rerun may the paper issue a whole-controlled-object semantic-substitution verdict;
- if the discovery shows recurrent lossiness in the four-horizon × four-capability partition, route that evidence to **Validation Program 2**.

This closure rule prevents the reference model from defining the only universe against which its own completeness is judged.

#### Article §6.5 — Semantic substitution and practical preference

State two conclusions separately.

**Relationship-level semantic equivalence** is the gate. For each material relationship, define the required semantic properties before testing the substitute. Semantic equivalence exists only when the substitute preserves those properties for the same relevant scope and assumptions; different vocabulary or structure is acceptable. “Stronger” means the substitute preserves all required material semantics and adds a demonstrably stronger guarantee, coverage, assurance, or failure behavior for the same purpose. Trade-offs across dimensions are not evidence of dominance: where one property improves while another weakens, or scopes cannot be aligned, mark the comparison unresolved rather than compressing it into one stronger/weaker label.

For a material **economics/viability relationship**, semantic equivalence concerns the decision semantics: the accountable viability owner, the relevant cost/capacity/latency/burden input categories, the legitimate decision right, the available outcomes such as continue/narrow/redesign/defer/No-Go, and the reassessment trigger. A substitute may therefore be semantically equivalent even when its actual costs or operating burden are higher. Those measured or estimated values belong to the practical-preference comparison below.

**Whole-controlled-object semantic substitution** is established only when every material relationship in the exact mapping ID/version/snapshot passes that relationship-level test as equivalent or stronger. If that condition is met, the semantic integration gap is absent for the tested scope even if the substitute is more expensive, slower, or operationally heavier. Residual, unresolved, non-comparable, or untested material relationships prevent a whole-object substitution verdict.

**Practical preference** is a second decision. Among semantically adequate concrete operating compositions, compare material control overhead: lifecycle cost, latency, capacity demand, operational friction, Human Authority burden, maintenance burden, failure surface, and additional control work. Compare the existing composition with any proposed augmentation or replacement needed to close residual gaps. A semantically adequate composition with higher overhead remains a semantic substitute; it may simply be the less attractive implementation choice. If the existing composition is already semantically complete, no operational augmentation is required merely to instantiate the derived map; the map may still be used as an analytical/review lens without becoming a runtime, workflow, or document layer.

Apply the semantic-substitution test equally to conceptual, implementation, and organizational-practice substitutes; pure authority/obligation inputs alone do not qualify as substitutes, while an adopted and operated risk/management composition may qualify.

Define **conceptual overhead** separately as an **explanatory-economy criterion only**. It asks whether the paper's partition and vocabulary make the problem easier to reason about than an established alternative. An existing method that preserves the relationships with equal or lower conceptual overhead narrows the paper's explanatory contribution. Conceptual overhead does not determine semantic equivalence and does not overturn a practical-preference decision based on material control overhead.

If existing mechanisms preserve the material relationships credibly and keep them connected through operation, **they already implement the required control architecture; the paper should not claim a semantic gap merely because another composition is cheaper or easier to operate**. Practical economics determines which adequate operating composition to prefer, not whether the relationship is semantically present.

Do not repeat the **Article §5** carrier checklist or the three-result worked test from **Article §6.4**.

#### Article §6.6 — Known risks and drafting boundaries

Preserve these for drafting and external review:

- **Fast-moving tools:** recheck every named capability against current first-party documentation immediately before drafting and publication.
- **Category overlap:** integrated platforms span orchestration, enforcement, evaluation, identity, governance, and observability; classify functions rather than forcing one product into one category.
- **Selection bias:** a representative set cannot establish market-wide absence.
- **Comparison asymmetry:** methods, laws, standards, research, runtimes, and platforms have different purposes; coverage is not a common maturity score.
- **Reference-frame asymmetry:** translating everything into the paper's categories can hide concepts the map does not represent well; record lossiness as evidence against the partition and invoke the reverse-mapping closure rule before any whole-object verdict.
- **Semantic-equivalence ambiguity:** define the relationship-level equivalence basis before seeing a preferred substitute. Different vocabulary is acceptable, but scope/assumption mismatches, cross-dimensional trade-offs, or insufficient evidence produce an unresolved comparison rather than a convenient “stronger” verdict.
- **Snapshot/self-reference risk:** do not require the blueprint-owned mapping to contain the commit SHA of the file that contains that same SHA. Capture an immutable mapping snapshot in the verdict/test record after freeze; prefer a deterministic mapping-content digest when repository history may be rebased or squashed. Any material mapping change requires a version increment and retest.
- **Verdict-version drift:** every whole-object verdict must name the mapping ID/version and immutable snapshot tested. Mapping-version changes make the verdict stale for the new mapping until rerun; do not silently carry an old verdict forward.
- **Authority nuance:** governance products may encode decision rights, approvals, policy mappings, and integrations; distinguish recorded/delegated authority from the source that legitimizes it.
- **Guarantee nuance:** map the complete realized path; never label an entire product Hard or Soft.
- **Economics semantics:** preserve the semantics of a material viability decision separately from the numerical control burden. Different cost/latency/staffing values affect practical preference; they do not by themselves create or close a semantic gap.
- **Overhead-semantics risk:** do not let material control overhead decide whether semantic substitution exists. Semantic equivalence closes the semantic integration gap for the tested scope; material control overhead decides practical preference among semantically adequate concrete operating compositions; conceptual overhead only narrows explanatory contribution.
- **Layer-reification risk:** use of the derived map as an analytical or review lens is not itself an operational layer. Compare concrete existing/augmented/replacement operating compositions rather than assuming UA-specific runtime, workflow, or document machinery must be added.
- **Novelty risk:** do not claim first, unique, exhaustive coverage, or universal absence without systematic evidence.
- **Length risk:** keep volatile product detail in source notes. The manuscript needs a compact approach-class comparison, one required matrix-or-figure representation, one support-system substitution result, and reverse mapping—not a market catalog.
- **Duplication risk:** do not reteach the capability anatomy, horizons, Human Authority, Hard/Soft, baseline reconstructability, fallback credibility, or reassessment semantics already established in **Article §§3–4**.

**Alternative required representation — Adjacent approaches and compositions around the derived map:**

If a coverage-band figure is chosen instead of the compact matrix, show approach classes around the already established decision-horizon × capability-family map. Use brackets or shaded regions—not causal execution arrows, product logos, checkmark marketing, or numerical scores. Include reverse-mapping notation or an explicit question indicating that adjacent approaches can reveal lossiness in the reference model. Do not publish both representations unless each passes the additive-information test.

Caption requirement for the figure alternative:

> **Adjacent approaches tested against the derived operating map. Coverage indicates where an approach may contribute capability, obligation, evidence, decision support, or implementation. It does not imply inferiority, exclusivity, or that the reference model implements those functions. Reverse mapping asks what the reference model itself loses.**

**Repository anchors:**

- [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
- [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
- [`AI Control Plane`](../../../02-ai-control-plane/README.md)
- [`Specification`](../../../SPECIFICATION.md)
- [`Research Track`](../index.md)

**Transition:** After application and substitution analysis, the paper can formally delimit the relationship between its research synthesis and the open draft UA specification boundary defined and indexed by `SPECIFICATION.md`. The next section should not introduce a new layer or repeat the landscape; it should state precisely what the specification already organizes, which additions remain paper-level hypotheses, what neither surface owns, and what maturity can honestly be claimed.

**Closing claims:**

> Existing approaches solve many parts of the control problem. The comparison tests whether a material unresolved semantic problem lies in the connections among their normal scopes—or whether an existing method or composition already carries those connections.

> If an existing composition semantically preserves every material relationship under the defined equivalence basis, including the semantics of any material viability decision without conflating those semantics with numerical burden, the derived map should recognize that result; material control overhead then determines which semantically adequate operating composition is practically preferable.

**Working word budget:** 1,250–1,650

---

### Article §7 — Situating and Delimiting the Research Synthesis Relative to Uncertainty Architecture

**Purpose:** Formally situate and delimit the research synthesis already derived, applied, and challenged in the preceding sections relative to the existing open draft Uncertainty Architecture specification. The section explains what `SPECIFICATION.md` defines and indexes as the specification boundary, how each indexed document contributes only within its declared status and scope, which additions remain paper-only hypotheses, what neither surface owns, how both relate to the repository and antecedent traditions, and what maturity can honestly be claimed.

**Core claim:** **`SPECIFICATION.md` is the canonical owner of the Uncertainty Architecture specification boundary and document-status model.** It defines and indexes the current open draft specification; each indexed document acts only within its declared status and scope. This research paper proposes and tests a publication-facing synthesis that composes current specification constructs with carrier-sufficiency, semantic-substitution, reverse-mapping, integration-gap, and validation questions. Paper-only extensions remain research unless explicit framework review accepts or narrows them and a corresponding status-bearing change translates them into the specification. Rejection or supersession is recorded in the owning research/traceability surface without enlarging the specification.

**Reveal correction:**

The publication title and abstract already identify Uncertainty Architecture for attribution, and **Article §4** may refer to “UA forms” when rejecting mandatory artifacts. Therefore this section must not pretend to reveal the name for the first time. Its job is to **formally delimit the relationship between the specification boundary defined/indexed by `SPECIFICATION.md` and the paper's research synthesis, and expose the maturity boundary of each** without using the named framework as the premise of the earlier engineering deduction.

**Do not reteach the operating map:**

**Article §§1–6** already establish:

- the category and whole-system controlled object;
- the capability anatomy, Hard/Soft, and Human Authority;
- the four decision horizons and invalidated-decision-basis routing;
- full-map-before-depth proportionality;
- carrier sufficiency and artifact/tool neutrality;
- landscape substitution and reverse mapping;
- negative-case learning/stabilization as a hypothesis under validation.

Refer back. Do not repeat the definitions, four horizon descriptions, landscape categories, carrier checklist, or learning loop.

#### Article §7.1 — Required argument sequence

**1. State the existing UA identity and specification boundary.**

Explain **Uncertainty Architecture** as the repository's existing open draft specification for locating, bounding, observing, deciding about, correcting, and reassessing consequential uncertainty produced by a software Thinking System through a socio-technical control architecture. **`SPECIFICATION.md` defines and indexes that boundary.** The documents it indexes contribute only according to their own declared status and scope; no generic phrase such as “status-bearing modules” becomes a second boundary owner. The name describes the reference problem and relationships; it does not claim that uncertainty can be eliminated, and it does not automatically name or absorb the paper-only extensions that the next step proposes.

**2. State the paper's proposed integration contribution precisely.**

This paper proposes one explicit composition model connecting:

- Thinking-System classification and the whole controlled object;
- capability functions without treating them as products, layers, or one execution sequence;
- decision ownership without turning horizons into departments or a delivery waterfall;
- authority, decision rights, and Constraints flowing downward by reference while scoped realizations become concrete, with realization/operation evidence routed upward to the owning decision basis;
- complete realized-path Hard/Soft semantics;
- substantive Human Authority and complete control-perimeter economics as architecture/viability concerns;
- proportional implementation through credible existing carriers;
- relationship-level semantic equivalence, whole-object semantic substitution, practical-preference separation, and reverse mapping when an existing method or composition already carries the relationships.

This is the paper's **synthesis claim**, not a claim that the individual concepts are novel or uniquely owned by UA and not an implicit enlargement of the specification boundary defined by `SPECIFICATION.md`.

**3. Delimit what UA is and is not.**

Prefer a compact publication-facing table:

| UA and the paper's relationship to it | UA and the paper are not |
|---|---|
| an open draft specification whose boundary is defined and indexed by `SPECIFICATION.md`; each indexed document contributes only within its declared status and scope | a runtime product, SDK, agent framework, or managed platform |
| a vocabulary for connected controlled-object, capability, authority, evidence, action, and reassessment relationships | ownership of control theory, systems safety, runtime assurance, orchestration, guardrails, evaluation, observability, governance, or AI risk management |
| a draft specification that equivalent existing records and platforms may implement within current conformance semantics | a mandatory artifact package, department structure, ceremony, or implementation topology |
| a framework accompanied by research surfaces that may challenge, narrow, or propose additions to it | a scored claim that UA “covers more” than concrete methods and tools, or proof of maturity, uniqueness, or empirical effectiveness |
| a subject of this paper's carrier, substitution, reverse-mapping, and validation hypotheses | automatic specification authority for those hypotheses before explicit framework acceptance |

**4. Separate specification boundary from research hypotheses.**

Describe repository authority by each document's declared status and scope while keeping `SPECIFICATION.md` as the canonical boundary/index owner. Doctrine, patterns, capabilities, Control Plane guidance, and the failure-mode taxonomy may carry normative weight only where their own status/scope and the `SPECIFICATION.md` index say they do. Reference architectures, reference compositions, worked examples, and templates are supporting or optional surfaces unless their own status says otherwise. Provenance and framework traceability remain research. Do not imply that a reference composition is proof of conformance or a mandatory architecture.

The article additionally proposes or tests publication-facing claims that must remain visibly under validation:

- whether the selected combination is useful and sufficiently complete as one map;
- whether the four horizons × four capability families partition remains usable and non-lossy across domains;
- whether the cross-boundary integration gap is material after serious semantic-substitution analysis;
- whether the relationship-level semantic-equivalence rule is usable without hiding scope/assumption differences, cross-dimensional trade-offs, or the distinction between viability-decision semantics and actual operating burden;
- whether semantically adequate existing compositions remain preferable or unattractive once material control overhead is considered separately;
- whether carrier sufficiency, the materiality rule, and proportionality can be applied independently without either overbuilding or hiding material relationships;
- whether the negative-case learning/stabilization discipline reduces uncontrolled recurrence in practice.

Do not promote these research hypotheses into normative doctrine merely because they appear in the paper. Contradictory or supporting evidence first updates the owning research, traceability, artifact, or framework-decision surface. A specification change occurs only when explicit framework review accepts, narrows, or translates a result into the appropriate `SPECIFICATION.md`-indexed status-bearing document; rejection or supersession remains recorded in the owning research/traceability surface unless a separate accepted specification change is required.

**5. Explain artifact and tool neutrality once.**

Existing tools, standards, governance systems, architecture records, delivery workflows, evaluation/observability stores, runtime controls, and incident processes may carry all or part of the current specification relationships. UA is not an obligatory runtime layer. The paper's research substitution test treats a method or composition as a semantic substitute only after each material relationship passes the defined equivalence basis under the same relevant scope and assumptions; material control overhead is assessed separately across concrete operating compositions to decide practical preference. Use of the derived map as an analytical/review lens does not itself create an implementation layer or mandatory document set. Do not present either paper-level test as part of status-bearing UA conformance semantics until a corresponding framework decision and status-bearing change say so.

Removing the two-review and `K-SEND-01` sections from the publication does not deprecate those repository patterns. It keeps the paper focused on the durable map while concrete artifacts remain available for worked applications and implementation guidance.

**6. Define maturity and publication identity.**

Present the paper as an **open engineering working paper / architecture map under validation**. Repository rigor supports internal consistency and traceability; it does not establish independent usability, empirical effectiveness, completeness, or unique landscape position. Avoid vendor-whitepaper tone and framework-advertisement language.

State the main maturity limits once here rather than repeating them as a second disclaimer in **Article §8**:

- independent real-team use, usability, time-to-apply, and decision-quality effects remain unvalidated;
- control-cost, substantive Human Authority capacity, and context-specific threshold-selection methods remain immature;
- practical methods for correlating the material active behavioral/control baseline across release/runtime evidence remain open operational work; the paper requires reconstructability where material but does not prescribe one universal registry;
- fallback/recovery independence, common-mode resilience, capacity, transition, and restoration patterns remain to be validated across consequence and latency profiles;
- evaluator/Golden Set/rubric/threshold/human-review-signal lifecycle validity, calibration, recalibration, and replacement methods remain open operational work;
- relationship-level semantic-equivalence judgments and whole-object substitution remain unvalidated research methods, including how independent teams handle scope mismatch, trade-offs, non-comparable semantics, viability-decision semantics, and immutable mapping-snapshot identification;
- the negative-case learning/stabilization discipline remains an unvalidated research proposal;
- current artifacts, terminology, horizon/capability partition, and landscape-gap claim are not proven optimal, sufficient, durable, or unique;
- systematic evidence does not support “first,” “unique,” or exhaustive absence claims.

#### Article §7.2 — Intellectual continuity and provenance

Use one compact attribution paragraph or note, not a second landscape survey.

State that UA is a synthesis and recomposition drawing continuity from:

- systems-theoretic and socio-technical safety traditions such as STAMP/STPA;
- runtime-assurance architectures such as Simplex;
- control-theoretic work on stochastic/model-mediated systems;
- production ML and software engineering for AI;
- AI risk-management and management-system approaches such as NIST AI RMF;
- ordinary architecture, delivery, operations, security, incident, and governance practice.

Refer back to **Article §6** for functional comparison. Do not redescribe each method here, imply direct derivation or endorsement, or claim UA invented closed-loop control, Constraints, Sensors, Controllers, Actuators, fallback, socio-technical control, Human Authority, orchestration, guardrails, observability, governance, or the broader SE-for-AI problem.

State that UA does not claim coinage of the phrase **Thinking Systems**; its claim is the paper's engineering definition and the responsibility boundary assigned to it.

Use **proposed contribution**, **synthesis**, or **recomposition** rather than “first,” “only,” “unique,” or “unprecedented” unless later systematic evidence supports a stronger statement.

#### Article §7.3 — Repository relationship

Compress the repository inventory into three groups:

1. **Specification boundary and indexed engineering surfaces** — `SPECIFICATION.md` defines/indexes the specification boundary and conformance/document-status model; the definitions, controlled object, capability anatomy, nested lifecycle, Requirements/Constraints/Correctness, Human Authority, patterns, capabilities, Control Plane guidance, and failure-mode taxonomy that it indexes are interpreted only according to each document's declared status and scope.
2. **Supporting and reference surfaces** — reference architectures, reference compositions, templates, and worked examples that illustrate implementation without becoming conformance requirements.
3. **Research and validation surfaces** — provenance, framework traceability, open issues, independent applications, and future evidence.

The article may link to representative entry points. It must not make the current repository shape the test for whether the conceptual synthesis is valid.

#### Article §7.4 — Running-example callback

Use no new scenario mechanics. In one paragraph, observe that the support-resolution case has already been viewed through:

```text
one controlled object
+ four capability functions
+ four decision horizons
+ external implementation/authority surfaces
+ proportional carrier choices
+ substitution questions
```

Relating the paper's synthesis to the UA specification does not add another control layer to that system. The constructed example demonstrates narrative continuity only; it validates neither the specification nor the paper-only hypotheses.

**Optional Article §7 boundary/composition architectural anchor:**

If retained, this representation must add a relationship not already present in Figures 8–9. Publication numbering is assigned only during integrated manuscript editing. Do **not** call it “Primary Figure 3” or redraw the full four-horizon × four-capability operating map or create an eight-box pipeline.

Show the already established **`SPECIFICATION.md`-defined/indexed specification boundary** and the paper's research synthesis as related but distinct surfaces, while keeping external authority directed at the controlled object rather than at the specification:

```text
external authority / obligation sources
            ↓ constrain or authorize
controlled object and legitimate decision scope

SPECIFICATION.md-defined/indexed UA specification boundary
            ↓ interpreted and composed by
publication-facing research synthesis under test
            → applied to and challenged against the controlled object
            ↔ implemented or substituted through existing methods, records, platforms, and tools
            ↔ challenged by reverse mapping and independent evidence
            ↓ record result in research / traceability / owning artifact
explicit framework decision
            ↓ only if accepted
corresponding status-bearing specification change
```

The figure should make clear:

- `SPECIFICATION.md` owns the boundary/index; each indexed status-bearing UA document owns only the relationships and vocabulary within its declared scope, not external laws, standards, methods, platforms, organizational authority, or paper-only research hypotheses;
- external approaches may implement capabilities more concretely or carry semantics UA lacks;
- proportional carriers are implementation surfaces, not children or mandatory UA nodes;
- the proposed negative-case learning/stabilization discipline and integration-gap claim remain visually marked as under validation if shown.

If this boundary/composition relationship is clearer in a compact `UA is / UA is not` table, the table may replace the visual. A third architectural anchor is an editorial option, not a requirement to add a redundant diagram.

**Repository anchors:**

- [`README.md`](../../../README.md)
- [`SPECIFICATION.md`](../../../SPECIFICATION.md)
- [`ROADMAP.md`](../../../ROADMAP.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)
- [`Research Track`](../index.md)

**Transition:** A formally delimited synthesis and a plausible landscape position are not validation. The final section must state which evidence would force the map to change, become smaller, split a category, demote a claim, accept substitution, or reject an operating hypothesis.

**Closing claim:**

> `SPECIFICATION.md` defines and indexes the current UA specification boundary; this paper's broader composition remains a testable research synthesis, not proof that every boundary, partition, artifact, operating hypothesis, or claimed landscape gap is already right.

**Working word budget:** 800–1,050

---

### Article §8 — Validation Agenda — What Evidence Should Change the Map

**Purpose:** Close the paper as a working paper rather than a framework advertisement. Convert current maturity limits into a small set of falsifiable programs that specify which evidence would revise, split, simplify, demote, substitute, or reject parts of the proposed synthesis.

**Core claim:** The next meaningful progress is not another layer of conceptual polish. It is independent evidence showing where the map is incomplete, too heavy, too weak, incorrectly partitioned, already solved more simply, or difficult to apply without the author.

**Inherited maturity boundary and validation objects:**

**Article §7** already distinguishes the UA specification boundary from the paper's research synthesis and distinguishes repository rigor from independent evidence. Do not repeat the full maturity disclaimer here. Begin with one bridge sentence, then distinguish:

- validation of the conceptual map;
- validation of particular repository artifacts or templates;
- validation of the proposed negative-case learning discipline;
- correctness of the current landscape mapping and integration-gap hypothesis.

These are different evidence questions.

#### Article §8.1 — Six validation programs

Organize the section around six programs rather than a catalogue of twenty-one loosely connected questions. For each program, state:

```text
claim being tested
→ evidence that would contradict or narrow it
→ which research, traceability, artifact, or framework-decision surface owns the response
→ explicit framework review before any status-bearing specification change
```

| Validation program | Claim being tested | Contradictory or narrowing evidence | Owning response before any specification change |
|---|---|---|---|
| **1. Category and controlled-object boundary** | Consequential Runtime Responsibility + probabilistic Model Judgment identifies a useful engineering class, the whole software Thinking System is the useful controlled object, and the surrounding control perimeter is correctly treated as socio-technical | systematic over/under-classification, inability to distinguish material from trivial model use, domains where a different object yields clearer decisions, or evidence that the controlled-process/control-architecture boundary is placed incorrectly | record the result in research/traceability; propose a narrower/replaced test or controlled-object rule; change doctrine only through explicit framework acceptance |
| **2. Structural sufficiency and reverse-mapping lossiness** | four decision horizons × four capability families plus the versioned material-relationship mapping preserve the material control relationships without forcing false one-to-one mappings or defining their own completeness universe | recurrent missing decision surfaces, capability functions that do not fit, reverse mapping repeatedly discovers material relationships absent from the current map, or important STAMP/STPA, Simplex, platform, governance, or domain concepts are lost in translation | stop affected whole-object substitution verdicts, version/revise the working mapping and comparison record, propose add/split/merge/demote or another partition, and change the appropriate `SPECIFICATION.md`-indexed status-bearing document(s) only if explicit framework review accepts the result |
| **3. Guarantee, evidence, authority, and reassessment semantics** | complete-path Hard/Soft claims, evidence-instrument validity for the decisions supported, active-baseline reconstructability where material, fallback/recovery credibility, substantive Human Authority, Controller/Actuator separation, and invalidated-decision-basis routing improve clarity and operability | teams cannot apply one or more distinctions consistently; material incidents cannot be reconstructed against the actual active source/authorization/configuration baseline; fallback shares the primary failure/common dependencies, lacks capacity, or cannot restore an authorized state; evaluators/Golden Sets/rubrics/thresholds/human-review signals lose validity without usable detection or recalibration; evidence cannot be routed to a credible owner; automation/Human Authority boundaries or reassessment ownership create systematic ambiguity, excessive escalation, or failures outside the proposed control anatomy | route each failed subclaim to its owning doctrine/pattern/research decision; revise semantics, evidence lifecycle, routing, authority, or ownership only through the applicable explicit framework decision and status-bearing change |
| **4. Proportionality, carrier sufficiency, usability, and economics** | independent teams can inspect the full map, apply the pre-substitution materiality rule, select the lightest credible carriers, preserve the approved operating contract and other material relationships, and estimate enough control-perimeter cost to make earlier architecture decisions | low-consequence systems are routinely overbuilt, materiality cannot be judged consistently before seeing a carrier/substitute, material relationships disappear into “existing tools,” authority-delta comparisons cannot be separated from lifecycle maturity, or cost/Human Authority/capacity cannot be assessed early enough to affect design | revise the paper's application method and evidence record; propose pattern/specification changes separately if the result warrants them |
| **5. Negative-case learning and stabilization effect** | **given a correctly identified owning decision basis under the current lifecycle semantics**, structured diagnosis of a material negative case and improvement of the weakest control element reduces uncontrolled recurrence more effectively than model-only correction or generic incident closure | no improvement, slower recovery, greater recurrence, perverse incentives, unnecessary control churn, or a simpler learning/stabilization method performs better | revise, narrow, or reject **only the paper's learning/stabilization discipline and effect claim**; do not prejudge the lifecycle structure from Program 5 evidence and do not imply a doctrine change without explicit review |
| **6. Semantic substitution, integration-gap, and practical-preference hypothesis** | within predefined target classes and boundary conditions, the frozen relationship-level equivalence basis can determine whether existing methods/compositions leave a recurring **semantic** gap across operating contract, scope, authority, guarantee, evidence, action, verification, reassessment, and viability-decision semantics; when no semantic gap remains, material control overhead separately differentiates concrete operating compositions | evidence that existing methods/compositions preserve every required semantic property for every material relationship under the same relevant scope/assumptions—including the owner, inputs, decision right, outcomes, and reassessment of any material viability decision—rejects or narrows the semantic integration-gap claim for the tested class **regardless of actual overhead**; frequent unresolved/non-comparable verdicts, scope-mismatch disputes, snapshot-identification failures, or inability of independent reviewers to reproduce equivalence judgments narrows the substitution method itself; material-control-overhead evidence separately determines practical preference | separate the response: revise/reject/narrow the integration-gap and contribution claim whenever semantic equivalence is demonstrated; revise the equivalence/snapshot method if independent reproducibility or comparability fails; record actual cost/latency/capacity/Human-Authority and other material-control-overhead results separately as practical-preference evidence; propose specification simplification only if an explicit framework decision accepts a specification consequence |

**Cross-program routing rule:** Program 5 begins only after the case has a credible owning decision basis under the current lifecycle semantics. Evidence that cases **cannot be routed cleanly**, repeatedly escalate because ownership is ambiguous, or expose reassessment failures belongs to **Program 3**. Evidence that important failures or relationships sit outside the proposed control anatomy belongs to **Program 2**. Program 5 tests the **learning/stabilization effect after routing**, not whether the lifecycle or anatomy is correct. It must not preserve or reject those structures by fiat.

Cross-domain durability and independent usability should be tested across these programs rather than becoming separate catch-all questions. Before each study, define the target class, boundary conditions, independent sample, observable success/failure criteria, and the decision rule for supporting, narrowing, demoting, or rejecting each subclaim. Where a claim depends on competent application, predefine practitioner competence and application-fidelity criteria so results cannot be dismissed post hoc. Any row that groups subclaims does so only for editorial economy; register and evaluate those subclaims separately wherever different evidence would require different responses.

#### Article §8.2 — Evidence requested

Request evidence capable of changing the map, including:

- independent documented or anonymized applications across different organizations and domains;
- examples where the category test or controlled-object boundary classified the engineering problem incorrectly;
- Organizational review traces involving changed authoritative sources, reserved/delegated decision rights, exception authority, shared capabilities, or cross-project evidence;
- project authorization, delivery/release, runtime correction, Project Reauthorization, and Organizational review traces;
- Constraint/realization cases where a claimed Hard boundary failed, was bypassable, or proved impossible to realize;
- release/runtime/incident records showing whether material source, Project, Delivery, realization, model/prompt-instruction/context-retrieval/tool-routing/evaluator-policy/deployment/fallback state could be correlated well enough to reconstruct the active behavioral/control baseline without relying on a new mandatory registry;
- incidents where monitoring detected a problem but fallback/containment/recovery failed, including common-mode/shared-dependency failures, insufficient fallback capacity or latency, transition failure, and inability to restore a known authorized state;
- cases where evaluators, Golden Sets, rubrics, thresholds, or structured human-review signals lost validity after a model, population, policy, data-distribution, or operating-condition change, including how versioning, calibration/validation, validity-loss detection, incident ingestion, recalibration, replacement, or changed decision use was handled;
- Sensor blind spots, misrouted evidence, Controller authority failures, ineffective Actuators, failed post-action verification, Human Authority overload, and automation/common-mode failures;
- examples where a supposedly simple case revealed hidden authority, evidence, fallback, dependency, or economics complexity;
- examples where the map clearly overbuilt a low-consequence case or where an existing carrier preserved the relationship more simply;
- examples where independent teams could or could not apply the pre-substitution materiality rule consistently, including relationships discovered only by reverse mapping;
- examples showing that authority/scope differences can or cannot be distinguished cleanly from lifecycle maturity in comparative application;
- control-cost, latency, capacity, false-block, fallback, and maintenance observations;
- negative-case learning traces showing improvement, no improvement, or perverse effects after the owning decision basis was correctly identified;
- contradictory cases that do not route cleanly to the proposed owning horizon—these belong to Program 3 rather than being counted as Program 5 learning failures;
- reverse mappings showing useful concepts or material relationships lost when an adjacent method is translated into the paper's partition, including discoveries that force a mapping-version increment and substitution rerun;
- independent duplicate substitution assessments against the same mapping ID/version/immutable snapshot, including disagreements about scope alignment, equivalence, stronger semantics, viability-decision semantics, or non-comparability;
- corrections from tool/framework maintainers demonstrating understated current capability or authority semantics;
- examples where an existing method, standard, platform composition, or organizational practice is a semantic substitute even when its actual material control overhead is higher, together with separate observations comparing concrete operating compositions when equal/lower overhead changes practical preference;
- evidence showing whether historical whole-object verdicts remain reproducible when the exact mapping ID/version/immutable snapshot is retained and whether mapping-version changes correctly force a rerun instead of silently inheriting the old verdict;
- independent usability evidence showing where terminology or application fails without author involvement.

Do not ask only for successful case studies. Failure, substitution, redundancy, and safe deletion are first-class results.

#### Article §8.3 — Running-example evidentiary boundary

State explicitly:

> The support-resolution example is editorially constructed. It demonstrates continuity of explanation; it cannot validate the category, operating map, proportionality method, landscape gap, or Uncertainty Architecture.

Use the case only to formulate transfer questions:

- Can another team find a responsibility the example made visible but its own process missed?
- Can it safely remove a control or artifact the example made explicit?
- Can it route evidence to the correct owner without author guidance?
- Can it reconstruct the material active authorization/configuration baseline after an incident using its existing records?
- Can it demonstrate that fallback is sufficiently independent, available, and restorable for the failure it is meant to contain?
- Can two independent teams using the same mapping ID/version/immutable snapshot reach a reproducible relationship-level semantic-equivalence verdict, including an explicit unresolved result when dimensions trade off and a viability-equivalent result when only the numerical burden differs?
- Can it show that its existing stack already preserves the material relationships semantically without requiring an additional operating layer, even if another concrete composition would be cheaper or easier to operate?
- Which example-specific assumptions fail in another domain?

Do not add a new support-system narrative in the final section.

#### Article §8.4 — Open revision and invitation

Invite reviewers to identify one concrete decision, boundary, evidence path, control obligation, substitution, or landscape claim that is placed incorrectly—or one part that can be safely removed. Explicitly welcome:

> Our existing method or stack already solves this more simply.

The desired outcome is a research synthesis that becomes smaller where evidence permits and more explicit where evidence demands it. The specification changes only where a separate framework decision accepts the result into the correct `SPECIFICATION.md`-indexed status-bearing surface.

**Why open:** enable independent critique and contradictory evidence, compare applications across domains, prevent vendor or author capture of the language, preserve visible evolution, and support multiple implementations.

**Licensing:** Documentation and specification material use CC BY 4.0; code and reference implementations use Apache 2.0 where present.

**Final representation:** Prefer a compact table or callout using:

```text
hypothesis
→ independent application / substitution / failure evidence
→ contradiction or support
→ record in the owning research / traceability / artifact / framework-decision surface
→ explicit accept / narrow / reject / supersede decision
→ update the owning surface or surfaces named by that program
→ include a status-bearing specification change only if explicit framework review accepts one
→ update the landscape mapping only where the evidence concerns that mapping
```

Do not add a final Mermaid diagram by default. Figure 15 already visualizes cross-level learning; another loop is justified only if it adds a distinct specification-revision relationship that prose or the validation table cannot show. Do not end with a sales funnel or product CTA.

**Repository anchors:**

- [`ROADMAP.md`](../../../ROADMAP.md)
- [`Research Track`](../index.md)
- [`Framework Traceability`](../framework-traceability.md)
- [`CONTRIBUTING.md`](../../../CONTRIBUTING.md)

**Closing claim:**

> The map is useful only if it survives contact with systems, methods, and tools it did not design. The next version should be shaped by evidence showing what is missing, unnecessary, already solved elsewhere, or wrong.

**Working word budget:** 1,150–1,450

## 6. Figure contract

The manuscript already contains fifteen figures through **Article §4**. Future sections must pass an **additive-information test**: a new figure is justified only when it shows a relationship that the existing figure sequence, a compact table, or prose cannot show clearly. Framework completeness is not measured by diagram count.

The architectural figure hierarchy is:

1. **Architectural anchor A — Figure 3: Controlled-object shift** — already established in **Article §2**: two responsibility diagrams placed side by side; the Thinking-System side highlights only the Judgment Node(s) where probabilistic Model Judgment changes the responsibility structure. The figure is descriptive of category membership, not a target production control architecture.
2. **Architectural anchor B — Figure 9: Two orthogonal models** — already established in **Article §4**: the decision side reproduces the four-horizon decision model, including reassessment evidence from Delivery realization or Runtime operation and the same direct return routes, while a visually distinct capability-family side shows Actuators, Constraints and realizations, Sensors and evidence, and Controllers and decision authority as functions that may appear at every horizon. Ordering is a reading aid, not an execution pipeline or one-to-one mapping.
3. **Architectural anchor C — optional Article §7 boundary/composition representation** — planned only if it adds information beyond Figure 9. It should show the relationship among the already derived operating map, external authority/obligation sources, existing implementation surfaces, substitution/reverse mapping, the `SPECIFICATION.md`-defined/indexed specification boundary, and evidence-driven revision. It must not redraw the complete map, turn tools/standards into children owned by UA, or create a fourth architecture model. A compact `UA is / UA is not` table may replace the figure if clearer; publication numbering is deferred until manuscript integration.

Figures already established through **Article §4**:

- Figure 1 — engineering responses around dominant uncertainty;
- Figure 2 — Thinking-System category boundary;
- Figure 3 — controlled-object shift;
- Figure 4 — Model Judgment placement;
- Figure 5 — connected uncertainty locations;
- Figure 6 — closed feedback loop;
- Figure 7 — complete bounded control architecture;
- Figure 8 — one controlled object across four decision horizons, including Delivery-realization and Runtime-operation evidence feeding direct reassessment;
- Figure 9 — the two orthogonal models;
- Figure 10 — organizational control process;
- Figure 11 — project control architecture and viability;
- Figure 12 — delivery translation and release loop;
- Figure 13 — runtime control and reassessment;
- Figure 14 — evidence and change routing;
- Figure 15 — cross-level learning and stabilization, clearly labeled proposed under validation.

Do not recreate these models in later sections merely to remind the reader. Reference them by their actual number and, where useful in source text, by a stable descriptive anchor name.

**Default future visual plan:**

- **Article §5:** use the lower-/higher-authority running-example comparison table plus one clearly labeled publication excerpt from the complete canonical material-relationship-to-carrier working mapping. A figure may replace that excerpt only if it carries the same relationships more clearly; do not add a third representation or redraw the full map.
- **Article §6:** use one approach-class landscape matrix or coverage-band figure. Include substitution and reverse mapping; avoid product logos, causal arrows, numerical scores, and red/green maturity signaling.
- **Article §7:** use the boundary/composition figure or the `UA is / UA is not` table, not both unless each contributes distinct information.
- **Article §8:** use the validation-program table and a compact final callout. Do not add another loop diagram by default because Figure 15 already carries the cross-level learning relationship.

All figures and tables must:

- materially strengthen comprehension;
- introduce no doctrine absent from owning repository sources;
- remain consistent with all earlier figures;
- preserve the orthogonality of decision horizons and capability families;
- distinguish external authority sources, implementation surfaces, evidence, decision ownership, action, and revision where material;
- avoid implying mandatory products, services, teams, departments, committees, roles, artifact sets, or execution pipelines;
- carry captions stating important scope, representative-tendency, and non-prescriptive boundaries;
- be renumbered and reread as one visual system after the complete manuscript exists.

Do not use the presentation's brain/nerves/skeleton/muscles stack as the canonical article architecture diagram. It may be mentioned as source history only.

## 7. Terminology and claim-safety rules

Use current terms: Thinking System, Linear Software, Model Judgment, Judgment Node, Constraint, Constraint Realization, Hard Constraint, Soft Constraint, Sensor, Controller, Actuator, Human Authority, Project Constraint Architecture, Constraint Realization Map, Nested Control Lifecycle, Project Authorization, Project Reauthorization, DoR, DoD, and Release Gate.

Treat Behavioral Software, Behavioral Applications, fixed specialist role titles, universal maturity ladders, universal thresholds, and the old three-part Actuator/Sensor/Controller model as historical or contextual only.

Do not:

- equate Thinking Systems with agentic applications;
- imply that fixed, sequential, or explicitly orchestrated workflows cannot be Thinking Systems when at least one **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment;
- use an agent label, dynamic control flow, autonomy level, or existing control completeness as a substitute for the Thinking System category test;
- imply that a poorly controlled or pre-production system is not a Thinking System merely because Constraints, evidence, decision rights, or corrective mechanisms are incomplete;
- imply that **Thinking** asserts consciousness, sentience, human-like cognition, or an anthropomorphic theory of model behavior;
- imply that the Thinking System category begins only after agentic, multi-agent, dynamic, or high-autonomy capabilities appear;
- imply that a non-agentic application cannot be a Thinking System;
- call a prompt, natural-language policy, probabilistic evaluator, classifier, or model preference a Hard Constraint by itself;
- call a schema, permission check, or other realization a Constraint without distinguishing the authoritative Constraint from its realization;
- describe an organizationally important prohibition as Hard unless the complete scoped realized path actually supports the deterministic claim;
- describe Actuators as defining policy or authorizing their own changes;
- collapse evaluator, gate decision, and release execution;
- assume an evaluator, Golden Set, rubric, threshold, or human-review signal remains a valid Sensor after material model, population, policy, data-distribution, or operating-condition change without a maintained validity/calibration basis;
- equate Controller with a team, a dashboard, or an algorithm; Controller means the decision function and legitimate authority, which may be socio-technical and partially automated;
- imply that automation creates authority that was not delegated;
- imply that automation is automatically safer, cheaper, or simpler than a human or socio-technical path;
- equate closed feedback with acceptable bounded operation;
- describe governance as a post-hoc review, policy document, compliance artifact, fifth capability family, or exact synonym for every element of the control architecture;
- imply that governance can become operational without the relevant socio-technical control architecture;
- imply that a Thinking System can be ready for production at the intended scope while a material control responsibility remains unowned, unrealized, insufficiently evidenced for its decision, or without a credible corrective or reassessment path; do not interpret “complete control architecture” as maximal instantiation of every map cell;
- imply that control-architecture design creates a fifth decision level separate from project / architecture;
- use red visual emphasis in the controlled-object figure anywhere except the Judgment Node(s) in a way that could imply surrounding deterministic responsibilities are part of the category change or that the entire Thinking System is probabilistic, unsafe, or erroneous;
- imply runtime reauthorizes a project automatically;
- allow a Delivery or Release Gate path to bypass Project Reauthorization when delivery evidence challenges Project Authorization merely because an organizational boundary may ultimately be involved;
- classify every negative case or deviation as a Bug;
- describe aggregate quality, cost, latency, or capacity tolerances as Hard Constraints without deterministic enforcement;
- imply that every negative case must escalate to Organization; route by invalidated decision basis;
- imply that every negative case is a model-quality failure; analyze the complete control architecture;
- use “measure everything” as a literal requirement; material evidence must be tied to decision ownership and latency;
- imply that listing independent component versions is enough when material evidence cannot be correlated to the active authorization/configuration baseline;
- create or imply a mandatory universal behavioral-configuration registry merely because material baseline reconstructability is required;
- treat fallback as safe, independent, available, or restorable merely because a secondary path exists;
- imply that the full map must be instantiated at maximum depth for every Thinking System; use proportionality while still inspecting the full map for hidden complexity;
- treat a simple UI, one model call, or one feature as proof that the control problem is simple;
- present the proposed cross-level negative-case learning/stabilization discipline as already validated or normative UA doctrine;
- present the two-living-review pattern, `K-SEND-01`, or any one repository template as the definition of UA or as independently validated proof of the map;
- imply that removing a repository artifact from the publication structure deprecates the artifact itself;
- use internal UA documents as evidence for current external standards, laws, products, or market practice;
- introduce UA as the premise that validates the early engineering argument;
- claim that UA invented generic control-loop primitives, systems-theoretic safety, runtime assurance, ML-systems engineering, AI risk management, agent orchestration, guardrails, observability, evaluation, human approval, or governance;
- claim that UA coined the phrase **Thinking Systems** itself rather than defining a specific engineering meaning for it;
- present STAMP/STPA, Simplex, NIST AI RMF, ISO standards, regulation, or other antecedents as equivalent to UA, endorsements of UA, or evidence that UA is uniquely correct;
- say or imply that **no existing framework spans the full problem** as an absolute fact without systematic evidence;
- say that UA is the **first**, **only**, **unprecedented**, or categorically more rigorous than all public alternatives without evidence sufficient for such a claim;
- call agent/orchestration frameworks “mere plumbing” or say they ignore control; describe their actual implementation scope and then separate it from authority/viability;
- say guardrails are “only filters” or only Sensors; modern guardrail systems may span realization, sensing, local decision logic, and Actuation;
- say observability/evaluation tools “only observe”; some include automated evaluation, alerts, rules, routing, or guardrail integrations;
- say managed AI platforms or governance suites “cannot solve governance”; state the narrower boundary between implemented/delegated control and the source of legitimate authority;
- say governance platforms are categorically disconnected from runtime; verify integration claims against current first-party documentation;
- say NIST AI RMF, ISO/IEC 42001, or the EU AI Act is detached from engineering; distinguish management/authority/obligation scope from application-specific control realization;
- treat law, standards, platforms, research papers, and open-source runtimes as if they were competing products with one common maturity score;
- label an entire product Hard or Soft; Hard/Soft is a scoped claim about a Constraint and complete realized path;
- infer market-wide absence from a small representative comparison set;
- force systems/safety/runtime-assurance concepts into UA categories without recording where the translation is lossy or where UA may need revision;
- allow the UA-derived material-relationship map to define the universe against which its own completeness is judged; reverse-mapping discoveries must be materiality-tested independently, versioned, and able to stop a whole-object verdict;
- define materiality after inspecting a preferred carrier or substitute in order to make that composition pass; apply the stated materiality invariant before substitution and allow reverse mapping to challenge it explicitly;
- claim semantic equivalence without defining the required material properties for the relationship first, or call a substitute “stronger” when relevant dimensions trade off, scopes differ materially, or evidence cannot support the dominance claim; use unresolved/non-comparable explicitly;
- embed a self-referential repository SHA in the blueprint-owned mapping or require a whole-object verdict to depend on branch history that may disappear after rebase/squash; freeze the mapping logically, record an immutable snapshot reference in the verdict/test record after freeze, and rerun after a mapping-version change;
- treat a higher or lower numerical cost, latency, staffing demand, or Human Authority burden as proof that viability-decision semantics are weaker or stronger; semantic equivalence preserves the decision relationship, while actual burden belongs to practical preference;
- present the proposed landscape integration gap as established fact rather than a bounded hypothesis to be challenged by substitution and reverse mapping;
- use a vendor matrix as marketing evidence that the derived map “covers more”; the map is a comparison reference, not a scored implementation-capability competitor;
- repeat the **Article §2** NIST/ISO category-boundary argument in **Article §6**; change the analytical lens to functional coverage and substitution;
- use “UA map” or “UA-shaped architecture” throughout **Article §6** in a way that makes the named framework the premise of its own comparison; use “derived operating map” until **Article §7** formally delimits the research synthesis in relation to the specification boundary defined/indexed by `SPECIFICATION.md`;
- re-derive Thinking-System classification, the controlled object, four capability families, four decision horizons, Hard/Soft, Human Authority, proportionality, baseline reconstructability, fallback credibility, or reassessment routing after **Article §4** when the later section should apply or test the established result;
- present the lower-authority **Article §5** variant as a chronological state or as another Delivery realization inside the canonical Project Authorization;
- compare lower-/higher-authority variants at different lifecycle maturity points and then attribute the difference to authority; separate scope/authority delta from lifecycle-maturity delta;
- present the Article §5 carrier-sufficiency/materiality mapping as current UA conformance or a mandatory artifact; it remains a paper-level research test unless later accepted through explicit framework review;
- create a third living article-planning note merely to host the Article §5 working mapping; keep that analysis blueprint-owned unless a separate explicit repository/editorial decision establishes an independent research artifact;
- use material control overhead to decide whether semantic substitution exists. Semantic equivalence decides substitution; material control overhead decides practical preference among semantically adequate concrete operating compositions; conceptual overhead only narrows explanatory contribution;
- imply that applying the derived map necessarily adds an operational, runtime, workflow, or document layer; distinguish analytical/review use from concrete operating augmentation;
- describe implementation surfaces as a one-to-one or simple many-to-one projection of the map; preserve the many-to-many composition and end-to-end traceability;
- attribute the specification boundary to generic “status-bearing modules.” `SPECIFICATION.md` defines and indexes the boundary; indexed documents contribute only within declared status/scope;
- add a figure merely to satisfy an expected count when an existing figure, table, or prose already carries the relationship;
- use internal or remembered product capabilities without checking current first-party sources immediately before publication.

Preferred landscape language:

- “these approaches cover substantial parts of the problem”;
- “this function is normally inside/outside the approach's scope”;
- “this paper examines whether a material remaining semantic gap lies in cross-boundary integration/authority/reassessment/viability-decision semantics”;
- “the derived operating map provides a reference for composing and challenging these pieces”;
- “within the cited comparison set, we have not identified…”;
- “reverse mapping may show where the reference model loses useful structure”;
- “this mapping should be corrected by maintainers and practitioners where it understates current capability”;
- “if an existing stack already carries the material decisions semantically, recognize substitution first; then compare concrete operating compositions and practical overhead.”

## 8. Repository source plan

### Authority-bearing framework sources

1. [`SPECIFICATION.md`](../../../SPECIFICATION.md)
2. [`Glossary`](../../../00-doctrine/glossary.md)
3. [`Uncertainty in the Controlled Object`](../../../00-doctrine/uncertainty-in-the-controlled-object.md)
4. [`Control-Loop Capability Anatomy`](../../../00-doctrine/control-loop-anatomy.md)
5. [`Nested Control Lifecycle`](../../../00-doctrine/nested-control-lifecycle.md)
6. [`Requirements, Correctness, and Bugs`](../../../00-doctrine/requirements-correctness-and-bugs.md)
7. [`Model Judgment Placement`](../../../00-doctrine/model-judgment-placement.md)
8. [`Project Control Architecture and Viability Review`](../../../01-patterns/project-control-architecture-and-viability-review.md)
9. [`Thinking System Review`](../../../01-patterns/thinking-system-review.md)
10. [`Judgment Node Boundary`](../../../01-patterns/judgment-node-boundary.md)
11. [`AI Control Plane`](../../../02-ai-control-plane/README.md)
12. [`Actuator Capabilities`](../../../02-ai-control-plane/00-actuators/README.md)
13. [`Constraint Capability Family`](../../../02-ai-control-plane/01-constraints/README.md)
14. [`Sensor and Evidence Capabilities`](../../../02-ai-control-plane/02-sensors/README.md)
15. [`Controller and Decision Authority`](../../../02-ai-control-plane/03-controller/README.md)

`SPECIFICATION.md` defines and indexes the normative specification boundary and document-status/conformance model. The remaining listed documents contribute only according to their own declared status and scope and the index relationship in `SPECIFICATION.md`; they do not independently redefine the boundary. The paper may derive an explanatory sequence and publication-facing operating model, but it must not override the specification, glossary, or owning source. New operating-model formulations discovered in the article remain research until separately reconciled through explicit framework review and, where accepted, a corresponding `SPECIFICATION.md`-indexed status-bearing change.

### Supporting repository sources

- [`Constraint Realization Catalog`](../../../02-ai-control-plane/01-constraints/constraint-realization-catalog.md) — informative implementation examples.
- [`Worked Support-Triage Review`](../../../03-reference-architectures/worked-thinking-system-review-support-triage.md) — illustrative delivery-level reference, not publication validation.
- [`Project Review Template`](../../../01-patterns/project-control-architecture-and-viability-review-template.md) and [`Thinking System Review Template`](../../../01-patterns/thinking-system-review-template.md) — implementation surfaces available in the repository, not mandatory publication artifacts.
- [`Failure Modes and Anti-Patterns`](../../../04-failure-modes/README.md) — reusable loss-of-control mechanisms according to document status.
- [`ROADMAP.md`](../../../ROADMAP.md) — current project state and open validation work.

Historical articles, talks, presentation material, and research may provide provenance and evidence. They must not override the specification boundary and authority order defined/indexed by `SPECIFICATION.md`.

### External evidence

Current factual claims about standards, laws, platform capabilities, market practice, or the state of AI governance must be checked against current primary or authoritative sources. Named platform capabilities must be checked against first-party documentation **at the time the manuscript section is drafted and again during the final publication pass**. Comparative claims should be narrow, dated where relevant, and should not imply exhaustive market coverage.

The running support-resolution example in Section 2.6 of this blueprint is **fictional/editorial**. It does not require external evidence for the invented company, illustrative refund threshold, or hypothetical runtime rates because those values are not factual claims. If the manuscript replaces any fictional property with a real legal, contractual, regulatory, vendor, or market claim, that claim must follow the normal external-evidence rules.

#### Early category-boundary sources for Article §2

Use these only for the narrower neighboring-label comparison unless another section explicitly needs them:

- ISO/IEC TR 29119-11:2020, *Guidelines on the testing of AI-based systems*: https://www.iso.org/standard/79016.html
- NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10

**Article §2** should not use these sources to make broad claims about the adequacy of NIST/ISO governance or engineering coverage.

#### Intellectual antecedent sources for Article §7

- Nancy G. Leveson, *Engineering a Safer World* / STAMP: https://mitpress.mit.edu/9780262016629/engineering-a-safer-world/
- Software Engineering Institute, *An Architectural Description of the Simplex Architecture*: https://www.sei.cmu.edu/library/an-architectural-description-of-the-simplex-architecture/
- Sculley et al., *Hidden Technical Debt in Machine Learning Systems*: https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/
- Amershi et al., *Software Engineering for Machine Learning: A Case Study* (ICSE 2019): https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/
- Martínez-Fernández et al., *Software Engineering for AI-Based Systems: A Survey* (TOSEM 2022): https://doi.org/10.1145/3487043
- NIST AI RMF may be referenced compactly for intellectual continuity, but functional/current comparison belongs to **Article §6**.

Use these to establish intellectual context, terminology scope, maturity, and comparison boundaries, not to imply direct derivation, endorsement, or equivalence.

#### Landscape source plan for Article §6

Use **approach families first** and only enough named examples to prove that the mapping is grounded in real current capabilities. Do not create a market catalog.

**Control-theoretic research**

- Bhargava et al., *What's the Magic Word? A Control Theory of LLM Prompting*: primary paper/arXiv source.
- Add one or two additional current peer-reviewed/preprint control/LLM or LLM-as-controller papers only if they materially demonstrate a distinct research direction; do not use them to claim exhaustive coverage of the field.

**Systems / safety / runtime-assurance engineering methods**

- Nancy G. Leveson, *Engineering a Safer World* / STAMP and current STPA primary material — use for hierarchical socio-technical control, safety constraints, unsafe control actions, feedback, and process-model concepts.
- Software Engineering Institute, *An Architectural Description of the Simplex Architecture* and other primary runtime-assurance material where needed — use for trusted safety paths, decision modules, fallback, and assured runtime boundaries.
- Add one current systems/safety-engineering source only if it materially demonstrates lifecycle assurance or responsibility semantics not already covered by STAMP/STPA or Simplex; do not create a generic systems-engineering literature survey.
- Apply the same reverse-mapping rule: record what these methods contain that UA does not represent cleanly, rather than treating every mismatch as missing coverage in the antecedent.

**Production ML and software/systems engineering for AI**

- Sculley et al., *Hidden Technical Debt in Machine Learning Systems*: https://research.google/pubs/hidden-technical-debt-in-machine-learning-systems/
- Amershi et al., *Software Engineering for Machine Learning: A Case Study* (ICSE 2019): https://www.microsoft.com/en-us/research/publication/software-engineering-for-machine-learning-a-case-study/
- Martínez-Fernández et al., *Software Engineering for AI-Based Systems: A Survey* (TOSEM 2022): https://doi.org/10.1145/3487043
- Use these sources functionally in **Article §6** for lifecycle, technical-debt, testing, assurance, maintenance, change, and responsibility semantics. **Article §7** may refer back to that analysis in one compact provenance treatment rather than redescribing it.

**Agent/orchestration runtimes**

- LangGraph official documentation — durable execution, persistence, human-in-the-loop, orchestration.
- Microsoft AutoGen official documentation — agent runtime/orchestration capabilities.
- Microsoft Semantic Kernel official documentation — orchestration/agent/process capabilities.
- OpenAI Agents SDK official documentation — agents, tools/handoffs, guardrails, human-in-the-loop, tracing.
- CrewAI official documentation may be included as another representative approach if it adds a materially different capability and current docs support the claim.

**Guardrails / runtime enforcement**

- NVIDIA NeMo Guardrails official documentation.
- One or two managed guardrail examples from current first-party docs, e.g. Microsoft Foundry safety/guardrail capabilities, Amazon Bedrock Guardrails, Google Model Armor.
- Guardrails AI may be used if current official documentation materially adds a different realization pattern.

**Evaluation / observability**

- LangSmith official documentation — tracing/monitoring/alerts plus offline/online evaluation.
- Arize Phoenix official documentation — tracing/evaluation/datasets/experiments where current docs support the claim.
- TruLens official documentation — instrumentation/evaluation/runtime feedback where current docs support the claim.
- Prefer one sentence noting OpenTelemetry-compatible instrumentation where relevant rather than treating the telemetry standard itself as an AI-governance framework.

**Managed AI / agent platforms**

- Microsoft Foundry official documentation as a representative integrated platform; verify current agent runtime, identity, guardrail/safety, evaluation/observability, and deployment capabilities.
- Amazon Bedrock official documentation as another representative managed stack if needed.
- Google Cloud official documentation for agent/model protection/managed AI capabilities if needed.
- OpenAI official agent/application documentation may be referenced where the integrated stack materially differs from the SDK example.

**Enterprise AI governance / assurance**

- IBM watsonx.governance official product and documentation pages are a useful representative source for AI use-case governance, risk/compliance workflows, factsheets/lifecycle records, evaluation, monitoring, thresholds, and regulatory mapping.
- Add another enterprise governance suite only if necessary to avoid drawing general conclusions from one product; do not turn the paper into procurement research.

**Standards / management systems / regulation**

- NIST AI RMF 1.0 and **NIST AI RMF Playbook** — use the current official NIST pages. Preserve Govern / Map / Measure / Manage and the Playbook's explicit design/development/deployment/use scope.
- ISO/IEC 42001 official ISO overview — use it to establish AI management-system scope and continual improvement; do not infer details hidden behind the paid standard beyond the official public description unless a licensed source is available.
- EU AI Act — use EUR-Lex for legal text and current European Commission guidance for current implementation/applicability dates. Because the Act's implementation timeline and guidance can change, **recheck immediately before publication** rather than copying dates from an earlier drafting session.

**Current facts already verified during the August 2026 blueprint revision and requiring re-verification at manuscript/publication time:**

- LangGraph first-party docs describe a low-level orchestration/runtime focused on long-running stateful agents with durable execution, persistence and human-in-the-loop.
- OpenAI Agents SDK first-party docs describe HITL approval flows for sensitive tool calls plus guardrails and tracing.
- LangSmith first-party docs describe tracing/monitoring/alerts and offline/online evaluation.
- NVIDIA NeMo first-party docs describe configurable guardrail checks in the inference path; exact rail taxonomy should be checked against the current version used in the manuscript.
- IBM watsonx.governance first-party materials describe enterprise AI governance/risk/compliance, AI use-case/lifecycle records, evaluation/monitoring and policy/control relationships.
- NIST's AI RMF Playbook describes suggested actions for Govern, Map, Measure and Manage and explicitly targets design, development, deployment and use.
- ISO's public ISO/IEC 42001 description defines an AI management system for establishing, implementing, maintaining and continually improving organizational AI management.
- Current European Commission/EUR-Lex material describes risk-management, logging/traceability, human oversight, post-market monitoring/operation monitoring, incident response and corrective-action obligations for applicable high-risk systems; exact dates and applicability must be freshly checked.

These are **research notes for future drafting, not publication citations by themselves**. The manuscript must cite the then-current primary source and state only what that source supports.

## 9. Publication framing

### Working title

**Uncertainty Architecture: Engineering Thinking Systems with Consequential Runtime Responsibilities**

The title begins with **Uncertainty Architecture** for attribution and discoverability, while the article body delays full framework introduction until the engineering model has been derived and adjacent approaches have been mapped against it.

### Publication identity

Treat the repository edition as an **open engineering working paper / architecture working paper under validation**. This framing fits the article's purpose: define the problem space, propose an operating map and practices, expose assumptions, map the surrounding ecosystem, and invite external review and contradictory cases. “White paper” is acceptable as a distribution label only when the maturity caveat is preserved and the presentation does not imply a vendor product claim, final standard, or validated industry consensus.

The publication should explicitly invite review not only of whether the full map is complete, but also of **proportionality and substitution**: which parts can safely remain implicit or lightweight in simpler systems, which signals reveal hidden complexity early, where teams discover that an apparently small use case actually requires a much larger control perimeter, and where existing tools/frameworks already make a UA-specific representation unnecessary.

The publication should not frame current repository templates as the paper's principal deliverable. The public deliverable is the **engineering map, operating questions, and landscape/substitution lens**; templates and reference implementations are follow-on surfaces that can evolve independently as evidence accumulates.

### Length rule and soft planning ranges

**No hard word-count ceiling applies to the canonical manuscript during drafting or as a repository-publication acceptance criterion.** Section word budgets and overall word-count ranges in this blueprint are editorial planning heuristics only. Completeness, conceptual precision, continuity of the argument, and removal of unnecessary repetition take precedence over hitting a numerical target.

Do not shorten a section merely because it exceeds its working budget while the argument is still being constructed. Perform integrated compression only after all eight sections exist and have been reread as one paper. During that pass, cut duplicated explanation, redundant vendor/product detail, repeated restatement of the running example, and prose that no longer advances the argument before removing decision semantics, authority boundaries, reassessment logic, claim-safety qualifications, or evidence obligations.

The earlier 4,300–5,200-word and 9,000–11,500-word targets are obsolete as planning baselines. **Article §§1–4** alone now contain approximately **10,200** English words when Mermaid/code blocks are excluded. The current **Article §§5–8** planning ranges total **4,150–5,350** words, so the arithmetic canonical drafting orientation is **14,350–15,550 words** when the ~10,200-word current baseline is used. A later **11,500–13,500-word integrated-compression orientation** may be useful only after all eight sections exist and the complete argument has been reviewed; that compression range is not the arithmetic sum of section plans and depends on removing duplication across the integrated manuscript. These are soft ranges, not acceptance gates; exceeding them is preferable to deleting decision semantics, while meeting them does not excuse repetition or conceptual incompleteness.

The canonical repository paper is the full reference publication. Medium and LinkedIn editions may be shortened independently for distribution and should link back to the canonical repository edition rather than forcing the canonical argument to fit a platform-specific length preference.

### Target and publication paths

Working article:

```text
content/research/notes/open-engineering-specification-article-draft.md
```

Published repository edition:

```text
content/research/publications/uncertainty-architecture-thinking-systems.md
```

Medium and LinkedIn editions are distribution copies and should link back to the repository edition.

## 10. Iteration acceptance criteria

Every article-writing PR must satisfy all of the following:

- [ ] The complete blueprint was read before selecting the next section block.
- [ ] The complete target article was read before drafting.
- [ ] New prose continues the existing argument and terminology.
- [ ] Previously written sections were revised where the new block exposed repetition, contradiction, weak transitions, or premature framing.
- [ ] Word-count ranges and per-section budgets were treated as soft editorial guidance rather than gates; no argument, decision semantic, authority boundary, claim-safety qualification, or evidence obligation was removed solely to satisfy a numerical target.
- [ ] The canonical action-capable support-resolution trace remains consistent with Section 2.6 of this blueprint, is used as a narrative aid rather than validation evidence, and does not introduce example-specific doctrine; **Article §5** contains at most the one explicitly marked counterfactual sibling from the same business proposal.
- [ ] When the running trace is used, its canonical controlled object, Consequential Runtime Responsibilities, illustrative Hard/Soft distinction, Human Authority semantics, and three reassessment cases remain internally consistent; the **Article §5** sibling is treated as a different candidate Project design and scope rather than a second Delivery realization, states that its consequential human decision remains materially dependent on Model Judgment, records the resulting positive category retest, receives its own compact full-map inspection, and does not overwrite the canonical facts.
- [ ] The **Article §5 authority/scope comparison holds lifecycle maturity constant** across both candidates and explicitly separates scope/authority delta from later Delivery/Runtime maturity delta.
- [ ] Plan-driven development, iterative delivery, and modern operations remain the primary categories, with Waterfall, Agile and related approaches, and DevOps named consistently as familiar examples in the opening prose, Figure 1, and the comparison table.
- [ ] The abstract does not narrate the article's reveal sequence or contain internal editorial commentary; it identifies UA as an existing open draft specification whose boundary is defined/indexed by `SPECIFICATION.md`, distinguishes it from the paper's research synthesis, and does not promote paper-only claims into the specification by implication.
- [ ] Governance is framed as becoming operational through the active socio-technical control architecture rather than as a post-hoc review, document, or exact synonym for every control element.
- [ ] The consequence of an incomplete cross-level control architecture is explicit, scoped to readiness for production release at the intended scope, and visually emphasized once as a central engineering thesis without duplicating the argument.
- [ ] Figure 3 places two vertical top-to-bottom responsibility diagrams side by side, highlights only the Judgment Node(s) where Model Judgment changes the responsibility structure, and remains descriptive of category membership rather than prescribing a target production control architecture.
- [ ] The whole software Thinking System remains the controlled object while Human Authority, Constraint Realizations, Sensors, Controllers, Actuators, and other control relationships remain conceptually distinct within the surrounding socio-technical control perimeter; a component may implement multiple functions or sit inside the software boundary without collapsing the controlled-process/control-function distinction.
- [ ] Figure 4 places Model Judgment above Input Interpretation, Decision Logic, and Output Mediation, with the three placements aligned horizontally and no implied mandatory sequence.
- [ ] Figure 8 keeps Organization, Project / Architecture, Delivery, and Runtime in one centered vertical spine, preserves concise downward inheritance labels, places one reassessment-evidence node beneath the horizons with inputs from Delivery realization evidence and Runtime operation evidence, and routes invalidating evidence directly back to the owning decision level with the invalidated basis on the return edge rather than in a separate reassessment subsystem.
- [ ] Figure 9 reproduces the Figure 8 four-horizon decision model verbatim—including horizon questions, reassessment evidence from Delivery realization or Runtime operation, downward inheritance labels, and reassessment-route wording—and adds the capability-family dimension as a visually distinct green group with undirected structural grouping and no implied one-to-one mapping or execution pipeline.
- [ ] **Article §3** introduces the capability families in Actuator → Constraint/Realization → Sensor → Controller pedagogical order and explicitly distinguishes that reading sequence from execution order.
- [ ] **Article §3** defines Controller as a decision function that may combine legitimate human authority with automation and states that automation does not create undelegated authority.
- [ ] Automation recommendations are conditional on evidence quality, failure behavior, reversibility, consequence, and delegated authority, and automated control paths are themselves observable and correctable at Project, Delivery, and Runtime where automated control is used.
- [ ] Evidence instruments used as material Sensors carry active version/identity, validation or calibration basis where applicable, coverage/uncertainty/latency, and validity-loss triggers; the article permits recalibration, replacement, or changed evidence use rather than assuming permanent validity.
- [ ] Hard Constraint discussion prefers deterministic prevention where feasible but does not claim Hard strength when the complete scoped realized path remains probabilistic.
- [ ] **Article §2** closes with the reach of the expanded control perimeter and recurring control questions without introducing canonical horizon labels; **Article §4** introduces the four decision horizons and keeps control-architecture design inside the Project / Architecture level.
- [ ] **Article §2**'s NIST/ISO neighboring-label comparison remains scoped to category definition and does not pre-judge the later landscape analysis.
- [ ] **Article §4** treats all four levels as operating processes through time, not only static ownership descriptions.
- [ ] The article states explicitly that the complete map is a diagnostic reference for complex/high-consequence systems and that simpler systems may use proportionate subsets after the full map has been inspected for hidden complexity.
- [ ] Proportionality is justified by actual consequence, authority, exposure, reversibility, uncertainty, feedback latency, realization difficulty, Human Authority load, capacity, and economics—not by superficial implementation size such as one model call or one UI feature.
- [ ] Each decision level explicitly covers activation triggers, inputs/authority basis, owned decisions, capability obligations, outputs/artifacts, evidence received, local action versus escalation, and learning/stabilization where proposed.
- [ ] Organizational control owns admissibility, authoritative boundaries, shared capabilities, reserved/delegated decision rights, evidence obligations, and exceptions; it does **not** absorb the Project-owned AI-necessity, complete viability, or scope-expansion decision when the proposed change remains inside existing organizational authority.
- [ ] Organizational decision owners create downstream evidence obligations when they own a material boundary or outcome; the article connects authoritative source → scoped Constraint/assumption → realization requirement → Sensor/evidence → Controller → Actuator/escalation.
- [ ] Organizational evidence includes both lower-level project/runtime evidence and exogenous/cross-project evidence such as legal, contractual, audit, vendor, and shared-capability change.
- [ ] Figure 10 shows external/organizational evidence, authoritative reference sources, and lower-level evidence/authority requests as converging inputs to the Organizational Controller rather than a sequential pipeline.
- [ ] Project viability/authority requests and Runtime invalidation are represented as examples inside the lower-level evidence lane in Figure 10, not duplicated as additional parallel arrows.
- [ ] Figure 10 shows a real control relationship including Organizational Actuators, not only a list of participating departments or an approval box.
- [ ] Organizational control does not become a mandatory new department, committee, or standalone UA document; existing sources and roles may carry the authority.
- [ ] Project / Architecture explicitly owns business outcome, AI necessity, project boundary, intended Judgment landscape, Project Constraint Architecture, control viability, and Project Authorization for the specific system; it receives a hypothesis rather than presupposed proof of Model Judgment value and allows authorize/narrow/research/redesign/defer/No-Go outcomes without claiming ownership of Delivery's implementation-level Judgment Nodes or approved Requirement and Operating Envelope.
- [ ] Project sufficiency uses **credible complete bounded control path/architecture** language rather than conflating a closed feedback loop with a complete bounded control architecture.
- [ ] Figure 11 keeps the Project Constraint Architecture limited to scoped Project Constraints/assumptions and renders required operating-contract properties/evidence obligations as a **separate Project output** that Delivery translates into its approved Requirement and Operating Envelope.
- [ ] Project control economics uses non-overlapping conceptual cost buckets and does not double-count Human Authority, fallback, incident response, or operational friction inside and outside the control perimeter.
- [ ] Material evidence can be correlated to the active source/Project/Delivery/realization/model-config/evaluator/deployment/fallback baseline sufficiently to reconstruct what governed a material release, incident, or Actuator decision; no universal registry is implied.
- [ ] Fallback/recovery paths are not presumed safe by existence and expose/test relevant dependency independence/common-mode coupling, capacity/latency, transition behavior, and ability to restore an authorized state where material.
- [ ] Delivery clearly owns implementation-level Judgment Nodes and the approved Requirement and Operating Envelope for the bounded scope and distinguishes them from the inherited project boundary, intended Judgment landscape, Project Authorization, project Constraints, concrete realization, DoR, DoD, Release Gate, local repair, and Project Reauthorization.
- [ ] Figure 12 distinguishes Release Gate **rework**, **terminal stop/defer/reject**, and **Project Reauthorization for delivery-discovered project/organizational-boundary issues**; it does not bypass Project / Architecture to Organization. Direct Organizational review is reserved for a changed organizational basis, or is reached from Project when wider organizational authority/exception is required.
- [ ] Runtime distinguishes restoration of an authorized state from redesign or reauthorization and verifies that Actuator execution produced the intended state.
- [ ] The cross-level operating discipline ties material evidence to an owning decision and does not use “measure everything” as a literal telemetry requirement.
- [ ] A negative case is treated as evidence requiring diagnosis, not automatically as a Bug, Requirement violation, or model-quality failure.
- [ ] Every material negative case considered by the proposed learning discipline is analyzed against the complete control architecture—Sensor, Constraint, Constraint Realization, Controller, Actuator, Human Authority, fallback, automation, active-baseline correlation, assumptions, and economics—not only model quality.
- [ ] The proposed learning loop routes negative cases to the level whose decision basis they invalidate and does not imply that every case escalates to Organization.
- [ ] The article clearly distinguishes the current lifecycle reassessment structure from the **proposed cross-level negative-case learning/stabilization discipline under validation**.
- [ ] Stabilization is framed as a hypothesis about reducing uncontrolled recurrence through prevention, earlier detection, faster routing, more reliable correction, narrower exposure, cheaper recovery, or revised authorization rather than eliminating all probabilistic variance or claiming validated improvement.
- [ ] **Article §5** explicitly labels carrier sufficiency, the complete material-relationship mapping, the materiality rule, and the substitution handoff as paper-level research under validation rather than current UA conformance or a mandatory artifact.
- [ ] **Article §5** treats full-map-before-depth proportionality as inherited from **Article §4** and does not reteach the four-horizon pressure test or depth-factor explanation; it states that the defined counterfactual sibling's consequential human decision remains materially dependent on Model Judgment, records the resulting positive category retest, and inspects the sibling against the inherited full map as a distinct candidate controlled object and Project scope without presupposing Project Authorization. Only the material delta appears in publication prose.
- [ ] **Article §5** extracts the intended outcome and material authority/boundary/evidence/decision/action/verification/reassessment relationships, uses the active Delivery-approved Requirement and Operating Envelope only for an authorized bounded scope, uses proposed operating-contract properties for an unapproved candidate Project scope, and applies a credible-carrier test covering ownership, source/scope/assumptions/version, guarantee strength where applicable, lifecycle, correctness, evidence consumer/latency/validity, Actuation, post-action verification, failure, and reassessment.
- [ ] **Article §5** applies the materiality invariant before evaluating a particular carrier/substitute: absence/change must be able to materially affect intended outcome, Requirement/Constraint satisfaction, delegated authority/reachable consequence, correctness/release/continuation/stop decision, corrective/reassessment ability, or technical/operational/control-economic viability. Reverse mapping may challenge the set explicitly but materiality is not defined post hoc to favor a verdict.
- [ ] **Article §5** distinguishes a decision record from a Constraint Realization, Sensor, Controller, or Actuator and represents implementation surfaces as a many-to-many composition with end-to-end traceability.
- [ ] **Article §5** produces both the authority-variant comparison and a complete canonical material-relationship-to-carrier working mapping that **Article §6** can consume without rerunning the carrier analysis; the mapping has a stable ID/version, controlled-object/lifecycle baseline, source/authorization baseline, scope, assumptions, materiality decision rule, guarantee semantics where applicable, materiality rationales for inclusion/exclusion, explicit decision/reference semantics (including viability owner/input categories/decision right/outcomes where material), evidence/intended-consumer/action/verification semantics, and lifecycle/change-control/reassessment semantics. The mapping header does not contain a self-referential repository SHA; the substitution run/verdict records an immutable snapshot reference after freeze.
- [ ] The complete Article §5 working mapping remains **blueprint-owned** under the two-document drafting model; it does not create a third living article-planning note unless a separate explicit repository/editorial decision establishes an independent research artifact.
- [ ] **Article §§5–6** reference the same mapping ID/version and immutable snapshot for a substitution run; for a blueprint-owned mapping, a deterministic content digest is preferred when branch history may be rewritten. A clearly labeled manuscript excerpt cannot stand in for the full material analysis.
- [ ] Reverse mapping can discover a potentially material relationship absent from the imported map. Such a discovery stops the whole-controlled-object semantic-substitution verdict, requires independent materiality assessment, mapping versioning where material/uncertain, and a rerun before the verdict is restored; recurrent partition lossiness routes to Validation Program 2.
- [ ] A mapping-version change makes earlier whole-object substitution verdicts stale for the new mapping until rerun while preserving them as historical results against the exact version/snapshot originally tested.
- [ ] **Article §5** compares a counterfactual draft/human-execution Project alternative with the canonical action-capable support case without treating the variants as a chronology or as two Delivery realizations inside one Project Authorization.
- [ ] **Article §5** revisits implementation depth and carrier choice when authoritative sources, authorization, scope, Project assumptions, Delivery realization evidence, Runtime operation evidence, or evidence-instrument validity change; such evidence may strengthen, narrow, redistribute, consolidate, simplify, recalibrate, or replace parts of the implementation.
- [ ] **Article §5** does not make the two-living-review pattern, `K-SEND-01`, or any one template the paper's required practical artifact; repository patterns remain optional implementation/reference material rather than validation.
- [ ] **Article §6** uses “derived operating map” or equivalent until **Article §7** formally delimits the research synthesis in relation to the UA specification boundary; the named framework is not used as the premise of its own comparison.
- [ ] **Article §6** keeps the detailed bidirectional lens as a research worksheet but structures publication prose around three genuine substitution classes—conceptual/engineering, implementation/integrated-stack, and organizational-practice substitutes—while treating pure sources of obligation/authority as a separate input class rather than as substitutes by themselves.
- [ ] **Article §6** treats “outside scope” as a scope boundary rather than an inferiority score and allows adjacent methods to expose missing or poorly partitioned concepts in the reference model itself.
- [ ] **Article §6** includes systems/safety/runtime-assurance methods as real conceptual substitutes and reverse-maps STAMP/STPA, Simplex, control-theoretic, and other native concepts without flattening them into UA vocabulary.
- [ ] **Article §6** keeps runtime-assurance architectures and mathematical/control-theoretic research as separate comparison rows with distinct controlled objects, guarantees, lifecycle scope, and reverse-mapping losses.
- [ ] **Article §6** distinguishes pure authority sources from risk/management methods and operated management systems; the source alone is not a substitute, while an adopted and operated method composed with ordinary engineering may be.
- [ ] **Article §6** frames the proposed cross-boundary integration gap as a hypothesis under comparison/falsification rather than an established market-wide fact.
- [ ] **Article §6** matrix cells are representative tendencies, not guaranteed category properties; product/platform coverage is configuration-dependent and method coverage is application-dependent.
- [ ] **Article §6** acknowledges real current capabilities of orchestration runtimes, guardrails, observability/evaluation tools, managed AI platforms, and governance suites rather than using stale strawman descriptions.
- [ ] **Article §6** distinguishes current tool/platform implementation from the source of organizational/project authority without claiming that platforms or governance suites “cannot solve governance.”
- [ ] **Article §6** distinguishes applicable law/binding obligations from voluntary standards/frameworks and distinguishes compliance from operational control in both directions.
- [ ] **Article §6** defines relationship-level semantic equivalence before testing substitutes: the required material semantics are frozen from the complete mapping under the same relevant scope and assumptions; different vocabulary/structure is allowed; “stronger” requires preservation of all required semantics plus demonstrably stronger assurance/coverage/guarantee for the same purpose; trade-offs or scope mismatch produce unresolved/non-comparable rather than an intuitive dominance claim. For material viability/economic relationships, the frozen semantics are owner/input categories/decision right/outcomes/reassessment, not the numerical control burden.
- [ ] **Article §6** separates whole-controlled-object semantic substitution from practical preference: every material relationship must pass the frozen equivalence test for the exact mapping ID/version/immutable snapshot before the semantic integration gap is considered closed; material control overhead is evaluated only afterward among concrete semantically adequate operating compositions.
- [ ] Applying the derived map as an analytical/review lens is not treated as an additional operational layer, mandatory workflow, or document package; practical-preference comparison is between actual existing, augmented, or replacement operating compositions.
- [ ] A representative subset supports only relationship-level findings, and whole-controlled-object semantic substitution requires every material relationship to be tested.
- [ ] **Article §6** uses **conceptual overhead only to assess explanatory contribution**, never as the semantic-substitution or practical-control-overhead criterion.
- [ ] **Article §6** landscape matrix/figure is approach-class based, not a product-logo scorecard; the derived map is a reference frame rather than a scored row.
- [ ] Named landscape claims use current first-party/primary sources and are rechecked immediately before publication.
- [ ] The landscape section does not claim UA is first/only/unique, infer market-wide absence, or repeat **Article §2**'s NIST/ISO category-boundary argument.
- [ ] **Article §7** formally situates and delimits the research synthesis already derived, applied, and challenged relative to the UA specification; it does not pretend to reveal the name for the first time, reteach the operating map, repeat the current-product survey, or promote paper-only claims by implication.
- [ ] **Article §7** states explicitly that **`SPECIFICATION.md` defines and indexes the specification boundary**, and every indexed document acts only within its declared status/scope; “status-bearing modules” is not treated as an independent boundary owner.
- [ ] **Article §7** states the proposed contribution as a paper-level synthesis/recomposition, separates the existing specification boundary from paper-only carrier/substitution/reverse-mapping/integration-gap hypotheses, defines what UA is and is not, and requires explicit framework review plus a corresponding status-bearing change before research can alter the specification.
- [ ] **Article §7** uses one compact provenance treatment and does not repeat the functional STAMP/STPA, Simplex, NIST, platform, or tool analysis from **Article §6**.
- [ ] **Article §8** organizes validation into falsifiable programs that name the claim, contradictory evidence, owning response surface, and required remove/revise/split/demote/substitute/reject response, and applies one shared study-design protocol requiring each study to predefine its target class, boundary conditions, independent sample, observable criteria, decision rule, and any competence/application-fidelity criteria; bundled subclaims are evaluated separately when evidence would require different revisions.
- [ ] **Validation Program 2** routes any accepted specification consequence to the appropriate `SPECIFICATION.md`-indexed status-bearing document(s), not to a generic second boundary owner.
- [ ] **Validation Program 3** owns evidence that reassessment routing/authority semantics fail, active-baseline reconstructability fails materially, fallback/recovery credibility fails, or authority semantics create excessive escalation or leave cases without a credible owning decision basis; **Program 2** owns evidence that important failures/relationships sit outside the anatomy/partition.
- [ ] **Validation Program 5** starts only after a credible owning decision basis has been established and tests the learning/stabilization effect only; it does not precommit to retaining the lifecycle structure when evidence actually challenges Programs 2 or 3.
- [ ] **Validation Program 6** tests both the semantic integration-gap claim and the reproducibility of the relationship-level equivalence/snapshot method: semantic equivalence with no residual material relationship narrows/rejects the gap regardless of actual overhead; persistent unresolved/non-comparable judgments, snapshot-identification failures, or independent disagreement narrow the method; actual material control overhead is recorded separately to compare practical operating compositions.
- [ ] **Article §8** explicitly requests evidence on active behavioral/control baseline reconstruction, fallback/common-mode/capacity/restoration behavior, and evaluator/Golden Set/rubric/threshold/human-review-signal validity loss, versioning, calibration/validation, incident ingestion, recalibration, replacement, and changed decision use.
- [ ] **Article §8** explicitly states that the constructed support example cannot validate the framework and asks for independent applications, failures, substitutions, reverse mappings, and safe deletions.
- [ ] **Article §8** remains a validation agenda rather than a product CTA, welcomes evidence that existing approaches solve the problem more simply, and distinguishes map validation, artifact validation, learning-hypothesis validation, and landscape-mapping correctness.
- [ ] Every future figure passes the additive-information test; an existing figure, compact table, or prose is preferred when a new diagram would only repeat the established map.
- [ ] Figure 10 is process-oriented rather than a department influence map and shows exogenous evidence, downward obligations, Organizational Actuators, and return evidence/reauthorization routes.
- [ ] Figure 15, if used, is labeled as proposed under validation and does not imply every negative case is a Bug or must escalate to Organization.
- [ ] The adjacent-landscape figure uses coverage bands/mappings, not causal arrows or marketing scores, states that external approaches may implement capabilities more concretely than the reference model, and includes reverse mapping.
- [ ] **Article §5** uses the authority-variant comparison plus one clearly labeled publication excerpt from the complete canonical relationship-to-carrier working mapping, **Article §6** uses one landscape matrix/coverage figure, **Article §7** uses either the boundary/composition figure or the `UA is / UA is not` table, and **Article §8** uses the validation table/callout rather than another loop.
- [ ] The final UA boundary/composition representation references rather than redraws Figure 9 and shows authority sources, implementation surfaces, substitution, and evidence-driven revision outside the UA ownership boundary.
- [ ] Article references use **Article §1…§8 / Article §§n–m** consistently; blueprint subsection numbers such as `2.6` remain blueprint-local, and actual established figures use their manuscript numbers (Figures 1–15) rather than a competing “Primary Figure 1/2” scheme.
- [ ] All figures were reviewed as one visual sequence and renumbered consistently.
- [ ] The complete target article was reread after integration.
- [ ] This blueprint was updated after the target article review.
- [ ] Section purposes, required content, transitions, claims, examples, known risks, rejected formulations, and unresolved decisions remain detailed rather than compressed.
- [ ] UA is not introduced as the premise of the early engineering argument.
- [ ] Thinking-System category identity is separated from control adequacy; **Consequential Runtime Responsibility** is implementation-neutral, has an operational material-effect test, and is explicitly distinguished from risk severity; the category figure classifies by whether such a responsibility depends partly on probabilistic Model Judgment and shows orchestration topology, autonomy, and delegated authority as independent dimensions.
- [ ] **Thinking** is explicitly functional and non-anthropomorphic, with no claim about consciousness or human-like cognition.
- [ ] **Article §7** acknowledges established antecedents and intellectual context, distinguishes conceptual continuity from equivalence or direct derivation, and scopes UA's proposed contribution without claiming novelty for generic control-loop or socio-technical safety primitives.
- [ ] The article explains why broader labels such as AI-based system do not provide the narrower consequential-responsibility boundary and does not claim that UA discovered the broader SE-for-AI problem space.
- [ ] Evidence maturity is explicit: repository rigor is not empirical validation, and the next validation threshold is practical application, failure/correction traces, baseline-reconstruction evidence, fallback/common-mode/capacity/restoration evidence, evidence-instrument validity traces, negative-case learning traces, proportionality tests, landscape corrections, reproducible semantic-equivalence/substitution cases, practical-overhead comparisons, immutable mapping-snapshot reruns, cross-project comparison, and revision under contradictory evidence.
- [ ] Decision levels and capability families remain orthogonal.
- [ ] Constraint and Constraint Realization remain distinct.
- [ ] Project Authorization, DoR, DoD, Release Gate, runtime correction, and Project Reauthorization remain separate.
- [ ] Project Constraint Architecture and Constraint Realization Map remain canonical repository concepts without being presented as mandatory publication artifacts.
- [ ] Runtime evidence and proposed authority changes are not conflated.
- [ ] Platform implementation and decision authority remain separate.
- [ ] Illustrative material is not presented as independent validation.
- [ ] Source authority, external-evidence rules, maturity boundaries, and publication framing remain accurate.
