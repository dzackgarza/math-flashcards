---
title: "Reading::AG_General"
---

::: {.front card-id="card-e0262b52c2d6df11"}
What is the Albanese variety of $ Z $? Its corresponding embedding?
:::

::: {.back card-id="card-e0262b52c2d6df11"}
$ \operatorname{Alb}(Z)=H^0\left(Z, \Omega_Z^1\right)^* / H_1(Z, \mathbf{Z}) $

$ \Phi: Z\to \mathrm{Alb}(Z) $ sends a base point $ p\in Z $ to the origin and $ \Phi(z)(\eta) \coloneqq\int_p^z \eta $.
:::

::: {.front card-id="card-a3ae8ea6c8023dc0"}
What is $ {\mathsf{G}{\hbox{-}}\mathsf{Torsors}}_{/ {X}} $?
:::

::: {.back card-id="card-a3ae8ea6c8023dc0"}
Schemes $ Y\to X $ with a fiberwise $ G{\hbox{-}} $action which etale-locally looks like $ G\times X $ with $ G\curvearrowright G $ by right-translation, and morphisms are $ G{\hbox{-}} $equivariant morphisms over $ X $.
:::

::: {.front card-id="card-e02f999b03b66a35"}
What is an etale morphism in $ \mathsf{CAlg}_{/ {{\mathbf{Z}}}} $?
:::

::: {.back card-id="card-e02f999b03b66a35"}
$ \pi: R\to S\in \mathsf{CAlg}_{/ {{\mathbf{Z}}}} $ is etale iff

$ \pi $ is flat

$ {\partial}_2: S{ {}^{ \scriptstyle\otimes_{R}^{2} }  }\to S $ is flat.

$ S $ is finitely presented over $ R $
:::

::: {.front card-id="card-bee224ddfaf88c1f"}
Discuss how etaleness is related to smoothness.
:::

::: {.back card-id="card-bee224ddfaf88c1f"}
Etale $ \implies $ smooth.

Smooth and $ \Omega_{S/R} = 0 \implies $ etale.
:::

::: {.front card-id="card-6e3dcdd9b9d82af7"}
What is an ample bundle?
:::

::: {.back card-id="card-6e3dcdd9b9d82af7"}
Some power is very ample

Very ample: bpf/gg and $ \phi_{{\left\lvert {L} \right\rvert}}: X\to {\mathbf{P}}^{h^0(L) - 1} $ is a closed immersion.

Tensoring high powers with a coherent sheaf gives many global sections.
:::

::: {.front card-id="card-80fa03cc214825fe"}
When is $ {\mathcal{O}}_{{\mathbf{P}}^n}(d) $ ample? Very ample?
:::

::: {.back card-id="card-80fa03cc214825fe"}
BPF iff $ d\geq 0 $

Very ample iff ample iff $ d\geq 1 $.
:::

::: {.front card-id="card-70ffac49f824101f"}
What is a big bundle?
:::

::: {.back card-id="card-70ffac49f824101f"}
Sections grow maximally: $ h^0(L^k)\geq { \mathsf{O}}( k^{\dim X} ) $.
:::

::: {.front card-id="card-79afba969c884033"}
What is a nef bundle?
:::

::: {.back card-id="card-79afba969c884033"}
$ L $ has non-negative degree on every irreducible curve $ C $

Degree: $ \deg \operatorname{div}(s) $ for $ s $ any rational section of $ L $.
:::

::: {.front card-id="card-ea9654ae52152e47"}
What is a big and nef bundle?
:::

::: {.back card-id="card-ea9654ae52152e47"}
$ L^2 > 0 $ and $ L $ is nef.
:::

::: {.front card-id="card-e0267814e9c4ee2e"}
What is a large complex structure limit?
:::

::: {.back card-id="card-e0267814e9c4ee2e"}
Idea: line bundle $ L $ over the total space of a family which specifies $ c_1(L) $ and thus a symplectic class.

A polarized algebraic family of $ n $-dim CY manifolds $ X \rightarrow S \backslash\{0\} $ over a punctured algebraic curve, whose 'essential skeleton' (simplicial subcomplex of dual complex) has dimension $ n $.

Also called "maximal degeneration"

Semistable SNC model.
:::

::: {.front card-id="card-2f2ff8053177735a"}
Describe a toric Fano variety and its singularities.
:::

::: {.back card-id="card-2f2ff8053177735a"}
Primitive generators form a convex polytope in $ N $

$ -K $ is ample

If integral points on boundary: canonical singularities

If all integral points outside: terminal
:::

::: {.front card-id="card-603471e11d967b1a"}
What is a stable curve?
:::

::: {.back card-id="card-603471e11d967b1a"}
Nodal with $ {\sharp}\mathop{\mathrm{Aut}}(X) < \infty $ (nodes: $ xy=0 $).
:::

::: {.front card-id="card-a20232b0e49681e4"}
What is the scheme-theoretic definition of an elliptic curve over $ R $?
:::

::: {.back card-id="card-a20232b0e49681e4"}
A smooth proper morphism $ \pi: E\to \operatorname{Spec}R $ with a section $ 0: \operatorname{Spec}R\to E $ where the geometric fibers of $ \pi $ are connected genus 1 curves.

Implies $ h^0(E; \Omega_{E/R}) =1 $.
:::

::: {.front card-id="card-693a53dc1f51c51e"}
What is a hyperplane section? Give an example.
:::

::: {.back card-id="card-693a53dc1f51c51e"}
$ Y \subseteq X $ of the form $ Y = X\cap H $ for $ X\hookrightarrow{\mathbf{P}}^N $ and $ H\subseteq {\mathbf{P}}^N $ a hyperplane.

Any hypersurface is an example.
:::

::: {.front card-id="card-1473584e4048a634"}
What is the Lefschetz decomposition?
:::

::: {.back card-id="card-1473584e4048a634"}
$$H^k(X; {\mathbf{C}}) = \bigoplus_{2r\leq k}L^r H^{k-2r}_{\operatorname{prim}}(X)$$
:::

::: {.front card-id="card-6c5784cabdbc59b9"}
Draw a picture of 3-dimensional vanishing cycles.
:::

::: {.back card-id="card-6c5784cabdbc59b9"}
For the smoothing $X_t=\{z_1^2+z_2^2+z_3^2+z_4^2=t\}\subset\mathbb C^4$ with $t>0$, the real locus $\{(x_1,\ldots,x_4)\in\mathbb R^4:\sum x_i^2=t\}$ is a three-sphere $S^3\subset X_t$. It shrinks to the node as $t\to0$; this is the vanishing cycle.
:::

::: {.front card-id="card-00f3486c354c5d79"}
What is Bertini's theorem? Give a consequence.
:::

::: {.back card-id="card-00f3486c354c5d79"}
A generic hyperplane section is smooth.
:::

::: {.front card-id="card-34fab36bd27bc9e8"}
What is the Torelli theorem for K3s?
:::

::: {.back card-id="card-34fab36bd27bc9e8"}
Isomorphisms $ \sigma: X^{\prime} \rightarrow X $ are in bijection with the isometries $ \sigma^*: H^2(X, \mathbb{Z}) \rightarrow H^2\left(X^{\prime}, \mathbb{Z}\right) $ satisfying $ \sigma^*\left(H^{2,0}(X)\right)=H^{2,0}\left(X^{\prime}\right) $ and $ \sigma^*\left(\mathcal{K}_X\right)=\mathcal{K}_{X^{\prime}} $.
:::

::: {.front card-id="card-49cc848db9c8f1bf"}
What is the hard Lefschetz theorem?
:::

::: {.back card-id="card-49cc848db9c8f1bf"}
For $ X $ compact Kahler, for $ k\leq n\coloneqq\dim X $,

$ L^{n-k}: H^k(X; {\mathbf{R}}) { \, \xrightarrow{\sim}\, }H^{2n-k}(X; {\mathbf{R}}) $

$ H^k(X; {\mathbf{R}}) = \bigoplus_{i\geq 0} L^i H^{k-2i}(X; {\mathbf{R}})_{\operatorname{prim}} $

$ H^k(X; {\mathbf{R}})_{\operatorname{prim}}\otimes_{\mathbf{R}}{\mathbf{C}}=\bigoplus_{p+q=k} H^{p, q}(X)_{\operatorname{prim}} $.
:::

::: {.front card-id="card-e035601038997a30"}
What is the Hodge index theorem?
:::

::: {.back card-id="card-e035601038997a30"}
For $ X $ a compact Kahler surface, the intersection form satisfies

$$\operatorname{sgn}H^2(X; {\mathbf{Z}}) = (2h^{2, 0} + 1,\, h^{1,1} -1), \qquad \operatorname{sgn}H^{1,1}(X) = (1,\, h^{1,1}-1)$$

Equivalently, if $ L\in {\operatorname{NS}}(X)^{\mathrm{amp}} $ (or even $ L^2 \gt 0 $) then the intersection form is negative definite on $ L^\perp $.
:::

::: {.front card-id="card-94bd03bf46f7461f"}
What is the Lefschetz $ (1, 1){\hbox{-}} $theorem?
:::

::: {.back card-id="card-94bd03bf46f7461f"}
For $ X $ compact Kahler, $ \operatorname{Pic}(X) \twoheadrightarrow H^{1, 1}(X) $.
:::

::: {.front card-id="card-32d30066fccb982b"}
What is nonabelian Hodge theory?
:::

::: {.back card-id="card-32d30066fccb982b"}
$ {\mathcal{M}}_B $ is the moduli of irreducible reps of $ \pi_1(X) $, $ {\mathcal{M}}_{\mathrm{Dol}} $ of stable Higgs bundles, and $ {\mathcal{M}}_{\mathrm{dR}} $ of stable flat connections:
:::

::: {.front card-id="card-a62507d3e1e915e7"}
What is $ {\mathsf{Bun}}_G $?
:::

::: {.back card-id="card-a62507d3e1e915e7"}
$ {\mathsf{Bun}}_G(k) $ is the maximal subgroupoid of $ {\mathsf{G}{\hbox{-}}\mathsf{Torsors}}_{/ {X}} $.

Forms an algebraic stack.

Observation due to Weil: $ \dcoset{G(F)}{G({\mathbf{A}}_F)}{\prod_{x\in {\left\lvert {X} \right\rvert}}' G({\mathcal{O}}_x)}  { \, \xrightarrow{\sim}\, }{\mathsf{Bun}}_G $ where $ F= k(X) $, $ F_x $ is the completion at $ x $, and $ {\mathcal{O}}_x $ is its valuation ring. Supposed to resemble

$$\dcoset{G(F)}{G({\mathbf{A}}_F)}{K }$$
:::

::: {.front card-id="card-af845a3fa43df735"}
What is a rigid representation?
:::

::: {.back card-id="card-af845a3fa43df735"}
Only trivial deformations, isolated point in character variety.

Conjecture: rigid representations are "motivic", of geometric origin.

E.g. irreducible rigid flat connections are subquotients of the Gauss-Manin connection on a family of smooth projective varieties over an open dense subvariety of $ X $.

The underlying local system is a summand of $ {\mathbf{R}}^if_* \underline{{\mathbf{C}}} $ for $ f:Y\to U $ a smooth projective morphism to a dense subvariety.
:::

::: {.front card-id="card-8e8acdcff9808d4b"}
What are Higgs bundles? Why care?
:::

::: {.back card-id="card-8e8acdcff9808d4b"}
$ (E, \theta) $ where $ E $ is a holomorphic bundle and $ \theta: E\to E\otimes\Omega^1_{X} $ is an endomorphism-valued 1-form satisfying $ \theta\wedge \theta =0 $.

Stable Higgs bundles with $ c_1(E) = 0 $ biject with irreducible representations of $ \pi_1(X) $.
:::

::: {.front card-id="card-5ab68700993ee9f6"}
What is Batyrev-Borisov's mirror symmetry?
:::

::: {.back card-id="card-5ab68700993ee9f6"}
For e.g. complete intersections in Fanos, $ H^1(X; {\mathbf{T}} {}^{ \vee }X) \cong H^1(X {}^{ \vee }; {\mathbf{T}}X {}^{ \vee }) $.

LHS: variations of $ \omega_X $ a symplectic form (A-model)

RHS: variations of complex structure (B-model)
:::
