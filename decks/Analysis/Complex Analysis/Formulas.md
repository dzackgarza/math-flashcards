---
title: "Analysis::Complex Analysis::Formulas"
---

::: {.front card-id="card-f959da8514f073d1" tags="formula"}
Standard parameterization of a circle in $\CC$
:::

::: {.back card-id="card-f959da8514f073d1"}
$$F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2}$$
where $x = \tan(t)$ and $t\in (-\pi/2, \pi/2)$. Since $F(t) = \cos(2t) + i\sin(2t) = e^{2it}$, this traces the unit circle except $-1$.
:::

::: {.front card-id="card-54a4f4e158f3a677" tags="definition"}
Exponential definitions of $\sin,\cos, \sinh, \cosh$.
:::

::: {.back card-id="card-54a4f4e158f3a677"}
$$\begin{align}  \cos(z) &= {e^{iz} + e^{-iz}\over 2} \qquad \cosh(z) = {e^{z} + e^{-z}\over 2}  \\ \sin(z) &= {e^{iz} - e^{-iz}\over 2i} \qquad \sinh(z) = {e^{z} - e^{-z}\over 2} \end{align}.$$
:::

::: {.front card-id="card-a9efbdda15a4c467" tags="formula"}
Relating hyperbolic functions to usual ones: $\cosh(iz) = \cdots$
:::

::: {.back card-id="card-a9efbdda15a4c467"}
$$\cosh(iz) = \cos(z), \qquad \cos(iz) = \cosh(z).$$
:::

::: {.front card-id="card-f8a5b441dd2af28f" tags="formula"}
Relating hyperbolic functions to usual ones: $\sin(z) = \sinh(?)$
:::

::: {.back card-id="card-f8a5b441dd2af28f"}
$$\sinh(iz) = i\sin(z),\qquad \sin(iz) = i\sinh(z),\qquad \sin(z) = {1\over i} \sinh(iz).$$
:::

::: {.front card-id="card-4a77bc4987f9aafb" tags="formula"}
Series expansion for ${ \mathrm{sech} }(z) = {1\over \cosh(z)}$
:::

::: {.back card-id="card-4a77bc4987f9aafb"}
$$\operatorname{sech} x=1-\frac{x^{2}}{2}+\frac{5 x^{4}}{24}-\frac{61 x^{6}}{720}+\cdots.$$
:::

::: {.front card-id="card-80cd9af57714d4d1" tags="formula"}
Series expansion for $\operatorname{csch}(z) = {1\over \sinh(z)}$
:::

::: {.back card-id="card-80cd9af57714d4d1"}
$$\operatorname{csch} x=x^{-1}-\frac{x}{6}+\frac{7 x^{3}}{360}-\frac{31 x^{5}}{15120}+\cdots.$$
:::

::: {.front card-id="card-05bb5c6be34086f4" tags="formula"}
Inverting series: for $A(z) = \sum a_k z^k$ and $1/A(z) = \sum b_k z^k$, the formula for the $b_k$ in terms of $a_k$.
:::

::: {.back card-id="card-05bb5c6be34086f4"}
- $b_0 = a_0^{-1}$
- $b_1 = -a_0^{-1}(a_1 b_0 )$
- $b_2 = -a_0^{-1}(a_1b_1 + a_2b_0)$
- $b_3 = -a_0^{-1}(a_1b_2 + a_2b_1 + a_3 b_0)$
- $\cdots$

****
For $n \geq 1$,
$$b_n = -a_0^{-1}\sum_{k=1}^n a_k b_{n-k} = -a_0^{-1}\qty{a_1b_{n-1} + a_2b_{n-2} + \cdots + a_n b_0}$$
i.e. count up the $a$s and down the $b$s, starting at $b_{n-1}$ since $b_n$ is unknown.
:::

::: {.front card-id="card-b6b2adc676e612d5" tags="complex, identity"}
Exponential expansions of $\sin(z)$
:::

::: {.back card-id="card-b6b2adc676e612d5"}
$$\begin{align*}
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i} \\
d\theta &= \frac{dz}{iz}
\end{align*}$$
where $z = e^{i\theta}$.
:::

::: {.front card-id="card-9465f22f6383b800" tags="formula, theorem"}
Cauchy Inequalities
:::

::: {.back card-id="card-9465f22f6383b800"}
If $f$ is holomorphic on a neighborhood of the closed disc $\abs{z-z_0} \leq R$, then
$$
\abs{f^{(n)} (z_0) \over n!} \leq R^{-n} \sup_{\abs{z-z_0}=R} \abs{f(z)}
.$$
This follows from the Cauchy integral formula for $f^{(n)}$ on the circle $\abs{z-z_0}=R$.
:::

::: {.front card-id="card-4389c6cb6c33756e" tags="formula, theorem"}
Cauchy Integral Formula for $f(z)$
:::

::: {.back card-id="card-4389c6cb6c33756e"}
For $D$ a disc and $f$ holomorphic in $U\supseteq \bar D$, then for any $z\in D$,
$$
f(z) = {1 \over 2\pi i} \int_{\bd D} {f(\xi) \over \xi - z} \,d\xi
.$$
:::

::: {.front card-id="card-ab937e5872db595c" tags="formula, theorem"}
Cauchy Integral Formula for $f^{(n)}(z)$
:::

::: {.back card-id="card-ab937e5872db595c"}
For $f$ holomorphic in an open set $U$ and $C$ a circle such that $C \cup C^\circ \subset U$, for any $z\in C^\circ$ and $n \geq 0$,
$$
f^{(n)}(z)=\frac{n !}{2 \pi i} \int_{C} \frac{f(\zeta)}{(\zeta-z)^{n+1}} d \zeta
.$$
For $C = \theset{\abs{z} = r}$ and $z = 0$, this gives the Cauchy inequality
$$
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
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

::: {.front card-id="card-369bdc193b986b1f" tags="formula"}
Series expansion for $\cosh(z)$
:::

::: {.back card-id="card-369bdc193b986b1f"}
$$
\cosh x=1+\frac{x^{2}}{2 !}+\frac{x^{4}}{4 !}+\frac{x^{6}}{6 !}+\cdots=\sum_{n=0}^{\infty} \frac{x^{2 n}}{(2 n) !}
.$$
:::

::: {.front card-id="card-fb4b00995220ce78" tags="formula"}
Series expansion for $\sinh(z)$
:::

::: {.back card-id="card-fb4b00995220ce78"}
$$
\sinh x=x+\frac{x^{3}}{3 !}+\frac{x^{5}}{5 !}+\frac{x^{7}}{7 !}+\cdots=\sum_{n=0}^{\infty} \frac{x^{2 n+1}}{(2 n+1) !}
.$$
:::

::: {.front card-id="card-35b13a0efffb3cb4" tags="formulas"}
Angle addition formulas: $\cosh(x+iy) = \cdots .$
:::

::: {.back card-id="card-35b13a0efffb3cb4"}
$$
\cosh (x+i y) =\cosh (x) \cos (y)+i \sinh (x) \sin (y)
.$$
:::

::: {.front card-id="card-7c7fbda8f367558e" tags="formulas"}
Angle addition formulas: $\sinh(x+iy) = \cdots .$
:::

::: {.back card-id="card-7c7fbda8f367558e"}
$$
\sinh (x+i y) =\sinh (x) \cos (y)+i \cosh (x) \sin (y)
.$$
:::
