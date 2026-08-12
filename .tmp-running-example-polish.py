from pathlib import Path

manuscript = Path('content/research/notes/open-engineering-specification-article-draft.md')
text = manuscript.read_text()

old = '''Consider a fictional customer-support team trying to reduce resolution cost and latency. It has a capable model, retrieval and tool access, traces, evaluation suites, policy guidance, a human-review path, and a pilot that interprets requests and proposes resolutions. Each local component can be competent. The dashboard may be green. The demo may be impressive. The complete system may still lack a defensible connection between what the organization permits, what the project authorizes, what the delivery team has realized, what runtime evidence means, and what action follows when assumptions fail. We will return to this support-resolution system as the argument develops. For now, the important fact is only that consequential interpretation and resolution may depend partly on Model Judgment while the surrounding controls and decision rights are not yet connected.
'''
new = '''### Running Example — Bounded Customer-Support Resolution

Throughout this paper, one fictional system will make the control model concrete: a company wants to reduce the cost and latency of customer-support resolution without surrendering the authority, evidence, and corrective paths required for consequential decisions.

The proposed system receives a customer request, retrieves authorized account, order, product, and support-policy context, interprets the issue, selects or recommends a resolution path, and drafts consequential customer communication. In explicitly authorized low-impact cases it may eventually be allowed to invoke a tool that changes downstream business state, such as issuing a bounded credit or refund; cases requiring reserved judgment or authority remain under Human Authority.

The controlled object in this example is not the model or chatbot interface. It is the whole support-resolution system: deterministic identity, access, retrieval, policy, tool, and execution paths; one or more Model-Judgment-dependent responsibilities; Human Authority where required; and the evidence and corrective paths around them. The same controlled object will be carried through the rest of the paper—from category classification and AI-necessity questions through organizational authorization, Project / Architecture viability, Delivery realization, Runtime operation, and reassessment. Details will be introduced only when the corresponding concept requires them.

At this point, assume only a credible pilot: a capable model, retrieval and tool access, traces, evaluation suites, policy guidance, and a human-review path. Each local component can be competent. The dashboard may be green. The demo may be impressive. The complete system may still lack a defensible connection between what the organization permits, what the project authorizes, what the delivery team has realized, what runtime evidence means, and what action follows when assumptions fail. For now, the important fact is only that consequential interpretation and resolution may depend partly on Model Judgment while the surrounding controls and decision rights are not yet connected.
'''
assert old in text, 'Section 1 running example block not found'
text = text.replace(old, new, 1)

old2 = '''Consider a fixed project-planning workflow that interprets a brief, generates requirements, constructs a plan, identifies risks, and drafts work items. The sequence may be predefined end to end. Yet if one of those consequential responsibilities depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. Later additions such as tools, memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment.
'''
new2 = '''Return to the running support-resolution example. Its workflow may be fixed end to end: receive the request, retrieve authorized context, interpret the issue, select or recommend a resolution, prepare customer communication, check authority, and either execute a bounded action or route the case to Human Authority. Nothing in that sequence requires dynamic orchestration. Yet if interpretation, resolution selection, consequential communication, or another **Consequential Runtime Responsibility** depends partly on Model Judgment, the mapping from situation to consequential behavior is no longer fully authored before runtime. Later additions such as memory, dynamic routing, cooperating agents, or broader autonomy may increase complexity and control demand, but they do not create the category. The category begins when a **Consequential Runtime Responsibility** first depends partly on probabilistic Model Judgment.
'''
assert old2 in text, 'Section 2 fixed workflow block not found'
text = text.replace(old2, new2, 1)
text = text.replace('The fictional support-resolution system introduced in Section 1 already contains this mixed structure.', 'The running support-resolution example already contains this mixed structure.', 1)
manuscript.write_text(text)

blueprint = Path('content/research/notes/open-engineering-specification-article-blueprint.md')
b = blueprint.read_text()
anchor = '''The example must remain stable enough that the reader can recognize the **same controlled object** as it moves from business proposal through organizational authorization, Project / Architecture viability, Delivery realization, Runtime operation, and reassessment. Do not replace it with unrelated examples at each level. Short counterexamples from other domains may be used to prevent overfitting, but they must remain secondary.
'''
addition = anchor + '''\n**Progressive-disclosure rule.** Introduce the running example explicitly in Section 5.1 as a named pedagogical spine and define the business goal and whole controlled object there, but reveal implementation detail only when the corresponding concept is introduced. For each major conceptual section, prefer the sequence `generic model → application to the same running example → optional secondary counterexample or transfer check`. Do not let a new domain example silently replace the support-resolution system as the primary explanatory object.\n'''
assert anchor in b, 'Blueprint running-example anchor not found'
b = b.replace(anchor, addition, 1)
marker = '- Use the customer-support running example to show the mixed deterministic / Model-Judgment structure, but defer refund thresholds, Hard/Soft realization details, and full control-loop mechanics to later sections.\n'
replacement = marker + '- Use the same support-resolution system, rather than a separate project-planning scenario, to demonstrate that a fixed predefined workflow can already cross the Thinking-System category boundary.\n'
assert marker in b, 'Section 2 accepted decision marker not found'
b = b.replace(marker, replacement, 1)
blueprint.write_text(b)
