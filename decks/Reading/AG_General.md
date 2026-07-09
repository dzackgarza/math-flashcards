---
title: "Reading::AG_General"
---

- What is the Albanese variety of $ Z $? Its corresponding embedding?

    $ \operatorname{Alb}(Z)=H^0\left(Z, \Omega_Z^1\right)^* / H_1(Z, \mathbf{Z}) $

    $ \Phi: Z\to \mathrm{Alb}(Z) $ sends a base point $ p\in Z $ to the origin and $ \Phi(z)(\eta) \coloneqq\int_p^z \eta $.

- What is $ {\mathsf{G}{\hbox{-}}\mathsf{Torsors}}_{/ {X}} $?

    Schemes $ Y\to X $ with a fiberwise $ G{\hbox{-}} $action which etale-locally looks like $ G\times X $ with $ G\curvearrowright G $ by right-translation, and morphisms are $ G{\hbox{-}} $equivariant morphisms over $ X $.

- What is an etale morphism in $ \mathsf{CAlg}_{/ {{\mathbf{Z}}}} $?

    $ \pi: R\to S\in \mathsf{CAlg}_{/ {{\mathbf{Z}}}} $ is etale iff

    $ \pi $ is flat

    $ {\partial}_2: S{ {}^{ \scriptstyle\otimes_{R}^{2} }  }\to S $ is flat.s

    $ S $ is finitely presented over $ R $

- Discuss how etaleness is related to smoothness.

    Etale $ \implies $ smooth.

    Smooth and $ \Omega_{S/R} = 0 \implies $ etale.

- What is an ample bundle?

    Some power is very ample

    Very ample: bpf/gg and $ \phi_{{\left\lvert {L} \right\rvert}}: X\to {\mathbf{P}}^{h^0(L) - 1} $ is a closed immersion.

    Tensoring high powers with a coherent sheaf gives many global sections.

- When is $ {\mathcal{O}}_{{\mathbf{P}}^n}(d) $ ample? Very ample?

    BPF iff $ d\geq 0 $

    Very ample iff ample iff $ d\geq 1 $.

- What is a big bundle?

    Sections grow maximally: $ h^0(L^k)\geq { \mathsf{O}}( k^{\dim X} ) $.

- What is a nef bundle?

    $ L $ has non-negative degree on every irreducible curve $ C $

    Degree: $ \deg \operatorname{div}(s) $ for $ s $ any rational section of $ L $.

- What is a big and nef bundle?

    $ L^2 > 0 $ and $ L $ is nef.

- What is a large complex structure limit?

    Idea: line bundle $ L $ over the total space of a family which specifies $ c_1(L) $ and thus a symplectic class.

    A polarized algebraic family of $ n $-dim CY manifolds $ X \rightarrow S \backslash\{0\} $ over a punctured algebraic curve, whose 'essential skeleton' (simplicial subcomplex of dual complex) has dimension $ n $.

    Also called "maximal degeneration"

    Semistable SNC model.

- Describe a toric Fano variety and its singularities.

    Primitive generators form a convex polytope in $ N $

    $ -K $ is ample

    If integral points on boundary: canonical singularities

    If all integral points outside: terminal

- What is a stable curve?

    Nodal with $ {\sharp}\mathop{\mathrm{Aut}}(X) < \infty $ (nodes: $ xy=0 $).

- What is the scheme-theoretic definition of an elliptic curve over $ R $?

    A smooth proper morphism $ \pi: E\to \operatorname{Spec}R $ with a section $ 0: \operatorname{Spec}R\to E $ where the geometric fibers of $ \pi $ are connected genus 1 curves.

    Implies $ h^0(E; \Omega_{E/R}) =1 $.

- What is a hyperplane section? Give an example.

    $ Y \subseteq X $ of the form $ Y = X\cap H $ for $ X\hookrightarrow{\mathbf{P}}^N $ and $ H\subseteq {\mathbf{P}}^N $ a hyperplane.

    Any hypersurface is an example.

- What is the Lefschetz decomposition?

    $$H^k(X; {\mathbf{C}}) = \bigoplus_{2r\leq k}L^r H^{k-2r}_{\operatorname{prim}}(X)$$

- Draw a picture of 3-dimensional vanishing cycles.

    *(Answer was a figure; image not recovered.)*

- What is Bertini's theorem? Give a consequence.

    A generic hyperplane section is smooth.

- What is the Torelli theorem for K3s?

    Isomorphisms $ \sigma: X^{\prime} \rightarrow X $ are in bijection with the isometries $ \sigma^*: H^2(X, \mathbb{Z}) \rightarrow H^2\left(X^{\prime}, \mathbb{Z}\right) $ satisfyings $ \sigma^*\left(H^{2,0}(X)\right)=H^{2,0}\left(X^{\prime}\right) $ and $ \sigma^*\left(\mathcal{K}_X\right)=\mathcal{K}_{X^{\prime}} $.

- What is the hard Lefschetz theorem?

    For $ X $ compact Kahler, for $ k\leq n\coloneqq\dim X $,

    $ L^{n-k}: H^k(X; {\mathbf{R}}) { \, \xrightarrow{\sim}\, }H^{2n-k}(X; {\mathbf{R}}) $

    $ H^k(X; {\mathbf{R}}) = \bigoplus_{i\geq 0} L^i H^{k-2i}(X; {\mathbf{R}})_{\operatorname{prim}} $

    $ H^k(X; {\mathbf{R}})_{\operatorname{prim}}\otimes_{\mathbf{R}}{\mathbf{C}}=\bigoplus_{p+q=k} H^{p, q}(X)_{\operatorname{prim}} $.

- What is the Hodge index theorem?

    For $ X $ a compact Kahler surface, the intersection form satisfies

    $$\operatorname{sgn}H^2(X; {\mathbf{Z}}) = (2h^{2, 0} + 1,\, h^{1,1} -1), \qquad \operatorname{sgn}H^{1,1}(X) = (1,\, h^{1,1}-1)$$

    Equivalently, if $ L\in {\operatorname{NS}}(X)^{\mathrm{amp}} $ (or even $ L^2 \gt 0 $) then the intersection form is negative definite on $ L^\perp $.

- What is the Lefschetz $ (1, 1){\hbox{-}} $theorem?

    For $ X $ compact Kahler, $ \operatorname{Pic}(X) \twoheadrightarrow H^{1, 1}(X) $.

- What is nonabelian Hodge theory?

    $ {\mathcal{M}}_B $ is the moduli of irreducible reps of $ \pi_1(X) $, $ {\mathcal{M}}_{\mathrm{Dol}} $ of stable Higgs bundles, and $ {\mathcal{M}}_{\mathrm{dR}} $ of stable flat connections:

- What is $ {\mathsf{Bun}}_G $?

    $ {\mathsf{Bun}}_G(k) $ is the maximal subgroupoid of $ {\mathsf{G}{\hbox{-}}\mathsf{Torsors}}_{/ {X}} $.

    Forms an algebraic stack.

    Observation due to Weil: $ \dcoset{G(F)}{G({\mathbf{A}}_F)}{\prod_{x\in {\left\lvert {X} \right\rvert}}' G({\mathcal{O}}_x)}  { \, \xrightarrow{\sim}\, }{\mathsf{Bun}}_G $ where $ F= k(X) $, $ F_x $ is the completion at $ x $, and $ {\mathcal{O}}_x $ is its valuation ring. Supposed to resemble

    $$\dcoset{G(F)}{G({\mathbf{A}}_F)}{K }$$

- What is a rigid representation?

    Only trivial deformations, isolated point in character variety.

    Conjecture: rigid representations are "motivic", of geometric origin.

    E.g. irreducible rigid flat connections are subquotients of the Gauss-Manin connection on a family of smooth projective varieties over an open dense subvvariety of $ X $.

    The underlying local system is a summand of $ {\mathbf{R}}^if_* \underline{{\mathbf{C}}} $ for $ f:Y\to U $ a smooth projective morphism to a dense subvariety.

- What are Higgs bundles? Why care?

    $ (E, \theta) $ where $ E $ is a holomorphic bundle and $ \theta: E\to E\otimes\Omega^1_{X} $ is an endomorphism-valued 1-form satisfying $ \theta\wedge \theta =0 $.

    Stable Higgs bundles with $ c_1(E) = 0 $ biject with irreducible representations of $ \pi_1(X) $.

- What is Batyrev-Borisov's mirror symmetry?

    For e.g. complete intersections in Fanos, $ H^1(X; {\mathbf{T}} {}^{ \vee }X) \cong H^1(X {}^{ \vee }; {\mathbf{T}}X {}^{ \vee }) $.

    LHS: variations of $ \omega_X $ a symplectic form (A-model)

    RHS: variations of complex structure (B-model)
