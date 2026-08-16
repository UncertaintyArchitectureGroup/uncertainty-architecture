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

# 1) Central manuscript diagrams must route only reserved-boundary research to Organization.
m = replace_exact(
    m,
    'P -->|specific research request / viable production basis<br/>or changed Organizational premise / continuation decision| O',
    'P -->|reserved-boundary research request / viable production basis<br/>or changed Organizational premise / continuation decision| O',
    'Figure 8/9 reserved-boundary research edge',
    expected=2,
)

# 2) Final Section 4 ownership takeaway must preserve research proportionality.
m = replace_exact(
    m,
    '> **Project / Architecture owns Model-Judgment necessity, technical/design selection within the standing Organizational business/authority basis, category confirmation, and the viability conclusion. Organization owns the business outcome and basis plus the decisions to authorize a specific bounded experiment, pursue a viable production basis, reshape that basis, defer, or stop. Project Authorization is the scoped technical baseline that connects the applicable Organizational decision to Delivery.**',
    '> **Project / Architecture owns Model-Judgment necessity, technical/design selection within the standing Organizational business/authority basis, category confirmation, and the viability conclusion. Organization owns the business outcome and basis plus the decisions to authorize specific bounded research when the experiment crosses an Organizationally reserved boundary, pursue a viable production basis, reshape that basis, defer, or stop. Project Authorization is the scoped technical baseline that connects the applicable Organizational decision to Delivery.**',
    'Section 4 closing ownership takeaway',
)

# 3) Blueprint Organization activation/questions: an experiment reaches Organization only when reserved authority is implicated.
b = replace_exact(
    b,
    '- a Project-defined bounded experiment whose evidence question, scope, data/tools, reachable authority, stopping conditions, and control envelope are ready for an Organizational research decision;',
    '- a Project-defined bounded experiment that crosses an Organizationally reserved boundary and whose evidence question, scope, data/tools, reachable authority, stopping conditions, and control envelope are ready for an Organizational research decision;',
    'Organization activation trigger for research',
)

b = replace_exact(
    b,
    '- When Project returns a finding that implicates Organizationally owned research, business, authority, investment, or continuation decisions, should the organization proceed/continue on the viable production basis, authorize the Project-defined bounded experiment, reshape the business case or authority basis, defer, or stop? Project-local technical/category outcomes inside the standing Organizational basis do not require this second Organizational decision.',
    '- When Project returns a finding that implicates Organizationally owned research, business, authority, investment, or continuation decisions, should the organization proceed/continue on the viable production basis, authorize the Project-defined reserved-boundary experiment, reshape the business case or authority basis, defer, or stop? Project-local technical/category outcomes and evidence generation inside the standing Organizational assessment/business basis do not require this second Organizational decision.',
    'Organization question for reserved-boundary research',
)

b = replace_exact(
    b,
    '- If production viability remains unresolved but Project proposes a credibly bounded experiment, is **that specific evidence** worth acquiring, and do the proposed exposure, data/tools, authority, stopping conditions, Human Authority/fallback, and evidence obligations fit Organizational limits?',
    '- If production viability remains unresolved and the needed credibly bounded experiment crosses an Organizationally reserved boundary, is **that specific evidence** worth acquiring, and do the proposed exposure, data/tools, authority, stopping conditions, Human Authority/fallback, and evidence obligations fit Organizational limits?',
    'Organization research decision question qualification',
)

# 4) Section 5 reusable research carrier chain must support recurrent reassessment, not only initial pre-production flow.
b = replace_exact(
    b,
    '```text\ninitial assessment eligibility\n→ Project viability conclusion: further research required\n→ Project-defined reserved-boundary experiment: purpose / control envelope / exposure / stopping conditions / evidence obligations\n→ specific Organizational Bounded Research Authorization\n→ research-only Project Authorization\n→ Delivery-approved bounded research Requirement and Operating Envelope\n→ experiment evidence\n→ Project viability reassessment\n→ no automatic production promotion\n```',
    '```text\nstanding Organizational assessment / research / business basis\n→ Project viability analysis or reassessment: further research required\n→ Project-defined reserved-boundary experiment: purpose / control envelope / exposure / stopping conditions / evidence obligations\n→ specific Organizational Bounded Research Authorization\n→ research-only Project Authorization\n→ Delivery-approved bounded research Requirement and Operating Envelope\n→ experiment evidence\n→ Project viability reassessment\n→ no automatic production promotion\n```\n\nFor the first research cycle, the standing basis may be only initial assessment eligibility; later cycles may begin from an existing research or production basis that new evidence has caused Project to reassess.',
    'Section 5 recurrent reserved-boundary research chain',
)

# 5) Keep the category-exit term precise everywhere in the two living article documents.
for name, text in [('blueprint', b), ('manuscript', m)]:
    text = text.replace('Thinking-System lifecycle', 'Thinking-System-specific lifecycle')
    if name == 'blueprint':
        b = text
    else:
        m = text

# Guards for the findings being closed.
joined = b + '\n' + m
for obsolete in [
    'P -->|specific research request / viable production basis<br/>or changed Organizational premise / continuation decision| O',
    'Organization owns the business outcome and basis plus the decisions to authorize a specific bounded experiment, pursue a viable production basis',
    'a Project-defined bounded experiment whose evidence question, scope, data/tools, reachable authority, stopping conditions, and control envelope are ready for an Organizational research decision',
    'authorize the Project-defined bounded experiment, reshape the business case',
    'If production viability remains unresolved but Project proposes a credibly bounded experiment, is **that specific evidence** worth acquiring',
    '```text\ninitial assessment eligibility\n→ Project viability conclusion: further research required\n→ Project-defined reserved-boundary experiment',
    'Thinking-System lifecycle',
]:
    if obsolete in joined:
        raise SystemExit('obsolete wording remains: ' + obsolete)

required = [
    'reserved-boundary research request / viable production basis',
    'authorize specific bounded research when the experiment crosses an Organizationally reserved boundary',
    'Project-defined bounded experiment that crosses an Organizationally reserved boundary',
    'Project-defined reserved-boundary experiment',
    'standing Organizational assessment / research / business basis',
    'Project viability analysis or reassessment: further research required',
    'For the first research cycle, the standing basis may be only initial assessment eligibility',
    'Thinking-System-specific lifecycle',
]
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
