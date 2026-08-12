from pathlib import Path

manuscript = Path('content/research/notes/open-engineering-specification-article-draft.md')
text = manuscript.read_text()
start = text.index('## 3. From Model Quality to Bounded Control')
end = text.index('\n## 4. Four Decision Levels for Thinking Systems', start)

new_section = '''## 3. From Model Quality to Bounded Control

The controlled-object shift changes what counts as sufficient engineering evidence. Once a **Consequential Runtime Responsibility** depends partly on probabilistic Model Judgment, teams naturally invest in measurement: test sets, evaluators, traces, model comparisons, cost and latency monitoring, incident data, and downstream outcome analysis. All of that is necessary. None of it, by itself, establishes control.

Measurement answers questions such as *what happened, how often, under which conditions, and with what confidence?* Control adds different questions: *relative to which approved boundary, who or what may decide that action is required, which action can actually change operation, and what happens when the assumptions behind the boundary no longer hold?*

A feedback loop becomes closed when evidence about the controlled process reaches a decision function and an authorized action can affect the process again:

```mermaid
flowchart LR
    R["Reference<br/>Requirement and intended conditions"]
    P["Thinking System<br/>controlled process"]
    S["Sensors and evidence"]
    C["Controller and decision authority"]
    A["Actuators"]

    R --> C
    P --> S --> C
    C -->|authorized action| A
    A -->|changes operation| P
```

**Figure 7 — A closed feedback loop.** Evidence reaches a decision function and an authorized action changes the controlled process. The figure deliberately does not yet claim that the loop operates inside a legitimate or adequately realized boundary.

A closed loop can still be unacceptable. It may optimize the wrong objective, react too slowly for the consequence, rely on evidence that misses the relevant failure, or possess authority that was never legitimately delegated. Its Actuator may be able to change a prompt but not prevent a transaction. It may keep an evaluator score inside tolerance while Human Authority, fallback capacity, latency, or unit economics collapse. Closing feedback is therefore weaker than bounding operation.

The running support-resolution system makes the distinction concrete. Suppose the organization permits automated low-value credits but requires **Human Authority** before a refund above a delegated amount can execute. The important engineering object is not the sentence “large refunds require approval.” The control problem is whether that authoritative boundary survives the complete path from Model Judgment to downstream transaction.

The four capability families describe the logical functions needed to make such a boundary operational. The order below is a pedagogical traversal, not a mandatory execution pipeline or physical stack.

### Actuators and corrective action

An **Actuator** executes an authorized change in operation or in a Constraint Realization. It is the part of the control path that can actually make the system behave differently.

In the support system, Actuators may block a transaction, route a case to Human Authority, narrow autonomous scope, switch to a manual path, disable refund execution, roll back a model or configuration, or compensate downstream state. A feature flag, API call, workflow step, deployment action, or human intervention is an Actuator only when it provides a real path from an authorized decision to changed operation.

The distinction from decision authority matters. A Controller decides or authorizes; an Actuator executes. One component may perform both, but treating them as the same concept hides who may decide, who may execute, what happens when execution fails, and what evidence proves that the requested change actually occurred. A Controller without an effective Actuator can diagnose but cannot correct.

### Constraints and their realizations

A **Constraint** is an approved condition limiting the allowed operating space. A **Constraint Realization** is the technical or socio-technical mechanism through which that condition is implemented, enforced or influenced, evidenced, and operated for a defined scope. They belong to one capability family because either side alone is incomplete: policy without realization is intent; realization without an authoritative Constraint is mechanism without a defensible boundary.

For the running example, an authoritative Constraint might state that refunds above the delegated amount must not execute without Human Authority. That statement is not yet a technical guarantee. A credible realization might combine transaction permissions, an amount precondition, an approval token or equivalent authorization state, and a transaction endpoint that rejects execution when the precondition is absent.

This is also where **Hard** and **Soft** must be separated carefully. A Hard Constraint is a scoped claim that the complete realized path deterministically prevents or rejects violation within stated assumptions, subject, path, scope, and enforcement boundaries. A prompt saying “never issue a refund above the threshold,” a natural-language policy, a model preference, or a probabilistic evaluator is not hard by itself. Those mechanisms may influence behavior, but they do not make the prohibited transaction unreachable.

Where a prohibited consequential state can feasibly be made unreachable through deterministic enforcement, deterministic realization should carry that boundary. Where deterministic prevention is not feasible, the remaining uncertainty should stay explicit rather than being renamed “Hard” because the business intent is important. The same business rule may therefore require separate records for a hard transaction boundary and a soft semantic boundary around customer communication.

### Sensors and evidence

**Sensors** produce evidence about behavior, outcomes, operating conditions, realization state, control health, Actuator execution, and the assumptions on which authorization depends.

For the refund boundary, useful evidence includes attempted and blocked high-value refunds, approval requests and outcomes, realization health, bypass attempts, downstream transaction results, false blocks, Human Authority queue size and latency, fallback load, and the state produced after an Actuator fires. Evaluators may also estimate semantic properties such as whether the model applied policy appropriately or whether a customer explanation is grounded.

A Sensor need not produce one objective truth value. Semantic acceptability may remain uncertain. Evidence must instead be fit for the decision it informs and expose coverage, uncertainty, latency, and blind spots. A detector that identifies a prohibited transaction only after settlement may be accurate and still be useless for prevention. An average-quality dashboard may be informative and still miss the low-frequency event that defines the relevant boundary.

Telemetry without a decision path is observation. Valuable observation is not yet control.

### Controllers and decision authority

A **Controller** compares or interprets evidence relative to approved Requirements, Constraints, assumptions, and a defined decision boundary, then selects or authorizes action. What makes something a Controller is not intelligence, automation, a dashboard, or a job title. It is ownership of a defined decision together with legitimate authority over the available response.

In the running example, one Controller function may determine that a transaction cannot proceed automatically and must be routed to Human Authority. Another may decide, from repeated realization failures or abnormal financial behavior, that autonomous refund execution should be disabled or narrowed. The associated Actuator performs that change. A dashboard presenting the evidence is not itself the Controller.

Controllers are often socio-technical. Human decision authority may be combined with automated evidence collection, invariant checks, routing, decision support, and bounded automated decisions where delegation permits them. **Human Authority** is substantive only when the person has enough information, time, competence, capacity, independence, and power to change the outcome. An approval button attached to an overloaded queue is not a complete control path.

Automation should remove repetitive sensing, checking, routing, evidence aggregation, and safe bounded response where evidence quality, failure behavior, reversibility, and delegated authority make the automated path credible. Maximum automation is not an independent objective. Automated Controller and Actuator behavior is itself part of the control architecture: its decisions, configuration, latency, failures, execution, and resulting state must remain observable and correctable.

Read together, the four families form a bounded control relationship: Controllers authorize Actuators; Actuators change operation or a Constraint Realization; Constraints define what changes and operating states are legitimate; Realizations enforce or influence those boundaries; Sensors expose behavior, outcomes, realization health, and action effects; evidence returns to Controllers.

```mermaid
flowchart LR
    R["Authorized intent,<br/>Requirement, and assumptions"]
    K["Constraints<br/>approved operating boundaries"]
    KR["Constraint Realizations<br/>enforce or influence the boundary"]
    P["Thinking System<br/>controlled process"]
    S["Sensors and evidence<br/>behavior · outcomes · conditions<br/>realization and execution state"]
    C["Controller and decision authority<br/>compare · interpret · authorize"]
    A["Actuators<br/>execute authorized change"]

    R --> C
    R --> K
    K --> KR
    K -. defines decision boundary .-> C
    K -. defines action boundary .-> A
    KR -. enforces or influences .-> P
    KR -. may gate .-> A
    P --> S
    KR -->|state, violations, and health| S
    A -->|execution state and effects| S
    S --> C
    C -->|authorized action| A
    A --> P
    A -->|change within delegated authority| KR
```

**Figure 8 — Complete bounded control architecture.** The four capability families are logical functions, not mandatory services, products, teams, layers, or one execution order. Realizations may act before, during, or after Model Judgment; Controllers and Actuators may be synchronous or asynchronous; one component may perform several functions.

This is the difference between a measured system, a closed feedback loop, and a bounded controlled system. The last requires not merely feedback but an approved and credibly realized operating boundary, evidence fit for the decisions being made, legitimate decision authority, effective corrective action, and a path for reassessment when the basis of control changes.

What is often called AI governance is therefore not a fifth capability family and not a post-hoc checkpoint. Governance becomes operational through this socio-technical control architecture. Until material boundaries are credibly realized, required evidence reaches legitimate decision authority, effective Actuators exist, Human Authority and fallback are viable where needed, and invalidated assumptions can trigger reassessment, the system may be demonstrable or testable but is not ready for production at the intended scope.

The capability anatomy explains **how** bounded control becomes possible. It does not yet determine **where** organizational authorization, project viability, delivery release, runtime correction, and reauthorization decisions belong. That is the role of the second model.
'''

manuscript.write_text(text[:start] + new_section + text[end:])

blueprint = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
b = blueprint.read_text()
marker = '**Working word budget:** 950–1,150\n\n---\n\n### 5.4 Four Decision Levels for Thinking Systems — the operating map'
if marker not in b:
    raise SystemExit('Section 5.3 blueprint marker not found')
decisions = '''**Accepted drafting decisions from the 2026-08-12 Section 3 rewrite:**

- Preserve the deduction sequence `measurement → closed feedback → bounded control`; do not present evaluation or observability as control by themselves.
- Reuse the bounded customer-support system as the primary explanatory object and introduce the refund-above-delegated-authority boundary here as the first concrete Constraint example.
- Use that same boundary to distinguish authoritative Constraint from Constraint Realization, Hard from Soft guarantee strength, Sensor evidence from Controller decision authority, and Controller authorization from Actuator execution.
- Prefer deterministic realization where a prohibited consequential state can feasibly be made unreachable; when prevention remains probabilistic, keep the residual uncertainty explicit rather than overstating the guarantee.
- Treat Human Authority as an architectural capability with information, time, competence, capacity, independence, and power requirements rather than as an approval UI.
- Make automation conditional on evidence quality, failure behavior, reversibility, and delegated authority; automated control remains part of the controlled architecture and must itself be observable and correctable.
- Keep the four-family order Actuators → Constraints and realizations → Sensors → Controllers as a pedagogical traversal only; Figure 8 expresses the actual relationship topology without implying one execution sequence.
- Close by separating the two models explicitly: capability anatomy explains how bounded control becomes operational; Section 5.4 explains where the relevant decisions are owned.

'''
b = b.replace(marker, decisions + marker, 1)
blueprint.write_text(b)
