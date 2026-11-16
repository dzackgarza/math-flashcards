---
title: "Topology::Four-Manifolds"
---

::: {.front card-id="four-manifold-intersection-form" tags="definition comparison"}
Define the integral intersection form of a closed oriented four-manifold. Explain unimodularity, parity, signature, and its geometric meaning.
:::

::: {.back card-id="four-manifold-intersection-form"}
For connected closed oriented $X$,
$$L_X=H^2(X,\mathbb Z)/\mathrm{torsion},\qquad
Q_X(a,b)=\langle a\smile b,[X]\rangle.$$
Graded commutativity makes $Q_X$ symmetric; integral Poincaré duality makes it unimodular ($\det Q_X=\pm1$). Torsion classes pair trivially with integral classes.

| Term | Meaning |
| --- | --- |
| Even | $Q_X(a,a)\in2\mathbb Z$ for every $a\in L_X$ |
| Odd | Some $a$ has odd square |
| $b_2^\pm$ | Positive/negative inertia indices of $Q_X\otimes\mathbb R$ |
| Signature | $\sigma(X)=b_2^+-b_2^-$ |
| Definite | One of $b_2^+,b_2^-$ is zero |

For transverse oriented embedded surfaces, their signed intersection count equals the pairing of their Poincaré duals. Self-intersection is the Euler number of the oriented normal bundle, computed by intersecting with a small transverse push-off.

For manifolds with boundary the absolute pairing need not be unimodular or nondegenerate; Poincaré–Lefschetz duality pairs relative with absolute classes.
:::

::: {.front card-id="four-manifold-characteristic-numbers" tags="formula application"}
Relate the Euler characteristic, signature, and characteristic numbers of a closed oriented smooth four-manifold. Specialize to a compact complex surface.
:::

::: {.back card-id="four-manifold-characteristic-numbers"}
For connected $X$, Poincaré duality gives $b_0=b_4=1$, $b_3=b_1$:
$$\chi(X)=2-2b_1+b_2^++b_2^-,\qquad
\sigma(X)=b_2^+-b_2^-=\tfrac13\langle p_1(TX),[X]\rangle.$$
If an almost-complex structure induces the orientation,
$$\langle c_2(TX),[X]\rangle=\chi(X),\qquad
\langle c_1(TX)^2,[X]\rangle=2\chi(X)+3\sigma(X).$$
For a compact Kähler surface with complex orientation,
$$b_1=2q,\qquad b_2^+=1+2p_g,\qquad b_2^-=h^{1,1}-1.$$
Thus $\mathbb{CP}^2$ has $(\chi,\sigma,c_1^2)=(3,1,9)$; a K3 has $(24,-16,0)$. The Chern-number equations require an almost-complex tangent bundle, whereas the Pontryagin signature formula does not.
:::

::: {.front card-id="four-manifold-standard-examples" tags="example comparison"}
Give the intersection forms, inertia pairs, and spin status of $S^4$, $\mathbb{CP}^2$, $\overline{\mathbb{CP}}^{\,2}$, $S^2\times S^2$, and a K3 surface.
:::

::: {.back card-id="four-manifold-standard-examples"}
Use complex orientations for $\mathbb{CP}^2$ and K3; the bar reverses orientation. Write $U=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ and take $E_8$ positive definite.

| $X$ | $Q_X$ | $(b_2^+,b_2^-)$ | Spin? |
| --- | --- | --- | --- |
| $S^4$ | Rank-zero form | $(0,0)$ | Yes |
| $\mathbb{CP}^2$ | $\langle1\rangle$ | $(1,0)$ | No |
| $\overline{\mathbb{CP}}^{\,2}$ | $\langle-1\rangle$ | $(0,1)$ | No |
| $S^2\times S^2$ | $U$ | $(1,1)$ | Yes |
| K3 | $3U\oplus2E_8(-1)$ | $(3,19)$ | Yes |

All are simply connected, so evenness of $Q_X$ is equivalent to spin. On $S^2\times S^2$, the factor spheres have square zero and intersect once. On $\mathbb{CP}^2$, two distinct lines intersect once, so the line generator has square one.
:::

::: {.front card-id="four-manifold-connected-sum-blowup" tags="construction application"}
How do orientation reversal, connected sum, and blowup change four-manifold invariants? Distinguish $S^2\times S^2$ from $\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2}$.
:::

::: {.back card-id="four-manifold-connected-sum-blowup"}
For closed connected oriented smooth $X,Y$, remove balls and identify boundary three-spheres by an orientation-reversing map:
$$Q_{X\#Y}=Q_X\oplus Q_Y,\quad
\sigma(X\#Y)=\sigma(X)+\sigma(Y),\quad
\chi(X\#Y)=\chi(X)+\chi(Y)-2.$$
Also $\pi_1(X\#Y)=\pi_1(X)*\pi_1(Y)$. Reversal gives $Q_{\bar X}=-Q_X$, exchanges $b_2^\pm$, and leaves $\chi$ unchanged.

Blowing up a complex surface at a point has underlying oriented smooth manifold $X\#\overline{\mathbb{CP}}^{\,2}$. Its exceptional sphere has square $-1$; $b_2^-$ and $\chi$ increase by one, $\sigma$ and $c_1^2$ decrease by one.

The forms $U$ and $\langle1\rangle\oplus\langle-1\rangle$ both have rank two and signature zero but differ in parity. Therefore $S^2\times S^2$ and $\mathbb{CP}^2\#\overline{\mathbb{CP}}^{\,2}$ are not homeomorphic. Rank and signature alone do not determine the integral form.
:::

::: {.front card-id="four-manifold-spin-spinc" tags="definition comparison"}
Define spin and $\mathrm{Spin}^c$ structures in dimension four. Relate them to $w_2$, characteristic elements, determinant lines, and twisting.
:::

::: {.back card-id="four-manifold-spin-spinc"}
A spin structure lifts the oriented orthonormal frame bundle through $\mathrm{Spin}(4)\to\mathrm{SO}(4)$; it exists iff $w_2(TX)=0$. Its isomorphism classes, when nonempty, form a torsor for $H^1(X,\mathbb Z/2)$.

A $\mathrm{Spin}^c$ structure lifts through
$$\mathrm{Spin}^c(4)=(\mathrm{Spin}(4)\times U(1))/\langle(-1,-1)\rangle
\longrightarrow\mathrm{SO}(4).$$
It has rank-two complex spinor bundles $W^\pm$, determinant line $L=\det W^\pm$, and Clifford multiplication $T^*X\otimes\mathbb C\to\operatorname{Hom}(W^+,W^-)$, with
$$c_1(L)\bmod2=w_2(TX).$$
Every closed oriented smooth four-manifold admits a $\mathrm{Spin}^c$ structure. Their classes form a torsor for $H^2(X,\mathbb Z)$; twisting by a line bundle $B$ changes $W^\pm$ to $W^\pm\otimes B$ and $c_1(L)$ to $c_1(L)+2c_1(B)$. Determinant classes do not distinguish twists by nonzero two-torsion.

Wu's formula says $w_2$ is characteristic: $\langle w_2\smile\bar a,[X]\rangle\equiv Q_X(a,a)\pmod2$ for integral $a$. A lift $c$ satisfies $Q_X(c,a)\equiv Q_X(a,a)\pmod2$. Simply connected $X$ is spin iff $Q_X$ is even; with torsion, test $w_2$ itself.
:::

::: {.front card-id="four-manifold-handles-kirby" tags="definition application"}
Define a four-dimensional handle and a Kirby diagram. How can a diagram give an intersection matrix? Give the simplest examples.
:::

::: {.back card-id="four-manifold-handles-kirby"}
An index-$k$ handle is $D^k\times D^{4-k}$ attached along $S^{k-1}\times D^{4-k}$ in the boundary of the existing manifold. A Morse function yields one such handle for each index-$k$ critical point.

A Kirby diagram records one-handles by dotted circles and two-handles by framed attaching knots; the framing trivializes the normal two-plane bundle of the knot in the boundary. With a zero-handle and only two-handles, the integral linking matrix is the intersection matrix of the resulting four-manifold with boundary: diagonal entries are framings, off-diagonal entries pairwise linking numbers.

| Diagram, then cap the $S^3$ boundary by a four-handle | Closed manifold |
| --- | --- |
| Empty two-handle diagram | $S^4$ |
| One $+1$ framed unknot | $\mathbb{CP}^2$ |
| One $-1$ framed unknot | $\overline{\mathbb{CP}}^{\,2}$ |
| Hopf link with both framings zero | $S^2\times S^2$ |

Handle slides change the basis of two-handle classes and act by integral congruence on the matrix. Cancellation removes an adjacent-index pair when the attaching sphere meets the belt sphere once with the required framing. With one-handles present, compute the handle chain complex; the raw two-handle linking matrix alone need not be the form on $H_2$.
:::

::: {.front card-id="four-manifold-freedman-donaldson-rokhlin" tags="theorem comparison"}
Compare Freedman's classification, Donaldson's diagonalization theorem, and Rokhlin's theorem. Apply them to an $E_8$ intersection form.
:::

::: {.back card-id="four-manifold-freedman-donaldson-rokhlin"}
| Theorem | Hypotheses and conclusion |
| --- | --- |
| Freedman | Closed simply connected oriented topological four-manifolds are classified up to oriented homeomorphism by their unimodular symmetric integral form and Kirby–Siebenmann invariant $\mathrm{ks}\in\mathbb Z/2$. Every such form occurs. For even forms, $\mathrm{ks}=\sigma/8\bmod2$; for odd forms, both values occur. |
| Donaldson | A closed simply connected smooth oriented four-manifold with definite form has form $\langle1\rangle^{\oplus b_2}$ or $\langle-1\rangle^{\oplus b_2}$. |
| Rokhlin | A closed smooth spin four-manifold has $\sigma\equiv0\pmod{16}$. |

The Kirby–Siebenmann class obstructs a PL structure; smooth manifolds have $\mathrm{ks}=0$. Vanishing alone does not guarantee smoothability in dimension four.

Freedman produces a simply connected closed topological manifold with form $E_8$. It has $\sigma=8$ and $\mathrm{ks}=1$, so it is not smoothable. Donaldson also excludes its even definite non-diagonal form from the smooth category; if smooth it would be spin, contradicting Rokhlin.

Even $E_8\oplus E_8$ has $\mathrm{ks}=0$ and signature divisible by sixteen, but Donaldson still excludes a smooth structure. The theorems impose different restrictions.

Reference: Freedman, *The topology of four-dimensional manifolds*; Donaldson, *An application of gauge theory to four-dimensional topology*.
:::

::: {.front card-id="four-manifold-exotic-smooth-structures" tags="definition comparison"}
What is an exotic smooth structure? What do the intersection form and smooth invariants distinguish? Contrast exotic $\mathbb R^4$ with the smooth four-dimensional Poincaré problem.
:::

::: {.back card-id="four-manifold-exotic-smooth-structures"}
Two smooth manifolds are exotic relative to one another if they are homeomorphic but not diffeomorphic. A smooth structure is an equivalence class of smooth atlases on the fixed topological manifold, modulo diffeomorphism.

For closed simply connected smooth oriented four-manifolds, the intersection form determines the oriented homeomorphism type by Freedman, since $\mathrm{ks}=0$. It need not determine the diffeomorphism type. Donaldson and Seiberg–Witten invariants can distinguish smooth structures sharing the same form.

Exotic $\mathbb R^4$ exists: a smooth manifold homeomorphic but not diffeomorphic to standard $\mathbb R^4$. It is noncompact; closed-manifold intersection-form classification does not apply. Existence of an exotic smooth $S^4$ is the smooth four-dimensional Poincaré problem and remains open. Freedman's topological Poincaré theorem does not settle it.
:::

::: {.front card-id="four-manifold-seiberg-witten-equations" tags="definition"}
State the Seiberg–Witten equations and gauge quotient, including the fields, determinant connection convention, and quadratic term.
:::

::: {.back card-id="four-manifold-seiberg-witten-equations"}
Fix a closed oriented Riemannian four-manifold and a $\mathrm{Spin}^c$ structure $\mathfrak s$ with spinors $W^\pm$ and determinant $L$. The fields are a unitary connection $A$ on $L$ and $\psi\in\Gamma(W^+)$; the Levi–Civita connection and $A$ induce the Dirac operator $D_A:\Gamma(W^+)\to\Gamma(W^-)$.

Choose the Clifford identification $\rho:i\Lambda^2_+\to\operatorname{Herm}_0(W^+)$ and define $q$ by $\rho(q(\psi))=(\psi\psi^*)_0$. In this normalization the perturbed equations are
$$D_A\psi=0,\qquad F_A^+=q(\psi)+i\eta,\qquad \eta\in\Omega^2_+(X;\mathbb R).$$
Other Clifford normalizations rescale $q$; keep the convention fixed.

For $u:X\to U(1)$ the gauge action is
$$u\cdot(A,\psi)=(A-2u^{-1}du,\ u\psi).$$
The factor two reflects that $A$ is the determinant connection. The moduli space is the solution set modulo this action. Reducible solutions have $\psi=0$; their curvature equation is $F_A^+=i\eta$. Irreducible solutions have trivial gauge stabilizer.
:::

::: {.front card-id="four-manifold-seiberg-witten-invariant" tags="definition formula"}
Define the numerical Seiberg–Witten invariant in expected dimension zero. State the dimension, orientation, metric-independence, and chamber conditions.
:::

::: {.back card-id="four-manifold-seiberg-witten-invariant"}
For a $\mathrm{Spin}^c$ structure $\mathfrak s$ on closed connected oriented smooth $X$, set $c=c_1(L)$:
$$d(\mathfrak s)=\frac{c^2-(2\chi(X)+3\sigma(X))}{4}.$$
This is the real expected dimension. Choose a homology orientation, an orientation of $H^1(X;\mathbb R)\oplus H^2_+(X;\mathbb R)$, to orient the moduli.

For $b_2^+>1$, a generic metric and perturbation avoiding reducibles give a compact regular moduli space. If $d=0$, its signed count is $\mathrm{SW}_X(\mathfrak s)\in\mathbb Z$ and is independent of these generic choices. Positive-dimensional invariants require cohomology insertions of total degree $d$; they are not counts of points. A nonzero invariant makes $c$ a basic class (possibly with distinct $\mathrm{Spin}^c$ structures sharing $c$ when there is two-torsion).

For $b_2^+=1$, paths can cross reducible walls, so an invariant requires a chamber in the metric/perturbation space. For $b_2^+=0$, this metric-independence statement does not apply. A dimension-zero space alone does not define an invariant without compactness, regularity, and orientations.

Reference: Morgan, *The Seiberg–Witten Equations and Applications to the Topology of Smooth Four-Manifolds*.
:::

::: {.front card-id="four-manifold-sw-applications" tags="application theorem"}
How do Seiberg–Witten invariants constrain positive scalar curvature and the genus of embedded surfaces? Apply the dimension formula to a K3.
:::

::: {.back card-id="four-manifold-sw-applications"}
For closed oriented smooth $X$ with $b_2^+>1$:

- A metric of positive scalar curvature forces all Seiberg–Witten invariants to vanish, by the spinor Weitzenböck formula and small generic perturbations.
- If $c$ is a basic class and $\Sigma\subset X$ is a connected smoothly embedded oriented surface of genus $g\ge1$, with non-torsion class and $\Sigma^2\ge0$, the adjunction inequality is
$$2g-2\ge\Sigma^2+|\langle c,[\Sigma]\rangle|.$$
The self-intersection and genus hypotheses are part of this version.

For K3, $\chi=24$, $\sigma=-16$, so $2\chi+3\sigma=0$. Its spin structure has $c=0$ and $d=0$, with $\mathrm{SW}(0)=\pm1$ according to homology orientation. Thus K3 admits no positive-scalar-curvature metric. The adjunction bound becomes $2g-2\ge\Sigma^2$; a smooth elliptic fiber has $g=1$ and square zero, attaining equality.
:::
