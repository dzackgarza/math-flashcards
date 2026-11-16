---
title: "Algebraic Geometry::Numerical Invariants::Chow Groups and Rings"
---

::: {.front card-id="standard-chow-conventions" tags="formula"}
For a smooth complex variety $X$ of pure dimension $n$, relate $\operatorname{CH}_i(X)$, $\operatorname{CH}^j(X)$, and $\operatorname{Pic}(X)$.
:::

::: {.back card-id="standard-chow-conventions"}
$$\operatorname{CH}^j(X)=\operatorname{CH}_{n-j}(X),\qquad\operatorname{CH}^1(X)\cong\operatorname{Pic}(X).$$
Chow groups use rational equivalence. Unless a coefficient subscript is supplied, they have integral coefficients; $\operatorname{CH}^*(X)_{\mathbb Q}=\operatorname{CH}^*(X)\otimes\mathbb Q$.
:::

::: {.front card-id="standard-chow-affine" tags="formula"}
Compute the Chow ring of $\mathbb A^n_{\mathbb C}$. Does a closed point generate a nonzero zero-cycle class for $n>0$?
:::

::: {.back card-id="standard-chow-affine"}
$$\operatorname{CH}^*(\mathbb A^n)=\mathbb Z\quad\text{in codimension }0.$$
For $n>0$, $\operatorname{CH}_0(\mathbb A^n)=0$. The degree map on zero-cycles requires properness to descend to rational equivalence.
:::

::: {.front card-id="standard-chow-curves" tags="formula"}
Describe the integral Chow ring of a smooth connected projective complex curve $C$.
:::

::: {.back card-id="standard-chow-curves"}
$$\operatorname{CH}^0(C)=\mathbb Z,\qquad\operatorname{CH}^1(C)=\operatorname{Pic}(C),\qquad\operatorname{CH}^i(C)=0\ (i>1).$$
$\alpha\beta=0$ for $\alpha,\beta\in\operatorname{CH}^{>0}(C)$, and $\ker(\deg:\operatorname{CH}_0(C)\to\mathbb Z)\cong\operatorname{Jac}(C)(\mathbb C)$.
:::

::: {.front card-id="standard-chow-hirzebruch" tags="formula"}
Give the integral Chow ring of $\mathbb F_e$ in terms of its minimal section $s$ and a fiber $f$.
:::

::: {.back card-id="standard-chow-hirzebruch"}
$$\operatorname{CH}^*(\mathbb F_e)=\mathbb Z[s,f]/(f^2,s^2+esf),\qquad\deg(sf)=1.$$
Both generators have codimension one; $s^2=-e$ as an intersection number.
:::

::: {.front card-id="standard-chow-plane-blowup" tags="formula"}
Give the integral Chow ring of the blowup of $\mathbb P^2_{\mathbb C}$ at $r$ distinct points, with pullback hyperplane class $h$ and exceptional classes $e_i$.
:::

::: {.back card-id="standard-chow-plane-blowup"}
$$\operatorname{CH}^*(S)=
\frac{\mathbb Z[h,e_1,\ldots,e_r]}
{(h^3,\ he_i,\ e_ie_j\ (i\ne j),\ e_i^2+h^2)}.$$
All generators have codimension one, and $\deg(h^2)=1$.
:::

::: {.front card-id="standard-chow-blowup-groups" tags="formula"}
For the blowup of a smooth complex variety $X$ along a smooth center $Z$ of codimension $c\ge2$, state the additive Chow-group formula.
:::

::: {.back card-id="standard-chow-blowup-groups"}
$$\operatorname{CH}^k(\operatorname{Bl}_ZX)\cong\operatorname{CH}^k(X)\oplus\bigoplus_{i=1}^{c-1}\operatorname{CH}^{k-i}(Z).$$
This is an additive decomposition, not a direct-product presentation of rings.
:::

::: {.front card-id="standard-chow-quadrics" tags="formula"}
Describe the ranks of the integral Chow groups of a smooth complex quadric $Q^n$. Does the hyperplane class generate its integral Chow ring?
:::

::: {.back card-id="standard-chow-quadrics"}
Each $\operatorname{CH}^i(Q^n)$ is free of rank one for $0\le i\le n$, except that the middle group has rank two when $n$ is even. The cycle map identifies these groups with $H^{2i}(Q^n,\mathbb Z)$. For $n\ge1$ the hyperplane class does not generate the integral ring: $h^n=2[\mathrm{pt}]$.
:::

::: {.front card-id="standard-chow-quadric-threefold" tags="formula"}
Give generators and relations for the integral Chow ring of a smooth complex quadric threefold.
:::

::: {.back card-id="standard-chow-quadric-threefold"}
With hyperplane class $h$ and line class $\ell$,
$$\operatorname{CH}^*(Q^3)=\mathbb Z[h,\ell]/(h^2-2\ell,\ell^2),\qquad\deg h=1,\quad\deg\ell=2.$$
Here grading means codimension. The point class is $h\ell$, and $\int h^3=2$.
:::

::: {.front card-id="standard-chow-grassmannian" tags="formula"}
Present the integral Chow ring of $\operatorname{Gr}(k,n)$ using the tautological subbundle $S$ and quotient bundle $Q$.
:::

::: {.back card-id="standard-chow-grassmannian"}
Write $s_i=c_i(S)$, $q_j=c_j(Q)$, $s_0=q_0=1$, and set out-of-range classes to zero. Then
$$\operatorname{CH}^*(\operatorname{Gr}(k,n))=
\frac{\mathbb Z[s_1,\ldots,s_k,q_1,\ldots,q_{n-k}]}
{\left(\sum_{i+j=m}s_iq_j:\ 1\le m\le n\right)}.$$
Schubert classes indexed by partitions in a $k\times(n-k)$ rectangle form an integral additive basis. The cycle map is an isomorphism onto even integral cohomology.
:::

::: {.front card-id="standard-chow-cycle-map" tags="formula"}
Is the cycle map $\operatorname{CH}^p(X)\to H^{2p}(X,\mathbb Z)$ always an isomorphism for smooth projective complex $X$? Give a counterexample in codimension one.
:::

::: {.back card-id="standard-chow-cycle-map"}
No. For a positive-genus curve, nontrivial elements of $\operatorname{Pic}^0(C)=\operatorname{CH}^1(C)_{\deg0}$ have zero first Chern class. On a surface, integral $(1,1)$ classes describe the image of $\operatorname{Pic}$, not all of $H^2$.
:::

::: {.front card-id="standard-chow-torsion" tags="formula"}
What happens to the canonical class of a complex Enriques surface under passage from $\operatorname{CH}^1(S)$ to $\operatorname{CH}^1(S)_{\mathbb Q}$?
:::

::: {.back card-id="standard-chow-torsion"}
It is a nonzero class of order $2$ in $\operatorname{CH}^1(S)=\operatorname{Pic}(S)$ and becomes zero after tensoring with $\mathbb Q$. Rational coefficients lose this information.
:::

::: {.front card-id="standard-chow-quadric-product-exercise" tags="formula"}
On $Q^2\cong\mathbb P^1\times\mathbb P^1$, compute the intersection of divisors of bidegrees $(2,3)$ and $(4,1)$ from the Chow ring.
:::

::: {.back card-id="standard-chow-quadric-product-exercise"}
Using $\operatorname{CH}^*(Q^2)=\mathbb Z[f_1,f_2]/(f_1^2,f_2^2)$,
$$(2f_1+3f_2)(4f_1+f_2)=14f_1f_2.$$
Their intersection number is $14$.
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

::: {.front card-id="formula-projective-bundle-chow" tags="formula"}
Let $X$ be smooth over $\mathbb C$ and $E$ have rank $r$. For the quotient bundle $\pi:\mathbb P(E)=\operatorname{Proj}(\operatorname{Sym}E)\to X$, set $\xi=c_1(\mathcal O(1))$. Compute the Chow ring.
:::

::: {.back card-id="formula-projective-bundle-chow"}
$$A^*(\mathbb P(E))=\frac{A^*(X)[\xi]}{\left(\sum_{i=0}^r(-1)^ic_i(E)\xi^{r-i}\right)}.$$
:::

