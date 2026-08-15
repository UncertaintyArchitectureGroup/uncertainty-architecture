from pathlib import Path

bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms = Path('content/research/notes/open-engineering-specification-article-draft.md')


def replace_exact(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected exactly 1 occurrence, found {n}')
    return text.replace(old, new)

b = bp.read_text()

# 1) Project primary question must preserve the two-route result semantics.
b = replace_exact(
    b,
    "**Primary question owned:** Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist for production, is a simpler candidate preferable, or what evidence remains missing—and what is the resulting technical/operational/economic **Project viability conclusion** to return to Organization?",
    "**Primary question owned:** Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist for production, is a simpler candidate preferable, or what evidence remains missing—and what technical/category outcome or Project viability finding follows, including whether that result requires Organizational action?",
    'blueprint Project primary question',
)

# Narrow generic blanket wording in the Organizational decision question.
b = replace_exact(
    b,
    "- After receiving the Project viability conclusion and Project-selected technical basis, should the organization proceed/continue on the viable production basis, authorize the Project-defined bounded experiment, reshape the business case or authority basis, defer, or stop?",
    "- When Project returns a finding that implicates Organizationally owned research, business, authority, investment, or continuation decisions, should the organization proceed/continue on the viable production basis, authorize the Project-defined bounded experiment, reshape the business case or authority basis, defer, or stop? Project-local technical/category outcomes inside the standing Organizational basis do not require this second Organizational decision.",
    'blueprint Organizational second-moment question',
)

# 2) Figure 10 contract: no generic Runtime-evidence direct decision route.
b = replace_exact(
    b,
    "**Supporting figure — Figure 10: Organizational control process across the lifecycle:** Replace the current department-centric influence map with a process-oriented Organizational control loop showing initial authoritative/business context, external/Organizational evidence, and Project/Runtime evidence as **converging inputs**, not as a sequential evidence pipeline. The figure may show assessment eligibility and the later specific research/business decision in one Organizational decision surface while labels keep them distinct.",
    "**Supporting figure — Figure 10: Organizational control process across the lifecycle:** Replace the current department-centric influence map with a process-oriented Organizational control loop showing initial authoritative/business context, external/Organizational evidence, and **Project findings / Organizationally relevant escalated evidence** as converging inputs, not as a sequential evidence pipeline. Generic Runtime evidence is not a direct Organizational decision route merely because it exists; operational notification may be broad, while reassessment ownership follows the decision basis being challenged. The figure may show assessment eligibility and the later specific research/business decision in one Organizational decision surface while labels keep them distinct.",
    'blueprint Figure 10 intro',
)

b = replace_exact(
    b,
    "Project viability conclusion / bounded-research proposal / Runtime evidence / authority-change request ─────────┘",
    "Project findings / Organizationally relevant escalated evidence ───────────────────────────────────────────────┘",
    'blueprint Figure 10 lower lane',
)

b = replace_exact(
    b,
    "Examples within the lower-level evidence lane include a Project viability conclusion, bounded-research proposal/result, Architectural Veto, economics/business-case finding, authority request, and Runtime evidence that invalidates an Organizational basis. They are examples of that lane, not additional independent inputs that should be drawn a second time. Exogenous Organizational evidence/basis change remains a parallel direct input to the Organizational Controller.",
    "Examples within the lower-level evidence lane include a Project viability finding requiring Organizational action, bounded-research proposal/result, Architectural Veto, economics/business-case finding, authority request, and lower-level evidence that has been escalated because it materially challenges an Organizationally owned basis. They are examples of that lane, not additional independent inputs that should be drawn a second time. Exogenous Organizational evidence/basis change remains a parallel direct input to the Organizational Controller. Runtime evidence that remains a Delivery- or Project-owned reassessment matter must not be drawn as a generic direct Organizational decision input.",
    'blueprint Figure 10 lane examples',
)

bp.write_text(b)

# 3) Running example must demonstrate research-authorization proportionality.
m = ms.read_text()
m = replace_exact(
    m,
    "For the support-resolution example, Organization might reserve refunds above €50 to Human Authority, constrain customer-data access to approved paths, and permit only approved transaction capabilities. Initial assessment eligibility lets Project compare candidate designs and define evidence gaps. If Project later needs evidence about approval load or evaluator validity, it proposes a concrete experiment; Organization may then issue a specific Bounded Research Authorization for a research-only experiment with no customer-facing transaction authority. If Project later concludes that the production architecture is credible but Human Authority makes each resolution too expensive, Organization may change the business model or scope. If Project concludes that no credible realization can prevent unauthorized transactions for the proposed path, the unchanged proposal cannot proceed merely because its expected revenue is attractive.",
    "For the support-resolution example, Organization might reserve refunds above €50 to Human Authority, constrain customer-data access to approved paths, and permit only approved transaction capabilities. Initial assessment eligibility lets Project compare candidate designs and define evidence gaps. If Project needs to validate evaluator behavior on synthetic or already-authorized offline cases with transaction tools disabled, that evidence work can remain Project-local inside the standing assessment envelope. If Project instead needs to measure real approval load using live customer cases, reserved customer data, production-like tool authority, or another Organizationally owned exposure, it first defines the concrete experiment and control/evidence envelope; Organization may then issue a specific Bounded Research Authorization, after which Project may issue the corresponding research-only technical authorization. If Project later concludes that the production architecture is credible but Human Authority makes each resolution too expensive, Organization may change the business model or scope. If Project concludes that no credible realization can prevent unauthorized transactions for the proposed path, the unchanged proposal cannot proceed merely because its expected revenue is attractive.",
    'manuscript running-example research proportionality',
)
ms.write_text(m)
