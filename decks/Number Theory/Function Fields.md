---
title: "Number Theory::Function Fields"
---

::: {.front card-id="card-b84d44b44375c1aa"}
Essential feature of Wiles FLT: arithmetic cohomology.
:::

::: {.back card-id="card-b84d44b44375c1aa"}
- Put a topology on the algebra of functions, vs the discrete set of solutions over ${ \mathbf{F} }_q$.
:::

::: {.front card-id="card-01e3480a67dce5a8"}
$e_C(\ell z) = C_\ell(e_C(z))$ where $C_\ell$ is an additive polynomial: analog of $e^{\ell z} = (e^z)^\ell$.
:::

::: {.back card-id="card-01e3480a67dce5a8"}
- The map $\ell \mapsto C_\ell(z)$ is the Carlitz module.
- Yields a theory of $n!$ (i.e. $\Gamma(n)$) and Bernoulli functions.
- "Division values" of $e_C(z)$ generate abelian cyclotomic extensions of $\QQ$, analogous to division values of $e^{2\pi i z}$.
- Has "rank" 1.
:::

::: {.front card-id="card-678431dcdb3f4394" cite="[@Dri74]"}
Drinfeld generalizes in 74: general exponentials of higher rank, for arbitrary function fields and choices of infinite places.
:::

::: {.back card-id="card-678431dcdb3f4394"}
- The Carlitz module is the simplest Drinfeld modules.
- Constructs a moduli of such modules
- Uniformize the moduli using Tate's rigid analytic geometry.
- His goal: prove Langlands-esque reciprocity laws.
- Yields class fields.
- Generalize elliptic curves and higher so-called $T\dash$modules which generalize abelian varieties.
- Generalize *to* shtukas: Drinfeld modules with a vector bundle.
:::

::: {.front card-id="card-27040a809f277e7f"}
Toward analogs of $L\dash$functions for abelian varieties and analogs of RH for them: fix $K$ a function field,
:::

::: {.back card-id="card-27040a809f277e7f"}
- $A \coloneqq$ functions in $K$ which are regular away from $\infty$, generalizes ${ \mathbf{F} }_q[T]$, is a Dedekind domain with finite unit group and class number.
- Given a Drinfeld module $\psi$ over a field $L$, this gives $L$ a new $A\dash$module structure. Use this to define an analog of the Tate module of $\psi$.
- The charpoly of $\operatorname{Frob}_L$ has coefficients in $A$ (instead of $\ZZ$), assemble these into an Euler product and thus an $L\dash$function.
:::

::: {.front card-id="card-6ce63f23672491e6"}
Three themes:
:::

::: {.back card-id="card-6ce63f23672491e6"}
- Function fields are "bigger" than number fields: over $\QQ$, analytically complete and then take a degree 2 field extension to close algebraically to get $\CC$, but for function fields, completing yields a local field which may have infinitely many extensions of a fixed degree. Things identified in the number field case split up in the function field case.
- Arithmetic/geometric dichotomy: function fields have two types of cyclotomic extensions, adjoining $\zeta_n$ (everywhere unramified, related to extensions of constant field) or ramified "geometric" extensions (by division values of Drinfeld modules).
- Two $T$'s, as an operator (gives rise to $L\dash$functions and a scalar (gives rise to $\Gamma\dash$functions).
:::

::: {.front card-id="card-c660fc641e641fdb"}
Main features of Drinfeld modules:
:::

::: {.back card-id="card-c660fc641e641fdb"}
- The lattice ${ \mathbf{F} }_q[T]\xi$
- Its exponential, similar to $e_C(x)$
- The multiplication formula for $e_C(x)$, similar to the Carlitz module $C$
- Algebraicity of $C$ and reduction to "finite fields"
- The action of ${ \mathbf{F} }_q[t]$ on rational points via $C$.
:::

::: {.front card-id="card-eea3b0fb490a56f6"}
Notation:
:::

::: {.back card-id="card-eea3b0fb490a56f6"}
- $X$ smooth projective geometrically connected curve over ${ \mathbf{F} }_r$ where $r = p^{m_0}$.
- $\infty\in X$ a fixed closed point of degree $d_\infty$ over ${ \mathbf{F} }_q$.
- $k$ is the function field of $X$
- $A \subset k$ the functions regular away from $\infty$
- $v_\infty$ the valuation at $\infty$
- $K \coloneqq k_\infty$ its completion at $\infty$.
- $C_\infty$ the completion of $\operatorname{cl}^{\mathrm{alg}}K$ (algebraically closed)
- $\deg D$ for $D\in \operatorname{Div}(X)$ is the degree of $D$ over ${ \mathbf{F} }_r$.
- $d_\infty = \deg \infty$.
- For $x\in K$, $\deg(x) \coloneqq-d_\infty v_\infty(x)$ so $\deg(a) = \log_r({\sharp}{\mathbf{A}}/a)$ for $a\in A\setminus\left\{{0}\right\}$ (the degree of the finite part of the divisor of $a$)
- ${\left\lvert {x} \right\rvert}_\infty \coloneqq r^{\deg x}$the normalized absolute value, extended to $C_\infty$.
- $Jac_X({ \mathbf{F} }_q)$ the (finite) group of degree zero divisors on $X$, mod divisors of elements of $k^{\times}$.
- $h(k) = {\sharp}\operatorname{Jac}_X({ \mathbf{F} }_q)$ the "class number" of $k$. $h(A)$ is the class number of $A$ as a Dedekind domain.
:::

::: {.front card-id="card-168edf39343d86d9"}
Facts:
:::

::: {.back card-id="card-168edf39343d86d9"}
- $A$ is Dedekind at $\operatorname{Spec}A = X\setminus\left\{{ \infty }\right\}$
- $A^{\times}= { \mathbf{F} }_q^{\times}$ since every nonconstant $a\in A$ needs zeros to balance out the pole at $\infty$ since $\deg a = 0$ for any principal divisor $a$.
:::

::: {.front card-id="card-6cc1394c5c90ca55"}
For a nonzero fractional $A$-ideal $I\subseteq k$, what are the topological properties of $I\subset K$? Why?
:::

::: {.back card-id="card-6cc1394c5c90ca55"}
$I$ is discrete and cocompact in $K$.

- Discreteness: $\exists a\in k^{\times}$ st $aI \subseteq A$.
- Compactness of $K/I$: Riemann-Roch
:::

::: {.front card-id="card-15b76f738e1bec0f"}
Analogies:
:::

::: {.back card-id="card-15b76f738e1bec0f"}
- $\ZZ\leadsto A$
- $\QQ\leadsto k$
- ${\mathbf{R}}\leadsto K$\
:::

::: {.front card-id="card-71f738e7fc96b2c4"}
Motto: function field theory decomposes classical number-theoretic objects into arithmetic components.
:::

::: {.back card-id="card-71f738e7fc96b2c4"}
- Example: will need many Hilbert class fields to play the role of $\QQ$,
:::

::: {.front card-id="card-9d15d0cc12f3a90f"}
What is an $M$-lattice, and what is its rank?
:::

::: {.back card-id="card-9d15d0cc12f3a90f"}
Let $M\subseteq C_\infty$ be a field containing $k$. An $M$-lattice is an $A$-submodule $L\subseteq M^{\mathrm{sep}}\subseteq C_\infty$ that is finitely generated over $A$, discrete in $C_\infty$, and stable under $G_M=\operatorname{Gal}(M^{\mathrm{sep}}/M)$. Its rank is $\operatorname{rank}_A L$.
:::

::: {.front card-id="card-a47a773808d252c6"}
For an $M$-lattice $L$, where is $e_L$ analytic, and where do its Taylor coefficients lie? Why?
:::

::: {.back card-id="card-a47a773808d252c6"}
$e_L$ is entire on $C_\infty$, with Taylor coefficients at $0$ in $M$.

- Proof: convergence is due to discreteness of $L$, the Taylor expansion is from $G_M \coloneqq \Gal(M^{ {}^{ \operatorname{sep} } }/M)$ which fixes $L$ and the nature of the continuous action $G_M\curvearrowright M^{ {}^{ \operatorname{sep} } }$. So $e_L$ is a non-constant entire function and thus surjective.
:::

::: {.front card-id="card-8f2e3bd06d6b417a"}
For $0\ne a\in A$, express $e_L(ax)$ in terms of $e_L(x)$ and the nonzero classes in $a^{-1}L/L$.
:::

::: {.back card-id="card-8f2e3bd06d6b417a"}
$$e_L(ax) = ae_L(x)\cdot \prod_{a\in (a^{-1}L/L)\setminus\left\{{0}\right\}} \qty{1 - {e_L(x)\over e_L(a)}}$$

- Proof: short.
:::

::: {.front card-id="card-fa7e496f4f0f935c"}
For the additive polynomials defined by $e_L(ax)=\phi_a(e_L(x))$, how does $a\mapsto\phi_a$ respect scalars and multiplication?
:::

::: {.back card-id="card-fa7e496f4f0f935c"}
$$\begin{align} A &\to M\left\{{\tau}\right\} \\ a&\mapsto \phi_a\end{align}$$
satisfies:

- ${ \mathbf{F} }_r\dash$linear,
- $a\in { \mathbf{F} }_r \subset A\implies \phi_a = a \tau^0$,
- $\phi_{ab}(\tau) = \phi_a(\tau)\phi_b(\tau) = \phi_b(\tau)\phi_a(\tau) = \phi_{ba}(\tau)$.
:::

::: {.front card-id="card-360f6bdb868cede0"}
What is the Drinfeld module associated to an $A$-lattice $L$, and what is its rank?
:::

::: {.back card-id="card-360f6bdb868cede0"}
The injection
$$\begin{align} A &\to M\left\{{\tau}\right\} \\ a&\mapsto \phi_a\end{align}$$
which has rank $d = \operatorname{rank}_A(L)$.
:::

::: {.front card-id="card-0d5faf71b98a4979"}
What is an $A$-field? Define its $A$-characteristic and distinguish generic from finite characteristic.
:::

::: {.back card-id="card-0d5faf71b98a4979"}
An $A\dash$field $F$ is a field with a morphism $i:A\to F$; $\ker i =\mfp$ is prime and $\operatorname{ch}F \coloneqq\mfp$; $F$ has "generic characteristic" (char zero) if $\mfp= \left\langle{0}\right\rangle$, otherwise $F$ has finite characteristic.

- Agrees with definition for $A = { \mathbf{F} }_r[T]$.
:::

::: {.front card-id="card-4373490afd563e55"}
There is a theory of morphisms of Drinfeld modules, parallels elliptic curves
:::

::: {.back card-id="card-4373490afd563e55"}
- isomorphism iff degree zero,
- if $G/F$ is any algebraically closed extension then $\hom_{\overline{F}}(\psi,\psi) \hookrightarrow\mathop{\mathrm{Hom}}_G(\phi, \psi)$,
- ${ \operatorname{End} }_F(\psi)$ is commutative and torsionfree projective $A\dash$module of rank $\leq d^2$
- Characterization of when certain group schemes are kernels of isogenies
:::

::: {.front card-id="card-fddae515b7c5749f"}
Let $E/k \subseteq C_\infty$ be a finite extension, then $E$ is a $\CM_\infty\dash$field iff it contains exactly one prime above $\infty$.
:::

::: {.back card-id="card-fddae515b7c5749f"}
- Can constructed Drinfeld modules with CM by the maximal order ${\mathcal{O}}\coloneqq A_E$, the $A\dash$integers in $E$ where ${\mathcal{O}}\hookrightarrow{ \operatorname{End} }(\psi)$
- For $L\subset C_\infty$ a lattice for ${\mathcal{O}}$ of rank $d_1$, it induces an $A\dash$lattice of rank $d\coloneqq d_1\cdot [E:k]$ which induces a Drinfeld module $\psi$; say $\psi$ has sufficiently many CMs iff $d_1 = 1$ iff $L\cong I$ where $I$ is an ${\mathcal{O}}\dash$ideal.
- Can define conductors: letting $\tilde {\mathcal{O}}$ be the maximal order (the $A\dash$integers), the conductor is the largest ideal $\mathfrak c\normal\tilde {\mathcal{O}}$ which is also an ideal in ${\mathcal{O}}$.
:::

::: {.front card-id="card-2f5aae3903cdd2cd"}
For $X\in \Sch$, define an Euler product
:::

::: {.back card-id="card-2f5aae3903cdd2cd"}
$$\zeta_X(s) \coloneqq\prod_{x\in {\left\lvert {X} \right\rvert}} {1\over 1 - {\left\lVert {x} \right\rVert}^{-s} },\qquad {\left\lVert {x} \right\rVert} \coloneqq{\sharp}\kappa(x) \coloneqq{\sharp}({\mathcal{O}}_{X, x}/\mfm_x)$$

- Can expand in a sum
$$\zeta_X(s) = \sum_{D\in \operatorname{Div}_{>0}(X)} {1\over {\left\lVert {D} \right\rVert}^{-s} },\qquad {\left\lVert {D} \right\rVert} \coloneqq r^{\deg D}$$
where $\operatorname{Div}_{>0}(X)$ are positive divisors.
:::

::: {.front card-id="card-040257f9706efe04"}
Set$u\coloneqq r^{-s}$ to define $Z_X(u) \coloneqq\zeta_X(s)$ and
:::

::: {.back card-id="card-040257f9706efe04"}
$$Z_X(u) = {P_X(u) \over (1-u)(1-ru)}, \qquad \deg P_X(u) = 2g(X)$$
where $P_X(1) = h(k)$ is the class number of the field $k$.

- Satisfies a functional equation
$$P_X(u) = r^g u^{2g} P_X\qty{1\over ru}$$
, and setting $\xi_X(s) = r^{s(g-1)} Z_X(s)$ one has
$$\xi_X(s) = \xi_X(1-s)$$
:::

::: {.front card-id="card-3676abd814105539"}
$L\dash$series: $X$ a curve over ${ \mathbf{F} }_r$ where $r= p^{m_0}$, fixed closed point $\infty$, function field $k$ with completion $K$ at $\infty$, $\operatorname{Spec}A = X\setminus\left\{{ \infty }\right\}$, $C_\infty =$ complete $k$, take algebraic closure, take completion. $G = \Gal(k{ {}^{ \operatorname{sep} } }/k)$, $\ell\neq p\in \ZZ$ a prime, $\rho: G\to \operatorname{GL}(V)$ a continuous finite dimensional $\ell\dash$adic representation.
:::

::: {.back card-id="card-3676abd814105539"}
- E.g. for $Z$ an abelian variety over $k,$ define $\ell\dash$adic Tate module $T_\ell(Z)$ and set

$$V \coloneqq\mathop{\mathrm{Hom}}_{{ \ZZ_{\widehat{\ell}} }}(T_\ell(Z), { \QQ_\ell }) \cong H^1_\text{ét}(Z; { \QQ_\ell }) \in   {}_{G}\Mod$$

- For $w\in {\left\lvert {X} \right\rvert}$, define

$$f_w(u) \coloneqq f_{\overline{w}}(u) \coloneqq\operatorname{det}\qty{1 - \operatorname{Frob}_{\overline{w}}u \st V^{I_{\overline{w}}}}$$
where $\overline{w}$ is an point over $w$ in $\kbar$ and $I_{\overline{w}}$ is its inertia group and $V^{I_{\overline{w}}}$ is the fixed subspaces with $\operatorname{Frob}_{\overline{w}}(u) \in D_{\overline{w}}/I_{\overline{w}}$ the geometric Frobenius (inverse of usual).

- Define
$$L_V(s) \coloneqq\prod_{w\in {\left\lvert {X} \right\rvert}} f_w({\left\lVert {w} \right\rVert}^{-s})^{-1},\qquad {\left\lVert {w} \right\rVert} \coloneqq{\sharp}\kappa(w)$$
:::

::: {.front card-id="card-998ffc9f1e45a806" cite="[@Yu86; @Gos98, Theorem 8.18.8]"}
For $A={\mathbf F}_r[T]$, what does Yu's theorem say about transcendence of $\zeta_A(i)$ and $\zeta_A(i)/\varepsilon^i$ for positive integers $i$?
:::

::: {.back card-id="card-998ffc9f1e45a806"}
$\zeta_A(i)$ is transcendental over $k$ for every positive integer $i$. If $r-1\nmid i$, then $\zeta_A(i)/\varepsilon^i$ is also transcendental over $k$.

- Here $\zeta_A(s) = \sum_{I\subseteq A} I^{-s}$.
:::

::: {.front card-id="card-370ac2c151e43eba" cite="[@Wan96; @Gos98, Theorem 8.24.5]"}
Define the completed Riemann zeta function and its entire normalization. State RH and compare its zero-location assertion with Wan's function-field result.
:::

::: {.back card-id="card-370ac2c151e43eba"}
$$\xi(s) \coloneqq\zeta_\infty(s)\cdot \zeta(s), \qquad \zeta_\infty(s) \coloneqq\Gamma\qty{s\over 2} \pi^{-{s\over 2}}$$
and
$$\widehat{\xi}(s) \coloneqq s(1-s)\xi(s)$$
to get an entire function with $\widehat{\xi}(s) = \widehat{\xi}(1-s)$.

- RH: the zeroes of $\widehat{\xi}$ are of the form ${1\over 2} + i\beta$ for $\beta\in {\mathbf{R}}$; can shift and rotate to get a function $\theta(u)$ and equivalently ask that the zeros of $\theta$ are real.
- Relate to Wan's theorem: Let $y\in { \ZZ_{\widehat{p}} }$ where each $r\dash$adic digit of $-y$ is less than $p$ or equal to $r-1$. Then the zeros of $\zeta_A(x, y)$ are in $K$ and simple.
- ${\mathbf{R}}$ is a "small" local field and the zeros of $\theta(u)$ are either in ${\mathbf{R}}$ or $\CC$, a degree 2 extension. Compare to zeros of $\zeta_A(s)$ which could be in an extension of $K$ of arbitrary (even infinite) degree but are in $K$ itself.
:::

::: {.front card-id="card-ae19b5ca76b254e2" tags="definition"}
What is the definition of Additive polynomial?
:::

::: {.back card-id="card-ae19b5ca76b254e2"}
An additive polynomial over a ring of characteristic $p$ is a polynomial $f(x)$ satisfying $f(x+y)=f(x)+f(y)$; equivalently, $f(x)=\sum_i a_i x^{p^i}$ is a linearized polynomial. The Carlitz module is defined by additive polynomials $C_\ell$.
:::

::: {.front card-id="card-c67566c48c2a34b5" tags="definition"}
What is the definition of Carlitz module?
:::

::: {.back card-id="card-c67566c48c2a34b5"}
The Carlitz module is the Drinfeld module over $\mathbb{F}_q[T]$ given by the $\mathbb{F}_q$-algebra homomorphism $\mathbb{F}_q[T]\to\operatorname{End}(\mathbb{G}_a)$, $T\mapsto C_T$, where $C_T(x)=Tx+x^q$. It is the simplest Drinfeld module and the function-field analogue of the multiplicative group $\mathbb{G}_m$.
:::

::: {.front card-id="card-e680d9239eb8efcc" tags="definition"}
What is the definition of Class number?
:::

::: {.back card-id="card-e680d9239eb8efcc"}
The class number $h_K$ of a number field $K$ is the order $\#\mathrm{Cl}(K)$ of its ideal class group; for a function field it is $\#\mathrm{Jac}_X(\mathbb{F}_q)$. It measures the failure of the ring of integers to be a unique factorization domain: $h_K=1$ iff $\mathcal{O}_K$ is a UFD.
:::

::: {.front card-id="card-b78b5390e64274e8" tags="definition"}
What is the definition of Cocompact subgroup?
:::

::: {.back card-id="card-b78b5390e64274e8"}
A subgroup $\Gamma$ of a topological group $G$ is cocompact if the quotient space $G/\Gamma$ with the quotient topology is compact.
:::

::: {.front card-id="card-a83d9f2a77039635" tags="definition"}
What is the definition of Conductor of an order?
:::

::: {.back card-id="card-a83d9f2a77039635"}
For an order $\mathcal{O}$ in the maximal order $\widetilde{\mathcal{O}}$ of a number field (or an $A$-order in a finite extension), the conductor is $\mathfrak{c}=\{x\in\widetilde{\mathcal{O}}:x\widetilde{\mathcal{O}}\subseteq\mathcal{O}\}$, the largest ideal of $\widetilde{\mathcal{O}}$ contained in $\mathcal{O}$ (equivalently, also an ideal of $\mathcal{O}$).
:::

::: {.front card-id="card-8bcaeb6ede9a28e4" tags="definition"}
What is the definition of Division value?
:::

::: {.back card-id="card-8bcaeb6ede9a28e4"}
A division value of an exponential $e_C$ (or $e_L$) is a value $e_C(a)$ at a torsion point $a$ of the lattice or module. Division values generate abelian extensions of the base field, analogous to how roots of unity generate cyclotomic extensions.
:::

::: {.front card-id="card-c93dee3736bd75a3" tags="definition"}
What is the definition of Function field?
:::

::: {.back card-id="card-c93dee3736bd75a3"}
(1) A function field in one variable over a field $k$ is a finitely generated field extension of $k$ of transcendence degree $1$. In number theory $k$ is usually a finite field $\mathbb{F}_q$, and the function field is the field of rational functions on a smooth projective curve over $\mathbb{F}_q$. (2) For an integral scheme $X$ with generic point $\eta$, the function field is $K(X)=\mathcal O_{X,\eta}$. For an integral variety over a field $k$, it is the field of rational functions on $X$.
:::

::: {.front card-id="card-f8f953bc6c2c0578" tags="definition"}
What is the definition of Functional equation?
:::

::: {.back card-id="card-f8f953bc6c2c0578"}
A functional equation for a zeta or $L$-function is an identity relating $\Lambda(s)$ to $\Lambda(1-s)$ (or $Z(u)$ to $Z(1/(ru))$), where $\Lambda$ is the completed function including archimedean and conductor factors. It expresses the symmetry of the completed function about the critical line.
:::

::: {.front card-id="card-e2876b1ae69fd850" tags="definition"}
What is the definition of Geometric frobenius?
:::

::: {.back card-id="card-e2876b1ae69fd850"}
For a variety over $\mathbb{F}_q$, the geometric Frobenius is the inverse of the arithmetic Frobenius $x\mapsto x^q$ in $\mathrm{Gal}(\overline{\mathbb{F}}_q/\mathbb{F}_q)$; it acts on $\ell$-adic étale cohomology. For a closed point $w$ of a curve, $\mathrm{Frob}_w$ denotes this geometric Frobenius, normalized as the inverse of $x\mapsto x^q$.
:::

::: {.front card-id="card-b4b61ca1d1381eb5" tags="definition"}
What is the definition of Hilbert class field?
:::

::: {.back card-id="card-b4b61ca1d1381eb5"}
The Hilbert class field $H$ of a number field $K$ is the maximal abelian extension of $K$ that is unramified at all finite primes. Its Galois group is canonically isomorphic to the ideal class group $\mathrm{Cl}(K)$, so $[H:K]=h_K$.
:::

::: {.front card-id="card-3612cc90f4815c4b" tags="definition"}
What is the definition of Jacobian variety?
:::

::: {.back card-id="card-3612cc90f4815c4b"}
The Jacobian $\mathrm{Jac}(X)$ of a smooth projective curve $X$ is the abelian variety whose points over a field $k$ are the degree-zero divisors on $X$ modulo principal divisors. Its dimension is the genus $g$ of $X$, and $\mathrm{Jac}(X)(\mathbb{F}_q)$ is the degree-zero divisor class group.
:::

::: {.front card-id="card-8626a74576d0a13a" tags="definition"}
What is the definition of L-adic representation?
:::

::: {.back card-id="card-8626a74576d0a13a"}
An $\ell$-adic representation of a Galois group $G_K$ is a continuous homomorphism $\rho:G_K\to\mathrm{GL}_n(\mathbb{Q}_\ell)$ (or $\mathrm{GL}_n(E_\lambda)$ for a finite extension $E_\lambda/\mathbb{Q}_\ell$), equivalently a finite-dimensional $\mathbb{Q}_\ell$-vector space with a continuous $G_K$-action.
:::

::: {.front card-id="card-c94b06514997fb8a" tags="definition"}
What is the definition of Langlands program?
:::

::: {.back card-id="card-c94b06514997fb8a"}
The Langlands program is a set of conjectures relating Galois representations (or motives) to automorphic representations of reductive groups, and matching their $L$-functions. It generalizes class field theory, which is the abelian case.
:::

::: {.front card-id="card-e00493795c1a16cc" tags="definition"}
What is the definition of Maximal order?
:::

::: {.back card-id="card-e00493795c1a16cc"}
An order in a finite-dimensional algebra $A$ over $\mathbb{Q}$ (or over a Dedekind domain) is a subring that is a finitely generated projective module of full rank; it is maximal if it is maximal with respect to inclusion among orders. For a number field $K$, the unique maximal order is the ring of integers $\mathcal{O}_K$.
:::

::: {.front card-id="card-03a196f43d5f49b0" tags="definition"}
What is the definition of R-adic expansion?
:::

::: {.back card-id="card-03a196f43d5f49b0"}
For an integer $r\ge2$, the $r$-adic expansion of $x\in\mathbb{Z}_p$ (when $r$ is a power of $p$) is $x=\sum_{i\ge0}a_i r^i$ with digits $0\le a_i<r$. The $a_i$ are the $r$-adic digits; for $r=p$ this is the usual $p$-adic expansion.
:::

::: {.front card-id="card-6ba0dca2b7c27ecd" tags="definition"}
What is the definition of Rigid analytic geometry?
:::

::: {.back card-id="card-6ba0dca2b7c27ecd"}
Rigid analytic geometry is Tate's theory of analytic spaces over a nonarchimedean field, built from affinoid algebras (quotients of Tate algebras) and admissible open coverings. It provides a nonarchimedean analogue of complex analytic geometry and is used to uniformize Drinfeld moduli spaces.
:::

::: {.front card-id="card-4972336cd57309b4" tags="definition" cite="[@Dri87; @Gos98, Example 6.2.13 and Remarks 6.2.14]"}
What is the definition of Shtuka?
:::

::: {.back card-id="card-4972336cd57309b4"}
A (right) shtuka of rank $d$ over a field $L$, on a smooth projective curve $X$ over $\mathbb{F}_r$, is a diagram of locally free rank-$d$ sheaves on $X_L$: injections $\beta:\mathcal{F}_0\to\mathcal{F}_1$ and $\alpha:\tilde\sigma^*\mathcal{F}_0\to\mathcal{F}_1$, where $\tilde\sigma$ is the Frobenius on $X_L$, such that both cokernels have length 1. The support of $\operatorname{coker}\alpha$ is the *pole*, the support of $\operatorname{coker}\beta$ the *zero*. A rank-$d$ Drinfeld module gives a shtuka; shtukas are the function-field objects used to realize Galois representations.
:::

::: {.front card-id="card-6aa5244a68396c66" tags="definition" cite="[@And86; @Gos98, Definition 5.4.5]"}
What is the definition of T-module?
:::

::: {.back card-id="card-6aa5244a68396c66"}
A $T$-module (in the sense of Anderson) over a field $k$ is a pair $(E,\phi)$ consisting of a vector group $E\cong\mathbb{G}_a^d$ and an $\mathbb{F}_q$-linear ring homomorphism $\phi:\mathbb{F}_q[T]\to\operatorname{End}(E)$ such that $d\phi(T)-\theta$ is nilpotent on $\operatorname{Lie}(E)$, where $\theta\in k$ is the image of $T$. Drinfeld modules are the dimension-one case ($d=1$), of arbitrary rank; $T$-modules are function-field analogues of abelian varieties.
:::

::: {.front card-id="card-2e6db27fb7b674d9" tags="definition"}
What is the definition of Tate module?
:::

::: {.back card-id="card-2e6db27fb7b674d9"}
For an abelian group or abelian variety $A$ and a prime $\ell$, the $\ell$-adic Tate module is $T_\ell(A)=\varprojlim_n A[\ell^n]$, the inverse limit of $\ell^n$-torsion subgroups. If $A$ is an abelian variety of dimension $g$ over a field of characteristic $\neq\ell$, then $T_\ell(A)\cong\mathbb{Z}_\ell^{2g}$ as a $\mathbb{Z}_\ell$-module.
:::

::: {.front card-id="card-73127fa341e1af1f" tags="definition"}
What is the definition of Uniformization?
:::

::: {.back card-id="card-73127fa341e1af1f"}
Uniformization is the representation of an analytic or algebraic object as a quotient of a simpler space by a discrete group action, e.g. $\mathbb{C}/\Lambda$ for a complex elliptic curve, or the Drinfeld upper half-plane modulo a lattice for Drinfeld modules.
:::
