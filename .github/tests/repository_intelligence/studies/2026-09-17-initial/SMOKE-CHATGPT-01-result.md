# ChatGPT rehearsal — reported GitHub access; capture pending

Disposition: **unscored client rehearsal; raw evidence and model configuration pending**. No primary A/B pair, score or RI verdict is created.

## Evidence provenance

- Received from the maintainer in the organizer conversation on 2026-09-17.
- Maintainer reports another ChatGPT account, a free plan, the default model and a configured GitHub connector. The exact model/reasoning setting, client/device and original session ID were not provided. “Default” is not a verified model identifier.
- Available evidence is the pasted response below. Its statement that a full tool transcript exists describes the original client; that transcript has not been supplied to the organizer.
- The exact submitted prompt is not available. This receipt follows SMOKE-01, but its filename does not assert a submitted Task ID. The prepared SMOKE-02 prompt had not been issued before this return.
- The response lists 16 operations. These are reported operations, not an independently established complete call count or measured transport cost.

## Organizer assessment

1. The response reports pinned GitHub file/blob reads, which is promising evidence of an available transport. Its named licensing files and broad split agree with the pinned repository. This source check is unscored and does not verify the original tool calls.
2. Recording RI as unverified and using authoritative sources is appropriate fallback behavior. It is not proof of RI failure or benefit. A primary Treatment session may use fallback; a study with no verified RI use cannot establish the protocol's BENEFIT outcome.
3. The reported sequence does not include the successful projection job's freshness record. Locating a blob in a commit tree alone does not demonstrate that its generated contents are fresh. Compare actual client evidence against the accepted checkout/tree/blob/content-hash record before upgrading delivery.
4. The statement that the recursive tree's identity equals the commit SHA needs the original response for interpretation. The organizer's verified preparation commit is `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`; its Git tree is `ed4dcf068af29ad0eb42867e1548076e21eca67d`. A tool may echo its input ref: do not treat that field alone as either proof of verification or proof of fabrication.
5. Several reads are reported truncated. Later full blob reads may recover some content, but completeness and read order must be checked in the actual outputs. Do not reconstruct missing output using fresh organizer reads and attribute it to the tested session.
6. If complete returned RI content is present in the existing capture, the organizer can compute its hash from that captured content and compare it with the accepted record. The model need not invent a hash or byte count. Preserve wrappers, truncation and unavailable metrics honestly. Missing context measurements prevent the efficiency claim; they do not alone invalidate every quality comparison.
7. The same actual model/settings and isolation must hold across the primary arms. Inspect the client's displayed configuration before freezing it; neither the free-plan label nor the model's self-description establishes that parity. If the client exposes only an unidentifiable default, leave that limitation unresolved rather than invent a model name.

## Next action

Request the original session share link/export with visible tool inputs and outputs, if the client exposes them, plus its displayed model/settings and submitted prompt. Inspect existing evidence before asking the maintainer to repeat any task. If the export omits tool outputs, record that limitation and determine whether they can be copied directly from the original session.

After client qualification, complete independent task selection and freeze the study before issuing the 24 primary prompts. Both rehearsals remain outside the primary sample and are not compared as a Gemini-versus-ChatGPT experiment. The v11 protocol and thresholds remain unchanged.

## Response as pasted by the maintainer

The account/plan information above is maintainer metadata. The following is the supplied response, not an independently verified raw transcript.

```text
## Short answer

At the verified study checkout `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`, the repository states a dual-license model:

* **Documentation / specifications / architectural doctrine / diagrams / operating-model material:** **Creative Commons Attribution 4.0 International (CC BY 4.0)**. The governing summary is `LICENSING.md`, with the full license text in `LICENSE-DOCS.md`.
* **Code / scripts / reference implementations / executable artifacts:** **Apache License 2.0**. The governing summary is `LICENSING.md`, with the full license text in `LICENSE-CODE.md`.

The repository tree at the study ref explicitly contains `LICENSING.md`, `LICENSE-DOCS.md`, and `LICENSE-CODE.md`.

### Capture note

**Prior repository context:** none was visible before this run, apart from the repository/task metadata in the prompt. No hidden Memory setting was inspected or verified.

**Verified checkout identity:** study ref `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`; the recursive tree response independently reported that same SHA as its tree identity.

| #  | Operation    | Resource                                                 | Ref                                             | Result                                                                                                |
| -- | ------------ | -------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| 1  | `fetch`      | repository tree                                          | `989fc1398fc221ffca4e1f7a141b2c03bfc7cfb3`      | success; response display truncated                                                                   |
| 2  | `fetch_file` | `AGENTS.md`                                              | study SHA                                       | success, but display truncated                                                                        |
| 3  | `fetch_file` | `AGENTS.md`                                              | study SHA                                       | success; attempted fuller read                                                                        |
| 4  | `search`     | `license`                                                | default branch / no explicit ref                | success, 0 results                                                                                    |
| 5  | `fetch_file` | `.github/REPOSITORY-INTELLIGENCE.md`                     | study SHA                                       | success, display truncated                                                                            |
| 6  | `search`     | `Agent Context Surface`                                  | default branch / no explicit ref                | success, 0 results                                                                                    |
| 7  | `fetch_file` | `.github/tests/repository_intelligence/AB-EVALUATION.md` | study SHA                                       | success                                                                                               |
| 8  | `fetch_file` | `.github/AGENTS.md`                                      | study SHA                                       | success                                                                                               |
| 9  | `fetch`      | recursive Git tree                                       | study SHA                                       | success; returned `truncated:false` and exposed compact-surface blob identity                         |
| 10 | `fetch_blob` | `assets/repository-intelligence/agent-context.json`      | blob `1b1c3f07ed7202d566fca1dda0004f89cb6e5219` | returned content; complete delivery could not be cryptographically verified from exposed measurements |
| 11 | `fetch_file` | `LICENSING.md`                                           | study SHA                                       | success                                                                                               |
| 12 | `fetch_file` | `LICENSE-DOCS.md`                                        | study SHA                                       | success, display truncated                                                                            |
| 13 | `fetch_file` | `LICENSE-CODE.md`                                        | study SHA                                       | success                                                                                               |
| 14 | `fetch_blob` | `AGENTS.md`                                              | blob `0652e812be1474f61081162c19b34bdbbc122f98` | success; full content visibly returned                                                                |
| 15 | `fetch_blob` | `LICENSE-DOCS.md`                                        | blob `4ea99c213c5c0c005ae4e80df8e52169d06896ec` | success; full content visibly returned                                                                |
| 16 | `fetch_blob` | `LICENSE-CODE.md`                                        | blob `7a4a3ea2424c09fbe48d455aed1eaa94d9124835` | success; full content visibly returned                                                                |

**RI delivery:** the compact surface was located at `assets/repository-intelligence/agent-context.json`, and its blob identity was established from the study-ref tree. Its returned content appeared structurally complete, including its source-identity and producer fields, but the client did **not** expose a measurable complete-returned-content SHA-256/byte count with which to satisfy the protocol's `verified` criterion. Therefore I recorded RI as **unverified**, not successful verified delivery, and used authoritative license files as fallback. The A/B protocol explicitly requires fallback for missing, stale, or unverifiable RI.

**Visible limitations:** several `fetch_file` displays were truncated by the client response budget. The subsequent blob reads for `AGENTS.md`, `LICENSE-DOCS.md`, and `LICENSE-CODE.md` visibly returned their complete content. No repository modification, local checkout, shell retrieval, or non-GitHub repository access was used.

**Traffic measurements:** returned UTF-8 byte counts / input tokens: **unavailable**. No estimates were made from repository file sizes.

**Complete tool capture:** the client exposes the GitHub calls and returned tool transcript in this conversation; the individual truncated displays are preserved as shown above rather than reconstructed or estimated.
```
