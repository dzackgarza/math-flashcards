---
title: "Algebraic Geometry::Moduli::Hurwitz and Prym"
---

::: {.front card-id="hurwitz-data-monodromy" tags="definition construction example"}
What data specify a Hurwitz space of covers of $\mathbb P^1$? Express connectedness and branching through monodromy.
:::

::: {.back card-id="hurwitz-data-monodromy"}
Fix degree $d$, branch conjugacy classes $C_1,\ldots,C_b\subset S_d$, and conventions for labeling branch points and identifying targets. The Hurwitz space parametrizes finite covers $C\to\mathbb P^1$ with smooth connected source and that branch data, up to the prescribed isomorphisms.

For ordered distinct branch points and chosen loops:
$$\sigma_i\in C_i,\qquad \sigma_1\cdots\sigma_b=1,\qquad
\langle\sigma_1,\ldots,\sigma_b\rangle\text{ transitive on }[d].$$
Simultaneous conjugation relabels sheets; braiding the branch points changes the tuple by Hurwitz moves. Unlabeling branch points and quotienting the target by $\operatorname{PGL}_2$ are additional quotients.

Riemann–Hurwitz gives
$$2g(C)-2=-2d+\sum_i\bigl(d-\#\text{cycles}(\sigma_i)\bigr).$$
For the $W(E_6)$ degree-$27$ action, a reflection has six transpositions and fifteen fixed points. With $24$ such branch points, $2g-2=-54+144=90$, hence $g=46$.

Reference: Alexeev–Donagi–Farkas–Izadi–Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, §1.
:::

::: {.front card-id="hurwitz-admissible-cover" tags="definition local-model"}
Define an admissible cover of nodal curves over $\mathbb C$. State the node condition and its family equation.
:::

::: {.back card-id="hurwitz-admissible-cover"}
A finite map $\pi:C\to P$ of connected nodal projective curves, with stable marked target, is admissible with specified branch profiles when:

- Nodes of $C$ are exactly preimages of nodes of $P$.
- Away from nodes and marked branch points it is étale; over marked points it has the prescribed profiles.
- At each source node over a target node, both branches have the **same** ramification index $e$:
$$k[[x,y]]/(xy)\longrightarrow k[[u,v]]/(uv),\qquad x\mapsto u^e,\quad y\mapsto v^e.$$

In a smoothing, $uv=s$, $xy=t$, and $t=s^e$. Thus one branch cannot have index two and the other index three. A Galois admissible cover additionally carries the specified deck-group action.

Reference: Alexeev–Donagi–Farkas–Izadi–Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, admissible-cover compactification.
:::

::: {.front card-id="prym-correspondence-exponent" tags="definition comparison example"}
Define the endomorphism induced by a curve correspondence, a Prym variety, and a Prym–Tyurin variety of exponent $e$.
:::

::: {.back card-id="prym-correspondence-exponent"}
For a smooth projective complex curve $C$ and correspondence $Z\subset C\times C$ finite over both factors:
$$D_Z:\operatorname{Pic}^0C\to\operatorname{Pic}^0C,\qquad
L\mapsto\operatorname{Nm}_{p_2}(p_1^*L).$$
Extend additively to correspondence cycles.

For a finite map $f:C\to B$, its Prym is
$$P(C/B)=\ker(\operatorname{Nm}_f:JC\to JB)^0.$$
The superscript takes the identity component. For a connected étale double cover, $\Theta_C|_P=2\Xi$ with $\Xi$ principal; the restricted polarization itself is not principal.

A Prym–Tyurin variety of exponent $e$ is an abelian subvariety $P\subset JC$ with principal polarization $\Xi$ such that $\Theta_C|_P\equiv e\Xi$.

In the $E_6$ construction, $(D-1)(D+5)=0$ and
$$P=\operatorname{im}(D-1)=\ker(D+5)^0,\qquad \Theta_C|_P=6\Xi.$$

Reference: Alexeev–Donagi–Farkas–Izadi–Ortega, *The uniformization of the moduli space of principally polarized abelian 6-folds*, §1.
:::

::: {.front card-id="hurwitz-isotypical-hodge" tags="definition construction"}
Define the isotypical Hodge bundles for a family of Galois covers. Distinguish an isotypical summand from its multiplicity bundle.
:::

::: {.back card-id="hurwitz-isotypical-hodge"}
For a smooth proper family of complex curves $f:\widetilde{\mathcal C}\to S$ with fiberwise $G$-action, put $\widetilde{\mathbb E}=f_*\omega_{\widetilde{\mathcal C}/S}$. For an irreducible complex representation $V_\rho$:
$$\mathbb E_\rho=\operatorname{Hom}_G(V_\rho,\widetilde{\mathbb E}),\qquad
\widetilde{\mathbb E}\simeq\bigoplus_\rho V_\rho\otimes\mathbb E_\rho.$$
$\mathbb E_\rho$ is the multiplicity bundle; $V_\rho\otimes\mathbb E_\rho$ is the isotypical summand. Define $\lambda_\rho=c_1(\mathbb E_\rho)$, so
$$c_1(\widetilde{\mathbb E})=\sum_\rho(\dim V_\rho)\lambda_\rho.$$
For a double cover this is the invariant/anti-invariant splitting; the anti-invariant part corresponds to Prym differentials. Stable curves use the relative dualizing sheaf.

Reference: Alexeev–Donagi–Farkas–Izadi–Ortega, *Hodge classes on the moduli space of $W(E_6)$-covers and the geometry of $\mathcal A_6$*, §3.
:::
