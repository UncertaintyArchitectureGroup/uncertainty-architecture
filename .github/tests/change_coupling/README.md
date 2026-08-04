# Change-Coupling Regression Fixtures

These dependency-free fixtures create small temporary git repositories and compare a synthetic base commit with a proposed head commit. Each case combines an actual diff, a machine-readable `ua-change-contract` declaration, and optional labels.

The suite covers:

- valid repository-policy coupling;
- missing, duplicated, malformed, and schema-invalid PR contracts;
- unknown and uncontrolled PR fields;
- changelog enforcement for notable changes;
- glossary, roadmap, and research-traceability declaration/file consistency;
- research-state decisions that require traceability;
- maintained-file deletion and rename compatibility decisions;
- owning-path intersection with the actual diff;
- narrow exception labels and rejection of unrelated exception labels.

The fixtures test policy behavior independently of the live pull-request event. The GitHub Actions workflow separately validates the real pull-request body, labels, and git diff.
