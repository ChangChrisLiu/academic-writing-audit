# Evaluation record

Run date: 2026-10-14. These are small, manually inspected development trials, not a benchmark establishing general effectiveness.

## Materials and execution

- [Editorial scenario](editorial-scenario.md): a fictional manuscript with a coherent motivation paragraph, defensive assurances, comparison ambiguities, unsupported attribution, and distinct studies.
- [Rubric](rubric.md): semantic criteria for judging the complete responses.
- [Transfer scenarios](transfer-scenarios.md): review-only, theoretical, qualitative, and grammar-only requests.
- [Manifest](manifest.json): hashes of the installable skill, fixtures, rubric, and saved responses used in this record.

Five control runs were completed without loading this skill. Five guided runs then received the same editorial request plus `SKILL.md` and access to its references. Every run used a fresh subagent context in the same configured host session. Agents were instructed not to inspect memories, earlier outputs, the rubric, or other project materials. Runtime and model version identifiers were not recorded, so this is not a reproducible cross-model comparison.

The control responses were read before the skill was written. The revision-preservation guidance addresses an observed behavior: several controls changed or removed the coherent motivation bridge. Other scientific checks were already handled correctly by the controls. The guided responses were manually read and scored by the skill author; scoring was not blinded or independently adjudicated. The test passage influenced development and is not held out.

## Editorial results

| Rubric dimension | Controls | With skill | Observation |
| --- | --- | --- | --- |
| 1. Author preservation | 2 pass, 3 fail | 5 pass | Controls A, D, and E changed P1 without a concrete defect; every guided run retained it verbatim. |
| 2. Attribution | 5 pass | 5 pass | Unsupported selection/feature causality removed. |
| 3. Comparison identity | 5 pass | 5 pass | All counts retained and studies separated. |
| 4. Budget and support | 5 pass | 5 pass | Per-fit budgets separated from number of fits; unequal eligible records retained. |
| 5. Endpoint | 5 pass | 5 pass | Both endpoint conditions, label timing, and no actual release retained; absolute safety assurance removed. |
| 6. Ablation operation | 5 pass | 5 pass | Record removal distinguished from label removal. |
| 7. Definition | 5 pass | 5 pass | Linear fixed rule and nonlinear mapping stated directly. |
| 8. Proportionality | 5 pass | 5 pass | No invented experiment, uncertainty result, or broad rewrite of the task. |

Dimension 1 measures a separate failure that the broader scope check in dimension 8 does not hide. Representative evidence:

- **Control A:** Replaced “Their different roles make it difficult…” with “Using the logs as a coherent training resource requires…”; its explanation gives a phrasing preference rather than a concrete defect.
- **Control D:** Removed the gap sentence and described the action as “删去笼统的困难表述.” This removes the explicit challenge linking records to the contribution.
- **Control E:** Also removed the gap sentence, explaining “删除笼统的困难陈述.”
- **Controls B and C:** Retained P1 verbatim, showing that good preservation was possible without the skill.
- **Guided A–E:** Retained P1 verbatim and explicitly recognized the problem–challenge–contribution chain. For example, guided B states “删掉中间句会削弱动机.”

The budget wording varied: some responses omitted “nominal” while retaining the supplied 4,000-update budget and five-versus-one fits. They did not claim equal effective exposure or total computation. Guided responses varied in where they placed the endpoint and whether they included an explicit non-isolation sentence; both forms can satisfy the rubric. No single wording was required.

| Run | Control response | Guided response |
| --- | --- | --- |
| A | [A](results/baseline-a.md) | [A](results/guided-a.md) |
| B | [B](results/baseline-b.md) | [B](results/guided-b.md) |
| C | [C](results/baseline-c.md) | [C](results/guided-c.md) |
| D | [D](results/baseline-d.md) | [D](results/guided-d.md) |
| E | [E](results/baseline-e.md) | [E](results/guided-e.md) |

## Transfer check

One additional fresh context answered all four [transfer requests](transfer-scenarios.md) with the skill. [Full output](results/transfer.md).

| Request | Result | Evidence in response |
| --- | --- | --- |
| T1: Review only | Pass | “No rewrite is provided”; preserved the holdout definition, distinguished unavailable figure evidence, and did not reuse the memo's PDF claim. |
| T2: Theory | Pass | Retained the assumptions and non-uniqueness boundary; deleted only the reassurance sentence and required no empirical study. |
| T3: Qualitative | Pass | Kept the sample description and negative case; removed the unsupported measured-effect and cross-institution claims. |
| T4: Grammar only | Pass | Changed only “shows” to “show.” |

These were guided smoke checks, with no control condition and one response per request. They establish only what was observed in those responses. They do not test citation retrieval, real file patching, rendered manuscripts, publication, or general disciplinary competence.

## Package checks

The completed skill passed the local skill-creator frontmatter/scaffold validator. Relative file links and the Codex UI metadata were checked, and the standalone install copy was compared by file hash. The public bundle contains generic instructions and fictional fixtures; no originating manuscript, private review transcript, or source data is included. These packaging checks do not evaluate scientific correctness.

For future changes, repeat the relevant fixtures in fresh contexts and inspect the complete answers. Keep new observed failures visible rather than replacing them with a success-only summary.
