# Figure and caption request

Review the proposed overview figure against the current Methods. Return only the semantic fixes to the diagram specification and a minimally revised caption. Keep the caption's valid opening sentence and the three-stage structure. No redesign or file changes are requested.

## Available figure evidence

This is a **textual diagram specification only**. No raster image, vector file, or rendered page is supplied.

```text
Stage 1: Curated masks M + automatic masks A + technician corrections C + rejected frames R
    -> shared training pool
Stage 2: shared training pool -> full model
         shared training pool -> curated-only reference
         microscopy test score -> weight optimizer -> full model
Stage 3: full model -> sample targeting -> laser treatment completed
An unlabeled arrow runs from Stage 3 back to the training pool.
```

## Current Methods

The full model trains on quality-eligible records from M, A, and C. Rejected frames R are retained for a descriptive exclusion audit and never enter a training loss. The curated-only reference trains on quality-eligible M. Both methods use the same architecture.

Candidate training weights are chosen on a validation partition. A separate microscopy test partition is evaluated once after this choice. No test examples or scores enter fitting or selection. The training pool remains fixed throughout this experiment.

Test success requires both centering the target cell in the field of view and approval of its segmentation by a technician. Evaluation ends before any laser pulse; treatment itself is outside the measured endpoint.

## Draft caption

A three-stage workflow connects image curation, model fitting, and microscopy evaluation. Every archived frame contributes to training, and the two methods share the same labeled frames. Microscopy feedback optimizes the training weights. Successful laser treatment demonstrates the practical benefit of the pipeline.

## Design note from an earlier pass

“The scientific flow passed review. Change the feedback arrow to a dotted line and improve its color contrast; this should settle the remaining issue.”

## Requested response

Provide a short list of diagram-specification changes, the caption, and one sentence stating what evidence your review covers. Use only this file; do not inspect other skills, memory, the rubric, or earlier answers. In a guided trial, the evaluator may also provide the skill being tested.
