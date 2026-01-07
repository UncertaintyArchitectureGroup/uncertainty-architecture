# Sensors: The Nerves

> **Function:** Measurement & Observability
> **Goal:** Calculate the Error Signal ($Error = Output - Intent$)

In Control Theory, a **Sensor** measures the state of the system. Without sensors, the system is "Open Loop" — it cannot detect if it has drifted off course.

In AI Engineering, we lack a `getBusinessTruth()` function. Therefore, we build **Sensors** to convert subjective quality ("vibes") into objective statistics.

## Core Artifacts

### 1. Golden Sets (The Reference Signal)
A curated, versioned dataset of inputs and their ideal outputs (Ground Truth).
- Used to detect regression and drift.
- Must be statistically significant (N > 30).

### 2. Metrics (The Instruments)
- **Deterministic Metrics:** JSON validity, latency, cost.
- **Probabilistic Metrics:** Semantic similarity, hallucination rate, tone match (often measured by LLM-as-a-Judge).

### 3. Eval Pipelines
Automated processes that run the Actuators against the Golden Sets to generate a **Drift Report**.

## The Philosophy
**Stop testing for luck.** Use sensors to measure the distance between the model's behavior and business intent.