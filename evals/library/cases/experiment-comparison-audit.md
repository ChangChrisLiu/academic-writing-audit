# Comparison audit: acoustic event classifier

This is a fictional evaluation fixture.

## User request

Check whether this Methods paragraph describes the experiments correctly. Identify consequential errors and give one corrected paragraph in plain language. Keep the full answer under 350 words. Use only the packet; no files need editing.

## Draft

“We compare our validation-selected weighting method with an equivalent fixed baseline and a uniform baseline under identical data and compute budgets. The fixed baseline is our mapping without selection. The no-feedback ablation removes feedback labels, isolating their effect.”

## Experiment record

All methods use the same classifier architecture and optimizer and receive 8,000 optimizer updates per fit. Each is evaluated on the same held-out audio set. The pool contains 24,000 routine clips and 6,000 operator-corrected clips. Every clip has a source tag; corrected clips also have an error-type annotation.

| Variant | Weight rule | Eligible training clips | Fitting and selection |
| --- | --- | --- | --- |
| Selected | Normalize a smooth nonlinear function of confidence and error-type features, then apply source multipliers | Exclude 2,000 routine clips failing a quality gate | Fit six candidates with different coefficients; choose by validation accuracy |
| Fixed map | The same nonlinear formula with one preset coefficient vector and preset source multipliers | The same quality gate as Selected | One fit; no validation selection |
| Threshold | Assign one of two constant weights according to a confidence threshold, then apply preset source multipliers | The same quality gate as Selected | One fit; no validation selection |
| Uniform | Assign weight 1 to every clip | All 30,000 clips | One fit; no validation selection |
| No feedback | Use the chosen Selected coefficients and remove all operator-corrected clips | Quality-passing routine clips only | One fit; no retuning |

The draft's “fixed baseline” refers to Threshold. Fixed map is reported separately. The No feedback variant keeps the source tags on retained clips; it has no corrected clips on which an error-type annotation could be removed. Per-update batch size is the same, but total measured runtime and effective weighted exposure were not recorded. The manuscript can report these variants; no numerical results are supplied here.
