---
title: "Algebraic Geometry::Covers"
---

::: {.front card-id="covers-galois-flat-inertia" tags="definition comparison example"}
Define an abelian $G$-cover and its branch inertia data. Which extra assumption makes its character eigensheaves line bundles?
:::

::: {.back card-id="covers-galois-flat-inertia"}
$k$ algebraically closed, $G$ finite abelian, $\operatorname{char}k\nmid|G|$. A $G$-cover is a finite quotient map $\pi:X\to Y=X/G$ with generically free $G$-action; varieties may be reducible or nonnormal. For normal integral varieties this is a Galois extension $k(X)/k(Y)$ with specified group $G$.

For a prime branch divisor $D$ of a normal cover, $H_D\subset G$ fixes a ramification component pointwise. It is cyclic; its action on the normal direction gives a generating character $\psi_D\in H_D^*$. The pair $(H_D,\psi_D)$ is the inertia datum; the order alone loses information.

The character decomposition is
$$\pi_*\mathcal O_X=\bigoplus_{\chi\in G^*}\mathcal F_\chi,\qquad
\mathcal F_1=\mathcal O_Y.$$
The $\mathcal F_\chi$ have generic rank one. Finite flatness makes them invertible; write $\mathcal F_\chi=L_\chi^{-1}$. Normality of $Y$ alone does not imply flatness.

Reference: Alexeev–Pardini, *Non-normal abelian covers*, §1; *On the existence of ramified abelian covers*, §2.
:::

::: {.front card-id="covers-building-data-standard" tags="definition construction"}
State the building data and fundamental relations of a standard abelian cover. How do they define the covering algebra?
:::

::: {.back card-id="covers-building-data-standard"}
Over algebraically closed $k$ with $|G|$ invertible, choose effective Cartier divisors $D_i$, cyclic subgroups $H_i$ of orders $m_i$, generators $\psi_i\in H_i^*$, and line bundles $L_\chi$ with $L_1=\mathcal O_Y$.

Write $\chi|_{H_i}=\psi_i^{a_i(\chi)}$, $0\le a_i(\chi)<m_i$, and put
$$\varepsilon_i(\chi,\chi')=
\left\lfloor\frac{a_i(\chi)+a_i(\chi')}{m_i}\right\rfloor.$$
Choose compatible isomorphisms
$$L_\chi\otimes L_{\chi'}\simeq
L_{\chi\chi'}\otimes\mathcal O_Y\!\left(\sum_i\varepsilon_i(\chi,\chi')D_i\right).$$
Multiplication by the indicated products of divisor sections gives associative maps
$$L_\chi^{-1}\otimes L_{\chi'}^{-1}\longrightarrow L_{\chi\chi'}^{-1}.$$
The **standard cover** is $\operatorname{Spec}_Y\bigoplus_\chi L_\chi^{-1}$ with this algebra structure. Line-bundle classes alone do not specify the multiplication isomorphisms. Repeated branch components can produce nonnormal covers.

For $G=\mathbb Z/2$: $L^2\simeq\mathcal O_Y(D)$ and the algebra is $\mathcal O_Y\oplus L^{-1}$ with local equation $z^2=s_D$.

Reference: Alexeev–Pardini, *Non-normal abelian covers*, §1.2.
:::

::: {.front card-id="covers-bidouble-data" tags="construction application"}
Construct a bidouble cover from three branch divisors. Write its line-bundle relations and local equations.
:::

::: {.back card-id="covers-bidouble-data"}
$G=(\mathbb Z/2)^2$, $k$ algebraically closed of characteristic $\ne2$. Label nonzero elements $g_1,g_2,g_3$ and characters $\chi_i$ with $\ker\chi_i=\langle g_i\rangle$. For branch divisors $D_i$ labeled by $g_i$:
$$2L_i\sim D_j+D_k,\qquad L_i+L_j\sim L_k+D_k
\quad(\{i,j,k\}=\{1,2,3\}).$$
With compatible trivializations and local equations $d_i$:
$$z_i^2=d_jd_k,\qquad z_iz_j=d_kz_k.$$
The rank-four algebra is $\mathcal O_Y\oplus L_1^{-1}\oplus L_2^{-1}\oplus L_3^{-1}$.

On a smooth surface, reduced SNC branch with distinct labels at each crossing and no triple points gives a smooth cover. Locally at a crossing of two labels, the map is $(u,v)\mapsto(u^2,v^2)$. At a collision of equal labels, this local smoothness test fails.

Reference: Alexeev–Pardini, *Explicit compactifications of moduli spaces of Campedelli and Burniat surfaces*, §2.
:::

::: {.front card-id="covers-total-ramification-hurwitz" tags="definition formula example"}
Define total ramification for an abelian cover and its Hurwitz boundary. Distinguish total ramification from ramification at every point.
:::

::: {.back card-id="covers-total-ramification-hurwitz"}
For a tame normal abelian cover $\pi:X\to Y$:

- **Totally ramified:** the inertia subgroups of the prime branch divisors generate $G$. This is a global generation condition.
- If the branch order along $D_i$ is $m_i$, the Hurwitz boundary is
$$B=\sum_i(1-1/m_i)D_i,\qquad K_X=\pi^*(K_Y+B).$$
The equality is of rational divisors after compatible canonical choices, when the pullback is defined, for example $Y$ smooth.

A connected étale isogeny of positive degree is not totally ramified. A connected double cover with a nonempty branch divisor is totally ramified, although most points are unramified.

For nonnormal standard covers, the coefficient along $D$ is instead the sum $\sum_i(1-1/m_i)\operatorname{mult}_D D_i$ over the building divisors; coincident branch components matter.

Reference: Alexeev–Pardini, *On the existence of ramified abelian covers*, §2; *Non-normal abelian covers*, §2.1.
:::

::: {.front card-id="covers-toric-lattice" tags="definition construction example"}
What is a finite toric cover? Recover its group and branch orders from an inclusion of lattices.
:::

::: {.back card-id="covers-toric-lattice"}
Fix a fan $\Sigma$ in $N_{\mathbb R}$ and a finite-index sublattice $N'\subset N$. The same cones give a finite toric map
$$X_{\Sigma,N'}\longrightarrow X_{\Sigma,N}.$$
For dual lattices $M\subset M'$, the kernel on dense tori is the diagonalizable group with character group $M'/M$. In characteristic prime to $[N:N']$ it is finite étale.

If $v_\rho$ is primitive in $N$ and $v'_\rho=e_\rho v_\rho$ primitive in $N'$, the ramification order along the invariant divisor for $\rho$ is $e_\rho$.

Example: $N'=m\mathbb Z\subset\mathbb Z$ and the complete one-dimensional fan give $\mathbb P^1\to\mathbb P^1$, $z\mapsto z^m$, branched at $0,\infty$ with order $m$.

Reference: Alexeev–Pardini, *On the existence of ramified abelian covers*, §3.
:::
