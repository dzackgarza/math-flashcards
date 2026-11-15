---
title: "Algebraic Geometry::Divisors"
---

::: {.front card-id="application-bertini-general-choice" tags="application"}
A research argument needs a divisor in a complex linear system satisfying several properties, each known to hold for a general member. Can the properties be imposed simultaneously? Does the same argument guarantee a member defined over a finite field?
:::

::: {.back card-id="application-bertini-general-choice"}
Each general-member property holds on a nonempty Zariski-open subset of the projective parameter space. Finitely many such opens have nonempty intersection because the parameter space is irreducible. Over $\mathbb C$ that intersection has a point. The conclusion applies to finitely many conditions; a countable collection instead involves a very-general choice. Over a finite field, a nonempty open need not have a rational point, so this argument alone does not produce a divisor over that field.
:::

::: {.front card-id="application-bertini-prescribed-points" tags="application"}
Let $X\subset\mathbb P^N_{\mathbb C}$ be smooth projective of dimension at least two, and let $Z$ be a finite set of distinct points of $X$. Can one choose a smooth irreducible divisor in $|\mathcal I_Z(d)|$ for sufficiently large $d$? What must be checked at the imposed points?
:::

::: {.back card-id="application-bertini-prescribed-points"}
For sufficiently large $d$, the system has base locus exactly $Z$ and permits arbitrary linear terms at each point of $Z$. Bertini gives smoothness off $Z$. At $p\in Z$, a local equation defines a smooth divisor exactly when its image in $\mathfrak m_p/\mathfrak m_p^2$ is nonzero. These are finitely many nonempty open conditions on sections, so a general section satisfies all of them. The resulting divisor is ample and connected; a smooth connected divisor is irreducible. Imposing vanishing to order two instead would force singularities at those points.
:::

::: {.front card-id="application-bertini-successive-sections" tags="application"}
Let $X\subset\mathbb P^N_{\mathbb C}$ be smooth integral projective of dimension $n$. Choose general hypersurfaces of fixed positive degrees $d_1,\ldots,d_r$. For $r<n$, what can be arranged for every successive intersection? What changes for $r=n$?
:::

::: {.back card-id="application-bertini-successive-sections"}
The restricted hypersurface systems are very ample. At each stage whose ambient dimension is at least two, Bertini gives a smooth irreducible divisor of codimension one. Thus one can arrange a smooth irreducible flag with final dimension $n-r$. At $r=n$, the last step cuts a smooth curve in a reduced finite set of points of cardinality $\deg(X)\prod_i d_i$. Smoothness remains, but irreducibility generally does not.
:::

::: {.front card-id="application-bertini-transverse-fixed-subvariety" tags="application"}
Let $X\subset\mathbb P^N_{\mathbb C}$ be smooth projective, and let $Z_1,\ldots,Z_s\subset X$ be smooth closed subvarieties of positive dimension. Can one choose a hyperplane section smooth on $X$ and transverse to all the $Z_i$? What condition gives transversality at an intersection point?
:::

::: {.back card-id="application-bertini-transverse-fixed-subvariety"}
Apply Bertini to the embedded $X$ and to each embedded $Z_i$, and intersect the finitely many open sets of acceptable hyperplanes. At $z\in Z_i\cap H$, smoothness of the restricted hyperplane equation means its differential is nonzero on $T_zZ_i$. Hence
$$T_zZ_i\not\subset T_z(X\cap H),$$
which is transversality inside $X$. Each $Z_i\cap H$ is smooth of dimension $\dim Z_i-1$.
:::

::: {.front card-id="application-bertini-frobenius-system" tags="application"}
Over an algebraically closed field of characteristic $p>0$, consider $V=\langle x_0^p,x_1^p,x_2^p\rangle\subset H^0(\mathbb P^2,\mathcal O(p))$. Is $V$ base-point-free? Is a general member smooth? Does this contradict Bertini for hyperplane sections of an embedding?
:::

::: {.back card-id="application-bertini-frobenius-system"}
The system is base-point-free. But every nonzero section is
$$a_0x_0^p+a_1x_1^p+a_2x_2^p=(b_0x_0+b_1x_1+b_2x_2)^p,$$
so its divisor is a nonreduced multiple of a line. The associated morphism is Frobenius, not an immersion. Smooth hyperplane sections of a smooth embedded variety remain a valid Bertini conclusion; arbitrary base-point-free systems in positive characteristic require additional hypotheses.
:::

::: {.front card-id="card-bcba6e654f0b5155" tags="definition"}
What is the **Picard group**?
:::

::: {.back card-id="card-bcba6e654f0b5155"}
The group of isomorphism classes of invertible sheaves (or line bundles) on $X$, with group operation $\otimes$.

Equivalently, $H^1(X; {\mathcal{O}}_X^{\times})$.
:::

::: {.front card-id="card-96215ab0361f9245"}
What is a **rational section** of a line bundle?
:::

::: {.back card-id="card-96215ab0361f9245"}
A pair $(s, U)$ with $U\subseteq X$ open containing all associated points of $X$, $s\in H^0(U; \mcl)$, and $(s_1, U_1) \sim (s_2, U_2) \iff$ $s_1=s_2$ on $U_{12}$.
:::

::: {.front card-id="card-4ee8f97372f5a928" tags="definition"}
How are Weil divisors related to Cartier divisors? When do they coincide?
:::

::: {.back card-id="card-4ee8f97372f5a928"}
A Weil divisor on a Noetherian integral scheme is a finite integral sum of codimension-one integral closed subschemes.

They coincide when $X$ is integral, separated, Noetherian, locally factorial (local rings are UFDs), and principal divisors coincide as well. In general one has a map $\operatorname{CDiv}(X) \to \operatorname{Div}(X)$ where $D$ defined by $\left\{{(U_i, f_i)}\right\}$ is mapped to $\sum_{Y\in \operatorname{Div}(X)} v_Y(f_i) Y$ where $i$ is any index where $U_i \cap Y$ is nonempty. The inverse construction: given $D\in \operatorname{Div}(X)$, it induces $D_x \in \operatorname{Spec}{\mathcal{O}}_{X, x}$, which is a UFD so $D_x$ is a principal divisor $D_x = (f_x)$ where $f_x \in K(X)$. Lift to a principal divisor $(f_x)$ on $X$; its restriction to $\operatorname{Spec}{\mathcal{O}}_{X, x}$ coincides with $D$ so they differ only by prime divisors that don't pass through $x$. Only finitely many such primes have nonzero coefficients in $D$ or $(f_x)$, so there is an open $U_x \ni x$ such that $D$ and $(f_x)$ restrict to the same divisor. Now cover $X$ by the $U_x$ and use the $f_x$ to define a Cartier divisor.
:::

::: {.front card-id="card-4693c6587767ae37" tags="definition"}
What is the Cartier divisor associated to a (rational) section of an invertible sheaf?
:::

::: {.back card-id="card-4693c6587767ae37"}
Rational section: $s: X\to \mcl$ defined on an open dense subset. A nonzero rational section $s$ of an invertible sheaf $\mcl$ defines a Cartier divisor: write $s=f_i e_i$ in each local frame $e_i$ and use the rational functions $f_i$ as local equations. With the convention $\mcl\cong\mathcal O_X(D)$, the canonical rational section of $\mathcal O_X(D)$ has divisor $D$.

As a Weil divisor: for any $Y\in \operatorname{Div}(X)$ define $(s) \coloneqq\sum_{Y\in \operatorname{Div}(X)} v_Y(s) Y$, where $v_Y(s) \coloneqq v_Y(\sigma(s))$ for a trivialization $\sigma: \mcl_{X, Y} { \, \xrightarrow{\sim}\, }{\mathcal{O}}_{X, Y}$ of the stalk at the generic point of $Y$. This is a valuation ring when $X$ is integral (and regular in codimension one). For $s\in H^0(\mcl)\setminus\left\{{0}\right\}$, $(s)$ is effective.
:::

::: {.front card-id="card-20c128cfdff9a4d9"}
For $D$ a divisor, what is ${\mathcal{O}}_X(D)$?
:::

::: {.back card-id="card-20c128cfdff9a4d9"}
${\mathcal{O}}_X(D)(U) \coloneqq\left\{{f\in K(X)^{\times}\st(f) + D \geq 0 \text{ on } U}\right\} \cup \left\{{0}\right\}$, a subsheaf of the constant sheaf $K(X)$. Global sections: $H^0({\mathcal{O}}_X(D)) = \left\{{f\in K(X)^{\times}\st(f) + D \geq 0}\right\} \cup \left\{{0}\right\}$.
:::

::: {.front card-id="card-971d2e611559217c"}
Show that every degree zero divisor on ${\mathbf{P}}^1$ is principal.
:::

::: {.back card-id="card-971d2e611559217c"}
Any $p_1, p_2$ are linearly equivalent by taking $f(z) = {z-a\over z-b}$.
:::

::: {.front card-id="card-15a0017a811c7b24"}
Show that not every degree zero divisor on an elliptic curve is principal. What is $\operatorname{Pic}(E)$?
:::

::: {.back card-id="card-15a0017a811c7b24"}
Take $p_1\neq p_2$, then if $p_1-p_2 = (f)$ for some $f: E\to {\mathbf{P}}^1$ this produces an injective holomorphic map and forces $E\cong {\mathbf{P}}^1$; however e.g. $g(E) = 1\neq 0 = g({\mathbf{P}}^1)$. In general $\operatorname{Pic}(E) \cong \operatorname{Pic}^0(E) \oplus \ZZ\cong E\oplus \ZZ$.
:::

::: {.front card-id="card-5f35d5826acfaa91"}
Show that if $D = V(f)$ is a hypersurface in ${\mathbf{P}}^n$ then $D\sim \deg(f) H$, so $\operatorname{Pic}({\mathbf{P}}^n) = \left\langle{H}\right\rangle_\ZZ$.
:::

::: {.back card-id="card-5f35d5826acfaa91"}
Let $d\coloneqq\deg f$ and $H = V(x_0)$, then $D - dH = (g)$ where $g(x_0,\cdots, x_n) = {f(x_0,\cdots, x_n) \over x_0^d}$.
:::

::: {.front card-id="card-fb3d8547bc4d2498"}
Give a definition of **very ample divisors** in terms of hyperplane sections.
:::

::: {.back card-id="card-fb3d8547bc4d2498"}
$D\in \operatorname{Div}(X)$ is very ample iff $D \sim D'$ where $D'$ is the divisor of a hyperplane section under an embedding $X\hookrightarrow{\mathbf{P}}^n$.
:::

::: {.front card-id="card-b593bed2e5b71670"}
What is a **prime** divisor?
:::

::: {.back card-id="card-b593bed2e5b71670"}
On an integral Noetherian scheme $X$, a prime divisor is an integral closed subscheme of codimension one.
:::

::: {.front card-id="card-4229cc42c6837e32"}
What is a **Weil** divisor?
:::

::: {.back card-id="card-4229cc42c6837e32"}
The free $\ZZ\dash$module on prime divisors, so $D = \sum_{i\in I} n_i Y_i$ where $I$ indexes prime divisors.
:::

::: {.front card-id="card-5f848017f4ff3d8a"}
What is an **effective** divisor?
:::

::: {.back card-id="card-5f848017f4ff3d8a"}
$n_i\geq 0$ for all $i$.
:::

::: {.front card-id="card-07970e097309b8ad"}
What is the **divisor of a rational function** $f\in K(X)$?
:::

::: {.back card-id="card-07970e097309b8ad"}
$(f) \coloneqq\sum_{i\in I} v_{Y_i}(f) Y_i$ where $v_Y$ is a valuation: for $Y$ prime, let $\eta$ be its generic point, then ${\mathcal{O}}_{Y, \eta}$ is a DVR $R$ with $\operatorname{ff}(R) = K(X)$ and discrete valuation $v_Y$. It's a theorem that $v_Y(f) = 0$ for almost all $Y$.
:::

::: {.front card-id="card-d0f2478c9024ff61"}
What is a **principal** divisor?
:::

::: {.back card-id="card-d0f2478c9024ff61"}
Any $D$ of the form $D = (f)$ for $f\in K(X)$.
:::

::: {.front card-id="card-9c3a89a72680196c"}
What is **linear equivalence** of divisors?
:::

::: {.back card-id="card-9c3a89a72680196c"}
$D \sim D'$ iff $D-D' = (f)$ for some $f\in K(X)^{\times}$.
:::

::: {.front card-id="card-5536323d59151c69"}
What is the **divisor class group** $\operatorname{Cl}(X)$?
:::

::: {.back card-id="card-5536323d59151c69"}
$\operatorname{Cl}(X) = \operatorname{coker}(K(X)^{\times}\xrightarrow{ ({-})} \operatorname{Div}(X))$, i.e. Weil divisors modulo linear equivalence.
:::

::: {.front card-id="card-fa7b1a663d3791dd"}
Discuss $\operatorname{Cl}(X)$.
:::

::: {.back card-id="card-fa7b1a663d3791dd"}
For $A$ a Noetherian domain, $A$ is a UFD iff $\operatorname{Spec}A$ is normal and $\operatorname{Cl}(\operatorname{Spec}A) = 0$.

This follows from the equivalence $A$ is a UFD iff every prime ideal of height 1 is principal.

$\operatorname{Cl}(\mathbb A^n_k)=0$ since $k[x_1,\ldots,x_n]$ is a UFD. For $n\ge1$, $\operatorname{Cl}(\mathbb P^n_k)=\mathbb Z[H]$, where a degree-$d$ hypersurface has class $dH$.

For $X$ normal integral Noetherian, $Z\subsetneq X$ closed, and $U=X\setminus Z$, restriction gives a surjection $\operatorname{Cl}(X)\to\operatorname{Cl}(U)$. It sends a prime divisor not contained in $Z$ to its intersection with $U$, and divisors supported in $Z$ to zero. The kernel is generated by the codimension-one components of $Z$. In particular, restriction is an isomorphism if $\operatorname{codim}_X Z\ge2$.
If $Z$ is irreducible of codimension one, this gives the right-exact sequence
$$\mathbb Z\xrightarrow{1\mapsto[Z]}\operatorname{Cl}(X)\longrightarrow\operatorname{Cl}(U)\longrightarrow0.$$
For projective space, the isomorphism $\operatorname{Cl}(\mathbb P^n_k)\cong\mathbb Z$ is induced by degree, sending $[H]$ to $1$.
:::

::: {.front card-id="card-c8a4fd5da4688a38"}
Is $\operatorname{Cl}(X)$ always free?
:::

::: {.back card-id="card-c8a4fd5da4688a38"}
No, it can contain torsion: let $Y\subseteq {\mathbf{P}}^2$ be an irreducible curve of degree $d$ and let $X\coloneqq{\mathbf{P}}^2\setminus Y$, then $\ZZ\xrightarrow{\times d}  \operatorname{Cl}({\mathbf{P}}^2)\cong \ZZ\twoheadrightarrow \operatorname{Cl}({\mathbf{P}}^2\setminus Y) \implies  \operatorname{Cl}(X) \cong C_d$
:::

::: {.front card-id="card-9437c471081d18e9"}
What are minimal conditions for which it makes sense to discuss Weil divisors?
:::

::: {.back card-id="card-9437c471081d18e9"}
Hartshorne's condition $(*)$: Noetherian, integral, separated, regular in codimension 1.
:::

::: {.front card-id="card-5a7dc879dfd7ff8c"}
Discuss **complete divisors** on a smooth complete curve.
:::

::: {.back card-id="card-5a7dc879dfd7ff8c"}
Every principal divisor has degree zero: use the general result that if $\Phi: X\to Y$ is a finite morphism of curves, $\deg(\Phi^* D) = \deg(\Phi) \deg D$ for any $D\in \operatorname{Div}(Y)$.

If $f\in k$ then $(f) = 0$, otherwise $f\not\in k$ so consider the extension $L \coloneqq k(f)$. The inclusion $L \hookrightarrow K(X)$ induces a finite morphism $\phi: X\to {\mathbf{P}}^1$ and $(f) = \phi^{-1}(D)$ where $D\coloneqq 1[0] - 1[\infty]$, and $\deg D = 0$ on ${\mathbf{P}}^1$.

Since $\phi$ is a finite morphism of curves, we have $\deg (f) = \deg(\phi^* D) = \deg(\phi)\cdot 0 = 0$.
:::

::: {.front card-id="card-823f5b1aae28c159"}
What is a **rational curve**?
:::

::: {.back card-id="card-823f5b1aae28c159"}
Birational to ${\mathbf{P}}^1$, equivalently admits distinct points $p, q$ with $p\sim q$.
:::

::: {.front card-id="card-c82773a251b250bd"}
Give an example of a curve that is not rational.
:::

::: {.back card-id="card-c82773a251b250bd"}
Take $y^2 = x^3-x$ and homogenize to $y^2z = x^3-xz^2$.
:::

::: {.front card-id="card-200a691d7831622a"}
What is a **reduced** divisor? An irreducible divisor?
:::

::: {.back card-id="card-200a691d7831622a"}
Reduced: $n_i = 1$ for all $i$. Irreducible: $n_i = 1$ for exactly one $i$.
:::

::: {.front card-id="card-3412fb386a2efba5"}
What is a **Cartier** divisor?
:::

::: {.back card-id="card-3412fb386a2efba5"}
A global section $s\in H^0(X; \mck^{\times}/{\mathcal{O}}^{\times})$, described by an open cover $U_i\rightrightarrows X$, $f_i \in H^0(U_i; \mck^{\times})$, and ${f_i\over f_j}\in H^0(U_{ij}; {\mathcal{O}}^{\times})$.

Equivalently, a locally principal Weil divisor.
:::

::: {.front card-id="card-765642427aa86626"}
What is a **principal** Cartier divisor?
:::

::: {.back card-id="card-765642427aa86626"}
Anything in the image of $H^0(\mck^{\times}) \to H^0(\mck^{\times}/{\mathcal{O}}^{\times})$.
:::

::: {.front card-id="card-b39fa8bac52d9231"}
Give an example of a Weil divisor that is not Cartier.
:::

::: {.back card-id="card-b39fa8bac52d9231"}
Take $X = V(xy-z^2) \subseteq {\mathbf{A}}^3$ and let $Y$ be its ruling $\left\{{ p\in Y\st y=z=0}\right\}$. Then $Y$ can not be locally principal in a neighborhood of the cone point. However, $2Y$ is locally principal and in fact principal. The divisor $D=V(x,z)$ is not of the form $V = (f)$ for any $f\in K(X)$ near the origin.
:::

::: {.front card-id="card-15ea337ffea63d93" tags="definition"}
What are **ample** and **very ample** invertible sheaves (divisors)?
:::

::: {.back card-id="card-15ea337ffea63d93"}
Very ample: $\mcl$ invertible is very ample relative to $f:X\to Y$ if $\exists \mce\in \QCoh(Y)$ and an immersion $\iota: X\to {\mathbf{P}}(\mce)$ such that $\mcl\cong \iota^* {\mathcal{O}}_{{\mathbf{P}}(\mce)}(1)$. Over $S$: an immersion $X\hookrightarrow\mathbb P_S^n$ with $\mcl\cong i^*\mathcal O(1)$. Over a field: $\mcl$ is bpf/gg and $\phi_{{\left\lvert {\mcl} \right\rvert}}: X\to {\mathbf{P}}^{h^0(\mcl) - 1}$ is a closed immersion.

Ample: equivalent conditions (for $X$ of finite type over a Noetherian ring):

- $\mcl^n$ is very ample for some $n > 0$, so defines an embedding $\phi_{{\left\lvert {\mcl^n} \right\rvert}}: X\to {\mathbf{P}}^N$ where ${\mathbf{P}}^N \cong {\mathbf{P}}H^0(X; \mcl^n) {}^{ \vee }$.
- (Serre) For any $\mcf\in \QCoh(X)^\mathrm{ft}$, the twist $\mcf(n) \coloneqq\mcf\otimes\mcl{ {}^{ \scriptstyle\otimes_{}^{n} }  }$ is globally generated for all $n> N_0 \gg 0$: tensoring high powers with a coherent sheaf gives many global sections.
- Every point has an affine neighborhood of the form $X_s=\{s\ne0\}$ for some global section $s$ of some positive power $\mcl^{\otimes n}$.
:::

::: {.front card-id="card-f8c8b2968ad6e404"}
What is a **simple normal crossings (SNC)** divisor?
:::

::: {.back card-id="card-f8c8b2968ad6e404"}
Normal crossings: A Weil divisor $D = \sum D_i$ is NC iff for every $x\in X$ a local equation for $D$ is $\prod_{i=1}^r x_i$ for independent local parameters $x_i\in {\mathcal{O}}_{X, x}$. SNC is if every $D_i$ is smooth and $r\leq n$.

Equivalently, $D$ is SNC if there exists a finite family of sections $\left\{{f_i}\right\} \subseteq H^0({\mathcal{O}}_X)$ such that $D = \sum (f_i)$ and for each $x\in \mathop{\mathrm{supp}}D$, the restrictions $(f_i)_x \in \mfm_x$ land in the maximal ideal and form part of a regular system of parameters for ${\mathcal{O}}_{X, x}$.\
:::

::: {.front card-id="card-836a20db1f7c129c"}
Give examples and non-examples of SNC divisors.
:::

::: {.back card-id="card-836a20db1f7c129c"}
A nodal curve is NC but not SNC (NC need not have smooth components).
:::

::: {.front card-id="card-44a22971b30133e2"}
What is the **divisor of zeros and poles** of $f \in k(X)^{\times}$?
:::

::: {.back card-id="card-44a22971b30133e2"}
Writing $Z_f, P_f$ for the sets of zeros and poles, $(f) = \sum n_i Z_i - \sum m_i P_i$ where $n_i$ is the multiplicity of the zero $Z_i$ (and similarly $m_i$ for $P_i$ the order of the pole).
:::

::: {.front card-id="card-fa6361e0b3eb64cd" tags="definition"}
What is the **invertible sheaf** associated to a Cartier divisor?
:::

::: {.back card-id="card-fa6361e0b3eb64cd"}
On an integral scheme, a Cartier divisor $D$ is given by local nonzero rational functions $\left\{{(U_i, f_i)}\right\}$ with $f_i/f_j\in\mathcal O_X^\times$ on overlaps. Then ${\mathcal{O}}_X(D) = \mcl(D) \leq \mck$ is the sub-${\mathcal{O}}_X$-module of the sheaf of rational functions generated by $\left\{{f_i^{-1}}\right\}$, i.e. locally $f_i^{-1}\mathcal O_X$. There is a bijection between Cartier divisors and invertible subsheaves of $\mck$.
:::

::: {.front card-id="card-4c5b6d6b7feab01a"}
What is the relationship between the Cartier class group and $\operatorname{Pic}(X)$?
:::

::: {.back card-id="card-4c5b6d6b7feab01a"}
In general, $\mathop{\mathrm{Cart}} \operatorname{Cl}(X) \hookrightarrow\operatorname{Pic}(X)$ by $D\mapsto \mcl(D)$; this is surjective when $X$ is integral.
:::

::: {.front card-id="card-bd0d8d0f314b34c2"}
What is the relationship between $\operatorname{Cl}(X)$ and $\operatorname{Pic}(X)$?
:::

::: {.back card-id="card-bd0d8d0f314b34c2"}
Isomorphic when $X$ is integral, separated, locally factorial.
:::

::: {.front card-id="card-f17b84b7f14023ed"}
What is an **effective** Cartier divisor?
:::

::: {.back card-id="card-f17b84b7f14023ed"}
Represented by $\left\{{(U_i, f_i)}\right\}$ where each $f_i\in H^0(U_i, {\mathcal{O}}_{U_i})$.
:::

::: {.front card-id="card-f974099d7333a060"}
What is the subscheme associated to a Cartier divisor?
:::

::: {.back card-id="card-f974099d7333a060"}
For $D$ effective, the subscheme $Y$ of codimension 1 defined by the sheaf of ideals $\mci_Y$ which is locally generated by the $f_i$. In fact $\mci_Y \cong \mcl(-D)$ in this case.
:::

::: {.front card-id="card-a6344b3c32690757"}
What does it mean for two divisors to be **numerically equivalent**?
:::

::: {.back card-id="card-a6344b3c32690757"}
$D\sim 0$ iff $D\cdot C = 0$ for every curve $C\subseteq X$, and $D_1\sim D_2 \iff D_1- D_2\sim 0$.
:::

::: {.front card-id="card-f2807a7963334d91" tags="definition"}
What is the **degree** of a divisor?
:::

::: {.back card-id="card-f2807a7963334d91"}
For a divisor $D=\sum_P n_P[P]$ on a proper curve over $k$, $\deg D=\sum_P n_P[\kappa(P):k] \in \ZZ$. Over an algebraically closed field, this is $\deg(D) = \sum_P n_P$.
:::

::: {.front card-id="card-e8e202eb43c56fe4"}
For $D$ a prime divisor and $Y\in \mathop{\mathrm{supp}}D$, what is the **multiplicity** of $Y$ in $D$?
:::

::: {.back card-id="card-e8e202eb43c56fe4"}
$D = \sum n_{Y_i} Y_i$ and $Y= Y_j$ for some $j$ since $Y\in \mathop{\mathrm{supp}}D$, so $\mult_D(Y) = n_Y$.
:::

::: {.front card-id="card-f8d3ad922064fbf7" tags="definition"}
What are the **multiplicity** and the **support** of a Cartier divisor?
:::

::: {.back card-id="card-f8d3ad922064fbf7"}
Coefficient along a prime divisor: for a Cartier divisor $D$ on a regular (or normal) integral scheme, its coefficient at a codimension-one point $\eta$ (prime divisor $Y$) is the valuation $v_Y(f_i) = \operatorname{ord}_\eta(f_i)$ of a local equation $f_i$ on any $U_i$ with $U_i \cap Y\neq \emptyset$.

Multiplicity at a point: for $D$ an effective Cartier divisor on $X$, let $f$ be a local equation at $p$ and define $\mu_p(D)$ to be the largest $N$ such that $f\in \mfm_p^N \subseteq {\mathcal{O}}_{X, p}$. Note $\mu_p \geq 1 \iff p\in \mathop{\mathrm{supp}}D$, and for $X$ smooth at $p$, $\mu_p = 1 \iff D$ is smooth at $p$.

Support: $\mathop{\mathrm{supp}}D = {\left\lvert {D} \right\rvert}$ is the union of poles and zeros of $D$, i.e. the set of points where a local equation is not a unit. On a regular integral scheme this is the union of the prime divisors $Y$ with $v_Y(f_i) \neq 0$.

Equivalently, define $D$ as a line bundle ${\mathcal{O}}_X(D)$ with a rational section $s_D$, set $U \subseteq X$ to be the maximal open set on which $s_D$ is defined and nonzero, and define ${\left\lvert {D} \right\rvert} \coloneqq X\setminus U$.
:::

::: {.front card-id="card-6ba72069d5f9a4b6"}
What is a **linear system**?
:::

::: {.back card-id="card-6ba72069d5f9a4b6"}
Any subspace of a complete linear system.
:::

::: {.front card-id="card-67f0df55debb4328"}
What is a **complete linear system**?
:::

::: {.back card-id="card-67f0df55debb4328"}
For a Cartier divisor $D$ on an integral projective variety, the complete linear system $|D|$ consists of all effective divisors linearly equivalent to $D$. With $L=\mathcal O_X(D)$, it is the projective space of nonzero sections of $L$ modulo scalar multiplication, $\mathbf P H^0(X,L)$.
:::

::: {.front card-id="card-a59770df8f80107c"}
What is the linear system associated to the canonical divisor $K_X$?
:::

::: {.back card-id="card-a59770df8f80107c"}
${\left\lvert {K_X} \right\rvert} = {\mathbf{P}}H^0(X; \omega_X)$.
:::

::: {.front card-id="card-ae8d56478c62b8d7"}
What does it mean for a linear system to be **base point free**?
:::

::: {.back card-id="card-ae8d56478c62b8d7"}
A point $p\in X$ is a base point of a linear system $S$ iff $p$ is contained in the support of every divisor $D\in S$. $S$ is bpf iff it contains no basepoints.

Equivalently, the corresponding line bundle $\mcl$ is generated by global sections, where $S$ corresponds to $V \subseteq H^0(X; \mcl)$ for some $\mcl\in \operatorname{Pic}(X)$, since $p$ is a base point iff $s_p\in \mfm_p \mcl_p$ for all $s\in V$.
:::

::: {.front card-id="card-7dfe2d5e36a21bf9"}
When is the morphism defined by a linear system a closed immersion?
:::

::: {.back card-id="card-7dfe2d5e36a21bf9"}
Separates points and separates tangents: $\forall p, q\in X$ there exists $D\in S$ with $p\in D$ and $q\not\in D$; given $p\in X, t\in {\mathbf{T}}_p X$, there is a $D\in S$ with $p\in D$ but $t\not \in {\mathbf{T}}_p(D) \coloneqq\qty{\mfm_{P, D}/\mfm_{P, D} } {}^{ \vee }$
:::

::: {.front card-id="card-a7508a5971d896ab"}
What is the base locus of a complete linear system $|L|$?
:::

::: {.back card-id="card-a7508a5971d896ab"}
The maximal closed subscheme of $X$ contained in every $D\in {\left\lvert {L} \right\rvert}$.

Equivalently
$$\mathrm{Bs}{\left\lvert {L} \right\rvert} = \bigcap_{s\in H^0(L)} Z(s)$$
:::

::: {.front card-id="card-d83459b52d448c66"}
What is a **hyperplane section**?
:::

::: {.back card-id="card-d83459b52d448c66"}
For $X \subseteq {\mathbf{P}}^n$ projective, the intersection $X \cap H$ for some hyperplane $X = V(f)$.
:::

::: {.front card-id="card-2a3c393c9009915d"}
What is a **polarization**? What is a principal polarization?
:::

::: {.back card-id="card-2a3c393c9009915d"}
A choice of $\mcl\in \NS(X)^\mathrm{amp}$, where $\NS(X) \coloneqq\operatorname{Pic}(X)/\operatorname{Pic}^0(X)$. Principal if $\deg \mcl= 1$.
:::

::: {.front card-id="card-317a749884b346c7"}
What is the **ramification divisor** of a finite morphism $f:X\to Y$ of smooth projective curves?
:::

::: {.back card-id="card-317a749884b346c7"}
$R \coloneqq\sum_{p\in X} \mathop{\mathrm{length}}(\Omega_{X/Y})_p \cdot p$.
:::

::: {.front card-id="card-a565549a3fed53d5"}
Prove the ramification formula for canonical divisors.
:::

::: {.back card-id="card-a565549a3fed53d5"}
For $f: X\to Y$ take the cotangent exact sequence
$$f^* \Omega_{Y/k} \hookrightarrow\Omega_{X/k} \twoheadrightarrow\Omega_{X/Y}$$
tensor by $\Omega_{X/k} {}^{ \vee }$ to get
$$f^* \Omega_{Y/k}\otimes\Omega_{X/k} {}^{ \vee }\hookrightarrow{\mathcal{O}}_X \twoheadrightarrow\Omega_{X/Y} \otimes\Omega_{X/k} {}^{ \vee }$$
Use that $\Omega_{X/Y}$ has finite support, so $\Omega_{X/Y} \cong \Omega_{X/Y} \otimes\Omega_{X/k} {}^{ \vee }$ and
$$f^* \Omega_{Y/k}\otimes\Omega_{X/k} {}^{ \vee }\hookrightarrow{\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_R$$
but $\ker({\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_R) \cong \mcl(-R)$, so
$$f^* \Omega_{Y/k} \otimes\Omega_{X/k} {}^{ \vee }\cong \mcl(-R)$$
and taking associated divisors yields $f^*K_Y, -K_X, -R$ respectively, so $f^* K_Y - K_X \sim -R \implies K_X \sim f^* K_Y + R$.
:::

::: {.front card-id="card-6b377b686ddf940e"}
Can ${\mathbf{P}}^1$ admit an unramified cover by a curve?
:::

::: {.back card-id="card-6b377b686ddf940e"}
No: if $f: X\to {\mathbf{P}}^1$ is a finite etale cover of degree $n \geq 1$ then $\deg R = 0$, so by Riemann-Hurwitz $\chi(X) = n\chi({\mathbf{P}}^1) \implies 2g_X - 2 = n(-2) \leq -2 \implies g_X \leq 0$, so this forces $g_X = 0$ and $n=1$, so $f$ must be an isomorphism.
:::

::: {.front card-id="card-bdcb54fbf9a23367"}
What is a **branch point**? A **ramification point**?
:::

::: {.back card-id="card-bdcb54fbf9a23367"}
$e_p = 1\implies$ unramified, $e_p > 1 \implies p$ is ramified and $q\coloneqq f(p)$ is a branch point.
:::

::: {.front card-id="card-56d81b8301f8afa2"}
What is the **branch locus**?
:::

::: {.back card-id="card-56d81b8301f8afa2"}
For $f:X\to Y$, the set of critical values in $Y$. Compare to the ramification locus in $X$, which is its preimage.
:::

::: {.front card-id="card-8fa02aa33202f47b"}
What is the result of taking determinants in an exact sequence?
:::

::: {.back card-id="card-8fa02aa33202f47b"}
$A\to B \to C$ a SES in ${}_{{\mathcal{O}}_X}\Mod$ yields $\operatorname{det}(A) \otimes_{{\mathcal{O}}_X} \operatorname{det}(C) \cong \operatorname{det}(B)$.
:::

::: {.front card-id="card-8d85a1b7ab49e41b"}
What is a **canonical divisor**?
:::

::: {.back card-id="card-8d85a1b7ab49e41b"}
A divisor $K_X$ defined by any meromorphic section of $\omega_{X/k}$.
:::

::: {.front card-id="card-6f854b0e887f821f" tags="definition"}
What is: The Picard group and class group
:::

::: {.back card-id="card-6f854b0e887f821f"}
$\operatorname{Pic}(X)$ is the group of invertible sheaves up to isomorphism under tensor product. For a normal integral Noetherian scheme, $\operatorname{Cl}(X)$ is the group of Weil divisors modulo principal divisors. Cartier divisors modulo principal divisors give $\operatorname{Pic}(X)$; on a locally factorial scheme, $\operatorname{Pic}(X)\cong\operatorname{Cl}(X)$.
:::

::: {.front card-id="card-80fa03cc214825fe"}
When is ${\mathcal{O}}_{{\mathbf{P}}^n}(d)$ ample? Very ample?
:::

::: {.back card-id="card-80fa03cc214825fe"}
BPF iff $d\geq 0$

Very ample iff ample iff $d\geq 1$.
:::

::: {.front card-id="card-c024cb955d1ceca5"}
What is a polarized scheme?
:::

::: {.back card-id="card-c024cb955d1ceca5"}
$(X, \mcl)$ a scheme with an ample line bundle.
:::

::: {.front card-id="card-12cc1c6c9aa5697e"}
What does it mean for $\mcl\in \operatorname{Pic}(X)$ to be **ample**?
:::

::: {.back card-id="card-12cc1c6c9aa5697e"}
For all $\mcf\in \Coh(X)$, the twist $\mcf\otimes\mcl^n$ is globally generated for $n\gg 0$.
:::

::: {.front card-id="card-600a9b022ee0b85d"}
Discuss ampleness of sheaves of affine schemes.
:::

::: {.back card-id="card-600a9b022ee0b85d"}
Every $X\in \Coh(\operatorname{Spec}A)$ is globally generated, so if $\mcf$ is invertible then it is necessarily ample.
:::

::: {.front card-id="card-979041d2022161e4"}
Discuss ampleness of ${\mathcal{O}}_{{\mathbf{P}}^m}(n)$.
:::

::: {.back card-id="card-979041d2022161e4"}
${\mathcal{O}}(1)$ is very ample: write ${\mathbf{P}}^n = \mathop{\mathrm{Proj}}k[x_0, \cdots, x_{n}]$, then $x_0,\cdots, x_n$ induce $n+1$ global sections . For $n\geq 1$, ${\mathcal{O}}(n)$ corresponds to the Veronese embedding into ${\mathbf{P}}^N$, and so is very ample.
:::

::: {.front card-id="card-a4380c8c6119e01f"}
What is a **base point** of a linear system?
:::

::: {.back card-id="card-a4380c8c6119e01f"}
For $p\in X$ and a linear system ${\left\lvert {D_0} \right\rvert}$, $p$ is a base point iff $p\in \mathop{\mathrm{supp}}D$ for all $D\in {\left\lvert {D_0} \right\rvert}$, where $\mathop{\mathrm{supp}}D$ is the union of all prime divisors in $D$.
:::

::: {.front card-id="card-fed03351b6881aaa"}
What is the ample divisor associated to an embedding?
:::

::: {.back card-id="card-fed03351b6881aaa"}
If $\phi: S\hookrightarrow{\mathbf{P}}^n$, take the hyperplane section $L = \phi(S) \cap H$ for $H$ any hyperplane.
:::

::: {.front card-id="card-e8ee05a2704a0cc0"}
Describe $\NS(X)$ and $\operatorname{Pic}(X)$ in terms of divisors.
:::

::: {.back card-id="card-e8ee05a2704a0cc0"}
$\NS(X) = \operatorname{CDiv}(X)/\sim$ modulo algebraic equivalence.

$\operatorname{Pic}(X) = \operatorname{CDiv}(X)/\sim$ modulo linear equivalence.

$\CH_k(X) = Z_k(X)/\sim$ modulo rational equivalence
:::

::: {.front card-id="card-8ea4c5bc81520a4a"}
What is the Picard number $\rho(X)$?
:::

::: {.back card-id="card-8ea4c5bc81520a4a"}
$\rho(X) \coloneqq\operatorname{rank}_\ZZ\NS(X)$, where $\NS(X) \coloneqq\operatorname{coker}(\operatorname{Pic}^0(X) \hookrightarrow\operatorname{Pic}(X))$; also written $p(X)$.

For $X$ compact complex,
$$\rho(X) = \operatorname{rank}_\ZZ\operatorname{im}(c_1: \operatorname{Pic}(X) \to H^2(X; \ZZ))$$
If $X$ is Kahler, Lefschetz $(1,1)$ gives $\rho(X) = \operatorname{rank}_\ZZ(H^{1,1}(X) \cap H^2(X; \ZZ))$, so $\rho(X)\leq h^{1,1}(X)$.

For a K3, $\rho(X) = \operatorname{rank}_\ZZ\operatorname{Pic}(X) = \operatorname{rank}_\ZZ\NS(X)$. Since $\NS(X) \leq H^{1, 1}(X)$, there is a bound $\rho(X) \leq 20$ over $\CC$.
:::

::: {.front card-id="card-aa5478294141e3a4"}
Define the Neron-Severi group.
:::

::: {.back card-id="card-aa5478294141e3a4"}
$S_X \coloneqq\NS(X) \coloneqq\operatorname{Pic}(X) / \operatorname{Pic}^0(X) = \operatorname{coker}(\operatorname{Pic}^0(X) \hookrightarrow\operatorname{Pic}(X))$: line bundles modulo those algebraically equivalent to zero.

For $X$ compact Kahler, $c_1$ identifies $\NS(X)$ with $\operatorname{im}c_1 \subseteq H^2(X; \ZZ)$, and by Lefschetz $(1,1)$ this image is the set of integral classes of type $(1,1)$. For a K3, $H^2(X;\ZZ)$ is torsionfree, so
$$\NS(X) = H^{1, 1}(X) \cap H^{2}(X; \ZZ)\subseteq H^2(X; \CC)$$
:::

::: {.front card-id="card-4f556cf6edfaace8"}
What does it mean for a line bundle $L$ to be numerically trivial?
:::

::: {.back card-id="card-4f556cf6edfaace8"}
$L. \mcl= 0$ for all $\mcl\in \operatorname{Pic}(X)$, e.g. any $L\in \operatorname{Pic}^0(X)$.
:::

::: {.front card-id="card-95620d7653e21270"}
What is $\mathrm{Num}(X)$?
:::

::: {.back card-id="card-95620d7653e21270"}
$\operatorname{Pic}(X)/\operatorname{Pic}(X)^\tau$. quotienting by the subgroup of numerically trivial line bundles.

A ${}_{\ZZ}\Mod$ with a nondegenerate symmetric integral pairing.
:::

::: {.front card-id="card-97124755dd1c9baa"}
Give an equivalent characterization of when a line bundle is trivial.
:::

::: {.back card-id="card-97124755dd1c9baa"}
Both $H^0(L)$ and $H^0(L {}^{ \vee })$ are nontrivial.
:::

::: {.front card-id="card-bee54f0820921fff"}
When does $L$ induce a rational map?
:::

::: {.back card-id="card-bee54f0820921fff"}
If $h^0(L) > 1$, inducing $\phi_L: X\dashrightarrow{\mathbf{P}}H^0(L) {}^{ \vee }$ regular on $X\setminus\mathrm{Bs}{\left\lvert {L} \right\rvert}$.
:::

::: {.front card-id="card-8516e525f30da86c"}
What is the fixed-mobile decomposition $L = M + F$ for $L\in \operatorname{Pic}(X)$?
:::

::: {.back card-id="card-8516e525f30da86c"}
$F$ is the 1-dimensional part of $\mathrm{Bs}{\left\lvert {L} \right\rvert}$.

$M\coloneqq L(-F)$ is the mobile part, is nef, satisfies $M^2 \geq 0$. Has a finite set of base points, contains the zero-dimensional locus of $\mathrm{Bs}{\left\lvert {L} \right\rvert}$.
:::

::: {.front card-id="card-3cc4412c0c60050d"}
Discuss ampleness of line bundles on abelian varieties.
:::

::: {.back card-id="card-3cc4412c0c60050d"}
If $L\in \operatorname{Pic}(A)$ is ample in any characteristic, $L^k$ is very ample for $k\geq 3$ independent of $\dim A$.
:::

::: {.front card-id="card-44659fa94f8ffffe"}
What is Fujita's conjecture?
:::

::: {.back card-id="card-44659fa94f8ffffe"}
For $L\in \operatorname{Pic}(X)^\amp$ for $X$ smooth projective over $\CC$, $L^k\otimes\omega_X$ is

Globally generated for $k\geq \dim(X) + 1$ and

Very ample for $k\geq \dim(X) + 2$.

True for surfaces, a stronger version is true for K3s.
:::












::: {.front card-id="theorem-bertini-smoothness" tags="theorem"}
Let $X$ be a smooth complex variety and $V\subset H^0(X,L)$ a finite-dimensional linear system. State Bertini smoothness for a base-point-free system and for a system with base locus $B$.
:::

::: {.back card-id="theorem-bertini-smoothness"}
If the system is base-point-free, a general member is smooth or empty. In general, a general member is smooth outside $B$.
:::

::: {.front card-id="theorem-nakai-moishezon" tags="theorem"}
State the Nakai–Moishezon criterion for a Cartier divisor $D$ on a complex projective variety $X$.
:::

::: {.back card-id="theorem-nakai-moishezon"}
The divisor $D$ is ample if and only if
$$D^{\dim V}\cdot V>0$$
for every positive-dimensional integral subvariety $V\subset X$.
:::

::: {.front card-id="theorem-kleiman-ampleness" tags="theorem"}
State Kleiman's ampleness criterion for $D\in N^1(X)_{\mathbb R}$ on a complex projective variety. How are the ample and nef cones related?
:::

::: {.back card-id="theorem-kleiman-ampleness"}
The class $D$ is ample if and only if
$$D\cdot\gamma>0\qquad(0\ne\gamma\in\overline{\operatorname{NE}}(X)).$$
Moreover,
$$\operatorname{Amp}(X)=\operatorname{Int}\operatorname{Nef}(X).$$
:::

::: {.front card-id="theorem-seshadri-ampleness" tags="theorem"}
State Seshadri's ampleness criterion for a line bundle $L$ on a complex projective variety. For $X$ smooth and $L$ nef, express the local Seshadri constant using the blowup at $x$.
:::

::: {.back card-id="theorem-seshadri-ampleness"}
The line bundle is ample if and only if there is $\varepsilon>0$ such that
$$L\cdot C\ge\varepsilon\,\operatorname{mult}_xC$$
for every integral curve $C\subset X$ and every $x\in C$. For $\pi:\operatorname{Bl}_xX\to X$ with exceptional divisor $E$,
$$\varepsilon(L;x)=\sup\{t\ge0:\pi^*L-tE\text{ is nef}\}.$$
:::

::: {.front card-id="theorem-grothendieck-lefschetz-picard" tags="theorem"}
For a smooth ample divisor $H$ in a smooth complex projective variety $X$, state the Grothendieck–Lefschetz theorem for restriction of Picard groups in dimensions at least three.
:::

::: {.back card-id="theorem-grothendieck-lefschetz-picard"}
The map
$$\operatorname{Pic}(X)\longrightarrow\operatorname{Pic}(H)$$
is an isomorphism if $\dim X\ge4$, and is injective if $\dim X=3$.
:::

::: {.front card-id="theorem-noether-lefschetz" tags="theorem"}
What does the Noether–Lefschetz theorem say about the Picard group of a very general smooth degree-$d$ surface in $\mathbb P^3_{\mathbb C}$, for $d\ge4$?
:::

::: {.back card-id="theorem-noether-lefschetz"}
For such a surface $S$,
$$\operatorname{Pic}(S)=\mathbb Z[\mathcal O_S(1)].$$
:::

::: {.front card-id="theorem-khovanskii-teissier" tags="theorem"}
Let $A,B$ be nef classes on a smooth complex projective $n$-fold. State log-concavity of their mixed intersections, the resulting end inequality, and the equality criterion when $A,B$ are ample.
:::

::: {.back card-id="theorem-khovanskii-teissier"}
For $a_i=A^{n-i}B^i$,
$$a_i^2\ge a_{i-1}a_{i+1}\quad(1\le i\le n-1),\qquad (A^{n-1}B)^n\ge(A^n)^{n-1}B^n.$$
For ample $A,B$ and $n\ge2$, equality in a nondegenerate Teissier inequality holds exactly when $A$ and $B$ are numerically proportional.
:::

::: {.front card-id="theorem-thom-porteous" tags="theorem"}
Let $E\to F$ be a map of vector bundles of ranks $e,f$ on a smooth complex variety $X$, and $0\le r<\min(e,f)$. State the expected codimension of $D_r$ and its Thom–Porteous class when that codimension holds.
:::

::: {.back card-id="theorem-thom-porteous"}
The expected codimension is $(e-r)(f-r)$. If it holds, then
$$[D_r]=\det\left(c_{f-r+i-j}(F-E)\right)_{1\le i,j\le e-r}\cap[X],$$
with $c(F-E)=c(F)c(E)^{-1}$, $c_0=1$, and $c_j=0$ for $j<0$.
:::

::: {.front card-id="application-ample-product-positive" tags="application"}
On $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, prove that $D=(2,3)$ is ample using intersections with all curves. Which criterion applies?
:::

::: {.back card-id="application-ample-product-positive"}
Every integral curve has class $(a,b)$ with $a,b\ge0$ and $(a,b)\ne(0,0)$. Thus $D\cdot C=2b+3a>0$, and $D^2=12>0$. The surface Nakai–Moishezon criterion gives ampleness.
:::

::: {.front card-id="application-nef-product-fiber" tags="application"}
On $\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, determine whether $D=(1,0)$ is nef, ample, big, and globally generated. Explain how a fiber separates these properties.
:::

::: {.back card-id="application-nef-product-fiber"}
The bundle is pulled back from $\mathcal O_{\mathbb P^1}(1)$, so it is globally generated and nef. For $F=\{p\}\times\mathbb P^1$, one has $D\cdot F=0$, so it is not ample. Since $D^2=0$ and $D$ is nef, its volume is zero and it is not big.
:::

::: {.front card-id="application-bertini-pencil-disconnected" tags="application"}
On $X=\mathbb P^1_{\mathbb C}\times\mathbb P^1_{\mathbb C}$, consider $|\mathcal O_X(2,0)|$. Is a general member smooth? Is it irreducible? Explain which two Bertini hypotheses lead to different answers.
:::

::: {.back card-id="application-bertini-pencil-disconnected"}
The system is base-point-free on a smooth variety, so a general member is smooth. A general section on the first factor has two distinct zeros, so its divisor on $X$ is the disjoint union of two fibers. It is not irreducible. The associated morphism has one-dimensional image, so the image-dimension hypothesis of Bertini irreducibility fails.
:::

::: {.front card-id="application-bertini-base-point-singularity" tags="application"}
Fix $p\in\mathbb P^2_{\mathbb C}$ and let $V$ be the system of conics vanishing to order at least two at $p$. Where can Bertini guarantee smoothness of a general member? Is the general member smooth at $p$?
:::

::: {.back card-id="application-bertini-base-point-singularity"}
Bertini gives smoothness away from the base locus $\{p\}$. At $p$, every local equation belongs to $\mathfrak m_p^2$, so both first derivatives vanish and every member is singular there. A general such conic is two distinct lines through $p$, smooth away from their intersection.
:::

::: {.front card-id="application-seshadri-plane" tags="application"}
For $L=\mathcal O_{\mathbb P^2_{\mathbb C}}(d)$ with $d>0$, compute $\varepsilon(L;p)$ at a point $p$. Show both bounds rather than merely invoking ampleness.
:::

::: {.back card-id="application-seshadri-plane"}
For any integral curve $C$ through $p$, $\operatorname{mult}_p C\le\deg C$, so $L\cdot C/\operatorname{mult}_p C\ge d$. A line through $p$ has degree and multiplicity both one, giving the reverse bound. Hence $\varepsilon(L;p)=d$.
:::

::: {.front card-id="application-porteous-points-plane" tags="application"}
A general morphism $\mathcal O_{\mathbb P^2}^{\oplus2}\to\mathcal O_{\mathbb P^2}(1)^{\oplus3}$ has a rank-at-most-one locus of the expected dimension. Compute its length. Choose a formula and verify the codimension before using it.
:::

::: {.back card-id="application-porteous-points-plane"}
The expected codimension is $(2-1)(3-1)=2$, so the locus is zero-dimensional. Thom–Porteous gives its class as
$$c_2\bigl(\mathcal O(1)^{\oplus3}-\mathcal O^{\oplus2}\bigr)=[(1+H)^3]_2=3H^2.$$
Since $\int_{\mathbb P^2}H^2=1$, the scheme has length three.
:::

::: {.front card-id="theorem-connected-ample-divisor" tags="theorem"}
State the connectedness theorem for an effective ample Cartier divisor $D$ on a connected normal projective variety $X$ over an algebraically closed field. Include the dimension hypothesis.
:::

::: {.back card-id="theorem-connected-ample-divisor"}
If $\dim X\ge2$, then $D$ is connected.
:::

::: {.front card-id="application-ample-connected-not-irreducible" tags="application"}
On $\mathbb P^2_{\mathbb C}$, let $D$ be the union of two distinct lines. Which of connectedness, irreducibility, and smoothness follows from $D$ being an effective ample Cartier divisor? How does this compare with a general member of $|\mathcal O(2)|$?
:::

::: {.back card-id="application-ample-connected-not-irreducible"}
Connectedness follows from the ample-divisor theorem. This $D$ is reducible and singular at the intersection of the lines. A general plane conic is smooth by Bertini and connected by ampleness, hence irreducible. The general-member hypothesis distinguishes Bertini from connectedness of every effective ample divisor.
:::

::: {.front card-id="theorem-kleiman-transversality" tags="theorem"}
Let a connected smooth algebraic group $G$ act transitively on a smooth variety $X$ over an algebraically closed field. State Kleiman's theorem for subvarieties $Y,Z\subseteq X$. What strengthens in characteristic zero when $Y$ and $Z$ are smooth?
:::

::: {.back card-id="theorem-kleiman-transversality"}
For $g$ in a dense open subset of $G$, the intersection $gY\cap Z$ is empty or pure of dimension $\dim Y+\dim Z-\dim X$. If this number is negative, the general intersection is empty. In characteristic zero, smooth $Y$ and $Z$ meet transversely for general $g$.
:::

::: {.front card-id="card-f76ef7641c052805" tags="definition"}
What is the definition of Algebraic cycle?
:::

::: {.back card-id="card-f76ef7641c052805"}
A $k$-cycle on $X$ is a finite formal sum $Z=\sum_i n_i[Y_i]$ with $n_i\in\mathbb Z$ and $Y_i\subset X$ a $k$-dimensional integral closed subscheme. The group of $k$-cycles is denoted $Z_k(X)$.
:::

::: {.front card-id="card-f97dfbd590c2c919" tags="definition"}
What is the definition of Algebraic equivalence?
:::

::: {.back card-id="card-f97dfbd590c2c919"}
Divisors $D_0,D_1$ on $X$ are algebraically equivalent if there exist a connected variety $T$, a divisor $\mathcal D\subset X\times T$, and points $t_0,t_1\in T$ with $\mathcal D|_{X\times\{t_i\}}=D_i$. Algebraic equivalence lies between rational and numerical equivalence.
:::

::: {.front card-id="card-4d010758d2a10d0a" tags="definition"}
What is the definition of Ample line bundle?
:::

::: {.back card-id="card-4d010758d2a10d0a"}
A line bundle $L$ on a proper scheme $X$ such that for every coherent sheaf $\mathcal F$, the twist $\mathcal F\otimes L^{\otimes m}$ is globally generated for all $m\gg0$ (Serre's criterion). Equivalently, some positive tensor power $L^{\otimes m}$ is very ample.
:::

::: {.front card-id="card-57cf0333ff7b50ba" tags="definition"}
What is the definition of Ampleness?
:::

::: {.back card-id="card-57cf0333ff7b50ba"}
The property of a line bundle or Cartier divisor $L$ on a proper scheme of satisfying Serre's criterion: $\mathcal F\otimes L^{\otimes m}$ is globally generated for every coherent $\mathcal F$ and all $m\gg0$. Equivalently, $L^{\otimes m}$ is very ample for some $m>0$.
:::

::: {.front card-id="card-696f6dce4f6a24e9" tags="definition"}
What is the definition of Chow group?
:::

::: {.back card-id="card-696f6dce4f6a24e9"}
$\operatorname{CH}_k(X)=Z_k(X)/{\sim_{\mathrm{rat}}}$, the free abelian group on $k$-dimensional integral closed subschemes modulo rational equivalence. For smooth $X$, intersection product makes $\operatorname{CH}^*(X)=\bigoplus_k\operatorname{CH}^k(X)$ a graded ring.
:::

::: {.front card-id="card-ebf397cbf5b93cb3" tags="definition"}
What is the definition of Cone of curves?
:::

::: {.back card-id="card-ebf397cbf5b93cb3"}
$\overline{\operatorname{NE}}(X)$ is the closed convex cone in $N_1(X)_{\mathbb R}$ generated by classes of integral curves on a projective variety $X$. Its dual cone is the nef cone $\operatorname{Nef}(X)\subset N^1(X)_{\mathbb R}$.
:::

::: {.front card-id="card-d5369545a0396ce2" tags="definition"}
What is the definition of Discrete valuation ring?
:::

::: {.back card-id="card-d5369545a0396ce2"}
A Noetherian local domain $(R,\mathfrak m)$ whose maximal ideal $\mathfrak m$ is nonzero and principal; equivalently a principal ideal domain with exactly one nonzero prime ideal. Its fraction field carries a discrete valuation $v$ with $R=\{x:v(x)\ge 0\}$.
:::

::: {.front card-id="card-289720bdec6846ed" tags="definition"}
What is the definition of Divisor?
:::

::: {.back card-id="card-289720bdec6846ed"}
A Weil divisor is a finite formal sum $\sum n_i D_i$ of prime divisors with $n_i\in\mathbb Z$. A Cartier divisor is a global section of $\mathcal K_X^\times/\mathcal O_X^\times$, represented by rational functions on an open cover; on a locally factorial scheme the two notions agree.
:::

::: {.front card-id="card-e5948fc8d434e3f9" tags="definition"}
What is the definition of Effective divisor?
:::

::: {.back card-id="card-e5948fc8d434e3f9"}
A Weil divisor $D=\sum_i n_i[Y_i]$ is effective if every coefficient $n_i\ge 0$. An effective Cartier divisor on a scheme $X$ is a closed subscheme locally defined by a nonzerodivisor; equivalently, it is a Cartier divisor represented by a section of $\mathcal K_X^\times/\mathcal O_X^\times$ that lifts to a regular section of some invertible sheaf.
:::

::: {.front card-id="card-54e70e3f7b7c02ea" tags="definition"}
What is the definition of Fixed part?
:::

::: {.back card-id="card-54e70e3f7b7c02ea"}
In the fixed-mobile decomposition $L=M+F$ on a surface, the fixed part $F$ is the effective divisor equal to the one-dimensional part of $\operatorname{Bs}|L|$; every member of $|L|$ contains $F$.
:::

::: {.front card-id="card-b6efa81777a96edf" tags="definition"}
What is the definition of Integral closed subscheme?
:::

::: {.back card-id="card-b6efa81777a96edf"}
A closed subscheme $Y\subset X$ that is reduced and irreducible as a scheme, equivalently an integral scheme with the reduced induced structure. A prime divisor is an integral closed subscheme of codimension one.
:::

::: {.front card-id="card-13ec36d1e75c44cc" tags="definition"}
What is the definition of Invertible subsheaf?
:::

::: {.back card-id="card-13ec36d1e75c44cc"}
A subsheaf $\mathcal L\subseteq\mathcal K_X$ of the sheaf of rational functions that is locally free of rank one; locally $\mathcal L|_U=f^{-1}\mathcal O_U$ for some $f\in K(X)^\times$. Invertible subsheaves of $\mathcal K_X$ correspond bijectively to Cartier divisors.
:::

::: {.front card-id="card-2da8a915ff90da87" tags="definition"}
What is the definition of Linear equivalence?
:::

::: {.back card-id="card-2da8a915ff90da87"}
Two divisors $D,D'$ on a scheme $X$ are linearly equivalent, written $D\sim D'$, if $D-D'=\operatorname{div}(f)$ for some nonzero rational function $f\in K(X)^\times$; equivalently $\mathcal O_X(D)\cong\mathcal O_X(D')$. For Weil divisors these classes form the divisor class group $\operatorname{Cl}(X)$; for Cartier divisors they form $\operatorname{Pic}(X)$.
:::

::: {.front card-id="card-29de05ab26c80359" tags="definition"}
What is the definition of Local equation?
:::

::: {.back card-id="card-29de05ab26c80359"}
For a Cartier divisor $D$ at $x\in X$, a rational function $f$ on a neighborhood $U$ of $x$ such that $D|_U=\operatorname{div}(f)$; for effective $D$ it generates the ideal sheaf $\mathcal O_X(-D)$ near $x$. It is unique up to a unit in $\mathcal O_{X,x}^\times$.
:::

::: {.front card-id="card-5ed1016302f16005" tags="definition"}
What is the definition of Local parameter?
:::

::: {.back card-id="card-5ed1016302f16005"}
At a smooth point $x$ of an $n$-dimensional variety, a local parameter is an element $t\in\mathfrak m_x$ whose image generates $\mathfrak m_x/\mathfrak m_x^2$. An $n$-tuple of local parameters is a regular system of parameters.
:::

::: {.front card-id="card-a97a66e7c7fd460e" tags="definition"}
What is the definition of Locally principal?
:::

::: {.back card-id="card-a97a66e7c7fd460e"}
A Cartier divisor (or ideal sheaf) is locally principal if every point has an open neighborhood $U$ on which it is defined by one nonzerodivisor $f\in\mathcal O_X(U)$. Cartier divisors are exactly the locally principal Weil divisors.
:::

::: {.front card-id="card-f73ab1eaa29f6bf6" tags="definition"}
What is the definition of Maximal minors?
:::

::: {.back card-id="card-f73ab1eaa29f6bf6"}
For a matrix of $\varphi:E\to F$, the maximal minors of size $r$ are the determinants of its $r\times r$ submatrices. Their ideal cuts out $\{x:\operatorname{rank}\varphi_x\le r-1\}$; when the expected codimension holds, its class is $c_{f-r+1}(F-E)\cap[X]$.
:::

::: {.front card-id="card-568c54ff627ce381" tags="definition"}
What is the definition of Meromorphic section?
:::

::: {.back card-id="card-568c54ff627ce381"}
A section of a line bundle $L$ over a dense open subset of $X$, locally $s=f\,e$ with $f$ meromorphic and $e$ a local frame; equivalently a rational section of $L$. Its zeros and poles define a Cartier divisor.
:::

::: {.front card-id="card-11b5750ad90e4b9c" tags="definition"}
What is the definition of Mobile part?
:::

::: {.back card-id="card-11b5750ad90e4b9c"}
In the fixed-mobile decomposition $L=M+F$, the mobile part is $M=L(-F)$. It is nef, satisfies $M^2\ge 0$, and has at most a zero-dimensional base locus.
:::

::: {.front card-id="card-a8f303b6686b9598" tags="definition"}
What is the definition of Normal crossing divisor?
:::

::: {.back card-id="card-a8f303b6686b9598"}
An effective divisor on a smooth variety such that at each point it is defined by $x_1\cdots x_k=0$ for part of a regular system of parameters, so its branches meet transversely. When every irreducible component is smooth it is a simple normal crossings divisor.
:::

::: {.front card-id="card-3419eda9697a9bff" tags="definition"}
What is the definition of Order of vanishing?
:::

::: {.back card-id="card-3419eda9697a9bff"}
For a prime divisor $Y$ with discrete valuation $v_Y$ and $f\in K(X)^\times$, $\operatorname{ord}_Y(f)=v_Y(f)$, positive at zeros and negative at poles. For a Cartier divisor $D$, $\operatorname{ord}_Y(D)=v_Y(f_U)$ for any local equation $f_U$ meeting $Y$.
:::

::: {.front card-id="card-bbf4fa36ebc32812" tags="definition"}
What is the definition of Picard variety?
:::

::: {.back card-id="card-bbf4fa36ebc32812"}
The identity component $\operatorname{Pic}^0(X)\subset\operatorname{Pic}(X)$, consisting of line bundles algebraically equivalent to $\mathcal O_X$. For a smooth projective curve it is an abelian variety of dimension $g=h^1(X,\mathcal O_X)$.
:::

::: {.front card-id="card-154c64bcc6a9b942" tags="definition"}
What is the definition of Pure dimension?
:::

::: {.back card-id="card-154c64bcc6a9b942"}
A scheme is pure of dimension $n$ if every irreducible component has dimension $n$. Kleiman transversality gives that a general translate $gY\cap Z$ is empty or pure of dimension $\dim Y+\dim Z-\dim X$.
:::

::: {.front card-id="card-52521761b1264fd0" tags="definition"}
What is the definition of Rational equivalence?
:::

::: {.back card-id="card-52521761b1264fd0"}
Two $k$-cycles are rationally equivalent if their difference is a sum of pushforwards along morphisms $\mathbb P^1\to X$ of divisors $\operatorname{div}(f)$ of rational functions on $\mathbb P^1$. The Chow group $\operatorname{CH}_k(X)$ is the group of $k$-cycles modulo this relation.
:::

::: {.front card-id="card-6be11a2773451a11" tags="definition"}
What is the definition of Rational function field?
:::

::: {.back card-id="card-6be11a2773451a11"}
For an integral scheme $X$ with generic point $\eta$, $K(X)=\mathcal O_{X,\eta}$; for an integral affine variety $X=\operatorname{Spec}A$ it is $\operatorname{Frac}(A)$. Its elements are the rational functions on $X$.
:::

::: {.front card-id="card-2aacb7cbbb4c8bc0" tags="definition"}
What is the definition of Regular system of parameters?
:::

::: {.back card-id="card-2aacb7cbbb4c8bc0"}
In a regular local ring $(R,\mathfrak m)$ of dimension $n$, a regular system of parameters is a minimal generating set $x_1,\dots,x_n$ of $\mathfrak m$, equivalently a basis of $\mathfrak m/\mathfrak m^2$. Geometrically these are independent local coordinates.
:::

::: {.front card-id="card-3db395d10336f96a" tags="definition"}
What is the definition of Very ample?
:::

::: {.back card-id="card-3db395d10336f96a"}
A line bundle $L$ on a scheme $X$ is very ample if global sections $s_0,\dots,s_N\in H^0(X,L)$ define a closed immersion $X\hookrightarrow\mathbb P^N$, $x\mapsto(s_0(x):\cdots:s_N(x))$. Equivalently, $L\cong i^*\mathcal O_{\mathbb P^N}(1)$ for some closed immersion $i:X\hookrightarrow\mathbb P^N$.
:::
