---
title: "Topology::Algebraic Topology"
---

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
$ H_* \mathbb{RP}^2 $
:::

::: {.back card-id="card-d624fd05eb724e0e"}
$$  
\RP^2 = [\mathbb{Z}, \mathbb{Z}_2, 0, 0, 0, 0\rightarrow ]
.$$
:::
