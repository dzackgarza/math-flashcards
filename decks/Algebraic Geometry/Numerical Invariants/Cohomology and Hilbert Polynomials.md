---
title: "Algebraic Geometry::Numerical Invariants::Cohomology and Hilbert Polynomials"
---

::: {.front card-id="hilbert-coefficient-meaning" tags="formula"}
For a nonempty projective scheme $X$ over a field, polarized by a very ample divisor $H$, what do the degree, leading coefficient, and constant term of $P_{X,H}(m)$ record?
:::

::: {.back card-id="hilbert-coefficient-meaning"}
Writing $n=\dim X$,
$$\deg P_{X,H}=n,\qquad [m^n]P_{X,H}=\frac{\deg_H X}{n!},\qquad P_{X,H}(0)=\chi(X,\mathcal O_X).$$
Degree includes scheme-theoretic multiplicities. The constant term is the coherent Euler characteristic, not the topological Euler characteristic.
:::

::: {.front card-id="hilbert-function-comparison" tags="formula"}
For a projective scheme $X$ with a very ample line bundle $\mathcal O_X(1)$, when does $P_X(m)$ equal $\chi(\mathcal O_X(m))$, and when does it equal $h^0(\mathcal O_X(m))$?
:::

::: {.back card-id="hilbert-function-comparison"}
$$P_X(m)=\chi(\mathcal O_X(m))\quad\text{for every integer }m.$$
Serre vanishing gives $P_X(m)=h^0(\mathcal O_X(m))$ for $m\gg0$. Equality with $h^0$ in small degrees requires checking higher cohomology.
:::

::: {.front card-id="hilbert-todd-coefficients" tags="formula"}
For a smooth projective complex $n$-fold $X$ with ample divisor $H$, express every coefficient of $P_{X,H}(m)$ using Todd classes.
:::

::: {.back card-id="hilbert-todd-coefficients"}
$$P_{X,H}(m)=\int_X e^{mH}\operatorname{td}(T_X),\qquad [m^j]P_{X,H}=\frac1{j!}\int_X H^j\operatorname{td}_{n-j}(T_X).$$
Here $\operatorname{td}_i$ denotes the codimension-$i$ component. The lower coefficients generally record combinations of characteristic numbers.
:::

::: {.front card-id="hilbert-arithmetic-genus" tags="formula"}
For a projective scheme $X$ of dimension $n$, how does its arithmetic genus relate to the constant term of its Hilbert polynomial?
:::

::: {.back card-id="hilbert-arithmetic-genus"}
$$p_a(X)=(-1)^n\bigl(P_X(0)-1\bigr).$$
For a curve, $P_C(0)=1-p_a(C)$; for a surface, $P_S(0)=1+p_a(S)$.
:::

::: {.front card-id="hilbert-curve-polynomial" tags="formula"}
For a projective curve $C$ of degree $d$ and arithmetic genus $p_a(C)$, compute its Hilbert polynomial.
:::

::: {.back card-id="hilbert-curve-polynomial"}
$$P_C(m)=dm+1-p_a(C).$$
For a smooth connected curve, $p_a(C)=g(C)$. For a singular integral curve, the constant term determines arithmetic genus, not the genus of its normalization.
:::

::: {.front card-id="hilbert-surface-polynomial" tags="formula"}
For a smooth projective complex surface $S$ with ample divisor $H$, compute $P_{S,H}(m)$ and interpret its coefficients.
:::

::: {.back card-id="hilbert-surface-polynomial"}
$$P_{S,H}(m)=\frac{H^2}{2}m^2-\frac{K_S\cdot H}{2}m+\chi(\mathcal O_S).$$
The quadratic coefficient gives half the degree; the linear coefficient gives $-K_S\cdot H/2$; the constant term gives $1-q+p_g$.
:::

::: {.front card-id="hilbert-finite-scheme" tags="formula"}
What is the Hilbert polynomial of a zero-dimensional projective scheme $Z$ over an algebraically closed field?
:::

::: {.back card-id="hilbert-finite-scheme"}
$$P_Z(m)=\operatorname{length}(Z).$$
A nonreduced point contributes its local length, not just one.
:::

::: {.front card-id="hilbert-plane-curves" tags="formula"}
Compute the Hilbert polynomial of a degree-$d$ plane curve, and specialize to a line, conic, cubic, and quartic.
:::

::: {.back card-id="hilbert-plane-curves"}
$$P_C(m)=dm+\frac{d(3-d)}2.$$
| Curve | Hilbert polynomial |
| --- | --- |
| Line | $m+1$ |
| Conic | $2m+1$ |
| Cubic | $3m$ |
| Quartic | $4m-2$ |

The formula holds for every plane hypersurface of degree $d$, including singular and nonreduced ones.
:::

::: {.front card-id="hilbert-rational-normal" tags="formula"}
What is the Hilbert polynomial of the rational normal curve of degree $d$ in $\mathbb P^d$? Specialize to the twisted cubic.
:::

::: {.back card-id="hilbert-rational-normal"}
$$P_C(m)=dm+1.$$
The twisted cubic has $P_C(m)=3m+1$.
:::

::: {.front card-id="hilbert-veronese" tags="formula"}
What is the Hilbert polynomial of $\mathbb P^n$ embedded by $\mathcal O(d)$, for $d\ge1$? Specialize to the Veronese surface in $\mathbb P^5$.
:::

::: {.back card-id="hilbert-veronese"}
$$P(m)=\binom{dm+n}{n}.$$
For the quadratic Veronese surface, $P(m)=2m^2+3m+1$, so its degree is $4$.
:::

::: {.front card-id="hilbert-segre" tags="formula"}
Compute the Hilbert polynomial of $\mathbb P^a\times\mathbb P^b$ in its Segre embedding. Specialize to the smooth quadric surface.
:::

::: {.back card-id="hilbert-segre"}
$$P(m)=\binom{m+a}{a}\binom{m+b}{b}.$$
For $\mathbb P^1\times\mathbb P^1$ with $\mathcal O(1,1)$, $P(m)=(m+1)^2$.
:::

::: {.front card-id="hilbert-k3" tags="formula"}
For a complex K3 surface $S$ with ample line bundle $L$ satisfying $L^2=2g-2$, compute $P_{S,L}(m)$. Specialize to a quartic surface.
:::

::: {.back card-id="hilbert-k3"}
$$P_{S,L}(m)=(g-1)m^2+2.$$
A smooth quartic surface with its hyperplane polarization has $P(m)=2m^2+2$.
:::

::: {.front card-id="hilbert-abelian" tags="formula"}
For a complex abelian variety $A$ of dimension $g$ with ample line bundle $L$, compute $P_{A,L}(m)$.
:::

::: {.back card-id="hilbert-abelian"}
$$P_{A,L}(m)=\frac{c_1(L)^g}{g!}m^g.$$
The tangent bundle is trivial, so its Todd class is $1$. For a principal polarization, $P_{A,L}(m)=m^g$.
:::

::: {.front card-id="hilbert-repolarization" tags="formula"}
If $L$ is ample and $a>0$, how does replacing $L$ by $L^{\otimes a}$ change the Hilbert polynomial and degree on an $n$-dimensional projective scheme?
:::

::: {.back card-id="hilbert-repolarization"}
$$P_{X,L^{\otimes a}}(m)=P_{X,L}(am),\qquad \deg_{L^{\otimes a}}X=a^n\deg_LX.$$
The coefficient of $m^j$ is multiplied by $a^j$; the constant term is unchanged.
:::

::: {.front card-id="hilbert-hyperplane-difference" tags="formula"}
Let $Y\subset X$ be an effective Cartier divisor in $|\mathcal O_X(1)|$ on a projective scheme. Express $P_Y$ in terms of $P_X$.
:::

::: {.back card-id="hilbert-hyperplane-difference"}
$$P_Y(m)=P_X(m)-P_X(m-1).$$
Use $0\to\mathcal O_X(m-1)\to\mathcal O_X(m)\to\mathcal O_Y(m)\to0$.
:::

::: {.front card-id="hilbert-read-curve" tags="application"}
An integral projective curve has Hilbert polynomial $7m-5$. Recover its degree and arithmetic genus. Does this determine its geometric genus?
:::

::: {.back card-id="hilbert-read-curve"}
$$\deg C=7,\qquad p_a(C)=6.$$
If $C$ is smooth, its genus is $6$. If it is singular over $\mathbb C$, its normalization has genus $6-\sum_p\delta_p$, which the polynomial alone does not determine.
:::

::: {.front card-id="hilbert-read-surface" tags="application"}
A smooth projective complex surface with very ample divisor $H$ has $P(m)=3m^2+2$. Recover $H^2$, $K_S\cdot H$, $\chi(\mathcal O_S)$, and the genus of a smooth connected hyperplane section. Does this prove $K_S$ is trivial?
:::

::: {.back card-id="hilbert-read-surface"}
$$H^2=6,\qquad K_S\cdot H=0,\qquad \chi(\mathcal O_S)=2,\qquad g(H)=1+\frac{H^2+K_S\cdot H}{2}=4.$$
The single intersection $K_S\cdot H=0$ does not prove that $K_S$ is trivial.
:::

::: {.front card-id="hilbert-read-threefold" tags="application"}
A smooth projective complex threefold with very ample divisor $H$ has $P(m)=\frac56m^3+\frac{25}6m$. Recover $H^3$, $K_XH^2$, $H(K_X^2+c_2(X))$, and $\chi(\mathcal O_X)$.
:::

::: {.back card-id="hilbert-read-threefold"}
$$H^3=5,\qquad K_XH^2=0,\qquad H(K_X^2+c_2(X))=50,\qquad \chi(\mathcal O_X)=0.$$
These are coefficient identities; they do not identify the threefold or prove $K_X\sim0$.
:::

::: {.front card-id="hilbert-small-degree" tags="application"}
A smooth plane cubic has $P_C(m)=3m$. Why does $P_C(0)=0$ not imply $H^0(C,\mathcal O_C)=0$?
:::

::: {.back card-id="hilbert-small-degree"}
$$h^0(C,\mathcal O_C)=h^1(C,\mathcal O_C)=1,\qquad \chi(\mathcal O_C)=0.$$
The polynomial gives Euler characteristic in every degree and the section count only in sufficiently large degrees.
:::

::: {.front card-id="hilbert-integer-valued" tags="formula"}
Must the coefficients of a Hilbert polynomial in the monomial basis be integers? Give a basic example.
:::

::: {.back card-id="hilbert-integer-valued"}
No. Hilbert polynomials are integer-valued on integers, but can have rational coefficients:
$$P_{\mathbb P^2}(m)=\binom{m+2}{2}=\frac12m^2+\frac32m+1.$$
:::

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
