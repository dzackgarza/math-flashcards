---
title: "Qual Complex Analysis::Formulas and Technical Theorems"
---

::: {.front card-id="card-d807266aef1df875" tags="theorem"}
Rouche
:::

::: {.back card-id="card-d807266aef1df875"}
If $f$ and $g$ are holomorphic on $\abs{z-z_0} \leq R$ with $f,g\neq 0$ on $\abs{z-z_0} = R$ and
$$
\abs{f-g} < \abs{f} + \abs{g}
,$$
then $f$ and $g$ have the same number of zeros in this region.
:::

::: {.front card-id="card-81d872650e8bba5c" tags="formula, theorem"}
Cauchy Inequalities
:::

::: {.back card-id="card-81d872650e8bba5c"}
$$
\abs{f^{(n)} (z_0) \over n!} \leq R^{-n} \sup_{\abs{z}=R} \abs{f(z)}
.$$
:::

::: {.front card-id="card-007c6dd8698ab88e" tags="formula, theorem"}
Cauchy Integral Formula for $f(z)$
:::

::: {.back card-id="card-007c6dd8698ab88e"}
For $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
$$
f(z) = {1 \over 2\pi i} \int _{\bd D} {f(\xi) \over \xi - z} \,d\xi
.$$
:::

::: {.front card-id="card-2adb6452bd8a1425" tags="formula, theorem"}
Cauchy Integral Formula for $f^{(n)}(z)$
:::

::: {.back card-id="card-2adb6452bd8a1425"}
For $f$ holomorphic in $U\supseteq \bar D$ and $C$ is a circle such that $C^\circ \subset U$ then for any $z\in C^\circ$,
$$
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
.$$
:::

::: {.front card-id="card-df2aea44015043e1"}
Maximum Length Lemma
:::

::: {.back card-id="card-df2aea44015043e1"}
$$
\abs{\int _\gamma f} \leq \sup_{z\in \gamma} \abs{f(z)} \cdot \ell(\gamma)
.$$
:::

::: {.front card-id="card-df28c7619c664624" tags="formula"}
Double angle formulas involving $\tan$
:::

::: {.back card-id="card-df28c7619c664624"}
The double angle formulas:
$$
\sin(2t) = {2\tan(t) \over 1+\tan^2(t)} \\ 
\cos(2t) = {1-\tan^2(2t) \over 1+\tan^2(t)}
.$$
:::

::: {.front card-id="card-5c1c5c94fd550f90" tags="formula"}
Standard parameterization of a circle in $\CC$
:::

::: {.back card-id="card-5c1c5c94fd550f90"}
$$
F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2} \quad x = \tan(t), t\in (-\pi/2, \pi/2)
.$$
:::

::: {.front card-id="card-4f8f6033cc85f2ce" tags="formula"}
Cross-ratio map
:::

::: {.back card-id="card-4f8f6033cc85f2ce"}
$$
R(z) \da (z, z_2, z_3, z_4) \da {z - z_3\over z-z_4}{z_2 - z_4 \over z_2 - z_3} \\
.$$

Sends 

- $z_2 \to 1$
- $z_3\to 0$
- $z_4\to \infty$
:::

::: {.front card-id="card-9618eed93a7024e3" tags="formula"}
The generalized residue formula
:::

::: {.back card-id="card-9618eed93a7024e3"}
$$
\Res_{z=z_0} f = \lim_{z\to z_0} {1 \over (n-1)!} \qty{\dd{}{z}}^{n-1} (z-z_0)^n f(z)
.$$
:::

::: {.front card-id="card-b602c26fa3763b47" tags="formula"}
Inverting series: ${1\over \sin(z) } = \cdots$
:::

::: {.back card-id="card-b602c26fa3763b47"}
$$
{1\over \sin(z)} = \frac{1}{z}+\frac{1}{3 !} z+\frac{7}{360} z^{3}+\mathrm{O}\left(z^{5}\right)
.$$
:::

::: {.front card-id="card-4b8d8aa4b9902ec5" tags="formula"}
Inverting series: for $A(z) = \sum c_k z^k$ and $1/A(z) = \sum b_k z^k$, the formula for the $b_k$ in terms of $c_k$.
:::

::: {.back card-id="card-4b8d8aa4b9902ec5"}
- $b_0 = c_0\inv$
- $b_1 = -c_0\inv(c_1 b_0 )$
- $b_2 = -c_0\inv(c_2b_0 + c_1b_1)$
- $\cdots$
:::
