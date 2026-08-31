# GitHub Policy and CI Protocol for AI Contributors

## Scope

This file applies only to work under `.github/` and supplements the root [`AGENTS.md`](../AGENTS.md). Read [`CONTRIBUTING.md#code-contributions`](../CONTRIBUTING.md#code-contributions) before changing validators, policy, tests, or workflows.

## Required route

Keep one owner per responsibility and follow this chain when a repository rule becomes executable:

human-readable owner
→ machine-readable policy
→ validator or context collector
→ regression or mutation fixture
→ workflow orchestration

Extend the existing owner instead of creating a parallel validator or workflow when the responsibility already exists.

## Scoped invariants

- Workflows orchestrate commands; they must not hide policy logic that belongs in a validator or machine-readable contract.
- A `pull_request_target` workflow must never check out or execute candidate-controlled code.
- Policy and security checks fail closed when required repository state or evidence cannot be established.
- Keep validators deterministic and dependency-light. Separate live GitHub-state checks from pure repository checks when possible.
- Protect observable invariants, commands, and failure behavior rather than private helper names or incidental implementation shape.
- Every defect fix needs a regression that fails without the fix. Every deliberate protected-rule change updates its owner, policy, validator/tests, and workflow wiring together.
- Changed repository-owned Python must parse successfully; changed maintained JSON/YAML and web source must pass the bounded formatter contract when selected by the code-quality validator.
- Preserve pinned third-party actions, minimal permissions, and existing supply-chain checks when editing workflows.

For Quartz or publication behavior touched from `.github/`, also read [`../quartz/AGENTS.md`](../quartz/AGENTS.md) and [`../quartz/README.md`](../quartz/README.md).
