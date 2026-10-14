Diagram-specification changes:

- Stage 1: Route quality-eligible M, A, and C to the full model's training pool. Route R only to a descriptive exclusion audit, with no training-loss connection.
- Stage 2: Give the curated-only reference a separate input containing quality-eligible M only. Mark the two methods as using the same architecture.
- Stage 2: Replace the microscopy-test-score-to-weight-optimizer connection with validation-partition-to-candidate-weight-selection. Reserve the separate microscopy test partition for one evaluation after weight selection; no test data or scores enter fitting or selection.
- Stage 3: Replace “laser treatment completed” with the measured success endpoint: target-cell centering AND technician approval of segmentation. End evaluation before any laser pulse.
- Remove the Stage 3-to-training-pool arrow. The pool is fixed, so making that arrow dotted would still imply an unsupported feedback operation.

Caption:

A three-stage workflow connects image curation, model fitting, and microscopy evaluation. Image curation supplies quality-eligible M, A, and C for the full model and quality-eligible M for the curated-only reference; rejected frames R are retained only for a descriptive exclusion audit. Model fitting uses the same architecture for both methods, with candidate training weights selected on a validation partition and the training pool held fixed. The separate microscopy test partition is evaluated once after weight selection, with success requiring both target-cell centering and technician approval of segmentation; evaluation ends before any laser pulse.

This review covers the semantics of the supplied textual diagram specification and caption against the current Methods; no image, layout, color, or rendered-page inspection was possible.
