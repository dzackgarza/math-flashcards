---
title: "Algebraic Geometry::Moduli::Stable Pairs"
---

::: {.front card-id="pairs-log-positivity-comparison" tags="definition comparison example"}
Compare log Fano, log Calabi–Yau, log general type, and stable pairs. Where does an auxiliary polarizing divisor enter?
:::

::: {.back card-id="pairs-log-positivity-comparison"}
$X/\mathbb C$ normal projective, $\Delta\ge0$ a rational boundary, $K_X+\Delta$ $\mathbb Q$-Cartier:

| Name | Positivity condition |
| --- | --- |
| Log Fano | $-(K_X+\Delta)$ ample |
| Log Calabi–Yau | $K_X+\Delta\sim_{\mathbb Q}0$ |
| Log general type | $K_X+\Delta$ big |

State the singularity condition separately: “klt log Fano” and “lc log Fano” differ. Numerical log Calabi–Yau means $K_X+\Delta\equiv0$; it is not the definition of $\mathbb Q$-linear triviality.

A **stable pair** allows demi-normal $X$: $(X,\Delta)$ slc, $X$ projective, $K_X+\Delta$ ample.

A boundary-polarized log Calabi–Yau pair adds an effective ample $\mathbb Q$-Cartier divisor $B$ with $(X,\Delta+\epsilon B)$ slc for every $0<\epsilon<\epsilon_0$ for some $\epsilon_0>0$. These perturbed pairs are stable.

Example: $(\mathbb P^1,\{0\}+\{\infty\})$ is log Calabi–Yau; adding $\epsilon\{1\}$ gives log-canonical degree $\epsilon>0$.
:::

::: {.front card-id="pairs-mumford-kflat" tags="definition comparison"}
For a flat projective family with reduced $S_2$ fibers, define a relative Mumford divisor and give a precise K-flatness test in characteristic zero.
:::

::: {.back card-id="pairs-mumford-kflat"}
A relative Mumford divisor $D$ is the scheme-theoretic closure of a relative effective Cartier divisor on $U\subset X$, where $\operatorname{codim}_{X_s}(X_s\setminus U_s)\ge2$ for all $s$; $X_s$ is smooth at every generic point of $D_s$. Divisorial base change takes this closure again.

For local $S$ with infinite residue field and pure relative dimension $n$, test **every** finite $\pi:X\to\mathbb P^n_S$ whose restriction on reduced $D$ is birational onto its image and which is étale at the generic points of $D_s$. K-flatness means each scheme-theoretic image $\pi(D)$ is a relative Cartier divisor. For general $S$, test after localization; finite residue fields require a flat local extension with infinite residue field.

Reference: [Kollár, *Families of varieties of general type*, Definitions 4.68 and 7.1](https://web.math.princeton.edu/~kollar/FromMyHomePage/modbook-final.pdf).
:::

::: {.front card-id="pairs-ksba-family-kollar" tags="definition comparison"}
State the family conditions for rational-coefficient KSBA pairs, including Kollár's condition. Why is checking the geometric fibers alone insufficient?
:::

::: {.back card-id="pairs-ksba-family-kollar"}
Over a $\mathbb Q$-scheme $S$, fix labeled $\Delta=\sum a_iD_i$, $a_i\in\mathbb Q\cap(0,1]$, and $N=\operatorname{lcm}(\operatorname{denom}a_i)$.

- $f:X\to S$ flat, proper, finite type, pure relative dimension.
- $D_i$ K-flat relative Mumford divisors.
- Every geometric $(X_s,\Delta_s)$ slc.
- $K_{X/S}+\Delta$ relatively ample.
- For every $m\in N\mathbb Z$ and $B=\sum_{j\in J}D_j$ with $a_j=1$, the divisorial sheaf $\omega_{X/S}^{[m]}(m\Delta-B)$ is $S$-flat and its formation commutes with every base change.

The last condition controls infinitesimal families and specialization of pluricanonical sheaves. Fiberwise slc and ampleness do not impose it. Brackets mean reflexive/divisorial extension of the tensor power from the relative Gorenstein locus.

Reference: [Kollár, *Families of varieties of general type*, §8.2, Definition 8.7](https://web.math.princeton.edu/~kollar/FromMyHomePage/modbook-final.pdf).
:::

::: {.front card-id="pairs-qg-deformations-index-cover" tags="definition construction example"}
Define an index-one cover and a $\mathbb Q$-Gorenstein deformation. How does the index-one covering stack organize the construction?
:::

::: {.back card-id="pairs-qg-deformations-index-cover"}
Let $(X,x)$ be a normal complex germ with $K_X$ of Cartier index $r$. Shrink and trivialize $\mathcal O_X(rK_X)$. The canonical cyclic algebra gives
$$\widetilde X=\operatorname{Spec}_X\bigoplus_{i=0}^{r-1}\mathcal O_X(-iK_X),$$
with reflexive multiplication and reduction of exponents using the trivialization. It has a $\mu_r$-action, quotient $X$, and Cartier canonical class; it is unramified in codimension one. “Index-one” means Cartier canonical class; Gorenstein additionally requires Cohen–Macaulayness.

A $\mathbb Q$-Gorenstein deformation is locally induced by a $\mu_r$-equivariant deformation of these covers. For a flat family $X\to S$ of finite type over $\mathbb C$ with demi-normal fibers, the relative formulation requires every divisorial power $\omega_{X/S}^{[m]}$ to be flat over $S$ and commute with arbitrary base change, with some positive power invertible. Here the divisorial power is extended from the relative Gorenstein locus; $m$ ranges over all integers.

The local stacks $[\widetilde X/\mu_r]$ glue to the **index-one covering stack**. A family is “almost lci” in Alexeev's usage when its index-one covering stack is lci over the base.

Example: $\frac13(1,1)=\mathbb A^2/\mu_3$ has index three and canonical cover $\mathbb A^2$.

Reference: Alexeev, *Kappa classes on KSBA spaces*, §2; Hacking, *Compact moduli of plane curves*, §3.
:::

::: {.front card-id="pairs-weight-chambers-models" tags="definition construction example"}
Define a chamber for varying stable-pair coefficients and describe reduction to smaller weights. Why is the contraction part of the operation?
:::

::: {.back card-id="pairs-weight-chambers-models"}
For fixed labeled divisors $D_i$, vary $b$ in a rational weight domain where the log canonical models exist. A chamber is a region where the resulting marked log canonical model is unchanged; walls occur when singularity or positivity inequalities become equalities.

For $c_i\le b_i$, form the log canonical model at the smaller weights:
$$X_c=\operatorname{Proj}\bigoplus_{m\ge0}
H^0\!\left(X,\mathcal O_X\!\left(mN(K_X+\sum c_iD_i)\right)\right),$$
where $N$ clears denominators and the divisor is big with finitely generated ring. Contract the curves on which the model map has degree zero; retain the images of the labeled divisors. Merely changing coefficients can destroy ampleness.

For weighted curves, a rational tail carrying new total weight at most one contracts. For hyperplane arrangements the walls come from $\sum_{i\in I}b_i=k$, with $k$ an incidence codimension. Global reduction morphisms require the corresponding moduli construction; they are not asserted for arbitrary weight changes.

Reference: Alexeev, *Moduli of Weighted Hyperplane Arrangements*, Chapters 1 and 5.
:::

::: {.front card-id="ksba-kappa-cycle-cm" tags="definition formula example"}
Define higher-dimensional $\kappa$-classes of a KSBA family as Chow cycles. Identify $\kappa_0$ and the CM class, with a normalization.
:::

::: {.back card-id="ksba-kappa-cycle-cm"}
$f:(X,D)\to S$ a KSBA family of relative dimension $d$, $S$ equidimensional of dimension $s$; $L=K_{X/S}+D$ a $\mathbb Q$-line bundle. With rational Chow coefficients:
$$\kappa_i(S)=f_*\bigl(c_1(L)^{d+i}\cap[X]\bigr)
\in\operatorname{CH}_{s-i}(S)_{\mathbb Q}.$$
Compute using an invertible multiple $NL$, dividing its $(d+i)$th power by $N^{d+i}$.

- $\kappa_0=v[S]$, $v=(K_{X_s}+D_s)^d$ on each component with fixed volume.
- For smooth $S$, identify this cycle with a codimension-$i$ Chow class.
- Canonical-polarization normalization: $c_1(\lambda_{\mathrm{CM}})=\kappa_1$. The rational line bundle can be constructed by the $(d+1)$-fold Deligne pairing of $L$. Other CM conventions may multiply by a constant.

Example: for a constant family with boundary pulled back from its fiber, $\kappa_i=0$ for $i>0$, since powers above the fiber dimension vanish.

Reference: Alexeev, *Kappa classes on KSBA spaces*, Definitions 2.3–2.6.
:::

::: {.front card-id="ksba-operational-chow-gysin" tags="definition comparison construction"}
Distinguish Chow cycles, operational Chow classes, and the cohomological $\kappa$ construction. What changes when the base is singular?
:::

::: {.back card-id="ksba-operational-chow-gysin"}
An operational class $c\in A^i(S)$ gives, for every $g:T\to S$, operators
$$c_g:\operatorname{CH}_k(T)\to\operatorname{CH}_{k-i}(T)$$
compatible with proper pushforward, flat pullback, and refined Gysin pullback. A cycle on $S$ alone is not such a system.

For smooth $s$-dimensional $S$, capping with $[S]$ identifies $A^i(S)$ with $\operatorname{CH}_{s-i}(S)$. This identification fails in general for singular $S$.

For proper $f:X\to S$ of pure relative dimension $d$ with $S/\mathbb C$ smooth, define the cohomological pushforward on the relevant classes by
$$H^{2(d+i)}(X,\mathbb Q)\xrightarrow{\cap[X]}
H^{\mathrm{BM}}_{2s-2i}(X,\mathbb Q)\xrightarrow{f_*}
H^{\mathrm{BM}}_{2s-2i}(S,\mathbb Q)\cong H^{2i}(S,\mathbb Q).$$
Apply it to $c_1(K_{X/S}+D)^{d+i}$. The final isomorphism uses smoothness of $S$. Arbitrary-base-change compatibility does not follow just from writing this formula; lci families provide refined Gysin tools for that question.

Reference: Alexeev, *Kappa classes on KSBA spaces*, Definitions 2.6–2.8.
:::

::: {.front card-id="ksba-generalized-hodge-line" tags="definition formula"}
Define the generalized Hodge line bundle for a log Calabi–Yau family. Relate it to the CM class after adding a small polarization.
:::

::: {.back card-id="ksba-generalized-hodge-line"}
For $f:(X,\Delta+\epsilon B)\to S$ in the log Calabi–Yau moduli setting, the generalized Hodge $\mathbb Q$-line bundle $\lambda$ is characterized by
$$K_{X/S}+\Delta=f^*\lambda.$$
For a smooth connected family with trivial canonical bundles, it recovers $f_*\omega_{X/S}$ when evaluation is an isomorphism. Fiberwise numerical triviality alone is not a definition of this pullback identity.

Write $d=\dim X_s$, $v_B=B_s^d$. Expanding the $(d+1)$th power and pushing forward gives
$$\kappa_1(\epsilon)
=(d+1)\epsilon^d v_B\,c_1(\lambda)+\epsilon^{d+1}f_*(B^{d+1}).$$
Terms with fewer than $d$ fiber-divisor factors push forward to zero. This relates the Hodge class to the CM class without identifying the two normalizations.

Reference: Alexeev, *Kappa classes on KSBA spaces*, Definition 2.9.
:::
