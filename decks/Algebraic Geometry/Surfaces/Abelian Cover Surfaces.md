---
title: "Algebraic Geometry::Surfaces::Abelian Cover Surfaces"
---

::: {.front card-id="surfaces-classical-campedelli" tags="definition construction example"}
Construct a classical Campedelli surface as an abelian cover. Distinguish the construction from the numerical invariants.
:::

::: {.back card-id="surfaces-classical-campedelli"}
Over $\mathbb C$, choose seven lines $D_g\subset\mathbb P^2$, labeled by $0\ne g\in G=(\mathbb Z/2)^3$, with no three concurrent. For every nontrivial character $\chi$, take
$$L_\chi=\mathcal O_{\mathbb P^2}(2),\qquad
2L_\chi\sim\sum_{\chi(g)=-1}D_g.$$
There are four lines in each sum. The standard $G$-cover is smooth: at every crossing the two distinct labels are independent.
$$K_X=\pi^*\!\left(-3H+\tfrac72H\right)=\tfrac12\pi^*H,\qquad K_X^2=8/4=2.$$
Also $\pi_*\mathcal O_X=\mathcal O\oplus\mathcal O(-2)^{\oplus7}$, so $p_g=q=0$.

A numerical Campedelli surface is a minimal surface of general type with $p_g=q=0$, $K^2=2$. These invariants alone do not identify the classical cover construction.

Reference: Alexeev–Pardini, *Explicit compactifications of moduli spaces of Campedelli and Burniat surfaces*, §3.
:::

::: {.front card-id="surfaces-primary-burniat" tags="definition construction"}
Give explicit branch data for a primary Burniat surface. Recover $K^2$ from the bidouble cover.
:::

::: {.back card-id="surfaces-primary-burniat"}
Let $Y=\operatorname{Bl}_{p_1,p_2,p_3}\mathbb P^2$, with noncollinear $p_i$, exceptional curves $E_i$, and strict transforms $L_{ij}$ of the triangle sides. Choose two further lines through each $p_i$, avoiding the other vertices; denote their strict transforms by $M_{i1},M_{i2}$.

Indices cyclic modulo three; label the branch divisors by the three nonzero elements of $(\mathbb Z/2)^2$:
$$D_i=E_i+L_{i+1,i+2}+M_{i+1,1}+M_{i+1,2}.$$
Require distinct lines and no triple intersection away from the $p_i$. Each $D_i$ has disjoint smooth components; each $D_i+D_j$ is twice a Picard class. Construct the standard bidouble cover.
$$D_1+D_2+D_3\sim-3K_Y,\qquad
K_X=\pi^*(K_Y+\tfrac12D)=-\tfrac12\pi^*K_Y,\qquad K_X^2=6.$$
This is the primary Burniat construction; $p_g=q=0$. The branch configuration, not just these invariants, defines the family.

Reference: Alexeev, *Divisors on Burniat surfaces*, §1; Alexeev–Hu, *Explicit KSBA compactifications of moduli spaces of secondary and tertiary Burniat surfaces*, §2.
:::

::: {.front card-id="surfaces-secondary-tertiary-burniat" tags="definition construction comparison"}
How do secondary and tertiary Burniat surfaces arise from the primary branch arrangement? What distinguishes nodal degree four?
:::

::: {.back card-id="surfaces-secondary-tertiary-burniat"}
Specialize the six interior lines so that $n$ points away from the triangle lie on three interior lines, one of each branch color. Blow up those points on $Y=\operatorname{Bl}_3\mathbb P^2$; use the strict transforms of the branch curves, **without** the new exceptional curves, for the bidouble cover of $Y'$.
$$D'\sim-3K_{Y'},\qquad K_{X'}=-\tfrac12\pi^*K_{Y'},\qquad K_{X'}^2=6-n.$$

| $n$ | Name | Degree |
| --- | --- | --- |
| $1$ | Secondary | $5$ |
| $2$ | Secondary | $4$ |
| $3$ | Tertiary | $3$ |

An interior curve passing through two blown-up triple points has strict-transform square $-2$. Its reduced preimage is also a $(-2)$-curve; contract these curves to obtain the canonical model. For degree four, the two triple points lying on one interior branch curve give the nodal family; otherwise the family is nonnodal.

Reference: Alexeev–Hu, *Explicit KSBA compactifications of moduli spaces of secondary and tertiary Burniat surfaces*, §2.
:::

::: {.front card-id="surfaces-index-two-involution-pairs" tags="definition comparison construction"}
Define the index-at-most-two log del Pezzo pairs used in ADE degenerations and their associated polarized involution pairs.
:::

::: {.back card-id="surfaces-index-two-involution-pairs"}
Over $\mathbb C$, $Y$ normal, $C$ reduced, $(Y,C)$ lc:
$$L=-2(K_Y+C)\ \text{Cartier and ample},\qquad
B\in|L|\ \text{reduced},\qquad
(Y,C+\tfrac{1+\epsilon}{2}B)\ \text{lc for every }0<\epsilon<\epsilon_0$$
for some $\epsilon_0>0$.

The associated double cover has involution $\iota$, reduced boundary $D$, and ramification divisor $R$:
$$K_X+D\sim0\ \text{Cartier},\qquad R\ \text{ample Cartier},\qquad
(X,D+\epsilon R)\ \text{lc}.$$
The fixed locus is $R$ together with possibly isolated points. The construction uses the reflexive rank-one sheaf $\mathcal O_Y(K_Y+C)$ with its square identified with $\mathcal O_Y(-B)$; form its double-cover algebra. This works even when $K_Y+C$ is not Cartier.

“Index at most two” concerns Cartier divisibility of $K_Y+C$, not the Fano index of $Y$.

Reference: Alexeev–Thompson, *ADE surfaces and their moduli*, §2.
:::
