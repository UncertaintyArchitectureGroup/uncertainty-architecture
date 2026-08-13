from pathlib import Path
p=Path('content/research/notes/open-engineering-specification-article-draft.md')
s=p.read_text()
old='The model proposes a **€450** refund for a customer case. The same event creates different questions at different horizons; the destination depends on which decision basis the evidence challenges.'
new='The model selects or proposes a **€450** refund for a customer case, and the workflow reaches the transaction-authority check. The same event creates different questions at different horizons; the destination depends on which decision basis the evidence challenges.'
if s.count(old)!=1: raise SystemExit(f'expected 1 match, found {s.count(old)}')
p.write_text(s.replace(old,new,1))
