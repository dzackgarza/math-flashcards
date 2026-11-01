---
title: "Topology::Algebraic Topology"
---

::: {.front card-id="card-d06476a2144212bb" tags="definition"}
Retract
:::

::: {.back card-id="card-d06476a2144212bb"}
Retract: A subspace $A \subset X$ is a *retract* of $X$ iff there exists a continuous map $f: X\to A$ such that $f\mid_{A} = \id_A$.

Equivalently it is a *left* inverse to the inclusion.
:::

::: {.front card-id="card-05ac910bdb95eefa" tags="definition"}
Semilocally Simply Connected
:::

::: {.back card-id="card-05ac910bdb95eefa"}
Every point admits a neighborhood $U$ such that $\pi_1(U) = 0$.
:::

::: {.front card-id="card-32e8524b3015ce58" tags="fact"}
Classification of Closed Surfaces
:::

::: {.back card-id="card-32e8524b3015ce58"}
There is a commutative monoid $\Sigma = \generators{P, K, T, S \suchthat S=0, 3P = PT, PK = PT}$ where $P = \RP^2, K$ is the Klein bottle, and $T$ is a 2-torus of genus 1.
Thus every surface is homeomorphic to either $\Sigma_{g}$ for $g\geq 0$, i.e. $S^2, \Sigma_1 = T^2, \Sigma_2 = T^2\# T^2, \cdots$
**or**
if it is nonorientable, a surface $\bar \Sigma_1 = \RP^2, \bar \Sigma_2 = \RP^2 \# \RP^2, \cdots$.
:::

::: {.front card-id="card-103c90768348292e" tags="formulas"}
Euler Characteristics of Surfaces: $S^n, \Sigma_g, \RP^2, K$.
:::

::: {.back card-id="card-103c90768348292e"}
- $\chi(S^1) = 0$
- $\chi(S^2) = 2$
- $\chi(\Sigma_1) = 0$
- $\chi(\Sigma_2) = -2$
- $\chi(\Sigma_3) = -4$
- $\chi(\Sigma_g) = 2-2g$
- $\chi(\RP^2) = 1$
- $\chi(K) = 0$
:::

::: {.front card-id="card-a82ce1e18cfd83bd" tags="definition"}
Definition: Closed Surfaces
:::

::: {.back card-id="card-a82ce1e18cfd83bd"}
Compact and without boundary.
:::

::: {.front card-id="card-1d8d3dd04e78abea" tags="definition"}
Deformation Retract
:::

::: {.back card-id="card-1d8d3dd04e78abea"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a deformation retraction: a continuous map $F:X\cross I \to X$ such that
$$\begin{align*}
F(x, 0) &= x  \iff F_0 = \id_X \\
F(x, 1) &\in A \iff F_1(X) \subseteq A \\
F(a, 1) &= a \iff F_1\mid_A = \id_A
\end{align*}$$
Equivalently it is a homotopy between a retraction $X\to A$ and $\id_X$.
:::

::: {.front card-id="card-89293b7f113d57d5" tags="math"}
Long Exact Sequence of a Pair $(A, B)$
:::

::: {.back card-id="card-89293b7f113d57d5"}
$$\ldots H_n(B) \to H_n(A) \to H_n(A,B) \to H_{n-1}(B) \ldots$$
:::

::: {.front card-id="card-f1fa7adf8ae83421" tags="math"}
UCT: Cohomology and Homology SES
:::

::: {.back card-id="card-f1fa7adf8ae83421"}
$${ 0\to \mathrm{Ext}_{\mathbb{Z}}^{1}(H_{i-1}(X; \mathbb{Z}),A)\to H^{i}(X; A)\to \mathrm{Ext}_{\mathbb{Z}}^{0}(H_{i}(X; \mathbb{Z}),A) \to 0}$$
:::

::: {.front card-id="card-a683dbc7cfd3c6d6" tags="math, definition"}
Cohomology in terms of homology (nice case)
:::

::: {.back card-id="card-a683dbc7cfd3c6d6"}
$$
H^i(X; \mathbb{Z}) = F(H_i(X; \mathbb{Z})) \times T(H_{i-1}(X; \mathbb{Z}))
.$$
:::

::: {.front card-id="card-e0c4672665da8517" tags="math"}
Homology in terms of cohomology (nice case)
:::

::: {.back card-id="card-e0c4672665da8517"}
$$H_i(X; \mathbb{Z}) = F(H^i(X; \mathbb{Z})) \times T(H^{i+1}(X; \mathbb{Z}))$$
:::

::: {.front card-id="card-12349ef1a579719a" tags="math, definition"}
Kunneth isomorphism (nice case)
:::

::: {.back card-id="card-12349ef1a579719a"}
For $F$ a field,
$$
H_{k}(X\times Y;F) \cong \bigoplus_{i+j=k}H_{i}(X;F)\otimes_F H_{j}(Y;F)
.$$
For $R$ a PID, the same isomorphism holds with $R$ coefficients when the $\operatorname{Tor}_1^R$ terms of the Kunneth SES vanish, e.g. when $H_*(X;R)$ is free:
$$H_{k}(X\times Y;R) \cong \bigoplus_{i+j=k}H_{i}(X;R)\otimes_R H_{j}(Y;R)$$
:::

::: {.front card-id="card-d624fd05eb724e0e" tags="definition, math"}
Homology of real projective space, $H_* \RP^2$
:::

::: {.back card-id="card-d624fd05eb724e0e"}
$$
H_* \RP^2 = [\mathbb{Z}, \mathbb{Z}_2, 0, 0, 0, 0\rightarrow ] = \ZZ\cdot t^0 + C_2 \cdot t^1
.$$
:::

::: {.front card-id="card-f5a281c3e878e255" tags="math"}
Mayer Vietoris LES for $X = A \cup B$
:::

::: {.back card-id="card-f5a281c3e878e255"}
$$\ldots  H_n(A \cap B) \xrightarrow{(i^*,~ j^*)} H_n(A) \oplus H_n(B) \xrightarrow{l^* - r^*}  H_n(X) \xrightarrow{\delta} H_{n-1}(A\cap B)\ldots$$
:::

::: {.front card-id="card-39f28c635a20cb85" tags="math"}
$H_* \mathbb{RP}^3$
:::

::: {.back card-id="card-39f28c635a20cb85"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    \mathbb{Z},      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-fd6c486619334ea2" tags="math"}
$H_* \mathbb{RP}^4$
:::

::: {.back card-id="card-fd6c486619334ea2"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    \mathbb{Z}_2,      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-ee476ac92b94d4f6" tags="math"}
$H_* K$
:::

::: {.back card-id="card-ee476ac92b94d4f6"}
$$[\mathbb{Z}, \mathbb{Z} \oplus \mathbb{Z}_2, 0, 0, 0, 0 \rightarrow]$$
:::

::: {.front card-id="card-fa3b288ff43e8eb1" tags="math"}
$H_* \mathbb{CP}^2$
:::

::: {.back card-id="card-fa3b288ff43e8eb1"}
$$[\mathbb{Z}, 0,                 \mathbb{Z},  0,      \mathbb{Z},  0\rightarrow  ]$$
:::

::: {.front card-id="card-7ab86bce55c8c218" tags="math"}
Orientable Surfaces
:::

::: {.back card-id="card-7ab86bce55c8c218"}
$S^n, T^n, \mathbb{RP}^\text{odd}$
:::

::: {.front card-id="card-37fd9d95a5b78829" tags="math"}
Nonorientable Surfaces
:::

::: {.back card-id="card-37fd9d95a5b78829"}
$\mathbb{RP}^\text{even}, \mathbb{M}, \mathbb{K}$
:::

::: {.front card-id="card-c998b608b2d72e42" tags="math"}
$\chi(\Sigma) = 2 \implies\cdots$
:::

::: {.back card-id="card-c998b608b2d72e42"}
$g=0$ so $\Sigma \cong S^2$.
:::

::: {.front card-id="card-3ae9906f7a303204" tags="math"}
$\chi(\Sigma) = 0 \implies\cdots$
:::

::: {.back card-id="card-3ae9906f7a303204"}
$g=1$ so $\Sigma \cong T^2$ (no boundary, orientable), or

$K$ the Klein bottle (no boundary, nonorientable), or

$M$ the Mobius band (1 boundary, nonorientable), or

$S^2\setminus\left\{{ \pt_1, \pt_2 }\right\} \simeq S^1\times I$ an annulus (2 boundaries).
:::

::: {.front card-id="card-f63353ec9a4bff1f" tags="math"}
$\chi(\Sigma) = -2 \implies\cdots$
:::

::: {.back card-id="card-f63353ec9a4bff1f"}
$g=2$ so $\Sigma\cong \Sigma_2$ is a 2-holed torus (no boundary, orientable), or

$\RP^2 \# \RP^2 \# \RP^2 \# \RP^2$ (no boundary, nonorientable, since $\chi(M_g) = 2-g$), or

$S^2\setminus\left\{{ \pt_1,\cdots, \pt_4 }\right\}$.
:::

::: {.front card-id="card-0cdd58ef6d4b9e92" tags="math"}
What is the Euler characteristic in terms of genus?
:::

::: {.back card-id="card-0cdd58ef6d4b9e92"}
$\chi(\Sigma_g) = 2-2g$ if $\Sigma_g$ is orientable, $\chi(M_g) = 2-g$ if $M_g$ is nonorientable.

Puncturing reduces $\chi$ by 1.
:::

::: {.front card-id="card-e6106ff75ead6897"}
What is $\chi(A\# B)$?
:::

::: {.back card-id="card-e6106ff75ead6897"}
$\chi(A) + \chi(B) - 2$
:::

::: {.front card-id="card-bf8e6a277db99586" tags="definition"}
Boundary operator
:::

::: {.back card-id="card-bf8e6a277db99586"}
The boundary operator $\partial_n : C_n(X) \to C_{n-1}(X)$ is defined on a singular simplex $\sigma$ by $\partial_n \sigma = \sum_{i=0}^n (-1)^i \sigma \circ F_i^n$, where $F_i^n : \Delta^{n-1} \to \Delta^n$ is the $i$-th face map. It satisfies $\partial_{n-1} \circ \partial_n = 0$.
:::

::: {.front card-id="card-cee58820b5095527" tags="definition"}
Chain complex
:::

::: {.back card-id="card-cee58820b5095527"}
A chain complex $(C_\bullet,\partial_\bullet)$ is a sequence of abelian groups $C_n$ and homomorphisms $\partial_n : C_n \to C_{n-1}$ such that $\partial_{n-1} \circ \partial_n = 0$ for every $n$.
:::

::: {.front card-id="card-a9f0459542af1917" tags="definition"}
Cofibration
:::

::: {.back card-id="card-a9f0459542af1917"}
A cofibration is a map $i : A \to X$ with the homotopy extension property: for every space $Y$, every homotopy $H : A \times I \to Y$ and every map $f : X \to Y$ with $f|_A = H|_{A \times \{0\}}$ extend to a homotopy $\tilde H : X \times I \to Y$ with $\tilde H|_{X \times \{0\}} = f$.
:::

::: {.front card-id="card-3b4e4ffbf5cd9f2f" tags="definition"}
Cohomology group
:::

::: {.back card-id="card-3b4e4ffbf5cd9f2f"}
For a chain complex $C_\bullet$ and an abelian group $G$, the $n$-th cohomology group is $H^n(C;G) = H_n(\operatorname{Hom}(C_\bullet,G))$, that is, $\ker \delta^n / \operatorname{im} \delta^{n-1}$ for the dual coboundary $\delta$.
:::

::: {.front card-id="card-5abf4d513b1fa4dd" tags="definition"}
Complex projective space
:::

::: {.back card-id="card-5abf4d513b1fa4dd"}
Complex projective $n$-space is $\mathbb{CP}^n = S^{2n+1}/S^1$, where $S^1$ acts on $S^{2n+1} \subseteq \mathbb{C}^{n+1}$ by scalar multiplication; equivalently, it is the space of complex lines in $\mathbb{C}^{n+1}$.
:::

::: {.front card-id="card-7bc7af1796e569f7" tags="definition"}
Connecting homomorphism
:::

::: {.back card-id="card-7bc7af1796e569f7"}
For a short exact sequence of chain complexes $0 \to A_\bullet \to B_\bullet \to C_\bullet \to 0$, the connecting homomorphism $\partial : H_n(C) \to H_{n-1}(A)$ sends the class of a cycle $c \in C_n$ to the class of $a \in A_{n-1}$ obtained by lifting $c$ to $b \in B_n$, applying the differential, and writing $\partial b$ as the image of $a$.
:::

::: {.front card-id="card-6917134e0056ec60" tags="definition"}
Covering space
:::

::: {.back card-id="card-6917134e0056ec60"}
A covering space of $X$ is a space $\tilde X$ with a continuous surjection $p : \tilde X \to X$ such that every $x \in X$ has an open neighborhood $U$ for which $p^{-1}(U)$ is a disjoint union of open sets, each mapped homeomorphically onto $U$ by $p$.
:::

::: {.front card-id="card-c5e58950dd99070b" tags="definition"}
Cw complex
:::

::: {.back card-id="card-c5e58950dd99070b"}
A CW complex is a Hausdorff space $X$ with a filtration $X^{(0)} \subseteq X^{(1)} \subseteq \cdots$ such that $X = \bigcup_n X^{(n)}$, each $X^{(n)}$ is obtained from $X^{(n-1)}$ by attaching $n$-cells $D^n$ along maps $S^{n-1} \to X^{(n-1)}$, and $X$ carries the weak topology with respect to the closed cells.
:::

::: {.front card-id="card-f5a42525f19c2905" tags="definition"}
Eilenberg–maclane space
:::

::: {.back card-id="card-f5a42525f19c2905"}
For a group $G$ and an integer $n \ge 1$, with $G$ abelian when $n \ge 2$, an Eilenberg–MacLane space $K(G,n)$ is a CW complex with $\pi_n(K(G,n)) \cong G$ and $\pi_k(K(G,n)) = 0$ for $k \ne n$. It is unique up to homotopy equivalence.
:::

::: {.front card-id="card-82f7cf3a0add1918" tags="definition"}
Exact sequence
:::

::: {.back card-id="card-82f7cf3a0add1918"}
A sequence $\cdots \to A_{n+1} \xrightarrow{f_{n+1}} A_n \xrightarrow{f_n} A_{n-1} \to \cdots$ of abelian groups is exact if $\ker f_n = \operatorname{im} f_{n+1}$ for every $n$. A short exact sequence is $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$, exact at $A$, $B$, and $C$; a long exact sequence is an exact sequence indexed by all integers $n$.
:::

::: {.front card-id="card-1e151c4f5d969fd8" tags="definition"}
Fibration
:::

::: {.back card-id="card-1e151c4f5d969fd8"}
A Hurewicz fibration is a map $p : E \to B$ with the homotopy lifting property for every space $X$: given a homotopy $H : X \times I \to B$ and a lift $\tilde H_0 : X \to E$ of $H|_{X \times \{0\}}$, there is a homotopy $\tilde H : X \times I \to E$ lifting $H$ and extending $\tilde H_0$. A Serre fibration requires this lifting only for $X = I^n$.
:::

::: {.front card-id="card-915ddd72f4cf772d" tags="definition"}
Fundamental group
:::

::: {.back card-id="card-915ddd72f4cf772d"}
For a space $X$ with basepoint $x_0$, the fundamental group $\pi_1(X,x_0)$ is the group of homotopy classes of loops based at $x_0$, with multiplication induced by concatenation of loops.
:::

::: {.front card-id="card-40c4125547730aca" tags="definition"}
Homology group
:::

::: {.back card-id="card-40c4125547730aca"}
For a chain complex $(C_\bullet,\partial)$, the $n$-th homology group is $H_n = \ker \partial_n / \operatorname{im} \partial_{n+1}$. Its elements are homology classes of cycles modulo boundaries.
:::

::: {.front card-id="card-fa439de69b1adf91" tags="definition"}
Homology with coefficients
:::

::: {.back card-id="card-fa439de69b1adf91"}
For an abelian group $G$, the homology of $X$ with coefficients in $G$ is $H_n(X;G) = H_n(C_\bullet(X) \otimes_{\mathbb{Z}} G)$, where $C_\bullet(X)$ is the singular chain complex. The case $G = \mathbb{Z}$ is the ordinary homology $H_n(X)$.
:::

::: {.front card-id="card-3dc8eb2eaeb0d9b1" tags="definition"}
Loop space
:::

::: {.back card-id="card-3dc8eb2eaeb0d9b1"}
For a based space $(X,x_0)$, the loop space $\Omega X$ is the space of based loops $\gamma : (I,\partial I) \to (X,x_0)$ with the compact-open topology. It satisfies $\pi_n(X,x_0) \cong \pi_{n-1}(\Omega X,x_0)$ for $n \ge 1$.
:::

::: {.front card-id="card-3b2c616ce59766ee" tags="definition"}
Mapping cone
:::

::: {.back card-id="card-3b2c616ce59766ee"}
For a map $f : X \to Y$, the mapping cone $C_f$ is the quotient of $(X \times I) \sqcup Y$ by $(x,0) \sim (x',0)$ and $(x,1) \sim f(x)$; equivalently, $C_f = Y \cup_f CX$, where $CX = X \times I/(X \times \{0\})$ is the cone on $X$.
:::

::: {.front card-id="card-563c89aff894c25d" tags="definition"}
Pair of spaces
:::

::: {.back card-id="card-563c89aff894c25d"}
A pair of spaces $(X,A)$ consists of a topological space $X$ and a subspace $A \subseteq X$. A map of pairs $f : (X,A) \to (Y,B)$ is a continuous map $f : X \to Y$ with $f(A) \subseteq B$.
:::

::: {.front card-id="card-e9184a38fedb51e4" tags="definition"}
Relative homology
:::

::: {.back card-id="card-e9184a38fedb51e4"}
For a pair of spaces $(X,A)$, the relative homology $H_n(X,A)$ is the homology of the quotient chain complex $C_\bullet(X)/C_\bullet(A)$. When $A$ is a nonempty closed subspace that is a deformation retract of a neighborhood, $H_n(X,A) \cong \tilde H_n(X/A)$.
:::

::: {.front card-id="card-ce2d2b4fa17c3321" tags="definition"}
Singular chain
:::

::: {.back card-id="card-ce2d2b4fa17c3321"}
The group $C_n(X)$ of singular $n$-chains is the free abelian group on the set of singular $n$-simplices of $X$. A chain is a finite formal sum $\sum_\sigma a_\sigma \sigma$ with $a_\sigma \in \mathbb{Z}$.
:::

::: {.front card-id="card-2ad6b6e834e5dea3" tags="definition"}
Singular simplex
:::

::: {.back card-id="card-2ad6b6e834e5dea3"}
A singular $n$-simplex in a space $X$ is a continuous map $\sigma : \Delta^n \to X$, where $\Delta^n = \{(t_0,\ldots,t_n) \in \mathbb{R}^{n+1} : t_i \ge 0,\ \sum_i t_i = 1\}$ is the standard $n$-simplex.
:::

::: {.front card-id="card-b51fa5328f9d3138" tags="definition"}
Tor functor
:::

::: {.back card-id="card-b51fa5328f9d3138"}
For a ring $R$, a right $R$-module $M$, and a left $R$-module $N$, choose a free resolution $\cdots \to Q_1 \to Q_0 \to N \to 0$ and set $\operatorname{Tor}_n^R(M,N) = H_n(M \otimes_R Q_\bullet)$. Then $\operatorname{Tor}_0^R(M,N) \cong M \otimes_R N$.
:::

::: {.front card-id="card-ad23d8bdc43985fc" tags="definition"}
Universal cover
:::

::: {.back card-id="card-ad23d8bdc43985fc"}
A universal cover of $X$ is a simply connected covering space $p : \tilde X \to X$. It exists when $X$ is path-connected, locally path-connected, and semilocally simply connected, and it is unique up to homeomorphism over $X$.
:::
