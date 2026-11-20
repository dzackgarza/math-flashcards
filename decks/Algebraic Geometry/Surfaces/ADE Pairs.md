---
title: "Algebraic Geometry::Surfaces::ADE Pairs"
---

::: {.front card-id="ade-weyl-parameter-spaces" tags="theorem comparison example" cite="[@AT17, §5; @Loo76; @AEGS25, §§6.1 and 6.3]"}
Explain the torus/Weyl and elliptic/Weyl parameter spaces behind type III and type II ADE families. Specify the lattices and give rank-one examples.
:::

::: {.back card-id="ade-weyl-parameter-spaces"}
Let $Q$ be an ADE root lattice of rank $r$, $P=Q^*$ its weight lattice, and $W$ its Weyl group.

| Construction | Coarse quotient | Rank-one example |
| --- | --- | --- |
| Multiplicative: $T_P=\operatorname{Hom}(P,\mathbb C^\times)$ | $T_P/W\simeq\mathbb A^r$ | $t\mapsto t+t^{-1}$ identifies $\mathbb C^\times/(t\leftrightarrow t^{-1})$ with $\mathbb A^1$ |
| Elliptic: $E\otimes Q^\vee=\operatorname{Hom}(P,E)$ | Weighted projective space with weights $(1,a_1^\vee,\ldots,a_r^\vee)$ | $E/(p\leftrightarrow-p)\simeq\mathbb P^1$ |

Here $a_i^\vee$ are the coefficients of the coroot of the highest root in the simple-coroot basis. For simply-laced types they are the highest-root coefficients. The multiplicative invariant coordinates are the fundamental characters. Root, weight, and intermediate lattices give isogenous tori, not interchangeable moduli problems; shape symmetries can impose further finite quotients.

The type III polynomial coefficients in the normalized ADE family are coordinates on the affine quotient. In type II, fix the boundary elliptic curve $E$; the polynomial coefficients are homogeneous coordinates with the following weights:

| Type | Weighted projective parameter space |
| --- | --- |
| $\widetilde E_7$ | $\mathbb P(1,1,2,2,2,3,3,4)$ |
| $\widetilde E_8$ | $\mathbb P(1,2,2,3,3,4,4,5,6)$ |
| $\widetilde D_{2n}$ | $\mathbb P(1,1,1,1,2^{,2n-3})$ |

In the last row $2^{,2n-3}$ denotes repeated weights. Varying $E$ adds the elliptic modulus. A weighted projective coarse space does not by itself identify a quotient stack or supply a universal family on that coarse space.
:::

::: {.front card-id="ade-theta-sections-elliptic-cone" tags="construction calculation" cite="[@AEGS25, §6.3 and §6.6, with analytic theta sections on an elliptic curve]"}
Construct theta-function sections of an even-degree line bundle on $E_q=\mathbb C^\times/q^{\mathbb Z}$. How does inversion constrain an invariant branch section, and how does this enter the affine $A$ surface construction?
:::

::: {.back card-id="ade-theta-sections-elliptic-cone"}
Fix $0<|q|<1$, a choice of its fractional powers, and even $d=2n>0$. For $i\in\mathbb Z/d$, put
$$\theta_i(x)=\sum_{k\equiv i\ (d)}q^{k^2/(2d)}x^k.$$
The series converge normally on compact subsets of $\mathbb C^\times$. Reindexing gives
$$\theta_i(qx)=q^{-d/2}x^{-d}\theta_i(x),\qquad
\theta_i(x^{-1})=\theta_{-i}(x).$$
The common factor of automorphy defines a degree-$d$ line bundle $M$. Distinct residue classes give independent Laurent series; $h^0(E_q,M)=d$ by Riemann–Roch, so they form a basis. A section $g=\sum c_i\theta_i$ is invariant under the chosen inversion lift iff $c_i=c_{-i}$.

Choose a square root $L$ of $M$, of degree $n$. On $\mathbb P_E(\mathcal O\oplus L)$, with $y$ the local fiber coordinate of $L$, the expression $y^2+g$ defines a quadratic section. Contract the negative section to the cone over $(E,L)$ and take the associated double cover, locally
$$z^2+y^2+g(x)=0.$$
The deck involution changes the sign of $z$; an additional involution requires a compatible lift on $L$ and the coefficient symmetry. General branch sections give the affine $A$ pairs; special sections must still satisfy the lc condition.

This theta normalization makes the factor of automorphy explicit; multiplying by a nowhere-zero factor or changing the chosen line bundle changes the displayed series.
:::

::: {.front card-id="ade-geometric-folding-quotient-pairs" tags="construction comparison" cite="[@AEGS25, Proposition 6.1 and §§6.5–6.6]"}
What data and calculations turn a symmetry of an ADE diagram into geometric folding of a surface pair? Compare a torus-sign involution with a polytope-reflection involution.
:::

::: {.back card-id="ade-geometric-folding-quotient-pairs"}
Start with a polarized anticanonical ADE pair $(X,D+\epsilon R)$, its deck involution $d$, and a commuting nonsymplectic involution $a$ preserving $D,R$. Require the finite-fixed-locus conditions of the quotient construction, including the induced involution on $Y=X/d$. Then $b=da$ is symplectic and
$$Z=X/a,\quad Z'=X/b,\quad W=X/\langle d,a\rangle.$$
The quotient boundaries satisfy $D=q^*D_Z$, $R=q^*R_Z$ when there is no ramification along these divisors. The two log volume-form characters give
$$2(K_Z+D_Z)\sim0,\quad K_Z+D_Z\not\sim0,\qquad K_{Z'}+D_{Z'}\sim0.$$
For $\rho:Z\to W$, with boundary $C_W$ and branch divisor $B_W$:
$$K_Z+D_Z+\epsilon R_Z=\rho^*\bigl(K_W+C_W+\tfrac{1+\epsilon}{2}B_W\bigr).$$

| Involution in local toric coordinates | Computation |
| --- | --- |
| $a(x,y,z)=(-x,-y,-z)$ | Keep exponents with $i+j+k$ even; use the same polytope in this index-two character sublattice. Recompute primitive normals and boundary ramification. |
| $a(x,y,z)=(x^{-1},-y,-z)$ | Require the Laurent equation to be invariant under $x\leftrightarrow x^{-1}$. Paired coefficients agree; solve the fixed-point equations and resolve their quotient singularities. |

At an isolated fixed point of the base involution outside the branch curve, the two points in its double-cover fiber are either exchanged or both fixed by a lift. Multiplying by the deck involution exchanges these alternatives, explaining complementary isolated branch loci of $Z$ and $Z'$ over $W$.

A folded graph records the lattice symmetry; the equation, fixed loci, Cartier indices, and branch calculations establish the quotient surface pair.
:::

::: {.front card-id="ade-folded-quadric-worked-example" tags="application calculation" cite="[@AEGS25, Example 6.3 and Proposition 6.1]"}
For $Y=\mathbb P^1\times\mathbb P^1$, let $C$ be a fiber of each ruling and $B$ a smooth invariant $(2,2)$ curve avoiding torus-fixed points and the corner of $C$. Construct the anticanonical double cover and its two quotients above $W=Y/((x,y)\mapsto(-x,-y))$.
:::

::: {.back card-id="ade-folded-quadric-worked-example"}
Here $K_Y+C=(-1,-1)$ and $B\sim-2(K_Y+C)$. The cover $X:z^2+f_{2,2}=0$ has $D=\pi^{-1}C$, ramification $R$, and
$$K_X+D\sim0,\qquad R=\pi^*\mathcal O_Y(1,1),\qquad R^2=4.$$
Choose $C$ as the two toric sides at the distinguished corner. Then $D$ has two rational components. Each meets $R$ in two points.

The square polygon for $B$ has vertices $(0,0),(2,0),(0,2),(2,2)$. Passing from $\mathbb Z^2$ to $\{(i,j):i+j\text{ even}\}$ gives $W$. At each corner its local ring is $\mathbb C[s^2,st,t^2]$, hence $W$ has four $A_1$ points.

The two lifts differ by $z\mapsto-z$. Their signs on the fiber change between toric charts because $z$ belongs to $\mathcal O_Y(1,1)$. Each lift fixes points over two of the four base corners and exchanges the points over the other two. The lifts have opposite log-volume characters; the nonsymplectic quotient $Z$ has log canonical index two, while the symplectic quotient $Z'$ has index one. Their isolated branch loci over $W$ are complementary pairs of corners.

For either quotient $q:X\to Z$ or $Z'$, $q^*R_Z=R$ and $R_Z^2=2$. This is the basic folded $D_4$ construction: the index-two quotient is the $B_2$ surface shape. The shape describes the global pair, not one local $B_2$ singularity.
:::

::: {.front card-id="ade-pairs-shapes-branch-cover" tags="definition construction comparison" cite="[@AT17, Definitions 3.1–3.2 and Lemma 2.3; @AEGS25, §6, equation (6.1), and §7]"}
In Alexeev–Thompson's terminology, how do pure shapes, priming, and a branch divisor define an ADE or affine ADE pair? Distinguish this from an ADE surface singularity.
:::

::: {.back card-id="ade-pairs-shapes-branch-cover"}
Start with one of the pure surface–boundary pairs $(Y,C)$ in the polygon or nontoric constructions below, or a pair obtained from one by priming. Their polarization is the ample Cartier divisor
$$L=-2(K_Y+C).$$
An **ADE pair** (type III), or **affine ADE pair** (type II), adds $B\in|L|$ such that there exists $\epsilon_0>0$ for which $(Y,C+\frac{1+\epsilon}{2}B)$ is log canonical for every $0<\epsilon<\epsilon_0$. These pairs are stable since $K_Y+C+\frac{1+\epsilon}{2}B\sim_{\mathbb Q}\frac\epsilon2L$.

The associated double cover has branch data $B\sim-2(K_Y+C)$; its boundary $D$ is the reduced inverse image of $C$, and $K_X+D\sim0$. The decorated ADE symbol labels the **global shape**, not a claim that $Y$ has a single singularity of that name. Not every index-two log del Pezzo pair is one of these shapes.

Example: shape $A_1$ has $Y=\mathbb P^2$, $C$ two distinct lines, and $B$ a conic transverse to $C$ and avoiding their intersection. The double cover for smooth $B$ is a quadric surface.

For the cover $\pi:X\to Y$ with ramification divisor $R$:
$K_X+D+\epsilon R=\pi^*\!\left(K_Y+C+\tfrac{1+\epsilon}{2}B\right).$
Thus the branch pair and its anticanonical double cover give the two descriptions of the same component used in stable degenerations.
:::

::: {.front card-id="ade-pure-toric-polygons" tags="construction definition" cite="[@AT17, Table 1 and Definitions 3.5–3.6]"}
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
:::

::: {.front card-id="ade-pure-nontoric-affine-shapes" tags="construction definition" cite="[@AT17, §3B]"}
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
:::

::: {.front card-id="ade-priming-operation" tags="definition construction" cite="[@AT17, Definition 3.13 and §3C]"}
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
:::
