---
title: "Algebraic Geometry::Covers"
---

::: {.front card-id="covers-reflexive-torsion-twists" tags="construction example" cite="[@AEGS25, Remark 2.2 and Proposition 6.1]"}
How does a rank-one reflexive sheaf define a double cover of a normal variety? How can two covers have the same divisorial branch locus but differ over singular points?
:::

::: {.back card-id="covers-reflexive-torsion-twists"}
Over $\mathbb C$, choose a normal variety $Y$, a rank-one reflexive sheaf $A$, and a multiplication $A^{[2]}\to\mathcal O_Y$. Compose $A\otimes A\to A^{[2]}$ with this map and form
$$X=\operatorname{Spec}_Y(\mathcal O_Y\oplus A).$$
On the locus where $A$ is invertible this is $z^2=s$; the deck involution acts by $-1$ on $A$. Require normality of the resulting algebra when using normal-cover formulas. At singular points the cover need not be flat.

For a two-torsion class $T\in\operatorname{Cl}(Y)$, a chosen isomorphism $\mathcal O_Y(2T)\simeq\mathcal O_Y$ gives a cover unramified in codimension one. Twisting $A$ by $\mathcal O_Y(T)$, with reflexive tensor product, leaves $A^{[2]}$ unchanged but can alter the cover above the singular locus.

In the Enriques diagram, $\operatorname{Tors}\operatorname{Cl}(W)=\langle T\rangle\simeq\mathbb Z/2$. The sheaves $\mathcal O_W(K_W)$ and $\mathcal O_W(K_W+T)$, with multiplication given by $B_W\in|-2K_W|$, yield the K3 and Enriques intermediate covers. The torsion cover uses $\mathcal O_W\oplus\mathcal O_W(T)$.
:::

::: {.front card-id="covers-canonical-character-norm" tags="formula application" cite="[@AEGS25, Proposition 6.1, especially its eigensheaf and norm argument]"}
Let $\pi:(X,D)\to(Y,D_Y)$ be a connected double quotient of a proper normal log Calabi–Yau pair, unramified in codimension one, with $D=\pi^*D_Y$ reduced. How does the character on a log volume form decide the log canonical index downstairs?
:::

::: {.back card-id="covers-canonical-character-norm"}
Assume $K_X+D\sim0$, $H^0(X,\mathcal O_X)=\mathbb C$, and use reflexive sheaves across codimension two. Write
$$\pi_*\mathcal O_X=\mathcal O_Y\oplus A,$$
where $A$ is the nontrivial eigensheaf. On the étale locus $A^{\otimes2}\simeq\mathcal O_Y$, hence $A^{[2]}\simeq\mathcal O_Y$ globally.

| Character of a generator $\omega$ of $K_X+D$ | Descended sheaf | Consequence |
| --- | --- | --- |
| $+1$ | $\mathcal O_Y(K_Y+D_Y)\simeq\mathcal O_Y$ | Log canonical class trivial |
| $-1$ | $\mathcal O_Y(K_Y+D_Y)\simeq A$ | Nontrivial class of order two |

For the second row, $A\not\simeq\mathcal O_Y$: otherwise its global section would give a nonconstant anti-invariant regular function on proper connected $X$. The divisor norm also gives $2(K_Y+D_Y)\sim0$ from $\pi^*(K_Y+D_Y)\sim0$; the character decides whether the order is one or two.

For a finite surjective map of degree $d$, a $\mathbb Q$-Cartier divisor $H$ is ample, respectively nef, iff $\pi^*H$ is. On surfaces $(\pi^*H)^2=dH^2$. These formulas descend the polarization in the covering diagram.
:::

::: {.front card-id="covers-galois-flat-inertia" tags="definition comparison example" cite="[@AP12, §1; @AP13, §2]"}
Define an abelian $G$-cover and its branch inertia data. Which extra assumption makes its character eigensheaves line bundles?
:::

::: {.back card-id="covers-galois-flat-inertia"}
$k$ algebraically closed, $G$ finite abelian, $\operatorname{char}k\nmid|G|$. A $G$-cover is a finite quotient map $\pi:X\to Y=X/G$ with generically free $G$-action; varieties may be reducible or nonnormal. For normal integral varieties this is a Galois extension $k(X)/k(Y)$ with specified group $G$.

For a prime branch divisor $D$ of a normal cover, $H_D\subset G$ fixes a ramification component pointwise. It is cyclic; its action on the normal direction gives a generating character $\psi_D\in H_D^*$. The pair $(H_D,\psi_D)$ is the inertia datum; the order alone loses information.

The character decomposition is
$$\pi_*\mathcal O_X=\bigoplus_{\chi\in G^*}\mathcal F_\chi,\qquad
\mathcal F_1=\mathcal O_Y.$$
The $\mathcal F_\chi$ have generic rank one. Finite flatness makes them invertible; write $\mathcal F_\chi=L_\chi^{-1}$. Normality of $Y$ alone does not imply flatness.
:::

::: {.front card-id="covers-building-data-standard" tags="definition construction" cite="[@AP12, §1.2]"}
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

Example over $\mathbb C$: a smooth conic $D=(q_2=0)\subset\mathbb P^2$ has $L=\mathcal O(1)$. The double cover is the smooth quadric $w^2=q_2(x,y,z)$ in $\mathbb P^3$, hence $\mathbb P^1\times\mathbb P^1$.
:::

::: {.front card-id="covers-bidouble-data" tags="construction application" cite="[@AP23, §2]"}
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
:::

::: {.front card-id="covers-commuting-involutions-quotients" tags="construction application comparison" cite="[@AEGS25, §§2.1–2.2 and 6.4]"}
Two distinct commuting involutions act faithfully on a normal complex variety $X$. Recover the three intermediate double covers and their algebras from the character decomposition. Identify these quotients in the AEGS surface diagram. Must the eigensheaves be line bundles?
:::

::: {.back card-id="covers-commuting-involutions-quotients"}
The involutions generate $G\cong(\mathbb Z/2)^2$. Put $W=X/G$. Each nontrivial character $\chi$ has an order-two kernel $H_\chi$, giving
$$X\longrightarrow X/H_\chi\longrightarrow W.$$
For $\pi:X\to W$, write
$$\pi_*\mathcal O_X=\mathcal O_W\oplus\mathcal F_{\chi_1}\oplus\mathcal F_{\chi_2}\oplus\mathcal F_{\chi_3}.$$
Taking $H_\chi$-invariants gives the intermediate double-cover algebra
$$\bigl(\pi_*\mathcal O_X\bigr)^{H_\chi}=\mathcal O_W\oplus\mathcal F_\chi,$$
with multiplication inherited from the full covering algebra. Thus one bidouble cover packages all three double covers and their compatibility.

In the general AEGS construction, $X$ is a K3 double cover of $Y=\mathbb P^1\times\mathbb P^1$. Its involutions satisfy
$$\iota_{\mathrm{Nik}}=\iota_{\mathrm{dP}}\iota_{\mathrm{En}},\qquad
Y=X/\langle\iota_{\mathrm{dP}}\rangle,\quad
Z=X/\langle\iota_{\mathrm{En}}\rangle,\quad
Z'=X/\langle\iota_{\mathrm{Nik}}\rangle.$$
Here $Z$ is Enriques; all three intermediate surfaces map to $W=X/G$. The del Pezzo and Enriques involutions act by $-1$ on the holomorphic two-form, so their product acts by $+1$. The same commuting-involution construction organizes the ADE boundary quotients.

On a normal singular base, the character summands are rank-one reflexive sheaves; they need not be invertible. Finite flatness makes them line bundles. In AEGS, the cover algebras on $W$ use divisorial sheaves such as $\mathcal O_W(K_W)$ and $\mathcal O_W(K_W+A)$, with $A$ the nonzero torsion class in $\operatorname{Cl}(W)$; the smooth-base line-bundle recipe alone does not cover this case.
:::

::: {.front card-id="covers-total-ramification-hurwitz" tags="definition formula example" cite="[@AP13, §2; @AP12, §2.1]"}
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
:::

::: {.front card-id="covers-toric-lattice" tags="definition construction example" cite="[@AP13, §3]"}
What is a finite toric cover? Recover its group and branch orders from an inclusion of lattices.
:::

::: {.back card-id="covers-toric-lattice"}
Fix a fan $\Sigma$ in $N_{\mathbb R}$ and a finite-index sublattice $N'\subset N$. The same cones give a finite toric map
$$X_{\Sigma,N'}\longrightarrow X_{\Sigma,N}.$$
For dual lattices $M\subset M'$, the kernel on dense tori is the diagonalizable group with character group $M'/M$. In characteristic prime to $[N:N']$ it is finite étale.

If $v_\rho$ is primitive in $N$ and $v'_\rho=e_\rho v_\rho$ primitive in $N'$, the ramification order along the invariant divisor for $\rho$ is $e_\rho$.

Example: $N'=m\mathbb Z\subset\mathbb Z$ and the complete one-dimensional fan give $\mathbb P^1\to\mathbb P^1$, $z\mapsto z^m$, branched at $0,\infty$ with order $m$.
:::
