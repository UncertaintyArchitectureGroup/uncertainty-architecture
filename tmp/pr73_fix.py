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

# 2. Section 4 figures: Delivery realization evidence and Runtime operation evidence are distinct evidence origins.
sec4 = s.index('## 4. Four Decision Levels for Thinking Systems')
runex = s.index('### Running Example | One Refund Case Across Four Decision Horizons', sec4)
head = s[:sec4]
body = s[sec4:runex]
tail = s[runex:]
body = body.replace(
    '    D -->|realized boundary + release scope| R\n    R --> E\n',
    '    D -->|realized boundary + release scope| R\n    D -.->|realization evidence| E\n    R -->|operation evidence| E\n',
    2,
)
assert body.count('D -.->|realization evidence| E') >= 2
s = head + body + tail

# 3. Put the combined A×B model immediately after the standalone decision model; proportionality comes after composition.
start = s.index('### The full map is a reasoning reference, not a maximum-process mandate', sec4)
end = s.index('### Two orthogonal models', start)
block = s[start:end]
s = s[:start] + s[end:]
caption = '**Figure 9 — Two orthogonal models.**'
cap_start = s.index(caption, sec4)
cap_end = s.index('\n\n', cap_start) + 2
s = s[:cap_end] + block + s[cap_end:]

# 4. Unique final figure number.
s = s.replace(
    '**Figure 14 — Cross-level learning and stabilization loop.**',
    '**Figure 15 — Cross-level learning and stabilization loop.**',
    1,
)

p.write_text(s)
