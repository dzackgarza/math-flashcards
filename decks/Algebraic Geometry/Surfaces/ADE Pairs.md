---
title: "Algebraic Geometry::Surfaces::ADE Pairs"
---

::: {.front card-id="ade-pairs-shapes-branch-cover" tags="definition construction comparison"}
In Alexeev–Thompson's terminology, how do pure shapes, priming, and a branch divisor define an ADE or affine ADE pair? Distinguish this from an ADE surface singularity.
:::

::: {.back card-id="ade-pairs-shapes-branch-cover"}
Start with one of the pure surface–boundary pairs $(Y,C)$ in the polygon or nontoric constructions below, or a pair obtained from one by priming. Their polarization is the ample Cartier divisor
$$L=-2(K_Y+C).$$
An **ADE pair** (type III), or **affine ADE pair** (type II), adds $B\in|L|$ such that there exists $\epsilon_0>0$ for which $(Y,C+\frac{1+\epsilon}{2}B)$ is log canonical for every $0<\epsilon<\epsilon_0$. These pairs are stable since $K_Y+C+\frac{1+\epsilon}{2}B\sim_{\mathbb Q}\frac\epsilon2L$.

The associated double cover has branch data $B\sim-2(K_Y+C)$; its boundary $D$ is the reduced inverse image of $C$, and $K_X+D\sim0$. The decorated ADE symbol labels the **global shape**, not a claim that $Y$ has a single singularity of that name. Not every index-two log del Pezzo pair is one of these shapes.

Example: shape $A_1$ has $Y=\mathbb P^2$, $C$ two distinct lines, and $B$ a conic transverse to $C$ and avoiding their intersection. The double cover for smooth $B$ is a quadric surface.

Reference: Alexeev–Thompson, *ADE surfaces and their moduli*, Definitions 3.1–3.2 and Lemma 2.3.
:::

::: {.front card-id="ade-pure-toric-polygons" tags="construction definition"}
Give the polygon construction of the pure toric ADE shapes, including the distinguished point and boundary. What changes for affine shapes?
:::

::: {.back card-id="ade-pure-toric-polygons"}
Let $Y_P$ be the normal projective toric surface polarized by the lattice polygon $P\subset\mathbb Z^2$. Take $C$ to be the sum of boundary divisors for edges containing $p_*$. All other edges have lattice distance two from $p_*$, so $L_P=-2(K_{Y_P}+C)$.

| Shape | Range | $p_*$ | Vertices of $P$ |
| --- | --- | --- | --- |
| $A_{2n-1}$ | $n\ge1$ | $(0,2)$ | $(0,2),(0,0),(2n,0)$ |
| $A_{2n-2}^{-}$ | $n\ge1$ | $(0,2)$ | $(0,2),(0,0),(2n-1,0)$ |
| ${}^{-}A_{2n-3}^{-}$ | $n\ge2$ | $(0,2)$ | $(0,2),(1,0),(2n-1,0)$ |
| $D_{2n}$ | $n\ge2$ | $(2,2)$ | $(2,2),(0,2),(0,0),(2n-2,0)$ |
| $D_{2n-1}^{-}$ | $n\ge3$ | $(2,2)$ | $(2,2),(0,2),(0,0),(2n-3,0)$ |
| ${}^{-}E_6^{-}$ | — | $(2,2)$ | $(2,2),(0,3),(0,0),(3,0)$ |
| ${}^{-}E_7$ | — | $(2,2)$ | $(2,2),(0,3),(0,0),(4,0)$ |
| ${}^{-}E_8^{-}$ | — | $(2,2)$ | $(2,2),(0,3),(0,0),(5,0)$ |
| $\widetilde D_{2n}$ | $n\ge3$ | $(2,2)$ | $(0,2),(0,0),(2n-4,0),(4,2)$ |
| $\widetilde E_7$ | — | $(2,2)$ | $(0,4),(0,0),(4,0)$ |
| $\widetilde E_8^{-}$ | — | $(2,2)$ | $(0,3),(0,0),(6,0)$ |

For type III, $p_*$ is a vertex and $C$ has two sides. For the affine rows, $p_*$ lies inside an edge and $C$ has one side. The special shape $\widetilde D_4$ is instead $(\mathbb P^1\times\mathbb P^1,C)$ with $C$ a smooth $(1,1)$ curve, or a quadric cone with a smooth conic section avoiding the vertex.

Type III sides have $L\cdot C_i=2$ (long) or $1$ (short); type II sides have degree $4$ (long) or $3$ (short). A minus on the corresponding end of a symbol marks a short side. For instance $A_1$ uses $2\Delta_2$, giving $Y=\mathbb P^2$, $L=2H$, and two lines as boundary.

Reference: Alexeev–Thompson, Table 1 and Definitions 3.5–3.6.
:::

::: {.front card-id="ade-pure-nontoric-affine-shapes" tags="construction definition"}
Construct the nontoric pure affine $A$ shapes. Specify the surface, boundary, and branch system.
:::

::: {.back card-id="ade-pure-nontoric-affine-shapes"}
In each case $B\in|-2(K_Y+C)|$ must satisfy the log-canonicity condition for the pair.

| Shape | Construction |
| --- | --- |
| $\widetilde A_{2n-1}$, $n\ge1$ | Choose an elliptic curve $E$ and a degree-$n$ line bundle $F$. Contract the negative section of $\mathbb P_E(\mathcal O\oplus F)$ to obtain $Y$. Take $C=0$. Then $K_Y^2=n$, and $B\in|-2K_Y|$. |
| $\widetilde A_1^*$ | $Y=\mathbb P^2$, $C$ a smooth conic, $B$ a conic. Also include the degeneration $Y=\mathbb P(1,1,4)$: $C$ a section avoiding the vertex, of weighted degree $4$, and $B$ another such section. |
| $\widetilde A_0^{-}$ | $Y=\mathbb P(1,1,2)$. On its resolution $\mathbb F_2$, with negative section $s$ and fiber $f$, the strict transform of $C$ is a smooth member of $|s+3f|$. Thus $C$ passes through the vertex. Take $B$ a hyperplane section of the quadric cone avoiding the vertex. |

For $\widetilde A_1^*$ with smooth $B$, the double cover is $\mathbb P^1\times\mathbb P^1$. For $\widetilde A_0^{-}$ it is $\mathbb P^2$ with involution $[x:y:z]\mapsto[x:-y:z]$ and a smooth invariant cubic as boundary. Smoothing the corner of the two boundary lines in shape $A_1$ gives the conic boundary of $\widetilde A_1^*$.

Reference: Alexeev–Thompson, §3B.
:::

::: {.front card-id="ade-priming-operation" tags="definition construction"}
Define priming of an ADE surface–boundary pair. Which infinitesimal data are chosen, and which positivity condition permits the final contraction?
:::

::: {.back card-id="ade-priming-operation"}
Choose distinct points $P_i$ smooth on both $Y$ and $C$, and length-two subschemes supported there with tangent direction transverse to $C$. Locally take $C=(x=0)$ and ideal $(y,x^2)$.

1. Blow up $P_i$, then the point on the exceptional curve representing the chosen transverse direction.
2. Contract the strict transform of the first exceptional curve, now a $(-2)$-curve. This weighted blowup $f:Y'\to Y$ has an $A_1$ singularity on the strict transform $C'$.
3. Require $L'=-2(K_{Y'}+C')$ to be big, nef, and semiample. Its ample model is
$$\overline Y'=\operatorname{Proj}\bigoplus_{m\ge0}H^0(Y',mL'),\qquad \overline C'=g_*C'.$$
The pair $(\overline Y',\overline C')$ is the priming. Thus choosing arbitrary points and blowing up once is not the operation.

For a pair with branch curve $B$, choose $P_i\in B\cap C$ and the tangent direction of $B$; transversality makes the direction admissible. On the double cover this corresponds to blowing up the associated boundary–ramification points, then taking the ample model.

Reference: Alexeev–Thompson, Definition 3.13 and §3C.
:::
