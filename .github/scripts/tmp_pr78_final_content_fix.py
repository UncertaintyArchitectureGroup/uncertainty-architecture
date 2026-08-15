from pathlib import Path
import re

bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms=Path('content/research/notes/open-engineering-specification-article-draft.md')

m=ms.read_text()

# 1) Project question: make the two-route result explicit.
m=re.sub(
    r'\*\*Question owned:\*\* Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist, and what is the resulting technical, operational, and economic \*\*Project viability conclusion\*\* to return to Organization\?',
    '**Question owned:** Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist, what technical/category outcome or Project viability finding follows, and does that result require Organizational action?',
    m,
    count=1,
)

# 2) Local non-Thinking-System outcome: category exit is a governance handoff, not business authorization.
m=m.replace(
    'If no Consequential Runtime Responsibility remains materially dependent on Model Judgment, that design exits the Thinking-System lifecycle without a second Organizational architecture approval. If a narrower Thinking-System candidate remains, Project continues viability analysis at that narrower scope.',
    'If no Consequential Runtime Responsibility remains materially dependent on Model Judgment, that design exits the Thinking-System-specific lifecycle and hands off to ordinary product/software governance without a second Organizational architecture approval; the category decision does not itself authorize funding, initiative continuation, delivery, or release. If a narrower Thinking-System candidate remains, Project continues viability analysis at that narrower scope.'
)

# 3) Project research path: only Organizationally reserved exposure/commitment requires specific research authorization.
m=m.replace(
    'There is one important intermediate case: a material uncertainty may be unresolved while a **bounded experiment itself can be controlled credibly**. Project may then conclude `further research required` and specify the minimum research control envelope and evidence needed to answer the open question. This is not production viability. It is the technical basis for a **specific Bounded Research Authorization decision** by Organization. Initial assessment eligibility alone is not enough to expose the experiment.',
    'There is one important intermediate case: a material uncertainty may be unresolved while an **experiment itself can be controlled credibly**. Project may then conclude `further research required` and specify the minimum research control envelope and evidence needed to answer the open question. This is not production viability. When the experiment stays entirely inside the standing assessment envelope—for example local simulation, offline/synthetic evaluation, or engineering work with no Organizationally reserved exposure, authority, sensitive data access, material commitment, or external effect—Project may conduct it locally under the ordinary engineering controls applicable to that envelope. When the experiment crosses an Organizationally owned boundary, the Project-defined envelope becomes the technical basis for a **specific Bounded Research Authorization decision** by Organization, followed by a research-only Project Authorization. Initial assessment eligibility alone is not enough to expose an experiment beyond that standing envelope.'
)

# 4) Canonical category-exit nodes/captions.
m=m.replace('EXIT["Exit Thinking-System lifecycle<br/>ordinary product / software lifecycle"]', 'EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal funding · initiative · delivery · release authority still applies"]')
m=m.replace('EXIT["Exit Thinking-System lifecycle"]', 'EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product/software governance"]')
m=m.replace('EXIT["No → exit Thinking-System lifecycle<br/>continue ordinary product / software lifecycle"]', 'EXIT["No → exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal business/delivery authority still applies"]')
m=m.replace(
    'Project / Architecture owns technical/design selection within the standing Organizational business and authority basis and can confirm category locally: a selected design exits the Thinking-System lifecycle when no Consequential Runtime Responsibility remains materially dependent on Model Judgment.',
    'Project / Architecture owns technical/design selection within the standing Organizational business and authority basis and can confirm category locally: a selected design exits the Thinking-System-specific lifecycle when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, then hands off to ordinary product/software governance where normal funding, initiative, delivery, and release authorities still apply.'
)
m=m.replace(
    'A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System lifecycle immediately after a negative category test; it does not require an Organizational architecture-selection ceremony.',
    'A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System-specific lifecycle immediately after a negative category test; that exit is a handoff to ordinary product/software governance, not an Organizational funding, initiative, delivery, or release authorization, and it does not require an Organizational architecture-selection ceremony.'
)

# Accept already partially updated variants and strengthen them too.
m=m.replace('No → exit Thinking-System lifecycle<br/>continue ordinary product / software lifecycle', 'No → exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal business/delivery authority still applies')
m=m.replace('Exit Thinking-System lifecycle<br/>ordinary product / software lifecycle', 'Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal funding · initiative · delivery · release authority still applies')

# Essential postconditions.
required_m = [
    'what technical/category outcome or Project viability finding follows, and does that result require Organizational action?',
    'category decision does not itself authorize funding, initiative continuation, delivery, or release',
    'When the experiment crosses an Organizationally owned boundary',
    'handoff to ordinary product / software governance',
]
for s in required_m:
    if s not in m:
        raise SystemExit(f'manuscript postcondition missing: {s}')
ms.write_text(m)

b=bp.read_text()

# Core category-exit semantics.
b=b.replace(
    'A simpler alternative is a Project architecture/viability conclusion. When it satisfies the same standing Organizational business outcome and authority basis, Project may select it and confirm category status directly; the design exits this lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment.',
    'A simpler alternative is a Project architecture/viability conclusion. When it satisfies the same standing Organizational business outcome and authority basis, Project may select it and confirm category status directly; the design exits the Thinking-System-specific lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, and that exit hands the selected design to ordinary product/software governance rather than authorizing funding, initiative continuation, delivery, or release by itself.'
)
b=b.replace(
    'State explicitly that Project may identify a candidate simpler design/category result, but Project / Architecture selects the technical/design path within the standing Organizational business/authority basis; Organization changes the Organizational business/authority/investment basis when needed; a selected non-Thinking-System design exits this lifecycle only after Project confirms that the selected design no longer meets the category test.',
    'State explicitly that Project may identify a candidate simpler design/category result, but Project / Architecture selects the technical/design path within the standing Organizational business/authority basis; Organization changes the Organizational business/authority/investment basis when needed; a selected non-Thinking-System design exits the Thinking-System-specific lifecycle only after Project confirms that the selected design no longer meets the category test, and then hands off to ordinary product/software governance where otherwise applicable business, funding, delivery, and release authorities still apply.'
)

# Research proportionality in Article §4 lifecycle-refinement paragraph.
b=b.replace(
    'Research-only Project Authorization may follow only that specific Bounded Research Authorization while production viability remains open, provided the experiment itself has a credible bounded control envelope; **production-capable Project Authorization** follows only a positive Organizational Business Authorization on a technically viable production basis.',
    'Research-only Project Authorization may follow only that specific Bounded Research Authorization while production viability remains open, provided the experiment itself has a credible bounded control envelope; Project-local simulation, offline/synthetic evaluation, and engineering experiments may remain inside the standing assessment envelope without a separate Organizational research decision when they do not consume or create reserved Organizational exposure, authority, sensitive data access, material budget/capacity, external commitment, or another reserved premise; **production-capable Project Authorization** follows only a positive Organizational Business Authorization on a technically viable production basis.'
)

# Strengthen recurring shorthand.
b=b.replace('Project-selected-design category exit', 'Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization')
b=b.replace('exits this lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment', 'exits the Thinking-System-specific lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, with handoff to ordinary product/software governance rather than automatic business authorization')

required_b = [
    'ordinary product/software governance rather than authorizing funding, initiative continuation, delivery, or release by itself',
    'Project-local simulation, offline/synthetic evaluation, and engineering experiments may remain inside the standing assessment envelope',
]
for s in required_b:
    if s not in b:
        raise SystemExit(f'blueprint postcondition missing: {s}')
bp.write_text(b)
