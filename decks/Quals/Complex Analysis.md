---
title: "Quals::Complex Analysis"
---

::: {.front card-id="card-1e75a9c041f944fe"}
Prove the Schwarz lemma.
:::

::: {.back card-id="card-1e75a9c041f944fe"}
- In parts:
- $f(z) = \sum_{k\geq 1}c_k z^k$ since $f(0) = 0$ implies $c_0 = 0$.
- $g(z) \coloneqq f(z)/z = \sum_{k\geq 1}c_k z^{k-1}$ and $g(0) = c_1 = f'(0)$.
- ${\left\lvert {f} \right\rvert}\leq 1\implies {\left\lvert {g} \right\rvert} \leq r^{-1}$ on ${\left\lvert {z} \right\rvert} = r$, thus on ${\left\lvert {z} \right\rvert} \leq r$ by MMP.
- Take the limit $r\to 1$.
- Part 2: extremum in interior implies $g(z) \equiv c$ is constant.
- ${\left\lvert {f'(0)} \right\rvert} = 1$ or $f(z) = z$ for some $z\neq 0$ implies ${\left\lvert {c} \right\rvert} = 1$.
- The actual source:
:::

::: {.front card-id="card-4ae0c0de5beac5d5"}
Conformal map ${\mathbb{H}}\to \mathbb{D}$
:::

::: {.back card-id="card-4ae0c0de5beac5d5"}
$z\mapsto(z-i)/(z+i)$ maps $\mathbb H$ biholomorphically onto $\mathbb D$.
:::

::: {.front card-id="card-2b14a36e3cecc0f9"}
Conformal map: right-half-plane to $\mathbb{D}$
:::

::: {.back card-id="card-2b14a36e3cecc0f9"}
$z\mapsto(z-1)/(z+1)$ maps $\{\operatorname{Re}z>0\}$ biholomorphically onto $\mathbb D$.
:::

::: {.front card-id="card-d38f3ddcd71ba318"}
Conformal map: ${\mathbb{H}}\setminus(-\infty ,0]$ to a horizontal strip
:::

::: {.back card-id="card-d38f3ddcd71ba318"}
The principal logarithm maps $\mathbb H$ biholomorphically onto $\{w:0<\operatorname{Im}w<\pi\}$. The negative real ray is already outside $\mathbb H$.
:::

::: {.front card-id="card-f32689d12d5d73f7"}
Conformal map: what does $z+a^{-1}$ do?
:::

::: {.back card-id="card-f32689d12d5d73f7"}
For $a\ne0$, $z\mapsto z+a^{-1}$ translates the plane by $1/a$ and preserves angles and distances.
:::

::: {.front card-id="card-51daf9d2997f7b1f"}
Conformal map: upper half-disc to ${\mathbb{H}}$
:::

::: {.back card-id="card-51daf9d2997f7b1f"}
$z\mapsto-(z+z^{-1})$ maps $\{z:|z|<1,\ \operatorname{Im}z>0\}$ biholomorphically onto $\mathbb H$.
:::
