---
title: "Algebraic Geometry::Divisors"
---

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
A pair $(s, U)$ with $U\subseteq X$ open containing all associated points of $X$, $s\in H^0(U; {\mathcal{L}})$, and $(s_1, U_1) \sim (s_2, U_2) \iff$ $s_1=s_2$ on $U_{12}$.
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
Rational section: $s: X\to {\mathcal{L}}$ defined on an open dense subset. A nonzero rational section $s$ of an invertible sheaf ${\mathcal{L}}$ defines a Cartier divisor: write $s=f_i e_i$ in each local frame $e_i$ and use the rational functions $f_i$ as local equations. With the convention ${\mathcal{L}}\cong\mathcal O_X(D)$, the canonical rational section of $\mathcal O_X(D)$ has divisor $D$.

As a Weil divisor: for any $Y\in \operatorname{Div}(X)$ define $(s) \coloneqq\sum_{Y\in \operatorname{Div}(X)} v_Y(s) Y$, where $v_Y(s) \coloneqq v_Y(\sigma(s))$ for a trivialization $\sigma: {\mathcal{L}}_{X, Y} { \, \xrightarrow{\sim}\, }{\mathcal{O}}_{X, Y}$ of the stalk at the generic point of $Y$. This is a valuation ring when $X$ is integral (and regular in codimension one). For $s\in H^0({\mathcal{L}})\setminus\left\{{0}\right\}$, $(s)$ is effective.
:::

::: {.front card-id="card-20c128cfdff9a4d9"}
For $D$ a divisor, what is ${\mathcal{O}}_X(D)$?
:::

::: {.back card-id="card-20c128cfdff9a4d9"}
${\mathcal{O}}_X(D)(U) \coloneqq\left\{{f\in K(X)^{\times}{~\mathrel{\Big\vert}~}(f) + D \geq 0 \text{ on } U}\right\} \cup \left\{{0}\right\}$, a subsheaf of the constant sheaf $K(X)$. Global sections: $H^0({\mathcal{O}}_X(D)) = \left\{{f\in K(X)^{\times}{~\mathrel{\Big\vert}~}(f) + D \geq 0}\right\} \cup \left\{{0}\right\}$.
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
Take $p_1\neq p_2$, then if $p_1-p_2 = (f)$ for some $f: E\to {\mathbf{P}}^1$ this produces an injective holomorphic map and forces $E\cong {\mathbf{P}}^1$; however e.g. $g(E) = 1\neq 0 = g({\mathbf{P}}^1)$. In general $\operatorname{Pic}(E) \cong \operatorname{Pic}^0(E) \oplus {\mathbf{Z}}\cong E\oplus {\mathbf{Z}}$.
:::

::: {.front card-id="card-5f35d5826acfaa91"}
Show that if $D = V(f)$ is a hypersurface in ${\mathbf{P}}^n$ then $D\sim \deg(f) H$, so $\operatorname{Pic}({\mathbf{P}}^n) = \left\langle{H}\right\rangle_{\mathbf{Z}}$.
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
A closed integral subscheme $Y\leq X$ of dimension 1.
:::

::: {.front card-id="card-4229cc42c6837e32"}
What is a **Weil** divisor?
:::

::: {.back card-id="card-4229cc42c6837e32"}
The free ${\mathbf{Z}}{\hbox{-}}$module on prime divisors, so $D = \sum_{i\in I} n_i Y_i$ where $I$ indexes prime divisors.
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

$\operatorname{Cl}({\mathbf{A}}^n)$ is zero since $k[x_1, \cdots, x_{n}]$ is a UFD, $\operatorname{Cl}({\mathbf{P}}^n_{/ {k}}) \cong k$ generated by a hyperplane, induced by the degree morphism.

For $Z\leq X$ proper closed and $U\coloneqq X\setminus Z$, $\operatorname{Cl}(X) \twoheadrightarrow \operatorname{Cl}(U)$ by taking $\sum n_i Y_i \mapsto \sum n_i (Y_i \cap Z)$ and is injective if $\operatorname{codim}_X(Z) \geq 2$. If $Z$ is irreducible of codimension 1, then one gets a right-SES ${\mathbf{Z}}\to  \operatorname{Cl}(X) \twoheadrightarrow \operatorname{Cl}(U)$.
:::

::: {.front card-id="card-c8a4fd5da4688a38"}
Is $\operatorname{Cl}(X)$ always free?
:::

::: {.back card-id="card-c8a4fd5da4688a38"}
No, it can contain torsion: let $Y\subseteq {\mathbf{P}}^2$ be an irreducible curve of degree $d$ and let $X\coloneqq{\mathbf{P}}^2\setminus Y$, then ${\mathbf{Z}}\xrightarrow{\times d}  \operatorname{Cl}({\mathbf{P}}^2)\cong {\mathbf{Z}}\twoheadrightarrow \operatorname{Cl}({\mathbf{P}}^2\setminus Y) \implies  \operatorname{Cl}(X) \cong C_d$
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
A global section $s\in H^0(X; {\mathcal{K}}^{\times}/{\mathcal{O}}^{\times})$, described by an open cover $U_i\rightrightarrows X$, $f_i \in H^0(U_i; {\mathcal{K}}^{\times})$, and ${f_i\over f_j}\in H^0(U_{ij}; {\mathcal{O}}^{\times})$.

Equivalently, a locally principal Weil divisor.
:::

::: {.front card-id="card-765642427aa86626"}
What is a **principal** Cartier divisor?
:::

::: {.back card-id="card-765642427aa86626"}
Anything in the image of $H^0({\mathcal{K}}^{\times}) \to H^0({\mathcal{K}}^{\times}/{\mathcal{O}}^{\times})$.
:::

::: {.front card-id="card-b39fa8bac52d9231"}
Give an example of a Weil divisor that is not Cartier.
:::

::: {.back card-id="card-b39fa8bac52d9231"}
Take $X = V(xy-z^2) \subseteq {\mathbf{A}}^3$ and let $Y$ be its ruling $\left\{{ p\in Y{~\mathrel{\Big\vert}~}y=z=0}\right\}$. Then $Y$ can not be locally principal in a neighborhood of the cone point. However, $2Y$ is locally principal and in fact principal. The divisor $D=V(x,z)$ is not of the form $V = (f)$ for any $f\in K(X)$ near the origin.
:::

::: {.front card-id="card-15ea337ffea63d93" tags="definition"}
What are **ample** and **very ample** invertible sheaves (divisors)?
:::

::: {.back card-id="card-15ea337ffea63d93"}
Very ample: ${\mathcal{L}}$ invertible is very ample relative to $f:X\to Y$ if $\exists {\mathcal{E}}\in {\mathsf{QCoh}}(Y)$ and an immersion $\iota: X\to {\mathbf{P}}({\mathcal{E}})$ such that ${\mathcal{L}}\cong \iota^* {\mathcal{O}}_{{\mathbf{P}}({\mathcal{E}})}(1)$. Over $S$: an immersion $X\hookrightarrow\mathbb P_S^n$ with ${\mathcal{L}}\cong i^*\mathcal O(1)$. Over a field: ${\mathcal{L}}$ is bpf/gg and $\phi_{{\left\lvert {{\mathcal{L}}} \right\rvert}}: X\to {\mathbf{P}}^{h^0({\mathcal{L}}) - 1}$ is a closed immersion.

Ample: equivalent conditions (for $X$ of finite type over a Noetherian ring):

- ${\mathcal{L}}^n$ is very ample for some $n > 0$, so defines an embedding $\phi_{{\left\lvert {{\mathcal{L}}^n} \right\rvert}}: X\to {\mathbf{P}}^N$ where ${\mathbf{P}}^N \cong {\mathbf{P}}H^0(X; {\mathcal{L}}^n) {}^{ \vee }$.
- (Serre) For any ${\mathcal{F}}\in {\mathsf{QCoh}}(X)^\mathrm{ft}$, the twist ${\mathcal{F}}(n) \coloneqq{\mathcal{F}}\otimes{\mathcal{L}}{ {}^{ \scriptstyle\otimes_{}^{n} }  }$ is globally generated for all $n> N_0 \gg 0$: tensoring high powers with a coherent sheaf gives many global sections.
- Every point has an affine neighborhood of the form $X_s=\{s\ne0\}$ for some global section $s$ of some positive power ${\mathcal{L}}^{\otimes n}$.
:::

::: {.front card-id="card-f8c8b2968ad6e404"}
What is a **simple normal crossings (SNC)** divisor?
:::

::: {.back card-id="card-f8c8b2968ad6e404"}
Normal crossings: A Weil divisor $D = \sum D_i$ is NC iff for every $x\in X$ a local equation for $D$ is $\prod_{i=1}^r x_i$ for independent local parameters $x_i\in {\mathcal{O}}_{X, x}$. SNC is if every $D_i$ is smooth and $r\leq n$.

Equivalently, $D$ is SNC if there exists a finite family of sections $\left\{{f_i}\right\} \subseteq H^0({\mathcal{O}}_X)$ such that $D = \sum (f_i)$ and for each $x\in \mathop{\mathrm{supp}}D$, the restrictions $(f_i)_x \in {\mathfrak{m}}_x$ land in the maximal ideal and form part of a regular system of parameters for ${\mathcal{O}}_{X, x}$.\
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
On an integral scheme, a Cartier divisor $D$ is given by local nonzero rational functions $\left\{{(U_i, f_i)}\right\}$ with $f_i/f_j\in\mathcal O_X^\times$ on overlaps. Then ${\mathcal{O}}_X(D) = {\mathcal{L}}(D) \leq {\mathcal{K}}$ is the sub-${\mathcal{O}}_X$-module of the sheaf of rational functions generated by $\left\{{f_i^{-1}}\right\}$, i.e. locally $f_i^{-1}\mathcal O_X$. There is a bijection between Cartier divisors and invertible subsheaves of ${\mathcal{K}}$.
:::

::: {.front card-id="card-4c5b6d6b7feab01a"}
What is the relationship between the Cartier class group and $\operatorname{Pic}(X)$?
:::

::: {.back card-id="card-4c5b6d6b7feab01a"}
In general, $\mathop{\mathrm{Cart}} \operatorname{Cl}(X) \hookrightarrow\operatorname{Pic}(X)$ by $D\mapsto {\mathcal{L}}(D)$; this is surjective when $X$ is integral.
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
For $D$ effective, the subscheme $Y$ of codimension 1 defined by the sheaf of ideals ${\mathcal{I}}_Y$ which is locally generated by the $f_i$. In fact ${\mathcal{I}}_Y \cong {\mathcal{L}}(-D)$ in this case.
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
For a divisor $D=\sum_P n_P[P]$ on a proper curve over $k$, $\deg D=\sum_P n_P[\kappa(P):k] \in {\mathbf{Z}}$. Over an algebraically closed field, this is $\deg(D) = \sum_P n_P$.
:::

::: {.front card-id="card-e8e202eb43c56fe4"}
For $D$ a prime divisor and $Y\in \mathop{\mathrm{supp}}D$, what is the **multiplicity** of $Y$ in $D$?
:::

::: {.back card-id="card-e8e202eb43c56fe4"}
$D = \sum n_{Y_i} Y_i$ and $Y= Y_j$ for some $j$ since $Y\in \mathop{\mathrm{supp}}D$, so ${\operatorname{mult}}_D(Y) = n_Y$.
:::

::: {.front card-id="card-f8d3ad922064fbf7" tags="definition"}
What are the **multiplicity** and the **support** of a Cartier divisor?
:::

::: {.back card-id="card-f8d3ad922064fbf7"}
Coefficient along a prime divisor: for a Cartier divisor $D$ on a regular (or normal) integral scheme, its coefficient at a codimension-one point $\eta$ (prime divisor $Y$) is the valuation $v_Y(f_i) = \operatorname{ord}_\eta(f_i)$ of a local equation $f_i$ on any $U_i$ with $U_i \cap Y\neq \emptyset$.

Multiplicity at a point: for $D$ an effective Cartier divisor on $X$, let $f$ be a local equation at $p$ and define $\mu_p(D)$ to be the largest $N$ such that $f\in {\mathfrak{m}}_p^N \subseteq {\mathcal{O}}_{X, p}$. Note $\mu_p \geq 1 \iff p\in \mathop{\mathrm{supp}}D$, and for $X$ smooth at $p$, $\mu_p = 1 \iff D$ is smooth at $p$.

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
${\left\lvert {D} \right\rvert} = \left\{{ D' {~\mathrel{\Big\vert}~}D'\sim D}\right\}$
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

Equivalently, the corresponding line bundle ${\mathcal{L}}$ is generated by global sections, where $S$ corresponds to $V \subseteq H^0(X; {\mathcal{L}})$ for some ${\mathcal{L}}\in \operatorname{Pic}(X)$, since $p$ is a base point iff $s_p\in {\mathfrak{m}}_p {\mathcal{L}}_p$ for all $s\in V$.
:::

::: {.front card-id="card-7dfe2d5e36a21bf9"}
When is the morphism defined by a linear system a closed immersion?
:::

::: {.back card-id="card-7dfe2d5e36a21bf9"}
Separates points and separates tangents: $\forall p, q\in X$ there exists $D\in S$ with $p\in D$ and $q\not\in D$; given $p\in X, t\in {\mathbf{T}}_p X$, there is a $D\in S$ with $p\in D$ but $t\not \in {\mathbf{T}}_p(D) \coloneqq\qty{{\mathfrak{m}}_{P, D}/{\mathfrak{m}}_{P, D} } {}^{ \vee }$
:::

::: {.front card-id="card-a7508a5971d896ab"}
What is the **base locus** of a linear system?
:::

::: {.back card-id="card-a7508a5971d896ab"}
The union of all base points in $S$.
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
A choice of ${\mathcal{L}}\in {\operatorname{NS}}(X)^\mathrm{amp}$, where ${\operatorname{NS}}(X) \coloneqq\operatorname{Pic}(X)/\operatorname{Pic}^0(X)$. Principal if $\deg {\mathcal{L}}= 1$.
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
but $\ker({\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_R) \cong {\mathcal{L}}(-R)$, so
$$f^* \Omega_{Y/k} \otimes\Omega_{X/k} {}^{ \vee }\cong {\mathcal{L}}(-R)$$
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
$A\to B \to C$ a SES in ${}_{{\mathcal{O}}_X}{\mathsf{Mod}}$ yields $\operatorname{det}(A) \otimes_{{\mathcal{O}}_X} \operatorname{det}(C) \cong \operatorname{det}(B)$.
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
