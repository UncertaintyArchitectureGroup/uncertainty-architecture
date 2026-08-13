from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-draft.md')
s=p.read_text()

# Clarify that the shared evidence node contains evidence that challenges a decision basis,
# not all delivery/runtime telemetry.
s=s.replace(
    'E["Realization / operation evidence<br/>behavior · outcomes · control state · changed assumptions"]',
    'E["Reassessment evidence<br/>realization or operation evidence that challenges a decision basis"]'
)

# Section 3 establishes that legitimate authority must be connected; Section 4 allocates it.
s=s.replace(
    'Until material boundaries are credibly realized, required evidence reaches legitimate decision authority, effective Actuators exist, Human Authority and fallback are viable where needed, and invalidated assumptions can trigger reassessment, the system may be demonstrable or testable but is not ready for production at the intended scope.',
    'Until material boundaries are credibly realized, required evidence can reach and inform legitimate decision authority, effective Actuators exist, Human Authority and fallback are viable where needed, and invalidated assumptions can trigger reassessment, the system may be demonstrable or testable but is not ready for production at the intended scope.'
)

# Normalize Mermaid source indentation for the standalone and combined horizon models.
s=s.replace('    D -.->|realization evidence| E\n  R -->|operation evidence| E', '    D -.->|realization evidence| E\n    R -->|operation evidence| E')
s=s.replace('  D -.->|realization evidence| E\n    R -->|operation evidence| E', '  D -.->|realization evidence| E\n  R -->|operation evidence| E')

# Keep captions aligned with the narrower evidence-node meaning.
s=s.replace(
    'Evidence from realization or operation returns directly to the horizon whose decision basis it invalidates; reassessment is therefore not a mandatory upward sequence and need not originate only at Runtime.',
    'Realization or operation evidence that challenges a standing decision basis becomes reassessment evidence and returns directly to the horizon that owns that basis; reassessment is therefore not a mandatory upward sequence and need not originate only at Runtime.'
)
s=s.replace(
    'realization or operation evidence returns directly to the horizon whose decision basis it invalidates.',
    'reassessment evidence from realization or operation returns directly to the horizon whose decision basis it invalidates.'
)

p.write_text(s)
