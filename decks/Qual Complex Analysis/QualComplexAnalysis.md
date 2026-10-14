---
title: "Qual Complex Analysis::QualComplexAnalysis"
---

::: {.front card-id="card-efc30f716ad672e5" tags="example"}
An analytic function with convergence radius 1 which fails to converge at any point on $S^1$
:::

::: {.back card-id="card-efc30f716ad672e5"}
$$ \sum_{n=1}^\infty nz^n $$
:::

::: {.front card-id="card-7bccff7082dd2084" tags="example"}
An analytic function with convergence radius 1 which converges at every point on $S^1$
:::

::: {.back card-id="card-7bccff7082dd2084"}
$$ \sum_{n=1}^\infty {z^n\over n^2} $$
:::

::: {.front card-id="card-51377d9d4492f0fc" tags="example"}
An analytic function with convergence radius 1 that converges at every point on $S^1$ except $z=1$
:::

::: {.back card-id="card-51377d9d4492f0fc"}
$$ \sum_{n=1}^\infty {z^n\over n} $$
:::

::: {.front card-id="card-4be5fee745d0e9a2" tags="theorem"}
Dirichlet's Test
:::

::: {.back card-id="card-4be5fee745d0e9a2"}
If $\theset{a_n}, \theset{b_n}$ satisfy

- $a_{n+1} \leq a_n$ and $a_n \to 0$ (i.e. $a_n \searrow 0$),
- The partial sums are uniformly bounded: there exists an $M$ such that $\abs{\sum_{n=1}^N b_n} \leq M$ for all $N$,

then $\sum_{n=1}^\infty a_n b_n < \infty$.
:::

::: {.front card-id="card-fb9c4e33dc877caa" tags="theorem"}
Morera's Theorem
:::

::: {.back card-id="card-fb9c4e33dc877caa"}
If $f$ is continuous in an open disc $\DD$ and
$$
\text{for all triangles } T\subset \DD, \qquad \int_T f = 0
,$$
then $f$ is holomorphic.
:::

::: {.front card-id="card-4bdee4a57b66ba87" tags="theorem"}
Riemann's Removable Singularity Theorem
:::

::: {.back card-id="card-4bdee4a57b66ba87"}
Let $U\subset \CC$ be open, $a\in U$, and $f$ holomorphic on $U\setminus\theset{a}$.
Then TFAE

- $f$ extends holomorphically to all of $U$
- $f$ extends continuously to all of $U$
- There exists a neighborhood of $a$ on which $f$ is bounded.
- $\lim_{z\to a} (z-a)f(z) = 0$.
:::

::: {.front card-id="card-4da52bef893255f0" tags="definition"}
Definition: A pole $a$ of order $m$
:::

::: {.back card-id="card-4da52bef893255f0"}
The smallest $m$ such that
$$
\lim_{z\to a}(z-a)^{m+1}f(z) = 0
.$$
:::

::: {.front card-id="card-e3a32d81f79b9b3d" tags="definition"}
Definition: A removable singularity
:::

::: {.back card-id="card-e3a32d81f79b9b3d"}
A pole of order zero.
:::

::: {.front card-id="card-4a33b738ee8e674f" tags="definition"}
Definition: An essential singularity
:::

::: {.back card-id="card-4a33b738ee8e674f"}
An isolated singularity that is not a pole (or removable).
:::

::: {.front card-id="card-7832025b03ddda69" tags="theorem"}
Casorati-Weierstrass Theorem
:::

::: {.back card-id="card-7832025b03ddda69"}
- If $f$ is holomorphic on $\Omega\setminus\theset{z_0} \subseteq \CC$ where $z_0$ is an essential singularity and $V\subseteq \Omega$ then $f(V\setminus\theset{z_0}) \injects \CC$ is dense.
- If $f$ is non-constant and entire then $f(\CC)\injects \CP^1$ is dense.
:::

::: {.front card-id="card-9465f22f6383b800" tags="formula, theorem"}
Cauchy Inequalities
:::

::: {.back card-id="card-9465f22f6383b800"}
$$
\left| f^{(n)}(z_0) \right| \leq \frac{n!\, \sup_{z\in\gamma} \abs{f(z)}}{R^{n}}
.$$
:::

::: {.front card-id="card-4389c6cb6c33756e" tags="formula, theorem"}
Cauchy Integral Formula (First Derivative)
:::

::: {.back card-id="card-4389c6cb6c33756e"}
For $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
$$
f(z) = {1 \over 2\pi i} \int_{\bd D} {f(\xi) \over \xi - z} \,d\xi
.$$
:::

::: {.front card-id="card-ab937e5872db595c" tags="formula, theorem"}
Cauchy Integral Formula (Higher Derivatives)
:::

::: {.back card-id="card-ab937e5872db595c"}
For $f$ holomorphic in $U\supseteq \bar D$ and $C$ is a circle such that $C^\circ \subset U$ then for any $z\in C^\circ$,
$$
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
.$$
:::

::: {.front card-id="card-4d52249d5829378c"}
Maximum Length Lemma
:::

::: {.back card-id="card-4d52249d5829378c"}
$$
\abs{\int_\gamma f} \leq \sup_{z\in \gamma} \abs{f(z)} \cdot \ell(\gamma)
.$$
:::

::: {.front card-id="card-144ba502d18bd437" tags="complex, theorem"}
Maximum Modulus Principle
:::

::: {.back card-id="card-144ba502d18bd437"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $\abs{f}$ is unbounded in $\Omega^\circ$.
:::

::: {.front card-id="card-6c67d1a6d998a5c5" tags="complex, theorem"}
Open Mapping Theorem
:::

::: {.back card-id="card-6c67d1a6d998a5c5"}
If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.
:::

::: {.front card-id="card-1e6b1cfd5351159c" tags="complex, identity"}
Exponential expansions of $\sin(z)$
:::

::: {.back card-id="card-1e6b1cfd5351159c"}
$$\begin{align*}
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i} \\
d\theta &= \frac{dz}{iz}
\end{align*}$$
:::

::: {.front card-id="card-9cda9ad59c4e4475" tags="complex, theorem"}
Rouché's Theorem
:::

::: {.back card-id="card-9cda9ad59c4e4475"}
If $f, g$ are holomorphic on $\bar{D}(z_0)$ and
$$
\abs{f - g} < \abs{f} + \abs{g} \quad\text{on}\quad \bd D
,$$
then $f,g\neq 0$ on $\bd D$ and have the same number of zeros.
:::

::: {.front card-id="card-a5cee680c8e83d80" tags="complex, theorem"}
Cauchy-Goursat Theorem
:::

::: {.back card-id="card-a5cee680c8e83d80"}
If $f$ is holomorphic on a simply connected region $\Omega$ containing a contour $\gamma$, then $$\int_\gamma f = 0.$$
Moreover, this holds for any contour $\gamma \subset \Omega$.
:::

::: {.front card-id="card-67a9dbe9f796ffae" tags="complex, fact"}
Types of singularities
:::

::: {.back card-id="card-67a9dbe9f796ffae"}
- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
:::

::: {.front card-id="card-a5f6e191256caee2" tags="definition"}
Conformal Map
:::

::: {.back card-id="card-a5f6e191256caee2"}
A holomorphic map with nowhere vanishing derivative (locally injective).
:::

::: {.front card-id="card-9cf6c389465d65d4" tags="examples"}
Example of a conformal map that is not injective.
:::

::: {.back card-id="card-9cf6c389465d65d4"}
$$z\mapsto e^z$$
Not injective because it is periodic, not surjective because it's never zero.
:::

::: {.front card-id="card-bf3b3326661ef644" tags="fact"}
General form of maps in $\aut(\DD)$.
:::

::: {.back card-id="card-bf3b3326661ef644"}
$$f_\alpha(z) \definedas {\alpha - z \over 1 - \bar\alpha z}$$
:::

::: {.front card-id="card-ee39d4fa15b1849d" tags="formula"}
Cauchy's Integral Formula for Derivatives
:::

::: {.back card-id="card-ee39d4fa15b1849d"}
$$
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.$$
:::

::: {.front card-id="card-f3cd7c86184973f4" tags="complex, theorem"}
Rouche's Theorem
:::

::: {.back card-id="card-f3cd7c86184973f4"}
If $f, g$ are holomorphic on $\bar{D}(z_0)$ and $\abs{f - g} < \abs{f} + \abs{g}$ on $\bd D$, then $f,g$ are nonvanishing on $\bd D$ and have the same number of zeros.
:::
