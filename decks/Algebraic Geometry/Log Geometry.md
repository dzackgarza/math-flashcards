---
title: "Algebraic Geometry::Log Geometry"
---

::: {.front card-id="log-structure-chart-characteristic" tags="definition construction example"}
Define a prelog structure, its associated log structure, a chart, and the characteristic monoid. Give the divisorial example.
:::

::: {.back card-id="log-structure-chart-characteristic"}
On $X_{\mathrm{et}}$, a prelog structure is a sheaf of commutative monoids $M$ with $\alpha:M\to(\mathcal O_X,\cdot)$. It is a log structure iff $\alpha^{-1}\mathcal O_X^*\to\mathcal O_X^*$ is an isomorphism.
$$M^a=\bigl(M\oplus_{\alpha^{-1}\mathcal O_X^*}\mathcal O_X^*\bigr)^{\mathrm{sh}},\qquad
\overline M=M/\mathcal O_X^*.$$
A chart is a monoid map $P\to\mathcal O_X$ whose associated log structure is $M$.

For a smooth variety with SNC divisor $D$ and $j:X\setminus D\hookrightarrow X$, the divisorial log structure is $\mathcal O_X\cap j_*\mathcal O_{X\setminus D}^*$. Near $D=(x_1\cdots x_r=0)$, chart $\mathbb N^r\to\mathcal O_X$, $e_i\mapsto x_i$. At a point on precisely $s$ branches, $\overline M_x\simeq\mathbb N^s$; away from $D$, $\overline M_x=0$.

Reference: Abramovich et al., *Logarithmic geometry and moduli*, §2.
:::

::: {.front card-id="log-fine-saturated" tags="definition comparison example"}
Define integral, fine, saturated, and sharp monoids. Apply them to charts of log schemes.
:::

::: {.back card-id="log-fine-saturated"}
For an additive commutative monoid $P$, with group completion $P^{\mathrm{gp}}$:

| Property | Criterion |
| --- | --- |
| Integral | $P\to P^{\mathrm{gp}}$ injective, equivalently cancellation |
| Fine | Integral and finitely generated |
| Saturated | Integral; $x\in P^{\mathrm{gp}}$, $nx\in P$ for some $n>0$ imply $x\in P$ |
| Sharp | Only invertible element is $0$ |

A log scheme is fine (resp. fine saturated, fs) if it has étale-local charts by fine (resp. fs) monoids. Characteristic monoids are sharp.

$\mathbb N^r$: fine, saturated, sharp. $\langle2,3\rangle\subset\mathbb Z$: fine, sharp, not saturated since $2\cdot1\in P$ but $1\notin P$; saturation $\mathbb N$.

Reference: Abramovich et al., *Logarithmic geometry and moduli*, §2.
:::

::: {.front card-id="log-smooth-node-chart" tags="definition construction example"}
State the chart criterion for log smoothness of fine log schemes. Explain why $xy=t$ is log smooth at the node.
:::

::: {.back card-id="log-smooth-node-chart"}
For a locally finitely presented morphism of fine log schemes $X\to Y$, log smoothness is equivalent to étale-local charts $Q\to P$ such that:

- $\ker(Q^{\mathrm{gp}}\to P^{\mathrm{gp}})$ and the torsion part of its cokernel are finite of orders invertible on $X$.
- $X\to Y\times_{\operatorname{Spec}\mathbb Z[Q]}\operatorname{Spec}\mathbb Z[P]$ is smooth.

For $xy=t$, use $Q=\mathbb N\to P=\mathbb N^2$, $1\mapsto(1,1)$, with $t$ on the base and $x,y$ upstairs. The group cokernel is $\mathbb Z$; the induced scheme map is an isomorphism. Thus log smooth, although the fiber at $t=0$ is singular. The central fiber is log smooth over the standard log point $\mathbb N\to k$, $1\mapsto0$.

Reference: Abramovich et al., *Logarithmic geometry and moduli*, Theorem 3.10.
:::

::: {.front card-id="log-polync-colored-dual" tags="definition construction example"}
Define a polync variety, its polysimplicial dual complex, and a coloring. Give a two-parameter semistable local model.
:::

::: {.back card-id="log-polync-colored-dual"}
Over $\mathbb C$, polync means étale-locally a product of normal-crossing spaces and a smooth factor:
$$\prod_{i\in I}\{x_{i1}\cdots x_{im_i}=0\}\times\mathbb A^a.$$
The dual complex has local cells $\prod_i\Delta^{m_i-1}$, glued along faces according to the strata. An $S$-coloring assigns a distinct color in $S$ to each simplex factor of each cell, compatibly on faces; edges in a factor have its color.

A semistable morphism over a smooth base has local equations $\prod_jx_{ij}=t_i$ in disjoint groups of coordinates, together with smooth coordinates. Example:
$$xy=s,\qquad uv=t.$$
The central fiber has four components; its local dual cell is a square $\Delta^1\times\Delta^1$, with horizontal and vertical edges differently colored. The total space is smooth. A polync space need not itself be a normal-crossing hypersurface.

Reference: [Engel, *Polync varieties*, §1](https://arxiv.org/abs/2601.21871).
:::

::: {.front card-id="log-polync-d-semistability" tags="definition comparison example"}
Define $d$-semistability for a colored polync variety. Relate it to smoothing and to the normal bundles in a two-component crossing.
:::

::: {.back card-id="log-polync-d-semistability"}
For an $S$-colored polync variety $X_0$, let $Z_s$ be the union of singular strata involving color $s$. The sheaf of local first-order smoothing parameters splits as
$$\mathcal T^1_{X_0}=\mathcal Ext^1(\Omega^1_{X_0},\mathcal O_{X_0})
=\bigoplus_{s\in S}\mathcal L_s,$$
where $\mathcal L_s$ is a line bundle on $Z_s$, pushed forward to $X_0$.

$d$-semistable means $\mathcal L_s\simeq\mathcal O_{Z_s}$ for every $s$. A semistable smoothing supplies these trivializations. Conversely this condition gives a log structure of semistable type; a global smoothing requires further hypotheses.

For $X_0=Y_1\cup_DY_2$ with smooth components and smooth transverse double locus, no triple locus:
$$\mathcal T^1_{X_0}|_D\simeq N_{D/Y_1}\otimes N_{D/Y_2}.$$
Thus a necessary condition for a smooth-total-space semistable smoothing is $N_{D/Y_2}\simeq N_{D/Y_1}^{-1}$.

Reference: [Engel, Definition 1.13 and Proposition 2.2](https://arxiv.org/abs/2601.21871).
:::
