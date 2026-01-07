# Controller: The Brain (Operating Model)

> **Function:** Judgment & Correction
> **Goal:** Close the Feedback Loop and minimize Error over time.

In Control Theory, the **Controller** reads the Sensor data, compares it to the Intent, and adjusts the Actuators.

In GenAI, "Truth" is often subjective and fluid (e.g., "Is this tone professional?"). Therefore, the Controller is not just a script — it is a **Socio-Technical System**. It is the specific configuration of **People and Processes** that injects judgment back into the loop.

## Core Components

### 1. Roles (The Operators)
Functional responsibilities required to manage the loop:
- **Prompt Steward:** Tunes the Actuators (Prompts).
- **Eval Owner:** Calibrates the Sensors (Golden Sets).
- **Reliability Engineer:** Maintains the infrastructure.

### 2. Rituals (The Control Logic)
Structured processes for decision making:
- **Drift Review:** Weekly analysis of sensor data.
- **Eval Bash:** Periodic calibration of Golden Sets.

### 3. Gates (The Decision Points)
- **Release Gates:** Hard thresholds (e.g., "Accuracy > 95%") that prevent bad configuration from reaching production.

## The Mission
**Governance is not bureaucracy.** Governance is the mechanism that corrects the system when it drifts.