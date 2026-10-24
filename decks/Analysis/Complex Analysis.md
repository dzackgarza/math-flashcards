---
title: "Analysis::Complex Analysis"
---

::: {.front card-id="card-cad38830857677f5"}
Define $\log(z)$ for $z\in \CC$.
:::

::: {.back card-id="card-cad38830857677f5"}
$\log(z) = \log\left(re^{i\theta}\right) = \log(r) + i\theta = \log(|z|)+i\arg(z)$
:::

::: {.front card-id="card-1772fa06172bf1d1" tags="definition"}
Definition: A pole $a$ of order $m$
:::

::: {.back card-id="card-1772fa06172bf1d1"}
The smallest $m$ such that
$$
\lim_{z\to a}(z-a)^{m+1}f(z) = 0
.$$
Equivalently, $\lim_{z\to a}(z-a)^{m}f(z)$ is finite and nonzero, while $\lim_{z\to a}\abs{(z-a)^{k}f(z)} = \infty$ for every $k < m$.
:::

::: {.front card-id="card-8cdacf40fc69f9b6" tags="definition"}
Definition: A removable singularity
:::

::: {.back card-id="card-8cdacf40fc69f9b6"}
A pole of order zero, so
$$
\lim_{z\to z_0}(z-z_0)f(z) = 0
.$$
Equivalently, $\lim_{z\to z_0}f(z)$ exists and is finite, and $f$ is bounded on some punctured neighborhood of $z_0$.
:::

::: {.front card-id="card-42fcb708069d4ac4" tags="definition"}
Definition: An essential singularity
:::

::: {.back card-id="card-42fcb708069d4ac4"}
An isolated singularity that is not a pole (or removable). Equivalently,
$$
\lim_{z\to z_0 } f(z) \text{ DNE in } \CC\cup\theset{\infty}
.$$
:::

::: {.front card-id="card-d56e3e1aa8104309" tags="definition"}
Conformal Map
:::

::: {.back card-id="card-d56e3e1aa8104309"}
A holomorphic map with nowhere vanishing derivative (locally injective).
:::

::: {.front card-id="card-281605aabeb43de5" tags="definition"}
Normal family
:::

::: {.back card-id="card-281605aabeb43de5"}
A family of functions $\mcf \definedas \theset{f_j}_{j\in J}$ is **normal** iff every sequence $\theset{f_k}$ has a subsequence that converges locally uniformly, i.e. $\theset{f_{k_i}}$ converges uniformly on every compact subset.
:::

::: {.front card-id="card-50336b73cd2145a3" tags="definition"}
Equicontinuity
:::

::: {.back card-id="card-50336b73cd2145a3"}
A family of functions $f_n$ is **equicontinuous** iff for every $\eps$ there exists a $\delta = \delta(\eps)$ (not depending on $n$ or $f_n$) such that
$$
\abs{x-y}<\delta \implies \abs{f_n(x) - f_n(y)} < \eps
\qquad \forall n
.$$
:::

::: {.front card-id="card-563af3ac08990f07" tags="complex, fact"}
Types of isolated singularities
:::

::: {.back card-id="card-563af3ac08990f07"}
- Removable: $\abs{f(z)}$ is bounded in a punctured disc.
- Poles: $\lim_{z\to p} \abs{f(z)} = \infty$.
- Essential: neither removable nor a pole.
:::

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
\sin(\theta) &= \frac{e^{i\theta} - e^{-i\theta}}{2i} = \frac{z - \inverseof{z}}{2i} \\
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
R(z) \definedas (z, z_2, z_3, z_4) \definedas {z - z_3\over z-z_4}{z_2 - z_4 \over z_2 - z_3} \\
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
State the open mapping theorem for holomorphic functions.
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
General form of maps in $\Aut(\DD)$.
:::

::: {.back card-id="card-bf3b3326661ef644"}
$$f(z) = e^{i\theta} f_\alpha(z), \qquad f_\alpha(z) \definedas {\alpha - z \over 1 - \bar\alpha z}, \qquad \abs{\alpha} < 1,\ \theta\in\RR$$
$f_\alpha$ is an involution that swaps $\alpha$ and $0$.
:::

::: {.front card-id="card-389acb9375a9480e" tags="definition"}
Give a proof sketch of Liouville's theorem.
:::

::: {.back card-id="card-389acb9375a9480e"}
If $f$ is entire and $|f|\leq M$, Cauchy's estimate on a circle of radius $R$ about $a$ gives $|f'(a)|\leq M/R$. Let $R\to\infty$. Thus $f'\equiv0$, so $f$ is constant.
:::

::: {.front card-id="card-e385647e44f3ec34" tags="definition"}
Give a proof sketch of the maximum modulus principle.
:::

::: {.back card-id="card-e385647e44f3ec34"}
If $f$ is holomorphic on a connected domain and $|f|$ has a local maximum at an interior point, the circle mean value formula and the triangle inequality force equality on every small circle about that point. Hence $f$ is constant near the point, and then everywhere by the identity theorem.
:::

::: {.front card-id="card-6fef2276cb7249f3" tags="definition"}
Give a proof sketch of the fundamental theorem of algebra.
:::

::: {.back card-id="card-6fef2276cb7249f3"}
If a nonconstant polynomial $p$ had no zero, $1/p$ would be entire. As $|p(z)|\to\infty$ when $|z|\to\infty$, $1/p$ is bounded outside a disc and hence bounded everywhere. Liouville's theorem makes $1/p$ constant, a contradiction.
:::

::: {.front card-id="card-0818ba219e3247e0" tags="definition"}
Give a proof sketch of the standard form of Rouché's theorem.
:::

::: {.back card-id="card-0818ba219e3247e0"}
If $f,g$ are holomorphic inside and on a simple closed contour $\gamma$ and $|g|<|f|$ on $\gamma$, then $f$ and $f+g$ have the same number of zeros inside, with multiplicity. Sketch: $f+tg$ has no zero on $\gamma$ for $0\leq t\leq1$; its winding number about $0$ stays fixed. Apply the argument principle.
:::

::: {.front card-id="card-90c2f93c024fe386" tags="definition"}
Prove the Schwarz lemma.
:::

::: {.back card-id="card-90c2f93c024fe386"}
In parts:

- $f(z) = \sum_{k\geq 1}c_k z^k$ since $f(0) = 0$ implies $c_0 = 0$.
- $g(z) \definedas f(z)/z = \sum_{k\geq 1}c_k z^{k-1}$ and $g(0) = c_1 = f'(0)$.
- $\abs{f}\leq 1\implies \abs{g} \leq \inverseof{r}$ on $\abs{z} = r$, thus on $\abs{z} \leq r$ by MMP.
- Take the limit $r\to 1$: $\abs{g} \leq 1$, so $\abs{f(z)} \leq \abs{z}$ and $\abs{f'(0)} \leq 1$.
- Part 2: $\abs{f'(0)} = 1$ or $\abs{f(z)} = \abs{z}$ for some $z\neq 0$ means $\abs{g}$ attains its maximum $1$ at an interior point.
- By MMP, $g(z) \equiv c$ is constant with $\abs{c} = 1$, so $f(z) = cz$ is a rotation.
:::

::: {.front card-id="card-15dc7afe22da0cc8" tags="definition"}
Give a proof sketch of the open mapping theorem for holomorphic functions.
:::

::: {.back card-id="card-15dc7afe22da0cc8"}
For nonconstant holomorphic $f$ and $a$ in its domain, write $f(z)-f(a)=(z-a)^m h(z)$ near $a$, with $h(a)\ne0$. A holomorphic $m$th root of $h$ exists on a small disc. In the resulting coordinate, $f(z)-f(a)=w^m$, whose image contains a disc about $0$. Thus $f$ is open.
:::

::: {.front card-id="card-b5d8cadff0214af0" tags="definition"}
Give a proof sketch of the Casorati–Weierstrass theorem.
:::

::: {.back card-id="card-b5d8cadff0214af0"}
If $a$ is an essential isolated singularity of $f$ and $f$ omits a disc about $w$ on some punctured neighborhood of $a$, then $1/(f-w)$ is bounded there. It extends holomorphically across $a$. Its reciprocal makes $f$ meromorphic at $a$, contradicting essentiality. Hence the image of every punctured neighborhood is dense in $\mathbb C$.
:::

::: {.front card-id="card-462d71a1697301ad" tags="definition"}
Give a proof sketch of the Riemann mapping theorem.
:::

::: {.back card-id="card-462d71a1697301ad"}
Every nonempty simply connected proper domain $\Omega\subsetneq\mathbb C$ is biholomorphic to $\mathbb D$. Sketch: construct a bounded injective holomorphic map $\Omega\to\mathbb D$ using a square root of $z-a$ for $a\notin\Omega$. Among normalized injective maps, choose one maximizing the derivative at a base point; normal families give an extremizer. If its image omits a point of $\mathbb D$, a disc automorphism and square root produce a larger derivative, a contradiction.
:::

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

::: {.front card-id="card-9cf6c389465d65d4" tags="examples"}
Example of a conformal map that is not injective.
:::

::: {.back card-id="card-9cf6c389465d65d4"}
$$z\mapsto e^z$$
Not injective because it is periodic, not surjective because it's never zero.
:::

::: {.front card-id="card-8f650043a174ec60" tags="definition"}
Conformal map: $\HH\to \DD$
:::

::: {.back card-id="card-8f650043a174ec60"}
$w=(z-i)/(z+i)$ maps the upper half-plane $\mathbb H$ biholomorphically onto the unit disc $\mathbb D$; $i\mapsto0$ and the real axis maps to the unit circle.
:::

::: {.front card-id="card-4907d3a3dc6d8806" tags="definition"}
Conformal map: right-half-plane to $\DD$
:::

::: {.back card-id="card-4907d3a3dc6d8806"}
$w=(z-1)/(z+1)$ maps $\{\operatorname{Re}z>0\}$ biholomorphically onto $\mathbb D$; $1\mapsto0$ and the imaginary axis maps to the unit circle.
:::

::: {.front card-id="card-56fad98534b35cc5" tags="definition"}
Conformal map: image of a region under the exponential map
:::

::: {.back card-id="card-56fad98534b35cc5"}
Write $z=x+iy$. Then $e^z=e^x e^{iy}$: vertical lines $x=c$ map to circles $|w|=e^c$, and horizontal lines $y=c$ map to rays of argument $c$ (mod $2\pi$). Thus a horizontal strip of height less than $2\pi$ maps injectively to an angular sector.
:::

::: {.front card-id="card-412951010185d47d" tags="definition"}
Conformal map: strip to half-plane
:::

::: {.back card-id="card-412951010185d47d"}
$z\mapsto e^{\pi z/b}$ maps the horizontal strip $0<\operatorname{Im}z<b$ biholomorphically onto $\mathbb H$: its argument ranges over $(0,\pi)$.
:::

::: {.front card-id="card-d0cd68c2d4ae8a2d" tags="definition"}
Conformal map: $\CC \sm (-\infty ,0]$ to a horizontal strip
:::

::: {.back card-id="card-d0cd68c2d4ae8a2d"}
The principal logarithm $z\mapsto\Log z$ maps the slit plane $\CC\sm(-\infty,0]$ biholomorphically onto the horizontal strip $\theset{w : -\pi<\operatorname{Im}w<\pi}$. It restricts to a biholomorphism of $\mathbb H$ onto $\theset{w : 0<\operatorname{Im}w<\pi}$.
:::

::: {.front card-id="card-b6ff03aaf0820e35" tags="definition"}
Conformal map: what does $z+\inverseof{a}$ do?
:::

::: {.back card-id="card-b6ff03aaf0820e35"}
For $a\ne0$, $z\mapsto z+a^{-1}$ is a translation by $1/a$. It moves every point and the whole region by the same vector; it preserves angles and distances.
:::

::: {.front card-id="card-595105d101b34f0b" tags="definition"}
Conformal map: upper half-disc to $\HH$
:::

::: {.back card-id="card-595105d101b34f0b"}
$w=-(z+z^{-1})$ maps $\{z:|z|<1,\ \operatorname{Im}z>0\}$ biholomorphically onto $\mathbb H$. Indeed, $\operatorname{Im}w=\operatorname{Im}z\,(|z|^{-2}-1)>0$; its boundary maps to $\mathbb R$.
:::
