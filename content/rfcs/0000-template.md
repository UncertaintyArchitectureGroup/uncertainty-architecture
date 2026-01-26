---
rfc_id: 0000 # Leave empty when submitting
title: [Short Descriptive Title]
authors: [Your Name]
status: Draft # Options: Draft, Internal Review, Advisor Review, Public Review, Active, Rejected, Deprecated
scope: Pattern # Options: Doctrine, Pattern, Operating Model, Meta
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# RFC: [Title]

## Summary
A brief explanation of the proposal. It should be understandable by someone familiar with Uncertainty Architecture but not necessarily an expert in this specific pattern.

## Motivation
Why are we doing this?
*   What problem in AI Governance or Engineering does this solve?
*   Why is the current solution (or lack thereof) insufficient?
*   How does this align with the "Containment, Not Certainty" principle?

## Detailed Design
This is the core of the RFC. Explain the design in detail:
*   **Architecture:** How does this fit into the Control Plane layers (Actuator, Sensor, Controller)?
*   **Interface:** Define any new JSON schemas, prompt structures, or API signatures.
*   **Behavior:** How does the system react to uncertainty here?
*   **Failure Modes:** How does this pattern fail safely?

## Reference Implementation (Optional)
Link to a prototype, pseudo-code, or a specific implementation branch demonstrating the concept.

## Drawbacks
Why should we *not* do this?
*   Does it add necessary complexity?
*   Does it impact latency or cost significantly?

## Alternatives
What other designs have been considered? Why were they rejected?

## Unresolved Questions
What parts of the design are still up for debate?

---

## Governance Log (Internal Use)
*Track approvals before Public Release.*

*   [ ] **Internal Review:** (Vitalii / Sam) - *Date*
*   [ ] **Advisor Review:** (Markus / Otman) - *Date / N/A*
*   [ ] **Ready for Public:** *Date*
