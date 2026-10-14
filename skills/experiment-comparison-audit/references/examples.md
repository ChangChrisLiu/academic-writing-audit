# Worked example: sorting records

This scenario is fictional.

**Request:** “Does this paragraph accurately describe our baselines?”

**Draft:** “All baselines use the same data and compute. The fixed rule is our method without tuning. Removing advice labels tests whether annotations help.”

**Records:** A sorter is trained on 12,000 ordinary and 3,000 expert-corrected records. The selected method and its preset-map control exclude 1,200 ordinary records using a quality gate. They use the same smooth nonlinear weight formula. The selected method fits four candidate parameterizations; the preset-map control fits one. A separately named fixed rule assigns constant weights on either side of a threshold. A uniform variant uses all 15,000 records. Every fit uses 5,000 updates with the same batch size. “Removing advice” actually drops all expert-corrected records, keeps source tags on retained records, and reuses the selected method's coefficients without retuning. Runtime is unreported.

**Audit:**

- The preset-map control is the shared-formula comparison without validation selection. The threshold rule is a different operation, even though both are fixed in advance.
- Quality-gated variants have 13,800 eligible records; Uniform has 15,000. Sharing the initial pool is a true but insufficient description of training support.
- Equal updates and batch size describe each fit. Four versus one candidate fits differ at the procedure level. The records do not establish a fourfold measured runtime.
- “Removing advice” removes a data source, leaving 10,800 quality-passing ordinary records. It does not isolate label information on otherwise identical examples. Its conclusion is conditional on the reused coefficients.

**Corrected wording:** “All variants use 5,000 updates per fit. The selected method evaluates four parameterizations of a nonlinear weighting rule; the preset-map control uses the same formula with one preset configuration. The threshold baseline uses a different, two-level weight rule. The quality-gated variants train on 13,800 eligible records, whereas Uniform uses all 15,000. The source-removal variant excludes expert-corrected records and retains the selected coefficients without retuning.”

**What to keep:** These comparisons remain reportable. The audit changes their descriptions and inferential scope; it does not establish that any variant wins or that the experiment is invalid.
