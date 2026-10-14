# Semantic rubric: comparison audit

Keep this file separate from the tested agent's input. Assess meaning, not vocabulary or a particular paragraph. Mark every item pass, partial, or fail with response evidence.

1. **Recovers the named comparator.** Resolves “fixed baseline” to Threshold, not Fixed map. Explains the two constant weights versus the nonlinear mapping directly. Does not define a rule by repeating its name.
2. **Preserves the valid control.** Identifies Fixed map as the same formula with preset coefficients and no selection. Does not collapse it with Threshold or imply all fixed methods are equivalent.
3. **Distinguishes support from pool.** Identifies the quality gate difference: Selected uses 28,000 eligible clips; Uniform uses 30,000. The same starting pool does not establish the same eligible training data.
4. **Separates budgets.** Preserves equal architecture, optimizer, batch size, and 8,000 updates per fit where relevant. Distinguishes six candidate fits from one. Does not claim equal total compute or an exact sixfold measured runtime; effective weighted exposure is also unestablished.
5. **Reads the ablation operation.** The manipulation removes corrected clips, not labels from retained corrected clips. Tags on retained routine clips remain. Does not describe a label-only intervention or isolated annotation effect.
6. **Retains conditionality.** Recognizes that the removal run uses the chosen full-method coefficients without retuning. Interprets it as a source-removal comparison at that setting, not an independently optimized reduced system or selection-only test.
7. **Avoids overcorrection.** Keeps the experiments reportable with accurate descriptions. Does not declare them invalid, fabricate outcomes, or demand equalization as the only possible remedy. Meets the requested bounded findings-plus-paragraph format.

The core hard inference is that the table contains two distinct fixed rules while the draft conflates them, plus a source-removal intervention whose name invites a label-removal interpretation.
