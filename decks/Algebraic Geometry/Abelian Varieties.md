---
title: "Algebraic Geometry::Abelian Varieties"
---

::: {.front card-id="abelian-minimal-hodge-classes" tags="definition comparison formula example"}
For a complex principally polarized abelian $g$-fold $(A,\Theta)$, define the minimal class in codimension $k$. Compare integral algebraicity, rational algebraicity, and effective representability.
:::

::: {.back card-id="abelian-minimal-hodge-classes"}
Write $\theta=c_1(\Theta)$ and $0\le k\le g$:
$$\theta_k=\frac{\theta^k}{k!}\in H^{2k}(A,\mathbb Z)\cap H^{k,k}(A).$$
This class is integral and primitive: in a symplectic basis $\theta=\sum_i a_i\wedge b_i$, division by $k!$ leaves a sum of distinct basis wedges with coefficient one.

- Integral algebraic: in the image of $\operatorname{CH}^k(A)\to H^{2k}(A,\mathbb Z)$; cycles allow negative coefficients.
- Rational algebraic: in the image after tensoring with $\mathbb Q$. Here $k!\theta_k=\theta^k$ is algebraic, so rational algebraicity is automatic.
- Effective representability asks for a cycle with nonnegative integral coefficients; it is stronger.

The integers $m$ with $m\theta_k$ algebraic form $a_k\mathbb Z$, where $a_k>0$ and $a_k\mid k!$. For a smooth genus-$g$ curve embedded in its Jacobian, $[C]=\theta_{g-1}$. Hence $\Theta\cdot C=g$; in general a curve class $m\theta_{g-1}$ has theta degree $mg$.

References: Engel–de Gaay Fortman–Schreieder, *Matroids and the integral Hodge conjecture for abelian varieties*, §1; Engel–Sertöz, *On the degree of subvarieties of abelian varieties*, §1.
:::

::: {.front card-id="abelian-monodromy-cone-nilpotent-orbit" tags="definition construction example"}
For a family of principally polarized abelian varieties over $(\Delta^*)^r$ with unipotent monodromy, define the monodromy cone and describe the nilpotent-orbit approximation in Siegel coordinates.
:::

::: {.back card-id="abelian-monodromy-cone-nilpotent-orbit"}
Choose an adapted symplectic basis so the commuting monodromies act on period matrices by $\tau\mapsto\tau+B_i$, with $B_i$ integral symmetric positive semidefinite. The monodromy cone is
$$\sigma=\sum_i\mathbb R_{\ge0}B_i,$$
defined up to simultaneous integral change of basis $B_i\mapsto AB_iA^t$. Coordinate-free: $B_i(x,y)=L(N_ix,y)$ on the weight-zero quotient of the homology lattice, where $N_i=\log T_i$ and $L$ is the polarization pairing.

Put $t_i=e^{2\pi iz_i}$. The untwisted period map $\Psi(t)=\tau(z)-\sum_i z_iB_i$ extends to the origin in the compact dual. The nilpotent orbit replaces it by its limit:
$$\tau_{\mathrm{nilp}}(z)=\Psi(0)+\sum_i z_iB_i.$$
It lies in Siegel space when every $\operatorname{Im}z_i$ is large enough. For a one-node curve degeneration, $B=e^*\otimes e^*$, with $e^*$ the graph coedge. A separating node has $e^*=0$ and contributes no abelian monodromy.

Reference: Engel–de Gaay Fortman–Schreieder, *A survey of the Mumford construction*, Definitions 2.6–2.8.
:::

::: {.front card-id="abelian-polarization-type" tags="definition comparison example"}
Define a polarization, its type, and a principal polarization on a complex abelian variety. Distinguish a polarization from a chosen theta divisor.
:::

::: {.back card-id="abelian-polarization-type"}
For $A/\mathbb C$ abelian and $L$ ample:
$$\lambda_L:A\to\widehat A=\operatorname{Pic}^0(A),\qquad
a\mapsto t_a^*L\otimes L^{-1}.$$
A polarization is the isogeny $\lambda_L$ induced by such an $L$. Twisting by $\operatorname{Pic}^0(A)$ leaves it unchanged.

The alternating Riemann form on $H_1(A,\mathbb Z)$ has elementary divisors $d_1\mid\cdots\mid d_g$, $d_i>0$. Its **type** is $(d_1,\ldots,d_g)$:
$$\ker\lambda_L\simeq\prod_i(\mathbb Z/d_i)^2,\quad
\deg\lambda_L=(\prod_i d_i)^2,\quad h^0(A,L)=\prod_i d_i.$$
Principal means $\lambda_L$ is an isomorphism, equivalently all $d_i=1$. A theta divisor is an effective divisor representing a principal polarization; the polarization itself does not choose its translate.

On an elliptic curve, $\mathcal O_E(d[0])$ has type $(d)$; $\mathcal O_E([0])$ is principal.
:::

::: {.front card-id="abelian-siegel-torelli" tags="definition construction"}
Define Siegel upper half-space, $\mathcal A_g$, and the Torelli morphism. What does the polarization contribute?
:::

::: {.back card-id="abelian-siegel-torelli"}
$$\mathfrak H_g=\{\tau\in M_g(\mathbb C):\tau^T=\tau,\ \operatorname{Im}\tau>0\},\qquad
A_\tau=\mathbb C^g/(\mathbb Z^g+\tau\mathbb Z^g).$$
The standard symplectic form on the lattice defines a principal polarization. The group $\operatorname{Sp}_{2g}(\mathbb Z)$ acts by
$$\begin{pmatrix}A&B\\C&D\end{pmatrix}\tau=(A\tau+B)(C\tau+D)^{-1}.$$
Its analytic quotient stack is the moduli stack $\mathcal A_g$ of principally polarized abelian varieties; the orbit space is its coarse moduli space.

The Torelli morphism sends
$$\mathcal M_g\longrightarrow\mathcal A_g,\qquad
C\longmapsto(\operatorname{Pic}^0C,\Theta_C).$$
Here $\Theta_C$ is the translate of the effective degree-$(g-1)$ locus in $\operatorname{Pic}^{g-1}C$. Torelli recovers $C$ from the principally polarized Jacobian, not from an unspecified unpolarized torus.

Reference: Alexeev–Brunyate, *Extending the Torelli map to toroidal compactifications of Siegel space*, §§1–2.
:::

::: {.front card-id="abelian-semiabelic-stability" tags="definition comparison example"}
Define a semiabelian variety and a stable semiabelic pair. Where does the theta divisor enter the stability condition?
:::

::: {.back card-id="abelian-semiabelic-stability"}
Over algebraically closed $k$, a semiabelian variety is an extension
$$1\to T\to G\to A\to0,\qquad T\simeq\mathbb G_m^r,\quad A\text{ abelian}.$$
The torus rank is $r$; “semiabelian” does not require the extension to split.

A stable semiabelic pair $(G\curvearrowright P,\Theta)$ consists of:

- $P$ connected, projective, seminormal, pure dimension $\dim G$.
- Finitely many $G$-orbits; every stabilizer connected, reduced, and contained in $T$.
- $\Theta$ effective ample Cartier, containing no $G$-orbit.

Its degree is $h^0(P,\mathcal O_P(\Theta))$; degree one is the principal case.

Example: identify $0$ and $\infty$ in $\mathbb P^1$. The resulting nodal genus-one curve has a $\mathbb G_m$-action; a single smooth point gives its degree-one theta divisor. Placing that point at the node fails the orbit condition.

Reference: [Alexeev, *Complete moduli in the presence of semiabelian group action*](https://annals.math.princeton.edu/2002/155-3/p01), §1.
:::

::: {.front card-id="abelian-admissible-cones" tags="definition construction"}
Which cone and lattice data define toroidal compactifications of $\mathcal A_g$? State admissibility, including the rational-radical condition.
:::

::: {.back card-id="abelian-admissible-cones"}
Fix $\Lambda\simeq\mathbb Z^g$. Put $M=\operatorname{Sym}^2\Lambda$ and $N=M^\vee$; in coordinates $M$ consists of integral quadratic polynomials and $N$ of symmetric integral matrices, paired by trace using half-integral matrices for the polynomials.

$C\subset N_{\mathbb R}$ is the positive-definite cone. Its rational closure is
$$C^{\mathrm{rat}}=\{Q\ge0:\ker Q\text{ is spanned by rational vectors}\}.$$
An admissible fan consists of rational polyhedral cones, closed under faces, intersecting along common faces, covering $C^{\mathrm{rat}}$, invariant under $\operatorname{GL}(\Lambda)$, with finitely many cone orbits. It specifies the toric charts at the cusps.

The rational closure is smaller than the ordinary closed semidefinite cone: a rank-one form in dimension two can have an irrational kernel.

Reference: Alexeev–Brunyate, *Extending the Torelli map to toroidal compactifications of Siegel space*, §2.
:::

::: {.front card-id="abelian-three-toroidal-fans" tags="definition comparison example"}
Distinguish the perfect-cone, second-Voronoi, and central-cone fans. Define the Delaunay decomposition used in the second.
:::

::: {.back card-id="abelian-three-toroidal-fans"}
Use the dual lattices of integral quadratic forms and symmetric tensors, paired by evaluation.

| Fan | Defining construction |
| --- | --- |
| Perfect cone / first Voronoi | For a positive-definite form $q$, cone generated by $vv^T$ for its shortest nonzero lattice vectors $v$; include faces |
| Second Voronoi | Closures of loci of positive-definite forms with the same Delaunay subdivision; extend to rational semidefinite boundary |
| Central cone | In the dual space, take the convex hull of positive-definite integral quadratic forms; take its normal cones for minimizing the pairing |

For positive-definite $q$ on $\mathbb R^g$ with lattice $\mathbb Z^g$, a Delaunay cell is
$$\operatorname{conv}\{v\in\mathbb Z^g:q(v-c)=\min_{w\in\mathbb Z^g}q(w-c)\}$$
for some center $c$. These cells tile $\mathbb R^g$ periodically. For $g=1$ they are unit intervals, and the three fans agree.

The central-cone compactification is the normalization of the Igusa blowup. In higher genus the three constructions need not agree.

Reference: Alexeev–Brunyate, *Extending the Torelli map to toroidal compactifications of Siegel space*, §2.
:::

::: {.front card-id="abelian-graph-coedges-emm-dicing" tags="definition construction example"}
Define graph coedges, an edge-minimizing metric, and a lattice dicing. Explain the role of bridges.
:::

::: {.back card-id="abelian-graph-coedges-emm-dicing"}
Orient a connected graph $\Gamma$ and set $H_1=\ker(\partial:\mathbb Z^E\to\mathbb Z^V)$. The **coedge** $e^*$ is the restriction of the $e$th coordinate functional to $H_1$, an element of $H^1(\Gamma,\mathbb Z)$. It is zero iff $e$ is a bridge.

An edge-minimizing metric is a positive-definite quadratic form $q$ on $H^1(\Gamma,\mathbb R)$ such that
$$q(e^*)=1\quad(e^*\ne0),\qquad q(v)\ge1\quad(0\ne v\in H^1(\Gamma,\mathbb Z)).$$
It is strong if equality occurs only at the nonzero signed coedges. Specify whether $q$ has integral, rational, or real coefficients.

A **dicing** is the periodic subdivision cut out by $u_i(x)=m$, $m\in\mathbb Z$, for a spanning unimodular system of integral covectors: every maximal independent subset is a lattice basis. Thus all subdivision vertices are lattice points.

Example: for a cycle graph all nonzero coedges equal $\pm1$ in $H^1\simeq\mathbb Z$; $q(x)=x^2$ is strong. Its dicing is the unit-interval subdivision.

Reference: Alexeev–Brunyate, §§3 and 5; Alexeev, *Moduli of Weighted Hyperplane Arrangements*, §3.10.
:::
