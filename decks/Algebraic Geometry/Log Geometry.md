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

::: {.front card-id="log-normal-crossing-d-semistability" tags="definition comparison example"}
Define $d$-semistability for a normal-crossing variety. What normal-bundle condition does it impose on a two-component crossing?
:::

::: {.back card-id="log-normal-crossing-d-semistability"}
For a normal-crossing variety $X_0/\mathbb C$ with singular locus $D$, the sheaf of local first-order smoothing parameters is
$$\mathcal T^1_{X_0}=\mathcal Ext^1(\Omega^1_{X_0},\mathcal O_{X_0}),$$
an invertible sheaf on $D$. The variety is $d$-semistable iff $\mathcal T^1_{X_0}\simeq\mathcal O_D$.

A semistable smoothing with smooth total space supplies a nowhere-zero smoothing parameter, hence this trivialization. This necessary condition alone does not assert global smoothability.

For $X_0=Y_1\cup_DY_2$ with smooth components, smooth transverse double locus, and no triple locus:
$$\mathcal T^1_{X_0}|_D\simeq N_{D/Y_1}\otimes N_{D/Y_2}.$$
Thus $d$-semistability means $N_{D/Y_2}\simeq N_{D/Y_1}^{-1}$. Local example: $xy=t$ smooths $xy=0$; changing the local equations $x,y$ multiplies the parameter by the product of their transition units, explaining the tensor product.

Reference: Abramovich et al., *Logarithmic geometry and moduli*, §5.
:::
