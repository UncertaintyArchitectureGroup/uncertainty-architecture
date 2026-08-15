from pathlib import Path

bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms=Path('content/research/notes/open-engineering-specification-article-draft.md')
tr=Path('content/research/framework-traceability.md')

b=bp.read_text()
m=ms.read_text()
t=tr.read_text()

# 1) Research-authorization proportionality: make blanket statements conditional on crossing an Organizationally reserved boundary.
replacements_m = [
("**Assessment eligibility does not authorize exposure of a concrete experiment.**",
 "**Assessment eligibility permits Project-local analysis and evidence generation inside the standing assessment envelope; it does not authorize an experiment that crosses an Organizationally reserved exposure, authority, data, material-commitment, or external-effect boundary.**"),
("At the start, Organization may declare the proposal eligible for Project assessment inside standing data, vendor, and authority boundaries. That **does not yet authorize an experiment**.",
 "At the start, Organization may declare the proposal eligible for Project assessment inside standing data, vendor, and authority boundaries. That eligibility may cover Project-local simulation, offline/synthetic evaluation, and other engineering evidence generation inside the standing envelope, but it **does not authorize an experiment that crosses an Organizationally reserved boundary**."),
("A Project-defined experiment may run only after specific Bounded Research Authorization and under research-only Project Authorization, then return evidence without creating production permission.",
 "A Project-defined experiment that remains inside the standing assessment envelope may run under applicable Project-local engineering controls. When the experiment crosses an Organizationally reserved boundary, it may run only after specific Bounded Research Authorization and under research-only Project Authorization; in either case, research evidence returns without creating production permission."),
]
for old,new in replacements_m:
    if old not in m:
        raise SystemExit('missing manuscript proportionality text: '+old[:80])
    m=m.replace(old,new)

replacements_b = [
("Distinguish **assessment eligibility** from **specific Bounded Research Authorization**. Initial eligibility permits Project to formulate a research experiment; the concrete experiment is exposed only after Project defines its control/evidence envelope and Organization authorizes that specific research.",
 "Distinguish **assessment eligibility** from **specific Bounded Research Authorization**. Initial eligibility permits Project-local analysis, simulation, offline/synthetic evaluation, and other evidence generation inside the standing assessment envelope. A concrete experiment requires specific Organizational authorization only when it crosses an Organizationally reserved exposure, authority, data, material-commitment, external-effect, or other reserved boundary; Project first defines that experiment's control/evidence envelope, then Organization authorizes that specific research."),
]
for old,new in replacements_b:
    if old not in b:
        raise SystemExit('missing blueprint proportionality text: '+old[:80])
    b=b.replace(old,new)

# 2) Figure 11 routing: Project-local narrower redesign and local evidence generation must not flow unconditionally to Organization.
old_block='''    V["Project viability conclusion<br/> viable · narrower · research<br/> economic non-viability · Architectural Veto"]
    OD["Organization<br/> specific bounded research · proceed / continue<br/> reshape business / authority basis · defer · do not proceed"]
    PRA["Project / Architecture<br/> research-only Project Authorization<br/> bounded experiment · no production permission"]
    PPA["Project / Architecture<br/> production-capable Project Authorization<br/> versioned technical baseline"]
    D["Delivery"]

    ORG --> NEED
    NEED -->|Project selects technical design<br/>inside standing Organizational basis| CAT
    CAT -->|No| EXIT
    CAT -->|Yes| RISK
    NEED -->|preferred design requires changed<br/>Organizational outcome / authority / investment basis| OD
    RISK --> K --> PATH
    RISK --> PROP --> PATH
    PATH --> HUMAN --> ECON --> V --> OD
    OD -->|changed business / authority basis| NEED
    OD -->|specific Bounded Research Authorization| PRA --> D
    OD -->|positive Business Authorization<br/>on viable production basis| PPA --> D
'''
new_block='''    V["Project viability conclusion<br/> viable production basis · narrower redesign · further research<br/> economic non-viability · Architectural Veto"]
    LRE["Project-local evidence generation<br/> inside standing assessment envelope<br/> simulation · offline / synthetic evaluation"]
    OD["Organization<br/> specific bounded research · proceed / continue<br/> reshape business / authority basis · defer · do not proceed"]
    PRA["Project / Architecture<br/> research-only Project Authorization<br/> bounded experiment · no production permission"]
    PPA["Project / Architecture<br/> production-capable Project Authorization<br/> versioned technical baseline"]
    D["Delivery"]

    ORG --> NEED
    NEED -->|Project selects technical design<br/>inside standing Organizational basis| CAT
    CAT -->|No| EXIT
    CAT -->|Yes| RISK
    NEED -->|preferred design requires changed<br/>Organizational outcome / authority / investment basis| OD
    RISK --> K --> PATH
    RISK --> PROP --> PATH
    PATH --> HUMAN --> ECON --> V
    V -->|narrower technical redesign<br/>inside standing Organizational basis| NEED
    V -->|further research remains inside<br/>standing assessment envelope| LRE --> NEED
    V -->|viable production basis requires Business Authorization<br/>or research crosses reserved boundary<br/>or economics / changed basis / Veto requires Organizational action| OD
    OD -->|changed business / authority basis| NEED
    OD -->|specific Bounded Research Authorization| PRA --> D
    OD -->|positive Business Authorization<br/>on viable production basis| PPA --> D
'''
if old_block not in m:
    raise SystemExit('missing Figure 11 Mermaid block')
m=m.replace(old_block,new_block)

# 3) Traceability must identify both doctrine and pattern as current conflicting status-bearing surfaces.
old='Current status-bearing Project pattern combines project viability, authorization, deferral, and No-Go inside the Project decision surface and does not yet express the paper\'s explicit assessment-eligibility versus specific bounded-research distinction'
new='Current status-bearing Nested Control Lifecycle doctrine and Project Control Architecture and Viability Review pattern both place business outcome, project authorization, bounded research, deferral/No-Go, or closely related decision ownership on the Project surface and do not yet express the paper\'s explicit assessment-eligibility versus specific bounded-research distinction'
if old not in t:
    raise SystemExit('missing traceability source wording')
t=t.replace(old,new)
old2='then deliberately accept, narrow, reject, or otherwise reconcile it through framework review before status-bearing sources change.'
new2='then deliberately accept, narrow, reject, or otherwise reconcile it through framework review across both the Nested Control Lifecycle doctrine and affected Project pattern(s) before status-bearing sources change.'
if old2 not in t:
    raise SystemExit('missing traceability reconciliation wording')
t=t.replace(old2,new2,1)

# Guards against the exact contradictory forms fixed here.
for bad in [
    'That **does not yet authorize an experiment**',
    'A Project-defined experiment may run only after specific Bounded Research Authorization',
    'PATH --> HUMAN --> ECON --> V --> OD',
    'Current status-bearing Project pattern combines project viability, authorization, deferral, and No-Go',
]:
    if bad in m or bad in t:
        raise SystemExit('obsolete wording remains: '+bad)

bp.write_text(b)
ms.write_text(m)
tr.write_text(t)
