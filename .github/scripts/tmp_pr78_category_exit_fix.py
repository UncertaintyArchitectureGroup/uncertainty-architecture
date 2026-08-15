from pathlib import Path

bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms=Path('content/research/notes/open-engineering-specification-article-draft.md')

def replace_all_checked(text, old, new, label, minimum=1):
    n=text.count(old)
    if n < minimum:
        raise SystemExit(f'{label}: expected >= {minimum}, got {n}')
    return text.replace(old,new)

def one(text, old, new, label):
    n=text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1, got {n}')
    return text.replace(old,new)

b=bp.read_text()
# Connected argument: distinguish local technical/category result from finding requiring Organization.
b=one(b,
"→ Project / Architecture owns the Model-Judgment-necessity analysis, concrete bounded control architecture, technical feasibility, Human Authority/fallback/capacity analysis, and complete control economics, and returns a Project viability conclusion rather than silently converting that analysis into the organization's business decision",
"→ Project / Architecture owns the Model-Judgment-necessity analysis, concrete bounded control architecture, technical feasibility, Human Authority/fallback/capacity analysis, and complete control economics; its result may be either a Project-local technical/category outcome inside the standing Organizational basis or a Project viability finding that requires Organizational research, business-basis, investment, continuation, or other reserved authority",
'connected argument project result')
b=one(b,
"→ when Project concludes that a deterministic/manual or otherwise simpler architecture can satisfy the same Organizationally authorized business outcome and stay within the standing authority/business basis, Project / Architecture owns that technical design choice and confirms the category of the selected design; the design exits the Thinking-System lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment; if obtaining the desired result requires changing the business outcome, value hypothesis, authority, investment basis, or another Organizationally owned premise, Project returns that changed-basis requirement and its engineering recommendation to Organization before reassessment",
"→ when Project concludes that a deterministic/manual or otherwise simpler architecture can satisfy the same Organizationally authorized business outcome and stay within the standing authority/business basis, Project / Architecture owns that technical design choice and confirms the category of the selected design; when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, the design exits the Thinking-System-specific lifecycle and hands off to the ordinary product/software lifecycle, where any otherwise applicable Organizational funding, portfolio, initiative, delivery, or release authority still applies; if obtaining the desired result requires changing the business outcome, value hypothesis, authority, investment basis, or another Organizationally owned premise, Project returns that changed-basis requirement and its engineering recommendation to Organization before reassessment",
'connected argument category exit')
b=one(b,
"→ Organization owns the business outcome and authoritative/investment basis, the decision to issue a specific Bounded Research Authorization, and the decision to proceed / continue, reshape the business basis, defer, or do not proceed after receiving the Project viability conclusion; Project / Architecture owns technical/design selection—including a deterministic, manual, narrower model-assisted, or broader Thinking-System architecture—when the selected design still satisfies that standing Organizational basis; Organization is reactivated when the engineering conclusion requires a changed outcome, authority, price, target segment, service promise, funding, investment assumption, or another premise it owns",
"→ Organization owns the business outcome and authoritative/investment basis, specific Bounded Research Authorization when a proposed experiment consumes or creates Organizationally reserved exposure or commitments, and proceed / continue, reshape, defer, or do-not-proceed decisions when a Project finding implicates those authorities; Project / Architecture owns technical/design selection—including deterministic, manual, narrower model-assisted, or broader Thinking-System architecture—when the selected design still satisfies the standing Organizational basis; Organization is reactivated only when the engineering conclusion requires a changed outcome, authority, price, target segment, service promise, funding, investment assumption, material reserved exposure/commitment, or another premise it owns",
'connected argument org authority')
# Research boundary rule: local/offline experiments need not invoke Organization.
needle="Blueprint-owned working analyses needed to draft later sections—including the complete Article §5 material-relationship mapping—remain inside this living blueprint as working sections or appendices."
insert=needle+"\n\n**Research-authorization proportionality rule.** Initial assessment eligibility may include Project-local architecture analysis, simulation, offline/synthetic evaluation, and engineering experiments that remain inside the standing Organizational envelope and do not consume or create Organizationally reserved exposure, authority, sensitive data access, external commitment, material budget/capacity, or another reserved premise. A **specific Bounded Research Authorization** is required when a concrete experiment crosses one of those Organizationally owned boundaries. Research-only Project Authorization then scopes the technical experiment; it is not a ceremony required for every notebook, sandbox run, or local evaluation."
b=one(b,needle,insert,'research proportionality rule')
# Future-section rule category exit handoff.
b=b.replace("explicit category exit when Project selects and confirms a simpler design that still satisfies that basis and leaves no Consequential Runtime Responsibility dependent on Model Judgment,", "explicit category exit when Project selects and confirms a simpler design that still satisfies that basis and leaves no Consequential Runtime Responsibility dependent on Model Judgment—where exit means handoff from the Thinking-System-specific lifecycle to ordinary product/software governance rather than automatic business authorization—,")
# Add acceptance semantic wherever concise phrase appears.
b=b.replace("exit this lifecycle when the selected design is no longer a Thinking System", "exit this Thinking-System-specific lifecycle and hand off to ordinary product/software governance when the selected design is no longer a Thinking System")
bp.write_text(b)

m=ms.read_text()
# Clarify local category exit does not authorize initiative.
m=replace_all_checked(m,
"exits this Thinking-System lifecycle into the ordinary product/software lifecycle",
"exits this Thinking-System-specific lifecycle and hands off to the ordinary product/software lifecycle; that category exit does not itself authorize funding, initiative continuation, delivery, or release, and any otherwise applicable Organizational or ordinary product/software decision rights still apply",
'manuscript category exit',1)
m=replace_all_checked(m,
"the design exits this Thinking-System lifecycle",
"the design exits this Thinking-System-specific lifecycle and hands off to ordinary product/software governance; category exit is not business authorization",
'manuscript shorter category exit',1)
# Organizational second moment: bounded research threshold.
old="A specific Bounded Research Authorization is therefore downstream of Project's experiment design, not a duplicate of initial eligibility. Project first defines the research question, technical control envelope, environment/population, data/tool access, reachable authority, stopping conditions, and required evidence. Organization decides whether acquiring that evidence is worth the bounded exposure and whether the proposed experiment fits Organizational limits. Only then may Project issue a **research-only Project Authorization**. Evidence from the experiment returns to Project viability analysis and, where necessary, to Organization."
new="A specific Bounded Research Authorization is therefore downstream of Project's experiment design, not a duplicate of initial eligibility, **when the proposed experiment consumes or creates an Organizationally reserved exposure or commitment**—for example live/external exposure, reserved authority, sensitive or specially governed data access, material budget/capacity, external commitments, or another Organizationally owned premise. Project first defines the research question, technical control envelope, environment/population, data/tool access, reachable authority, stopping conditions, and required evidence. Organization decides whether acquiring that evidence is worth that reserved exposure and whether the proposed experiment fits Organizational limits. Only then may Project issue a **research-only Project Authorization**. Project-local simulation, offline/synthetic evaluation, and engineering experiments that remain entirely inside the standing assessment envelope need no additional Organizational ceremony merely because they generate evidence. Evidence from an Organizationally authorized bounded experiment returns to Project viability analysis and, where necessary, to Organization."
m=one(m,old,new,'manuscript bounded research boundary')
# Figure captions/nodes exit wording if exact common label exists.
m=m.replace('EXIT["Exit Thinking-System lifecycle<br/>ordinary product/software lifecycle"]','EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product/software governance<br/>ordinary business/delivery authority still applies"]')
m=m.replace('EXIT["Exit Thinking-System lifecycle<br/>ordinary software/product lifecycle"]','EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product/software governance<br/>ordinary business/delivery authority still applies"]')
ms.write_text(m)
