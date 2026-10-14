---
title: "Analysis::Complex Analysis::Formulas"
---

::: {.front card-id="card-f959da8514f073d1"}
Standard parameterization of a circle in ${\mathbf{C}}$
:::

::: {.back card-id="card-f959da8514f073d1"}
$$F(t) = {1-x^2\over 1+x^2} + i{2x\over 1+x^2}$$
where $x = \tan(t)$ and $t\in (-\pi/2, \pi/2)$.
:::

::: {.front card-id="card-54a4f4e158f3a677"}
Exponential definitions of $\sin,\cos, \sinh, \cosh$.
:::

::: {.back card-id="card-54a4f4e158f3a677"}
$$\begin{align}  \cos(z) &= {e^{iz} + e^{-iz}\over 2} \qquad \cosh(z) = {e^{z} - e^{-z}\over 2}  \\ \sin(z) &= {e^{iz} + e^{-iz}\over 2i} \qquad \sinh(z) = {e^{z} - e^{-z}\over 2} \end{align}.$$
:::

::: {.front card-id="card-a9efbdda15a4c467"}
Relating hyperbolic functions to usual ones: $\cosh(iz) = \cdots$
:::

::: {.back card-id="card-a9efbdda15a4c467"}
$$\cosh(iz) = \cos(z), \qquad \cos(iz) = \cosh(z).$$
:::

::: {.front card-id="card-f8a5b441dd2af28f"}
Relating hyperbolic functions to usual ones: $\sin(z) = f(\sinh(\cdots)$
:::

::: {.back card-id="card-f8a5b441dd2af28f"}
$$\sinh(iz) = i\sin(z),\qquad \sin(iz) = i\sinh(z).$$
:::

::: {.front card-id="card-4a77bc4987f9aafb"}
Series expansion for ${ \mathrm{sech} }(z) = {1\over \cosh(z)}$
:::

::: {.back card-id="card-4a77bc4987f9aafb"}
****
$$\operatorname{sech} x=1-\frac{x^{2}}{2}+\frac{5 x^{4}}{24}-\frac{61 x^{6}}{720}+\cdots.$$
:::

::: {.front card-id="card-80cd9af57714d4d1"}
Series expansion for $\operatorname{csch}(z) = {1\over \sinh(z)}$
:::

::: {.back card-id="card-80cd9af57714d4d1"}
****
$$\operatorname{csch} x=x^{-1}-\frac{x}{6}+\frac{7 x^{3}}{360}-\frac{31 x^{5}}{15120}+\cdots.$$
:::

::: {.front card-id="card-05bb5c6be34086f4"}
Inverting series: for $A(z) = \sum a_k z^k$ and $1/A(z) = \sum b_k z^k$, the formula for the $b_k$ in terms of $a_k$.
:::

::: {.back card-id="card-05bb5c6be34086f4"}
- $b_0 = a_0^{-1}$
- $b_1 = -a_0^{-1}(a_1 b_0 )$
- $b_2 = -a_0^{-1}(a_1b_1 + a_2b_0)$
- $b_3 = -a_0^{-1}(a_1b_2 + a_2b_1 + a_3 b_0)$
- $\cdots$

****
$$b_n = -a_0^{-1}\sum_{k=1}^n a_n b_{n-k} = -a_0^{-1}\qty{a_1b_{n-1} + a_2b_{n-2} + \cdots + a_n b_0}$$
i.e. count up the $a$s and down the $b$s, starting at $b_{n-1}$ since $b_n$ is unknown.
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

::: {.front card-id="card-ee39d4fa15b1849d" tags="formula"}
Cauchy's Integral Formula for Derivatives
:::

::: {.back card-id="card-ee39d4fa15b1849d"}
$$
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.$$
:::

::: {.front card-id="card-75999ddbfbc85b0a" tags="complex, identity"}
Exponential expansions of $\sin(z)$
:::

::: {.back card-id="card-75999ddbfbc85b0a"}
$$
\sin(\theta) = \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - z\inv}{2i},~~d\theta = \frac{dz}{iz}
$$
:::

::: {.front card-id="card-4d16e931b88a3f4a" tags="formula"}
Cauchy's Integral Formula for Derivatives
:::

::: {.back card-id="card-4d16e931b88a3f4a"}
\begin{align*}
\left|f^{(n)}(0)\right| \leq \frac{n !}{r^{n}} \sup _{|z|=r}|f(z)|
.\end{align*}
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

::: {.front card-id="card-c1aad0f8e8c5afee" tags="definition"}
Exponential definitions of $\cosh$ and $\sinh$
:::

::: {.back card-id="card-c1aad0f8e8c5afee"}
$$
\cosh(z) = {e^{iz} + e^{-iz}\over 2} \\
\sinh(z) = {e^{iz} - e^{-iz}\over 2} \\
.$$
:::

::: {.front card-id="card-d97139d4344d2372" tags="formula"}
Relating hyperbolic functions to usual ones: $\cos(z) = \cosh(?)\\ .$
:::

::: {.back card-id="card-d97139d4344d2372"}
$$
\cos(z) = \cosh(iz)\\
.$$
:::

::: {.front card-id="card-5cd2a73d5a9468af" tags="formula"}
Relating hyperbolic functions to usual ones: $\sin(z) = \sinh(?) .$
:::

::: {.back card-id="card-5cd2a73d5a9468af"}
$$
\sin(z) = {1\over i} \sinh(iz)
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

::: {.front card-id="card-002c0c12fc741ea8" tags="formula"}
Series expansion for $\sech(z) = {1\over \cosh(z)}$
:::

::: {.back card-id="card-002c0c12fc741ea8"}
$$
\operatorname{sech} x=1-\frac{x^{2}}{2}+\frac{5 x^{4}}{24}-\frac{61 x^{6}}{720}+\cdots
.$$
:::

::: {.front card-id="card-a3e8ea65c1b2375b" tags="formula"}
Series expansion for $\csch(z) = {1\over \sinh(z)}$
:::

::: {.back card-id="card-a3e8ea65c1b2375b"}
$$
\operatorname{csch} x=x^{-1}-\frac{x}{6}+\frac{7 x^{3}}{360}-\frac{31 x^{5}}{15120}+\cdots
.$$
:::
