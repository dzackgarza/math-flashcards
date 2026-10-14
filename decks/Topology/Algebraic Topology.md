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
There is a commutative monoid $\Sigma = \gens{P, K, T, S \suchthat S=0, 3P = PT, PK = PT}$ where $P = \RP^2, K$ is the Klein bottle, and $T$ is a 2-torus of genus 1.
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

::: {.front card-id="card-8e1068b00b1b80c0" tags="definition"}
Retract
:::

::: {.back card-id="card-8e1068b00b1b80c0"}
Retract: A subspace $A \subset X$ is a *retract* of $X$ iff there exists a continuous map $f: X\to A$ such that $f\mid_{A} = \id_A$.
Equivalently it is a *left* inverse to the inclusion.
:::

::: {.front card-id="card-1d8d3dd04e78abea" tags="definition"}
Deformation Retract
:::

::: {.back card-id="card-1d8d3dd04e78abea"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a morphism $F:X\cross I$ to $X$ such that $F(x, 0) = x, F(x, 1)\in A, F(a, 1) = a$.
Equivalently it is a homotopy between a retraction and the identity.
:::

::: {.front card-id="card-71975ecfbe1f419d" tags="fact"}
Classification of Closed Surfaces
:::

::: {.back card-id="card-71975ecfbe1f419d"}
There is a commutative monoid $\Sigma = \gens{P, K, T, S \suchthat S=0, 3P = PT, PK = PT}$ where $P = \RP^2, K$ is the Klein bottle, and $T$ is a 2-torus of genus 1.
Thus every surface is homeomorphic to either $\Sigma_{g}$ for $g\geq 0$, i.e. $S^2, \Sigma_1 = T^2, \Sigma_2 = T^2\# T^2, \cdots$ **or** if it is nonorientable, a surface $\bar \Sigma_1 = \RP^2, \bar \Sigma_2 = \RP^2 \# \RP^2, \cdots$.
:::

::: {.front card-id="card-89293b7f113d57d5" tags="math"}
Long Exact Sequence of a Pair $(A, B)$
:::

::: {.back card-id="card-89293b7f113d57d5"}
$$\ldots H_n(B) \to H_n(A) \to H_n(A,B) \to H_{n-1}(B) \ldots$$
:::

::: {.front card-id="card-01f8f61f9fa5a206" tags="math"}
UCT: Change of Coefficients SES
:::

::: {.back card-id="card-01f8f61f9fa5a206"}
$${\displaystyle 0\to \mathrm{Tor}_\mathbb{Z}^0 (H_{i}(X;\mathbb{Z}), A)\,{\to }\,H_{i}(X;A)\to \mathrm{Tor}_\mathbb{Z}^1 (H_{i-1}(X;\mathbb{Z} ),A)\to 0}$$
:::

::: {.front card-id="card-f1fa7adf8ae83421" tags="math"}
UCT: Cohomology and Homology SES
:::

::: {.back card-id="card-f1fa7adf8ae83421"}
$${ 0\to \mathrm{Ext}_{\mathbb{Z}}^{1}(H_{i-1}(X; \mathbb{Z}),A)\to H^{i}(X; A)\to \mathrm{Ext}_{\mathbb{Z}}^{0}(H_{i}(X; \mathbb{Z}),A) \to 0}$$
:::

::: {.front card-id="card-0ed7741abe7127ca" tags="math"}
Kunneth SES
:::

::: {.back card-id="card-0ed7741abe7127ca"}
$$0\to \bigoplus_{i+j=k}H_{i}(X;R)\otimes _{R}H_{j}(Y;R)\to H_{k}(X\times Y;R)\to \bigoplus_{i+j=k-1}{\mathrm  {Tor}}_{R}^{1}(H_{i}(X;R),H_{j}(Y;R))\to 0$$
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
Kunneth (nice case)
:::

::: {.back card-id="card-12349ef1a579719a"}
$$
H_{k}(X\times Y;F) \cong \bigoplus_{i+j=k}H_{i}(X;F)\otimes H_{j}(Y;F)
.$$
:::

::: {.front card-id="card-6af26ae228ea633a" tags="math"}
Hom Table
:::

::: {.back card-id="card-6af26ae228ea633a"}
$$
\begin{array}{c|c|c|c}
Hom & Z_m & Z & Q \\\hline
Z_n  & Z_d & 0 & 0 \\\hline
Z   & Z_m & Z & Q \\\hline
Q   & 0  & 0 & Q
\end{array}
$$
:::

::: {.front card-id="card-205ac8f4c3a11ce3" tags="math"}
Tor Table
:::

::: {.back card-id="card-205ac8f4c3a11ce3"}
$$
\begin{array}{c|c|c|c}
Tor & Z_m & Z & Q \\\hline
Z_n  & Z_d & 0 & 0 \\\hline
Z   & 0  & 0 & 0 \\\hline
Q   & 0  & 0 & 0
\end{array}
$$
:::

::: {.front card-id="card-c935c4621c362acc" tags="math"}
Ext Table
:::

::: {.back card-id="card-c935c4621c362acc"}
$$
\begin{array}{c|c|c|c}
Ext & Z_m & Z    & Q \\\hline
Z_n  & Z_d & Z_n   & 0 \\\hline
Z   & 0  & 0    & 0 \\\hline
Q   & 0  & A_p/Q & 0
\end{array}
$$
:::

::: {.front card-id="card-d624fd05eb724e0e" tags="definition"}
$H_* \mathbb{RP}^2$
:::

::: {.back card-id="card-d624fd05eb724e0e"}
$$
\RP^2 = [\mathbb{Z}, \mathbb{Z}_2, 0, 0, 0, 0\rightarrow ]
.$$
:::

::: {.front card-id="card-f5a281c3e878e255" tags="math"}
Mayer Vietoris LES for $X = A \cup B$
:::

::: {.back card-id="card-f5a281c3e878e255"}
$$\ldots  H_n(A \cap B) \xrightarrow{(i^*,~ j^*)} H_n(A) \oplus H_n(B) \xrightarrow{l^* - r^*}  H_n(X) \xrightarrow{\delta} H_{n-1}(A\cap B)\ldots$$
:::

::: {.front card-id="card-da12721834a63f60" tags="math"}
$H_* \mathbb{RP}^2$
:::

::: {.back card-id="card-da12721834a63f60"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    0,      0,    0\rightarrow  ]$$
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
Euler Characteristic 2
:::

::: {.back card-id="card-c998b608b2d72e42"}
$\chi X = 2 \implies X \cong S^2$
:::

::: {.front card-id="card-3ae9906f7a303204" tags="math"}
Euler Characteristic 0
:::

::: {.back card-id="card-3ae9906f7a303204"}
$\chi X = 0 \implies X \cong T^2$ or $K$
:::

::: {.front card-id="card-f63353ec9a4bff1f" tags="math"}
Euler Characteristic -2
:::

::: {.back card-id="card-f63353ec9a4bff1f"}
$\chi X = -2 \implies X \cong \mathbb{RP}^2$
:::

::: {.front card-id="card-0cdd58ef6d4b9e92" tags="math"}
Euler Characteristic: Formula Involving Genus
:::

::: {.back card-id="card-0cdd58ef6d4b9e92"}
$\chi(X) = 2-2g$
:::

::: {.front card-id="card-1445dbb2db7d9ab6" tags="definition"}
Deformation Retract
:::

::: {.back card-id="card-1445dbb2db7d9ab6"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a deformation retraction: a continuous map $F:X\cross I \to X$ such that
$$\begin{align*}
F(x, 0) &= x  \iff F_0 = \id_X \\
F(x, 1) &\in A \iff F_1(X) \subseteq A \\
F(a, 1) &= a \iff F_1\mid_A = \id_A
\end{align*}$$
Equivalently it is a homotopy between a retraction $X\to A$ and $\id_X$.
:::

::: {.front card-id="card-6a307fa00f74c3b9" tags="math"}
$H_* K$
:::

::: {.back card-id="card-6a307fa00f74c3b9"}
$$[\mathbb{Z}, \mathbb{Z} \times \mathbb{Z}_2,             0,    0,      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-185e273a2e55c6e1" tags="definition"}
Deformation Retract
:::

::: {.back card-id="card-185e273a2e55c6e1"}
Deformation Retract: A subspace $A \subset X$ is a *deformation retract* of $X$ iff there exists a deformation retraction: a continuous map $F:X\cross I$ to $X$ such that
$$
\begin{align*}
F(x, 0) &= x  \iff F_0 = \id_X \\
F(x, 1) &\in A \iff F_1(X) \subseteq A \\
F(a, 1) &= a \iff F_1\mid_A = \id_A
.\end{align*}
$$
Equivalently it is a homotopy between a retraction $X\to A$ and $\id_X$.
:::

::: {.front card-id="card-3a917df8f423b44f"}
What is the Euler characteristic in terms of genus?
:::

::: {.back card-id="card-3a917df8f423b44f"}
$\chi(\Sigma_g) = 2-2g$ if $\Sigma_g$ is orientable, $\chi(M_g) = 2-g$ if $M_g$ is nonorientable.

Puncturing reduces $\chi$ by 1.
:::

::: {.front card-id="card-9e8114fdc2e6992d"}
$\chi(\Sigma) = 2 \implies\cdots$
:::

::: {.back card-id="card-9e8114fdc2e6992d"}
$g=0$ so $\Sigma \cong S^2$.
:::

::: {.front card-id="card-89e50babfc15999b"}
$\chi(\Sigma) = 0 \implies\cdots$
:::

::: {.back card-id="card-89e50babfc15999b"}
$g=1$ so $\Sigma \cong T^1$ (no boundary, orientable), or

$K$ the Klein bottle (no boundary, nonorientable).

$M$ the Mobius band (1 boundary, nonorientable), or

$S^2\setminus\left\{{ {\operatorname{pt}}_1, {\operatorname{pt}}_2 }\right\} \cong S^1\times I$ an annulus (2 boundaries), or
:::

::: {.front card-id="card-ea0ba476b1570b73"}
$\chi(\Sigma) = -2 \implies\cdots$
:::

::: {.back card-id="card-ea0ba476b1570b73"}
$g=2$ so $\Sigma\cong \Sigma_2$ is a 2-holed torus, or

$S^2\setminus\left\{{ {\operatorname{pt}}_1,\cdots, {\operatorname{pt}}_4 }\right\}$.
:::

::: {.front card-id="card-e6106ff75ead6897"}
What is $\chi(A\# B)$?
:::

::: {.back card-id="card-e6106ff75ead6897"}
$\chi(A) + \chi(B) - 2$
:::

::: {.front card-id="card-6ad5dd725c330752"}
Kunneth isomorphism (nice case)
:::

::: {.back card-id="card-6ad5dd725c330752"}
$$H_{k}(X\times Y;R) \cong \bigoplus_{i+j=k}H_{i}(X;R)\otimes H_{j}(Y;R)$$
:::

::: {.front card-id="card-455916a5a5f17b7d"}
The tor complex between $C_n$ and $A$.
:::

::: {.back card-id="card-455916a5a5f17b7d"}
$$\operatorname{Tor}^{\mathbf{Z}}_*(C_n, A) = (A/nA)\cdot t^0 \oplus A[n]\cdot t^1 \oplus \cdots$$
:::

::: {.front card-id="card-9bf5130224135f26"}
The ext complex between $C_n$ and $A$.
:::

::: {.back card-id="card-9bf5130224135f26"}
$$ \operatorname{Ext}^*_{\mathbf{Z}}(C_n, A) = A[n]\cdot t^0 \oplus (A/nA) \cdot t^1 \oplus \cdots$$
:::

::: {.front card-id="card-c32162ef36bb98b4"}
Full tor complex table:
:::

::: {.back card-id="card-c32162ef36bb98b4"}
E.g. top-left is $\operatorname{Tor}_*^{\mathbf{Z}}(C_n, C_m)$.

First row: $C_n\otimes_{\mathbf{Z}}A = A/nA$ and $\operatorname{Tor}_1^{\mathbf{Z}}(C_n, A) = A[n]$.

Second row: ${\mathbf{Z}}\otimes_{\mathbf{Z}}A = A$ and $\operatorname{Tor}_1^{\mathbf{Z}}({\mathbf{Z}}, A) = 0$ since ${\mathbf{Z}}$ is projective.

Third row: $G\otimes_{\mathbf{Z}}{\mathbf{Q}}= {\mathbf{Q}}\otimes_{\mathbf{Z}}G = 0$ for $G$ any group

Also $\operatorname{Tor}(A, B) = \operatorname{Tor}(B, A)$. | $\operatorname{Tor}_*^{\mathbf{Z}}(V, H)$ | $C_m$ | ${\mathbf{Z}}$ | ${\mathbf{Q}}$ | |:---------------------|:-----------------------------------------------|:----------------------------------------------|:------------------------------------------| | $C_n$ | $C_m/nC_m \oplus C_m[n]t = C_d \oplus C_d t$ | ${\mathbf{Z}}/n{\mathbf{Z}}\oplus {\mathbf{Z}}[n]t = C_n \oplus C_nt$ | ${\mathbf{Q}}/n{\mathbf{Q}}\oplus {\mathbf{Q}}[n]t =0\oplus 0t$ | | ${\mathbf{Z}}$ | ${\mathbf{Z}}/m{\mathbf{Z}}+ {\mathbf{Z}}[m]t = C_m + C_m t$ | ${\mathbf{Z}}+ 0t$ | ${\mathbf{Q}}+ 0t$ | | ${\mathbf{Q}}$ | ${\mathbf{Q}}/n{\mathbf{Q}}+ {\mathbf{Q}}[n]t = 0 + 0t$ | ${\mathbf{Q}}+ 0t$ | $0 + 0t$ |
:::

::: {.front card-id="card-47515f1125a40ca3"}
Homology of real projective space, $H_* {\mathbf{RP}}^2$
:::

::: {.back card-id="card-47515f1125a40ca3"}
$$H_* {\mathbf{RP}}^2 = {\mathbf{Z}}\cdot t^0 + C_2 \cdot t^1$$
:::
