from pathlib import Path

p = Path('content/research/notes/open-engineering-specification-article-draft.md')
s = p.read_text()

# 1. Section 2: keep the early discussion generic; the primary return to the support case belongs in the callout.
start = s.index('Return to the running support-resolution example.')
end = s.index('\n\nThe distinction matters because engineering needs a stable name', start)
replacement = (
    'A workflow may be fixed end to end and still contain the changed controlled object. '
    'Nothing about a predefined sequence of retrieval, interpretation, decision support, communication, authority checking, and bounded execution requires dynamic orchestration. '
    'Yet if interpretation, selection, consequential communication, or another **Consequential Runtime Responsibility** depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. '
    'Later additions such as memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. '
    'The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment.'
)
s = s[:start] + replacement + s[end:]

# 2. Section 4 figures: realization evidence may originate at Delivery, operation evidence at Runtime.
sec4 = s.index('## 4. Four Decision Levels for Thinking Systems')
runex = s.index('### Running Example | One Refund Case Across Four Decision Horizons', sec4)
head, body, tail = s[:sec4], s[sec4:runex], s[runex:]
body = body.replace('R --> E', 'D -.->|realization evidence| E\n    R -->|operation evidence| E')
body = body.replace('  R --> E', '  D -.->|realization evidence| E\n  R -->|operation evidence| E')
s = head + body + tail

# 3. Keep model A -> model B -> A×B contiguous; proportionality comes after the combined model.
start = s.index('### The full map is a reasoning reference, not a maximum-process mandate', sec4)
end = s.index('### Two orthogonal models', start)
block = s[start:end]
s = s[:start] + s[end:]
caption = '**Figure 9 — Two orthogonal models.**'
cap_start = s.index(caption, sec4)
cap_end = s.index('\n\n', cap_start) + 2
s = s[:cap_end] + block + s[cap_end:]

# 4. Restore unique final figure number.
s = s.replace('**Figure 14 — Cross-level learning and stabilization loop.**', '**Figure 15 — Cross-level learning and stabilization loop.**', 1)

p.write_text(s)
