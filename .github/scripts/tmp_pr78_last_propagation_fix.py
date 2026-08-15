from pathlib import Path

bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms=Path('content/research/notes/open-engineering-specification-article-draft.md')

b=bp.read_text()
m=ms.read_text()

# 1) Top-level connected argument: research authorization proportionality.
old="→ Organization first supplies admissibility, authoritative boundaries, shared capabilities, reserved authority, business intent, and assessment eligibility; this permits Project / Architecture analysis but does not itself authorize exposure of a concrete experiment"
new="→ Organization first supplies admissibility, authoritative boundaries, shared capabilities, reserved authority, business intent, and assessment eligibility; this permits Project / Architecture analysis and Project-local evidence generation inside the standing assessment envelope, but does not authorize an experiment that crosses an Organizationally reserved exposure, authority, data, material-commitment, external-effect, or other reserved boundary"
if old not in b: raise SystemExit('missing connected argument eligibility sentence')
b=b.replace(old,new,1)

old="→ when production viability remains unresolved but a bounded experiment itself has a credible control envelope, Project may conclude further research is required and define the research question, scope, reachable authority, stopping conditions, and evidence obligations; Organization may then issue a specific Bounded Research Authorization and Project issues a research-only technical authorization that cannot silently become production permission"
new="→ when production viability remains unresolved, Project may conduct evidence generation locally when the work remains inside the standing assessment envelope; when the needed experiment crosses an Organizationally reserved boundary, Project defines the research question, scope, reachable authority, stopping conditions, and evidence obligations, Organization may then issue a specific Bounded Research Authorization, and Project issues a research-only technical authorization that cannot silently become production permission"
if old not in b: raise SystemExit('missing connected argument research sentence')
b=b.replace(old,new,1)

# 2) Remove lingering Organization path-selection semantics.
old="The article must distinguish these actions from Project or Runtime Actuators. Organization changes the authoritative/business/research context or chooses the path; it does not design the concrete control architecture, determine category membership by preference, or directly perform a runtime rollback unless the same person or mechanism separately holds runtime authority."
new="The article must distinguish these actions from Project or Runtime Actuators. Organization changes the authoritative/business/research context and makes initiative-level business, basis, research, continuation, exception, and reserved-authority decisions; it does not select the technical/design path inside a standing basis, design the concrete control architecture, determine category membership by preference, or directly perform a runtime rollback unless the same person or mechanism separately holds runtime authority."
if old not in b: raise SystemExit('missing organization chooses-path sentence')
b=b.replace(old,new,1)

# 3) Running example: make reserved boundary explicit for BRA.
old="Suppose Project then cannot estimate how often Human Authority will be required. It concludes `further research required` and defines an experiment in which the model can recommend remedies but transaction execution is disabled, together with cases, data, tools, duration, stopping conditions, and evidence needs. Organization may now issue a **specific Bounded Research Authorization** for that experiment. Project then issues a **research-only Project Authorization**. Delivery realizes and releases only that experiment. Its evidence returns to Project; the experiment itself cannot become production simply because the results look promising."
new="Suppose Project then cannot estimate how often Human Authority will be required from offline/synthetic evidence alone. It concludes `further research required` and defines an experiment that uses live customer cases and reserved customer data to measure real approval load while transaction execution remains disabled, together with population, data, tools, duration, stopping conditions, and evidence needs. Because that experiment crosses an Organizationally reserved live-data/external-exposure boundary, Organization may now issue a **specific Bounded Research Authorization** for it. Project then issues a **research-only Project Authorization**. Delivery realizes and releases only that bounded experiment. Its evidence returns to Project; the experiment itself cannot become production simply because the results look promising."
if old not in m: raise SystemExit('missing running-example research paragraph')
m=m.replace(old,new,1)

# Guard exact obsolete phrases from this review.
for bad in [
    'does not itself authorize exposure of a concrete experiment',
    'Organization may then issue a specific Bounded Research Authorization and Project issues a research-only technical authorization',
    'Organization changes the authoritative/business/research context or chooses the path',
]:
    if bad in b:
        raise SystemExit('obsolete blueprint wording remains: '+bad)

bp.write_text(b)
ms.write_text(m)
