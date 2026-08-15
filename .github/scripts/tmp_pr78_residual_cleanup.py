from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()

pairs=[
("selected-path category handshake", "Project-selected-design category confirmation and Organizational business/research/basis handoff where required"),
("Organizational specific-research / business/design review as required", "Organizational specific-research / business-basis / continuation review where required"),
("a new business/design decision", "a new Organizational business/basis decision"),
("Organizational path / specific research / business decision", "Organizational business/basis/specific-research/continuation decision where required"),
("Organizational path/specific-research/business decision", "Organizational business/basis/specific-research/continuation decision where required"),
("Organizational selected-path/business/research", "Organizational business/basis/research/continuation authority where required"),
("business/design authority", "business/basis authority"),
("selected-path/business/research", "business/basis/research/continuation"),
]
for old,new in pairs:
    s=s.replace(old,new)

s=s.replace(
"only a negative category result exits the Thinking-System lifecycle. A selected narrower model-assisted candidate remains a Thinking System if the material dependency remains.",
"only a negative category result exits the Thinking-System-specific lifecycle and hands the design off to ordinary product/software governance without granting business, funding, delivery, or release authorization. A selected narrower model-assisted candidate remains a Thinking System if the material dependency remains.")

s=s.replace(
"current authority-bearing lifecycle/pattern sources do not yet express this exact `assessment eligibility → Project viability conclusion → Organizational business/basis/specific-research/continuation decision where required → scoped Project Authorization` semantics.",
"current authority-bearing lifecycle/pattern sources do not yet express this exact `assessment eligibility → Project technical/design selection and viability → Organizational business/basis/specific-research/continuation decision where required → scoped Project Authorization` semantics.")

# Clean any residual wording from §5/§6 equivalence basis that still conflates path selection with Organization.
s=s.replace("Organizational business/basis decision where required/specific-research/business authorization", "Organizational specific-research/business/basis authority where required")
s=s.replace("Project viability owner/conclusion, Organizational business/basis decision where required/business/research-decision consumer/options", "Project technical/design selection and viability owner/conclusion, Organizational business/basis/research/continuation-decision consumer/options where required")

# Targeted guards: these old semantics should no longer survive in the living blueprint.
for bad in [
    'selected-path category handshake',
    'business/design authority',
    'Organizational path / specific research / business decision',
    'Organizational path/specific-research/business decision',
    'Organizational selected-path',
    'a new business/design decision',
]:
    if bad in s:
        raise SystemExit(f'obsolete phrase remains: {bad}')

p.write_text(s)
