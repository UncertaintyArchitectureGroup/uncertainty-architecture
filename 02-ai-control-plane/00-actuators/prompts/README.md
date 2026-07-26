---
title: Prompt Interfaces
artifact_type: control-capability
status: informative
maturity: active
module: control-plane
topics:
  - actuators
  - constraints
  - model-judgment
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/informative
  - ua/topic/actuators
  - ua/topic/constraints
---

# Prompt Interfaces

Prompt artifacts are one possible actuator surface for shaping Model Judgment. They should be treated as versioned, reviewable behavior-affecting configuration rather than as magic spells or guaranteed business rules.

Relevant concerns include:

- instruction and system prompts;
- context framing and examples;
- persona or judgment scaffolding;
- prompt ownership and versioning;
- boundaries between prompt-level influence and deterministic enforcement;
- traceability from a prompt change to evaluation and release evidence.

A prompt may influence behavior, but it does not by itself create a hard invariant, complete containment, or a functioning control loop.