---
title: "Complex"
---

::: {.front card-id="card-b058ee496f4162bf" tags="complex, theorem"}
Maximum Modulus Principle
:::

::: {.back card-id="card-b058ee496f4162bf"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $\abs{f}$ is unbounded in $\Omega^\circ$.
:::

::: {.front card-id="card-187a7172b3e74b78" tags="complex, theorem"}
Open Mapping Theorem
:::

::: {.back card-id="card-187a7172b3e74b78"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.
:::

::: {.front card-id="card-75999ddbfbc85b0a" tags="complex, identity"}
Exponential expansions of $\sin(z)$
:::

::: {.back card-id="card-75999ddbfbc85b0a"}
$$
\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i},~~d\theta = \frac{dz}{iz}
$$
:::

::: {.front card-id="card-7047e5a0609b6b95" tags="complex, theorem"}
Rouche's Theorem
:::

::: {.back card-id="card-7047e5a0609b6b95"}
If $f, g$ are holomorphic on $\bar{D}(z_0)$ and $\abs{f - g} < \abs{f} + \abs{g}$ on $\bd D$, then $f,g$ are nonvanishing on $\bd D$ and have the same number of zeros.
:::

::: {.front card-id="card-457cf4c6a02c9f16" tags="complex, theorem"}
Cauchy-Goursat Theorem
:::

::: {.back card-id="card-457cf4c6a02c9f16"}
If $f$ is analytic on a simply connected region $\Omega$ containing a contour $\gamma$, then $\int_\gamma f = 0$.
Moreover, this holds for any contour $\gamma \subset \Omega$.
:::

::: {.front card-id="card-2b9165d93afe009d" tags="complex, fact"}
Types of singularities
:::

::: {.back card-id="card-2b9165d93afe009d"}
- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
:::

::: {.front card-id="card-5d0fe1a638f42d1e" tags="definition"}
Conformal Map
:::

::: {.back card-id="card-5d0fe1a638f42d1e"}
A holomorphic map with nowhere vanishing derivative (locally injective).
:::

::: {.front card-id="card-9bd860e460526ce8" tags="examples"}
Example of a conformal map that is not injective.
:::

::: {.back card-id="card-9bd860e460526ce8"}
$$z\mapsto e^z$$
:::

::: {.front card-id="card-b07cf1f02557bb55" tags="fact"}
General form of maps in $\aut(\DD)$.
:::

::: {.back card-id="card-b07cf1f02557bb55"}
$$f_\alpha(z) - {\alpha - z \over 1 - \bar\alpha z}$$
:::

::: {.front card-id="card-4d16e931b88a3f4a" tags="formula"}
Cauchy's Integral Formula for Derivatives
:::

::: {.back card-id="card-4d16e931b88a3f4a"}
\begin{align*}
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.\end{align*}
:::
