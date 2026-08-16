from pathlib import Path
p = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s = p.read_text()
old = '- [ ] **Article §8** explicitly requests evidence on initial assessment versus specific bounded-research authorization, pre-production Project technical/design viability and Organizational business/basis decisions, research-only versus production-capable Project Authorization, Project-selected-design category transition, exogenous Organizational change routing, Architectural Veto versus economic non-viability, active behavioral/control baseline reconstruction, fallback/common-mode/capacity/restoration behavior, and evaluator/Golden Set/rubric/threshold/human-review-signal validity loss, versioning, calibration/validation, incident ingestion, recalibration, replacement, and changed decision use.'
new = '- [ ] **Article §8** explicitly requests evidence on initial assessment versus specific bounded-research authorization, pre-production Project technical/design viability and Organizational business/basis decisions, research-only versus production-capable Project Authorization, whether changed production scope remains covered by the applicable existing Organizational Business Authorization or requires renewed/reshaped Organizational authorization, Project-selected-design category transition, exogenous Organizational change routing, Architectural Veto versus economic non-viability, active behavioral/control baseline reconstruction, fallback/common-mode/capacity/restoration behavior, and evaluator/Golden Set/rubric/threshold/human-review-signal validity loss, versioning, calibration/validation, incident ingestion, recalibration, replacement, and changed decision use.'
if s.count(old) != 1:
    raise SystemExit(f'expected 1 acceptance evidence line, found {s.count(old)}')
s = s.replace(old, new)
if old in s or new not in s:
    raise SystemExit('acceptance evidence guard failed')
p.write_text(s)
