from pathlib import Path
import re

p = Path('content/research/notes/open-engineering-specification-article-draft.md')
s = p.read_text()

# 1. Make the early Section 2 return generic so the primary case return stays inside the callout.
pattern = re.compile(
    r"Return to the running support-resolution example\. Its workflow may be fixed end to end:.*?The category begins when a \*\*Consequential Runtime Responsibility\*\* first depends partly on probabilistic Model Judgment\.",
    re.S,
)
replacement = (
    "A workflow may be fixed end to end and still contain the changed controlled object. "
    "Nothing about a predefined sequence of retrieval, interpretation, decision support, communication, authority checking, and bounded execution requires dynamic orchestration. "
    "Yet if interpretation, selection, consequential communication, or another **Consequential Runtime Responsibility** depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. "
    "Later additions such as memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. "
    "The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment."
)
s, n = pattern.subn(replacement, s, count=1)
assert n == 1, f'early case return replacements={n}'

# 2. Let realization evidence originate at Delivery as well as operation evidence at Runtime.
pattern = re.compile(
    r"(\s+D -->\|realized boundary \+ release scope\| R\n)\s+R --> E\n(\s+E -\.->\|implementation / realization / evidence issue\| D)"
)
def repl(m):
    indent = re.match(r"\s*", m.group(1)).group(0)
    return (
        m.group(1)
        + indent + "D -.->|realization evidence| E\n"
        + indent + "R -->|operation evidence| E\n"
        + m.group(2)
    )
s, n = pattern.subn(repl, s, count=2)
assert n == 2, f'evidence topology replacements={n}'

# 3. Keep model A -> model B -> A×B contiguous; move proportionality after the combined figure.
start = s.index('### The full map is a reasoning reference, not a maximum-process mandate')
end = s.index('### Two orthogonal models', start)
block = s[start:end]
s = s[:start] + s[end:]
anchor = re.search(r"\*\*Figure 9 — Two orthogonal models\.\*\*.*?All four capability families may appear at every horizon\.\n", s, re.S)
assert anchor, 'combined figure caption not found'
pos = anchor.end()
s = s[:pos] + '\n' + block + s[pos:]

# 4. Restore unique sequential numbering for the final learning-loop figure.
old = '**Figure 14 — Cross-level learning and stabilization loop.**'
assert s.count(old) == 1, f'learning-loop Figure 14 count={s.count(old)}'
s = s.replace(old, '**Figure 15 — Cross-level learning and stabilization loop.**', 1)

p.write_text(s)
