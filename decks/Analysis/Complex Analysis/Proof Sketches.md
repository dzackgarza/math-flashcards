---
title: "Analysis::Complex Analysis::Proof Sketches"
---

::: {.front card-id="card-389acb9375a9480e" tags="definition"}
Liouville's Theorem
:::

::: {.back card-id="card-389acb9375a9480e"}
If $f$ is entire and $|f|\leq M$, Cauchy's estimate on a circle of radius $R$ about $a$ gives $|f'(a)|\leq M/R$. Let $R\to\infty$. Thus $f'\equiv0$, so $f$ is constant.
:::

::: {.front card-id="card-e385647e44f3ec34" tags="definition"}
The maximum modulus principal
:::

::: {.back card-id="card-e385647e44f3ec34"}
If $f$ is holomorphic on a connected domain and $|f|$ has a local maximum at an interior point, the circle mean value formula and the triangle inequality force equality on every small circle about that point. Hence $f$ is constant near the point, and then everywhere by the identity theorem.
:::

::: {.front card-id="card-6fef2276cb7249f3" tags="definition"}
The fundamental theorem of algebra
:::

::: {.back card-id="card-6fef2276cb7249f3"}
If a nonconstant polynomial $p$ had no zero, $1/p$ would be entire. As $|p(z)|\to\infty$ when $|z|\to\infty$, $1/p$ is bounded outside a disc and hence bounded everywhere. Liouville's theorem makes $1/p$ constant, a contradiction.
:::

::: {.front card-id="card-0818ba219e3247e0" tags="definition"}
Rouché's theorem
:::

::: {.back card-id="card-0818ba219e3247e0"}
If $f,g$ are holomorphic inside and on a simple closed contour $\gamma$ and $|g|<|f|$ on $\gamma$, then $f$ and $f+g$ have the same number of zeros inside, with multiplicity. Sketch: $f+tg$ has no zero on $\gamma$ for $0\leq t\leq1$; its winding number about $0$ stays fixed. Apply the argument principle.
:::

::: {.front card-id="card-90c2f93c024fe386" tags="definition"}
The Schwarz lemma
:::

::: {.back card-id="card-90c2f93c024fe386"}
In parts:

- $f(z) = \sum_{k\geq 1}c_k z^k$ since $f(0) = 0$ implies $c_0 = 0$.
- $g(z) \da f(z)/z = \sum_{k\geq 1}c_k z^{k-1}$ and $g(0) = c_1 = f'(0)$.
- $\abs{f}\leq 1\implies \abs{g} \leq r\inv$ on $\abs{z} = r$, thus on $\abs{z} \leq r$ by MMP.
- Take the limit $r\to 1$.
- Part 2: extremum in interior implies $g(z) \equiv c$ is constant.
- $\abs{f'(0)} = 1$ or $f(z) = z$ for some $z\neq 0$ implies $\abs{c} = 1$.
:::

::: {.front card-id="card-15dc7afe22da0cc8" tags="definition"}
Open mapping theorem
:::

::: {.back card-id="card-15dc7afe22da0cc8"}
For nonconstant holomorphic $f$ and $a$ in its domain, write $f(z)-f(a)=(z-a)^m h(z)$ near $a$, with $h(a)\ne0$. A holomorphic $m$th root of $h$ exists on a small disc. In the resulting coordinate, $f(z)-f(a)=w^m$, whose image contains a disc about $0$. Thus $f$ is open.
:::

::: {.front card-id="card-b5d8cadff0214af0" tags="definition"}
Casorati-Weierstrass
:::

::: {.back card-id="card-b5d8cadff0214af0"}
If $a$ is an essential isolated singularity of $f$ and $f$ omits a disc about $w$ on some punctured neighborhood of $a$, then $1/(f-w)$ is bounded there. It extends holomorphically across $a$. Its reciprocal makes $f$ meromorphic at $a$, contradicting essentiality. Hence the image of every punctured neighborhood is dense in $\mathbb C$.
:::

::: {.front card-id="card-462d71a1697301ad" tags="definition"}
The Riemann mapping theorem
:::

::: {.back card-id="card-462d71a1697301ad"}
Every nonempty simply connected proper domain $\Omega\subsetneq\mathbb C$ is biholomorphic to $\mathbb D$. Sketch: construct a bounded injective holomorphic map $\Omega\to\mathbb D$ using a square root of $z-a$ for $a\notin\Omega$. Among normalized injective maps, choose one maximizing the derivative at a base point; normal families give an extremizer. If its image omits a point of $\mathbb D$, a disc automorphism and square root produce a larger derivative, a contradiction.
:::

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
