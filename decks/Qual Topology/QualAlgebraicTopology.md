---
title: "Qual Topology::QualAlgebraicTopology"
---

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
