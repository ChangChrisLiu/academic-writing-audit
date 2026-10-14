# Editorial request

The following fictional Methods and Results text sounds defensive after several review rounds. Please remove that tone and unnecessary repetition, while preserving the meaning and the transition into the result. Give replacement paragraphs and at most four short reasons. Do not change the protocol, add experiments, or rewrite the rest of the paper. Use only these materials.

## Current manuscript

P1: Reflection patterns vary across glass surfaces, so a detector calibrated on one surface may be uncertain on another. We therefore evaluate both defect detection and referral of uncertain images for manual review.

P2: We emphasize that the referral threshold was fixed using the development set, and it was certainly not chosen after seeing the test outcomes. Test images were not used to select the threshold. Images outside the calibrated intensity range were not assigned a defect label; the detector referred them for manual review. This is not an attempt to avoid difficult examples. These images remained in the evaluation denominator.

P3: Under the evaluated surface changes, the detector referred more out-of-range images than the reference system. This behavior is consistent with the intended referral rule. We do not claim that this result proves safety, and we stress that this is a limited experiment. The study did not measure whether human reviewers subsequently identified the defects correctly.

## Supplied protocol and result record

- Threshold selection used the development set only and was completed before the test outcomes were examined.
- Out-of-range images trigger referral instead of a defect label. They remain in the evaluation denominator.
- The reported outcome distinguishes defect labels from referrals. Referral by itself is not a correct defect classification.
- The test changed glass surfaces. The observed referral difference is descriptive; no statistical or causal analysis is supplied.
- Human-review accuracy was outside the evaluated endpoint. No downstream deployment or safety assessment was performed.

The next section discusses what the observed referral behavior means for a possible workflow that includes human review.
