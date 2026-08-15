from pathlib import Path
import re

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')
ch = Path('CHANGELOG.md')

def exact(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {count}')
    return text.replace(old, new)

b = bp.read_text()
b = exact(b, 'Organization owns business/design selection and authority over the initiative, including the levers that may change the decision basis.', 'Organization owns the business outcome, authoritative/investment basis, and initiative-level research/continuation decisions. It does not select the technical architecture when Project / Architecture can satisfy the standing Organizational basis without changing an Organizationally owned premise.', 'blueprint Organization ownership')
b = exact(b, '- a Project conclusion that Model Judgment is unnecessary for the stated outcome or that a deterministic/manual/narrower design is preferable;', '- a Project conclusion that Model Judgment is unnecessary or a simpler design is preferable **only when** adopting that engineering recommendation would require changing an Organizationally owned premise or deciding whether to continue, defer, or stop the initiative;', 'blueprint Organization activation')
b = exact(b, '- business/design decisions repeatedly ignored or obscured Project viability evidence;', '- Organizational business/basis decisions repeatedly ignored or obscured Project viability evidence;', 'blueprint learning wording')
b = exact(b, 'enough cost/capacity/latency information to make the viability conclusion usable by Organization as a business/design decision input;', 'enough cost/capacity/latency information to make the viability conclusion usable by Organization as a business/basis decision input where Organizational action is actually required;', 'blueprint viability input')
b = exact(b, 'Project viability reassessment → Organization: business/design choice challenged, new specific research authorization needed, Architectural Veto, or changed business/authority input required', 'Project viability reassessment → Organization: Organizational business/authority/investment basis challenged, new specific research authorization needed, Architectural Veto requires a changed proposal, or a continuation/defer/stop decision is required', 'blueprint evidence routing')
b = exact(b, '   └→ business/design basis challenged / new research authorization needed / Architectural Veto / wider authority required → Organizational review', '   └→ Organizational business/authority/investment basis challenged / new research authorization needed / Architectural Veto requires a changed proposal / continuation decision required → Organizational review', 'blueprint Delivery routing')
b = exact(b, '- **Organization / Project boundary and handshake:** Organization owns initial admissibility/assessment eligibility, authoritative boundaries, shared capabilities, reserved decisions, evidence obligations, exceptions, business intent, selection of the business/design path, specific Bounded Research Authorization, and the business decision to proceed/continue/reshape/defer/stop. Project / Architecture owns Model-Judgment necessity, alternative/category analysis, concrete control architecture, technical/control feasibility, Human Authority/fallback/capacity analysis, complete control economics, Architectural Veto, and the Project viability conclusion. Project Authorization is a scoped technical baseline, not the Organizational business/research decision.', '- **Organization / Project boundary and handshake:** Organization owns initial admissibility/assessment eligibility, authoritative boundaries, shared capabilities, reserved decisions, evidence obligations, exceptions, the business outcome and authoritative/investment basis, specific Bounded Research Authorization, and initiative-level proceed/continue/reshape/defer/stop decisions. Project / Architecture owns Model-Judgment necessity, alternative/category analysis, technical/design selection inside that standing Organizational basis, concrete control architecture, technical/control feasibility, Human Authority/fallback/capacity analysis, complete control economics, Architectural Veto, category confirmation, and the Project viability conclusion. A Project-selected simpler design does not require Organizational architecture approval unless an Organizationally owned premise or continuation decision must change. Project Authorization is a scoped technical baseline, not the Organizational business/research decision.', 'blueprint known-risk ownership')

for old, new in {
    'Organizational-selected-path-specific-research-business': 'Organizational-specific-research/business/basis',
    'Organizational selected-path / specific-bounded-research / business decision': 'Organizational specific-bounded-research / business / changed-basis decision',
    'selected-path category confirmation / exit': 'Project-selected-design category confirmation / exit',
    'selected-path category exit': 'Project-selected-design category exit',
    'selected-path lifecycle-exit rule': 'Project-selected-design lifecycle-exit rule',
    'Organizational selected-path/specific-bounded-research/business decision': 'Organizational specific-bounded-research/business/changed-basis decision',
    'Organizational path/business/research decisions': 'Organizational business/basis/research decisions',
    'Organizational path/business/research decision': 'Organizational business/basis/research decision',
    'Organizational path / continuation / reshape / defer / do-not-proceed review': 'Organizational business/basis / continuation / reshape / defer / do-not-proceed review',
    'business/design choice': 'Organizational business/basis decision',
    'business/design selection': 'Organizational business/basis authority',
    'business/design basis': 'Organizational business/authority/investment basis',
}.items():
    b = b.replace(old, new)

b = b.replace('Figure 8 keeps Organization, Project / Architecture, Delivery, and Runtime as four decision horizons while showing: initial Organizational **assessment eligibility** → Project viability conclusion → Organizational specific-bounded-research / business / changed-basis decision → correspondingly scoped Project Authorization → Delivery.', 'Figure 8 keeps Organization, Project / Architecture, Delivery, and Runtime as four decision horizons while showing: initial Organizational **assessment eligibility** → Project analysis / technical selection; Project-local category confirmation and exit when a selected design remains inside the standing Organizational basis; and an Organizational specific-bounded-research / Business Authorization / changed-basis decision only when Project evidence actually requires Organizational action → correspondingly scoped Project Authorization → Delivery.')
b = b.replace('Figure 9 reproduces the Figure 8 four-horizon decision model—including assessment eligibility, specific bounded research, Project-selected-design category confirmation / exit, research-only versus production-capable Project Authorization, reassessment evidence from Delivery realization or Runtime/research operation, and independent exogenous Organizational change—', 'Figure 9 reproduces the Figure 8 four-horizon decision model—including assessment eligibility, Project-owned technical selection and category confirmation/exit inside the standing Organizational basis, specific bounded research, research-only versus production-capable Project Authorization, reassessment evidence from Delivery realization or Runtime/research operation, and independent exogenous Organizational change—')
bp.write_text(b)

m = ms.read_text()
fig8_pattern = re.compile(r'```mermaid\nflowchart TB\n    O\["Organization<br/>What may the organization assess, research, pursue, or continue\?"\].*?```\n\n\*\*Figure 8 — Four decision-ownership horizons around one controlled object\.\*\*.*?(?=\n\n### Two orthogonal models)', re.S)
fig8_new = '''```mermaid
flowchart TB
    O["Organization<br/>What may the organization assess, research, pursue, or continue?"]
    P["Project / Architecture<br/>Model-Judgment necessity · technical selection<br/>control feasibility · economics · viability"]
    CAT{"Selected technical design<br/>still a Thinking System?"}
    EXIT["Exit Thinking-System lifecycle<br/>ordinary product / software lifecycle"]
    D["Delivery<br/>Is this bounded realization complete and releasable<br/>for the authorized research or production scope?"]
    R["Runtime<br/>Does active operation remain inside the authorized boundary?"]
    E["Delivery / Runtime reassessment evidence<br/>realization or operation evidence that challenges a decision basis"]
    X["Exogenous Organizational change<br/>law · contract · policy · vendor · business basis<br/>price · segment · funding · portfolio intent"]

    O -->|initial admissibility + assessment eligibility<br/>authoritative / business basis| P
    P -->|Project selects technical design<br/>inside standing Organizational basis| CAT
    CAT -->|No| EXIT
    CAT -->|Yes: Thinking-System candidate remains| P
    P -->|specific research request / viable production basis<br/>or changed Organizational premise / continuation decision| O
    O -->|specific Bounded Research Authorization<br/>Business Authorization or changed basis| P
    P -->|research-only or production-capable<br/>Project Authorization where applicable| D
    D -->|approved realization + authorized exposure| R
    D -.->|realization / experiment evidence| E
    R -->|operation evidence| E
    E -.->|implementation / realization / evidence issue| D
    E -.->|risk / feasibility / Model Judgment necessity<br/>capacity / economics invalidated or research answered| P
    X --> O
```

**Figure 8 — Four decision-ownership horizons around one controlled object.** Organization and Project / Architecture are connected by a recurrent decision relationship rather than a one-pass stage gate. Initial Organizational action establishes admissibility and **assessment eligibility**; it does not pre-authorize a concrete experiment. Project / Architecture owns technical/design selection within the standing Organizational business and authority basis and can confirm category locally: a selected design exits the Thinking-System lifecycle when no Consequential Runtime Responsibility remains materially dependent on Model Judgment. Organization is reactivated only when Project evidence requires a specific bounded-research decision, Business Authorization for a viable production basis, a changed Organizationally owned premise, or a continuation/defer/stop decision. Project turns the applicable Organizational decision into a scoped technical Project Authorization where one is needed. Delivery and Runtime may operate only inside that scope. Exogenous Organizational change is an independent input to Organization rather than evidence generated by Delivery or Runtime.'''
m, n = fig8_pattern.subn(fig8_new, m, count=1)
if n != 1:
    raise SystemExit(f'Figure 8 replacement expected 1, found {n}')

fig9_pattern = re.compile(r'```mermaid\nflowchart LR\n    subgraph L\["Decision ownership: where the decision belongs"\].*?```\n\n\*\*Figure 9 — Two orthogonal models\.\*\*.*?(?=\n\n### The full map is a reasoning reference)', re.S)
fig9_new = '''```mermaid
flowchart LR
    subgraph L["Decision ownership: where the decision belongs"]
        direction TB
        subgraph SPINE9[" "]
            direction TB
            O["Organization<br/> What may the organization assess, research, pursue, or continue?"]
            P["Project / Architecture<br/> Model-Judgment necessity · technical selection<br/> control feasibility · economics · viability"]
            CAT{"Selected technical design<br/> still a Thinking System?"}
            EXIT["Exit Thinking-System lifecycle"]
            D["Delivery<br/> Is this bounded realization complete and releasable<br/> for its authorized scope?"]
            R["Runtime<br/> Does active operation remain inside the authorized boundary?"]
            E["Delivery / Runtime reassessment evidence<br/> realization or operation evidence that challenges a decision basis"]
            X["Exogenous Organizational change<br/> authoritative or business basis"]

            O -->|initial admissibility + assessment eligibility<br/>authoritative / business basis| P
            P -->|technical design selected<br/>inside standing Organizational basis| CAT
            CAT -->|No| EXIT
            CAT -->|Yes| P
            P -->|specific research request / viable production basis<br/>or changed Organizational premise / continuation decision| O
            O -->|specific Bounded Research Authorization<br/>Business Authorization or changed basis| P
            P -->|research-only or production-capable<br/>Project Authorization where applicable| D
            D -->|approved realization + authorized exposure| R
            D -.->|realization / experiment evidence| E
            R -->|operation evidence| E
            X --> O
        end

        E -.->|implementation / realization / evidence issue| D
        E -.->|risk / feasibility / Model Judgment necessity<br/>capacity / economics invalidated or research answered| P
        style SPINE9 fill:none,stroke:none
    end

    subgraph F["Capability functions: how control becomes operational"]
        direction TB
        subgraph F1[" "]
            direction LR
            J1(( )) --- A["Actuators and corrective action<br/> execute authorized change"]
        end
        subgraph F2[" "]
            direction LR
            J2(( )) --- K["Constraints and realizations<br/> define and operationalize boundaries"]
        end
        subgraph F3[" "]
            direction LR
            J3(( )) --- S["Sensors and evidence<br/> observe behavior, conditions, and control state"]
        end
        subgraph F4[" "]
            direction LR
            J4(( )) --- C["Controllers / decision functions<br/> interpret evidence and select bounded response"]
        end
        J1 --- J2
        J2 --- J3
        J3 --- J4
        style F1 fill:none,stroke:none
        style F2 fill:none,stroke:none
        style F3 fill:none,stroke:none
        style F4 fill:none,stroke:none
    end

    L -. "all four capability families may appear at every decision horizon" .- F
    classDef capability fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#1b5e20;
    classDef railpoint fill:transparent,stroke:transparent,color:transparent;
    class A,K,S,C capability;
    class J1,J2,J3,J4 railpoint;
```

**Figure 9 — Two orthogonal models.** The left side reproduces the decision model from Figure 8: initial assessment eligibility is distinct from a later specific Bounded Research Authorization; Project / Architecture owns technical/design selection and category confirmation inside the standing Organizational basis; Organization is reactivated only when its business/authority/investment basis or an initiative-level research/continuation decision is implicated; research-only and production-capable Project Authorization remain distinct; Delivery/Runtime reassessment evidence returns to Delivery or Project; and exogenous Organizational change activates Organization independently. The green side is the capability anatomy. Its ordering is a reading aid, not an execution pipeline. There is no one-to-one mapping between horizons and capability families.'''
m, n = fig9_pattern.subn(fig9_new, m, count=1)
if n != 1:
    raise SystemExit(f'Figure 9 replacement expected 1, found {n}')

old_outputs = '''The Project output therefore occurs in two related forms.

First, Project returns a **versioned Project viability conclusion** to Organization. It records the candidate design and scope, Model-Judgment necessity rationale and alternatives, candidate category result where relevant, Project Constraint Architecture, required operating-contract properties, credible bounded control paths or explicitly unresolved production questions, Human Authority/fallback/capacity assumptions, control economics, residual exposure/uncertainty, viability status, and the assumptions whose change requires reassessment.

Second, after the relevant Organizational decision, Project may issue a **scoped Project Authorization** for Delivery:'''
new_outputs = '''Project output has two routes rather than one mandatory return to Organization for every technical conclusion.

For a **Project-local technical outcome**, Project / Architecture may select a deterministic, manual, narrower model-assisted, or other technical design that still satisfies the standing Organizational business outcome and authority basis. It records the technical/design decision and applies the category test to the selected design. If no Consequential Runtime Responsibility remains materially dependent on Model Judgment, that design exits the Thinking-System lifecycle without a second Organizational architecture approval. If a narrower Thinking-System candidate remains, Project continues viability analysis at that narrower scope.

When **Organizational action is required**, Project returns a **versioned Project viability conclusion**. It records the candidate design and scope, Model-Judgment necessity rationale and alternatives, candidate category result where relevant, Project Constraint Architecture, required operating-contract properties, credible bounded control paths or explicitly unresolved production questions, Human Authority/fallback/capacity assumptions, control economics, residual exposure/uncertainty, viability status, and the assumptions whose change requires reassessment. Organizational action is required when Project requests a specific bounded experiment, presents a viable production basis that needs Business Authorization, finds that economics or another Organizational premise must change, raises an Architectural Veto that can only be addressed by changing the proposal, or needs an initiative-level continue/defer/stop decision.

After the applicable Organizational decision, Project may issue a **scoped Project Authorization** for Delivery:'''
m = exact(m, old_outputs, new_outputs, 'manuscript Project outputs')
m = exact(m, 'G{"Release Gate<br/> release only inside authorized exposure"]', 'G{"Release Gate<br/> release only inside authorized exposure"}', 'Figure 12 Mermaid')
m = m.replace('Organization owns the business/design choice because it can change levers the project cannot.', 'Organization owns the business/basis decision because it can change levers the project cannot; it does not re-select a technical architecture that remains inside the standing basis.')
m = m.replace('Organizational business/design choice', 'Organizational business/basis decision')
m = m.replace('business/design choice', 'business/basis decision')
m = m.replace('business/design basis', 'Organizational business/authority/investment basis')
ms.write_text(m)

c = ch.read_text()
old = '- Reopened lifecycle-ownership research in the synthesis article and framework traceability. The paper now tests a sharper distinction between initial Organizational **assessment eligibility**, Project-owned Model-Judgment-necessity / bounded-control / economics analysis and **Project viability conclusion**, Organization-owned selection of the business/design path plus **specific Bounded Research Authorization** or production Business Authorization, and scoped technical **research-only** versus **production-capable Project Authorization**. A simpler candidate remains a Project conclusion until Organization selects that path; Project then confirms whether the selected design remains a Thinking System. Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.'
new = '- Reopened lifecycle-ownership research in the synthesis article and framework traceability. The paper now tests a sharper distinction between initial Organizational **assessment eligibility**; Project-owned Model-Judgment necessity, technical/design selection inside the standing Organizational business/authority basis, bounded-control/economics analysis, category confirmation, and **Project viability conclusion**; Organization-owned business outcome/basis plus **specific Bounded Research Authorization**, production Business Authorization, changed-basis, and initiative-level proceed/reshape/defer/stop decisions; and scoped technical **research-only** versus **production-capable Project Authorization**. A simpler design that still satisfies the standing Organizational basis may be selected and category-tested at Project without a second Organizational architecture approval; Organization is reactivated only when an Organizationally owned premise or initiative-level decision must change. Exogenous Organizational authoritative/business changes are treated as direct Organization inputs rather than as Runtime/Delivery evidence. These semantics remain research under validation and do not change status-bearing doctrine or patterns by implication.'
c = exact(c, old, new, 'CHANGELOG lifecycle entry')
ch.write_text(c)
