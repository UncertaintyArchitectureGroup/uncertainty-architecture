from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')


def exact(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1, found {n}')
    return text.replace(old, new)


def replace_at_least(text, old, new, label, minimum=1):
    n = text.count(old)
    if n < minimum:
        raise SystemExit(f'{label}: expected >= {minimum}, found {n}')
    return text.replace(old, new)

b = bp.read_text()

# 1) Remove remaining old Organization-selects-design/path semantics from §§7–8.
b = exact(
    b,
    "including its explicit assessment-eligibility / Project-viability / Organizational-path-research-business / scoped-Project-Authorization lifecycle refinement",
    "including its explicit assessment-eligibility / Project technical-design-and-viability / Organizational business-research-basis authority where required / scoped-Project-Authorization lifecycle refinement",
    'section7 closing claim ownership'
)

b = exact(
    b,
    "category confirmation can also identify when an Organizationally selected redesign removes the system from the class",
    "category confirmation can also identify when a Project-selected redesign inside the standing Organizational basis removes the system from the class",
    'program1 category ownership'
)

b = exact(
    b,
    "Project and Organization cannot separate technical/design authority from business-outcome/basis authority; category exit is ambiguous;",
    "Project and Organization cannot separate Project-owned technical/design authority from Organization-owned business-outcome/basis authority; category exit is ambiguous;",
    'program3 authority wording'
)

b = replace_at_least(
    b,
    "Project viability and Organizational path/business/research authority",
    "Project technical/design viability and Organizational business/basis/research authority",
    'section8 old path authority phrase',
    1
)

b = exact(
    b,
    "cases where Project concluded Model Judgment was unnecessary and Organization either selected the simpler design, changed the intended outcome, or stopped, including the resulting category confirmation;",
    "cases where Project concluded Model Judgment was unnecessary and selected a simpler design inside the standing Organizational basis, including the resulting category confirmation; separately record cases where Organization changed the intended outcome/basis or stopped the initiative and Project then reassessed the changed basis;",
    'section8 evidence simpler-design ownership'
)

b = replace_at_least(
    b,
    "assessment/viability/path/research/business-authorization semantics",
    "assessment/technical-viability/business-basis/research-authorization semantics",
    'section8 substitution wording',
    1
)

b = replace_at_least(
    b,
    "Organizational-path-research-business",
    "Organizational-business-research-basis-authority-where-required",
    'remaining old org path token',
    1
)

# 2) Make canonical Figure 8 category exit explicitly a governance handoff, not business authorization.
b = exact(
    b,
    "   ├─ simpler deterministic/manual design → category confirmation → exit Thinking-System lifecycle when category test is negative",
    "   ├─ simpler deterministic/manual design → category confirmation → if negative, exit the Thinking-System-specific lifecycle and hand off to ordinary product/software governance; normal funding / initiative / delivery / release authority still applies",
    'figure8 category exit handoff'
)

# Also reinforce the explanatory paragraph immediately below the canonical model.
b = exact(
    b,
    "The repeated Organization and Project / Architecture labels are repeated **decisions at the same two horizons**, not additional lifecycle levels. The diagram must make the handshake legible without turning it into a mandatory sequence of separate meetings or implying that every local Project Reauthorization requires a new Organizational decision. A Project change that remains production-viable and inside the standing Organizational business/authority basis may be reauthorized at Project level; research may remain under a research-only Project Authorization only while the **specific** Organizational research basis still applies; Organization is reactivated when its own business/authority basis is implicated or changes exogenously. Initial assessment eligibility must never be drawn as if it already authorized a concrete experiment.",
    "The repeated Organization and Project / Architecture labels are repeated **decisions at the same two horizons**, not additional lifecycle levels. The diagram must make the handshake legible without turning it into a mandatory sequence of separate meetings or implying that every local Project Reauthorization requires a new Organizational decision. A Project change that remains production-viable and inside the standing Organizational business/authority basis may be reauthorized at Project level; a negative category confirmation exits only the Thinking-System-specific lifecycle and hands the selected design to ordinary product/software governance, without granting funding, initiative, delivery, or release authorization; research may remain under a research-only Project Authorization only while the **specific** Organizational research basis still applies; Organization is reactivated when its own business/authority basis is implicated or changes exogenously. Initial assessment eligibility must never be drawn as if it already authorized a concrete experiment.",
    'figure8 explanatory handoff'
)

bp.write_text(b)

m = ms.read_text()

# 3) Narrow Figure 10's Model-Judgment-necessity lane to findings that actually require Organization.
m = exact(
    m,
    'LOW["Project findings / Organizationally relevant escalated evidence<br/> research proposal · Architectural Veto · economics<br/> Model Judgment necessity · authority-change requests"]',
    'LOW["Project findings / Organizationally relevant escalated evidence<br/> research proposal · Architectural Veto · economics<br/> Model-Judgment-necessity finding requiring Organizational basis / continuation action · authority-change requests"]',
    'manuscript figure10 model-judgment lane'
)

ms.write_text(m)
