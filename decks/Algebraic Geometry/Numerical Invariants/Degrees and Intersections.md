---
title: "Algebraic Geometry::Numerical Invariants::Degrees and Intersections"
---

::: {.front card-id="formula-smooth-center-blowup-euler" tags="formula"}
For the blowup $\widetilde X\to X$ of a smooth projective complex variety along a smooth center $Z$ of codimension $c\ge2$, compute $e(\widetilde X)$.
:::

::: {.back card-id="formula-smooth-center-blowup-euler"}
$$e(\widetilde X)=e(X)+(c-1)e(Z).$$
:::

::: {.front card-id="formula-point-blowup-exceptional-power" tags="formula"}
For a point blowup of a smooth complex $n$-fold, $n\ge2$, compute the top intersection of the exceptional divisor $E$.
:::

::: {.back card-id="formula-point-blowup-exceptional-power"}
$$E^n=(-1)^{n-1}.$$
:::

::: {.front card-id="formula-cyclic-quotient-resolution" tags="formula"}
For the complex cyclic quotient singularity $\frac1r(1,a)$, with $0<a<r$ and $\gcd(r,a)=1$, write $r/a=[b_1,\ldots,b_s]^-$ with $b_i\ge2$. Compute the exceptional intersection matrix of its minimal resolution.
:::

::: {.back card-id="formula-cyclic-quotient-resolution"}
$$E_i^2=-b_i,\qquad E_iE_{i+1}=1,\qquad E_iE_j=0\quad(|i-j|>1),\qquad \frac ra=b_1-\cfrac1{b_2-\cfrac1{\ddots-\cfrac1{b_s}}}.$$
:::

::: {.front card-id="formula-surface-discrepancy-equations" tags="formula"}
For a resolution $\pi:\widetilde X\to X$ of a normal complex $\mathbb Q$-Gorenstein surface singularity with smooth rational exceptional curves $E_i$, give the canonical discrepancy formula and the linear system for its coefficients.
:::

::: {.back card-id="formula-surface-discrepancy-equations"}
$$K_{\widetilde X}=\pi^*K_X+\sum_i a_iE_i,\qquad \sum_i a_i(E_iE_j)=-2-E_j^2.$$
:::

::: {.front card-id="formula-du-val-resolution-invariants" tags="formula"}
For the minimal resolution $\pi:\widetilde X\to X$ of a complex Du Val surface singularity, compute the exceptional self-intersections, canonical discrepancy, and $R^1\pi_*\mathcal O_{\widetilde X}$.
:::

::: {.back card-id="formula-du-val-resolution-invariants"}
$$E_i^2=-2,\qquad K_{\widetilde X}=\pi^*K_X,\qquad R^1\pi_*\mathcal O_{\widetilde X}=0.$$
:::

::: {.front card-id="formula-chow-projective-space" tags="formula"}
For complex projective space with hyperplane class $H$, give its Chow ring and degree map.
:::

::: {.back card-id="formula-chow-projective-space"}
$$A^*(\mathbb P^n)=\mathbb Z[H]/(H^{n+1}),\qquad \int_{\mathbb P^n}H^n=1.$$
:::

::: {.front card-id="formula-chow-product-projective-spaces" tags="formula"}
For $\mathbb P^m_{\mathbb C}\times\mathbb P^n_{\mathbb C}$ with the pulled-back hyperplane classes $H_1,H_2$, compute the Chow ring and its top monomial degree.
:::

::: {.back card-id="formula-chow-product-projective-spaces"}
$$A^*(\mathbb P^m\times\mathbb P^n)=\frac{\mathbb Z[H_1,H_2]}{(H_1^{m+1},H_2^{n+1})},\qquad \int H_1^mH_2^n=1.$$
:::

::: {.front card-id="formula-diagonal-projective-space" tags="formula"}
Compute the diagonal class in $A^n(\mathbb P^n_{\mathbb C}\times\mathbb P^n_{\mathbb C})$, using the hyperplane classes $H_1,H_2$.
:::

::: {.back card-id="formula-diagonal-projective-space"}
$$[\Delta]=\sum_{i=0}^nH_1^iH_2^{n-i}.$$
:::

::: {.front card-id="formula-hyperplane-degree" tags="formula"}
For a projective complex $n$-fold $X\subset\mathbb P^N$ with hyperplane class $H$, compute its top hyperplane intersection.
:::

::: {.back card-id="formula-hyperplane-degree"}
$$\int_X H^n=\deg X.$$
:::

::: {.front card-id="formula-finite-pullback-intersections" tags="formula"}
For a finite surjective map $f:X\to Y$ of smooth projective complex $n$-folds and divisors $D_1,\ldots,D_n$ on $Y$, compute the intersection of their pullbacks.
:::

::: {.back card-id="formula-finite-pullback-intersections"}
$$(f^*D_1)\cdots(f^*D_n)=(\deg f)D_1\cdots D_n.$$
:::

::: {.front card-id="formula-projective-bundle-chow" tags="formula"}
Let $X$ be smooth over $\mathbb C$ and $E$ have rank $r$. For the quotient bundle $\pi:\mathbb P(E)=\operatorname{Proj}(\operatorname{Sym}E)\to X$, set $\xi=c_1(\mathcal O(1))$. Compute the Chow ring.
:::

::: {.back card-id="formula-projective-bundle-chow"}
$$A^*(\mathbb P(E))=\frac{A^*(X)[\xi]}{\left(\sum_{i=0}^r(-1)^ic_i(E)\xi^{r-i}\right)}.$$
:::

::: {.front card-id="formula-projective-bundle-pushforward" tags="formula"}
For a rank-$r$ bundle $E$ on smooth $X/\mathbb C$, use the quotient convention for $\pi:\mathbb P(E)\to X$ and $\xi=c_1(\mathcal O(1))$. Compute $\pi_*\xi^{r-1+j}$ for $0\le j\le3$.
:::

::: {.back card-id="formula-projective-bundle-pushforward"}
$$\begin{aligned}\pi_*\xi^{r-1}&=1,\\\pi_*\xi^r&=c_1(E),\\\pi_*\xi^{r+1}&=c_1(E)^2-c_2(E),\\\pi_*\xi^{r+2}&=c_1(E)^3-2c_1(E)c_2(E)+c_3(E).\end{aligned}$$
:::

::: {.front card-id="formula-projective-bundle-canonical" tags="formula"}
For a rank-$r$ vector bundle $E$ on smooth $X/\mathbb C$, compute the canonical class of the quotient projective bundle $\pi:\mathbb P(E)\to X$, with $\xi=c_1(\mathcal O(1))$.
:::

::: {.back card-id="formula-projective-bundle-canonical"}
$$K_{\mathbb P(E)}=-r\xi+\pi^*(K_X+c_1(E)).$$
:::

::: {.front card-id="formula-maximal-minors-class" tags="formula"}
For a map $E\to F$ of vector bundles of ranks $e\le f$ on smooth $X/\mathbb C$, suppose the locus $D_{e-1}$ of rank at most $e-1$ has codimension $f-e+1$. Compute its cycle class.
:::

::: {.back card-id="formula-maximal-minors-class"}
$$[D_{e-1}]=c_{f-e+1}(F-E)\cap[X],\qquad c(F-E)=c(F)c(E)^{-1}.$$
:::

::: {.front card-id="formula-hodge-index-inequality" tags="formula"}
For an ample divisor $H$ and any divisor $D$ on a smooth projective complex surface, give the numerical Hodge index inequality.
:::

::: {.back card-id="formula-hodge-index-inequality"}
$$(HD)^2\ge H^2D^2.$$
:::

::: {.front card-id="formula-nef-surface-volume" tags="formula"}
For a nef divisor $D$ on a smooth projective complex surface, compute its volume and bound its self-intersection.
:::

::: {.back card-id="formula-nef-surface-volume"}
$$\operatorname{vol}(D)=D^2\ge0.$$
:::

::: {.front card-id="formula-cyclic-cover-euler" tags="formula"}
For a smooth degree-$n$ cyclic cover $X\to Y$ of smooth projective complex varieties branched along smooth $B\in\lvert L^n\rvert$, compute the topological and holomorphic Euler characteristics of $X$.
:::

::: {.back card-id="formula-cyclic-cover-euler"}
$$e(X)=ne(Y)-(n-1)e(B),\qquad \chi(\mathcal O_X)=\sum_{i=0}^{n-1}\chi(Y,L^{-i}).$$
:::

::: {.front card-id="formula-hypersurface-threefold-invariants" tags="formula"}
For a smooth degree-$d$ hypersurface $X\subset\mathbb P^4_{\mathbb C}$, compute $H^3,K_X,c_2(X),c_3(X)$ and $e(X)$.
:::

::: {.back card-id="formula-hypersurface-threefold-invariants"}
$$\begin{aligned}H^3&=d,\qquad K_X=(d-5)H,\\c_2(X)&=(d^2-5d+10)H^2,\\c_3(X)&=(-d^3+5d^2-10d+10)H^3,\\e(X)&=d(-d^3+5d^2-10d+10).\end{aligned}$$
:::

::: {.front card-id="formula-quintic-threefold-invariants" tags="formula"}
For a smooth quintic threefold $X\subset\mathbb P^4_{\mathbb C}$, compute $K_X,H^3,c_2(X)H,e(X)$ and $\chi(\mathcal O_X(mH))$.
:::

::: {.back card-id="formula-quintic-threefold-invariants"}
$$K_X\sim0,\quad H^3=5,\quad c_2(X)H=50,\quad e(X)=-200,\quad \chi(\mathcal O_X(mH))=\frac{5m^3+25m}{6}.$$
:::

::: {.front card-id="formula-grassmannian-degree" tags="formula"}
Compute the Plücker degree of $\operatorname{Gr}(k,n)$, parametrizing $k$-dimensional subspaces of $\mathbb C^n$, for $1\le k<n$.
:::

::: {.back card-id="formula-grassmannian-degree"}
$$\deg\operatorname{Gr}(k,n)=\frac{(k(n-k))!\prod_{i=0}^{k-1}i!}{\prod_{i=0}^{k-1}(n-k+i)!}.$$
:::

::: {.front card-id="formula-grassmannian-two-planes-degree" tags="formula"}
Compute the Plücker degree of $\operatorname{Gr}(2,n)$ and its values for $n=4,5,6$.
:::

::: {.back card-id="formula-grassmannian-two-planes-degree"}
$$\deg\operatorname{Gr}(2,n)=\frac1{n-1}\binom{2n-4}{n-2},\qquad \deg\operatorname{Gr}(2,4)=2,\quad \deg\operatorname{Gr}(2,5)=5,\quad \deg\operatorname{Gr}(2,6)=14.$$
:::

::: {.front card-id="formula-hypersurface-discriminant-degree" tags="formula"}
For $n\ge1,d\ge2$, compute the degree of the discriminant hypersurface of singular degree-$d$ hypersurfaces in $\mathbb P^n_{\mathbb C}$.
:::

::: {.back card-id="formula-hypersurface-discriminant-degree"}
$$\deg\Delta_{n,d}=(n+1)(d-1)^n.$$
:::

::: {.front card-id="formula-veronese-degree" tags="formula"}
Compute the degree of the image of $\mathbb P^n_{\mathbb C}$ under the $d$-uple Veronese embedding, $d\ge1$.
:::

::: {.back card-id="formula-veronese-degree"}
$$\deg\nu_d(\mathbb P^n)=d^n.$$
:::

::: {.front card-id="formula-segre-degree" tags="formula"}
Compute the degree of $\mathbb P^m_{\mathbb C}\times\mathbb P^n_{\mathbb C}$ in its Segre embedding.
:::

::: {.back card-id="formula-segre-degree"}
$$\deg\operatorname{Seg}(\mathbb P^m\times\mathbb P^n)=\binom{m+n}{m}.$$
:::

