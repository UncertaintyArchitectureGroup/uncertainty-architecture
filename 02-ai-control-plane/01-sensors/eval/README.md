---
title: Evaluation and Drift Analysis
artifact_type: control-capability
status: informative
maturity: active
module: control-plane
topics:
  - evaluation
  - evidence
  - drift
  - sensors
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/informative
  - ua/topic/evaluation
  - ua/topic/evidence
  - ua/topic/drift
---

# Evaluation and Drift Analysis

This area covers approaches for producing evidence about failure, degradation, regression, and changed operating conditions.

Relevant concerns include:

- the decision an evaluation is intended to support;
- representative scenarios and boundary cases;
- deterministic, statistical, model-assisted, and human evidence;
- calibration, uncertainty, coverage, and blind spots;
- semantic, logical, operational, and outcome drift;
- feedback latency and reassessment triggers;
- traceability from evidence to controller action.

Evaluation is a sensor capability. It does not become governance or control until evidence is connected to decision authority and a mechanism capable of changing, containing, or stopping behavior.