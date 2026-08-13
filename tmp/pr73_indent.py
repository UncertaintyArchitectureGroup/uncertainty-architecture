from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-draft.md')
s=p.read_text()
s=s.replace('  D -.->|realization evidence| E\n    R -->|operation evidence| E','  D -.->|realization evidence| E\n  R -->|operation evidence| E',1)
p.write_text(s)
