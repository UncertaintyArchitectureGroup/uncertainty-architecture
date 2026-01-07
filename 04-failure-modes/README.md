# Failure Modes & Anti-Patterns

> **Objective:** Taxonomy of Entropy
> **Motto:** "We learn from the crash, not the flight."

This directory documents the specific ways AI-integrated systems fail. Unlike traditional software bugs (which are logical errors), AI failures are often **probabilistic drifts** or **boundary breaches**.

We categorize failures into three distinct domains:

## 1. Syntactic Entropy (The Structure Breaks)
Failures where the model output violates the technical contract required by the host system.
*   **Malformed JSON:** The model returns text or Markdown instead of a structured object.
*   **Type Hallucination:** Returning a string where an integer was expected.
*   **Infinite Loops:** The model gets stuck in a repetition cycle.
*   **Context Overflow:** Input exceeds the model's window, causing truncation.

> *Mitigation:* Solved by **Actuators** (Strict Schemas, Pydantic, Retry Logic).

## 2. Semantic Entropy (The Meaning Breaks)
Failures where the output is technically valid (passes JSON validation) but functionally wrong, dangerous, or useless.
*   **Hallucination:** Confidently stating false facts.
*   **Tone Drift:** A support bot becoming aggressive, overly casual, or robotic.
*   **Refusal/Over-safety:** The model refuses a valid business request due to generic safety filters.
*   **Instruction Ignoring:** The model ignores negative constraints ("Do not mention X").

> *Mitigation:* Solved by **Sensors** (Evals, Golden Sets) and **Controller** (Human Review).

## 3. Process Anti-Patterns (The Governance Breaks)
Failures caused by treating probabilistic components as deterministic code.
*   **The "Vibe Check" Release:** Deploying a prompt because it "looked good" on 3 random examples.
*   **Magic Strings:** Hardcoding prompts deep inside Python functions instead of a Registry.
*   **Open Loop Deployment:** Running a model without any feedback mechanism to detect drift over time.
*   **The "Perfect Prompt" Fallacy:** Wasting weeks trying to engineer a prompt that works 100% of the time (instead of building error handling).

## Contribution
This section is a library of "Battle Scars." We encourage submitting **Post-Mortems** of real-world failures to help the community build better containment strategies.