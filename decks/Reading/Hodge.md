---
title: "Reading::Hodge"
---

- What is a QHS?

    For $ V\in  {}_{{\mathbf{Q}}}{\mathsf{Mod}}^{\mathrm{fd}} $, a decomposition $ V = \bigoplus_{p, q} V^{p, q} $ with $ \overline{V^{p, q}} = V^{q, p} $ where $ V_m \coloneqq\bigoplus_{p+q=m} V^{p, q} $ is defined over $ {\mathbf{Q}} $.

- What is a ZHS?

    A QHS $ V $ with a lattice $ V({\mathbf{Z}}) \subset V({\mathbf{Q}}) $.

- What is the Weil element of a QHS?

    $ C\in \operatorname{GL}(V) $ which acts as $ i^{p-q} $ in $ V^{p, q} $.

- What is a pure QHS of weight $ m $?

    $ p+q\neq m\implies V^{p, q} = 0 $

- What is the colevel of a HS?

    $ \min\left\{{p{~\mathrel{\Big\vert}~}h^{p, m-p} \neq 0}\right\} $.

- What are the filtrations on a HS?

    Increasing Hodge filtration: $ \operatorname{Fil}^n V \coloneqq\sum_{p > n, q} V^{p, q} $

    Decreasing weight filtration: $ \operatorname{Fil}_n V \coloneqq\sum_{p+q \leq n} V^{p, q} $.

- What are the Weil and Griffiths intermediate Jacobians?

    Define $ V_W $ the Weil complex structure $ V_W^{1, 0} $ and Griffiths complex structure $ V_G^{1 ,0} = F^{k+1}V $

    Then

    $$J_W(V)=V /\left(V(\mathbb{Z})+V_W^{1,0}\right) \text { and } J_G(V)=V /\left(V(\mathbb{Z})+F^{k+1} V\right)$$

- What is the Serre-Deligne torus $ S $? Why is it important?

    $ S({\mathbf{R}}) ={\mathbf{C}}^{\times} $, so $ S = \mathrm{Res}^{{\mathbf{C}}}_{{\mathbf{R}}} {\mathbf{G}}_m $.

    Alternatively $ { \begin{bmatrix} {a} & {-b}  \\ {b} & {a} \end{bmatrix} } \in \operatorname{GL}_2({\mathbf{R}}) $.

    There is a cocharacter $ w: {\mathbf{G}}_m\to S $ which on real points is $ {\mathbf{R}}^{\times}\hookrightarrow{\mathbf{C}}^{\times} $, a QHS on $ V $ is the same as an action $ S\curvearrowright V $ defined over $ {\mathbf{R}} $ with $ w $ defined over $ {\mathbf{Q}} $, so $ V^{p, q} $ are eigenspaces with characters $ z^p\overline{z}^q $.

- What is the Tate HS? Where does it come from?

    $ {\mathbf{Z}}(1) $ the ZHS on $ {\mathbf{C}} $ of bidegree $ (-1, -1) $ with lattice $ 2\pi i {\mathbf{Z}} $.

    Natural HS on $ H^1({\mathbf{G}}_m(k)) $ for $ k={ \overline{k} }\subseteq {\mathbf{C}} $, regard as $ H^2({\mathbf{CP}}^1; {\mathbf{Z}}) $.

- What is $ {\mathbf{Z}}(m) $? $ V(m) $?

    $ {\mathbf{Z}}(m) = {\mathbf{Z}}(1){ {}^{ \scriptstyle\otimes_{}^{m} }  } $ with lattice $ (2\pi i)^m {\mathbf{Z}} $

    $ V(m) = V\otimes_{\mathbf{Z}}{\mathbf{Z}}(m) $.

- What is a polarization of a QHS?

    For a pure HS of weight $ m $, $ Q:V{ {}^{ \scriptstyle\otimes_{}^{2} }  }\to {\mathbf{Z}}(-m) $ defined over $ {\mathbf{Q}} $ such that the form $ (v,w)\mapsto (2\pi i)^m Q(Cv, w) $ is Hermitian and positive-definite, where $ C $ is the Weil element.

    Alternatively a morphism $ V\to V {}^{ \vee }(-m) $, motivated by Poincare duality.

- What is the Hodge spectral sequence?

    $ E_1^{p, q} = H^q(M; \Omega_M^p) \Rightarrow H^{p+q}(M; {\mathbf{C}}) $.

- What is the primitive part of cohomology?

    $ H_{\operatorname{prim}}^{n-k}(M) \coloneqq\ker\qty{H^{n-k} \xrightarrow{L^{k+1}} H^{n+k+2} } $.

- Discuss the Hodge spectral sequence for $ M $ connected and projective (or more generally compact Kahler).

    Degenerates at $ E_1 $, yielding a decreasing filtration $ \operatorname{Fil}^* H^d(M;{\mathbf{C}}) $ with $ {\mathsf{gr}\,}^p H^d(M; {\mathbf{C}}) \cong H^{d-p}(M; \Omega_M^p) $.

    Puts a HS of pure weight $ d $ on $ H^d(M; {\mathbf{C}}) $ with Hodge filtration $ \operatorname{Fil}^* $.

    $ H^{2n}(M; {\mathbf{C}})= {\mathbf{Z}}(-n) $.

    For $ \eta\in H^2(M; {\mathbf{Q}}) $ a hyperplane class, $ \eta $ is type $ (1,1) $ and defines a Lefschetz operator $ L({-}) \coloneqq\eta\cup({-}) $.

    Hard Lefschetz holds: $ L^k: H^{n-k}(M; {\mathbf{Q}}) { \, \xrightarrow{\sim}\, }H^{n+k}(M; {\mathbf{Q}}) $ for all $ n $.

    $$\bigoplus_{k=0}^n H_{\operatorname{prim}}^{n-k}(M; {\mathbf{Q}})\otimes_{\mathbf{R}}{{\mathbf{C}}[L] \over \left\langle{L^{k+1}}\right\rangle} { \, \xrightarrow{\sim}\, }H^*(M; {\mathbf{C}})$$

    There is a polarization

    $$\begin{align}I: H_{\operatorname{prim}}^{n-k}(M; {\mathbf{Q}}){ {}^{ \scriptstyle\otimes_{}^{2} }  } &\to {\mathbf{Q}}\\ a\otimes b &\mapsto(-1)^{(n-k)(n-k-1)\over 2} \int_M L^k(a\wedge b)\end{align}$$

- Discuss relative differentials?

    For $ f: M\to S $, $ \Omega^*_M / \left\langle{f^* \Omega^1_S}\right\rangle $, a quotient of a sheaf of dg $ {\mathcal{O}}_M{\hbox{-}} $algebras.

    Fiber over $ s\in S $ is the de Rham sheaf complex of the fiber $ M_s $.

    Resolves $ f^{-1}{\mathcal{O}}_S $ by coherent $ {\mathcal{O}}_M $ modules

- What is a VHS?

    Over a smooth variety $ S $, a local system $ V $ on $ S $ of $   {}_{ {\mathbf{C}}}{\mathsf{Mod}}^{\mathrm{fd}} $ defined over $ {\mathbf{Q}} $

    With an increasing weight filtration by sub-local systems

    With a decreasing Hodge filtration on the underlying vector bundle $ {\mathcal{V}}\coloneqq{\mathcal{O}}_S \otimes{{\mathbf{C}}_S} V $ by sub-bundles satisfying

    Having a HS on every fiber

    The covariant derivative maps $ \operatorname{Fil}^p {\mathcal{V}}\to \operatorname{Fil}^{p-1}{\mathcal{V}} $.

- What is a PVHS over $ S $?

    For a VHS of pure weight $ m $, a polarization $ V\otimes_{{\mathbf{C}}_S}V\to {\mathbf{Z}}_S(-m) $.

- What is the Gysin sequence?

    $$\cdots \rightarrow \mathrm{H}_{\mathrm{Y}}^{\mathrm{d}}(\mathrm{X}) \rightarrow \mathrm{H}^{\mathrm{d}}(\mathrm{X}) \rightarrow \mathrm{H}^{\mathrm{d}}(\mathrm{X}-\mathrm{Y}) \rightarrow \mathrm{H}_{\mathrm{Y}}^{\mathrm{d}+1}(\mathrm{X}) \rightarrow \cdots$$

- What is an MHS?

    A decreasnig Hodge filtration $ \operatorname{Fil}_H V $ and an increasing weight filtration $ \operatorname{Fil}^W V $ such that the filtration on $ {\mathsf{gr}\,}_\ell^W $ induced by $ \operatorname{Fil}_H $ gives a HS of pure weight $ \ell $.

- Discuss MHSs.

    For $ X\in {\mathsf{Sch}}_{/ {{\mathbf{C}}}}^\mathrm{ft} $ a variety, $ H^d(X) $ carries a MHS with weights in $ \left\{{0,1,\cdots, 2d}\right\} $.

    If $ X $ is smooth, the weights are $ \geq d $.

    If $ X $ is complete, the weights are $ \leq d $.

    This extends the functor $ {\mathsf{Mfd}}_{\mathbf{C}}\to \mathsf{HS} $ to $ {\mathsf{Var}}_{/ {{\mathbf{C}}}}^\mathrm{ft}\to \mathsf{MHS} $.

- What is a primitively polarized K3 of genus $ g $?

    $ (X, \eta) $ where $ \eta\in H^{1,1}(X; {\mathbf{R}}) $ is a Kahler class.

    Torelli: iso type of $ (X, \eta) $ completely determined by $ (H^2(X;{\mathbf{Z}}), \cap) $, $ \eta $, and the HS on $ H^2(X;{\mathbf{C}}) $.

    Primitive: not a proper multiple of an integral class.

    $ g\coloneqq 1+{1\over 2}(\eta.\eta) $; the linear system $ \eta $ defines contains curves of arithmetic genus $ g $.

- What is the polarization on $ H^1(X) $ for $ X $ smooth Kahler?

    $ (\alpha, \beta)\mapsto \int_M \alpha\wedge\beta\wedge \omega^{\dim M - 1} \in {\mathbf{R}} $.

- Where do MHSs appear?

    Cohomology of noncompact $ {\mathbf{C}}{\hbox{-}} $varieties.

    Limits of PVHS

    $ \pi_1(X) \otimes{\mathbf{R}} $ for $ X\in \mathsf{Alg}{\mathsf{Var}}_{/ {{\mathbf{C}}}} $.

    $ \pi_*(X)\otimes{\mathbf{R}} $ for $ X\in  \mathsf{Alg}{\mathsf{Var}}_{/ {{\mathbf{C}}}} $ with $ \pi_1(X) = 1 $.

- What is a polarized Hodge structure on $ V\in {}_{{\mathbf{C}}}{\mathsf{Mod}} $?

    $ V = \bigoplus V^{p, q} $ with $ Q:V\otimes_{\mathbf{C}}\overline{V} \to {\mathbf{C}} $ such that

    the decomposition is orthogonal with respect to $ Q $ and

    $ (-1)^p Q $ is positive definite on $ V^{p, q} $, so there is a positive definite Hermitian product $ {\left\langle {v},~{w} \right\rangle} \coloneqq\sum_{p, q} (-1)^p Q(v^{p, q}, w^{p, q}) $.

- What is a polarized VHS for $ (E, d: A^0(E) \to A^1(E)) $ a flat bundle on $ X $?

    Puts a Hermitian metric on a vector bundle!

    $ E = \bigoplus_{p+q=k} E^{p, q} $ as sub-bundles such that

    $$d(A^0\left(E^{p, q}\right)) \subseteq A^{1,0}\left(E^{p, q}\right) \oplus A^{1,0}\left(E^{p-1, q+1}\right) \oplus A^{0,1}\left(E^{p, q}\right) \oplus A^{0,1}\left(E^{p+1, q-1}\right)$$

    Each fiber $ E_x $ is a Hodge structure of weight $ k $.

    Polarization: $ Q: A^0(E) \otimes_{A^0}\overline{A^0(E)} \to A^0 $ which satisfies the Leibniz rule wrt $ d $ and induces polarizations on every fiber.

    Yields a positive definite Hermitian metric $ h(u, w)\coloneqq\sum_{p+q=k} (-1)^p Q(v^{p, q}, w^{p, q}) $.

- What is Griffiths transversaility?

    $$\nabla({\mathcal{F}}^p)\subseteq {\mathcal{F}}^{p-1} \otimes\Omega^1$$

    Needed since the Hodge filtration on the fibers are not necessarily preserved by differentiation.

- What is the Leray spectral sequence?

    For $ f:X\to Y $,

    $$H^p\left(Y, {\mathbf{R}}^q f_* \mathbb{Q}\right) \Rightarrow H^{p+q}(X, \mathbb{Q})$$

- Give a sufficient condition for the Leray spectral sequence to degenerate.

    $ f:X\to Y $ smooth projective, by Deligne, as a conseuence of Hard Lefschetz.

- What is a connection?

    For $ L $ a local system on $ Y $,parallel transport induces $ \nabla_\eta: V_y\to V_y $ for $ \eta\in T_y Y $ and $ V\coloneqq{\mathcal{O}}_Y\otimes_{\mathbf{C}}L $ the associated vector bundle.

    Satisfies $ \nabla_\eta(fv) = \eta(f)v + f\nabla_\eta(v) $.

    View as an operator $ \nabla: V\to \Omega^1_Y \otimes V $ satisfying $ \nabla(fv) = df\otimes v + f\nabla(v) $.

- When is a connection integrable?

    E.g. if $ \nabla^2 = 0 $; equivalent to having $ \operatorname{rank}V $ solutions to $ \nabla v = 0 $.

- What is the Gauss-Manin connection?

    For $ f:X\to Y $, the integrable connection on $ V \coloneqq{\mathcal{O}}_Y \otimes_{\mathbf{C}}{\mathbf{R}}^i f_* \underline{{\mathbf{C}}} $, the vector bundle associated to the local system $ L\coloneqq{\mathbf{R}}^1 f_* \underline{{\mathbf{C}}} $.

    Sections $ L $ are precisely solutions to $ \nabla v = 0 $.

- Motivate perverse sheaves.

    The Leray spectral sequence doesn't degenerate for arbitrary morphisms $ f:X\to Y $, nor is there a decomposition $ {\mathbf{R}}f_* {\mathbf{Q}}= \bigoplus {\mathbf{R}}^q f_* {\mathbf{Q}}[-q] $.

    Instead $ {\mathbf{R}}f_* {\mathbf{Q}} $ decomposes (in a weaker sense) into perverse sheaves.

    Decomposition theorem: Let $ f: X \rightarrow Y $ be a projective map of complex algebraic varieties, with $ X $ smooth, then $ \mathbb{R} f_* \mathbb{Q} $ decomposes into a sum of translates of simple perverse sheaves.

- Motivate $ {}_{\mathcal{D}}{\mathsf{Mod}} $.

    Generalize integrable connections.

    Coherent such correspond to a system of PDEs.

    A PVHS gives a regular holonomic $    {}_{\mathcal{D}}{\mathsf{Mod}}  $.

- Define $ {}_{\mathcal{D}}{\mathsf{Mod}} $.

    For $ X $, let $ D_X $ be the sheaf of algebras of holomorphic differential operators.

    For $ X = {\mathbf{A}}^n $, $ H^0(D_X) = W^n $ the Weyl algebra: $ \left\langle{x_1,\cdots, x_n, {\partial}_1,\cdots, {\partial}_n}\right\rangle/\left\langle{\left[x_i, x_j\right]=\left[\partial_i, \partial_j\right]=0,\left[\partial_i, x_j\right]=\delta_{i j}}\right\rangle $.

    $ M\in   {}_{\mathcal D_X}{\mathsf{Mod}} \subset   {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $ if $ M\in {\mathsf{Sh}}(X; {\mathsf{Ab}}{\mathsf{Grp}}) $ where $ D_X\curvearrowright M $ from the left.

- Give an example of $ M\in {}_{\mathcal{D}}{\mathsf{Mod}} $.

    $ (V, \nabla) $ an integrable vector bundle, with $ {\partial}_i .v \coloneqq\nabla_{{\partial}_i}(v) $.

    Need integrability to get $ [{\partial}_i {\partial}_j] = 0 $.

- What is a perverse sheaf?

    An object of $ D_{{\operatorname{const.}}}^b(X,   {}_{ {\mathbf{C}}}{\mathsf{Mod}}) $ (complexes of sheaves of vector spaces with bounded constructible cohomology) isomorphic to $ \mathrm{RH}(M) $ for some $ M\in    {}_{\mathcal{D}}{\mathsf{Mod}} ^{\text{hol}} $ and $ \mathrm{RH}({-}) \coloneqq\mathop{\mathrm{\mathbb{R}Hom}}({-}, {\mathcal{O}}_X) $ is the functor inducing the Riemann-Hilbert equivalence.

- Motivate the sheaves $ \mathrm{IC}(L) $ for a local system $ L $.

    For singular spaces, only allow chains which meet the singular strata with appropriate codimensions.

    Always a perverse sheaf.

- What is Saito's theorem?

    For $ f:X\to Y $ projective, $ {\mathbf{R}}f_* K $ decomposes into a sum of IC complexes associated to PVHS when $ K $ is in a certain subcategory of regular holonomic $    {}_{\mathcal{D}}{\mathsf{Mod}}  $.

- What is the significant of the weight filtration?

    $ {\mathsf{gr}\,}_\ell W_* $ carries a pure HS of weight $ \ell $, so looks like $ H^\ell $ of a smooth projective variety.

- Discuss VHSs.

    For $ f:X\to Y $, suppose $ H^k(X_y; {\mathbf{C}}) $ carries a filtration

    Organize $ \left\{{H^k(X_y; {\mathbf{C}})}\right\}_{y\in Y} $ into a local system.

    Tensor with functions on the base to get a flat bundle $ (V, \nabla) $/

    Filtrations organize into sub-bundles.

- What is the monodromy theorem for VHSs?

    For $ V $ a PVHS over $ \mathbb{D}^\circ $, lift via $ \pi: {\mathbb{H}}\to \mathbb{D} $ to get a monodromy morphism $ \rho: \pi_1(\mathbb{D}^\circ) \to {\operatorname{O}}(H^0({\mathbb{H}}; \pi^* V)) $ with the form $ I $.

    Theorem: the eigenvalues of $ T\coloneqq\rho(1) $ are of the form $ \zeta_n $ for some $ n $, and in particular $ {\left\lvert {\lambda} \right\rvert} = 1 $.

    $ T $ has Jordan blocks of size at most $ d\coloneqq\max\left\{{{\left\lvert {p-q} \right\rvert}{~\mathrel{\Big\vert}~}h^{p, q}\neq 0}\right\} $.
