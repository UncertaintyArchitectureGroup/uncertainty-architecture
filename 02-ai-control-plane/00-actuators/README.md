# Actuators: The Muscles

> **Function:** Execution & Containment
> **Goal:** Manage the shape of the probability distribution $P(y|x)$

In Control Theory, an **Actuator** is the mechanism that applies force to move the system. In AI Engineering, Actuators are the components that interact directly with the model to generate output.

They represent the **Muscles** of the system: powerful but blind. They require strict constraints (Schemas) and precise configuration (Prompts) to function safely.

## Core Artifacts

### 1. Prompt Registry
Prompts are treated as **Versioned Configuration**, not code.
- **Immutability:** Once published, a prompt version (e.g., `summarizer:v1.2`) never changes.
- **Separation:** Prompts live outside the application logic to allow tuning without redeployment.

### 2. Constraints (Schemas)
Mechanisms to fight **Syntactic Entropy**.
- **Strict JSON Schemas:** We do not parse strings; we validate objects.
- **Guardrails:** Deterministic rules that reject outputs violating safety or format constraints immediately.

### 3. Hyperparameters
The "knobs" that control the variance (Temperature, Top-P, Frequency Penalty).

## The Golden Rule
**No magic strings in the code.** All interaction logic must be encapsulated within the Actuator layer.