---
title: "Article Blueprint Companion — Adjacent Landscape and Substitution Analysis"
artifact_type: research-note
status: research
maturity: draft
module: research
topics:
  - thinking-systems
  - control-loop
  - governance
  - tooling
  - standards
  - landscape
tags:
  - ua/module/research
  - ua/type/research-note
  - ua/status/research
  - ua/topic/thinking-systems
  - ua/topic/control-loop
created: 2026-08-11
updated: 2026-08-11
language: en
license: CC-BY-4.0
draft: true
---

# Article Blueprint Companion — Adjacent Landscape and Substitution Analysis

> **Status:** Detailed editorial memory for the landscape section of `open-engineering-specification-article-draft.md`. This is non-normative research planning, not article prose, not a market report, and not a specification source. It exists to preserve the comparison logic, source boundaries, claim-safety rules, figure contract, and unresolved questions before manuscript drafting. It must be reconciled into the main article blueprint during the next manuscript-writing iteration rather than treated as an independent publication.

## 1. Why this section exists

The article needs an explicit answer to a predictable reader objection:

> Why is another engineering map needed when teams already have agent runtimes, guardrails, evaluation and observability systems, managed AI platforms, governance suites, standards, risk frameworks, and control-theoretic research?

The answer must not be that the ecosystem lacks controls. It already contains many important control capabilities and, in some cases, sophisticated lifecycle and governance mechanisms.

The stronger publication claim is:

> **The landscape already contains many of the necessary capabilities. The unresolved engineering problem is how to know which capabilities are required, under whose authority, for which decision horizon, with what guarantee strength, evidence, corrective path, economics, and reassessment semantics.**

The landscape section therefore has three jobs:

1. show what adjacent approaches genuinely contribute;
2. map those contributions onto the UA operating map without pretending UA implements them;
3. expose responsibilities that remain outside an approach's normal scope and therefore must be supplied elsewhere in the system.

The section must not become a vendor comparison, competitive battlecard, literature-review detour, or claim that UA is categorically more rigorous than the field.

## 2. Placement in the eight-section article

The intended late-paper sequence is:

1. Sections 1–4 derive the controlled-object shift, capability anatomy, and four decision horizons;
2. Section 5 explains proportional application without requiring one artifact package;
3. **Section 6 maps adjacent research, tools, platforms, governance systems, standards, and regulation onto the operating map and asks what they can substitute for;**
4. Section 7 introduces UA as the open engineering synthesis after the landscape has been acknowledged;
5. Section 8 closes with falsification and validation questions, including whether existing approaches make parts of UA redundant.

The landscape belongs late in the argument because readers must understand the controlled object, four capability families, four decision horizons, authority/evidence routing, and proportionality before a comparison can be meaningful.

Do not introduce UA as the premise used to judge the market. Derive the engineering questions first, then use those questions as the comparison lens.

## 3. Relationship to early NIST / ISO / standards references

The current manuscript already uses NIST AI RMF and ISO/IEC TR 29119-11 in the early category/terminology discussion. That early use has a different editorial function and should not be deleted merely because Section 6 later discusses the landscape.

### Early-section function

Early references establish that broader categories such as `AI system` or `AI-based system` already exist and are useful, while explaining why the paper needs the narrower **Consequential Runtime Responsibility + Model Judgment** boundary for its specific engineering argument.

They answer:

> Why introduce the Thinking System category rather than simply reuse a broad existing AI-system label?

They must remain compact and must not become an early governance-framework comparison.

### Section 6 function

Section 6 asks a different question:

> Given the control problem derived by the paper, what do existing research traditions, tools, platforms, governance systems, standards, and regulation already cover, and what responsibilities remain outside their normal scope?

NIST may therefore appear in both places, but it must not receive the same explanation twice.

- **Early NIST/ISO mention:** category and terminology boundary.
- **Late NIST/ISO/AI Act treatment:** functional landscape mapping, authority/evidence relationship, and substitution analysis.

ISO/IEC 42001 and the EU AI Act belong primarily in the late landscape/organizational-authority discussion unless another earlier claim specifically requires them. Do not force them into the opening simply to make the source list symmetrical.

### Anti-duplication rule

When drafting Section 6, refer back to the earlier category discussion where useful and add only the new dimension. Do not re-explain what an AI system is, re-run the Thinking System naming argument, or repeat the early NIST/ISO paragraph.

## 4. Core landscape claim and tone

### Required core claim

> **Existing approaches cover substantial parts of the Thinking-System control problem, sometimes very well. Their blind spots arise primarily at boundaries between capability, authority, lifecycle decision ownership, guarantee semantics, evidence routing, and economics. UA is intended to provide a common map across those boundaries rather than replace tools that already implement pieces of them.**

### Strong publication paragraph to preserve conceptually

The section should communicate the following idea in publication prose, although wording may change after source verification:

> The surprising problem is not that the ecosystem lacks controls. Teams can assemble orchestration, guardrails, evaluation, observability, governance workflows, identity controls, and compliance processes and still have no explicit answer to who owns a consequential decision, what guarantee is actually being claimed, which evidence can invalidate authorization, which level must respond, or whether the resulting control perimeter makes the system worth building. The gap is therefore not another missing component. It is the architecture connecting components to authority and lifecycle decisions.

### Tone rule

Treat adjacent work as useful engineering input, not strawmen.

Do not write:

- “agent frameworks are plumbing”;
- “guardrails are only filters”;
- “observability tools only observe”;
- “governance platforms are dashboards”;
- “standards are disconnected from engineering”;
- “NIST/ISO only tell managers to manage risk”;
- “no existing framework spans the full problem” as an unqualified universal statement;
- “UA is the first”;
- “UA is more rigorous than all existing public work”;
- “Big Tech has no equivalent”;
- “existing tools ignore control.”

Prefer:

- “this approach covers substantial parts of…”;
- “within the cited comparison set, we have not identified one source that combines…”;
- “the remaining responsibility is…”;
- “this tool can implement…”;
- “the tool does not by itself establish…”;
- “UA proposes a synthesis…”;
- “this mapping is itself a claim to be challenged by maintainers and practitioners.”

## 5. Stable comparison lens

Every named approach or approach family must be evaluated through the same lens. Do not compare marketing feature lists.

For each category ask:

1. **Controlled object** — what does the approach primarily treat as the object of management or control: model, prompt, agent run, application, deployment, AI use case, organizational management system, or another object?
2. **Primary function** — orchestration, evaluation, enforcement, observability, runtime assurance, governance, compliance, risk management, etc.
3. **Capability-family coverage** — what can it contribute to Constraint/Realization, Sensor, Controller, and Actuator functions?
4. **Decision-horizon coverage** — where does it materially contribute across Organization, Project/Architecture, Delivery, and Runtime?
5. **Authority semantics** — does it establish legitimate decision ownership, represent delegated authority, or merely provide a mechanism through which an already-authorized decision can be executed?
6. **Guarantee semantics** — does it distinguish deterministic prevention/rejection from probabilistic influence, and can a claimed Hard boundary be traced through a complete realized path?
7. **Evidence routing** — does it define which evidence reaches which decision owner, at what latency, and what decision basis that evidence may invalidate?
8. **Lifecycle reassessment** — does it define changed assumptions, reauthorization, redesign, scope narrowing, suspension, or No-Go semantics?
9. **Human Authority** — is human involvement merely an approval/pause interface, or are information, expertise, capacity, latency, and real decision power represented?
10. **Control economics** — does the approach make the complete cost of control part of project viability rather than only reporting platform/model/runtime cost?
11. **Implementation versus authority** — which decisions can the approach technically execute without being the legitimate source of those decisions?
12. **Substitution inside UA** — which UA implementation responsibilities could this approach credibly carry so that no duplicate UA-specific mechanism should be built?
13. **Residual responsibility** — what still has to be supplied elsewhere in the socio-technical system?

This lens is a publication discipline, not a scoring framework. Do not turn it into maturity points, red/amber/green vendor ratings, or a procurement scorecard.

## 6. Landscape family A — control-theoretic research around LLMs and AI systems

Distinguish at least two research directions rather than treating “control theory for LLMs” as one thing.

### A. LLM as controlled stochastic/dynamical object

Relevant work may formalize prompts, context, hidden/internal state, trajectories, reachability, controllability, stability, steering, or intervention as control problems.

Publication purpose:

- acknowledge that applying control theory to LLMs is not a UA invention;
- identify mathematical contributions that may strengthen Runtime or Project/Architecture reasoning;
- avoid pretending a software operating model and a mathematical controllability result answer the same research question.

Likely UA mapping:

- strongest at Runtime;
- potentially important at Project/Architecture for feasibility and guarantee claims;
- may contribute Sensor, Controller, Actuator, and realization mechanisms for specifically formalized boundaries.

### B. LLM as or inside the controller of another system

This includes work where an LLM participates in control of robots, physical systems, infrastructure, or other dynamical environments.

Again, treat this as a different controlled object and research question.

### Comparison boundary

Do not say academic control theory “has no SDLC.” State instead:

> Such work generally studies a narrower mathematical or application-specific control problem and does not necessarily attempt to define the complete socio-technical decision architecture by which an organization establishes admissibility, a project decides whether Model Judgment is justified, delivery proves a bounded realization releasable, runtime evidence triggers reassessment, and control cost can veto the project.

### Novelty safety

Never claim:

> UA is the first application of control theory to LLMs.

The defensible claim is:

> UA's proposed contribution is not applying control theory to LLMs as such, but using control-loop distinctions as one part of a broader software/system-engineering operating map for Thinking Systems.

### Source plan

At minimum verify and cite the primary paper commonly referenced as *What’s the Magic Word? A Control Theory of LLM Prompting* and one or two sufficiently distinct, current control/LLM works if needed to establish breadth. Do not pad the bibliography with superficially similar papers.

## 7. Landscape family B — agent and orchestration frameworks

Representative examples may include LangGraph, AutoGen, Semantic Kernel, CrewAI, and the OpenAI Agents SDK. Do not create a long vendor catalogue; three to five representative examples are enough if their first-party documentation supports materially different functions.

### What these frameworks genuinely solve

Depending on the product and version, they may provide:

- execution graphs and workflow orchestration;
- state and persistence;
- durable execution;
- retries and resumability;
- handoffs and routing;
- tool invocation;
- memory/context management;
- human interruption and approval;
- tracing hooks;
- guardrails or validation hooks;
- distributed or multi-agent runtime mechanisms.

These are meaningful implementation capabilities. Do not dismiss them as “plumbing.”

### Likely UA mapping

Usually strongest in Delivery and Runtime, with possible Project/Architecture relevance through topology and feasibility.

Capability-wise they may implement:

- Actuator infrastructure;
- bounded Controller logic;
- some Constraint Realizations;
- Sensor/tracing hooks;
- Human Authority interfaces.

### Critical authority distinction

Preserve this idea explicitly:

> **A workflow graph can encode a decision, but its existence does not establish that the graph has legitimate authority to make that decision.**

A human-in-the-loop API may support `pause → approve → resume`, but that alone does not answer:

- who has the right to approve;
- what evidence the person receives;
- whether the person has adequate expertise;
- whether the person has enough time;
- whether approval capacity survives production volume;
- which outcomes the person can actually change;
- what happens when the reviewer is unavailable;
- whether the economics of that review path remain viable.

Use a current first-party example, such as a durable approval flow for sensitive tool calls, only after verifying current documentation. Present it as a **Human Authority realization primitive**, not as evidence that the product owns the authority semantics.

## 8. Landscape family C — runtime guardrails and enforcement

Representative examples may include NVIDIA NeMo Guardrails, Guardrails AI, Amazon Bedrock Guardrails, Microsoft Foundry guardrail mechanisms, Google Model Armor, or equivalent current products. Select a small representative set based on current first-party documentation.

### What they genuinely solve

Modern guardrail products may operate at multiple intervention points, including:

- input screening;
- retrieval checks;
- dialog/output checks;
- tool-call or execution checks;
- tool-response checks;
- policy/classifier evaluation;
- block/reject/rewrite/filter actions;
- content/security/safety checks.

Do not describe the category as only “output filtering.”

### UA mapping

A product marketed as a guardrail may perform several UA functions simultaneously:

- Constraint Realization;
- Sensor;
- local Controller logic;
- Actuator.

This is an important example of why UA classifies by **function in the specific system**, not product category.

### Residual questions

Even a technically strong guardrail does not automatically establish:

- the authoritative source of the Constraint;
- whether the claim is Hard or Soft across the complete realized path;
- who may change the configuration;
- whether a local block is sufficient for Project Authorization;
- when repeated violation invalidates architecture or economics;
- which decision horizon owns the response;
- whether the guardrail itself is degraded, bypassable, or operating outside assumptions.

Do not say “guardrails do not control.” Say they may implement substantial control capabilities while leaving cross-level authority and reassessment responsibilities elsewhere.

## 9. Landscape family D — evaluation and observability

Representative examples may include LangSmith, Arize Phoenix, TruLens, and equivalent current systems.

### What they genuinely solve

Depending on the product and version:

- tracing and run inspection;
- offline and online evaluation;
- datasets and experiments;
- production monitoring;
- alerts;
- evaluator pipelines;
- regression detection;
- quality/cost/latency evidence;
- sometimes automated actions or guardrails.

### UA mapping

Strongest as **Sensors and Evidence**, with some products also implementing bounded Controller logic and Actuators.

### Core distinction

Preserve this paragraph conceptually:

> **A rich Sensor surface does not by itself define the decision architecture that consumes the evidence.** An online evaluator may detect a regression, but the system still needs to know who may block release, whether the evidence represents a Delivery defect or Project-level invalidation, whether evaluator uncertainty is acceptable for the consequence, what decision latency is required, and what action follows.

Additional questions:

- who owns the threshold;
- who may change the evaluator;
- how evaluator drift is detected;
- whether the evaluator is independent enough for the claim;
- whether false positives/negatives are part of control economics;
- whether evidence reaches the right Controller in time.

UA should not duplicate LangSmith/Phoenix/TruLens telemetry. The map should explain why a Sensor exists, what decision it supports, and where the evidence routes.

## 10. Landscape family E — managed AI and agent platforms

This category is required because integrated cloud/agent platforms are a stronger technology substitute than a narrow orchestration library.

Representative examples may include Microsoft Foundry, Amazon Bedrock, Google Cloud AI/agent services, OpenAI's agent stack, or comparable current managed systems. Verify exact capabilities immediately before publication.

### What they may provide

Potentially:

- model access/hosting;
- agent runtime;
- identity and RBAC;
- tool permissions;
- network isolation;
- tracing and observability;
- evaluations;
- guardrails;
- deployment/versioning;
- workflow/orchestration;
- policy enforcement;
- human approval mechanisms.

### Why this category matters

A sufficiently integrated platform may appear to provide “the control plane already.” The article must take that objection seriously.

### UA mapping

Managed platforms may implement large portions of all four capability families, particularly at Delivery and Runtime, and may also support organizational/project evidence workflows.

### Remaining decision ownership

Platform completeness does not by itself determine:

- whether the use case is organizationally admissible;
- whether Model Judgment is justified for the business outcome;
- whether the allowed authority/exposure is acceptable;
- who may accept residual exposure;
- which organizational source is authoritative;
- whether Human Authority capacity is viable;
- whether the complete control perimeter destroys project economics;
- whether runtime evidence invalidates Project Authorization;
- whether an exception is legitimate.

Preserve the key argument:

> **As platforms become more capable at implementing control mechanics, the need to make authority and decision ownership explicit does not disappear. Capability concentration can make those semantics more important because more consequential functions are now executable through one platform.**

Do not imply that platform consolidation is necessarily bad. It can reduce integration cost and improve evidence continuity; it can also create common-mode dependency and concentrated configuration authority that must be controlled.

## 11. Landscape family F — enterprise AI governance platforms

This category is distinct from standards and from runtime guardrails.

Representative systems may provide:

- AI use-case/model/agent inventory;
- risk/compliance workflows;
- factsheets or governance records;
- evaluations and monitoring;
- thresholds;
- approval workflows;
- regulatory/control mappings;
- audit evidence;
- lifecycle governance.

IBM watsonx.governance is one possible representative example if current first-party documentation supports the required claims. Other platforms may be substituted based on source quality and current capability.

### UA mapping

Potentially strong at Organization and Project/Architecture, with evidence connections into Delivery/Runtime.

They may implement:

- governance records;
- Sensor/evidence aggregation;
- Controller workflow;
- policy/control objects;
- lifecycle decision records.

### Comparison boundary

Do not say governance platforms are “only dashboards” or disconnected from runtime. Some integrate evaluations and monitoring deeply.

The narrower UA question is:

> Are the governance objects and workflows connected to the actual scoped Constraint Realizations, Runtime Actuators, delegated authority, and the decision horizon whose basis may be invalidated?

A governance platform can therefore be a strong **UA implementation surface**, not necessarily a competitor in an either/or sense.

## 12. Landscape family G — standards, management frameworks, and regulation

Treat these as different authority/context objects, not one homogeneous category.

### NIST AI RMF

Use current NIST primary sources. Recognize that AI RMF is lifecycle-oriented and includes governance, mapping, measurement, and management rather than reducing it to abstract policy.

Section 6 should not repeat the early manuscript's category-label discussion. Here NIST is mapped functionally: it can supply risk-management structure, organizational expectations, evidence/measurement practices, and decision context.

### ISO/IEC 42001

Use the official ISO source. Treat it as an AI management-system standard with management-system and continual-improvement implications, not as a software architecture specification.

### EU AI Act

Treat it as law/regulation, not as an engineering framework. Where applicable, it can create authoritative Requirements, Constraints, documentation, monitoring, human-oversight, risk-management, and corrective-action obligations.

Do not flatten legal obligations into UA terminology as though the Act “uses UA.” The relationship is translation:

```text
law / standard / organizational policy
→ organizational authoritative source / obligation
→ scoped Project Requirement, Constraint, assumption, or evidence obligation
→ technical/socio-technical realization
→ Sensor/evidence
→ Controller decision
→ Actuator/corrective path
→ reassessment where the decision basis changes
```

### Core distinction

Preserve both directions:

> **Compliance is not identical to control, and control is not identical to compliance.**

Possible cases:

- a formally compliant process with weak operational control architecture;
- a locally well-controlled system that violates an organizational or legal Requirement;
- a technically effective enforcement mechanism whose business authority is undefined;
- a governance workflow with no adequate Sensor/Actuator path.

The point is connection, not dismissal.

## 13. Coverage matrix / figure contract

Create a conceptual matrix or coverage-band figure titled approximately:

**Adjacent approaches mapped onto the UA operating map**

Do not use vendor logos or a G2-style scorecard.

Candidate rows:

- control-theoretic research;
- orchestration frameworks;
- runtime guardrails;
- evaluation/observability;
- managed AI/agent platforms;
- enterprise governance platforms;
- standards/regulation;
- UA map/reference model.

Candidate columns should expose both orthogonal dimensions without pretending to produce precise scores:

- Organization;
- Project/Architecture;
- Delivery;
- Runtime;
- Constraints/Realizations;
- Sensors;
- Controllers;
- Actuators;
- control economics / viability.

Use qualitative labels such as `primary`, `material`, `implementation support`, `outside normal scope`, or equivalent. Avoid numeric scores.

### Required disclaimer

> **Coverage indicates where an approach can contribute capabilities, authority structure, evidence, or decision support. It does not imply inferiority, exclusivity, maturity ranking, or that UA itself implements those functions. Blind spots refer to responsibilities that normally remain outside the approach and must be supplied elsewhere in the socio-technical system.**

The UA row must not be “all green” as though UA were a product with every feature. It should be visually differentiated as **map / decision model / integration reference**, not implementation coverage.

The matrix is a hypothesis based on a bounded comparison set and current documentation. It must be dated or otherwise framed as publication-time evidence because platform capabilities change quickly.

## 14. Substitution test — “Can I just use X instead of UA?”

This subsection is required because it converts the landscape from thought leadership into a practical engineering test.

### Required answer

Potentially yes. UA does not require UA-branded tooling or duplicate artifacts.

If an organization's existing combination of standards, architecture practice, IAM, agent platform, guardrails, evaluation, observability, release controls, incident management, governance workflows, and decision records already preserves the necessary semantics, no duplicate UA mechanism should be added merely for branding.

The team should still be able to answer:

```text
What is the controlled object?
What Consequential Runtime Responsibility depends on Model Judgment?
What is authorized, and by whom?
Which Requirements and Constraints apply?
How are the Constraints realized?
Which claims are actually Hard, and along which complete realized path?
What evidence reaches which Controller?
At what latency must the decision be made?
Which Actuator can correct or narrow operation?
What remains reserved to Human Authority?
Does Human Authority have adequate information, capacity, latency, expertise, and power?
What evidence triggers Delivery repair, Project Reauthorization, or Organizational reassessment?
When does Project Authorization become invalid?
What does the complete control perimeter cost?
Is Model Judgment still economically and operationally justified after that cost is included?
```

If the existing stack answers these questions credibly, it may already implement the required control architecture. UA then functions as a **diagnostic/reference model**, not an additional software layer.

If it cannot answer them, the gap should be described as a missing decision/control responsibility—not automatically as a need to buy or build an “UA component.”

## 15. What UA is actually competing with

Do not use “competitors” as the publication heading unless editorial context makes it unavoidable. Preserve the distinction internally.

### Conceptual substitutes

Potentially:

- systems engineering and safety-engineering methods;
- AI risk frameworks;
- mature internal architecture/governance methods;
- future IEEE/SEI/industry engineering frameworks;
- other cross-lifecycle AI system methods.

### Implementation substitutes

Potentially:

- integrated agent/cloud platforms;
- governance suites;
- guardrail/evaluation/observability stacks;
- internal control platforms.

These substitute for implementation surfaces, not necessarily the conceptual map.

### Organizational substitutes

A mature organization may already possess an internal method that integrates authoritative sources, architecture decisions, release controls, runtime evidence, incident response, reauthorization, and economics. Such a method may make UA redundant for that organization.

### Real competitive test

Preserve this idea:

> **The meaningful substitute for UA is another coherent method that connects controlled-object definition, capability functions, lifecycle decision ownership, evidence routing, authority, guarantee strength, and economics with equal or lower conceptual overhead.**

If such a method already exists or emerges, the article should treat it as evidence against UA's distinctiveness, not as a branding threat.

## 16. Section 7 consequence — contribution boundary after the landscape

After Section 6, the UA introduction must change tone.

Do not say:

> Existing approaches are fragmented, therefore UA is the solution.

Prefer:

> Many elements of the map are already implemented by mature disciplines, standards, and platforms. UA does not claim to invent those elements. Its proposed contribution is to connect them around one controlled object and an explicit cross-level decision architecture.

### UA does not claim invention of

- feedback loops;
- Sensors/observability;
- Controllers;
- Actuators;
- Constraints or policy enforcement as generic ideas;
- guardrails;
- policy-as-code;
- human approval;
- runtime assurance;
- AI risk management;
- control theory;
- agent orchestration;
- management systems;
- socio-technical safety;
- the broad observation that AI changes software engineering.

### UA proposed synthesis to describe carefully

Subject to source validation and without “first” claims, the paper may present the proposed synthesis around:

- the Thinking System engineering category;
- Consequential Runtime Responsibility;
- Model Judgment inside the controlled object;
- the four control-capability families as functional distinctions;
- the four decision horizons;
- downward authority/Constraint concretization and upward evidence/invalidation;
- complete realized-path discipline for Hard/Soft claims;
- Project-level control economics and Architecture Veto/No-Go reasoning;
- proportionality through full-map inspection before simplification;
- connected socio-technical control architecture across lifecycle decisions.

Use **proposed contribution**, **proposed synthesis**, or **within the bounded comparison set**. Do not use **first**, **unique**, or **no one else** without a defensible systematic literature/market review.

## 17. Section 8 consequence — landscape falsification questions

Add explicit landscape challenges to the final validation agenda:

1. Is there an existing framework that already connects the four decision horizons more completely than the paper acknowledges?
2. Are there platforms that operationalize authority, evidence routing, and reassessment in ways this mapping understates?
3. Does a mature NIST/ISO/enterprise-governance implementation make parts of UA redundant?
4. Are the four capability families too coarse to map modern integrated agent platforms accurately?
5. Which UA distinctions add real decision value when teams already use an integrated cloud/governance stack?
6. Where does UA merely rename an established systems-engineering or safety-engineering concept without improving usability?
7. Can a simpler combination of existing standards, internal architecture practice, and tooling produce the same result with less conceptual overhead?
8. Which approach families are mapped unfairly because their scope has expanded since the cited documentation was reviewed?
9. Does the substitution test identify genuine missing responsibility, or does it create unnecessary terminology around decisions mature teams already make naturally?

The desired outcome is not proof that UA has no competitors. It is evidence about which parts of UA are useful, redundant, incorrectly scoped, or missing.

## 18. External source plan

Named product and current-standard claims must use current first-party or primary sources immediately before manuscript publication. Product capabilities change quickly; do not rely on old UA articles or memory for current features.

### Academic control / LLM

- primary paper for *What’s the Magic Word? A Control Theory of LLM Prompting*;
- one or two materially distinct current papers if needed to demonstrate breadth;
- do not infer “the field” from a single paper.

### Orchestration / agent runtimes

Candidate first-party sources:

- LangGraph official documentation;
- Microsoft AutoGen official documentation;
- Microsoft Semantic Kernel official documentation;
- OpenAI Agents SDK official documentation;
- CrewAI official documentation if it adds a distinct capability claim.

### Guardrails / runtime enforcement

Candidate first-party sources:

- NVIDIA NeMo Guardrails;
- one or two managed guardrail products such as Microsoft Foundry, Amazon Bedrock Guardrails, or Google Model Armor;
- Guardrails AI if materially useful.

### Evaluation / observability

Candidate first-party sources:

- LangSmith;
- Arize Phoenix;
- TruLens.

### Managed AI / agent platforms

Use a bounded representative set and current first-party architecture/security/observability documentation. Do not turn the paper into a cloud feature comparison.

### Enterprise governance

Use one or two representative current first-party sources, potentially including IBM watsonx.governance, only for capabilities explicitly documented.

### Standards / regulation

- NIST AI RMF 1.0 and relevant NIST Playbook material;
- ISO/IEC 42001 official ISO overview/source;
- EU AI Act official legal text and/or European Commission guidance appropriate to the claim;
- preserve the existing ISO/IEC TR 29119-11 reference where it supports the early category/SE-for-AI discussion rather than forcing it into a management-system role.

### Source discipline

- date-check product documentation;
- prefer primary documentation over vendor blogs when architecture docs exist;
- distinguish product feature claims from interpretation through the UA lens;
- do not cite UA repository material as evidence of what an external product, standard, or law currently does;
- do not imply endorsement by a vendor, standards body, researcher, or regulator merely because their work is mapped into UA terminology.

## 19. Known risks and unresolved editorial decisions

Preserve these questions until manuscript drafting and source review resolve them:

1. **Section length risk:** landscape coverage can easily overwhelm the article. Keep the argument about categories and boundaries; use named products as evidence, not as the structure of the section.
2. **Rapid product drift:** managed platforms and guardrail/observability products may change between drafting and publication. Keep vendor-specific prose narrow and date-sensitive.
3. **False novelty risk:** a bounded source set cannot prove no equivalent cross-lifecycle framework exists.
4. **Strawman risk:** adjacent products increasingly span orchestration, guardrails, evaluation, identity, observability, and governance; avoid old category assumptions.
5. **Category overlap:** one platform may belong to several landscape families. Classify a capability by function rather than forcing each vendor into one box.
6. **Authority ambiguity:** some governance products genuinely encode roles/approval rights. The distinction is not “tool has no authority”; it is whether the represented authority is legitimately sourced and connected to the actual controlled system.
7. **Hard/Soft translation:** external products may use “hard guardrail,” “policy,” “constraint,” or “control” differently. Do not silently map marketing terminology to UA guarantee semantics.
8. **NIST duplication:** preserve early NIST use for category/context and late NIST use for functional landscape mapping; do not repeat the same explanation.
9. **ISO confusion:** ISO/IEC TR 29119-11 and ISO/IEC 42001 serve different purposes. Do not treat them as interchangeable “ISO AI governance.”
10. **EU AI Act category error:** law creates obligations; it is not a competing software architecture framework.
11. **Matrix oversimplification:** coverage cells may imply precision or maturity ranking that the evidence does not support. Prefer qualitative bands and an explicit disclaimer.
12. **UA all-green problem:** never make UA look like a product that implements every capability. Its role in the matrix is mapping/integration semantics.
13. **Control-economics evidence:** the landscape section may find adjacent cost/risk methods. Incorporate them rather than protecting UA terminology.
14. **Enterprise maturity:** a mature internal architecture/governance method may already perform the integration UA proposes. State this possibility explicitly.
15. **Publication scope:** if Section 6 becomes too long, move detailed vendor mappings to an appendix/repository research note while preserving the comparison lens, representative examples, matrix, and substitution test in the article.

## 20. Rejected formulations

Reject or rewrite the following even if they appear rhetorically attractive:

- “There are no competitors.”
- “No existing work crosses the whole distance from control theory to SDLC and business economics.”
- “Academic work is pure mathematics with no practical relevance.”
- “Agent frameworks are plumbing.”
- “Guardrails provide sensors and brakes but no control.”
- “Observability is only telemetry.”
- “Governance frameworks are for lawyers and managers, not engineers.”
- “NIST and ISO are detached from code.”
- “The EU AI Act only declares that risks must be managed.”
- “Big Tech could become a competitor if it eventually discovers systems engineering.”
- “UA is qualitatively more rigorous than all public alternatives.”
- “UA uniquely combines these ideas.”
- “Using LangGraph/LangSmith/NIST cannot solve this problem.”

Replace the adversarial framing with scoped functional claims and the substitution test.

## 21. Drafting acceptance criteria for the landscape section

Before the manuscript landscape section is considered complete:

- [ ] The current manuscript was reread so early NIST/ISO references are not duplicated.
- [ ] Early standards references remain focused on category/terminology context; Section 6 adds functional mapping rather than repeating them.
- [ ] At least the following approach families are considered: control-theoretic research, orchestration, guardrails, evaluation/observability, managed AI/agent platforms, enterprise governance platforms, standards/regulation.
- [ ] Each family is evaluated through the stable comparison lens rather than marketing categories.
- [ ] Named current product claims are verified against first-party documentation.
- [ ] NIST, ISO/IEC 42001, and EU AI Act claims use primary/authoritative sources and are not treated as interchangeable artifacts.
- [ ] The section acknowledges substantial capabilities in adjacent approaches before describing residual responsibilities.
- [ ] No universal “first,” “only,” “none,” “all,” or exhaustive market claim is made without evidence that supports it.
- [ ] The article does not call agent frameworks plumbing or reduce guardrails to output filters.
- [ ] Human-in-the-loop implementation is distinguished from substantive Human Authority.
- [ ] Technical ability to execute a decision is distinguished from legitimate authority to make it.
- [ ] Guardrail product labels are decomposed into Constraint Realization / Sensor / Controller / Actuator functions where relevant.
- [ ] Observability is connected to a consuming Controller and decision path rather than dismissed as telemetry.
- [ ] Integrated platforms are treated as serious partial substitutes and their common-mode/concentration implications are considered without assuming they are harmful.
- [ ] Governance platforms are treated as possible UA implementation surfaces rather than caricatured as dashboards.
- [ ] Standards/regulation are mapped as sources of Requirements, Constraints, evidence obligations, and assurance expectations where appropriate rather than as competing software frameworks.
- [ ] Compliance and control are explicitly distinguished in both directions.
- [ ] A coverage matrix/figure includes a disclaimer that coverage is not a maturity or superiority score.
- [ ] UA is visually represented as map/integration semantics, not as an all-capabilities product.
- [ ] The substitution test explicitly allows an existing stack to make additional UA-specific tooling/artifacts unnecessary.
- [ ] The section states what residual responsibility remains after a tool/framework is used.
- [ ] Section 7's UA contribution claim is narrowed after the landscape and does not claim invention of generic control, safety, governance, or orchestration concepts.
- [ ] Section 8 includes landscape falsification questions capable of showing UA is redundant, too complex, incomplete, or unfairly differentiated.
- [ ] The section remains subordinate to the paper's main argument rather than becoming a market survey.
- [ ] The main article blueprint is reconciled with this companion memory after manuscript drafting so the two cannot drift indefinitely.

## 22. Intended transition into UA

The landscape section should end by creating the need for Section 7 without claiming victory over adjacent work.

Suggested conceptual transition:

> The ecosystem therefore does not lack mechanisms. It lacks, or distributes across several disciplines and products, the semantics that connect those mechanisms to one controlled object, legitimate decision ownership, guarantee strength, evidence routing, reassessment, and viability. A team may already possess all of those semantics through existing methods and tools; if so, it should not duplicate them. The remaining question is whether a common map makes those relationships easier to inspect, challenge, and preserve. That is the role proposed for Uncertainty Architecture.

Do not copy this paragraph mechanically if the manuscript develops a better transition, but preserve its logic.
