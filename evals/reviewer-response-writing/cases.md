# Response-writing development cases

All facts, names, counts, and comments below are fictional. Use only the information supplied within each case. They are separate requests, not one submission package.

## A. Short rebuttal with a separate manuscript proposal

**Request:** Draft a rebuttal of at most 180 English words, including headings. Group shared concerns if useful and retain comment IDs. Then give a separate proposed Results paragraph, outside that word limit. Do not edit any file.

**Venue instructions supplied for this case:** New results are allowed in the response. Only text can be submitted. No manuscript replacement is accepted during this phase.

**Comments:**

- R1-Q1: “Please define the preset comparator and explain whether the gain isolates candidate selection.”
- R2-Q1: “What is different about the comparator? Is training cost matched?”
- R2-Q2: “Please state the numerical rejection threshold.”
- R3-Q1: “Please evaluate another backbone.”

**Evidence:**

- The selected procedure fits six candidates with nonlinear evidence weights and chooses one using held-out validation. The comparator uses a preset linear score with fixed group multipliers and fits one model.
- Each fit has a budget of 3,000 updates. No total-compute measurements are supplied.
- The original evaluation recorded 78/100 versus 66/100 successes. A new stress test recorded 49/80 versus 34/80. No uncertainty analyses or trial-level data are supplied.
- The current Results sentence is “Candidate selection alone caused the improvement.”
- The historical rejection threshold has not been recovered. The current software default is 0.2, but no record links it to the reported experiments.
- No second-backbone experiment has been performed. The author has not committed to one.
- No manuscript changes have been made.

## B. Revision letter with mixed work status

**Request:** Draft a point-by-point English response letter for these three comments. Supply a separate proposed manuscript sentence for the unresolved claim. Do not edit source files or add an experiment plan. No word limit applies.

**Comments:**

- R1-Q1: “Explain what happens to incomplete records.”
- R1-Q2: “Does the model remain robust when training labels are corrupted?”
- R2-Q1: “Please include final page and line references for the changes.”

**Supplied artifacts and status:**

- The current source excerpt, marked revision C, Methods / Record handling, reads exactly: “Incomplete records trigger abstention and remain in the evaluation denominator.” The revision log and source diff both show that this sentence was inserted in revision C. No other files or rendered pages are available.
- The current Results sentence reads “Our model is robust to label corruption.” No edit has been made to it.
- Two annotators agreed on 94 of 100 labels under the stated rubric. No model was retrained with corrupted labels.
- The visible PDF is revision B. Revision C has not yet been compiled, so final page/line numbers are unavailable.

## C. Audit only; preserve a valid statement

**Request:** Audit this draft response and its proposed paper sentence. Do not rewrite either. Identify any actual problem and anything that should remain unchanged.

**Comment R2-Q3:** “The perturbation may hurt performance; please quantify its effect.”

**Evidence:** In the tested setting, the supplied estimate is +2 percentage points, with a 95% interval of [-9, 13]. No equivalence margin or equivalence analysis was specified.

**Draft response:** “The estimated difference is +2 percentage points (95% interval [-9, 13]). This establishes equivalence and resolves the robustness concern.”

**Proposed paper sentence:** “The estimated difference under the tested perturbation was +2 percentage points (95% interval [-9, 13]).”
