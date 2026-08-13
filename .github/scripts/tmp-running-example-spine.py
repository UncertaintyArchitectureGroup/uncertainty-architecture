from pathlib import Path

DRAFT = Path('content/research/notes/open-engineering-specification-article-draft.md')
BLUEPRINT = Path('content/research/notes/open-engineering-specification-article-blueprint.md')

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 match, found {count}')
    return text.replace(old, new, 1)

m = DRAFT.read_text()
b = BLUEPRINT.read_text()

# Metadata dates
m = m.replace('updated: 2026-08-12', 'updated: 2026-08-13', 1)
b = b.replace('updated: 2026-08-12', 'updated: 2026-08-13', 1)

old_s2 = '''The running support-resolution example already contains this mixed structure. Retrieval, identity, permissions, tool access, and execution paths can remain deterministic while request interpretation, resolution selection, or response generation depends partly on Model Judgment. That is enough to change the controlled object even before the paper decides whether the resulting authority, evidence, Human Authority, fallback, and economics are adequate for production.
'''
new_s2 = '''### Running Example — The Controlled Object Expands

The bounded support-resolution system already contains this mixed structure. Retrieval, identity, permissions, tool access, and execution paths can remain deterministic while request interpretation, resolution selection, or response generation depends partly on Model Judgment. That is enough to change the controlled object even before the paper decides whether the resulting authority, evidence, Human Authority, fallback, and economics are adequate for production.

Now follow the consequential responsibility rather than the model boundary. If Model Judgment can influence which remedy applies, what the customer is told, whether a refund is proposed, or whether an authorized tool changes downstream business state, then the engineering perimeter cannot stop at the model-serving component. The controlled object includes the path by which runtime judgment becomes a consequential outcome and the people, permissions, evidence, and corrective mechanisms needed to keep that path inside an authorized boundary.

For a material case, that control perimeter may therefore become explicitly **socio-technical** and span several decision horizons:

```text
organizational authority and reserved decision rights
→ Project / Architecture authorization and control assumptions
→ Delivery realization, verification, and release evidence
→ Runtime sensing, decision, correction, and containment
↺ evidence routed back to the horizon whose decision basis it invalidates
```

In the running example, an organizational decision might permit automated refunds only inside a delegated amount and reserve larger transactions to Human Authority. Project / Architecture must decide whether Model Judgment is justified inside that boundary and whether a credible control perimeter can exist. Delivery must realize the transaction boundary, approval state, evidence, fallback, and release conditions. Runtime must observe attempted actions and control health, block or route transactions inside delegated authority, and return evidence when a local defect, project assumption, or organizational boundary is no longer credible.

This does **not** mean every Thinking System needs four departments, four committees, or a maximal governance stack. The same people or platform may carry several responsibilities, and lower-consequence systems may implement the map lightly. The point is causal: once probabilistic Model Judgment participates in a consequential responsibility, the required control perimeter follows the authority and effects of the **whole controlled object**, potentially all the way to organizational decision rights.
'''
m = replace_once(m, old_s2, new_s2, 'section2 running example')

old_s3 = '''The running support-resolution system makes the distinction concrete. Suppose the organization permits automated refunds up to a delegated amount but requires **Human Authority** before a refund above that amount can execute. The important engineering object is not the sentence “large refunds require approval.” The control problem is whether that authoritative boundary survives the complete path from Model Judgment to downstream transaction.

The four capability families describe the logical functions needed to make such a boundary operational. The order below is a pedagogical traversal, not a mandatory execution pipeline or physical stack.
'''
new_s3 = '''### Running Example — From Authority to a Complete Control Path

Take one boundary in the same support-resolution system: automated refunds are permitted only up to a delegated amount; above that amount, execution requires **Human Authority**. The important engineering object is not the sentence “large refunds require approval.” The control problem is whether that authoritative boundary survives the complete path from Model Judgment to downstream transaction.

The same boundary exposes all four capability families:

```text
Constraint
→ refunds above the delegated amount must not execute without Human Authority

Constraint Realization
→ transaction permission + amount precondition + valid approval state/token + rejecting endpoint

Sensors
→ attempted and blocked high-value refunds + approval outcomes + bypass attempts
  + realization health + downstream transaction result + Human Authority latency

Controller / decision authority
→ decide whether execution is authorized, whether the case must route to Human Authority,
  and whether repeated evidence requires narrowing or disabling autonomous refund execution

Actuator
→ block, route, narrow, disable, roll back, fallback, or compensate within delegated authority
```

If any part is missing, the sentence “large refunds require approval” has not yet become a complete control path. A policy without a credible realization can be bypassed; a realization without evidence can silently degrade; evidence without a legitimate Controller is observation; a Controller without an effective Actuator cannot correct the system.

The four capability families describe the logical functions needed to make such a boundary operational. The order below is a pedagogical traversal, not a mandatory execution pipeline or physical stack.
'''
m = replace_once(m, old_s3, new_s3, 'section3 running example')

old_s4 = '''For the running example, a broken refund precondition in one release is a Delivery problem if it can be repaired inside the authorized architecture. Evidence that no available realization can make the required transaction boundary credible is a Project problem. A proposal to raise the delegated refund amount beyond the organizational limit is an authority expansion and must return through Project to Organization rather than becoming a runtime configuration tweak.

### Cross-level operating discipline — learn from negative cases without turning every deviation into governance
'''
new_s4 = '''### Running Example — One Refund Case Across Four Decision Horizons

Use one concrete event to make the ownership model visible. Assume the support system may execute refunds automatically only up to **€50**, while larger refunds require Human Authority. The model proposes a **€450** refund for a customer case. The same event creates different questions at different horizons; the destination depends on which decision basis the evidence challenges.

| Horizon | Question exposed by the same case | Illustrative decision owner | Legitimate output or response |
|---|---|---|---|
| **Organization** | May this class of system ever exercise refund authority, and what authority must remain reserved? | The organizational authority that legitimately owns the commercial, financial, customer, security/privacy, or exception boundary; several bundles may sit with the same person in an SMB. | Permit, prohibit, condition, or change delegated refund authority; define reserved Human Authority and evidence obligations. |
| **Project / Architecture** | Is Model Judgment justified for this resolution path, and can a credible control perimeter keep the system inside the organizational boundary at viable cost and capacity? | Product/architecture/engineering decision authority operating inside the organizational boundary. | Project Authorization, Project Constraint Architecture, narrower scope, bounded research, redesign, defer, or No-Go. |
| **Delivery** | Has the €50 boundary actually been realized and evidenced for this release, and is this deployment acceptable? | Delivery/release decision authority within Project Authorization. | DoR/DoD/Release decisions; repair a bypassable guard, improve evidence, narrow the release, or escalate when the project basis is invalid. |
| **Runtime** | What happened in this case, did the realized boundary hold, and what correction is authorized now? | Runtime Controller and, where required, Human Authority within delegated authority. | Block the €450 execution, route the case, verify resulting state, narrow/disable/rollback locally, or route invalidating evidence upward. |

The event does not automatically “escalate to governance.” Its routing depends on what failed:

- if the €450 transaction is deterministically blocked and the case is routed correctly, the Hard transaction boundary worked; Runtime records the evidence and no higher-level redesign is implied;
- if one release contains a bypassable amount precondition, Delivery can repair and re-release **if** the authorized architecture remains credible;
- if repeated evidence shows that no available realization can make the required transaction boundary credible, or that Human Authority capacity cannot meet the Project assumption, **Project Reauthorization** is required;
- if the business wants to raise the delegated threshold beyond the organizationally reserved limit, that is an **authority change**, not a runtime configuration tweak, and must return through Project to Organization;
- if abnormal refund patterns or repeated exceptions reveal that the organizational source, delegated decision right, or shared capability itself is wrong, the evidence belongs at **Organization**.

This is the point of carrying one controlled object through all four horizons. The layers are not four sequential approvals. They are distinct ownership surfaces around the same consequential system: authority is made progressively concrete downward, while evidence returns to the level whose earlier decision it can no longer support.

### Cross-level operating discipline — learn from negative cases without turning every deviation into governance
'''
m = replace_once(m, old_s4, new_s4, 'section4 running example')

bp_anchor = '''**Progressive-disclosure rule.** Introduce the running example explicitly in Section 5.1 as a named pedagogical spine and define the business goal and whole controlled object there, but reveal implementation detail only when the corresponding concept is introduced. For each major conceptual section, prefer the sequence `generic model → application to the same running example → optional secondary counterexample or transfer check`. Do not let a new domain example silently replace the support-resolution system as the primary explanatory object.
'''
bp_insert = bp_anchor + '''
#### Section-by-section running-example progression

The running example is a **cumulative architectural trace**, not a recurring anecdote. Each section should expose one additional property of the same support-resolution system and keep the example visibly separated from generic exposition with a consistent `Running Example` heading or equivalent callout.

- **Section 5.1** — establish the business goal, whole controlled object, Model-Judgment-dependent Consequential Runtime Responsibilities, and the fact that control/evidence/authority paths are intentionally unresolved.
- **Section 5.2** — show that a fixed workflow can already be a Thinking System; then make the engineering consequence explicit: once Model Judgment participates in consequential responsibility, the control perimeter follows the whole object and may become a socio-technical architecture spanning organizational authority, Project / Architecture, Delivery, and Runtime. Do not present those horizons as mandatory departments or stages.
- **Section 5.3** — take one stable refund-authority boundary and map it explicitly through `Constraint → Constraint Realization → Sensors → Controller / Human Authority → Actuator`, showing why a policy sentence is not yet a complete control path.
- **Section 5.4** — carry one concrete negative case through all four decision horizons. Make the owned question, illustrative decision owner, local response, escalation trigger, and reauthorization destination visible for Organization, Project / Architecture, Delivery, and Runtime. Use the same case to demonstrate routing by **invalidated decision basis**, not by where the signal first appeared.
- **Section 5.5** — use variants of the same support system to demonstrate proportionality: for example, draft-only/human-execution versus bounded autonomous refund execution. Show why the complete map is inspected first while implementation depth differs materially.
- **Section 5.6** — use the same system as a substitution/composition test for existing tooling and methods. Ask which parts of the support-system control relationship are already supplied by orchestration, guardrails, observability/evaluation, managed platforms, governance systems, standards, or regulation, and which ownership/reassessment relationships remain external.
- **Section 5.7** — when naming Uncertainty Architecture, show that UA organizes the relationships already derived in the running example rather than introducing a new layer after the fact. The example must remain evidence of explanatory continuity, not validation evidence for UA.
- **Section 5.8** — turn the same case into validation questions: can a team use the map to find an otherwise-missed responsibility, remove unnecessary control, route evidence correctly, or show that an existing stack already preserves the material relationships without additional UA artifacts?

The example should accumulate detail rather than restart. Later sections may refer back to earlier disclosed facts (`€50` delegated refund authority, Human Authority above the threshold, approved identity/data paths, the realized transaction guard, evidence and escalation routes) instead of re-explaining the business context.
'''
b = replace_once(b, bp_anchor, bp_insert, 'blueprint progression contract')

DRAFT.write_text(m)
BLUEPRINT.write_text(b)

print('running-example spine patched')
