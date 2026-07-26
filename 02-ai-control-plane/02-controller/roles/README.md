---
title: Controller Responsibility Bundles
artifact_type: control-capability
status: informative
maturity: active
module: control-plane
topics:
  - controller
  - human-authority
  - escalation
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/informative
  - ua/topic/controller
  - ua/topic/human-authority
  - ua/topic/escalation
---

# Controller Responsibility Bundles

Controller responsibilities should be assigned explicitly, but UA does not require dedicated job titles.

Useful responsibility bundles may include:

- ownership of intended outcomes and operating boundaries;
- ownership of prompts, policies, model configuration, or other behavior-affecting artifacts;
- evaluation design and calibration;
- release and change authority;
- runtime observation and incident response;
- escalation, containment, rollback, and shutdown decisions;
- auditability and preservation of decision rationale.

Small organizations may assign several bundles to one existing role or team. Larger or higher-consequence systems may separate responsibilities to reduce blind spots and conflicts of interest.

A named human-in-the-loop step is not sufficient unless the person or group has adequate context, competence, time, and authority to change the outcome.