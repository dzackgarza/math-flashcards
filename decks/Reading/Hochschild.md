---
title: "Reading::Hochschild"
---

- What is a dga?

    $ C $ a dg $   {}_{k}{\mathsf{Mod}} $ where for $ x \in C_i, y\in C_j $,

    $$d(xy) = d(x)y + (-1)^i x d(y)$$

- What is a dgla?

    $ C $ a dg $ {\mathsf{Lie}{\hbox{-}} \mathsf{Alg}} $ where for $ x\in C_i, y\in C_j $,

    $$d([xy]) = [d(x) y] + (-1)^i[x d(y)]$$

- What is a counital dg coalgebra?

    $ C $ a graded coalgebra, so $ \exists \Delta: C\to C\otimes_k C $ coassociative $ (\Delta\otimes 1)\Delta = (1\otimes\Delta)\Delta $ with

    $$(d\otimes 1 + 1\otimes d)\Delta = \Delta d$$

    Counital if $ \exists {\varepsilon}: C\to k $ with

    $$({\varepsilon}\otimes 1)\Delta = 1 = (1\otimes{\varepsilon})\Delta$$

- What is a formula for the pushout of module morphisms $ \alpha: Y\to A $ and $ \beta: Y\to B $?

    A quotient module:

    $$A\oplus B\twoheadrightarrow A{ \amalg_{Y} } B \cong { X\oplus B  \over  \left\langle{ (\,-\alpha(y)\,, \beta(y)\, ) {~\mathrel{\Big\vert}~}y\in Y}\right\rangle }$$

- What is a formula for the pullback of module morphisms $ \phi: A\to X $ and $ \psi: B\to X $?

    A submodule:

    $$A \underset{\scriptscriptstyle {X} }{\times} B = \left\langle{(a,b) \in A\oplus B {~\mathrel{\Big\vert}~}\phi(a) = \psi(b)}\right\rangle \subseteq A\oplus B$$

- Describe limits and colimits in terms of quotients and submodules.

    Colimits $ \sim $ quotients, e.g. pushouts (glue by equivalence)

    Limits $ \sim $ submodules, e.g. pullbacks (impose equality)

- What is a (left) hereditary ring? Give an example.

    Every (left) ideal is projective as a submodule, or $ \mathrm{gldim}_{\mathrm{left}} R \leq 1 $.

    $ k[x] $ is hereditary, since $ \mathrm{gldim}_{\mathrm{left}} k[x_1, \cdots, x_{n}]= n $ by the Hilbert syzygy theorem.

- What is the left global dimenson of a ring?

    $$\mathrm{gldim}_{\mathrm{left}} R \coloneqq\sup_{M\in   {}_{R}{\mathsf{Mod}}} \mathrm{projdim}_R M$$

    where the projective dimension is the smallest length of a projective resolution.

- What is the variance/contravariance of homs?

    $ [P_1\to P_0, N] = [P_0, N] \to [P_1, N] $, so $ \mathop{\mathrm{Hom}}({-}, N) $ is contravariant (like a dual module $ V {}^{ \vee } $)

    $ [M, I_1\to I_0] = [M, I_0]\to [M, I_1] $, so $ \mathop{\mathrm{Hom}}(M, {-}) $ is covariant.

- How do you compute $ \operatorname{Ext}_R^*(M, N) $?

    $ H_*(\mathop{\mathrm{Hom}}_R(P_M, N)) $ where $ P_M\rightrightarrows M $ is a projective resolution.

    $ H_*(\mathop{\mathrm{Hom}}_R(M, I_N)) $ where $ N\hookrightarrow I_N $ is an injective resolution.

- How do you compute $ \operatorname{Tor}^R_*(M, N) $?

    $ H_*(M\otimes_R P_N) $ where $ P_N\rightrightarrows N $ is a projective resolution.

- What is the Kunneth theorem?

    Theorem A.5.2 (Knneth Theorem). Let $ C $. and $ D $. be complexes of right and left $ R $-modules, respectively, for which $ C_n $ and $ d\left(C_n\right) $ are flat $ R $-modules for all $ n \in \mathbb{Z} $. Then for all $ n \in \mathbb{Z} $, there is a short exact sequence:

    $$\begin{aligned} 0 \longrightarrow \bigoplus_{i+j=n} \mathrm{H}_i(C) \otimes_R \mathrm{H}_j(D) \longrightarrow & \mathrm{H}_n\left(C \otimes_R D\right) \longrightarrow \\ & \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R\left(\mathrm{H}_i(C), \mathrm{H}_j(D)\right) \longrightarrow 0 \end{aligned}$$

- What is the UCT?

    Theorem A.5.4 (Universal Coefficients Theorem). Let $ C $ be a complex of right $ R $-modules in which all $ C_n, d\left(C_n\right) $ are flat, and let $ M $ be a left $ R $ module. There is a short exact sequence

    $$0 \longrightarrow \mathrm{H}_n(C) \otimes_R M \longrightarrow \mathrm{H}_n\left(C \otimes_R M\right) \longrightarrow \operatorname{Tor}_1^R\left(\mathrm{H}_{n-1}(C), M\right) \longrightarrow 0 .$$

- What is the enveloping algebra $ A^e $ of $ A\in {}_{k} \mathsf{Alg} $?

    $ A\otimes_k A^{^{\operatorname{op}}} $ where $ (a_1\otimes b_1)\cdot (a_2\otimes b_2) = (a_1a_2)\otimes(b_2b_1) $.

- How are enveloping algebras related to bimodules?

    $ ({A}, {A}){\hbox{-}}\mathsf{biMod}  { \, \xrightarrow{\sim}\, }  {}_{A^e}{\mathsf{Mod}} $ where if $ M\in ({A}, {A}){\hbox{-}}\mathsf{biMod} $ is sent to $ M $ with $ (a\otimes b).m = amb $.

- What is the $ {}_{A^e}{\mathsf{Mod}} $ structure on $ A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} } } $?

    Act on the first and last components:

    $$(a \otimes b) \cdot\left(c_1 \otimes c_2 \otimes \cdots \otimes c_{n-1} \otimes c_n\right)=a c_1 \otimes c_2 \otimes \cdots \otimes c_{n-1} \otimes c_n b$$

- How is the bar complex of $ A\in {}_{A^e}{\mathsf{Mod}} $ defined?

    $ B(A): A^{\otimes\bullet}  \xrightarrow[]{\pi} { \mathrel{\mkern-16mu}\rightarrow }\,  A $ where $ \pi(a\otimes b) = ab $, $ d_1(a\otimes b\otimes c) = ab\otimes c - a\otimes bc $ and the general differential is a sum over collapses:

    $$d_n\left(a_0 \otimes a_1 \otimes \cdots \otimes a_{n+1}\right)=\sum_{i=0}^n(-1)^i a_0 \otimes a_1 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_{n+1}$$

    If $ A\in   {}_{k}{\mathsf{Mod}}^{\mathrm{free}} $ then $ B(A) $ is an exact free resolution of $ A $ with $ H^*(B(A)) = A \cdot t^0 $.

- How are Hochschild chains and homology defined?

    For $ M\in   {}_{A^e}{\mathsf{Mod}} $, write

    $$C_*(A; M) = \bigoplus_{n\geq 0} M\otimes_{A^e} B_n(A) \cong \bigoplus_{n\geq 0} M\otimes_k A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  }$$

    I.e. apply $ {-}\otimes_{A^e} M $ to $ B(A) $ levelwise, with differential $ \operatorname{id}_M \otimes d_n $.

    Then $ {\operatorname{HH}}(A; M) = H^*(C_*(A; M)) $, i.e. $ {\operatorname{HH}}_n(A; M) = H_n(M\otimes A^{\otimes\bullet}) $.

- What are cycles? Boundaries?

    Cycles $ =\ker d_n $, boundaries $ =\operatorname{im}d_{n} $.

- How are Hochschild cochains and cohomology defined?

    Apply $   {}_{A^e}{\mathsf{Mod}}({-}, M) $ to $ B(A) $, has differentials $ d_n^*(f) \coloneqq fd_n $ for $ f\in   {}_{A^e}{\mathsf{Mod}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{n+1} }  }\to M ) $, $ {\operatorname{HH}}^*(A; M) $ is its homology.

- How is $ {\operatorname{HH}}_*(A) $ defined?

    Regard $ A\in  {}_{A^e}{\mathsf{Mod}} $ and take $ {\operatorname{HH}}_*(A; A) $.

- Discuss functoriality of $ {\operatorname{HH}}^*({-}) $.

    Not a functor! Instead $ (A, M)\mapsto {\operatorname{HH}}^*(A, M) $ defines a bifunctor equivalent to $  \operatorname{Ext}_{A^e}^*({-}, {-}) $ which is contravariant in $ A $ and covariant in $ M $.

- How are $ {\operatorname{HH}}_* $ and $ {\operatorname{HH}}^* $ related to ext and tor?

    $ \operatorname{HH}_n(A, M) \cong \operatorname{Tor}_n^{A^e}(M, A) \text { and } \operatorname{HH}^n(A, M) \cong \operatorname{Ext}_{A^e}^n(A, M) $

    First iso holds when $ A\in  {}_{k}{\mathsf{Mod}}^\flat $ and second when $ A\in   {}_{k}{\mathsf{Mod}}^{\mathop{\mathrm{proj}}} $.

- What is the reduced/normalized bar resolution?

    $ \overline{B}_n(A) = A\otimes(A/k){ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  } \otimes A $.

- What is $ {\operatorname{HH}}^*(k[x]) $?

    $ {\operatorname{HH}}^*(k[x]) = k[x] t^0 \oplus k[x] t^1 $, using the resolution $ 0\to R{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  }\xrightarrow{\otimes 1 - 1\otimes x} R{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  } \xrightarrow{\pi} R\to 0 $ where $ R\coloneqq k[x] $ and applying $ \mathop{\mathrm{Hom}}_{R^e}({-}, R) $, using $ \mathop{\mathrm{Hom}}_{R^e}(R\otimes R, R) \cong R $ in this case by $ f\mapsto f(1\otimes 1) $.

    Can write as a ring:

    $${\operatorname{HH}}^*(k[x]) \cong k[x, t]/\left\langle{t^2}\right\rangle,\qquad {\left\lvert {x} \right\rvert} = 0, {\left\lvert {t} \right\rvert} = 1$$

- What is $ {\operatorname{HH}}(k[x]/x^n) $?

    See example 1.1.21: set $ A\coloneqq k[x]/x^n $. One gets $ {\operatorname{HH}}^*(A) \cong \bigoplus_{i\geq 0} A t^i $ if $ \operatorname{ch}k \mathrel{\Big|}n $, otherwise

    $${\mathbb{H}}^*(A) = At^0 + \bigoplus_{m\geq 0} \left\langle{x}\right\rangle t^{2m + 1} + \bigoplus_{m\geq 0} A/\left\langle{ x^{n-1} }\right\rangle t^{2m}$$

- What are the interpretations of $ {\operatorname{HH}}^n(A) $ for small $ n $?

    $ n=0 $: $ Z(A) $

    $ n=1 $: $ \mathop{\mathrm{Out}}\mathop{\mathrm{Der}}_k(A) $, which equals $ \mathop{\mathrm{Der}}_k(A) $ when $ A $ is commutative since the only inner derivation is zero.

    $ n=2 $: Infinitesimal deformations of $ A $

    $ n=3 $: obstructions to lifting deformations to formal deformations.

- What are the interpretations of $ {\operatorname{HH}}^n(A; M) $ for small $ n $?

    $ n=0 $: $ Z_M(A) \coloneqq\left\{{m\in M{~\mathrel{\Big\vert}~}am=ma \, \forall a\in A}\right\} $.

    $ n=1 $: $ \mathop{\mathrm{Out}}\mathop{\mathrm{Der}}_k(A\to M) \coloneqq\mathop{\mathrm{Der}}_k(A\to M)/\mathop{\mathrm{Inn}}\mathop{\mathrm{Der}}_k(A\to M) $.

    $ n=2 $: Infinitesimal deformations of $ A $

    $ n=3 $: obstructions to lifting deformations to formal deformations.

- What is a Hochschild 2-cocycle? 2-coboundary?

    Functions $ f\in \mathop{\mathrm{Hom}}_{A^e}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  } \to M) $ which satisfy

    $$a f(b \otimes c)+f(a \otimes b c)=f(a b \otimes c)+f(a \otimes b) c$$

    These define $ { {}_{A}  \mathsf{Alg}} $ structures on $ A\oplus M $, i.e. square-zero extensions.

    Coboundaries are deformations isomorphic to the original algebra.

- What are orthogonal central idempotents?

    Each $ e_j\in Z(A) $ and $ e_j e_\ell = \delta_{j, \ell} e_j $.

- What is the cup product on $ {\operatorname{HH}}^* $?

    $$\begin{align} \smile: \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m} }  }\to A) \otimes_k \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m} }  }\to A) &\to \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m+n} }  }\to A) \\ (f \smile g)\left(a_1 \otimes \cdots \otimes a_{m+n}\right)&=(-1)^{m n} f\left(a_1 \otimes \cdots \otimes a_m\right) g\left(a_{m+1} \otimes \cdots \otimes a_{m+n}\right)\end{align}$$

    This makes $ C^*(A, A) $ into a dga.

- What is a consequence of $ {\operatorname{HH}}^1(A; M) = 0 $?

    Every derivation $ A\to M $ is inner.

- How do deformations of $ A $ arise?

    From noncommutative Poisson structures: elements $ x\in {\operatorname{HH}}^2(A) $ with $ \left\{{a, a}\right\} = 0 $.

- What is the circle product?

    $$\begin{aligned}& (f \circ g)\left(a_1 \otimes \cdots \otimes a_{m+n-1}\right) \\ & =\sum_{i=1}^m(-1)^u f\left(a_1 \otimes \cdots \otimes a_{i-1} \otimes g\left(a_i \otimes \cdots \otimes a_{i+n-1}\right) \otimes a_{i+n} \otimes \cdots \otimes a_{m+n-1}\right) \end{aligned}$$

- How is the Gerstenhaber bracket defined?

    $$\begin{align} [{-}, {-}]: \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m} }  } \to A) \otimes_k \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  } \to A) &\to \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m+n-1} }  }\to A) \\ [f, g]& =f \circ g-(-1)^{(m-1)(n-1)} g \circ f\end{align}$$

- What is a Gerstenhaber algebra?

    Definition 1.4.8. A Gerstenhaber algebra $ (H, \smile,[] $,$ ) is a free \mathbb{Z} $-graded $ k $-module $ H $ for which $ (H, \smile) $ is a graded commutative associative algebra, $ (H,[] $,$ ) is a graded Lie algebra with bracket [ $,$ ] of degree -1 $ and corresponding degree shift by $ -1 $ on elements, and

    $$[\gamma, \alpha \smile \beta]=[\gamma, \alpha] \smile \beta+(-1)^{|\alpha|(|\gamma|-1)} \alpha \smile[\gamma, \beta]$$

    for all homogeneous $ \alpha, \beta, \gamma $ in $ H $.

- What is the cap product?

    $$\begin{align} \frown: \mathrm{HH}_n(A) \otimes \mathrm{HH}^m(A) &\longrightarrow\mathrm{HH}_{n-m}(A) \\ \left(a_0 \otimes a_1 \otimes \cdots \otimes a_n\right) \frown f&=(-1)^{m(n-m)} a_0 f\left(a_1 \otimes \cdots \otimes a_m\right) \otimes a_{m+1} \otimes \cdots \otimes a_n\end{align}$$

- What is a $ (p, q) $ shuffle?

    For nonnegative integers $ p $ and $ q $, a $ (p, q) $-shuffle is an element $ \sigma $ of the symmetric group $ S_{p+q} $ for which $ \sigma(i)<\sigma(j) $ whenever $ 1 \leq i<j \leq p $ or $ p+1 \leq i<j \leq p+q $.

    Let $ S_{p, q} $ denote the subset of $ S_{p+q} $ consisting of all $ (p, q) $-shuffles.

- What is the shuffle product?

    Makes $ {\operatorname{HH}}_*(A) $ a graded commutative $  {}_{k}  \mathsf{Alg} $,

    $$\begin{aligned}

    & \left(a*0 \otimes a*1 \otimes \cdots \otimes a*p\right) \cdot\left(a*0^{\prime} \otimes a*{p+1} \otimes \cdots \otimes a*{p+q}\right) \

    & =\sum*{\sigma \in S*{p, q}}(\operatorname{sgn} \sigma) a*0 a*0^{\prime} \otimes a*{\sigma^{-1}(1)} \otimes \cdots \otimes a*{\sigma^{-1}(p+q)}

    \end{aligned}$$

- What is a map $ f: V\to W $ of graded vector spaces?

    $ \exists m $ such that $ f(V_n) \subseteq V_{n+m} $ for all $ n $; say $ {\left\lvert {f} \right\rvert} = m $ is its degree.

- For $ V, W $ graded vector spaces and $ f:V\to V', g:W\to W' $, what is $ f\otimes g $?

    $ v\otimes w\mapsto (-1)^{{\left\lvert {g} \right\rvert}{\left\lvert {v} \right\rvert}} f(v)\otimes g(w) \in V'\otimes W' $.

- What is the Yoneda splice of $ f\in {\operatorname{HH}}^n(A) $ and $ g\in {\operatorname{HH}}^m(A) $?

    *(Answer was a figure; image not recovered.)*

- What is the "base ring" action on Ext?

    $ {\operatorname{HH}}^*(A) \curvearrowright \operatorname{Ext}_A^*(M, N) $ for any $ M, N \in   {}_{A}{\mathsf{Mod}} $, making it a graded $ {\operatorname{HH}}^*(A){\hbox{-}} $module.

- What is the graded center of a graded algebra?

    $ Z_{\mathsf{gr}\,}(B) = \left\{{a\in B^ { \mathrm{homog} }{~\mathrel{\Big\vert}~}ab = (-1)^{{\left\lvert {a} \right\rvert}{\left\lvert {b} \right\rvert}} ba \,\,\forall b\in B^ { \mathrm{homog} }}\right\} $.

- Why is the graded center important?

    The map

    $${\operatorname{HH}}^*(A) \to  \operatorname{Ext}_A^*(M, M)$$

    where $ f\mapsto f\otimes\operatorname{id}_M $ is a ring morphism with image contained in $ Z_{\mathsf{gr}\,}( \operatorname{Ext}_A^*(M, M)) $.

- Give a free resolution of $ k\in {}_{A}{\mathsf{Mod}} $ using $ {\varepsilon}: A\to k $ where $ A = k[x]/x^n $.

    $$\cdots \longrightarrow A \stackrel{x^{n-1}}{\longrightarrow} A \stackrel{x \cdot}{\longrightarrow} A \stackrel{x^{n-1}}{\longrightarrow} A \stackrel{x \cdot}{\longrightarrow} A \stackrel{\varepsilon}{\longrightarrow} k \longrightarrow 0 .$$

- What is $ \operatorname{Ext}_A^*(k, k) $?

    $$ \operatorname{Ext}_A^*(k, k) = k[y]\cdot t^2 + \bigoplus_{n\neq 2} {k[y,z]\over y^2}\cdot t^n$$
