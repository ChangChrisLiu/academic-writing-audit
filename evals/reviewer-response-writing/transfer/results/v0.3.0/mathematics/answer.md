**Draft response letter**

Dear Editor and Reviewers,

Thank you for identifying two errors in the theorem and its proof. The original statement is false: boundedness alone does not ensure that a continuous function attains its minimum, and compactness does not ensure uniqueness. The intended result is existence of a minimum on a nonempty compact domain. We propose replacing the theorem and proof with the text below. These changes are proposed; the manuscript source has not yet been edited.

**R1.1:** Boundedness alone does not imply compactness. For example, \(f(x)=x\) on \((0,1)\) has infimum \(0\) but does not attain it.

**Response:** We agree. The assertion in the original proof that a bounded set is compact is incorrect. In the reviewer's example, the domain is nonempty and bounded and the function is continuous, yet no point in the domain attains the infimum. We propose replacing the bounded-domain hypothesis with the requirement that \(K\) be a nonempty compact subset of \(\mathbb{R}\). The corrected proof uses continuity to show that \(f(K)\) is nonempty and compact, so that it contains its infimum. This establishes attainment under the corrected hypothesis.

**Proposed change:** Replace the current theorem's domain assumption and its existence argument as shown in the proposed theorem and proof below.

**R2.1:** Compactness would not imply uniqueness. A constant function on \([0,1]\) is a counterexample.

**Response:** We agree. For a constant function on \([0,1]\), every point of the domain is a minimizer, so even a nonempty compact domain does not justify uniqueness. We propose deleting the uniqueness claim from both the theorem and the proof. The corrected theorem asserts only that at least one minimizer exists. We do not propose additional assumptions to obtain uniqueness, since no such conclusion is intended.

**Proposed change:** Remove “unique” from the theorem and remove the unsupported uniqueness assertion from the proof, using the complete replacement below.

Sincerely,
The Authors

**Proposed replacement theorem and proof**

**Theorem.** Let \(K\) be a nonempty compact subset of \(\mathbb{R}\), and let \(f:K\to\mathbb{R}\) be continuous. Then \(f\) attains a minimum on \(K\); that is, there exists \(x_{\min}\in K\) such that
\[
f(x_{\min})\leq f(x)\qquad\text{for every }x\in K.
\]

**Proof.** Since \(K\) is nonempty and compact and \(f\) is continuous, the image \(f(K)\) is a nonempty compact subset of \(\mathbb{R}\). In particular, it is bounded below and contains its infimum. Let \(m=\inf f(K)\). Because \(m\in f(K)\), there exists \(x_{\min}\in K\) with \(f(x_{\min})=m\). By the definition of the infimum, \(m\leq f(x)\) for every \(x\in K\). Thus \(f\) attains a minimum on \(K\). \(\square\)
