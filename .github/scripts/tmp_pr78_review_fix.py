from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')
tr = Path('content/research/framework-traceability.md')


def one(text, old, new, label):
    c = text.count(old)
    if c != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {c}')
    return text.replace(old, new)

# Blueprint: keep redesign authority Project-local when standing Organizational basis is unchanged.
b = bp.read_text()
b = one(
    b,
    "If Project concludes that the architecture is no longer viable, that economics/Model-Judgment necessity/business assumptions are invalid, that a simpler path is preferable, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued.",
    "If Project concludes that the architecture is no longer viable, that economics/Model-Judgment necessity or an Organizationally owned business assumption is invalid, that Architectural Veto now applies, that a new specific Bounded Research Authorization is required, or that a changed Organizational boundary/exception/business/continuation decision is required, Project routes the conclusion/proposal to Organization before a new scoped technical baseline can be issued. If Project instead prefers a simpler technical path that still satisfies the standing Organizational business/authority basis, Project may select that path, confirm its category, and either reauthorize the resulting narrower Thinking System or exit this lifecycle when the selected design is no longer a Thinking System; no Organizational architecture-selection step is required.",
    'blueprint delivery escalation')

b = one(
    b,
    "   → simpler path preferred / economics / Model-Judgment necessity / business basis invalidated / new research authorization needed / Architectural Veto / Organizational change required: Organizational review\nOrganizational review\n   → select simpler path / specific bounded research / changed business or authority basis / renewed Business Authorization\n   → Project category/viability reassessment before Delivery proceeds under a new scope",
    "   → simpler technical path still satisfies standing Organizational basis: Project selects path → category confirmation → local Project Reauthorization if still a Thinking System, otherwise exit this lifecycle\n   → economics / Model-Judgment necessity challenges an Organizationally owned premise / new research authorization needed / Architectural Veto requires a changed proposal / Organizational change or continuation decision required: Organizational review\nOrganizational review\n   → specific bounded research / changed business or authority basis / renewed Business Authorization / reshape / defer / stop\n   → Project category/viability reassessment before Delivery proceeds under a new scope",
    'blueprint figure12 routing')

bp.write_text(b)

# Manuscript: Organizational second decision only for findings that actually implicate Organization.
m = ms.read_text()
m = one(
    m,
    "The second is the **Organizational decision on the Project viability conclusion**. Project / Architecture returns evidence about Model-Judgment necessity, alternatives, control feasibility, Human Authority, fallback, capacity, residual uncertainty, and complete control economics. Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when production viability remains unresolved but Project has defined a credibly bounded experiment, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it. Organization may instead reshape the basis, defer, or stop.",
    "The second is an **Organizational decision on Project findings that implicate an Organizationally owned basis or initiative-level decision**. Project-local technical/design and category outcomes do not activate this second Organizational moment when they remain inside the standing business/authority basis. When Organizational action is required, Project / Architecture returns the relevant evidence about Model-Judgment necessity, alternatives, control feasibility, Human Authority, fallback, capacity, residual uncertainty, and complete control economics. Organization may then issue one of two different positive authorizations: a **specific Bounded Research Authorization** when production viability remains unresolved but Project has defined a credibly bounded experiment, or an **Organizational Business Authorization** when a technically viable production basis exists and the organization chooses to pursue it. Organization may instead reshape the basis, defer, or stop.",
    'manuscript org second moment')

m = one(
    m,
    'LOW["Project viability conclusion / Runtime evidence<br/> research proposal · Architectural Veto · economics<br/> Model Judgment necessity · authority-change requests"]',
    'LOW["Project findings / Organizationally relevant escalated evidence<br/> research proposal · Architectural Veto · economics<br/> Model Judgment necessity · authority-change requests"]',
    'manuscript figure10 low node')
m = one(
    m,
    "**Figure 10 — Organizational control process across the lifecycle.** Authoritative/business context, external evidence, and Project/Runtime evidence converge on legitimate Organizational decision owners.",
    "**Figure 10 — Organizational control process across the lifecycle.** Authoritative/business context, external evidence, and Project findings or Organizationally relevant escalated evidence converge on legitimate Organizational decision owners. Operational notification may occur broadly, but decision ownership still follows the basis being reassessed.",
    'manuscript figure10 caption')
ms.write_text(m)

# Traceability: keep one canonical Needs Resolution row for this lifecycle hypothesis.
t = tr.read_text()
old_row = "| A project-level engineering viability conclusion and the organizational business decision to pursue an initiative may need to remain distinct decision semantics; bounded research also needs an explicit technical authorization scope even when production viability is not yet established. | 2026-08-15 article blueprint/manuscript lifecycle synthesis | Doctrine, lifecycle, pattern, and artifact | Needs Resolution | Current status-bearing framework material places project viability, authorization, deferral, and No-Go together at Project level. The article is testing a sharper handshake: Project / Architecture owns AI necessity, technical/design selection within the standing Organizational business/authority basis, category confirmation, and the viability conclusion; Organization owns the business outcome and authoritative/investment basis plus specific bounded-research and proceed/continue/reshape/defer/do-not-proceed decisions; Project Authorization is a scoped technical baseline and may be **research-only** or **production-capable**. This remains research until deliberate framework review reconciles or rejects it. |\n"
if t.count(old_row) != 1:
    raise SystemExit(f'traceability duplicate row: expected 1, found {t.count(old_row)}')
t = t.replace(old_row, '')
if not t.endswith('\n'):
    t += '\n'
tr.write_text(t)
