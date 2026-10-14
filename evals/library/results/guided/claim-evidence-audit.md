1. **Selection is not isolated.** “Validation selection caused the improvement” exceeds the design: normalization and threshold selection both changed. The retained table supports 142/180 versus 128/180 on the same specimens. Keep that comparison, but remove attribution to selection alone; no paired error table or inferential analysis is supplied.

2. **Historical inputs and texture necessity remain unresolved.** The current loader removes a textured border, but it postdates the reported training runs. Without records linking the weights to their inputs and loader configuration, it cannot verify that all reported runs used texture-free inputs. Neither the historical texture-free claim nor the conclusion that texture is unnecessary follows from this packet. Remove both claims; describe current loader behavior separately if needed.

3. **The generalization claim exceeds the evaluation.** Three microscope settings in one laboratory do not establish performance across laboratories. Retain the three-setting coverage and explicitly locate it within one laboratory.

**Minimally changed paragraph**

“Our classifier identified 142 of 180 specimens correctly, compared with 128 of 180 for the preset configuration, on the same specimens from three microscope settings in one laboratory. Correct identification means that the predicted species matched the blinded reference label. The configurations differed in both normalization and threshold selection, so this comparison does not isolate the contribution of validation selection. The current loader removes a narrow border containing background texture, but the inputs used in the reported runs remain unverified. Generalization across laboratories was not evaluated.”
