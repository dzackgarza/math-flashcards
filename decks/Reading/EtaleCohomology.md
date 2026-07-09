---
title: "Reading::EtaleCohomology"
---

- Is an isogeny etale?

    Not always

- What are some examples of etale morphisms?

    $ \cdot n $ on an elliptic curve if $ n $ is invertible in the base field.

    $ t\mapsto t^m $ as a map $ {\mathbf{G}}_m{\circlearrowleft} $ if $ m $ is prime to the characteristic.

    $ {\mathbf{G}}_m\hookrightarrow{\mathbf{A}}^1 $: lfp since $ k[t, t^{-1}] = k[t][t^{-1}] $, flat since a Zariski open embedding, and $ \Omega^1_{{\mathbf{A}}^1/{\mathbf{G}}_m} = 0 $ for the same reason.

    Any Zariski open embedding

- Give an example of an etale morphism that is not finite onto its image.

    $ t\mapsto t^2 $ on $ {\mathbf{G}}_m\setminus\left\{{ 1 }\right\}\to {\mathbf{G}}_m $, not proper so not finite etale.

- Give an example of a non-etale morphism

    The normalization of $ k[x,y]/xy $, since it is not flat.

- Give an example of a finite flat map that is not etale

    $ t\mapsto t^2 $ on $ {\mathbf{A}}^1{\circlearrowleft} $ since it's ramified at zero: $ \Omega^1_f = k[t]\,dt/d(t^2) $ but $ 2t\,dt $ doesn't generate $ k[t]\,dt $. Not the relative differentials are torsion.

- Give an example of a morphism that is not etale, but is finite flat where $ \Omega^1_{X/Y} $ is not torsion?

    Take the relative Frobenius $ \operatorname{Frob}:{\mathbf{A}}^1\to {\mathbf{A}}^1 $ over $ { \mathbf{F} }_p $, then $ \Omega^1_{\operatorname{Frob}} = k[t]\,dt/d(t^p) = k[t]\,dt $ which is a line bundle and thus not torsion.

- Where is a map $ F:{\mathbf{A}}^m{\circlearrowleft} $ etale?

    $ F $ is given by $ f_1,\cdots, f_n $, and the etale locus is where $ \operatorname{Jac}_f $ is a unit.

- What is a formally etale morphism?

    Uniqueness of lifts through nilpotent quotients: for $ I $ nilpotent,

    Idea: tangent vectors lift

- Discuss the image of a flat morphism.

    Always open.

- What are the preservation properties of etale morphisms?

    Any open immersion is etale

    Compositions of etale are etale

    Base change of etale are etale

    2 out of 3 property: $ \phi \circ \psi, \phi $ etale $ \implies \psi $ etale.

- What is a site?

    $ \left\{{X_\alpha\to X}\right\}\rightrightarrows X $ in $ \mathsf{C} $ a covering family where

    Intersections exist: $ X_\alpha  \underset{\scriptscriptstyle {X} }{\times} Y $ exists in $ \mathsf{C} $ for any $ Y\to X $

    Intersecting with a cover is a cover: $ \left\{{X_\alpha \underset{\scriptscriptstyle {X} }{\times} Y}\right\}\rightrightarrows Y $.

    Closed under compositions: if $ \left\{{X_{\alpha\beta} \to X_\alpha}\right\}_{\alpha, \beta} \rightrightarrows X_\alpha $ then $ \left\{{X_{\alpha_\beta} \to X_\alpha \to X}\right\}_{\alpha, \beta} \rightrightarrows X $.

    Isos are always covers.

- What are the small and big etale sites?

    **Small**: $ X_\text{ét}\subset {\mathsf{Sch}}_{/ {X}} $ consisting of all etale morphisms over $ X $, and families $ \left\{{f_\alpha}\right\} $ cover if $ \cup\operatorname{im}f_\alpha = X $.

    **Big**: $ X_\text{Ét}= {\mathsf{Sch}}_{/ {X}} $ all schems over $ X $ where covering families $ f_\alpha $ all etale with $ \cup\operatorname{im}f_\alpha = X $.

- What is the fppf topology?

    $ X_{\operatorname{fppf}}\subset {\mathsf{Sch}}_{/ {X}} $ with faithfuly flat and finite presentation structure morphisms, covers are covers as in $ X_\text{ét} $.

- What are $ X_{\mathrm{zar}} $ and $ X_{\mathrm{Zar}} $?

    Small: the site associated to $ {\left\lvert {X} \right\rvert}\in{\mathsf{Top}} $.

    Big: $ X_{\mathrm{Zar}}= {\mathsf{Sch}}_{/ {X}} $ with Zariski-open embeddings and jointly surjective images.

- What is a sheaf on a site?

    $ F\in {\mathsf{Fun}}(\mathsf{C}, \mathsf{D}) $ where $ F(U) \hookrightarrow\prod_i F(U_i) \rightrightarrows\prod_{i, j} F(U_{ij}) $ is an equalizer for all covering families.

    Exactness in the middle is gluing, exactness at the beginning is uniqueness.

    So $ F(U) = \lim \prod F(U_i) \twoheadrightarrow\prod F(U_{ij}) $.

- Give an example of a sheaf on $ X_\text{Ét} $

    Any representable functor.

    $ \mu_n $, since represented by $ k[t]/t^n-1 $ with sections $ U\mapsto \left\{{f\in H^0({\mathcal{O}}_U) {~\mathrel{\Big\vert}~}f^n=1}\right\} $.

    $ U\mapsto H^0({\mathcal{O}}_U) $, since it's represented by $ {\mathbf{A}}^1_{/ {X}} $.

    $ \underline{C_\ell} $ represented by the $ C_\ell  \underset{\scriptscriptstyle {k} }{\times} X $ where $ C_\ell $ is the constant group scheme, so the underlying set is $ X{ {}^{ \scriptscriptstyle\coprod^{\ell} }  } $. This has sections $ U\mapsto {\mathsf{Top}}({\left\lvert {U} \right\rvert}, C_\ell) $.

    $ {\mathbf{G}}_m $ represented by $ {\mathbf{G}}_{m_{/ {X}}} = \operatorname{Spec}{\mathbf{Z}}[t, t^{-1}] \underset{\scriptscriptstyle {{\mathbf{Z}}} }{\times} X $, sending $ U\mapsto H^0({\mathcal{O}}_U)^{\times} $.

    $ {\mathbf{P}}^n $ represented by $ \mathop{\mathrm{Hom}}({-}, {\mathbf{P}}^n_{/ {X}}) $, written as a functor sending $ U $ to $ {\mathcal{L}}\in \operatorname{Pic}(U) $ with $ f_U: {\mathcal{O}}(U){ {}^{ \scriptscriptstyle\oplus^{n} }  } \twoheadrightarrow{\mathcal{L}} $.

- What is a morphism of sites?

    $ f\in \mathop{\mathrm{Hom}}(T_1, T_2) \iff f\in {\mathsf{Fun}}(T_2, T_1) $ which preserves fiber products and covering families.

    Compare to $ f\in {\mathsf{Top}}(X, Y) $ inducing $ f: {\mathsf{Open}}(Y)\to {\mathsf{Open}}(X) $ where $ U\mapsto f^{-1}(U) $.

- How are the various sites for a scheme related?

    $ X_{\operatorname{fppf}}\to X_\text{Ét}\to X_\text{ét}\to X_{\mathrm{zar}} $.

- Give examples of sheaves on $ X_{\operatorname{fppf}} $

    $ {\mathsf{Sch}}_{/ {X}}({-}, Y) $ for any $ Y\in {\mathsf{Sch}}_{/ {X}} $.

    $ (Z\xrightarrow{f} X) \mapsto H^0(Z, f^* {\mathcal{F}}) $ for any $ {\mathcal{F}}\in {\mathsf{Coh}}(X) $.

- What is $ {\operatorname{fpqc}} $?

    Finitely presented and quasicompact.

- What is descent data for $ {\mathcal{F}}\in {\mathsf{QCoh}}(U_{/ {X}}) $?

    $ {\mathcal{F}}\in {\mathsf{QCoh}}(U) $ and $ f: U\to X $

    Gluing data: $ \mathop{\mathrm{proj}}_1^* {\mathcal{F}}\underset{\phi}{ { \, \xrightarrow{\sim}\, }} \mathop{\mathrm{proj}}_2^* {\mathcal{F}} $ where $ \mathop{\mathrm{proj}}_i: U \underset{\scriptscriptstyle {X} }{\times} U\to U $.

    Cocyle condition: for $ \mathop{\mathrm{proj}}_{ij}U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{3} }  }\to U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{2} }  } $, $ \mathop{\mathrm{proj}}_{23}^* \phi \circ \mathop{\mathrm{proj}}_{12}^* \phi = \mathop{\mathrm{proj}}_{13}^*\phi $.

- What is effective descent?

    The pullback $ f^* $ induces an equivalence of categories.

- What is descent for $ {\mathsf{QCoh}}(X) $?

    If $ U\to X $ is fppf, there is an equivalence of categories between $ {\mathsf{QCoh}}(X) $ and descent data on $ U_{/ {X}} $ induced by $ f^* $, where $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $ is sent to $ f^* {\mathcal{F}}\in {\mathsf{QCoh}}(U) $ with descent data $ (f\circ \mathop{\mathrm{proj}}_1)^* {\mathcal{F}} { \, \xrightarrow{\sim}\, }(f\circ \mathop{\mathrm{proj}}_2)^*{\mathcal{F}} $ an isomorphism on $ U \underset{\scriptscriptstyle {X} }{\times} U $ induced by pulling back the identity.

- What is a quasicoherent sheaf on $ \operatorname{Spec}L $ for $ L $ a field?

    An $ L{\hbox{-}} $vector space.

- What is the sheaf-theoretic definition of a scheme?

    A sheaf on the Zariski site which is locally representable.

- What is the sheaf-theoretic definition of an algebraic space?

    A sheaf on the Zariski site which are is not representable by schemes but are locally representable in the etale topology.

- Give a sufficient condition for the Amitsur complex to be exact.

    $ R\to S $ faithfully flat, $ N\in   {}_{R}{\mathsf{Mod}} $, and forming the complex from $ ({-})\otimes_R S $.

- What is fppf descent for $ {\mathsf{QCoh}}(X) $?

    If $ f: U\to X $ is an fppf cover, then $ f^*: {\mathsf{QCoh}}(X)  { \, \xrightarrow{\sim}\, }\mathsf{Descent}(U_{/ {X}}) $ is an equivalence of categories.

- For $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $, describe $ {\mathcal{F}}^\text{ét} $.

    $ {\mathcal{F}}^\text{ét}(U\xrightarrow{\pi} X) \coloneqq\pi^* {\mathcal{F}}(U) $.

- Why is the presheaf $ {\mathcal{F}}^\text{ét} $ a sheaf?

    For $ U\to V $ an etale cover, need $ {\mathcal{F}}(V) \to {\mathcal{F}}(U) \rightrightarrows{\mathcal{F}}(U \underset{\scriptscriptstyle {V} }{\times} U) $.

    Use the equalizer $ \mathop{\mathrm{Hom}}_X({\mathcal{F}}_1, {\mathcal{F}}_2) \to \mathop{\mathrm{Hom}}_U(f^* {\mathcal{F}}_1, f^* {\mathcal{F}}_2) \rightrightarrows\mathop{\mathrm{Hom}}_{U \underset{\scriptscriptstyle {X} }{\times} U}(\mathop{\mathrm{proj}}_1 f^* {\mathcal{F}}_1, \mathop{\mathrm{proj}}_1 f^* {\mathcal{F}}_2) $ with $ {\mathcal{F}}_2 = {\mathcal{F}}, {\mathcal{F}}_1 = {\mathcal{O}} $.

- Describe $ {\mathcal{O}}_X^\text{ét} $.

    $ U\to X $ an etale cover maps to $ H^0(U; {\mathcal{O}}_U) $.

- Describe faithfully flat descent along $ \operatorname{Frob}: X\to X^{(p)} $ over $ { \mathbf{F} }_p $.

    Vector bundles on $ X^{(p)} $ are equivalent to descent date for vector bundles on $ X^{(p)} $, described as vector bundles $ {\mathcal{E}} $ on $ X $ with a flat connection $ \nabla:{\mathcal{E}}\to {\mathcal{E}}\otimes\Omega^1_{X} $ with $ p{\hbox{-}} $curvature zero.

- What is an algebraic space?

    Descent data relative to an etale cover $ U_{/ {X}} $.

- What is a polarized scheme?

    $ (X, {\mathcal{L}}) $ a scheme with an ample line bundle.

- What is an etale cover of $ \operatorname{Spec}k $?

    $ Y \coloneqq{\textstyle\coprod}_{i\in I} \operatorname{Spec}k $, corresponding to an etale $ k{\hbox{-}} $algebra.

- Describe $ {\mathsf{Sh}}(\operatorname{Spec}k) $ for $ k={ \overline{k} } $.

    $ {\mathsf{Sh}}(\operatorname{Spec}k) = {\mathsf{Set}} $.

- What is the (etale) skyscraper sheaf for $ {\mathcal{F}}\in {\mathsf{Sh}}(\operatorname{Spec}k) $?

    For $ \overline{x} = \operatorname{Spec}k \xhookrightarrow{\iota_{\overline{x}}} X $, take $ (\iota_{\overline{x}})_* {\mathcal{F}}(U\to X) {\mathcal{F}}(U \underset{\scriptscriptstyle {X} }{\times}\overline{x}) = {\mathcal{F}}({\textstyle\coprod}_i \operatorname{Spec}k) = \prod_i {\mathcal{F}}(\operatorname{Spec}k) $ where $ i\in I $ with $ {\sharp}I $ the number of preimages of $ \overline{x} $.

- What is the pullback of $ {\mathcal{F}}\in {\mathsf{Sh}}(X_\text{ét}) $ to a geometric point $ \overline{x} $?

    $ {\mathcal{F}}_{\overline{x}} = \iota_{\overline{x}}^*{\mathcal{F}}=\colim_{(U, \overline{u})} {\mathcal{F}}(U) $ where $ \overline{u}\to U $ is a cartesian over $ \overline{x}\to X $ and $ U\to X $ is etale.

- What is the stalk of an etale sheaf $ {\mathcal{F}} $?

    $ {\mathcal{F}}_{\overline{x}} \coloneqq(\iota_{\overline{x}})^* {\mathcal{F}} $, desribed as a colimit over pointed etale covers of $ \overline{x}\to X $.

- What is $ (\iota_{\overline{x}})^*{\mathcal{O}}_X^\text{ét} $?

    The strict henselization $ {\mathcal{O}}_{X, x}^{\mathrm{sh}} $ of the local ring at $ \overline{x} $.

- What is a Henselian ring? Strictly Henselian?

    Where Hensel's lemma is true: given a monic polynomial that factors in the residue field, that factorization lifts to the entire ring.

    Strict: Henselian with algebraically closed residue field.

- Show that $ {\mathcal{F}}\twoheadrightarrow{\mathcal{G}}\implies {\mathcal{F}}_{x} \twoheadrightarrow{\mathcal{G}}_x $.

    If not, let $ \Lambda = \operatorname{coker}({\mathcal{F}}_x \to {\mathcal{G}}_x) \neq 0 $ at an $ x $ where it fails, then let $ {\mathcal{H}}\coloneqq(\iota_x)_* \Lambda $ be the skyscraper sheaf.

    Get an equalizer $ {\mathcal{F}}\to {\mathcal{G}}\rightrightarrows^{0}_f {\mathcal{H}} $ where $ f $ sends a section to its stalk; the composition is zero, forcing $ \Lambda = 0 $, a contradiction.

- Describe global sections as a pushforward

    Let $ \pi:X\to \operatorname{Spec}k $ be the structure map, then if $ k={ \overline{k} } $ one has $ H^0(\operatorname{Spec}k; \pi_* {\mathcal{F}}) = H^0(X; {\mathcal{F}}) $.

- What is the espace etale for $ {\mathcal{F}} $?

    Write $ \text{Ét}({\mathcal{F}}) \coloneqq\prod_{\overline{x}}(\iota_{\overline{x}})_*{\mathcal{F}}_{\overline{x}} $ where $ \overline{x} $ is a geometric point lying over every $ x\in X $.

    Define $ {\mathcal{F}}^a \leq \text{Ét}({\mathcal{F}}) $ the subsheaf generated by $ {\mathcal{F}} $, where $ {\mathcal{F}}^a(U) $ are sections $ s\in \text{Ét}({\mathcal{F}})(U) $ where are locally in the image of the natural map $ {\mathcal{F}}\to \text{Ét}({\mathcal{F}}) $ sending sections to their germs at all points.

- When do colimits exist in $ \underset{ \mathsf{pre}} {\mathsf{Sh}}(\mathsf{C}, \mathsf{D}) $?

    A sufficient condition: colimits exist in $ \mathsf{D} $, since you can compute them pointwise.

- Why do colimits exist in $ {\mathsf{Sh}}(X_\text{ét}) $?

    Presheaves over cocomplete categories are cocomplete, and LAPC (left adjoints preserve colimits, left adjoints are easy to map *out* of).

- Discuss adjointness of sheafification.

    Left adjoint to the forgetful functor $ {\mathsf{Sh}}(X_\text{ét})\to  \underset{ \mathsf{pre}} {\mathsf{Sh}}(X_\text{ét}) $ (left adoints are a mapping out property).

- Why is $ {\mathsf{Sh}}(X_\text{ét}) $ abelian?

    Limits: computed pointwise, over a complete category

    Cokernels: a colimit.

    $ \operatorname{im}= \operatorname{coim} $ can be checked on stalks.

- Characterize injective objects in $ {}_{{\mathbf{Z}}}{\mathsf{Mod}} $.

    Divisible groups. Generally need Baer's criterion.

- How do you map into or out of a product?

    Into: map into each component.

- Describe pullbacks in terms of homs for representable functors.

    If $ {\mathcal{F}}= \mathop{\mathrm{Hom}}_X({-}, Z) $, then $ f^* {\mathcal{F}}= \mathop{\mathrm{Hom}}_Y({-}, Y \underset{\scriptscriptstyle {X} }{\times} Z) $.

- When does Cech cohomology compute etale cohomology?

    If $ X $ is qc and every finite subset is contained in an affine, e.g. if $ X $ is quasiprojective.

- Write global sections as a hom and cohomology as an ext

    $ {{\Gamma}\qty{X;{\mathcal{F}}} } = {\mathsf{Sh}}(X)(\underline{{\mathbf{Z}}}\to {\mathcal{F}}) $, so $ H^i({\mathcal{F}}) =  \operatorname{Ext}_{{\mathsf{Sh}}(X)}(\underline{{\mathbf{Z}}}, {\mathcal{F}}) $.

    For $ {\mathcal{F}}\in    {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, $ {{\Gamma}\qty{X;{\mathcal{F}}} } = {\mathsf{QCoh}}(X)({\mathcal{O}}_X, {\mathcal{F}}) $.

- What is $ H^*_\text{ét}({\mathbf{P}}^n; {\mathcal{O}}) $?

    $ k\cdot t^0 $.

- What is $ H^*(X; \underline{{ \mathbf{F} }_p}) $ for $ X\in {\mathsf{Sch}}_{/ {{ \mathbf{F} }_p}} $ quasiprojective?

    Use $ {\mathbf{G}}_a \coloneqq\mathop{\mathrm{Hom}}({-}, {\mathbf{A}}^1) $ where $ U\mapsto {\mathcal{O}}_U(U) $ and the Artin-Schreir exact sequence

    $$\underline{{ \mathbf{F} }_p} \hookrightarrow{\mathbf{G}}_a  \xrightarrow[]{x^p-x} { \mathrel{\mkern-16mu}\rightarrow }\, {\mathbf{G}}_a$$

- Is $ {\mathbf{G}}_a \xrightarrow{x^p-x}{\mathbf{G}}_a $ an etale morphism over $ { \mathbf{F} }_p $?

    Yes: $ {\frac{\partial }{\partial x}\,}(x^p-x) = -1 $ which is invertible.

- Why is $ H_\text{ét}(X; { \mathbf{F} }_p) $ poorly behaved?

    Expect a functorial assignment to $   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fg}} $, but e.g. even on affines on gets $ H^0(X;{ \mathbf{F} }_p)\hookrightarrow{\mathcal{O}}_X(X) \xrightarrow{\mathrm{AS}: t^p-t} {\mathcal{O}}_X(X)\twoheadrightarrow H^1(X; { \mathbf{F} }_p) $ where $ \operatorname{coker}\mathrm{AS} $ is not finitely generated.

- Give an example of an etale cover of $ \operatorname{Spec}k $.

    $ \operatorname{Spec}L $ where $ L/k $ is a separable extension.

- What is a $ G{\hbox{-}} $torsor?

    Idea: $ {\mathcal{F}}\in {\mathsf{Sh}}(X_\text{ét},{\mathsf{Set}}) $ where $ G\curvearrowright{\mathcal{F}} $ simply transitively on every fiber.

    Precisely: for $ G\in {\mathsf{Sh}}(X, {\mathsf{Grp}}) $ and $ {\mathcal{F}}\in {\mathsf{Sh}}(X, {\mathsf{Set}}) $, an action $ G\times {\mathcal{F}}\xrightarrow{\alpha} {\mathcal{F}} $ which is simply transitive, i.e. an isomorphism $ G\times {\mathcal{F}}\xrightarrow{\alpha \times \mathop{\mathrm{proj}}_2}{\mathcal{F}}\times {\mathcal{F}} $

- What is $ A\times B $ in terms of fiber products?

    $ A \underset{\scriptscriptstyle {T} }{\times} B $ where $ T $ is the terminal object.

- Describe $ {\mathsf{G}{\hbox{-}}\mathsf{Torsors}} $ for $ G\in {\mathsf{Fin}}{\mathsf{Grp}} $.

    A finite etale cover with Galois group $ G $.

    E.g. for $ X $ a smooth curve: an extension $ L/K(X) $ with $ { \mathsf{Gal}}(L/K(X)) = G $ which is everywhere unramified.

- What is the representing object for $ {\mathbf{G}}_m $?

    $ \mathop{\mathrm{Hom}}_X({-}, \operatorname{Spec}k[t, t^{-1}]) $.

- Describe $ {\mathsf{{\mathbf{G}}_m}{\hbox{-}}\mathsf{Torsors}} $

    A line bundle $ {\mathcal{L}}\setminus\left\{{0}\right\} $ with the zero section deleted.

    Send $ {\mathcal{L}}\to \underline{ \operatorname{Spec}} _X \bigoplus_{n\in {\mathbf{Z}}}{\mathcal{L}}{ {}^{ \scriptstyle\otimes_{}^{n} }  } $.

- Descibre $ {\mathsf{\operatorname{GL}_n}{\hbox{-}}\mathsf{Torsors}} $?

    Vector bundles of rank $ n $, sending a bundle $ {\mathcal{E}}\to \mathop{\mathrm{Frame}}({\mathcal{E}}) \coloneqq\mathop{\mathrm{Isom}}_{X_\text{ét}}({\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  }, {\mathcal{E}}) $ with inverse $ T\mapsto (T\times {\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  })/ \operatorname{GL}_n $, using that $ \operatorname{GL}_n = \underline{\mathop{\mathrm{Aut}}}({\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  }) $.

- What is a splitting of a $ G{\hbox{-}} $torsor?

    Locally trivial: $ T\in{\mathsf{G}{\hbox{-}}\mathsf{Torsors}} $ is split by an etale cover $ U\to X $ if $ { \left.{{T}} \right|_{{U}} }  { \, \xrightarrow{\sim}\, }{ \left.{{G}} \right|_{{U}} } $ as a torsor.

- Describe $ \mathop{\mathrm{Aut}}(T) $ for $ T\in{\mathsf{G}{\hbox{-}}\mathsf{Torsors}} $ trivial.

    An element of $ G $ -- look at $ G{\hbox{-}} $torsors over a point.

- Describe $ H^1_\text{ét}(\tau; {\mathcal{F}}) $ for $ \tau $ a site.

    Locally trivial $ {\mathcal{F}}{\hbox{-}} $torsors.

- What is Hilbert 90? How is it proved?

    $${\check{H}}^1(X_{\mathrm{zar}}; \underline{\operatorname{GL}_n})  { \, \xrightarrow{\sim}\, }{\check{H}}^1(X_\text{ét}; \underline{\operatorname{GL}_n})  { \, \xrightarrow{\sim}\, }{\check{H}}^1(X_{\operatorname{fppf}}; \underline{\operatorname{GL}_n})$$

    Use bijection with locally split $ \operatorname{GL}_n{\hbox{-}} $torsors, use this to get descent data for a vector bundle, use fppf descent.

    Alternative statement: $ H^1({ \mathsf{Gal}}(k^s/k), \overline{k}^{\times}) $.

- Describe how to parameterize $ n{\hbox{-}} $dimensional vector bundles on $ X $.

    $ H^1_\text{ét}(X_\tau; \operatorname{GL}_n) $ where $ \tau $ is any site appearing in Hilbert 90.

- Are all $ G{\hbox{-}} $torsors represented by an $ X{\hbox{-}} $scheme?

    Yes.

- If $ T\in{\mathsf{G}{\hbox{-}}\mathsf{Torsors}} $, does fppf-locally trivial imply etale locally trivial?

    No in general, yes if $ G $ is smooth.

    Take $ \ker \operatorname{Frob} $ on $ {\mathbf{G}}_a $ or $ {\mathbf{G}}_m $, so $ \alpha_p $ or $ \mu_p $, in characteristic $ p $.

    In general, any positive dimensional affine group scheme.

- What is $ H^1_\text{ét}(\operatorname{Spec}k; {\mathbf{G}}_m)? $

    Line bundles on a point are trivial: $ H^1_\text{ét}(\operatorname{Spec}k, {\mathbf{G}}_m) = 0 = H^1({ \mathsf{Gal}}(k^s/k), \overline{k}^{\times}) $.

- What is $ H^1(X_\text{ét}; {\mathbf{G}}_m) $?

    $ \operatorname{Pic}(X) $.

- What is $ H^1(X_\text{ét}; \mu_\ell) $ with $ \ell $ invertible in $ X $.

    Use the Kummer SES $ \mu_\ell \hookrightarrow{\mathbf{G}}_m  \xrightarrow[]{z\mapsto z^\ell} { \mathrel{\mkern-16mu}\rightarrow }\,  {\mathbf{G}}_m $.

- How do you explicitly write down a cover corresponding to an element in $ H^1(X_\text{ét}; { \mathbf{F} }_p) $?

    Write $ H^1 = \operatorname{coker}({\mathcal{O}}_X \xrightarrow{x^p - x}{\mathcal{O}}_X) \ni f $ and take $ Y = \left\{{y^p-y = f}\right\} $.

- How do you explicitly write down a cover corresponding to an element in $ H^1(X_\text{ét}; \mu_\ell) $?

    Write $ H^1 = \operatorname{coker}({\mathcal{O}}_X^{\times}\xrightarrow{x\mapsto x^\ell}{\mathcal{O}}_X^{\times})\ni f $ and take $ Y = \left\{{z^\ell = f}\right\} $.

    Needs $ \operatorname{Pic}(X) = 0 $.

- Describe $ H_\text{ét}(X; {\mathbf{G}}_m) $ for $ X $ a smooth curve over $ k={ \overline{k} } $.

    $ {\mathcal{O}}_X^{\times}+ \operatorname{Pic}(X) t $.

- Describe $ H_\text{ét}(X; \mu_\ell) $ for $ X $ a smooth proper curve over $ k={ \overline{k} } $.

    $ C_{\ell^n} + \operatorname{Pic}[\ell^n]t + C_\ell t^2 $ where $ \operatorname{Pic}(\ell^n) \cong C_{\ell^n}^{2g} $, using the Kummer sequence and that $ \operatorname{Pic}^0(X) \cong \operatorname{Jac}(X) $ is divisible and $ {\operatorname{NS}}(X) = {\mathbf{Z}} $.

- For $ f\in {\mathsf{Sch}}(X, Y) $, how is $ f_* \in [{\mathsf{Sh}}(X_\text{ét}), {\mathsf{Sh}}(Y_\text{ét})] $ defined?

    $ f_*{\mathcal{F}}(U\to X)\coloneqq{\mathcal{F}}(U \underset{\scriptscriptstyle {Y} }{\times} X) $.

- What is the interpretation of $ {\mathbf{R}}^* f_* $?

    Cohomology of fibers, sometimes -- obstructed by non-commuting with base change.

    Sheafification of $ V\mapsto H^i(f^{-1}(V); {\mathcal{F}}) $.

- Give an example where $ \tau_{\geq 1}{\mathbf{R}}f_* = 0 $.

    $ f $ a finite morphism, e.g. a closed immersion. Show $ f_* $ is right exact by checking on stalks $ \bigoplus_{\overline{x}\in f^{-1}(\overline{y})}{\mathcal{F}}_{\overline{x}} $.

- Why does $ f_* $ preserve injectives?

    True for any functor with an exact left adjoint, here take $ f^* $, exact since filtered colimits and sheafification are exact (or check on stalks).

- What is $ H_{ \mathsf{Gal}}(k; V) $ for $ k $ a finite field and $ V\in {}_{k}{\mathsf{Mod}} $?

    $ V^G t^0 + V_G t^1 $.

- Is a sequence of presheaves exact iff exact on all sections?

    True! Just not true for sheaves.

- For $ X $ integral and $ \iota:\eta \hookrightarrow X $ a generic point, what are the stalks of $ {\mathbf{R}}\iota_* {\mathcal{F}} $?

    Write $ K_X \coloneqq\operatorname{ff}({\mathcal{O}}_X) $, use that stalks agree on sheaves vs presheaves to get

    $$\colim_{u\hookrightarrow U} H^i(U_\eta; { \left.{{{\mathcal{F}}}} \right|_{{U_\eta}} }) = H^i(K_{X, \overline{x}}; { \left.{{{\mathcal{F}}}} \right|_{{K_{X, \overline{x}}}} })$$

    at $ \overline{x}\hookrightarrow X $ a geometric point.

- What is the point pushforward SES?

    If $ \iota:\eta \hookrightarrow X $ for $ X $ a regular variety,

    $${\mathbf{G}}_m \hookrightarrow\eta_*{\mathbf{G}}_m\twoheadrightarrow\bigoplus_{Z\leq X \,\, \operatorname{codim}_X(Z) = 1} \iota_* \underline{{\mathbf{Z}}}$$

    where the last term is the divisor sheaf.

    The first map is restriction to $ \eta $, the second is taking the associated divisor.

- How is an integral domain related to all of its localizations?

    $ A = \bigcap_{p\in \operatorname{Spec}(A)^{\operatorname{ht}= 1}} A_p $.

- Define the cohomological Brauer group.

    $ \Br(X_\text{ét}; {\mathbf{G}}_m)_{\operatorname{tors}} $.

- What is $ H^i(C; {\mathbf{C}}_m) $?

    $ {\mathcal{O}}_C(C)^{\times}t^0 + \operatorname{Pic}(C) t $.

- What does $ H^1 $ classify? $ H^2 $?

    $ H^1 $: torsors. $ H^2 $: gerbes.

- What is $ \Br^\mathop{\mathrm{coh}}(X) $?

    $ H^i_\text{ét}(X; {\mathbf{G}}_m)_{\operatorname{tors}} $.

    Equivalently, $ \operatorname{im}\qty{\bigcup_n {\mathcal{P}}_n \xrightarrow{\delta} H^2_\text{ét}(X; {\mathbf{G}}_m)} $ where $ {\mathcal{P}}_n $ is the set of all etale locally trivial $ \operatorname{PGL}_n{\hbox{-}} $torsors over $ X $, which is the boundary map coming from $ {\mathbf{G}}_m\hookrightarrow\operatorname{GL}_n\twoheadrightarrow\operatorname{PGL}_n $.

- What is the interpretation of $ \delta([T]) $?

    For $ T\in H^i(X_\text{ét}; \operatorname{PGL}_n) $, the obstruction to lifting $ T $ to a $ \operatorname{GL}_n{\hbox{-}} $torsor.

    Equivalently: the Brauer class of $ T $.

- Describe how to relate $ G{\hbox{-}} $torsors and forms.

    For $ T = {\mathsf{Sh}}(X_\text{ét}, {\mathsf{Set}}) $ and $ G = \mathop{\mathrm{Aut}}(X) $, locally split $ G{\hbox{-}} $torsors $ \rightleftharpoons $ forms of $ T $.

    Forms $ F $ map to $ \mathop{\mathrm{Isom}}(F, T) $.

    Torsors $ \tau $ map to the sheaf quotient $ (T\times \tau)/G $.

- What is a Severi-Brauer X`{\hbox{-}}`{=tex}$schemes?

    Forms of $ {\mathbf{P}}^n_X $; for $ X=\operatorname{Spec}k $ these are Severi-Brauer varieties.

- What is an Azumaya algebra?

    Forms of $ \operatorname{Mat}_{n\times n} = { \operatorname{End} }_{\mathcal{O}}({\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  }) $.

- What is $ {\mathsf{QCoh}}(X, \alpha) $?

    For $ U\to X $ an etale cover, $ \alpha\in H^0(U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{3} }  }; {\mathbf{G}}_m) $ representing $ [\alpha]\in H^2_\text{ét}(X; {\mathbf{G}}_m) $, a sheaf $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $ with an isomorphism $ \phi: \mathop{\mathrm{proj}}_1 {\mathcal{F}} { \, \xrightarrow{\sim}\, }\mathop{\mathrm{proj}}_2{\mathcal{F}} $ for $ \mathop{\mathrm{proj}}_i: U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{2} }  }\to U $ satisfying a twisted cocycle condition

    $$\pi_{23}^* \phi \circ \pi_{12}^* \phi = \alpha \cdot \pi_{13}^* \phi$$

    Morphisms are sheaf morphisms commuting with $ \phi $.

- State etale descent in terms of $ \alpha{\hbox{-}} $twisted sheaves.

    $ {\mathsf{QCoh}}(X, 1) = {\mathsf{QCoh}}(X) $ canonically.

- Describe homs, tensors, and symmetric powers on $ {\mathsf{QCoh}}(X, \alpha) $.

    $$\begin{align*}\mathop{\mathrm{Hom}}: {\mathsf{QCoh}}(X,\alpha_1) \times {\mathsf{QCoh}}(X,\alpha_2) &\to {\mathsf{QCoh}}(X,\alpha_1 \cdot \alpha_2^{-1}) \\ \otimes: {\mathsf{QCoh}}(X,\alpha_1) \times {\mathsf{QCoh}}(X,\alpha_2) &\to {\mathsf{QCoh}}(X,\alpha_1\cdot \alpha_2) \\ \operatorname{Sym}^n, \bigwedge^n: {\mathsf{QCoh}}(X,\alpha_1) &\to {\mathsf{QCoh}}(X,n \cdot \alpha_1)\end{align*}$$

- Discuss when a 2-cocycle $ [\alpha] $ for $ {\mathbf{G}}_m $ relates to Brauer classes.

    $ [\alpha]\in \Br(X) \iff \exists {\mathcal{E}} $ and $ \alpha{\hbox{-}} $twisted vector bundle.

    The forward direction corresponds to $ \delta([\alpha]) $, the reverse is projectiving a bundle to get a form of $ {\mathbf{P}}^n $.

- Why is $ \Br(X) $ a group?

    For $ \alpha_1\cdot \alpha_2 $, take $ {\mathcal{E}}_1\otimes{\mathcal{E}}_2 $ for the corresponding twisted vector bundles.

    For $ \alpha_1^{-1} $, take $ {\mathcal{E}}_1 {}^{ \vee } $.

- How can one check when $ [\alpha] $ is trivial?

    $ [\alpha] = 1 \iff \exists {\mathcal{L}} $ an $ \alpha{\hbox{-}} $twisted line bundle.

    Forward: take $ {\mathcal{L}}= {\mathcal{O}}_X $, reverse: use descent data to get $ \beta $ with $ \delta(\beta) = \alpha $.

- What does $ {\mathcal{E}} $ an $ \alpha{\hbox{-}} $twisted vector bundle of rank $ n $ correspond to in $ \Br(X) $?

    $ \alpha\in H^2(X_\text{ét}; {\mathbf{G}}_m)[n] $, $ n{\hbox{-}} $torsion.

    Proof: take $ \operatorname{det}{\mathcal{E}} $ to get an $ \alpha^n{\hbox{-}} $twisted line bundle, implies $ 1 = [\alpha^n] = [\alpha]^n $.

    Warning: $ n{\hbox{-}} $torsion elements do not generally yield rank $ n $ bundles.

- Give an example of a twisted form of $ {\mathbf{P}}^1 $.

    $ x^2+y^2+z^2 = 0 $ over $ {\mathbf{R}} $, a smooth conic with no rational points. By projection, a rational point induces an isomorphism to $ {\mathbf{P}}^1 $, and this acquires points after base-changing to $ {\mathbf{C}} $.

- What is the generator of $ \Br({\mathbf{R}}) $?

    Hamilton quaternions: central division algebra, hence Azumaya.

- How are twisted sheaves related to Severi-Brauers and Azumaya algebras?

    $ {\mathbf{P}}({\mathcal{E}}) $ is SB.

    $ { \operatorname{End} }({\mathcal{E}}) $ is Azumaya.

- What is $ \Br({ {\mathbf{Q}}_p }) $?

    $ \Br({ {\mathbf{Q}}_p }) = {\mathbf{Q}}/{\mathbf{Z}} $.

- What is the SES involving $ \Br({\mathbf{Q}}) $?

    $$\Br({\mathbf{Q}}) \hookrightarrow\bigoplus_{p\in {\operatorname{Places}}{{\mathbf{Q}}}} \Br({ {\mathbf{Q}}_p }) \twoheadrightarrow{\mathbf{Q}}/{\mathbf{Z}}$$

- What is the period-index question?

    Given $ \alpha\in \Br(X) $, what is the minimal rank of an $ \alpha{\hbox{-}} $twisted vector bundle?

    Over a field, for 2-torsion one can always find $ \operatorname{rank}{\mathcal{E}}= 2 $.
