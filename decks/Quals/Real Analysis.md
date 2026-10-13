---
title: "Quals::Real Analysis"
---

::: {.front card-id="card-2a577d56671cf6e0"}
What is the $ M{\hbox{-}} $test?
:::

::: {.back card-id="card-2a577d56671cf6e0"}
$ \sum_{n\geq 0} {\left\lVert {f_n} \right\rVert}_{\infty, A} < \infty \implies \sum f_n $ converges absolutely and uniformly on $ A $.

Here $ {\left\lVert {f_n} \right\rVert}_{\infty, A}\coloneqq\sup_{x\in A}{\left\lvert {f_n(x)} \right\rvert} $.

Equivalently, if there is a sequence $ \left\{{M_n}\right\} $ where $ {\left\lvert {f_n(x)} \right\rvert} \leq M_n $ for all $ x\in A $ and $ \sum M_n < \infty $.
:::

::: {.front card-id="card-ec57333f99b1f193"}
Give several equivalent characterizations of completeness.
:::

::: {.back card-id="card-ec57333f99b1f193"}
$ X $ is complete $ \iff $ $ X $ is Cauchy complete $ \iff $ absolutely convergent implies convergent for series.
:::

::: {.front card-id="card-5d62ff4e2881f209"}
What is the Arzela-Ascoli theorem?
:::

::: {.back card-id="card-5d62ff4e2881f209"}
A sequence $ f_i $ has a uniformly convergent subsequence $ \iff $ the sequence is uniformly bounded and uniformly equicontinuous.
:::

::: {.front card-id="card-b06159f3fcf0f68b"}
What is Minkowski's inequality?
:::

::: {.back card-id="card-b06159f3fcf0f68b"}
For $ 1 \leq p < \infty $,

$${\left\lVert {f + g} \right\rVert}_p \leq {\left\lVert {f} \right\rVert}_p + {\left\lVert {g} \right\rVert}_p$$
:::

::: {.front card-id="card-db9e5672e58a93c7"}
What is Young's inequality?
:::

::: {.back card-id="card-db9e5672e58a93c7"}
For $ 1\leq p, q\leq r \leq \infty $ with $ {1\over p} + {1\over q} - {1\over r} = 1 $, then

$${\left\lVert {f\ast g} \right\rVert}_r \leq {\left\lVert {f} \right\rVert}_p {\left\lVert {g} \right\rVert}_q$$

Useful cases:

$$\begin{aligned} \|f * g\|_1 & \leq\|f\|_1\|g\|_1 \\ \|f * g\|_p & \leq\|f\|_1\|g\|_p \\ \|f * g\|_{\infty} & \leq\|f\|_p\|g\|_q \\ \|f * g\|_{\infty} & \leq\|f\|_2\|g\|_2\end{aligned}$$
:::

::: {.front card-id="card-88ae1316ea60ef13"}
What is a Baire space?
:::

::: {.back card-id="card-88ae1316ea60ef13"}
$ X $ is a Baire space $ \iff $ whenever $ \left\{{U_n}\right\} $ is a *countable* collection of open dense subsets of $ X $, then their intersection $ \cap U_n $ is again dense.
:::

::: {.front card-id="card-15f43c2c593e1aa9"}
What is a first category set? A second category?
:::

::: {.back card-id="card-15f43c2c593e1aa9"}
A subset is *first category* $ \iff $ it is countable union of nowhere dense sets, *second category* otherwise.
:::

::: {.front card-id="card-b592c88d5f99eddc"}
What does it mean for a set to be nowhere dense?
:::

::: {.back card-id="card-b592c88d5f99eddc"}
A set is $ A $ **nowhere dense** if its closure has empty interior $ \qty{\overline{A}}^\circ $, equivalently it is not dense in *any* nonempty open set.

For $ {\mathbf{R}} $, every interval $ I $ contains a subinterval $ S\subset I $ with $ S\cap A = \emptyset $, i.e. its closure contains no intervals.

Intuition: elements are not tightly clustered, set is full of holes.
:::

::: {.front card-id="card-eb276d425f8e2a7c"}
Give an example of a set that is not nowhere dense.
:::

::: {.back card-id="card-eb276d425f8e2a7c"}
Counterexample: $ \left\{{1 \over n}\right\}, {\mathbf{Z}} $ are nowhere dense, $ {\mathbf{Q}}, {\mathbf{Z}}\cup\qty{(a, b)\cap{\mathbf{Q}}} $ is *not* nowhere dense
:::

::: {.front card-id="card-4a67647d55675c08"}
What is equicontinuity? Uniform equicontinuity?
:::

::: {.back card-id="card-4a67647d55675c08"}
For $ X, Y $ metric spaces and $ \mathcal{F} $ a family of functions, $ F $ is *equicontinuous at $ x_0 $* $ \iff $ for every $ \varepsilon > 0 $ there exists a $ \delta(\varepsilon, x_0)>0 $ such that

$$x\in B_\delta(x_0) \implies f_i(x) \in B_\varepsilon(f_i(x_0))$$

for all $ f_i \in \mathcal{F} $.

The family $ F $ is *uniformly equicontinuous* $ \iff $ $ \delta(\varepsilon) $ only depends on $ \varepsilon $ and holds for any pair $ x_1, x_2 $ with $ x_1 \in B_\delta(x_2) $.
:::

::: {.front card-id="card-003d9dc1a7872cf0"}
What is the reverse triangle inequality?
:::

::: {.back card-id="card-003d9dc1a7872cf0"}
$${\left\lvert {\, {\left\lVert {x_{}} \right\rVert} - {\left\lVert {y} \right\rVert} \,} \right\rvert} \leq {\left\lVert {x-y} \right\rVert}$$
:::

::: {.front card-id="card-b60b1f8c6208abf9"}
What is a meagre set?
:::

::: {.back card-id="card-b60b1f8c6208abf9"}
A set is *meagre* $ \iff $ it is a countable union of nowhere dense sets.
:::

::: {.front card-id="card-cac150611ba1d5db"}
Characterize the set $ D_f $ of discontinuities of a function.
:::

::: {.back card-id="card-cac150611ba1d5db"}
Always $ F_\sigma $, closed, positive oscillation.

$ f_n\to f $ with $ f_n $ continuous $ \implies D_f $ is meager.

(Lebesgue criterion) $ f \in \mathcal{R}(a, b) $ and bounded $ \implies D_f $ is null.

$ f $ monotone $ \implies D_f $ is countable, and additionally $ f $ d$ \iff $erentiable on $ (a, b) \implies D_f $ is null.
:::

::: {.front card-id="card-ca8a8f1c974ec6e5"}
What is the Baire category theorem?
:::

::: {.back card-id="card-ca8a8f1c974ec6e5"}
If $ X $ is a complete metric space or a locally compact Hausdorff space, then $ X $ is a Baire space.

A (non-empty) complete metric space is *not* the countable union of nowhere dense sets.
:::

::: {.front card-id="card-54eb01fbfeb9c100"}
What is the Caratheodory characterization of outer measure?
:::

::: {.back card-id="card-54eb01fbfeb9c100"}
$ E\subseteq {\mathbf{R}}^n $ is measurable \( \$\iff \)$ for all $ A\subset {\mathbf{R}}^n $,

$$m_*(A) = m_*(E\cap A) + m_*(E\cap A^c)$$
:::

::: {.front card-id="card-c9f47f0bf11b9c8b"}
What are almost disjoint sets?
:::

::: {.back card-id="card-c9f47f0bf11b9c8b"}
$ A^\circ \cap B^\circ = \emptyset $
:::

::: {.front card-id="card-56a80311947e75d8"}
What is convergence in measure?
:::

::: {.back card-id="card-56a80311947e75d8"}
$$\lim _{k \rightarrow \infty} m\left(\left\{x \in E|| f_{k}(x)-f(x) |>\alpha\right\}\right)=0$$
:::

::: {.front card-id="card-964eca48e0deed6c"}
What is a separable space?
:::

::: {.back card-id="card-964eca48e0deed6c"}
Contains a countable dense subset.
:::

::: {.front card-id="card-f934cf5abb9bbe43"}
Is the composition of Lebesgue measurable functions again Lebesgue measurable?
:::

::: {.back card-id="card-f934cf5abb9bbe43"}
**No:** Take $ f: [0, 1]\to [0, 1] $ the Cantor-Lebesgue function (monotonic and cts) and $ C $ the Cantor set

$ f(C) = [0, 1] $, so define $ g(x) = f(x) +x $ so $ g:[0, 1] \to [0, 2] $ (strictly monotonic and cts, so a homeomorphism), so $ g^{-1} $ is cts and thus measurable.

$ \mu(g(C)) = 1>0 $ (because $ f $ is constant on every interval in $ C^c $) so $ g(C) \supseteq A $ a non-measurable subset

$ g^{-1}(A) \subset C $ with $ \mu(C) = 0 $ implies $ g^{-1}(A) $ is a measurable set, so $ \chi_{g^{-1}(A)} $ is a measurable function

Then $ k\coloneqq\chi_{g^{-1}(A)} \circ g^{-1} $ isn't measurable since

$$k^{-1}(1) = \qty{ (g^{-1})^{-1}\circ \chi_{g^{-1}(A)} }(1) = g(g^{-1}(A)) = A.$$

is not a measurable set.
:::

::: {.front card-id="card-a8ab05152235b77b"}
What is a dense subset?
:::

::: {.back card-id="card-a8ab05152235b77b"}
A subset $ A\subseteq X $ is *dense* in $ X $ $ \iff $ $ \mathrm{cl}_X(A) = X $.
:::

::: {.front card-id="card-63fa36a22df22e28"}
What is the uniform boundedness principle?
:::

::: {.back card-id="card-63fa36a22df22e28"}
If $ \mathcal{F} $ is a family of bounded operators $ T_n:X\to Y $ between Banach spaces with

$$\forall x\in X, \qquad \sup_{T_n \in \mathcal{F}} {\left\lVert {T_n(x)} \right\rVert}_Y < \infty$$

then $ \sup_{T_n\in \mathcal{F}} {\left\lVert {T_n} \right\rVert}_X < \infty $.

Slogan: pointwise bounded sequences of operators are uniformly bounded.
:::

::: {.front card-id="card-018a3a1f68d39e33"}
What is the diameter of set?
:::

::: {.back card-id="card-018a3a1f68d39e33"}
$ \mathrm{diam}(A) = \sup_{x, y\in A} {\left\lvert {d} \right\rvert}(x, y) $
:::

::: {.front card-id="card-afd11594850b897d"}
What is the Bolzano-Weierstrass Property
:::

::: {.back card-id="card-afd11594850b897d"}
Every sequence has a convergent subsequence
:::

::: {.front card-id="card-7c34fd923f6f78d9"}
What is a complete measure?
:::

::: {.back card-id="card-7c34fd923f6f78d9"}
A measure whose domain includes all subsets of null sets.
:::

::: {.front card-id="card-a39170950c82c2ea"}
Define $ \limsup, \liminf $ for sequences of sets. What are their containments?
:::

::: {.back card-id="card-a39170950c82c2ea"}
$$\liminf _{n \rightarrow \infty} A_n=\bigcup_{n \geq 1} \bigcap_{j \geq n} A_j, \qquad \limsup _{n \rightarrow \infty} A_n=\bigcap_{n \geq 1} \bigcup_{j \geq n} A_j$$

- Supremum: Union, $ \limsup = \inf\sup $, in infinitely many
- Infimum: Intersection, $ \liminf = \sup\inf $, eventually in
- $ \liminf _{n \rightarrow \infty} A_n \subseteq \limsup _{n \rightarrow \infty} A_n $ since "all but finitely many" implies "infinitely often".
:::

::: {.front card-id="card-a18e45a44e26f012"}
What is the Hahn-Banach theorem?
:::

::: {.back card-id="card-a18e45a44e26f012"}
If $ p: V\to {\mathbf{R}} $ is a sublinear function and $ \phi: U\to {\mathbf{R}} $ a linear functional on $ U\leq V $ with $ \phi \leq p $, then there exists a $ p{\hbox{-}} $sublinear extension $ \tilde \phi: V\to {\mathbf{R}} $
:::

::: {.front card-id="card-7bc8fd9fa6929936"}
What is the Riesz Representation theorem?
:::

::: {.back card-id="card-7bc8fd9fa6929936"}
For $ H $ a Hilbert space and $ \varphi \in H {}^{ \vee } $, there exists an $ f\in H $ such that $ x\in H \implies \varphi(x) = {\left\langle {f},~{x} \right\rangle} $ with $ {\left\lVert {f} \right\rVert}_H = {\left\lVert {\varphi} \right\rVert}_{H {}^{ \vee }} $.
:::

::: {.front card-id="card-bbc73d2319c2d35e"}
What is a compact operator?
:::

::: {.back card-id="card-bbc73d2319c2d35e"}
The image of every bounded subset has compact closure.

Necessarily bounded

Closure of space of finite-rank operators in the norm topology
:::

::: {.front card-id="card-c2f05c220c261c17"}
What is the Borel-Cantelli lemma?
:::

::: {.back card-id="card-c2f05c220c261c17"}
$ \sum P(E_n) < \infty \implies P(\limsup_n E_n) == 0 $

If $ E_n $ are independent events and $ \sum P(E_n) = \infty $< then $ P(\limsup_n E_n) = 1 $.
:::

::: {.front card-id="card-495aa6676e1b151c"}
What does small tails mean? Absolute continuity?
:::

::: {.back card-id="card-495aa6676e1b151c"}
Let $ f\in L^1 $ and $ \varepsilon> 0 $.

**Small Tails**: there exists an $ N $ such that $ \int_{B_N^c} f < \varepsilon $.

**Absolute Continuity**: there exists a $ \delta $ such that $ m(E) < \delta \implies \int_E {\left\lvert {f} \right\rvert} < \varepsilon $.
:::
