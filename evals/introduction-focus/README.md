# Introduction focus checks

Run date: 2026-10-27. Three fresh-context executions examined introduction drafting and review using fictional environmental-sensing and archival-research materials. The initial drafting response repeated an already established explanation in its contribution paragraph. A narrow rule clarification was followed by a new drafting execution on the same packet.

The update establishes the destination before tailoring an introduction, then follows one narrowing argument from relevant progress through gap and motivation to contribution. Conference framing can integrate the connections compactly. Journal framing makes the unresolved issue, consequence, and rationale explicit, subject to the actual article requirements. Both retain necessary explanations and remove detours or repeated reassurance.

## Materials and execution

The [drafting packet](cases/draft.md) requests conference and journal introductions from the same evidence, followed by a request with no destination. The [audit packet](cases/audit.md) includes a journal introduction with an unrelated detour and defensive assurances, an over-compressed conference introduction, and a grammar-only request for a compact journal methods note.

The cases and [semantic rubric](rubric.md) were frozen before execution. Each agent received only its packet, the applicable frozen skills, and bounded file-output instructions. Parent-turn history, earlier outputs, the rubric, and external sources were excluded from the requested context. The [run metadata](run-metadata.json) records reported reads and limits; these were prompt-level isolation constraints, not a filesystem sandbox. The two freezes retain hashes for the [initial](initial-design-freeze.json) and [revised](regression-design-freeze.json) inputs. Initial drafting instructions are stored as a [snapshot](tested-skills/initial/research-manuscript-writing/SKILL.snapshot.md).

| Execution | Full response | Author-assessed result |
| --- | --- | --- |
| Initial drafting | [Response](outputs/initial-draft.md) | Five criteria pass; concision/explicitness is partial because the journal contribution paragraph repeats the source roles already explained. |
| Audit | [Response](outputs/audit.md) | Six criteria pass; necessary explanations and scope survive, the unrelated detour and assurances are removed, and a lost bridge is restored. |
| Revised drafting | [Response](outputs/regression-draft.md) | Six criteria pass; the contribution paragraph adds the evaluated estimator and finding without replaying the source-role explanation. |

See the [complete assessment](assessment.md) for evidence and the remaining optional wording observation. The clarification tells the contribution paragraph to add what the study did and found after motivation has established the rationale. A restatement still belongs when it serves a distinct function, such as bounding a broader claim.

These are semantic criteria applied to three constructed responses, not independent experimental samples. The skill author assessed the outputs without blinding or independent adjudication. There is no unguided control, so no improvement over unaided agents or general reliability is established. The regression uses the same development packet and is not held out. Four skill entrypoints were read by test agents; the umbrella academic-writing-audit update received consistency and package checks but was not read in these executions. No real venue policy, literature retrieval, source-file modification, or document rendering was tested.

Generated responses, case text, and rubric text are preserved unchanged. Published freeze records map local path keys to portable repository paths without changing file digests. The original local freeze hashes are recorded. The [manifest](manifest.json) identifies the published record and tested skill bytes.
