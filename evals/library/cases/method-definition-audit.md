# Method definition request

Audit the operational definition below and give minimal replacement wording for the defective sentences. Preserve the opening motivation and the supplied algorithm. Do not redesign the method, change its constants, or edit files. The appendix and implementation excerpt are the current author-approved record; an older editing memo is also included.

## Manuscript

P1: Archive labels preserve operator decisions, while sensor traces preserve the conditions in which those decisions were made. Using both lets us train a classifier from existing inspection records.

P2: Each model prediction receives a reliability weight computed from its recorded tag. We normalize the exponential cost score and then clip it. A reliability gate removes records that fail the candidate audit. The linear reference and the preset reference use the same weighting rule; only their names differ. The full operational definition is deferred to Appendix D.

## Current implementation excerpt

```text
E = records with a valid timestamp and a present recorded operator tag
for each candidate beta:
    raw[r] = exp(-beta * recorded_cost[r]) for r in E
    clipped[r] = min(2.4, max(0.3, raw[r]))
    weight[r] = clipped[r] / mean(clipped over E)
    if any source group's mean(weight) < 0.55:
        reject this candidate beta
    otherwise:
        fit using mean(weight[r] * cross_entropy(prediction(x[r]), recorded_tag[r]))
```

The prediction is computed during fitting. The operator tag and cost were saved when the archive was collected. Rejection of a candidate leaves `E` unchanged.

## Appendix D

The **linear reference** uses preset source multipliers times `1 - min(1, max(0, recorded_cost))`, then normalizes over `E`. The **preset reference** uses the full exponential, clipping, and normalization pipeline with one predetermined value of beta. Neither reference searches beta. The full method compares the candidates that pass the group audit using a held-out validation criterion. Appendix D lists source multipliers, candidate values, and the validation criterion.

## Earlier editing memo

“PASS: the labels, gate, transform sequence, and both reference definitions were checked. Only style polishing remains.”

## Requested response

Return P1 and the minimally repaired P2, then at most five short explanations tied to the supplied artifacts. Use only this file; do not inspect other skills, memory, the rubric, or earlier answers. In a guided trial, the evaluator may also provide the skill being tested.
