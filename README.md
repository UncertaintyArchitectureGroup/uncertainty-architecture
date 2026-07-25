# Uncertainty Architecture (UA)

## Engineering at the AI–Code Boundary

**Uncertainty Architecture** is an open doctrine and pattern language for building and operating software in which part of the system's behavior is delegated to **non-deterministic model judgment**, while the surrounding system remains **deterministic, inspectable, and governable**.

UA is not about eliminating uncertainty or pretending that AI can be made fully deterministic. It is about **containing uncertainty**: deciding where determinism must hold, where judgment is unavoidable, and how the boundary between the two is engineered, observed, and corrected over time.

The project is designed primarily for small and medium-sized engineering organizations that need practical control without building a large governance bureaucracy.

## Start Here

Choose the path that matches what you need:

- **Understand the core concepts:** [`00-doctrine/`](00-doctrine/)
- **Apply reusable engineering patterns:** [`01-patterns/`](01-patterns/)
- **Design the control loop:** [`02-ai-control-plane/`](02-ai-control-plane/)
- **Review concrete architectures:** [`03-reference-architectures/`](03-reference-architectures/)
- **Study recurring failure modes:** [`04-failure-modes/`](04-failure-modes/)
- **Trace the research behind the specification:** [`content/research/`](content/research/)
- **Follow project history, talks, discussions, and external references:** [`content/history/`](content/history/)
- **See what is being built next:** [`ROADMAP.md`](ROADMAP.md)

## The Core Shift

Traditional software is mostly built from deterministic components and predefined execution paths. LLM-backed and agentic systems introduce components whose behavior remains probabilistic at runtime.

UA calls this broader class **Behavioral Software**:

- **Linear Software** follows explicitly coded paths.
- **Behavioral Software** pursues goals within constraints while selecting or generating parts of the path dynamically.

The architectural problem is therefore not only model quality. It is how probabilistic judgment is connected to business rules, permissions, data, human authority, release processes, monitoring, and correction.

## What UA Is — and Is Not

UA is:

- a shared way of thinking about systems at the AI–code boundary;
- a set of patterns for containment, evaluation, escalation, and fallback;
- an operational doctrine for governing probabilistic behavior;
- a tool-neutral specification intended to evolve through research and implementation evidence.

UA is not:

- an SDK or universal agent framework;
- a prompt-template collection;
- a single metric or evaluation method;
- a compliance certification;
- a claim that uncertainty can be removed from model behavior.

## Core Model

UA treats AI governance as an engineering control problem.

> **Reliable AI = Actuators + Sensors + Controller**

- **Actuators** shape and constrain behavior: prompts, schemas, policies, permissions, tools, model settings, and execution boundaries.
- **Sensors** detect deviation: evaluations, golden scenarios, runtime signals, incidents, qualitative review, and drift monitoring.
- **Controller** determines corrective action: release gates, ownership, escalation, rollback, retraining, prompt or policy changes, and human decision authority.

This control loop surrounds a critical distinction:

- **Deterministic Core** — business rules, invariants, authentication, data handling, auditability, safety constraints.
- **Model Judgment** — interpretation, synthesis, classification under ambiguity, open-ended generation, and uncertain tool choice.

UA focuses on the boundary between these regions.

## Conceptual Architecture

```mermaid
graph TD;
    A[Deterministic Core / Business Logic] -->|Request + Constraints| B[Boundary Layer / AI Control Plane];
    B -->|Bounded Invocation| C{Model Judgment / LLM};
    C -->|Candidate Output| B;
    B -->|Validate + Gate| D[Quality, Safety, and Policy Checks];
    D -->|Pass| E[User / Downstream System];
    D -->|Fail| F[Fallback / Retry / Escalation];
    F --> B;
```

## Repository Map

### Normative framework

- [`00-doctrine/`](00-doctrine/) — core concepts, terminology, and boundary thinking.
- [`01-patterns/`](01-patterns/) — reusable containment and interface patterns.
- [`02-ai-control-plane/`](02-ai-control-plane/) — actuators, sensors, controllers, and operating controls.
- [`03-reference-architectures/`](03-reference-architectures/) — worked architectural applications.
- [`04-failure-modes/`](04-failure-modes/) — recurring technical and socio-technical failure modes.

### Supporting records

- [`content/research/`](content/research/) — publications, analysis, provenance, and research-to-framework traceability. Research remains non-normative until deliberately adopted.
- [`content/history/`](content/history/) — project timeline, talks, public stress tests, and independent references.
- [`ROADMAP.md`](ROADMAP.md) — canonical direction and future priorities.
- [`CHANGELOG.md`](CHANGELOG.md) — repository and specification-artifact changes only.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — contribution and review workflow.

### Operational assets

- [`assets/`](assets/) — diagrams and visual references.
- [`scripts/`](scripts/) — repository-maintenance automation.
- [`templates/`](templates/) — reusable contribution and specification templates.

## Current Status

**Active specification development.**

The current priority is to consolidate the research corpus into a coherent framework spine, clarify normative boundaries, and derive a practical SMB-facing artifact for mapping risks, required controls, and control cost.

Detailed status and sequencing are maintained in [`ROADMAP.md`](ROADMAP.md).

## Evidence and Project History

UA keeps different kinds of evidence separate:

- research explains where ideas and claims originated;
- public discussions record critique, alternatives, and stress tests;
- independent references record how third parties interpreted or used the concepts;
- the changelog records changes to repository artifacts.

This prevents visibility, attention, recommendations, or invited talks from being mistaken for technical validation or formal adoption.

See [`content/history/`](content/history/) for the evidence policy and historical records.

## Community and Contributions

GitHub is the canonical home for doctrine and specification changes. Community discussion and early design review may happen elsewhere, but accepted changes must be represented in the repository.

Useful contributions include operational failure reports, pattern proposals, critiques of terminology or control assumptions, examples of escalation and evaluation design, and provenance corrections.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Authors and Maintainers

### Vitalii Oborskyi — Creator and Lead Architect

Focus: operational framing, governance, delivery systems, adoption scaffolding, and system-level control.

- [LinkedIn](https://www.linkedin.com/in/vitaliioborskyi/)
- [GitHub](https://github.com/oborskyivitalii)

### Sam “stunspot” Walker — Technical Co-Author

Focus: AI–code boundary placement, containment patterns, prompt-as-medium realism, and real-world failure modes.

Additional contributors and reviewers are credited as the work matures.

## Advisors

### Markus Kopko — Strategic Advisor on Governance and Alignment

Focus: project-management standards, organizational alignment, and the operationalization of AI governance.

- [LinkedIn](https://www.linkedin.com/in/markuskleinpmp/)

### Otman Basir, Ph.D. — Academic Advisor

Professor of Intelligent Systems at the University of Waterloo and author of the Social Responsibility Stack. His role supports the connection between control-theoretic research and practical engineering governance.

- [LinkedIn](https://www.linkedin.com/in/otman-basir-ba1258178)

Advisory relationships are listed because they are part of the project's operating context. They do not imply institutional endorsement, certification, or formal adoption of UA.

See [`content/history/external-recognition.md`](content/history/external-recognition.md) for supporting public evidence and precise claim boundaries.

## How to Cite

```bibtex
@misc{oborskyi_walker2025uncertainty,
  author = {Oborskyi, Vitalii and Walker, Sam},
  title = {Uncertainty Architecture: An Operational Model for AI Governance},
  year = {2025},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/UncertaintyArchitectureGroup/uncertainty-architecture}}
}
```

## Licensing

This repository uses a dual-license model:

- documentation and specifications: CC BY 4.0;
- code and reference implementations: Apache 2.0.

See [`LICENSING.md`](LICENSING.md) for details.