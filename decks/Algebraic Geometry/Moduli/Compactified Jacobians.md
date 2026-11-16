---
title: "Algebraic Geometry::Moduli::Compactified Jacobians"
---

::: {.front card-id="jacobian-rank-one-torsion-free" tags="definition comparison example"}
For a reduced projective nodal curve $C$, define a rank-one torsion-free sheaf and its degree. Give a sheaf allowed in a compactified Jacobian but absent from $\operatorname{Pic}(C)$.
:::

::: {.back card-id="jacobian-rank-one-torsion-free"}
Rank one: generic rank one on every irreducible component. Torsion-free: no nonzero subsheaf supported at finitely many points; equivalently pure of dimension one.
$$\deg F=\chi(F)-\chi(\mathcal O_C).$$
For a line bundle, this agrees with its usual total degree. At a smooth point, a rank-one torsion-free sheaf is locally free; at a node it need not be.

Example: $I_p$ at a node $p$. In $k[[x,y]]/(xy)$, the ideal $(x,y)$ has generic rank one on both branches, no zero-dimensional subsheaf, but is not principal. From $0\to I_p\to\mathcal O_C\to k(p)\to0$, $\deg I_p=-1$ over algebraically closed $k$.

Reference: [Alexeev, *Compactified jacobians*, §1](https://arxiv.org/abs/alg-geom/9608012).
:::

::: {.front card-id="jacobian-stability-multidegree" tags="definition comparison formula"}
Define the polarization-dependent stability and equivalence relation used in a compactified Jacobian of a nodal curve. Distinguish total degree from multidegree.
:::

::: {.back card-id="jacobian-stability-multidegree"}
Fix ample $L$ on $C=\bigcup C_i$, $\lambda_i=\deg(L|_{C_i})>0$. For a pure sheaf $E$ of multirank $(r_i)$:
$$P_E(n)=\Bigl(\sum_i\lambda_i r_i\Bigr)n+\chi(E),\qquad
\mu_L(E)=\frac{\chi(E)}{\sum_i\lambda_i r_i}.$$
$F$ stable (semistable) iff every nonzero proper subsheaf $E\subset F$ satisfies $\mu_L(E)<\mu_L(F)$ (respectively $\le$).

$\overline J^{d,L}(C)$ parametrizes S-equivalence classes of semistable rank-one torsion-free sheaves of total degree $d$. S-equivalence means isomorphic associated graded objects for Jordan–Hölder filtrations with stable factors of the same slope.

Multidegree: degrees on components after restriction and removal of zero-dimensional torsion. For line bundles these sum to total degree. For sheaves not locally free at nodes between components, correction terms occur; use $\chi(F)-\chi(\mathcal O_C)$ for total degree. Changing $L$ changes the inequalities on subcurves.

Reference: [Alexeev, Definitions 1.4–1.11](https://arxiv.org/abs/alg-geom/9608012).
:::

::: {.front card-id="jacobian-compact-type-normalization" tags="definition construction example"}
Relate partial normalization, the dual graph, and compact type for a connected projective nodal curve over an algebraically closed field.
:::

::: {.back card-id="jacobian-compact-type-normalization"}
Normalize a chosen set of nodes: replace each by its two branches. Full normalization is $\widetilde C=\coprod C_i^\nu$. The dual graph $\Gamma$ has one vertex per component and one edge per node, including loops for self-nodes.
$$p_a(C)=\sum_i g(C_i^\nu)+b_1(\Gamma),\qquad
1\to\mathbb G_m^{b_1(\Gamma)}\to\operatorname{Pic}^0(C)
\to\prod_i\operatorname{Pic}^0(C_i^\nu)\to0.$$
Compact type $\iff\Gamma$ a tree $\iff$ every node separating $\iff\operatorname{Pic}^0(C)$ an abelian variety. Then the displayed map identifies it with the product of the component Jacobians.

Examples: $C_1\cup_pC_2$ has compact type and genus $g_1+g_2$. An irreducible one-nodal curve has a loop and a $\mathbb G_m$ factor; its generalized Jacobian is not proper.

Reference: Alexeev, *Compactified jacobians*, §2; Alexeev–Kuznetsov, *Augmentations, reduced ideal point gluings and compact type degenerations of curves*, §1.3.
:::
