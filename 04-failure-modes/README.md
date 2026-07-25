# Failure Modes and Anti-Patterns

**Status:** Draft normative taxonomy; examples are informative  
**Role:** Recurring mechanisms through which control is lost in Thinking Systems

## Purpose

This module documents recurring ways in which systems containing model-mediated judgment lose structural, semantic, operational, or organizational control.

Traditional software failures often arise from explicit logical defects. Thinking Systems also fail through probabilistic drift, boundary breaches, weak evidence, delayed feedback, unclear authority, and controls that exist on paper but cannot change runtime behavior.

## Defines

This module defines or develops a taxonomy of:

- structural and syntactic failures;
- semantic and outcome failures;
- runtime and feedback-loop failures;
- architectural boundary failures;
- governance and decision-authority failures;
- anti-patterns that treat probabilistic behavior as deterministic code.

## Does not define

This module does not provide:

- an exhaustive catalogue of every possible incident;
- one universal severity model;
- a guarantee that a single control eliminates a failure mode;
- mandatory implementation technology;
- post-mortems as normative requirements.

Individual examples are illustrative. Mitigation normally requires a combination of boundaries, actuators, sensors, controller decisions, and operating procedures proportional to the system's consequences and context.

## Key concepts

- syntactic entropy;
- semantic entropy;
- probabilistic drift;
- boundary breach;
- open-loop deployment;
- evidence failure;
- controller or authority failure;
- containment and recovery failure.

## Relationships

- [`00-doctrine/`](../00-doctrine/) provides the distinctions needed to explain why these failures occur.
- [`01-patterns/`](../01-patterns/) contains reusable responses to recurring failure mechanisms.
- [`02-ai-control-plane/`](../02-ai-control-plane/) provides the capabilities used to detect, interpret, and correct deviations.
- [`03-reference-architectures/`](../03-reference-architectures/) demonstrates how failure handling may be composed in concrete systems.
- [`SPECIFICATION.md`](../SPECIFICATION.md) defines the status and normative boundary of this taxonomy.

## Initial taxonomy

### 1. Syntactic entropy — the structure breaks

The model output violates a technical contract required by the surrounding system.

Illustrative examples:

- malformed structured output;
- incorrect field or value types;
- repetition or non-terminating behavior;
- context overflow or truncation;
- outputs that cannot be parsed, validated, or safely executed.

Typical controls include strict schemas, validation, bounded retries, deterministic parsing, execution limits, and explicit fallback paths.

### 2. Semantic entropy — the meaning breaks

The output is technically valid but functionally wrong, unsafe, misleading, or unsuitable for the operating context.

Illustrative examples:

- unsupported or false claims;
- tone or policy drift;
- unjustified refusal or over-restriction;
- ignored instructions or negative constraints;
- valid-looking actions that violate business intent.

Typical controls include evaluations, golden scenarios, runtime outcome signals, policy checks, human review, escalation, and controller-authorized changes.

### 3. Process and governance anti-patterns — the control system breaks

The organization treats probabilistic behavior as if ordinary development and release practices were sufficient.

Illustrative examples:

- **Vibe-check release:** deployment based on a few favorable examples rather than risk-derived evidence;
- **Hidden behavior configuration:** prompts, policies, or model settings embedded without ownership or traceability;
- **Open-loop deployment:** operation without meaningful feedback or a mechanism for corrective action;
- **Perfect-prompt fallacy:** attempting to eliminate uncertainty through prompting instead of engineering containment and recovery;
- **Telemetry without authority:** collecting metrics without assigning who may intervene or change the system;
- **Human-in-the-loop theatre:** nominal approval steps without adequate context, time, competence, or real decision power.

## Contribution

Operational failure reports and post-mortems are valuable inputs to this module. Contributions should distinguish observed evidence from interpretation, identify operating context and consequences, and avoid presenting a single incident as a universal rule.
