---
title: "Reading::Surfaces"
---

::: {.front card-id="card-1c6e367330b3dd9c"}
For $f: X\to X'$ a generically finite degree $d$ morphism, describe $f_* C$ for $C$ an irreducible curve.
:::

::: {.back card-id="card-1c6e367330b3dd9c"}
$f_*(C) = 0$ if $f(C)$ is a point

$f_*(C) = r C'$ if $f(C) = C'$ is a curve where ${ \left.{{f}} \right|_{{C}} }:C\to C'$ is degree $r$.
:::

::: {.front card-id="card-6ddcf58dc837cd23"}
What is the push-pull formula for divisors?
:::

::: {.back card-id="card-6ddcf58dc837cd23"}
$f_* f^* D = \deg(f)\cdot D$.
:::

::: {.front card-id="card-c9e811e57c8812b7"}
What is the local intersection multiplicity $m_x(C \cap C')$?
:::

::: {.back card-id="card-c9e811e57c8812b7"}
$m_x(C \cap C') \coloneqq\dim_{\mathbf{C}}{{\mathcal{O}}_x \over \left\langle{f, g}\right\rangle}$ where $f,g$ are the equations in ${\mathcal{O}}_x$.
:::

::: {.front card-id="card-4966e9028f45d255"}
When are $C, C'$ transverse?
:::

::: {.back card-id="card-4966e9028f45d255"}
$m_x(C \cap C') = 1 \iff \left\langle{f, g}\right\rangle = {\mathfrak{m}}_x$, so $f,g$ form a local coordinate system at $x$.
:::

::: {.front card-id="card-24a6a9b949e03010"}
What is the ideal sheaf of $C$?
:::

::: {.back card-id="card-24a6a9b949e03010"}
${\mathcal{O}}_X(-C)$.
:::

::: {.front card-id="card-ac6794481a78b2c6"}
How is $C . C'$ defined?
:::

::: {.back card-id="card-ac6794481a78b2c6"}
$C.C' = \sum_{x\in C\cap C'} {\mathfrak{m}}_x(C \cap C') = h^0(X; {\mathcal{O}}_{C\cap C'})$.
:::

::: {.front card-id="card-80f7d9a0ef117cb4"}
How is $L.L'$ defined for $L, L'\in \operatorname{Pic}(X)$?
:::

::: {.back card-id="card-80f7d9a0ef117cb4"}
$L.L' = \chi({\mathcal{O}}_X) - \chi(L^{-1}) - \chi((L')^{-1}) + \chi(L^{-1}\otimes(L')^{-1})$.
:::

::: {.front card-id="card-d5794332a0a4892d"}
For $C_1, C_2$ curves, what is ${\mathcal{O}}_X(C_1) . {\mathcal{O}}_X(C_2)$?
:::

::: {.back card-id="card-d5794332a0a4892d"}
${\mathcal{O}}_X(C_1) . {\mathcal{O}}_X(C_2) = C_1.C_2$
:::

::: {.front card-id="card-0ed89a7a2ea59f37"}
For $C$ a smooth irreducible curve and $L\in \operatorname{Pic}(X)$, what is ${\mathcal{O}}_X(C) . L$?
:::

::: {.back card-id="card-0ed89a7a2ea59f37"}
${\mathcal{O}}_X(C) . L = \deg{ \left.{{L}} \right|_{{C}} }$
:::

::: {.front card-id="card-350d5d1a93304ab1"}
For $f:X\to Y$ a generically degree $d$ morphism, what is $f^* D_1 . f^* D_2$?
:::

::: {.back card-id="card-350d5d1a93304ab1"}
$f^* D_1 . f^* D_2 = \deg(f) (D_1.D_2)$.
:::
