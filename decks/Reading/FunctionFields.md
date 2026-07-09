---
title: "Reading::FunctionFields"
---

- Essential feature of Wiles FLT: arithmetic cohomology.

    - Put a topology on the algebra of functions, vs the discete set of solutions over $ { \mathbf{F} }_q $.

- $ e_C(\ell z) = C_\ell(e_C(z)) $ where $ C_\ell $ is an additive polynomial: analog of $ e^{\ell z} = (e^z)^\ell $.

    - The map $ \ell \mapsto C_\ell(z) $ is the Carlitz module.
    - Yields a theory of $ n! $ (i.e. $ \Gamma(n) $) and Bernoulli functions.
    - "Division values" of $ e_C(z) $ generate abelian cyclotomic extensions of $ {\mathbf{Q}} $, analogous to division values of $ e^{2\pi i z} $.
    - Has "rank" 1.

- Drinfeld generalizes in 74: general exponentials of higher rank, for arbitrary function fields and choices of infinite places.

    - The Carlitz module is the simplest Drinfeld modules.
    - Constructs a moduli of such modules
    - Uiformize the moduli using Tate's rigid analytic geometry.
    - His goal: prove Langlands-esque reciprocity laws.
    - Yields class fields.
    - Generalize elliptic curves and higher so-called $ T{\hbox{-}} $modules which generalize abelian varieties.
    - Generlize *to* shtukas: Drinfeld modules with a vector bundle.

- Toward analogs of $ L{\hbox{-}} $functions for abelian varieties and analogs of RH for them: fix $ K $ a function field,

    - $ A \coloneqq $ functions in $ K $ which are regular away from $ \infty $, generalizes $ { \mathbf{F} }_q[T] $, is a Dedekind domain with finite unit group and class number.
    - Given a Drinfeld module $ \psi $ over a field $ L $, this gives $ L $ a new $ A{\hbox{-}} $module structure. Use this to define an analog of the Tate module of $ \psi $.
    - The charpoly of $ \operatorname{Frob}_L $ has coefficients in $ A $ (instead of $ {\mathbf{Z}} $), assemble these into an Euler product and thus an $ L{\hbox{-}} $function.

- Three themes:

    - Function fields are "bigger" than number fields: over $ {\mathbf{Q}} $, analytically complete and then take a degree 2 field extension to close algebraically to get $ {\mathbf{C}} $, but for function fields, completing yields a local field which may have infinitely many extensions of a fixed degree. Things identified in the number field case split up in the function field case.
    - Arithmetic/geometric dichotomy: function fields have two types of cylcotomic extensions, adjoining $ \zeta_n $ (everywhere unramified, related to extensions of constant field) or ramified "geometric" extensions (by division values of Drinfeld modules).
    - Two $ T $'s, as an operator (gives rise to $ L{\hbox{-}} $functions and a scalar (gives rise to $ \Gamma{\hbox{-}} $functions).

- Main fetures of Drinfeld modules:

    - The lattice $ { \mathbf{F} }_q[T]\xi $
    - Its exponential, similar to $ e_C(x) $
    - The multiplication formula for $ e_C(x) $, similar to the Carlitz module $ C $
    - Algebraicty of $ C $ and reduction to "finite fields"
    - The action of $ { \mathbf{F} }_q[t] $ on rational points via $ C $.

- Notation:

    - $ X $ smooth projective geometrically connected curve over $ { \mathbf{F} }_r $ where $ r = p^{m_0} $.
    - $ \infty\in X $ a fixed closed point of degree $ d_\infty $ over $ { \mathbf{F} }_q $.
    - $ k $ is the function field of $ X $
    - $ A \subset k $ the functions regular away from $ \infty $
    - $ v_\infty $ the valuation at $ \infty $
    - $ K \coloneqq k_\infty $ its completion at $ \infty $.
    - $ C_\infty $ the completion of $  \operatorname{cl}^{\mathrm{alg}}K $ (algebraically closed)
    - $ \deg D $ for $ D\in \operatorname{Div}(X) $ is the degree of $ D $ over $ { \mathbf{F} }_r $.
    - $ d_\infty = \deg \infty $.
    - For $ x\in K $, $ \deg(x) \coloneqq-d_\infty v_\infty(x) $ so $ \deg(a) = \log_r({\sharp}{\mathbf{A}}/a) $ for $ a\in A\setminus\left\{{0}\right\} $ (the degree of the finite part of the divisor of $ a $)
    - $ {\left\lvert {x} \right\rvert}_\infty \coloneqq r^{\deg x} $the normalized absolute value, extended to $ C_\infty $.
    - $ Jac_X({ \mathbf{F} }_q) $ the (finite) group of degree zero divisors on $ X $, mod divisors of elements of $ k^{\times} $.
    - $ h(k) = {\sharp}\operatorname{Jac}_X({ \mathbf{F} }_q) $ the "class number" of $ k $. $ h(A) $ is the class number of $ A $ as a Dedekind domain.

- Facts:

    - $ A $ is Dedekind at $ \operatorname{Spec}A = X\setminus\left\{{ \infty }\right\} $
    - $ A^{\times}= { \mathbf{F} }_q^{\times} $ since every nonconstant $ a\in A $ needs zeros to balance out the pole at $ \infty $ since $ \deg a = 0 $ for any principal divisor $ a $.

- Prop 4.1.1: for $ I \subseteq k $ a nontrivial $ A{\hbox{-}} $fractonal ideal, $ I\subset K $ is discrete and cocompact.

    - Discreteness: $ \exists a\in k^{\times} $ st $ aI \subseteq A $.
    - Compactness of $ K/I $: Riemann-Roch

- Analogies:

    - $ {\mathbf{Z}}\leadsto A $
    - $ {\mathbf{Q}}\leadsto k $
    - $ {\mathbf{R}}\leadsto K $\

- Motto: function field theory decomposes classifical number-theoretic objects into arithmetic components.

    - Example: will need many Hilber class fields to play the role of $ {\mathbf{Q}} $,

- Definition 4.2.1 ($ M{\hbox{-}} $lattices)

    *(Answer was a figure; image not recovered.)*

- Prop 4.2.4: $ e_L(x) $ is entire on $ C_\infty $ which has a Taylor expansion at $ x=0 $ with coefficiets in $ M $.

    - Proof: convergence is due to discreteness of $L, the Taylor expansion is from $ G_M \coloneqq{ \mathsf{Gal}}(M^{ {}^{ \operatorname{sep} } }/M $) which fixes $ L $ and the natura of the continuous action $ G_M\curvearrowright M^{ {}^{ \operatorname{sep} } } $. d it $ e_L $ is a non-constant entire function and thus surjective.

- Thm 4.3.1 (fundamental)

    $$e_L(ax) = ae_L(x)\cdot \prod_{a\in (a^{-1}L/L)\setminus\left\{{0}\right\}} \qty{1 - {e_L(x)\over e_L(a)}}$$

    - Proof: short.

- Prop 4.3.2: define

    $$\begin{align} A &\to M\left\{{\tau}\right\} \\ a&\mapsto \phi_a\end{align}$$

    satisfies:

    - $ { \mathbf{F} }_r{\hbox{-}} $linear,
    - $ a\in { \mathbf{F} }_r \subset A\implies \phi_a = a \tau^0 $,
    - $ \phi_{ab}(\tau) = \phi_a(\tau)\phi_b(\tau) = \phi_b(\tau)\phi_a(\tau) = \phi_{ba}(\tau) $.

- Definition 4.3.3: the Drinfeld module of $ L $ is the injection

    $$\begin{align} A &\to M\left\{{\tau}\right\} \\ a&\mapsto \phi_a\end{align}$$

    which has rank $ d = \operatorname{rank}_A(L) $.

- Def 4.4.1: an $ A{\hbox{-}} $field $ F $ is a field with a morphim $ i:A\to F $; $ \ker i ={\mathfrak{p}} $ is prime and $ \operatorname{ch}F \coloneqq{\mathfrak{p}} $; $ F $ has "generic characteristic" (char zero) if $ {\mathfrak{p}}= \left\langle{0}\right\rangle $, otherwise $ F $ has finite characteristic.

    - Agrees with definition for $ A = { \mathbf{F} }_r[T] $.

- There is a theory of morphisms of Drinfeld modules, parallels elliptic curves

    - isomorphism iff degree zero,
    - if $ G/F $ is any algebraically closed extension then $ \hom_{\overline{F}}(\psi,\psi) \hookrightarrow\mathop{\mathrm{Hom}}_G(\phi, \psi) $,
    - $ { \operatorname{End} }_F(\psi) $ is commutative and torsionfree projective $ A{\hbox{-}} $module of rank $ \leq d^2 $
    - Characterization of when certain group schemes are kernels of isogenies

- Let $ E/k \subseteq C_\infty $ be a finite extension, then $ E $ is a $ {\mathrm{CM}}_\infty{\hbox{-}} $field iff it contains exactly one prime above $ \infty $.

    - Can constructed Drinfeld modules with CM by the maximal order $ {\mathcal{O}}\coloneqq A_E $, the $ A{\hbox{-}} $integers in $ E $ where $ {\mathcal{O}}\hookrightarrow{ \operatorname{End} }(\psi) $
    - For $ L\subset C_\infty $ a lattice for $ {\mathcal{O}} $ of rank $ d_1 $, it induces an $ A{\hbox{-}} $lattice of rank $ d\coloneqq d_1\cdot [E:k] $ which induces a Drinfeld module $ \psi $; say $ \psi $ has sufficiently many CMs iff $ d_1 = 1 $ iff $ L\cong I $ where $ I $ is an $ {\mathcal{O}}{\hbox{-}} $ideal.
    - Can define conductors: letting $ \tilde {\mathcal{O}} $ be the maximal order (the $ A{\hbox{-}} $integers), the conductor is the largest ideal $ \mathfrak c{~\trianglelefteq~}\tilde {\mathcal{O}} $ which is also an ideal in $ {\mathcal{O}} $.

- For $ X\in {\mathsf{Sch}} $, define an Euler product

    $$\zeta_X(s) \coloneqq\prod_{x\in {\left\lvert {X} \right\rvert}} {1\over 1 - {\left\lVert {x} \right\rVert}^{-s} },\qquad {\left\lVert {x} \right\rVert} \coloneqq{\sharp}\kappa(x) \coloneqq{\sharp}({\mathcal{O}}_{X, x}/{\mathfrak{m}}_x)$$

    - Can expand in a sum

    $$\zeta_X(s) = \sum_{D\in \operatorname{Div}_{>0}(X)} {1\over {\left\lVert {D} \right\rVert}^{-s} },\qquad {\left\lVert {D} \right\rVert} \coloneqq r^{\deg D}$$

    where $ \operatorname{Div}_{>0}(X) $ are positive divisors.

- Set$ u\coloneqq r^{-s} $ to define $ Z_X(u) \coloneqq\zeta_X(s) $ and

    $$Z_X(u) = {P_X(u) \over (1-u)(1-ru)}, \qquad \deg P_X(u) = 2g(X)$$

    where $ P_X(1) = h(k) $ is the class number of the field $ k $.

    - Satsifies a functional equation

    $$P_X(u) = r^g u^{2g} P_X\qty{1\over ru}$$

    , and setting $ \xi_X(s) = r^{s(g-1)} Z_X(s) $ one has

    $$\xi_X(s) = \xi_X(1-s)$$

- $ L{\hbox{-}} $series: $ X $ a curve over $ { \mathbf{F} }_r $ where $ r= p^{m_0} $, fixed closed point $ \infty $, function field $ k $ with completion $ K $ at $ \infty $, $ \operatorname{Spec}A = X\setminus\left\{{ \infty }\right\} $, $ C_\infty = $ complete $ k $, take algebraic closure, take completion. $ G = { \mathsf{Gal}}(k{ {}^{ \operatorname{sep} } }/k) $, $ \ell\neq p\in {\mathbf{Z}} $ a prime, $ \rho: G\to \operatorname{GL}(V) $ a continuous finite dimensional $ \ell{\hbox{-}} $adic representation.

    - E.g. for $ Z $ an abelian variety over $ k, $ define $ \ell{\hbox{-}} $adic Tate module $ T_\ell(Z) $ and set

    $$V \coloneqq\mathop{\mathrm{Hom}}_{{ {\mathbf{Z}}_{\widehat{\ell}} }}(T_\ell(Z), { {\mathbf{Q}}_\ell }) \cong H^1_\text{ét}(Z; { {\mathbf{Q}}_\ell }) \in   {}_{G}{\mathsf{Mod}}$$

    - For $ w\in {\left\lvert {X} \right\rvert} $, define

    $$f_w(u) \coloneqq f_{\overline{w}}(u) \coloneqq\operatorname{det}\qty{1 - \operatorname{Frob}_{\overline{w}}u {~\mathrel{\Big\vert}~}V^{I_{\overline{w}}}}$$

    where $ \overline{w} $ is an point over $ w $ in $ { \overline{k} } $ and $ I_{\overline{w}} $ is its inertia group and $ V^{I_{\overline{w}}} $ is the fixed subspaces with $ \operatorname{Frob}_{\overline{w}}(u) \in D_{\overline{w}}/I_{\overline{w}} $ the geometric Frobenius (inverse of usual).

    - Define

    $$L_V(s) \coloneqq\prod_{w\in {\left\lvert {X} \right\rvert}} f_w({\left\lVert {w} \right\rVert}^{-s})^{-1},\qquad {\left\lVert {w} \right\rVert} \coloneqq{\sharp}\kappa(w)$$

- Thm 8.18.8 (Yu): let $ A = { \mathbf{F} }_r[T] $ and $ \zeta_A(s) $ be its zeta function, then $ \zeta_A(i) $ is transcendental over $ k $ for all positive $ i $. If $ i $ is not divisible by $ r-1 $, then $ \zeta_A(i)/{\varepsilon}^i $ is transcendental over $ k $.

    - Here $ \zeta_A(s) = \sum_{I\subseteq A} I^{-s} $.

- Recalling classical RH: define

    $$\xi(s) \coloneqq\zeta_\infty(s)\cdot \zeta(s), \qquad \zeta_\infty(s) \coloneqq\Gamma\qty{s\over 2} \pi^{-{s\over 2}}$$

    and

    $$\widehat{\xi}(s) \coloneqq s(1-s)\xi(s)$$

    to get an entire function with $ \widehat{\xi}(s) = \widehat{\xi}(1-s) $.

    - RH: the zeroes of $ \widehat{\xi} $ are of the form $ {1\over 2} + i\beta $ for $ \beta\in {\mathbf{R}} $; can shift and rotate to get a function $ \theta(u) $ and equivalently ask that the zeros of $ \theta $ are real.
    - Relate to a theorem of Wan 8.24.5: Let $ y\in { {\mathbf{Z}}_{\widehat{p}} } $ where each $ r{\hbox{-}} $adic digit of $ -y $ is less than $ p $ or equal to $ r-1 $. Then the zeros of $ \zeta_A(x, y) $ are in $ K $ and simple.
    - $ {\mathbf{R}} $ is a "small" local field and the zeros of $ \theta(u) $ are either in $ {\mathbf{R}} $ or $ {\mathbf{C}} $, a degree 2 extension. Compare to zeros of $ \zeta_A(s) $ which could be in an extension of $ K $ of arbitrary (even infinite) degree but are in $ K $ itself.
