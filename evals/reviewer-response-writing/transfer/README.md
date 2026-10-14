# Cross-domain response-writing trials

Run date: 2026-10-14. Ten guided executions across seven fictional domains, using fresh writer contexts, plus separate assessment agents. These are development trials on one configured host, not evidence of universal or cross-model generality. No unguided control was run.

## What was observed

**No reviewer-facing manuscript voice was found in the ten saved outputs.** The peer-review-research case retained “reviewers” as a legitimate participant label. Necessary limitations were preserved. This is an observation about these artifacts, not a guarantee for future writing.

The initial independent review passed all 24 shared criteria across six cases. A subsequent primary-author review raised an ambiguity: “no analysis is supplied” became “no analysis is available” in a manuscript or author letter. The assessor's explicitly prompted follow-up qualified the evidence/inference judgments for two cases. Both the original all-pass assessment and the narrower follow-up are preserved. The issue was **unsupported scope of an absence claim**, not demonstrated fabrication or reviewer-directed manuscript prose.

The skill now distinguishes missing inputs from confirmed study facts and keeps missing-evidence requests in author notes. Three fresh contexts reran relevant cases, and a fourth handled a new economics case with an unavailable appendix and unverified analysis execution. The new outputs avoid the ambiguous absence claims while retaining known study limitations.

## Initial six cases: v0.3.0

| Domain and case | Output | Manuscript independence | Evidence/inference after adjudication | Coverage/status; scope |
| --- | --- | --- | --- | --- |
| [Ecology](cases/ecology.md) | [Complete answer](results/v0.3.0/ecology/answer.md) | Pass | Qualified: the letter says no relevant analyses are available without limiting that knowledge to the packet. | Pass; pass |
| [Qualitative education](cases/education.md) | [Complete answer](results/v0.3.0/education/answer.md) | Pass | Pass | Pass; pass |
| [Materials science](cases/materials.md) | [Answer](results/v0.3.0/materials/answer.md), [edited manuscript](results/v0.3.0/materials/manuscript.md), [response](results/v0.3.0/materials/response.md) | Pass | Pass; the letter's input-supply wording was dispensable. | Pass; pass |
| [Mathematics](cases/mathematics.md) | [Complete answer](results/v0.3.0/mathematics/answer.md) | Pass | Pass | Pass; pass |
| [History, Chinese output](cases/history.md) | [Complete answer](results/v0.3.0/history/answer.md) | Pass | Pass | Pass; pass |
| [Peer-review research](cases/peer-review-research.md) | [Complete answer](results/v0.3.0/peer-review-research/answer.md) | Pass | Qualified: the paper says no uncertainty analysis is available although only input absence was established. | Pass; pass |

The uncertainty clauses in the two qualified rows are negative statements (“No … is/are available”). The wording concerns the authors' knowledge; the facts only establish what the agent received. The [prompted adjudication](assessments/supplemental-adjudication.md) gives the exact excerpts, charitable readings, and narrower judgments. The [original independent assessment](assessments/independent-review.md) and [original matrix](assessments/independent-review.json) remain unedited.

The education rebuttal has 124 whitespace-delimited words against a 150-word limit. The initial peer-review rebuttal has 132 against 160, counting Markdown heading markers. The materials trial edited a real isolated source file: Methods, Conclusion, and the six-value sentence were preserved, and the response's replacement quotations matched the saved source. The history response correctly left missing identifiers and quotations unresolved.

## Clarification and new executions

The change adds one paragraph to the core skill and one paired example. It does not prohibit words such as “reviewer,” “available,” or “not evaluated.” Confirmed absences remain valid scientific facts. It also does not require interrupting a useful draft when the unsupported availability claim can simply be omitted.

| Case | Full revised-skill output | Observable handling |
| --- | --- | --- |
| Ecology regression | [Answer](results/revised/ecology/answer.md) | Missing analyses appear in separate author notes; the letter and paper retain the observed contrast and confirmed design limitations. |
| Materials regression | [Answer](results/revised/materials/answer.md), [manuscript](results/revised/materials/manuscript.md), [response](results/revised/materials/response.md) | The letter describes the actual source edit without exporting the input-supply clause. Added means and their difference are simple descriptive arithmetic from the supplied values. |
| Peer-review research regression | [Answer](results/revised/peer-review-research/answer.md) | Reports the counts and measured endpoint; removes the unconfirmed availability assertion and retains reviewer participants. |
| New economics transfer case | [Case](cases/economics.md), [answer](results/revised/economics/answer.md) | Distinguishes a written analysis plan from executed analysis. Keeps the missing interval pending and requests its verification separately. |

These three repeated cases are regressions, not held-out tests. Economics was added after the clarification; it is a new transfer example, not an unbiased before/after comparison. Different writers produced the initial and revised outputs, so wording changes cannot be attributed causally to the instruction change.

The [fresh regression assessment](assessments/regression-review.md) and [verdict matrix](assessments/regression-review.json) record 15 criterion passes, one qualification, and no failures. All four manuscript-independence and evidence/inference judgments pass. Economics coverage is qualified because the executed uncertainty calculation and interval cannot be supplied from the packet: the answer keeps that item explicitly pending. This is honest evidence-dependent incompleteness, not a reason to invent a completed response. Both repeated materials executions preserved the approved source sections and matched their letters to the actual edits.

The [mechanical checks](mechanical-checks.json) separately record word counts, source preservation, and the initial output hashes. Revised peer-review and economics rebuttals contain 131/160 and 123/180 whitespace-delimited words respectively. Packaging and mechanical checks do not replace the semantic judgments above.

## Method and reproducibility

- Each writer received one case, a frozen skill directory, and its own isolated output directory. Parent history was not inherited. Writers were instructed not to read memories, other skills, scoring criteria, other outputs, or network sources.
- All ten execution logs are stored beside their answers. Each reports reading the entrypoint and both routed references. Writer outputs are preserved byte-for-byte, including weaknesses and unresolved placeholders.
- The initial [rubric](rubric.md) and six cases were fixed before the primary agent read any output. [Design hashes](design-freeze.json) preserve that set. The separate [regression criteria](regression-criteria.md) were added after the ambiguity was identified.
- The first assessor received the cases, outputs, and rubric, but no skill or prior judgments. Its prompted follow-up is labeled separately. A second assessor reviews only the four new executions against their packets and criteria.
- [Run metadata](run-metadata.json) records scope and task identity. Exact model/runtime version identifiers were not captured; all writers inherited the host configuration without an override. This is not a comparison of ten distinct models.
- The [manifest](manifest.json) binds case, output, assessment, and skill-version hashes. Initial instructions are recoverable from Git commit `a01ae7938c20a3c8a6c53b982d0a9e0977f44f6c`; revised instructions are included in the current skill package.

Synthetic cases intentionally expose difficult boundaries and do not represent a random sample of scholarly work. No real submission, literature verification, PDF rendering, journal compliance determination, or broad disciplinary review was tested. The materials case verifies source editing only. The earlier [v0.3.0 development fixtures](../README.md) remain a separate case set and are not counted as executions here.
