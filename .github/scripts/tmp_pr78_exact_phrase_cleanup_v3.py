from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()
for old,new in [
('Organization ↔ Project viability/path/business/research authorization','Organization ↔ Project technical-design-and-viability / business-basis-and-research authorization'),
('Case B for Project viability reassessment → Organizational business/design review → Project Reauthorization or category exit where required','Case B for Project viability reassessment → Project-local redesign/category action when the standing Organizational basis still holds, or Organizational business/basis/continuation review only when its premise is implicated → scoped Project Reauthorization or category exit where applicable'),
('Case B routes through Project viability reassessment to Organizational business/design review because economics, Model-Judgment necessity, or the business basis is invalidated; Project Reauthorization follows only for the resulting technically viable authorized Thinking-System basis, while a selected non-Thinking-System alternative exits after Project confirms category status.','Case B routes through Project viability reassessment; a Model-Judgment-necessity or technical-design change remains Project-local when the standing Organizational basis still holds, while economics or another Organizationally owned business/basis premise routes to Organizational review. Project Reauthorization follows only for the resulting technically viable authorized Thinking-System basis, while a selected non-Thinking-System alternative exits after Project confirms category status.'),
('Organizational Actuators such as assessment eligibility, specific bounded research, selected path, proceed/continue/reshape/do-not-proceed and business-assumption changes','Organizational Actuators such as assessment eligibility, specific bounded research, business/basis permission, proceed/continue/reshape/do-not-proceed, exception/vendor/shared-capability decisions, and business-assumption changes'),
("without claiming the Organizational business/design decision or Delivery's implementation-level Judgment Nodes / approved Requirement and Operating Envelope","without claiming Organizational business/basis authority or Delivery's implementation-level Judgment Nodes / approved Requirement and Operating Envelope"),
('selected-path category transition','Project-selected-design category transition'),
('pre-production viability/business/design decisions','pre-production Project technical/design viability and Organizational business/basis decisions'),
('path/business/authority basis, Architectural Veto, new specific research permission, or wider Organizational change is implicated','an Organizational business/authority/investment basis or continuation decision is implicated, Architectural Veto requires a changed proposal, new specific research permission is needed, or wider Organizational change is implicated'),
]:
    s=s.replace(old,new)
# Guard the phrases that encode the rejected ownership split.
for bad in ['Organization ↔ Project viability/path/business/research authorization','Organizational business/design review','Organizational Actuators such as assessment eligibility, specific bounded research, selected path','the Organizational business/design decision','selected-path category transition','pre-production viability/business/design decisions']:
    if bad in s: raise SystemExit('obsolete phrase remains: '+bad)
p.write_text(s)
