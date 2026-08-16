from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')

b = bp.read_text()
m = ms.read_text()


def replace_exact(text: str, old: str, new: str, label: str, expected: int = 1) -> str:
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'{label}: expected {expected} occurrences, found {count}')
    return text.replace(old, new)

# 1) Remove the last general pre-production-only research rule from the blueprint.
b = replace_exact(
    b,
    'If Project concludes that production viability is still open, it may continue evidence generation locally while the work remains inside the standing assessment envelope.',
    'If viability for the proposed experiment or change scope remains unresolved, Project may continue evidence generation locally while the work remains inside the standing assessment envelope.',
    'blueprint general scoped research rule',
)

# 2) Align the two architectural anchor figures with applicable authorization-set semantics.
old_edge = 'P -->|research-only or production-capable<br/>Project Authorization where applicable| D'
new_edge = 'P -->|applicable Project Authorization scope / set<br/>research-only and/or production-capable where applicable| D'
m = replace_exact(m, old_edge, new_edge, 'manuscript Figure 8/9 authorization-set edge', expected=2)

m = replace_exact(
    m,
    'Project turns the applicable Organizational decision into a scoped technical Project Authorization where one is needed. Delivery and Runtime may operate only inside that scope.',
    'Project turns the applicable Organizational decision into a scoped technical Project Authorization member or authorization set where one is needed. Delivery and Runtime may operate only inside the applicable scope/set and its explicit precedence or interaction semantics where multiple authorizations coexist.',
    'Figure 8 caption authorization set',
)

m = replace_exact(
    m,
    'research-only and production-capable Project Authorization remain distinct; Delivery/Runtime reassessment evidence returns to Delivery or Project;',
    'research-only and production-capable Project Authorization remain distinct scoped authorization forms and may coexist only under explicit scope/precedence semantics; Delivery/Runtime reassessment evidence returns to Delivery or Project;',
    'Figure 9 caption authorization set',
)

# Keep the blueprint figure contract in sync with the publication-facing anchor figures.
b = replace_exact(
    b,
    'including initial assessment eligibility, the Organization ↔ Project / Architecture viability/business/research-authorization handshake, research-only versus production-capable Project Authorization, downward inheritance into Delivery, and separate routing of lower-level reassessment evidence versus exogenous Organizational change.',
    'including initial assessment eligibility, the Organization ↔ Project / Architecture viability/business/research-authorization handshake, the applicable Project Authorization scope/set with research-only and/or production-capable scoped members where applicable, downward inheritance into Delivery, and separate routing of lower-level reassessment evidence versus exogenous Organizational change.',
    'blueprint Figure 8/9 contract authorization set',
)

b = replace_exact(
    b,
    'whether the current Project Authorization is research-only or production-capable, and whether the resulting control perimeter makes economic sense.',
    'which Project Authorization scope or authorization set applies—including member type/scope and precedence or interaction where multiple authorizations coexist—and whether the resulting control perimeter makes economic sense.',
    'blueprint landscape authorization-set question',
)

# Tight guards for the two review findings.
joined = b + '\n' + m
for obsolete in [
    'If Project concludes that production viability is still open, it may continue evidence generation locally',
    'P -->|research-only or production-capable<br/>Project Authorization where applicable| D',
    'Delivery and Runtime may operate only inside that scope.',
    'whether the current Project Authorization is research-only or production-capable',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'If viability for the proposed experiment or change scope remains unresolved, Project may continue evidence generation locally',
    'applicable Project Authorization scope / set<br/>research-only and/or production-capable where applicable',
    'authorization set where one is needed',
    'may coexist only under explicit scope/precedence semantics',
    'which Project Authorization scope or authorization set applies',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
