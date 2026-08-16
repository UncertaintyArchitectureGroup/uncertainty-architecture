from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')

b = bp.read_text()
m = ms.read_text()


def repl(text, old, new, label, count=1):
    actual = text.count(old)
    if actual < count:
        raise SystemExit(f'missing {label}: expected at least {count}, found {actual}')
    return text.replace(old, new, count)

# Manuscript: make the proportional research boundary and Project-local/Organization routes explicit.
m = repl(
    m,
    'Initial Organizational action establishes admissibility and **assessment eligibility**; it does not pre-authorize a concrete experiment.',
    'Initial Organizational action establishes admissibility and **assessment eligibility**; it permits Project-local analysis and evidence generation inside the standing assessment envelope, but it does not authorize an experiment that crosses an Organizationally reserved boundary.',
    'Figure 8 proportionality caption',
)

m = repl(
    m,
    '**Question owned:** Within which authoritative boundaries may Project / Architecture assessment proceed—and, after a Project viability conclusion, should the organization authorize a specific bounded experiment, proceed with a viable production initiative, reshape it, defer it, or stop it?',
    '**Question owned:** Within which authoritative boundaries may Project / Architecture assessment proceed—and, when a Project finding implicates an Organizationally owned basis or initiative-level decision, should the organization authorize specific bounded research, proceed with a viable production initiative, reshape it, defer it, or stop it?',
    'Organization primary question',
)

m = repl(
    m,
    '- Project conclusion that a deterministic/manual/narrower model-assisted design is preferable for the stated outcome;',
    '- Project conclusion that a deterministic/manual/narrower model-assisted design is preferable for the stated outcome **when adopting that recommendation would require an Organizationally owned premise or continuation decision to change**;',
    'Organization received-evidence qualification',
)

m = repl(
    m,
    'Project then confirms the category result; if no Consequential Runtime Responsibility remains materially dependent on Model Judgment, the design **exits this Thinking-System lifecycle**. A Project-selected narrower model-assisted alternative that still materially informs a consequential responsibility remains a Thinking System and is reassessed at its narrower scope.',
    'Project then confirms the category result; if no Consequential Runtime Responsibility remains materially dependent on Model Judgment, the design **exits the Thinking-System-specific lifecycle and hands off to ordinary product/software governance**; that category exit does not itself authorize funding, initiative continuation, delivery, or release. A Project-selected narrower model-assisted alternative that still materially informs a consequential responsibility remains a Thinking System and is reassessed at its narrower scope.',
    'running-example category exit handoff',
)

m = repl(
    m,
    '> **Initial assessment eligibility is not Bounded Research Authorization. Research-only Project Authorization follows only after Project defines a credible experiment and Organization authorizes that specific bounded research.**',
    '> **Initial assessment eligibility permits Project-local evidence generation inside the standing assessment envelope. When needed research crosses an Organizationally reserved boundary, Project defines the experiment, Organization may issue a specific Bounded Research Authorization, and a research-only Project Authorization scopes that bounded exposure.**',
    'manuscript closing research proportionality claim',
)

# Blueprint: remove remaining blanket "any concrete experiment needs Organization" semantics.
b = repl(
    b,
    'assessment eligibility**, which permits Project analysis but not exposure of a concrete experiment.',
    'assessment eligibility**, which permits Project-local analysis and evidence generation inside the standing assessment envelope but not experiment exposure that crosses an Organizationally reserved boundary.',
    'Article 4 progression eligibility wording',
)

b = repl(
    b,
    'If production viability is unresolved but a bounded experiment has a credible control envelope, Project defines the experiment and Organization may issue a **specific Bounded Research Authorization**, after which Project issues a research-only technical authorization whose evidence returns to viability analysis.',
    'If production viability is unresolved, Project may continue evidence generation locally while it remains inside the standing assessment envelope. When the needed experiment crosses an Organizationally reserved boundary, Project defines its credible control envelope and Organization may issue a **specific Bounded Research Authorization**, after which Project issues a research-only technical authorization whose evidence returns to viability analysis.',
    'Article 4 progression research branch',
)

b = repl(
    b,
    'Initial admissibility and assessment eligibility allow Project / Architecture to compare designs and formulate a bounded research proposal; they do not authorize experiment exposure.',
    'Initial admissibility and assessment eligibility allow Project / Architecture to compare designs and conduct Project-local evidence generation inside the standing assessment envelope; they do not authorize experiment exposure that crosses an Organizationally reserved boundary.',
    'running-example Organizational horizon proportionality',
)

b = repl(
    b,
    'If Project concludes that production viability is still open but a bounded experiment is credibly controllable, Project first defines that experiment; Organization then decides whether to authorize the **specific** evidence-generating exposure.',
    'If Project concludes that production viability is still open, it may continue evidence generation locally while the work remains inside the standing assessment envelope. When the needed experiment crosses an Organizationally reserved boundary, Project first defines that experiment; Organization then decides whether to authorize the **specific** reserved evidence-generating exposure.',
    'running-example bounded research branch',
)

b = repl(
    b,
    '- treat initial assessment eligibility as permission to expose a concrete experiment; specific Bounded Research Authorization follows Project\'s definition of the experiment and its credible control/evidence envelope;',
    '- treat initial assessment eligibility as permission for an experiment that crosses an Organizationally reserved boundary; specific Bounded Research Authorization follows Project\'s definition of that reserved-boundary experiment and its credible control/evidence envelope;',
    'claim-safety proportionality rule',
)

b = repl(
    b,
    '- [ ] Initial **assessment eligibility** permits Project analysis and design of a research proposal but does not authorize experiment exposure.',
    '- [ ] Initial **assessment eligibility** permits Project-local analysis and evidence generation inside the standing assessment envelope; it does not authorize experiment exposure that crosses an Organizationally reserved boundary.',
    'running-example acceptance proportionality',
)

b = repl(
    b,
    '- [ ] Initial assessment eligibility does not permit experiment exposure. A **specific Bounded Research Authorization** is based on a Project-defined experiment with explicit question, control envelope, scope, data/tools, reachable authority, stopping conditions, and evidence obligations.',
    '- [ ] Initial assessment eligibility permits Project-local evidence generation inside the standing assessment envelope but does not permit experiment exposure that crosses an Organizationally reserved boundary. A **specific Bounded Research Authorization** is based on a Project-defined reserved-boundary experiment with explicit question, control envelope, scope, data/tools, reachable authority, stopping conditions, and evidence obligations.',
    'article acceptance proportionality',
)

b = repl(
    b,
    'initial eligibility is not experiment authorization;',
    'initial eligibility is not authorization for experiment exposure that crosses an Organizationally reserved boundary;',
    'Figure 8 acceptance shorthand',
)

b = repl(
    b,
    'Initial assessment eligibility must never be drawn as if it already authorized a concrete experiment.',
    'Initial assessment eligibility must never be drawn as if it already authorized experiment exposure that crosses an Organizationally reserved boundary.',
    'Figure 11 proportionality guard',
)

b = repl(
    b,
    'This may allow Project to design a research proposal; **it does not authorize exposure of a concrete experiment**;',
    'This may allow Project-local analysis and evidence generation inside the standing assessment envelope; **it does not authorize experiment exposure that crosses an Organizationally reserved boundary**;',
    'Organization detailed decision moment',
)

b = repl(
    b,
    'why bounded research can be technically authorized without pretending production viability exists, why initial assessment eligibility is insufficient to expose a concrete experiment, and why evidence from research must return to Project viability analysis before any production-capable authorization;',
    'why bounded research can be technically authorized without pretending production viability exists, why initial assessment eligibility is insufficient to expose an experiment that crosses an Organizationally reserved boundary, and why evidence from research must return to Project viability analysis before any production-capable authorization;',
    'reader promise proportionality',
)

b = repl(
    b,
    'The point: initial assessment eligibility allows Project to formulate the experiment; it is not the experiment authorization. Research closes the evidence loop without pretending that the production case has already passed technical or business authorization.',
    'The point: initial assessment eligibility allows Project-local evidence generation inside the standing envelope; when the experiment crosses an Organizationally reserved boundary, that eligibility is not the authorization for the reserved exposure. Research closes the evidence loop without pretending that the production case has already passed technical or business authorization.',
    'Case D proportionality explanation',
)

# Make Case D explicitly the reserved-boundary research branch it is intended to demonstrate.
b = repl(
    b,
    'Project cannot yet resolve a material production-viability question, but it can define a bounded experiment whose own reachable authority and evidence path are credible.',
    'Project cannot yet resolve a material production-viability question. For this canonical Case D, assume the needed experiment crosses an Organizationally reserved exposure, data, authority, or material-commitment boundary, but Project can define a bounded experiment whose own reachable authority and evidence path are credible.',
    'Case D reserved-boundary assumption',
)

# Guard the exact stale formulations that caused repeated review findings.
for bad in [
    'does not pre-authorize a concrete experiment',
    'treat initial assessment eligibility as permission to expose a concrete experiment',
    'Initial **assessment eligibility** permits Project analysis and design of a research proposal but does not authorize experiment exposure',
    'Initial assessment eligibility does not permit experiment exposure',
    'initial eligibility is not experiment authorization',
    'Initial assessment eligibility must never be drawn as if it already authorized a concrete experiment',
    'does not authorize exposure of a concrete experiment',
    'initial assessment eligibility is insufficient to expose a concrete experiment',
    'after a Project viability conclusion, should the organization',
    '- Project conclusion that a deterministic/manual/narrower model-assisted design is preferable for the stated outcome;',
    'design **exits this Thinking-System lifecycle**.',
]:
    if bad in b or bad in m:
        raise SystemExit('obsolete wording remains: ' + bad)

bp.write_text(b)
ms.write_text(m)
