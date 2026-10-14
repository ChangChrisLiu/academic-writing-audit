# Claim evidence audit: microscopy classifier

This is a fictional evaluation fixture.

## User request

Review the paragraph below against the supplied evidence. Give the three most consequential findings, then a minimally changed paragraph. Keep supported findings direct. Use at most 300 words; do not invent experiments, search outside this packet, or edit files.

## Draft

“Our classifier identified 142 of 180 specimens correctly, compared with 128 of 180 for the preset configuration. This establishes that validation selection caused the improvement and confirms that background texture is unnecessary. All reported runs used texture-free inputs, as verified by the current loader. The method therefore generalizes across laboratories.”

## Supplied evidence

- Both configurations were evaluated on the same 180 specimens from three microscope settings in one laboratory. Correct identification means the predicted species matched the blinded reference label. The two counts are recorded in the retained evaluation table. No paired error table or inferential analysis is supplied.
- The selected configuration used both a different normalization rule and a validation-selected threshold. The preset configuration used the original normalization and a fixed threshold. There is no experiment changing threshold selection alone.
- The repository's current loader removes a narrow border that contains background texture. This version was committed after the reported training runs. The retained model weights have no recorded source revision, input manifest, or loader configuration. Nothing supplied establishes whether earlier inputs contained that border.
- There is no evaluation from another laboratory. The author wants to retain the observed performance comparison and the fact that evaluation covered three microscope settings.
