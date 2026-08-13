from pathlib import Path
import math
import re

mp = Path('content/research/notes/open-engineering-specification-article-draft.md')
bp = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
m = mp.read_text()
b = bp.read_text()

pairs = [
('It also appears in the runtime selection or construction of behavior inside the software boundary.', 'It also appears in the runtime selection or construction of behavior inside the controlled object.'),
('The final transition introduces the problem of engineering and operating systems in which consequential behavior is partly produced through probabilistic Model Judgment inside the software boundary.', 'The final transition introduces the problem of engineering and operating systems in which consequential behavior is partly produced through probabilistic Model Judgment inside the controlled object.'),
('The same controlled object will be carried through the rest of the paper—from category classification and AI-necessity questions through organizational authorization, Project / Architecture viability, Delivery realization, Runtime operation, and reassessment.', 'The same controlled object will be carried through the rest of the paper—from category classification and AI-necessity questions through authorization, architectural viability, concrete realization, active operation, and reassessment.'),
('The complete system may still lack a defensible connection between what the organization permits, what the project authorizes, what the delivery team has realized, what runtime evidence means, and what action follows when assumptions fail.', 'The complete system may still lack a defensible connection between the authoritative limits of the system, the assumptions under which it is designed, the boundary actually realized, the evidence produced in operation, and the corrective decisions available when those assumptions fail.'),
('Each substitution may be understandable, and each may be wrong.', 'Each substitution may be understandable, and each may be wrong. None of these substitutions establishes the missing control relationship by itself.')]
for old,new in pairs:
    assert m.count(old)==1,(old,m.count(old))
    m=m.replace(old,new)

old='- Define the whole support-resolution controlled object at this stage, but leave the required evidence, decision, authority, and corrective paths explicitly unresolved so Sections 5.2–5.4 derive them rather than smuggle the solution into the premise.'
new='- Define the whole support-resolution controlled object at this stage, but leave the required evidence, decision, authority, and corrective paths explicitly unresolved so Sections 5.2–5.4 derive them rather than smuggle the solution into the premise. Section 5.1 may name problem domains such as authorization, architectural viability, realization, operation, and reassessment, but it must not yet present `Organization`, `Project / Architecture`, `Delivery`, and `Runtime` as the canonical decision-horizon model.'
assert b.count(old)==1
b=b.replace(old,new)
old='- Use the material-control-responsibility release-readiness criterion here, but defer explicit `four horizons × four capability families` language until those models have been introduced.'
new='- Use the material-control-responsibility release-readiness criterion here, but defer canonical decision-horizon labels and explicit `four horizons × four capability families` language until those models have been introduced. Section 1 may foreshadow the underlying problem domains without presenting them as the operating model.'
assert b.count(old)==1
b=b.replace(old,new)

sec1=m.split('## 1. Engineering Evolves Around Dominant Uncertainty',1)[1].split('## 2. The Controlled Object Has Changed',1)[0]
count=len(re.findall(r"\b[\w’'-]+\b",sec1))
lower=int(math.floor((count*0.90)/50.0)*50)
upper=int(math.ceil((count*1.10)/50.0)*50)
old='**Working word budget:** 1,100–1,450'
new=f'**Working word budget:** {lower:,}–{upper:,}  <!-- reconciled against current Section 1 (~{count:,} words) -->'
assert b.count(old)==1
b=b.replace(old,new)

mp.write_text(m)
bp.write_text(b)
print(f'Section 1 words: {count}; budget: {lower}-{upper}')
