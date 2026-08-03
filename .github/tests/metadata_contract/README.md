# Metadata Contract Regression Fixtures

These dependency-free fixtures build a minimal synthetic repository and mutate one metadata invariant at a time.

They cover:

- required YAML frontmatter;
- controlled `artifact_type`, `status`, `maturity`, `module`, and `topics` values;
- structural and topic tag projection;
- active `canonical_for` uniqueness;
- protected glossary entries;
- non-blocking terminology warnings;
- malformed and duplicate frontmatter fields.

The fixture repository is intentionally synthetic. Real-repository validation runs in separate GitHub Actions jobs.
