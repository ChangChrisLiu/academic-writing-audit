Part 1

```latex
\section{Related Work}

Contraction analyses relate the behavior of an iteration to both the mapping's regularity and the presence of perturbations. For exact iteration on a complete metric space, a contraction constant $q<1$ supports existence of a unique fixed point and a geometric bound on the distance of iterates from that point \cite{c1}. A related analysis in a finite-dimensional normed space retains strict contraction while incorporating bounded deterministic error through the recursion $e_{k+1}\leq q e_k+\delta$ \cite{c2}. It derives the limiting upper bound $\delta/(1-q)$, connecting the perturbation magnitude to the asymptotic error estimate \cite{c2}. These results address a common question about control of iteration error, but their conclusions concern different error models. The exact-iteration estimate describes geometric decay, whereas the perturbed recursion supplies a limiting error bound. That bound alone does not establish vanishing error. The ambient space and perturbation assumptions therefore remain part of the interpretation of each result.

The role of strict contraction becomes clearer when these estimates are considered alongside results for nonexpansive mappings. The nonexpansive condition permits a Lipschitz bound of one, from which the strict-contraction geometric estimate cannot be obtained alone \cite{c3}. Thus, the geometric conclusion for exact contraction depends on more than a general requirement that a mapping not increase distances \cite{c1,c3}. The nonexpansive exposition discusses additional conditions for particular iteration schemes \cite{c3}. Together, these accounts distinguish two questions that shape convergence analysis. One concerns whether the mapping supplies strict contraction; the other concerns what error enters the iteration. Keeping these questions separate clarifies the assumptions supporting geometric distance estimates and bounds under bounded deterministic perturbations \cite{c1,c2,c3}.
```

Only source cards were supplied. The proof for c2 and the additional conditions discussed in c3 are unavailable. This fragment therefore makes no proof-level comparison or claim of a previously unaddressed gap.

Part 2

The title alone does not support a publication-ready abstract or a novelty claim. Please provide the concrete optimization problem and assumptions, what the algorithm changes relative to existing approaches, and the principal result with its supporting derivation or evaluation. For “fast,” include the runtime or convergence comparison and its conditions. These facts are needed to connect the contribution to a defensible conclusion.
