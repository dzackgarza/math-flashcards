---
title: "Qual Basics::Basics"
---

::: {.front card-id="card-9c83862120c41169" tags="fact"}
Descartes' Rule of Signs
:::

::: {.back card-id="card-9c83862120c41169"}
The number $r^+$ of positive real roots (counted with multiplicity) of a polynomial $p(x)$ are at most the number $n$ of sign changes in the coefficients.
Moreover, $r^+$ is *exactly* $n-2k$ for some $k\in \ZZ^{\geq 0}$.
Similarly, the number $r^-$ of negative real roots is the same idea applied to $p(-x)$.
The minimal number of nonreal roots is thus $n - (r^+ + r^-)$.

*Examples:*

- $f(x) = x^3 + x^2 - x - 1$ has exactly 1 positive real root.
- $f(-x) = -x^3 + x^2 + x - 1$ has either 2 or 0 positive real roots, so $f$ has 2 or 0 negative real roots.
- $g(x) = x^3 - 1$ has exactly 1 positive real root, $g(-x) = -x^3 - 1$ has 0 positive roots, so $g$ has 2 complex roots.
:::

::: {.front card-id="card-0bc178fa054568ae" tags="formula"}
Factor $x^n - a^n$
:::

::: {.back card-id="card-0bc178fa054568ae"}
$$
(x-a)\sum_{k=0}^{n-1} a^k x^{n-k}
$$
:::

::: {.front card-id="card-39cd778ed0f32a27" tags="formula"}
Factor $x^n + a^n$
:::

::: {.back card-id="card-39cd778ed0f32a27"}
$$
(x+a) \sum _{k=0}^{n-1} (-a)^k x^{n-k}
$$
:::

::: {.front card-id="card-44cb3f71b3da138c" tags="definition"}
Functional characterization of injective functions.
:::

::: {.back card-id="card-44cb3f71b3da138c"}
$$
f(x) = f(y) \implies x=y \iff f \text{ has a left inverse.}
.$$
:::

::: {.front card-id="card-0e941ec5ea10f983" tags="definition"}
Functional characterization of surjective functions.
:::

::: {.back card-id="card-0e941ec5ea10f983"}
$$
\forall y, \exists X \text{ such that } f(x) = y \iff f\text{ has a right inverse, } \exists g \text{ such that } f(g(y)) = y\, \forall y
.$$
:::

::: {.front card-id="card-b294a9fbcf87653a" tags="formula"}
Factor $x^n - y^n$
:::

::: {.back card-id="card-b294a9fbcf87653a"}
$$
(x-y)(x^{n-1} + x^{n-2} y + \cdots + y^{n-1})
$$
:::

::: {.front card-id="card-5f42b26733c7f9e1" tags="formula"}
Factor $x^n + y^n$
:::

::: {.back card-id="card-5f42b26733c7f9e1"}
$$
(x+y)(x^{n-1} + x^{n-2}(-y) + \cdots + (-y)^{n+1})
$$
:::
