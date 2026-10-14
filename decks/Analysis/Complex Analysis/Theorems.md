---
title: "Analysis::Complex Analysis::Theorems"
---

::: {.front card-id="card-eb4244d2003b0e64" tags="theorem"}
Dirichlet's Test
:::

::: {.back card-id="card-eb4244d2003b0e64"}
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_{n+1} \leq a_n$ and $a_n \to 0$ (i.e. $a_n \searrow 0$),
- the partial sums of $b_n$ are uniformly bounded: there exists an $M$, independent of $N$, such that $\abs{\sum_{n=1}^N b_n} \leq M$ for all $N$,

then $\sum_{n=1}^\infty a_n b_n$ converges.
:::

::: {.front card-id="card-db278e9d3b9f3414" tags="theorem"}
Morera's Theorem
:::

::: {.back card-id="card-db278e9d3b9f3414"}
If $f$ is continuous in an open disc $\DD$ and
$$
\text{For all triangles } T\subset \DD, \qquad \int_T f = 0
,$$
then $f$ is holomorphic.
:::

::: {.front card-id="card-80b0ce10c15510b0" tags="theorem"}
Riemann's Removable Singularity Theorem
:::

::: {.back card-id="card-80b0ce10c15510b0"}
Let $U\subset \CC$ be open, $a\in U$, and $f$ holomorphic on $U\setminus\theset{a}$.
Then TFAE

- $f$ extends holomorphically to all of $U$
- $f$ extends continuously to all of $U$
- There exists a neighborhood of $a$ on which $f$ is bounded.
- The limit characterization:
$$
\lim_{z\to a} (z-a)f(z) = 0
.$$
:::

::: {.front card-id="card-1d105542952c5ca9" tags="theorem"}
Casorati-Weierstrass Theorem
:::

::: {.back card-id="card-1d105542952c5ca9"}
- If $f$ is holomorphic on $\Omega\setminus\theset{z_0} \subseteq \CC$ where $z_0$ is an essential singularity and $V\subseteq \Omega$ then $f(V\setminus\theset{z_0}) \injects \CC$ is dense.
- If $f$ is non-constant and entire then $f(\CC)\injects \CP^1$ is dense.
:::

::: {.front card-id="card-f8ad2422cd303ab3" tags="complex, theorem"}
Maximum Modulus Principle
:::

::: {.back card-id="card-f8ad2422cd303ab3"}
If $f: \Omega \to \CC$ is holomorphic on a connected open set $\Omega$ and not constant, then $\abs{f}$ has no local maximum in $\Omega$. If $\Omega$ is also bounded and $f$ extends continuously to $\overline{\Omega}$, then $\max_{\overline{\Omega}} \abs{f}$ is attained on $\partial \Omega$.
:::

::: {.front card-id="card-5bdd235e0d0ecdbf" tags="complex, theorem"}
Open Mapping Theorem
:::

::: {.back card-id="card-5bdd235e0d0ecdbf"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.
:::

::: {.front card-id="card-eedce37757759076" tags="complex, theorem"}
Cauchy-Goursat Theorem
:::

::: {.back card-id="card-eedce37757759076"}
If $f$ is holomorphic (analytic) on a simply connected region $\Omega$, then
$$
\int_\gamma f = 0
$$
for every closed contour $\gamma \subset \Omega$.
:::

::: {.front card-id="card-ab44a5c54c77da84" tags="definition"}
Mean value theorem for holomorphic and harmonic functions
:::

::: {.back card-id="card-ab44a5c54c77da84"}
If $f$ is holomorphic on a neighborhood of $\overline{D(a,r)}$, then $f(a)=\frac1{2\pi}\int_0^{2\pi}f(a+re^{it})\,dt$. If $u$ is harmonic there, the same circle average equals $u(a)$; its average over $D(a,r)$ also equals $u(a)$.
:::

::: {.front card-id="card-f37b9861f4f3af0c" tags="definition"}
Schwarz Lemma
:::

::: {.back card-id="card-f37b9861f4f3af0c"}
If $f:\mathbb D\to\mathbb D$ is holomorphic and $f(0)=0$, then $|f(z)|\leq|z|$ and $|f'(0)|\leq1$. Equality at a nonzero $z$, or equality in the derivative bound, forces $f(z)=e^{i\theta}z$.
:::

::: {.front card-id="card-9cda9ad59c4e4475" tags="complex, theorem"}
Rouché's Theorem
:::

::: {.back card-id="card-9cda9ad59c4e4475"}
Let $f, g$ be holomorphic on the closed disc $\bar{D} = \theset{\abs{z-z_0} \leq R}$. If
$$
\abs{f - g} < \abs{f} + \abs{g} \quad\text{on}\quad \bd D
,$$
then $f,g\neq 0$ on $\bd D$ (a zero of either would violate the strict inequality), and $f$ and $g$ have the same number of zeros in $D$, counted with multiplicity.
:::

::: {.front card-id="card-bf3b3326661ef644" tags="fact"}
General form of maps in $\aut(\DD)$.
:::

::: {.back card-id="card-bf3b3326661ef644"}
$$f(z) = e^{i\theta} f_\alpha(z), \qquad f_\alpha(z) \definedas {\alpha - z \over 1 - \bar\alpha z}, \qquad \abs{\alpha} < 1,\ \theta\in\RR$$
$f_\alpha$ is an involution that swaps $\alpha$ and $0$.
:::
