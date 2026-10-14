---
title: "Qual Complex Analysis::Theorems facts and statements"
---

::: {.front card-id="card-eb4244d2003b0e64" tags="theorem"}
Dirichlet's Test
:::

::: {.back card-id="card-eb4244d2003b0e64"}
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_n \searrow 0$
- For every $N$, there exists an $M_N$ such that $\abs{\sum_{n=1}^N b_n} \leq M_N$

Then $$ \sum_{n=1}^\infty a_n b_n < \infty .$$
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
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $\abs{f}$ is unbounded in $\Omega^\circ$.
:::

::: {.front card-id="card-5bdd235e0d0ecdbf" tags="complex, theorem"}
Open Mapping Theorem
:::

::: {.back card-id="card-5bdd235e0d0ecdbf"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.
:::

::: {.front card-id="card-b6b2adc676e612d5" tags="complex, identity"}
Exponential expansions of $\sin(z)$
:::

::: {.back card-id="card-b6b2adc676e612d5"}
$$\begin{align*}
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i} \\
d\theta &= \frac{dz}{iz}
\end{align*}$$
:::

::: {.front card-id="card-eedce37757759076" tags="complex, theorem"}
Cauchy-Goursat Theorem
:::

::: {.back card-id="card-eedce37757759076"}
If $f$ is holomorphic on a simply connected region $\Omega$ containing a contour $\gamma$, then $$\int_\gamma f = 0.$$
Moreover, this holds for any contour $\gamma \subset \Omega$.
:::

::: {.front card-id="card-563af3ac08990f07" tags="complex, fact"}
Types of isolated singularities
:::

::: {.back card-id="card-563af3ac08990f07"}
- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
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
