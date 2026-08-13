from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-draft.md')
s=p.read_text()
a=s.index('For a material case, that control perimeter may therefore become explicitly **socio-technical** and span several decision horizons:')
z=s.index('**What this adds to the case:**', a)
close=s.index('\n\n---', z)
repl='''For a material case, that control perimeter may therefore become explicitly **socio-technical** and cross technical, delivery, architectural, human-authority, and organizational decision boundaries. In the running example, a bounded-refund authority may originate outside the runtime system, depend on architectural choices about where Model Judgment is permitted, require a concrete delivery realization, and ultimately constrain whether a runtime transaction can execute. The point here is the **reach of the perimeter**, not yet the ownership model inside it.

This does **not** mean every Thinking System needs four departments, four committees, or a maximal governance stack. The same people or platform may carry several responsibilities, and lower-consequence systems may implement the map lightly. The point is causal: once probabilistic Model Judgment participates in a consequential responsibility, the required control perimeter follows the authority and effects of the **whole controlled object**, potentially all the way to organizational decision rights.

**What this adds to the case:** the same support system now exposes why consequential responsibility can require a socio-technical control perimeter that extends beyond the model and runtime component.'''
s=s[:a]+repl+s[close:]
a=s.index('Once probabilistic judgment enters the controlled object, its consequences do not remain inside a model call.')
z=s.index('Across those horizons, the concrete subject changes but a recurring control structure appears:', a)+len('Across those horizons, the concrete subject changes but a recurring control structure appears:')
repl='''The example exposes a broader consequence: the control perimeter of a Thinking System may cross technical, delivery, architectural, human-authority, and organizational decision boundaries. Different decisions across that perimeter require different evidence, authority, and corrective mechanisms. Before assigning those decisions to explicit horizons, however, the engineering problem is more basic: **what capabilities must exist for bounded control to be possible at all?**

Across that expanded perimeter, the concrete subject changes but a recurring control structure appears:'''
s=s[:a]+repl+s[z:]
s=s.replace('The next section asks what capabilities are required to make that expanded control perimeter operational. The later decision-horizon section then asks where the consequential decisions around it are legitimately owned.', 'The next section therefore asks what capabilities are required to make that expanded control perimeter operational. Only after establishing those control functions does the paper assign consequential decisions to explicit decision horizons.')
p.write_text(s)
p=Path('content/research/notes/open-engineering-specification-article-blueprint.md')
s=p.read_text()
s=s.replace('Introduce those horizon names only as **foreshadowing of perimeter reach**: do not define their ownership model, detailed responsibilities, or reassessment semantics here, and do not present them as mandatory departments or stages. Reserve the canonical four-horizon operating model for Section 5.4.', 'Show the **reach of the perimeter without introducing the canonical horizon sequence**: it may cross technical, delivery, architectural, human-authority, and organizational decision boundaries. Do not define horizon ownership, detailed responsibilities, or reassessment semantics here. Reserve the canonical four-horizon model and its names as an operating structure for Section 5.4.')
s=s.replace('Section 5.2 uses those names only to foreshadow how far the perimeter may reach; detailed ownership, downward inheritance, and reassessment routing belong to Section 5.4.', 'Section 5.2 shows only how far the perimeter may reach across decision boundaries; the canonical horizon sequence, detailed ownership, downward inheritance, and reassessment routing belong to Section 5.4.')
p.write_text(s)
# trigger after runner is registered
