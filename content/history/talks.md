# Talks and Presentations

This document records public evidence of talks, workshops, and practitioner sessions in which Uncertainty Architecture was a substantive topic.

It is not an event calendar, marketing log, or claim of organizational adoption. Private meetings, sales calls, unconfirmed invitations, and passing references are excluded.

## June 2026 — Ukrainian Software Architecture Community (swarchua)

Vitalii Oborskyi delivered a community-preview session for the Ukrainian software architecture community on **Uncertainty Architecture: Designing Non-Deterministic Systems**.

The session examined why LLM-backed systems require a distinct engineering methodology rather than being treated only as an extension of conventional Machine Learning Engineering. The discussion focused on the change in the object being governed: core application behavior can now remain probabilistic at runtime.

Topics included:

- business risks and acceptable-deviation boundaries as inputs to requirements;
- changes to Definition of Ready and Definition of Done for AI-enabled features;
- statistical testing and risk thresholds;
- semantic-drift monitoring, fallback paths, and kill switches;
- Human-in-the-Loop as an architectural dependency;
- changes to collaboration across architecture, QA, product, delivery, and development;
- the role of an AI Control Plane in connecting stochastic components to deterministic business flows.

A public recording was linked from the follow-up post.

**What this establishes:** UA was presented and discussed in a public software-architecture community, with a recording and public follow-up material.

**What it does not establish:** endorsement by the community as a whole, formal adoption by participating organizations, or independent validation of every UA claim.

- [Session announcement](https://www.linkedin.com/posts/vitaliioborskyi_meet-activity-7471115607023947776-czyz/)
- [Public follow-up: methodology and software-architecture framing](https://www.linkedin.com/posts/vitaliioborskyi_software-architecture-activity-7477274339411693569-dJhu/)
- [Public follow-up: repository and recording](https://www.linkedin.com/posts/vitaliioborskyi_github-uncertaintyarchitecturegroupuncertainty-architecture-activity-7477275989761384448-k8J9/)

## July 2026 — Corning Incorporated Learn-AI-Palooza

Vitalii Oborskyi joined an internal technical AI workshop for Corning Incorporated's Science & Technology team as an external speaker. The session focused on **Designing Non-Deterministic Systems** and used Uncertainty Architecture to examine how probabilistic model judgment changes software architecture, delivery assumptions, governance, and accountability.

Topics included:

- the transition from deterministic software paths to Thinking Systems (then described in the session as behavioral systems);
- the use of control theory for socio-technical feedback loops;
- separating deterministic constraints from model judgment;
- risks that emerge at the level of teams, operating models, ownership, and escalation rather than only in source code;
- the need for sensing, correction, containment, and human decision authority.

Rod Montgomery publicly described the session as one of the highlights of the event and emphasized that important risks of AI participation in execution and business logic often sit above the code layer.

**What this establishes:** UA was presented and discussed with an enterprise technology audience, and the host independently documented the relevance of the system-level framing.

**What it does not establish:** formal adoption of UA by Corning, approval by Corning leadership outside the workshop, or a public commercial engagement.

- [Source: Rod Montgomery's public post](https://www.linkedin.com/posts/roderickm_one-of-the-highlights-of-our-recent-learn-al-palooza-share-7480960627696558081-9L4z/)

## Entry criteria

A talk should be added here only when:

1. there is public evidence that the session occurred;
2. UA was a substantive topic rather than a passing reference;
3. the description distinguishes presentation from endorsement, adoption, or certification;
4. duplicate announcement and follow-up posts are grouped under one event rather than listed as separate talks.
