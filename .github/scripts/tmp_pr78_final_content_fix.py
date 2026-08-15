from pathlib import Path

bp=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
ms=Path('content/research/notes/open-engineering-specification-article-draft.md')

def one(text, old, new, label):
    n=text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 occurrence, found {n}')
    return text.replace(old,new)

def atleast(text, old, new, label, minimum=1):
    n=text.count(old)
    if n < minimum:
        raise SystemExit(f'{label}: expected >= {minimum}, found {n}')
    return text.replace(old,new)

# --- Manuscript ---
m=ms.read_text()

# Question-owned wording must match two-route model.
m=one(m,
"**Question owned:** Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist, and what is the resulting technical, operational, and economic **Project viability conclusion** to return to Organization?",
"**Question owned:** Is Model Judgment needed for the stated outcome, does a credible complete bounded control architecture exist, what technical/category outcome or Project viability finding follows, and does that result require Organizational action?",
'manuscript project question')

# Project-local outcome must carry handoff semantics.
m=one(m,
"If no Consequential Runtime Responsibility remains materially dependent on Model Judgment, that design exits the Thinking-System lifecycle without a second Organizational architecture approval. If a narrower Thinking-System candidate remains, Project continues viability analysis at that narrower scope.",
"If no Consequential Runtime Responsibility remains materially dependent on Model Judgment, that design exits the Thinking-System-specific lifecycle and hands off to ordinary product/software governance without a second Organizational architecture approval; the category decision does not itself authorize funding, initiative continuation, delivery, or release. If a narrower Thinking-System candidate remains, Project continues viability analysis at that narrower scope.",
'manuscript project local output')

# Project research path must use proportional boundary rather than unconditional Organization.
m=one(m,
"There is one important intermediate case: a material uncertainty may be unresolved while a **bounded experiment itself can be controlled credibly**. Project may then conclude `further research required` and specify the minimum research control envelope and evidence needed to answer the open question. This is not production viability. It is the technical basis for a **specific Bounded Research Authorization decision** by Organization. Initial assessment eligibility alone is not enough to expose the experiment.",
"There is one important intermediate case: a material uncertainty may be unresolved while an **experiment itself can be controlled credibly**. Project may then conclude `further research required` and specify the minimum research control envelope and evidence needed to answer the open question. This is not production viability. When the experiment stays entirely inside the standing assessment envelope—for example local simulation, offline/synthetic evaluation, or engineering work with no Organizationally reserved exposure, authority, sensitive data access, material commitment, or external effect—Project may conduct it locally under the ordinary engineering controls applicable to that envelope. When the experiment crosses an Organizationally owned boundary, the Project-defined envelope becomes the technical basis for a **specific Bounded Research Authorization decision** by Organization, followed by a research-only Project Authorization. Initial assessment eligibility alone is not enough to expose an experiment beyond that standing envelope.",
'manuscript project research boundary')

# Figure 8 + Figure 9 exit nodes.
m=atleast(m,
'EXIT["Exit Thinking-System lifecycle<br/>ordinary product / software lifecycle"]',
'EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal funding · initiative · delivery · release authority still applies"]',
'manuscript figure8 exit node',1)
m=atleast(m,
'EXIT["Exit Thinking-System lifecycle"]',
'EXIT["Exit Thinking-System-specific lifecycle<br/>handoff to ordinary product/software governance"]',
'manuscript figure9 exit node',1)
m=atleast(m,
'EXIT["No → exit Thinking-System lifecycle<br/>continue ordinary product / software lifecycle"]',
'EXIT["No → exit Thinking-System-specific lifecycle<br/>handoff to ordinary product / software governance<br/>normal business/delivery authority still applies"]',
'manuscript figure11 exit node',1)

# Figure captions: category exit is handoff, not authorization.
m=one(m,
"Project / Architecture owns technical/design selection within the standing Organizational business and authority basis and can confirm category locally: a selected design exits the Thinking-System lifecycle when no Consequential Runtime Responsibility remains materially dependent on Model Judgment.",
"Project / Architecture owns technical/design selection within the standing Organizational business and authority basis and can confirm category locally: a selected design exits the Thinking-System-specific lifecycle when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, then hands off to ordinary product/software governance where normal funding, initiative, delivery, and release authorities still apply.",
'figure8 caption exit')
m=one(m,
"A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System lifecycle immediately after a negative category test; it does not require an Organizational architecture-selection ceremony.",
"A simpler architecture that still satisfies that standing basis may be selected at Project and can exit the Thinking-System-specific lifecycle immediately after a negative category test; that exit is a handoff to ordinary product/software governance, not an Organizational funding, initiative, delivery, or release authorization, and it does not require an Organizational architecture-selection ceremony.",
'figure11 caption exit')

ms.write_text(m)

# --- Blueprint ---
b=bp.read_text()

# Core lifecycle refinement: clarify category exit handoff, not business approval.
b=one(b,
"A simpler alternative is a Project architecture/viability conclusion. When it satisfies the same standing Organizational business outcome and authority basis, Project may select it and confirm category status directly; the design exits this lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment.",
"A simpler alternative is a Project architecture/viability conclusion. When it satisfies the same standing Organizational business outcome and authority basis, Project may select it and confirm category status directly; the design exits the Thinking-System-specific lifecycle only when no Consequential Runtime Responsibility remains materially dependent on Model Judgment, and that exit hands the selected design to ordinary product/software governance rather than authorizing funding, initiative continuation, delivery, or release by itself.",
'blueprint lifecycle exit handoff')

# Required framing in section 4 must preserve handoff semantics.
b=one(b,
"State explicitly that Project may identify a candidate simpler design/category result, but Project / Architecture selects the technical/design path within the standing Organizational business/authority basis; Organization changes the Organizational business/authority/investment basis when needed; a selected non-Thinking-System design exits this lifecycle only after Project confirms that the selected design no longer meets the category test.",
"State explicitly that Project may identify a candidate simpler design/category result, but Project / Architecture selects the technical/design path within the standing Organizational business/authority basis; Organization changes the Organizational business/authority/investment basis when needed; a selected non-Thinking-System design exits the Thinking-System-specific lifecycle only after Project confirms that the selected design no longer meets the category test, and then hands off to ordinary product/software governance where otherwise applicable business, funding, delivery, and release authorities still apply.",
'blueprint required framing handoff')

# Research branch boundary in section 4 blueprint.
old="Research-only Project Authorization may follow only that specific Bounded Research Authorization while production viability remains open, provided the experiment itself has a credible bounded control envelope; **production-capable Project Authorization** follows only a positive Organizational Business Authorization on a technically viable production basis."
new="Research-only Project Authorization may follow only that specific Bounded Research Authorization while production viability remains open, provided the experiment itself has a credible bounded control envelope; Project-local simulation, offline/synthetic evaluation, and engineering experiments may remain inside the standing assessment envelope without a separate Organizational research decision when they do not consume or create reserved Organizational exposure, authority, sensitive data access, material budget/capacity, external commitment, or another reserved premise; **production-capable Project Authorization** follows only a positive Organizational Business Authorization on a technically viable production basis."
b=one(b,old,new,'blueprint lifecycle research proportionality')

# Acceptance/figure contract wording: exit is handoff.
b=b.replace("Project-selected-design category exit", "Project-selected-design category exit as handoff to ordinary product/software governance rather than automatic business authorization")

bp.write_text(b)
