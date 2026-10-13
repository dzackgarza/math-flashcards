---
title: "Qual Algebra::QualAlgebraicTopology"
---

::: {.front card-id="card-b0ed03cf54959e23" tags="math"}
Mayer Vietoris LES for $X = A \cup B$
:::

::: {.back card-id="card-b0ed03cf54959e23"}
$$\ldots  H_n(A \cap B) \xrightarrow{(i^*,~ j^*)} H_n(A) \oplus H_n(B) \xrightarrow{l^* - r^*}  H_n(X) \xrightarrow{\delta} H_{n-1}(A\cap B)\ldots$$
:::

::: {.front card-id="card-054e66d15230f5c1" tags="math"}
$H_* \mathbb{RP}^2$
:::

::: {.back card-id="card-054e66d15230f5c1"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    0,      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-1d52fb7036e18893" tags="math"}
$H_* \mathbb{RP}^3$
:::

::: {.back card-id="card-1d52fb7036e18893"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    \mathbb{Z},      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-e4a0b4949c99986d" tags="math"}
$H_* \mathbb{RP}^4$
:::

::: {.back card-id="card-e4a0b4949c99986d"}
$$[\mathbb{Z}, \mathbb{Z}_2,             0,    \mathbb{Z}_2,      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-6a307fa00f74c3b9" tags="math"}
$H_* K$
:::

::: {.back card-id="card-6a307fa00f74c3b9"}
$$[\mathbb{Z}, \mathbb{Z} \times \mathbb{Z}_2,             0,    0,      0,    0\rightarrow  ]$$
:::

::: {.front card-id="card-8193876de9167d78" tags="math"}
$H_* \mathbb{CP}^2$
:::

::: {.back card-id="card-8193876de9167d78"}
$$[\mathbb{Z}, 0,                 \mathbb{Z},  0,      \mathbb{Z},  0\rightarrow  ]$$
:::

::: {.front card-id="card-5a6582cf0cd9929d" tags="math"}
Orientable Surfaces
:::

::: {.back card-id="card-5a6582cf0cd9929d"}
$S^n, T^n, \mathbb{RP}^\text{odd}$
:::

::: {.front card-id="card-7b4da9448eadf351" tags="math"}
Nonorientable Surfaces
:::

::: {.back card-id="card-7b4da9448eadf351"}
$\mathbb{RP}^\text{even}, \mathbb{M}, \mathbb{K}$
:::

::: {.front card-id="card-9af68c1e38580ade" tags="math"}
Euler Characteristic 2
:::

::: {.back card-id="card-9af68c1e38580ade"}
$\chi X = 2 \implies X \cong S^2$
:::

::: {.front card-id="card-ede93551afb67520" tags="math"}
Euler Characteristic 0
:::

::: {.back card-id="card-ede93551afb67520"}
$\chi X = 0 \implies X \cong T^2$ or $K$
:::

::: {.front card-id="card-2332ede4eafa19f1" tags="math"}
Euler Characteristic -2
:::

::: {.back card-id="card-2332ede4eafa19f1"}
$\chi X = -2 \implies X \cong \mathbb{RP}^2$
:::

::: {.front card-id="card-2f82ab100f956d2f" tags="math"}
Euler Characteristic: Formula Involving Genus
:::

::: {.back card-id="card-2f82ab100f956d2f"}
$\chi(X) = 2-2g$
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
