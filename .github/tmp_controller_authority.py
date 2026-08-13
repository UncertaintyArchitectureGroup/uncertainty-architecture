from pathlib import Path

mpath = Path('content/research/notes/open-engineering-specification-article-draft.md')
bpath = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
m = mpath.read_text()
b = bpath.read_text()

old = """**Controller / decision authority**
- for a given refund attempt, determine whether execution is authorized or must route to Human Authority;
- for accumulated evidence, decide within delegated authority whether runtime operation should be narrowed or disabled, or whether the evidence must be escalated for reassessment at the horizon that owns the challenged decision basis."""
new = """**Controller**
- for a given refund attempt, interpret the relevant evidence against the applicable Constraint and determine the authorized response within its delegated decision boundary;
- where substantive judgment is reserved to Human Authority, route the case and evidence to that authority rather than treating the Controller as the source of the authority itself;
- for accumulated evidence, narrow or disable runtime operation only within delegated authority, or route the evidence for reassessment to the horizon that owns the challenged decision basis."""
assert m.count(old) == 1, m.count(old)
m = m.replace(old, new)

old = "If the €450 transaction is deterministically blocked and the case is routed correctly, the Hard transaction boundary worked; the event is Runtime evidence and no higher-level reassessment is implied."
new = "If the €450 transaction is deterministically blocked and the case is routed correctly, the deterministic transaction guard preserved the authorized boundary; the event is Runtime evidence and no higher-level reassessment is implied."
assert m.count(old) == 1, m.count(old)
m = m.replace(old, new)

old = "- **Section 5.3** — take one stable refund-authority boundary and expose the four capability families as parallel control functions around that boundary: Constraint + Constraint Realization, Sensors, Controller / Human Authority, and Actuators. Show why a policy sentence is not yet a complete control path without implying an execution pipeline."
new = "- **Section 5.3** — take one stable refund-authority boundary and expose the four capability families as parallel control functions around that boundary: Constraint + Constraint Realization, Sensors, Controller functions operating within delegated decision authority, and Actuators. Where substantive judgment is reserved, show Human Authority as the holder of that authority or escalation destination rather than as a synonym for the Controller capability. Show why a policy sentence is not yet a complete control path without implying an execution pipeline."
assert b.count(old) == 1, b.count(old)
b = b.replace(old, new)

mpath.write_text(m)
bpath.write_text(b)
