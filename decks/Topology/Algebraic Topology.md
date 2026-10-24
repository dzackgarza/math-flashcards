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

