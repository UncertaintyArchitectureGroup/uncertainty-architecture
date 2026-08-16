from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')

b = bp.read_text()
m = ms.read_text()


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 occurrence, found {count}')
    return text.replace(old, new, 1)

# 1) Figure 11 caption: distinguish Project-local research from reserved-boundary research.
m = replace_once(
    m,
    'Organization is reactivated when a Project conclusion requires a changed business/authority/investment premise, when bounded research is requested, or when the business decision is to proceed, reshape, defer, or stop. Bounded research remains two-step: Project defines a controllable experiment, Organization issues a specific Bounded Research Authorization, and Project then issues the research-only technical baseline.',
    'Organization is reactivated when a Project conclusion requires a changed business/authority/investment premise, when proposed research crosses an Organizationally reserved boundary, or when the business decision is to proceed, reshape, defer, or stop. Research that stays inside the standing assessment envelope may remain Project-local; research that crosses an Organizationally reserved boundary follows the two-step authorization path: Project defines a controllable experiment, Organization issues a specific Bounded Research Authorization, and Project then issues the research-only technical baseline.',
    'Figure 11 reserved-boundary research caption',
)

# 2) Organization horizon: do not imply an exhaustive two-stage taxonomy; make exogenous activation explicit.
m = replace_once(
    m,
    'The Organizational horizon has **two distinct decision moments** inside one level.',
    'Two recurring authorization contexts are especially important in the Organization ↔ Project / Architecture handshake.',
    'Organization recurring contexts wording',
)

m = replace_once(
    m,
    'Organization may instead reshape the basis, defer, or stop.\n\nA specific Bounded Research Authorization is therefore downstream of Project\'s experiment design, not a duplicate of initial eligibility,',
    'Organization may instead reshape the basis, defer, or stop. The same Organizational horizon may also be reactivated directly by exogenous authoritative or business-basis changes, without a preceding Project finding.\n\nA specific Bounded Research Authorization is therefore downstream of Project\'s experiment design, not a duplicate of initial eligibility,',
    'Organization exogenous activation sentence',
)

# 3) Section 5 blueprint: qualify the bounded-research chain and remove duplicated wording.
b = replace_once(
    b,
    'For bounded research:\n\n```text\ninitial assessment eligibility\n→ Project viability conclusion: further research required\n→ Project-defined experiment: purpose / control envelope / exposure / stopping conditions / evidence obligations\n→ specific Organizational Bounded Research Authorization\n→ research-only Project Authorization\n→ Delivery-approved bounded research Requirement and Operating Envelope\n→ experiment evidence\n→ Project viability reassessment\n→ no automatic production promotion\n```',
    'For **reserved-boundary bounded research**:\n\nProject-local evidence generation that remains entirely inside the standing assessment envelope does not enter this authorization chain. When the needed experiment crosses an Organizationally reserved boundary, use:\n\n```text\ninitial assessment eligibility\n→ Project viability conclusion: further research required\n→ Project-defined reserved-boundary experiment: purpose / control envelope / exposure / stopping conditions / evidence obligations\n→ specific Organizational Bounded Research Authorization\n→ research-only Project Authorization\n→ Delivery-approved bounded research Requirement and Operating Envelope\n→ experiment evidence\n→ Project viability reassessment\n→ no automatic production promotion\n```',
    'Section 5 reserved-boundary research chain',
)

b = replace_once(
    b,
    '→ Organizational business/basis/research/continuation decision where required where required',
    '→ Organizational business/basis/research/continuation decision where required',
    'duplicate where required',
)

# Guards for the exact review findings.
for phrase in [
    'when bounded research is requested, or when the business decision',
    'Bounded research remains two-step:',
    'The Organizational horizon has **two distinct decision moments** inside one level.',
    'For bounded research:\n\n```text',
    'where required where required',
]:
    if phrase in m or phrase in b:
        raise SystemExit('obsolete wording remains: ' + phrase)

# Required replacements must now exist.
required = [
    'research that crosses an Organizationally reserved boundary follows the two-step authorization path',
    'Two recurring authorization contexts are especially important in the Organization ↔ Project / Architecture handshake.',
    'reactivated directly by exogenous authoritative or business-basis changes',
    'For **reserved-boundary bounded research**:',
    'Project-local evidence generation that remains entirely inside the standing assessment envelope does not enter this authorization chain.',
]
joined = b + '\n' + m
for phrase in required:
    if phrase not in joined:
        raise SystemExit('required wording missing: ' + phrase)

bp.write_text(b)
ms.write_text(m)
