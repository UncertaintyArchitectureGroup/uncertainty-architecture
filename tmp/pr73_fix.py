from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-draft.md')
s=p.read_text()

old="""Return to the running support-resolution example. Its workflow may be fixed end to end: receive the request, retrieve authorized context, interpret the issue, select or recommend a resolution, prepare customer communication, check authority, and either execute a bounded action or route the case to Human Authority. Nothing in that sequence requires dynamic orchestration. Yet if interpretation, resolution selection, consequential communication, or another **Consequential Runtime Responsibility** depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. Later additions such as memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment."""
new="""A workflow may be fixed end to end and still contain the changed controlled object. Nothing about a predefined sequence of retrieval, interpretation, decision support, communication, authority checking, and bounded execution requires dynamic orchestration. Yet if interpretation, selection, consequential communication, or another **Consequential Runtime Responsibility** depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. Later additions such as memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment."""
assert old in s
s=s.replace(old,new,1)

old="""    D -->|realized boundary + release scope| R
    R --> E
    E -.->|implementation / realization / evidence issue| D"""
new="""    D -->|realized boundary + release scope| R
    D -.->|realization evidence| E
    R -->|operation evidence| E
    E -.->|implementation / realization / evidence issue| D"""
assert s.count(old) >= 2
s=s.replace(old,new,2)

start=s.index('### The full map is a reasoning reference, not a maximum-process mandate')
end=s.index('### Two orthogonal models', start)
block=s[start:end]
s=s[:start]+s[end:]
anchor="""**Figure 9 — Two orthogonal models.** The left side reuses the four-horizon model introduced earlier: authority and Constraints become more concrete downward; realization or operation evidence returns directly to the horizon whose decision basis it invalidates. The green side is the orthogonal capability anatomy. Its ordering is a reading aid, not a pipeline. All four capability families may appear at every horizon.
"""
assert anchor in s
s=s.replace(anchor,anchor+'\n'+block,1)

assert s.count('**Figure 14 — Cross-level learning and stabilization loop.**') == 1
s=s.replace('**Figure 14 — Cross-level learning and stabilization loop.**','**Figure 15 — Cross-level learning and stabilization loop.**',1)

p.write_text(s)
