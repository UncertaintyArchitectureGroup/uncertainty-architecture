from pathlib import Path

p = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s = p.read_text()

def exact(old, new, label):
    global s
    n=s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1, found {n}')
    s=s.replace(old,new)

# Make the economics/viability decision structure explicitly two-route.
exact(
"""→ Project viability conclusion:
   Model Judgment unnecessary / simpler design preferable
   | viable as proposed
   | viable only with narrower scope / changed authority
   | further bounded research required
   | technically viable but economically unattractive under current assumptions
   | Architectural Veto — no credible bounded control architecture for the current proposal
→ Organization chooses:
   specific bounded research | proceed / continue | reshape Organizational basis | defer | do not proceed
→ Project reassesses any changed Organizational basis and issues scoped Project Authorization where applicable""",
"""→ Project result:
   Project-local technical/category outcome
      | Model Judgment unnecessary / simpler design preferable inside standing Organizational basis
      | narrower technical design that remains a Thinking System inside standing basis
   OR Project viability finding requiring Organizational action
      | viable production basis requiring Business Authorization
      | further bounded research requiring Organizationally reserved exposure/commitment
      | technically viable but economically unattractive under current assumptions
      | changed Organizational premise / continuation decision required
      | Architectural Veto — no credible bounded control architecture for the current proposal
→ Project-local outcome: select design + confirm category; hand off to ordinary product/software governance if no Thinking System remains
→ Organizational-action finding: Organization chooses specific bounded research | proceed / continue | reshape Organizational basis | defer | do not proceed
→ Project reassesses any changed Organizational basis and issues scoped Project Authorization where applicable""",
'decision structure two-route')

exact(
"- **Further bounded research required:** production viability remains unresolved, but Project can identify a credibly bounded experiment and the evidence it needs. Initial assessment eligibility does not expose that experiment. Organization decides whether the **specific** evidence is worth acquiring; a positive Bounded Research Authorization allows a research-only Project Authorization, not production permission.",
"- **Further bounded research required:** production viability remains unresolved, but Project can identify the evidence it needs and a credible experiment envelope. If the experiment remains entirely inside the standing assessment envelope and consumes no Organizationally reserved exposure, authority, specially governed data, material commitment, or external effect, Project may run it locally under ordinary engineering controls. If the experiment crosses an Organizationally owned boundary, initial assessment eligibility does not expose it: Organization decides whether the **specific** evidence is worth acquiring, and a positive Bounded Research Authorization allows a research-only Project Authorization, not production permission.",
'bounded research proportionality bullet')

# Split output A from local A2 instead of calling every result a return to Organization.
exact("**A. Viability conclusion returned to Organization:**", "**A. Project viability finding requiring Organizational action:**", 'output A heading')
exact(
"- viability status: viable / viable with conditions or narrower scope / further bounded research / technically viable but economically unattractive / Model Judgment unnecessary or simpler alternative preferred / Architectural Veto;",
"- viability/action status relevant to the Organizational decision: viable production basis requiring Business Authorization / further bounded research requiring Organizationally reserved exposure or commitment / technically viable but economically unattractive / changed Organizational premise or continuation decision required / Architectural Veto;",
'output A status list')

exact(
"- If Project proposes bounded research, initial assessment eligibility is insufficient. Organization must issue a **specific Bounded Research Authorization** for the Project-defined experiment before Project issues research-only Project Authorization.",
"- If Project proposes evidence-generating work that remains entirely inside the standing assessment envelope and consumes no Organizationally reserved exposure or commitment, Project may conduct it locally under the applicable engineering controls. If the proposed experiment crosses an Organizationally owned boundary, initial assessment eligibility is insufficient: Organization must issue a **specific Bounded Research Authorization** for the Project-defined experiment before Project issues research-only Project Authorization.",
'local action research proportionality')

# Figure 11 contract: simpler branch is explicitly a Project-local outcome, not a return to Organization.
exact(
"""   ├→ simpler alternative preferred
   │    → Project viability conclusion + candidate category result
   │    → Project selects simpler technical design inside standing Organizational basis""",
"""   ├→ simpler alternative preferred inside standing Organizational basis
   │    → Project-local technical/category outcome
   │    → Project selects simpler technical design inside standing Organizational basis""",
'figure11 simpler branch')

# Runtime/evidence routing must not imply Organization chooses a simpler design.
exact(
"""project economics, Model-Judgment-necessity rationale, business-value assumptions, or viable-scope conclusion changed materially
→ Project viability reassessment
→ Organizational business/basis / continuation / reshape / defer / do-not-proceed review
→ if simpler path selected: Project confirms category and exits this lifecycle only if the selected design is not a Thinking System
→ production Project Reauthorization only for a resulting authorized technically viable Thinking-System basis""",
"""project economics, business-value assumptions, or another Organizationally owned premise changed materially
→ Project viability reassessment
→ Organizational business/basis / continuation / reshape / defer / do-not-proceed review
→ Project reassesses any changed Organizational basis before a new production-capable technical baseline

Model-Judgment-necessity rationale or technical design changed materially
→ Project viability reassessment
→ if a simpler path still satisfies the standing Organizational basis: Project selects it and confirms category locally
   → exit the Thinking-System-specific lifecycle only if the selected design is not a Thinking System; ordinary product/software governance still applies
→ Organizational review only if the preferred path requires changing an Organizationally owned premise or continuation decision""",
'evidence routing simpler path')

exact(
"Ensure Figure 12 and Figure 14 agree: a Delivery-discovered issue that challenges Project Authorization routes first to Project viability reassessment; research results never self-promote to production; if Project can reauthorize inside the standing scope/basis, it does so. If economics/business basis/Model-Judgment necessity is invalidated, a simpler design is preferred, Architectural Veto applies, wider authority/new research permission is needed, or an Organizational authoritative/business basis changed exogenously, Organization owns the next path/business/authority decision before Project applies category consequences or issues the resulting scoped technical baseline.",
"Ensure Figure 12 and Figure 14 agree: a Delivery-discovered issue that challenges Project Authorization routes first to Project viability reassessment; research results never self-promote to production; if Project can reauthorize or select a simpler technical design inside the standing scope/business/authority basis, it does so and applies category consequences locally. Organization owns the next decision only when economics or another Organizationally owned business/investment premise must change, Architectural Veto requires a changed proposal, wider authority or new reserved research permission is needed, a continuation/defer/stop decision is implicated, or an Organizational authoritative/business basis changed exogenously. Project then reassesses any changed basis before issuing the resulting scoped technical baseline.",
'figure14 contract ownership')

p.write_text(s)
