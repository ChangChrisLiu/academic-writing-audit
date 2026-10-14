All three concerns remain in the current excerpts. They can be addressed through focused manuscript repairs; preserve the Introduction and the correct statement that the no-context variant tests contextual metadata.

| Concern | Current evidence | Smallest reader-facing action | Remaining evidence boundary |
| --- | --- | --- | --- |
| R1: What is removed? | Methods omit the operation; the table says reports are excluded. The experiment record retains every report and replaces metadata with a fixed missing-value token. | Add the masking operation in Methods and correct the table note. Remove the Discussion's defensive assurance. | No additional ablation is supplied or needed to describe this one accurately. |
| R2: Transfer across institutions? | All data come from one institution, split by month. Higher held-out-month accuracy does not establish institution transfer. | Replace the cross-institution claim with the observed temporal-split result and its population boundary. | Cross-institution transfer remains untested in this packet; no uncertainty analysis is supplied, so do not claim statistical significance. |
| R3: Why is the simple reference informative? | Appendix F defines department-level training-class frequencies with a global-frequency tie break; it uses neither report text nor learned representations. | State its construction in Methods and identify what comparison it provides; retain the appendix pointer. | Its definition is supported; higher accuracy alone does not establish a mechanism for the full model's advantage. |

**Methods replacement:** The no-context variant tests the contribution of contextual metadata by replacing its fields with a fixed missing-value token while retaining every training and evaluation report, its text, and its target label. The simple reference predicts the most frequent training-set class within each report's department, breaking ties using global training-set class frequency (Appendix F). It provides a department-frequency comparison without report text or learned representations.

**Table-note replacement:** The no-context variant retains every report and replaces contextual metadata fields with a fixed missing-value token; report text and target labels remain unchanged.

**Discussion replacement for both supplied sentences:** The full model achieved higher accuracy than the no-context variant and the simple reference on held-out collection months from the same institution. These results do not establish transfer to other institutions.

These are proposed repairs based on the current excerpts and experiment record, which contradict the earlier handoff's PASS judgments; no files were edited.
