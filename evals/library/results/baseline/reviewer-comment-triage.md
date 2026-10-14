| Concern | Current evidence | Smallest reader-facing action |
| --- | --- | --- |
| R1: What does no-context remove? | Every report is retained; contextual metadata fields are replaced with a fixed missing-value token. Report text and labels stay unchanged. The table note contradicts this operation. | Specify the operation in Methods and replace the table note. The earlier handoff's claim that this was fixed is unsupported. |
| R2: Does the method transfer across institutions? | All data come from one institution, split by month. The supplied results show higher full-model accuracy on held-out months; no institution-shift experiment or uncertainty analysis is supplied. | Replace the cross-institution conclusion with the observed temporal result and its scope. Delete the reviewer-directed defensive sentence. A temporal split does not establish institution transfer. |
| R3: Why is the simple reference informative? | Appendix F specifies a department-conditioned training-class-frequency predictor using neither report text nor learned representations. | Give its construction and comparison role in Methods, retaining the appendix pointer. |

Replacement Methods text:

“The no-context variant tests the contribution of contextual metadata by replacing its fields with a fixed missing-value token while retaining every training and evaluation report, its text, and its target label. The simple reference predicts the most frequent training-set class within a report's department, breaking ties using global training-set class frequency. It uses neither report text nor learned representations, providing a comparison with predictions based only on department-level class frequencies (Appendix F).”

Replacement table note:

“The no-context variant retains all reports and replaces contextual metadata fields with a fixed missing-value token; report text and target labels remain unchanged.”

Replacement Discussion text:

“On held-out collection months from one institution, the full model achieved higher accuracy than the no-context variant and the simple reference. These results do not establish generalization across institutions.”

Keep the Introduction unchanged. These repairs report the supplied accuracy ordering without claiming statistical significance or adding an unperformed experiment.
