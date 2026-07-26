---
title: Metrics with Skepticism
artifact_type: control-capability
status: informative
maturity: active
module: control-plane
topics:
  - evidence
  - evaluation
  - sensors
  - control-economics
tags:
  - ua/module/control-plane
  - ua/type/control-capability
  - ua/status/informative
  - ua/topic/evidence
  - ua/topic/evaluation
  - ua/topic/control-economics
---

# Metrics with Skepticism

Metrics are evidence instruments, not truth machines.

Useful metric design should make explicit:

- the decision the metric supports;
- the behavior or outcome being approximated;
- coverage, sampling, uncertainty, and latency;
- incentives and opportunities for gaming;
- distributional differences hidden by aggregates;
- calibration and review requirements;
- the action that may follow a material change.

A metric can create false confidence when its number is precise but its relationship to business intent is weak. UA therefore treats metrics as one sensor type within a larger evidence and control system.