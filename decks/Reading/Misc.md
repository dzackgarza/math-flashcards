---
title: "Reading::Misc"
---

- What is an $ A{\hbox{-}} $algebra $ B $?

    A ring $ B $ equipped with a ring morphism $ A\to B $.

- What is the trace of a module?

    Realized as a morphism

    $$\operatorname{Tr}:   {}_{A}{\mathsf{Mod}}(M, M) \to A$$

    of $ A{\hbox{-}} $modules for $ M\in   {}_{A}{\mathsf{Mod}}^{\mathrm{fg}} $. For $ M\in { {}_{A}  \mathsf{Alg}} \cap  {}_{B}{\mathsf{Mod}}^{{\mathrm{fg}}, {\mathrm{free}}} $, define

    $$\operatorname{Tr}_{B/A}(b) \coloneqq\operatorname{Tr}(x\mapsto bx) \in   {}_{A}{\mathsf{Mod}}$$

    which satisfies $ \operatorname{Tr}(a) = \operatorname{rank}_A(B)\cdot a $ for $ a\in A $.

- What is a separable algebra?

    When the following natural map is an iso:

    $$\begin{align}\phi: B &\to   {}_{A}{\mathsf{Mod}}(B, A) \\ x &\mapsto \operatorname{Tr}(x\cdot)\end{align}$$

- What are the free separable $ k{\hbox{-}} $algebras $ L $ over $ k $ a field?

    $ L = \prod_{i=1}^t B_i $ where each $ B_i/k $ is a finite separable extension and $ t>0 $.

- What is a finite etale morphism $ f:Y\to X $?

    $ \exists \operatorname{Spec}A_i \rightrightarrows Y $ where each $ f^{-1}(\operatorname{Spec}A_i) = \operatorname{Spec}B_i $ is affine and $ B_i/A_i $ is a free separable $ A_i{\hbox{-}} $algebra.

    In particular, $ f $ is a finite morphism, so each $ B_i\in   {}_{A_i}{\mathsf{Mod}}^{{\mathrm{fg}}} $ which need not be free, but turns out to always be projective.

- What are the finite etale covers $ Y\to \operatorname{Spec}{\mathbf{Z}}_K $, the ring of integers of an algebraic number field $ K $?

    $ Y\to X $ where $ Y \cong {\textstyle\coprod}_{i=1}^t \operatorname{Spec}A_i $ where $ t\geq 0 $ and each $ A_i = {\mathbf{Z}}_{K_i} $ where $ K_i/K $ is a finite extension unramified at all $ {\mathfrak{p}}\in \operatorname{Spec}(A_i)\setminus\left\{{0}\right\} $.

- How is the projective limit as a set?

    $$\varprojlim S_i=\left\{\left(x_i\right)_{i \in I} \in \prod_{i \in I} S_i {~\mathrel{\Big\vert}~}f_{i j}\left(x_i\right)=x_j \text { for all } i, j \in I \text { with } i \geq j\right\} \text {. }$$

- Discuss topological properties of profinite groups.

    Always compact and totally disconnected; conversely every compact totally disconnected topological group is profinite.

- What is the profinite completion of a group?

    Take the poset $ N\geq M \iff N \subseteq M $ for $ N, M {~\trianglelefteq~}G $ of finite index and the directed system of quotients $ G/N $.

- Give examples of profinite groups.

    $ \widehat{{\mathbf{Z}}}= \varprojlim_{n>0} {\mathbf{Z}}/n{\mathbf{Z}} $ the profinite completion of $ {\mathbf{Z}} $

    $ { {\mathbf{Z}}_{\widehat{p}} }\coloneqq\varprojlim {\mathbf{Z}}/p^n{\mathbf{Z}} $ the $ p{\hbox{-}} $completion

- What is the fundamental theorem of Galois theory for schemes?

    Let $ X $ be a connected scheme. Then there exists a profinite group $ \pi $, uniquely determined up to isomorphism, such that the category $ \mathbf{F E t}_X $ of finite tale coverings of $ X $ is equivalent to the category $ \pi $-sets of finite sets on which $ \pi $ acts continuously.

- What is $ \pi_1^\text{ét}\operatorname{Spec}{\mathbf{Z}} $?

    Trivial: every finite etale cover is the free separable $ {\mathbf{Z}}{\hbox{-}} $algebra $ {\mathbf{Z}}^n $ (and there are not others).

- What is $ \pi_1^\text{ét}\operatorname{Spec}k $ for $ k={ \overline{k} } $?

    Trivial: the only covers are $ k^n $.

- What is $ \pi_1^\text{ét}\operatorname{Spec}k $ in general?

    $ { \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k) $.

- What is $ \pi_1^\text{ét}\operatorname{Spec}{ \mathbf{F} }_q $?

    $ \widehat{{\mathbf{Z}}} $

- What is $ \pi_1^\text{ét}\operatorname{Spec}{\mathbf{Z}}_K $ for $ K $ an algebraic number field?

    $ { \mathsf{Gal}}(M/K) $ where $ M $ is the maximal algebraic extension unramified over $ \operatorname{Spec}({\mathbf{Z}}_K)\setminus\left\{{0}\right\} $.

- What is $ \pi_1^\text{ét}\operatorname{Spec}{{\mathbf{Z}}_K} { \left[ { \scriptstyle \frac{1}{a} } \right] } $ for $ a\in {\mathbf{Z}}_K\setminus\left\{{0}\right\} $ for $ K $ a number field?

    $ { \mathsf{Gal}}(M_a/K) $ where $ M_a $ is the maximal extension unramified at all primes not dividing $ a $.

- What is $ \pi_1^\text{ét}\operatorname{Spec}{ {\mathbf{Z}}_{\widehat{p}} } $?

    $ \widehat{{\mathbf{Z}}} $.

- What is $ \pi_1^\text{ét}{\mathbf{P}}^1_{/ {k}} $ for $ k $ a field?

    $ \pi_1^\text{ét}\operatorname{Spec}k = { \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k) $.

- Tags:

    - /untagged

- Refs:

    - /add-references

- Links:

    - /create-links

- What is a symmetric domain?

    Let $ G $ be a semisimple group over $ \mathbb{Q} $. A subgroup $ \Gamma \subseteq G(\mathbb{Q}) $ is called congruence if there exists an embedding $ G \hookrightarrow \mathrm{GL}_n $ such that $ \Gamma $ contains

    $$\operatorname{ker}\left(\mathrm{GL}_n(\mathbb{Z}) \rightarrow \mathrm{GL}_n(\mathbb{Z} / N \mathbb{Z})\right) \cap G(\mathbb{Q})$$

    for some $ N \geqslant 1 $. Set $ X_G^{+}=X^{+}:=G(\mathbb{R})^{+} / C $. Then, a space of the form $ \Gamma^{+} \backslash X^{+} $is called a symmetric space for $ G $ (here $ \Gamma^{+}=\Gamma \cap G(\mathbb{R})^{+} $).

    This is generally an orbifold since $ \Gamma $ may contain torsion.

- What is a locally symmetric space?

    Let $ G $ be a reductive group over $ \mathbb{Q} $. Let us fix a maximal compact subgroup $ K_{\infty}^{\max } $ of $ G(\mathbb{R}) $ and let $ C:=\left(K_{\infty}^{\max }\right)^{\circ} $. Let us then fix/denote:

    - $ K_{\infty} $ to be a compact subgroup of $ G(\mathbb{R}) $ such that $ C \subseteq K_{\infty} \subseteq K_{\infty}^{\max } $
    - $ A_G $ is the maximal $ \mathbb{Q} $-split subtorus of $ Z(G) $. Then, for any compact open subgroup $ K_f \subseteq G\left(\mathbb{A}_f\right) $ we set

    $$S_G\left(K_f\right):=G(\mathbb{Q}) \backslash G(\mathbb{A}) /\left(K_{\infty} K_f A_G(\mathbb{R})^{+}\right)$$

    A space of the form $ S_G\left(K_f\right) $ is called a locally symmetric space for $ G $. Here we are denoting by $ \mathbb{A}=\left(\widehat{\mathbb{Z}} \otimes_{\mathbb{Z}} \mathbb{Q}\right) \times \mathbb{R} $ the adele ring for $ \mathbb{Q} $ and by $ \mathbb{A}_f $ its subring of finite adeles $ \widehat{\mathbb{Z}} \otimes \mathbb{\mathbb { Z }} \mathbb{Q} $. We topologize this by the restricted direct topology and topologize $ G(\mathbb{A}) $ and $ G\left(\mathbb{A}_f\right) $ in the usual way (e.g. see $$Con12$$).

- What is a Hermitian symmetric domain?

    A hermitian space is a smooth manifold $ M $ endowed with a riemannian structure $ g $ and a complex structure $ J $ that are compatible in the sense that $ g(J x, J y)=g(x, y) $ for all $ m \in M $ and all $ x, y \in T_m M $. $ ^6 $ A hermitian space is symmetric if every point is an isolated fixed point of an involution. A hermitian symmetric domain is a hermitian symmetric space with negative (sectional) curvature.

    Every hermitian symmetric domain decomposes as a product of simple (irreducible) hermitian symmetric domains $ D $ whose automorphism groups $ \operatorname{Hol}(D) $ are simple Lie groups.

- What is a Shimura variety?

    Let $ D $ be a hermitian symmetric domain, and let $ \operatorname{Hol}(D)^{+} $be the identity component of $ \operatorname{Hol}(D) $. Then $ \operatorname{Hol}(D)^{+} $is a connected semisimple Lie group with trivial centre. Consider a simply connected semisimple algebraic group $ G $ over $ \mathbb{Q} $ and a surjective homomorphism

    $$G(\mathbb{R}) \rightarrow \operatorname{Hol}(D)^{+}$$

    with compact kernel (such pairs always exist, and are classified). Let $ \Gamma $ be a congruence subgroup in $ G(\mathbb{Q}) $ whose image $ \overline{\Gamma} $ in $ \operatorname{Aut}(D)^{+} $is torsion-free. Then $ \overline{\Gamma} $ acts freely $ D $, and so the quotient $ \overline{\Gamma} \backslash D $ is a complex manifold. We'll see shortly that it is, in fact, an algebraic variety.

    The Shimura varieties are the algebraic varieties that arise in this way. In other words, an algebraic variety over $ \mathbb{C} $ is a Shimura variety if its universal covering space (in the topological sense) is a hermitian symmetric domain, and its fundamental group is the image of a congruence group as above.

- What are full and faithful functors?

    Explicitly, let $ C $ and $ D $ be (locally small) categories and let $ F: C \rightarrow D $ be a functor from $ C $ to $ D $. The functor $ F $ induces a function

    $$F_{X, Y}: \operatorname{Hom}_{\mathcal{C}}(X, Y) \rightarrow \operatorname{Hom}_{\mathcal{D}}(F(X), F(Y))$$

    for every pair of objects $ X $ and $ Y $ in $ C $. The functor $ F $ is said to be - faithful if $ F_{X, Y} $ is injective $ { }^{[1][2]} $ - full if $ F_{X, Y} $ is surjective $ { }^{[2][3]} $ - fully faithful (= full and faithful) if $ F_{X, Y} $ is bijective for each $ X $ and $ Y $ in $ C $. A mnemonic for remembering the term "full" is that the image of the function fills the codomain; a mnemonic for remembering the term "faithful" is that you can trust (have faith) that $ F(X)=F(Y) $ implies $ X=Y $.

    Warning: faithful need not imply injective on objects or morphisms!

- What is Chow's theorem for complex projective varieties?

    Chow 1949: The functor $ X \rightsquigarrow X(\mathbb{C}) $ from nonsingular projective algebraic varieties to projective complex manifolds is an equivalence of categories. This remains true when singularities are allowed.

- How is $ {\operatorname{THH}}(A) $ defined?

    $ {\operatorname{THH}}(A) \coloneqq A \wedge_{A^e} A $ where $ A^e \coloneqq A\wedge A $, defined for $ A\in { {}_{{\mathbb{E}}_1}  \mathsf{Alg}} $.

- How is $ {\operatorname{HH}}^*_{{\mathbb{E}}_n}(A) $ defined for $ A\in { {}_{{\mathbb{E}}_n} \mathsf{Alg}} $?

    Essentially $ \int_{S^n} A $.

- Describe factorization homology.

    A homology theory for framed $ n $-manifolds with coefficients given by $ \mathcal{E}_n $-algebras, constructed as a topological analogue of Beilinson-Drinfeld's chiral homology (for factorization coalgebras, motivated by conformal field theory).

- Describe an $ {\mathbb{E}}_n{\hbox{-}} $algebra.

    Algebras with multiplication maps parametrized by configuration spaces of $ n $-dimensional disks inside a standard $ n $-disk.

- Describe a braided monoidal category in terms of $ {\mathbb{E}}_n{\hbox{-}} $algebras.

    An $ {\mathbb{E}}_2{\hbox{-}} $algebra object in $ \mathsf{Cat} $, since $ {\mathbb{E}}_2(n) = {\mathbf{B}}B_n $ where $ B_n $ is the pure braid group.

- What are the higher classifying spaces $ {\mathbf{B}}^n A $ for $ A\in { {}_{{\mathbb{E}}_n} \mathsf{Alg}} $?

    A $ \mathsf{C}{\hbox{-}} $enriched $ (\infty, n){\hbox{-}} $category whose object is a point, a single $ k{\hbox{-}} $morphism $ \phi^k $ for each $ 1\leq k\leq n-1 $, and $ {\mathbf{B}}^nA(\phi^{n-1}, \phi^{n-1})\simeq A $.

- Describe $ \Omega_A $ algebraically.

    $ I/I^2 $ where $ I \coloneqq\ker(A{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  }\to A) $.

    Corepresents derivations: $ \mathop{\mathrm{Der}}_k(A, {-}) \cong \mathop{\mathrm{Hom}}_A(\Omega_A, {-}) $.

- Describe $ {\mathbb{L}} $ algebraically.

    For $ A $ nonsmooth, $ \mathop{\mathrm{Der}}_k(A, {-}) $ is not right exact, and has Quillen right-derived functors corepresented by $ {\mathbb{L}}_A $.

- What is a presentable $ \infty{\hbox{-}} $category?

    Closed under small colimits and limits, and weakly generated by a small subcategory.

    Given by localizations of $ \infty{\hbox{-}} $categories of presheaves on a small $ \infty{\hbox{-}} $category.

- What is a continuous functor?

    Preserves all colimits.

- Give a precise definition of factorization homology.

    *(Answer was a figure; image not recovered.)*

- What motivates construction of the Tate diagonal?

    $ {\mathsf{Sp}} $ does not have a diagonal map, $ X\to X{ {}^{ \scriptstyle\otimes_{}^{2} }  } $ which factors through homotopy fixed points $ (X{ {}^{ \scriptstyle\otimes_{}^{2} }  })^{hC_2}\to X{ {}^{ \scriptstyle\otimes_{}^{2} }  } $ (i.e. is symmetric), although this does exist for $ \Sigma_+^\infty X $ for $ X\in {\mathsf{Top}} $ induced by the diagonal of spaces.

- Define the Tate diagonal.

    The natural transformation

    $$ \Delta_p: \mathrm{id}_{\mathrm{Sp}} \rightarrow T_p: X \rightarrow(X \otimes \ldots \otimes X)^{t C_p}$$

    of endofunctors of $ \mathrm{Sp} $ which corresponds to the map

    $$\mathbb{S} \rightarrow T_p(\mathbb{S})=\mathbb{S}^{t C_p}$$

    which is the composition $ \mathbb{S} \rightarrow \mathbb{S}^{h C_p} \rightarrow \mathbb{S}^{t C_p} $.

- What is the right analog of $ { {\mathbf{Z}}_{\widehat{p}} } $ in $ {\mathsf{Sp}} $?

    $ {\mathbf{S}}^{tC_p} $, since $ H{\mathbf{Z}}^{tC_p} $ is not connective.

- Motivate the passage from schemes to derived stacks.

    $ {\mathsf{Sch}}\to{\mathsf{St}} $: closure under taking quotients and other colimits

    $ {\mathsf{St}}\to \mathsf{dSt} $: closure under taking fiber products and other limits

    $ {\mathsf{Sch}}\to \mathsf{dSt}: $ closure under "imposing equations".

    Think of $ X\in \dSt $ as a functor $ F_X: \mathsf{dCRing}\to {\mathsf{Top}} $.

    Think of source as connective cdgas, more generally connective $ {\mathbb{E}}_\infty{\hbox{-}} $ring spectra.

- Give a notion of "smallness" for $ F\in {\mathsf{QCoh}}(X) $.

    Perfect, dualizable, or compact objects.

- What is the derived version of the center of an algebra $ Z(A) $?

    $ {\operatorname{HH}}(A) $, computes$ \mathop{\mathrm{\mathbb{R}Hom}}_{({A}, {A}){\hbox{-}}\mathsf{biMod}}(A, A) $ (the derived $ (A,A){\hbox{-}} $bimodule endomorphism algebra).

- What is the free loop space of a derived stack?

    $ {\mathcal{L}}X \coloneqq\mathop{\mathrm{Maps}}(X, S^1) = X \underset{\scriptscriptstyle {X^e} }{\times} X $ where $ X^e \coloneqq X \underset{\scriptscriptstyle {k} }{\times}X $.

- What is $ {\mathcal{L}}X $ when $ X\in {\mathsf{Sch}}_{/ {k}} $ in characteristic zero?

    $ {\mathcal{L}}X = {\mathbf{T}}_X[-1] = \operatorname{Spec}\operatorname{Sym}^*\Omega_X[1] $.

- What is $ {\mathcal{L}}{{\mathbf{B}}G} $?

    The adjoint quotient $ G/G $.

- What is the stacky version of a $ G{\hbox{-}} $local system on $ X $?

    $ \mathsf{Loc}_G(X) \cong \mathop{\mathrm{Maps}}(X, {{\mathbf{B}}G}) $.

- What is a stable $ \infty{\hbox{-}} $category?

    Zero object

    Closed under finite limits and colimits

    Pushouts equal pullbacks

- How are triangulated categories related to infinity categories?

    $ {\mathsf{ho}}\mathsf{C} $ has a canonical triangulated structure for $ \mathsf{C} $ a stable infty cat.

- What does it mean for a functor $ F:\mathsf{C}\times \mathsf{D}\to \mathsf{E} $ to be bilinear?

    Factors through $ \mathsf{C}\otimes\mathsf{D} $, commutes with colimits in both variables separately.

- What is the sheaf condition for a derived stack?

    $ X\in {\mathsf{Fun}}( {}_{k}  \mathsf{Alg}, {\mathsf{Top}}) $ where if $ A\to B $ is an etale cover, $ X(A)  { \, \xrightarrow{\sim}\, }\lim X(\tilde B) $ is an equivalence where $ \tilde B\rightrightarrows B $ is the cosimplicial bar resolution induced by $ {-}\otimes_A B $.

- What is a compact object?

    An object $ M $ of a stable $ \infty $-category $ \mathcal{C} $ is said to be compact if $ \operatorname{Hom}_{\mathcal{C}}(M,-) $ commutes with all coproducts (equivalently, with all colimits).

    $ M $ is compact iff any map $ M\to A $ where $ A $ is a small coproduct factors through a finite coproduct, when $ \mathsf{C} $ is stable presentable.

- What is a dualizable object?

    (2) An object $ M $ of a stable symmetric monoidal $ \infty $-category $ \mathcal{C} $ is said to be (strongly) dualizable if there is an object $ M^{\vee} $ and unit and trace maps

    $$1 \stackrel{u}{\longrightarrow} M \otimes M^{\vee} \stackrel{\tau}{\longrightarrow} 1$$

    such that the composite map

    $$M \stackrel{u \otimes \mathrm{id}}{\longrightarrow} M \otimes M^{\vee} \otimes M \stackrel{\mathrm{id} \otimes \tau}{\longrightarrow} M$$

    is the identity.

- What is the usefulness of dualizable objects?

    *(Answer was a figure; image not recovered.)*
