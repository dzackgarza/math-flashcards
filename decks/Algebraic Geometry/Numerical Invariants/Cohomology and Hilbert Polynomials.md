---
title: "Algebraic Geometry::Numerical Invariants::Cohomology and Hilbert Polynomials"
---

::: {.front card-id="card-610ae6d59c072f6d" tags="formula"}
For $n\ge1$ and $d\in\mathbb Z$, compute every $h^i(\mathbb P^n_{\mathbb C},\mathcal O(d))$.
:::

::: {.back card-id="card-610ae6d59c072f6d"}
$$h^i(\mathbb P^n,\mathcal O(d))=\begin{cases}\binom{n+d}{n}&i=0,\ d\ge0,\\\binom{-d-1}{n}&i=n,\ d\le-n-1,\\0&\text{otherwise}.\end{cases}$$
:::

::: {.front card-id="formula-projective-euler-polynomial" tags="formula"}
For $d\in\mathbb Z$ and $n\ge1$, compute $\chi(\mathbb P^n_{\mathbb C},\mathcal O(d))$ using a polynomial binomial coefficient.
:::

::: {.back card-id="formula-projective-euler-polynomial"}
$$\chi(\mathbb P^n,\mathcal O(d))=\binom{n+d}{n}.$$
:::

::: {.front card-id="formula-hilbert-leading-coefficients" tags="formula"}
For a smooth projective complex $n$-fold, $n\ge2$, and an ample divisor $H$, compute the leading two terms of $\chi(\mathcal O_X(mH))$.
:::

::: {.back card-id="formula-hilbert-leading-coefficients"}
$$\chi(\mathcal O_X(mH))=\frac{H^n}{n!}m^n-\frac{K_XH^{n-1}}{2(n-1)!}m^{n-1}+O(m^{n-2}).$$
:::

::: {.front card-id="formula-threefold-riemann-roch" tags="formula"}
For a divisor $D$ on a smooth projective complex threefold $X$, compute $\chi(\mathcal O_X(D))$.
:::

::: {.back card-id="formula-threefold-riemann-roch"}
$$\chi(\mathcal O_X(D))=\frac{D^3}{6}-\frac{K_XD^2}{4}+\frac{D(K_X^2+c_2(X))}{12}-\frac{K_Xc_2(X)}{24}.$$
:::

::: {.front card-id="formula-threefold-structure-euler" tags="formula"}
For a smooth projective complex threefold $X$, compute $\chi(\mathcal O_X)$ from its characteristic numbers.
:::

::: {.back card-id="formula-threefold-structure-euler"}
$$\chi(\mathcal O_X)=-\frac{K_Xc_2(X)}{24}.$$
:::

::: {.front card-id="formula-trivial-canonical-threefold-rr" tags="formula"}
For a divisor $D$ on a smooth projective complex threefold with $K_X\sim0$, compute $\chi(\mathcal O_X(D))$.
:::

::: {.back card-id="formula-trivial-canonical-threefold-rr"}
$$\chi(\mathcal O_X(D))=\frac{D^3}{6}+\frac{c_2(X)D}{12}.$$
:::

::: {.front card-id="formula-hypersurface-multiplicity" tags="formula"}
For a hypersurface $V(f)$ in a smooth complex variety, compute its multiplicity at $p$ using the maximal ideal $\mathfrak m_p$.
:::

::: {.back card-id="formula-hypersurface-multiplicity"}
$$\operatorname{mult}_pV(f)=\operatorname{ord}_{\mathfrak m_p}(f).$$
:::

::: {.front card-id="formula-complete-intersection-hilbert-series" tags="formula"}
Let $R=\mathbb C[x_0,\ldots,x_n]/(f_1,\ldots,f_r)$, with a homogeneous regular sequence of positive degrees $d_i$ and $r\le n$. Compute its Hilbert series.
:::

::: {.back card-id="formula-complete-intersection-hilbert-series"}
$$\operatorname{Hilb}_R(t)=\frac{\prod_{i=1}^r(1-t^{d_i})}{(1-t)^{n+1}}.$$
:::

::: {.front card-id="formula-complete-intersection-dimension-degree" tags="formula"}
For a projective complete intersection $X\subset\mathbb P^n_{\mathbb C}$ cut out by a regular sequence of degrees $d_1,\ldots,d_r$, compute dimension and degree.
:::

::: {.back card-id="formula-complete-intersection-dimension-degree"}
$$\dim X=n-r,\qquad \deg X=\prod_{i=1}^r d_i.$$
:::

::: {.front card-id="formula-complete-intersection-hilbert-polynomial" tags="formula"}
For a complete intersection $X\subset\mathbb P^n_{\mathbb C}$ of multidegree $(d_1,\ldots,d_r)$, compute $P_X(m)$ using polynomial binomial coefficients.
:::

::: {.back card-id="formula-complete-intersection-hilbert-polynomial"}
$$P_X(m)=\sum_{J\subseteq\{1,\ldots,r\}}(-1)^{|J|}\binom{n+m-\sum_{j\in J}d_j}{n}.$$
:::

::: {.front card-id="formula-hypersurface-hilbert-polynomial" tags="formula"}
For a degree-$d$ hypersurface $X\subset\mathbb P^n_{\mathbb C}$, compute $P_X(m)$ and $\chi(\mathcal O_X(m))$ for every integer $m$, using polynomial binomial coefficients.
:::

::: {.back card-id="formula-hypersurface-hilbert-polynomial"}
$$P_X(m)=\chi(\mathcal O_X(m))=\binom{m+n}{n}-\binom{m+n-d}{n}.$$
:::

::: {.front card-id="numerical-projective-betti" tags="formula"}
What are the Betti numbers and Euler characteristic of $\mathbb P^n_{\mathbb C}$?
:::

::: {.back card-id="numerical-projective-betti"}
$$b_{2i}=1\quad(0\le i\le n),\qquad b_{2i+1}=0,\qquad e(\mathbb P^n)=n+1.$$
:::

::: {.front card-id="numerical-abelian-hodge" tags="formula"}
For a complex abelian variety $A$ of dimension $g\ge1$, compute its Hodge numbers, Betti numbers, and Euler characteristics.
:::

::: {.back card-id="numerical-abelian-hodge"}
$$h^{p,q}(A)=\binom gp\binom gq,\qquad b_k(A)=\binom{2g}k,\qquad e(A)=\chi(\mathcal O_A)=0.$$
:::

