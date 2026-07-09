---
title: "Complex"
---

- Maximum Modulus Principle

    If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $\abs{f}$ is unbounded in $\Omega^\circ$.

    tags: complex, theorem

- Open Mapping Theorem

    If $f: \Omega \to \CC$ is holomorphic and not constant on $\Omega$, then $f$ is an open map.

    tags: complex, theorem

- Exponential expansions of $\sin(z)$

    $$
    \sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i},~~d\theta = \frac{dz}{iz}
    $$

    tags: complex, identity

- Rouche's Theorem

    If $f, g$ are holomorphic on $\bar{D}(z_0)$ and $\abs{f - g} < \abs{f} + \abs{g}$ on $\bd D$, then $f,g$ are nonvanishing on $\bd D$ and have the same number of zeros.

    tags: complex, theorem

- Cauchy-Goursat Theorem

    If $f$ is analytic on a simply connected region $\Omega$ containing a contour $\gamma$, then $\int_\gamma f = 0$.
    Moreover, this holds for any contour $\gamma \subset \Omega$.

    tags: complex, theorem

- Types of singularities

    - Removable: $\abs{f(z)}$ is bounded in a punctured disc.
    - Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
    - Essential: neither removable nor a pole.

    tags: complex, fact

- Conformal Map

    A holomorphic map with nowhere vanishing derivative (locally injective).

    tags: definition

- Example of a conformal map that is not injective.

    $$z\mapsto e^z$$

    tags: examples

- General form of maps in $\aut(\DD)$.

    $$f_\alpha(z) - {\alpha - z \over 1 - \bar\alpha z}$$

    tags: fact

- Cauchy's Integral Formula for Derivatives

    \begin{align*}
    \left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
    .\end{align*}

    tags: formula
