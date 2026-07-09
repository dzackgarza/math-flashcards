---
title: "Reading::ClassFieldTheory"
---

- When is $ k[G] $ commutative?

    Iff $ G $ is commutative.

- What is $ {}_{G}{\mathsf{Mod}} $?

    $ M\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}} $ with an action $ \psi\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}(G, \mathop{\mathrm{Aut}}({\mathbf{G}}_a M)) $, so $ g(x+y) = gx+gy $ and $ (gh)x = g(hx) $.

    $ G{\hbox{-}} $equivariant morphisms, $ gf(x) = f(gx) $.

- How can you determine if a SES $ \xi\in {}_{G}{\mathsf{Mod}} $ is exact?

    Exact iff exact in $   {}_{{\mathbf{Z}}}{\mathsf{Mod}} $

- Define $ M^G $ and $ M_G $ and discuss their exactness.

    $ M^G \coloneqq\left\{{m\in M{~\mathrel{\Big\vert}~}gm=m\,\,\forall G}\right\} $: invariants, largest $ G{\hbox{-}} $trivial **submodule**. Left exact as a functor $   {}_{G}{\mathsf{Mod}}\to  {}_{{\mathbf{Z}}}{\mathsf{Mod}} $, so preserves injections.

    $ M_G \coloneqq M/\left\langle{gm-m{~\mathrel{\Big\vert}~}m\in M, g\in G}\right\rangle_{\mathbf{Z}} $: coinvariants, largest $ G{\hbox{-}} $trivial **quotient**. Right exact as a functor, so preserves surjections.

- Interpret $ H^*(G; M) $ topologically.

    $ H^*(G; {\mathbf{Z}}) = H^*(K(G, 1); {\mathbf{Z}}) $ and $ H^*(G; M) = H^*(K(G, 1); \underline{M}) $ where $ \underline{M} $ is a the corresponding local system.

- Describe the monoid ring $ R[M] $ for $ R $ a ring and $ M $ a monoid. What is its universal property?

    Free $   {}_{R}{\mathsf{Mod}} $ with basis $ \left\{{m\in M}\right\} $ with $ [m_1]\cdot [m_2] \coloneqq[m_1 m_2] $ using the monoid operation, extended bilinearly.

    $  {}_{R}  \mathsf{Alg}(R[M], B) \cong \mathsf{Mon}(M, {\mathbf{G}}_m B) $.

- What is the norm element of a finite group? Why is it important?

    $ N\coloneqq\sum_{g\in G} g\in {\mathbf{Z}}[G] $, which is $ G{\hbox{-}} $invariant.

    $ {\mathbf{Z}}[G]^G = \left\langle{N}\right\rangle_{\mathbf{Z}} $.

- What is the augmentation on $ {\mathbf{Z}}[G] $? Describe the augmentation ideal.

    $ \alpha: {\mathbf{Z}}[G]\to {\mathbf{Z}} $ where $ \sum n_g[g] \mapsto \sum n_g $, "evaluate each $ g\in G $ at the point 1".

    $ I\coloneqq\ker \alpha $ fits into a SES $ I\hookrightarrow{\mathbf{Z}}[G]\twoheadrightarrow{\mathbf{Z}}\in \zgmod $ where $ {\mathbf{Z}} $ has the trivial action.

    $ I\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{free}} $ has basis $ \left\{{[g] - [e] {~\mathrel{\Big\vert}~}g\in G}\right\} $.

- When does the augmentation SES spit? Why care?

    Only if $ G $ is trivial: a section has to send 1 to a $ G{\hbox{-}} $invariant element, which is either zero or a multiple of $ N $.

    If $ G $ is nontrivial, $ {\mathbf{Z}} $ is not projective in $ \zgmod $.

- What is Maschke's theorem?

    For $ k $ a field and $ G $ finite, TFAE:

    $ \operatorname{ch}k \nmid {\sharp}G $

    $ k[G] $ is a semisimple module, so every $ M\in \kgmod $ is projective and injective, thus all higher cohomology vanishes.

- Describe group (co)homology in terms of Tor and Ext.

    $ M^G = \zgmod({\mathbf{Z}}\to M) $

    $ M_G = {\mathbf{Z}}\otimes_{{\mathbf{Z}}[G]} M $.

- Which resolutions can be used for $ \operatorname{Tor} $ and $ \operatorname{Ext} $?

    $ \operatorname{Tor}(A, B) $: a projective resolution of either argument

    $  \operatorname{Ext}(A, B) $: a projective resolution of $ A $ or an injective resolution of $ B $.

- Interpret $ H_1(G; {\mathbf{Z}}) $.

    $ I/I^2 = G^{\operatorname{ab}} $.

- Describe $ {\mathbf{Z}}[{\mathbf{Z}}] $.

    $ {\mathbf{Z}}[{\mathbf{Z}}] = {\mathbf{Z}}[t, t^{-1}] $ the Laurent polynomial ring with $ I = \left\langle{e-1}\right\rangle $ principal corresponding to $ \left\langle{t-1}\right\rangle $, so a free rank 1 $ \zgmod $.

    UFD of Krull dimension 2.

- Describe $ H^*({\mathbf{Z}}; M) $ and $ H_*({\mathbf{Z}}; M) $.

    Use the free resolution $ {\mathbf{Z}}[G] \hookrightarrow{\mathbf{Z}}[G] \twoheadrightarrow{\mathbf{Z}} $ using $ x\mapsto x\cdot([e] - [1]) $ and the augmentation and that $ I =\left\langle{e-1}\right\rangle \cong {\mathbf{Z}}[{\mathbf{Z}}] $.

    $ H_*(G; M) = M_G + M^G t $.

    $ H^*(G; M) = M^G + M_G t $

- What is $ I $ for $ G = C_n $?

    $ I = \left\langle{\sigma - 1}\right\rangle $ where $ C_n = \left\langle{\sigma}\right\rangle_{\mathbf{Z}} $.

- What is a free resolution of $ {\mathbf{Z}} $ in $ \zgmod $ for $ G = C_n $?

    Periodic:

    $$\cdots \xrightarrow{\sigma-1}{\mathbf{Z}}[G]\xrightarrow{\cdot N} {\mathbf{Z}}[G]\xrightarrow{\sigma-1}{\mathbf{Z}}[G]\xrightarrow{{\varepsilon}}{\mathbf{Z}}\to 0$$

- What are $ H^*(C_n; M) $ and $ H_*(C_n; M) $?

    $$H_*(C_n; M) = M_G \cdot t^0 + \bigoplus_{i}M^G/NM \cdot t^{2i+1} + \bigoplus_{i} \ker N/IM \cdot t^{2i}$$

    $$H^*(C_n; M) = M^G\cdot t^0 + \bigoplus_{i} \ker N/IM \cdot t^{2i+1} + \bigoplus_{i} M^G/NM\cdot t^{2i}$$

- What are $ K({\mathbf{Z}}, 1) $ and $ K(C_2, 1) $?

    $ K({\mathbf{Z}}, 1)\simeq S^1 $.

    $ K(C_2, 1)\simeq{\mathbf{RP}}^\infty $

- What are the $ {}_{G}{\mathsf{Mod}} $ structures on $ {}_{{\mathbf{Z}}}{\mathsf{Mod}}(A, B) $ and $ A\otimes_{\mathbf{Z}}B $?

    $ g\curvearrowright\sum a_i\otimes b_i \coloneqq\sum ga_i\otimes gb_i $ the diagonal action.

    $ (g\curvearrowright f)(x) \coloneqq g.f(g^{-1}x) $ the adjoint action.

- Describe $ f\in {}_{{\mathbf{Z}}}{\mathsf{Mod}}(A, B)^G $.

    $ gf(g^{-1}x) = f(x) \implies gf(x) = f(gx) $, so $ G{\hbox{-}} $equivariance.

- Define a free $ G{\hbox{-}} $action.

    Trivial stabilizers.

- What is the standard resolution of $ {\mathbf{Z}} $ as a $ \zgmod $?

    $ P_n \coloneqq\mathsf{Free}_{  {}_{{\mathbf{Z}}}{\mathsf{Mod}}}(G{ {}^{ \scriptscriptstyle\times^{n+1} }  }) $, so $ P_0 \cong {\mathbf{Z}}[G] $ and $ \operatorname{rank}_{\mathbf{Z}}P_n = {\sharp}(G)^n $ whose differential is

    $${\left[ {g_0,\cdots, g_n} \right]}\xrightarrow{{\partial}_n} \sum_{i=0}^n (-1)^i {\left[ {g_0, \cdots, \widehat{g}_i, \cdots, g_n} \right]}$$

- Describe $ \zgmod(P_n, M) $ for $ P_\bullet \rightrightarrows{\mathbf{Z}} $ the standard resolution.

    $ \zgmod(P_n\to M) =   {}_{{\mathbf{Z}}}{\mathsf{Mod}}(P_n \to M)^G $, so $ f(g.g_0,\cdots, g.g_n) = gf(g_0,\cdots, g_n) $ for $ f: G{ {}^{ \scriptscriptstyle\times^{n+1} }  }\to M $.

- Descriibe $ Z^1(G; M) $ and $ B^1(G; M) $

    $ f\in Z^1(G; M) $ are functions $ f: G\to M $ st $ f(g_1 g_2) = f(g_1) + g_1 f(g_2) $, so twisted by $ g_1 $.

    $ f\in B^1(G; M) $ are functions where $ f(g) = ga-a $ for all $ g $ for some fixed $ a\in M $.

- What is the cocycle condition for $ Z^2(G; M) $?

    $ g_1 f(g_2, g_3) - f(g_1g_2, g_3) + f(g_1, g_2 g_3) - f(g_1, g_2) = 0 $.

- Explain how an extension $ E $ of $ G $ by $ M\in {}_{{\mathbf{Z}}}{\mathsf{Mod}} $ puts a $ {}_{G}{\mathsf{Mod}} $ structure on $ M $

    For $ M\hookrightarrow E \twoheadrightarrow G $, let $ g.m \coloneqq\tilde g m \tilde g^{-1} $ where $ \tilde g\in E $ is any lift.

- How is $ H^2(G; M) $ interpreted?

    Equivalence classes of extensions $ M\hookrightarrow E \twoheadrightarrow G $.

    The trivial element is $ M \rtimes G $ where $ M{~\trianglelefteq~}E $.

- Why is $ H^*(G; M) $ finite with $ G, M $ are finite?

    $ {\sharp}Z^n(G; M) \leq ({\sharp}M)^{{\sharp}G} < \infty $.

- Define $ \mathrm{Ind}^{H}_{G} M $ for $ M\in {}_{H}{\mathsf{Mod}} $.

    $ \mathrm{Ind}^{H}_{G}({-}) \coloneqq{\mathbf{Z}}[G]\otimes_{{\mathbf{Z}}[H]} ({-}) \in \zgmod $ acting diagonally.

- Define $ \mathrm{coInd}^{H}_{G} M $ for $ M\in {}_{H}{\mathsf{Mod}} $.

    $ \mathrm{coInd}^{H}_{G}({-}) =   {}_{{\mathbf{Z}}[H]}{\mathsf{Mod}}({\mathbf{Z}}[G], {-}) \in \zgmod $ with a funny action $ (g.f)(x) \coloneqq f(xg) $.

- What is Artin's theorem on representations of finite groups?

    For $ G\in {\mathsf{Fin}}{\mathsf{Grp}} $, any $ V\in {\mathsf{Rep}}(G)^{\mathrm{fd}}_{/ {{\mathbf{C}}}} $ is a $ {\mathbf{Q}}{\hbox{-}} $linear combinations of $ \mathrm{Ind}^{H}_{G} W $ where $ H\leq G $ is cyclic and $ W $ is a character.

- What is Brauer's theorem on representations of finite groups?

    For $ G\in {\mathsf{Fin}}{\mathsf{Grp}} $, any $ V\in {\mathsf{Rep}}(G)^{\mathrm{fd}}_{/ {{\mathbf{C}}}} $ is a $ {\mathbf{Z}}{\hbox{-}} $linear combinations of $ \mathrm{Ind}^{H}_{G} W $ where $ H\leq G $ is an elementary subgroup, so $ H\cong C\times P $ with $ C $ cyclic and $ P $ a $ p{\hbox{-}} $group, and $ W $ is a character.

- What is Artin's holomorphy conjecture?

    Every Artin $ L{\hbox{-}} $function attached to a nontrivial representaiton of a finite group has a holomorphic continuation to $ {\mathbf{C}} $.

    Shown recently for $ A_5 $ using Langlands.

    Brauer shows *meromorphic* continuation as an easy corollary of his induction theorem.

- What is Shapiro's lemma?

    For $ H\leq G $ and $ N\in   {}_{H}{\mathsf{Mod}} $,

    $$H_n(G; \mathrm{Ind}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$

    $$H^n(G; \mathrm{coInd}^{H}_{G} N)  { \, \xrightarrow{\sim}\, }H_n(H; N)$$

- What are $ \mathrm{Ind}^{{\operatorname{pt}}}_{G} A $ and $ \mathrm{coInd}^{{\operatorname{pt}}}_{G} A $?

    $ \mathrm{Ind}^{{\operatorname{pt}}}_{G} A = {\mathbf{Z}}[G]\otimes_{\mathbf{Z}}A $ and $ \mathrm{coInd}^{{\operatorname{pt}}}_{G} A =   {}_{{\mathbf{Z}}}{\mathsf{Mod}}({\mathbf{Z}}[G] \to A) $.

- What are acyclic modules for group homology?

    Induced modules: any module isomorphic to $ \mathrm{Ind}^{H}_{G} A $ for some $ H $ and $ A $.

    E.g. $ H_n(G; \mathrm{Ind}^{{\operatorname{pt}}}_{G} A) = 0 $.

- Describe how any $ M\in {}_{G}{\mathsf{Mod}} $ is surjected onto by an induced module and injects into a coinduced module.

    $ \mathrm{Ind}^{{\operatorname{pt}}}_{G}M^\mathop{\mathrm{triv}}\twoheadrightarrow M $ and $ M\hookrightarrow\mathrm{coInd}^{{\operatorname{pt}}}_{G} M^\mathop{\mathrm{triv}} $.

    The maps are $ g\otimes m\mapsto gm $ and $ x\mapsto (\cdot x) $.

- What are weakly projective/injective modules? Why care?

    Direct summands of induced/coinduced modules respectively.

    Easiest acyclic objects to use in practice, since $ M\oplus N $ acyclic implies $ M, N $ acyclic, since $ H^n(G; \bigoplus M_i) = \bigoplus_i H^n(G; M_i) $.

- What are the homological versions of Shapiro's lemma?

    $$\operatorname{Tor}_n^{{\mathbf{Z}}[H]}(M, N)  { \, \xrightarrow{\sim}\, }\operatorname{Tor}_n^{{\mathbf{Z}}[G]}(M, \mathrm{Ind}^{H}_{G} N)$$

    $$ \operatorname{Ext}^n_{{\mathbf{Z}}[H]}(M, N)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{{\mathbf{Z}}[G]}(M, \mathrm{coInd}^{H}_{G} N)$$

    $$ \operatorname{Ext}^n_{{\mathbf{Z}}[H]}(N, M)  { \, \xrightarrow{\sim}\, } \operatorname{Ext}^n_{{\mathbf{Z}}[G]}(\mathrm{Ind}^{H}_{G} N, M)$$

- What is the adjunction induced by $ f\in \mathsf{CRing}(R\to S) $?

    $ (S\otimes_R({-}), \mathrm{Res}^{R}_{S}({-})) $.

    $ (\mathrm{Res}^{R}_{S} ({-}), \mathop{\mathrm{Hom}}_R(S, {-})) $.

- Summarize the adjoint relationships between restriction and (co)induction.

    $ (\mathrm{Ind}^{H}_{G}, \mathrm{Res}^{H}_{G}) $

    $ (\mathrm{Res}^{H}_{G}, \mathrm{coInd}^{H}_{G}) $.

- Compare induction vs. coinduction for finite index subgroups.

    If $ H\leq G $ is finite index, then $ \mathrm{Ind}^{H}_{G} \cong \mathrm{coInd}^{H}_{G} $.

- Discuss commuting limits with (co)homology.

    $ \colim_i H^n(G; A_i)  { \, \xrightarrow{\sim}\, }H^n(G; \colim_i A_i) $.

- Discuss how to push/pull homology under changes of group $ f: G\to G' $.

    $ H^n(G'; {-}) \to H^n(G; {-}) $ (contravariant).

- Discuss restriction and inflation.

    $ f: H\hookrightarrow G $ yields restriction $ H^n(G; M) \to H^n(H; M) $.

    $ N{~\trianglelefteq~}G $ and $ M\in   {}_{G}{\mathsf{Mod}} $ yields $ M^N\in   {}_{G/N}{\mathsf{Mod}} $ and inflation $ H^n(G/N; M^N) \to H^n(G; M) $.

- When do functors preserve injectives/projectives?

    Has an exact left adjoint $ \implies $ preserves injectives.

    Has an exact right adjoint $ \implies $ preserves projectives.

- Characterize projectives/injectives using Hom.

    $ \mathop{\mathrm{Hom}}(P, {-})\iff $projective

    $ \mathop{\mathrm{Hom}}({-}, I) \iff $injective

- What is the inflation-restriction exact sequence?

    $$H^1(G/H; A^H) \xhookrightarrow{\mathrm{Inf}} H^1(G; A) \xrightarrow{\mathrm{Res}} H^1(H; A)^{G/H} \longrightarrow H^2(G/H; A^H) \xrightarrow{\mathrm{Inf}} H^2(G/H; A^H) \to H^2(G; A)$$

- What is restriction? What is its important property?

    $ \mathop{\mathrm{coRes}}: H^*(H; N) \to H^*(G; N) $ for $ H\leq G $ finite index.

    Satisfies $ \mathop{\mathrm{coRes}}\circ \operatorname{res}= \cdot n $ where $ n = [G:H] $.

- What is the explicit map for corestriction in degree $ n=0 $?

    Sometimes called trace or norm

    $ \mathop{\mathrm{coRes}}: M^H \to M^G $ where $ x\mapsto \qty{ \sum_{g\in G/H}[g]}x $.

- Discuss $ H^*(G; M) $ and $ H_*(G; M) $ for $ G $ finite cycle.

    $ H^{2n}(G; M) \cong H_{2n+1}(G; M) = M^G / NM $ for $ N $ the norm

    $ H^{2n+1}(G; M) \cong H_{2n}(G; M) = (\ker N)/IM $ for $ I $ the augmentation ideal.

    Except at $ n=0 $, there $ H^0(G; M) = M^G $ and $ H_0(G; M) = M/IM $.

    So higher $ H^n $ are quotients of $ H^0 $ and higher $ H_n $ are subs of $ H_0 $.

- Define Tate cohomology:

    Set $ \tilde H^0 (G; M)\coloneqq M^G/NM $ and $ \tilde H_0(G; M) \coloneqq(\ker N)/ IM $

    Set $ \widehat{H}^n(G; M) \coloneqq H^n(G; M) $ for $ n\geq 1 $.

    $ \widehat{H}^0(G; M) \coloneqq\tilde H^0(G; M) = M^G/NM $

    $ \widehat{H}^{-1}(G; M) \coloneqq\tilde H_0(G; M) = (\ker N)/ IM $

    $ \widehat{H}^{-n}(G; M) \coloneqq H_{-n-1}(G; M) $ for all $ n\leq -2 $.

- What is the LES in Tate cohomology?

    $ A\hookrightarrow B\twoheadrightarrow C $ yields a bi-infinite LES

    $$\cdots \to\widehat{H}^i(G; C) \to \widehat{H}^i(G; B) \to \widehat{H}^i(G; A)\to \widehat{H}^{i+1}(G; C)\to \cdots$$

- Discuss vanishing of $ \widehat{H}(G; M) $ for $ G\in{\mathsf{Fin}}{\mathsf{Grp}} $.

    Since induced = coinduced for finite groups, weakly injective = weakly projective, so $ \widehat{H}^i(G; M) =0 $ for all $ i $, including $ i=0 $.

- Describe how to compute $ \widehat{H}^*(G; M) $ at the cochain level.

    Take the "resolution $ X_\bullet $ where $ X_n = X_{-1-n} = {\mathbf{Z}}[G{ {}^{ \scriptscriptstyle\times^{n+1} }  }] $ with the usual $ {\partial}_n $, then $ \widehat{H}^n(G; M) =H^n(\mathop{\mathrm{Hom}}(X_n, M)^G) $.

- What is dimension shifting for $ \widehat{H} $?

    For $ A\hookrightarrow I \twoheadrightarrow B\in   {}_{G}{\mathsf{Mod}} $ with $ I $ coinduced, then $ \widehat{H}(G; B)\cong \widehat{H}^{n+1}(G; A) $.

- Describe (co)restriction for $ L/K $ a Galois extension

    Noting $ {\mathbf{G}}_a(L)^G = K $ for $ G\coloneqq{ \mathsf{Gal}}(L/K) $,

    $ \mathrm{Res}^{H}_{G}: M^G\to M^H $ corresponds to $ K\hookrightarrow L $.

    $ \mathrm{coRes}^{H}_{G}: M^H \to M^K $ corresponds to $ \operatorname{Trace}_{L/K}: L\to K $.

- Discuss finiteness for Tate cohomology.

    $ \widehat{H}^n(G; M) = \widehat{H}^n(G; M)[m] $ is always a torsion $   {}_{{\mathbf{Z}}}{\mathsf{Mod}} $, where $ m = {\sharp}G $.

    If $ M\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fg}} $ then every $ \widehat{H}^n(G; M)\in{\mathsf{Fin}}{\mathsf{Grp}} $.

    Use that a group is finite iff finitely generated and torsion.

- What is the transfer?

    For $ H\leq G $ there is an obvious map $ H^{\operatorname{ab}}\to G^{\operatorname{ab}} $, but there is also a wrong-way transfer map $ G^{\operatorname{ab}}\to H^{\operatorname{ab}} $.

- What is the Herbrand quotient?

    $ h(A) \coloneqq h^0(A)/ h^1(A) \in {\mathbf{Z}}_{\geq 0} $ where $ h^i(A) \coloneqq{\sharp}\widehat{H}^i(G; A) $.

- Discuss the Herbrand quotient.

    For $ A\hookrightarrow B\twoheadrightarrow C $ a SES, if any two $ h({-}) $ are defined then it is also defined for the third, and $ h(B) = h(A) h(C) $.

    If $ A $ is finite then $ h(A) = 1 $ since $ h^1 = h^0 $.

    If $ f\in   {}_{G}{\mathsf{Mod}}(A\to B) $ with finite kernel and cokernel then $ h(A) = h(B) $.

- What is $ \sum (-1)^i {\sharp}A_i $ for $ A_i $ in a LES in $ {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fin}} $? For vector spaces?

    $ \sum (-1)^i {\sharp}A_i = 1 $.

    For vector spaces, $ \sum (-1)^i \dim A_i = 0 $.

- What is a cohomologically trivial group?

    Acyclic for group cohomology, not just for $ G $ itself but for all $ H\leq G $.

    So $ H\leq G \implies H^n(H; M) = 0 $ for all $ M\in   {}_{G}{\mathsf{Mod}} $.

- Discuss $ p{\hbox{-}} $groups $ G $ acting on $ p{\hbox{-}} $primary $ G{\hbox{-}} $modules $ M $.

    If $ M\neq 0 $ then $ M^G\neq 0 $.

- Discuss duality in group (co)homology.

    For $ A {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}(A, {\mathbf{Q}}/{\mathbf{Z}}) $, $ H^n(G; A) {}^{ \vee }\cong H_n(G; A {}^{ \vee }) $ for $ G $ finite.

- What is the universal property for $ \mathop{\mathrm{Hom}} $ and products?

    $ \mathop{\mathrm{Hom}}(A, \prod B_i) = \prod \mathop{\mathrm{Hom}}(A, B_i) $, i.e. homs **into** a product are determined by homs into coordinates.

- How can cohomological triviality be checked locally?

    $ A $ is $ G{\hbox{-}} $cohomologically trivial $ \iff A $ is $ G_p{\hbox{-}} $cohomologically trivial for every sylow $ p{\hbox{-}} $subgroup $ G_p $ for every $ p\mathrel{\Big|}{\sharp}G $.

- When does flat coincide with torsionfree?

    Modules over a PID.

- What is the cup product on cochains?

    $$\begin{align}K^p(G; A) \otimes_{\mathbf{Z}}K^q(G; B) &\to K^{p+q}(G; A\otimes_{\mathbf{Z}}B)\\ a\otimes b &\mapsto \mathbf{g} \mapsto a(g_0,\cdots, g_p)\otimes b(g_{p-1}, \cdots g_{p+q}) \end{align}$$

- How does $ {\partial} $ interact with $ \smile $?

    $ d(a\smile b) = (da)\smile b + (-1)^{p}a\smile(db) $.

- What is the Tate-Nakayama theorem?

    For $ A\in   {}_{G}{\mathsf{Mod}} $ and $ a\in H^2(G; A) $ satisfying for all primes $ p $ that $ H^1(G_p; A) = 0 $ and $ {\sharp}H^2(G_p; A) = {\sharp}G_p $ and is generated by $ a_p \coloneqq\mathrm{Res}^{G_p}_{G} a $, for $ G_p $ the Sylow $ p{\hbox{-}} $subgroups, then

    For all $ D\in   {}_{G}{\mathsf{Mod}} $ torsionfree and all $ H\leq G $, there are isomorphism $ \widehat{H}^n(H; D) \underset{ {{-}\smile a} }{ { \, \xrightarrow{\sim}\, }}\widehat{H}^{n+2}(H; A\otimes_{\mathbf{Z}}D) $.

    Taking $ D = {\mathbf{Z}} $ yields $ \widehat{H}^n(H; {\mathbf{Z}}) { \, \xrightarrow{\sim}\, }\widehat{H}^{n+2}(H; D) $, so $ D $ cohomology is just a shift of $ {\mathbf{Z}} $ cohomology.

- What is the significance of Tate-Nakayama?

    For $ K\in \mathsf{Local}\mathsf{Field} $ and $ L/K $ finite Galois, set $ G\coloneqq{ \mathsf{Gal}}(L/K) $ and $ A\coloneqq L^{\times} $

    The hypotheses of Tate-Nakayama apply and yields

    $$G^{\operatorname{ab}}= \widehat{H}^{-2}(G; {\mathbf{Z}})  { \, \xrightarrow{\sim}\, }\widehat{H}^0(G; L^{\times}) = K^{\times}/NL^{\times}$$

    Thus if $ L/K $ is abelian then $ G \cong \operatorname{coker}\operatorname{Nm}_{L/K} $.

    Suggests target group for CFT should be $ K^{\times} $, so there should be an isomorphism between $ { \mathsf{Gal}}^{\operatorname{ab}}(\overline{K}/K) $ and $ \mathsf{pro}K^{\times} $.

- Characterize compact totally disconneced spaces.

    Inverse limits of finite discrete spaces.

    Also called profinite spaces, Stone spaces, boolean spaces.

    See Stone duality.

- What is a profinite group?

    A group object in profinite spaces

    A topological group whose underlying space is a profinite space.

- Discuss open subgroups of compact topological groups

    A subgroup is open iff closed and finite index.

    Note that open iff closed always holds, so compactness is giving finite index.

    NOT true that every finite index subgroup is closed!

- How do you extra a Hausdorff topological group from an non-Hausdorff one?

    Mod out by the closure of the identity.

- What is $ \aleph_0 $?

    Countable cardinality.

- Is a finite index subgroup of a topological group open?

    No! $ V\coloneqq\prod { \mathbf{F} }_2 $ has $ \aleph_0 $ open subgroups but $ 2^{2^{\aleph_0}} $ index 2 subgroups.

- Write a profinte group as a limit.

    $ G = \cocolim_{U\leq G \text{ open}, [G:U] < \infty} G/U $.

- Describe the image of $ G $ in $ \mathsf{pro}G $.

    $ \operatorname{im}(G\to \mathsf{pro}G) $ is dense, but need not be an injection.

    E.g. cts image of connected is connected.

- What is a residually finite group? Why care?

    $ G\hookrightarrow\mathsf{pro}G $ is an injection, so any $ g\neq e $ admits a finite index subgroup not containing $ g $.

    Useful since $ \pi_1^\text{ét}(X) = \mathsf{pro}\pi_1(X({\mathbf{C}})) $, so not residually finite means losing information from $ \pi_1 $.

- What is the Galois correspondence for infinite extensions?

    Subextensions of $ k^{ {}^{ \operatorname{sep} } }/k $ correspond to **closed** subgroups of $ { \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k) $ with the Krull topology.

- Characterize topological groups acting on discrete modules.

    The action is cts iff $ {\operatorname{Stab}}_G(x) $ is open for every $ x $.

    If $ G $ is profinite, the actions is cts iff $ G = \bigcup_{U\leq G \text{ open}}M^U $, the union of its (open) invariants.

    Profinite groups acting on discrete modules have finite orbits.

- What does it mean to be topologically finitely generated?

    There is a generating set $ S $ such that the smallest closed subgroup of $ G $ containing $ S $ is $ G $ itself.

- Is $ H\leq G $ finite index iff open?

    Open $ \implies $ finite index, but not conversely.

    Converse is true if $ G $ is topologically finitely generated.

    $ \iff $ holds when $ G $ is strongly complete.

- Show that functions into a discrete space are locally constant.

    The fibers must be open sets

- Show that $ f:X\to Y $ with $ X $ profinite and $ Y $ discrete must have finite image.

    $ X $ is compact and partitioned into open fibers, thus finitely many fibers.

- Discuss commuting limits for profinite groups.

    If $ G $ is profinite and $ Y $ is discrete, $ f:G\to Y $ factors through a finite quotient $ \tilde f: G/U\to Y $ and so

    $${\mathsf{Top}}(G, Y) = {\mathsf{Top}}(\lim G/N, Y) = \colim {\mathsf{Top}}(G/N, Y)$$

- What are continuous cochains?

    $ K_\text{cts}^n(G; M) \coloneqq{\mathsf{Top}}(G{ {}^{ \scriptscriptstyle\times^{n} }  }, M) $.

- Discuss continuity for profinite group cohomology.

    $ H^n(\cocolim G_i; \colim M_i) \cong \colim H^n(G_i; M_i) $.

    In particular $ H^n(G; A)=\colim_U H^n(G/U; A^U) $ using that $ U_2\hookrightarrow U_1 \implies G/U_1 \twoheadrightarrow G/U_2 $ (inflation).

- Discuss limits for Galois cohomology.

    For $ g_K \coloneqq{ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k) $ and $ A\in   {}_{g_K}{\mathsf{Mod}} $ write $ A(L) \coloneqq A^{g_L} $, then

    $$H^1(g_U; A) = \colim_{L/K} H^n({ \mathsf{Gal}}(L/K); A(L))$$

- Write a module as a limit.

    $ A =\colim_{B\leq A \text{ f.g.}} B $; i.e. every module is a colimit of its finitely generated submodules.

- Discuss higher profinite cohomology.

    $ H^{\geq 1}(G; A)\in   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\operatorname{tors}} $ is always torsion.

    Proof: $ H^q(G; A) = \colim H^q(G/U; A^U) = \colim H^q(G/U; A^u)[n] $ for $ n \coloneqq[G: U] $ by restriction-corestriction, and $   {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\operatorname{tors}} $ is closed under colimits.

- What is $ H^q(K; M) $ for $ K\in \mathsf{Field} $?

    $ H^q({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); M) $ the profinite group cohomology.

- What is the Weil-Chatalet group $ \mathrm{WC}(A/K) $?

    For $ A\in{\mathsf{Grp}}{\mathsf{Sch}} $ commutative, or $ A $ any commutative group, $ H^1(K; A)\coloneqq H^1({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); A(k^{ {}^{ \operatorname{sep} } })) $.

- What is the relative Galois cohomology $ H^n(L/K; A) $?

    $ \ker\qty{H^n(K; M) \to H^n(L; M)} $.

- Define a Galois extension.

    Algebraic, normal, separable.

- What is $ H^n({ \mathsf{Gal}}(L/K); L) $?

    Zero for $ n\geq 1 $; "additive" Hilbert 90 since $ \implies H^n(K; {\mathbf{G}}_a) = 0 $.

- What is the norrmal basis theorem?

    For $ L/K $ Galois, $ \exists \alpha\in L $ such that $ G_{L/K}.\alpha $ generates $ L\in   {}_{K}{\mathsf{Mod}} $.

    For $ G\coloneqq G_{L/K} $, iff $ L \cong K[G] \in   {}_{K[G]}{\mathsf{Mod}} $, so rank 1 with generator $ \alpha $.

    Iff $ L\cong {\mathbf{Z}}[G]\otimes_{\mathbf{Z}}K \in   {}_{{\mathbf{Z}}[G]}{\mathsf{Mod}} $, so $ L $ is induced.

- What is Hilbert 90?

    For $ L/K $ Galois, $ G = { \mathsf{Gal}}(L/K) $,

    $$H^1(G; L^{\times}) = 0$$

    This is false for $ q\gt 1 $!

    Think of this as $ H^1(G; {\mathbf{G}}_m) = 0 $.

- What is $ \mathrm{Br}(K) $?

    $ \mathrm{Br}(K) \coloneqq H^2(K; {\mathbf{G}}_m) $.

- What is classical Hilbert 90?

    For $ L/K $ finite cyclic Galois with $ G_{L/K} = \left\langle{\sigma}\right\rangle $,

    For $ \alpha\in L $, $ \operatorname{Trace}_{L/K}(\alpha) = 0 \iff \exists \lambda\in L $ such that $ \alpha = \lambda - \sigma(\lambda) $.

    Why: $ 0 = H^1(G;L) = \widehat{H}^{-1}(G; L) = \widehat{H}_0(G; L) = \ker(N: L\to K)/(\sigma - 1)L $ but here $ N $ is the sum of Galois conjugates, hence the trace

    $ \operatorname{Trace}_{L/K}(\alpha) = 1 \iff \exists \lambda \in L $ such that $ \alpha = \lambda/\sigma(\lambda) $.

    Why: $ 0 = H^1(G; L^{\times}) = \widehat{H}^0(G; L^{\times})=\ker(N)/ (\sigma-1)L $ multiplicatively.

- Discuss Kummer theory for $ {\mathbf{G}}_m $.

    Set $ \mu_n = (k^{ {}^{ \operatorname{sep} } })^{\times}[n] $, then $ H^1(k; \mu_n) = k^{\times}/(k^{\times})^n $, where these are $ n $th powers.

    Proof: LES for $ \mu_n\hookrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times}\twoheadrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times} $ and apply Hilbert 90.

    If $ K $ contains an $ n $th root of unity, $ \mu_n = C_n $ has trivial $ G_K{\hbox{-}} $ action and $ H^1(K; \mu_n) = \mathop{\mathrm{Hom}}(g_K, C_n) $.

- What is the Pontryagin dual?

    $ G {}^{ \vee }\coloneqq{\mathsf{Top}}(G, {\operatorname{U}}_1) $ with the compact-open topology, for $ G $ a locally compact abelian topological group.

    Duality: profinite abelian groups $ \rightleftharpoons $ discrete torsion abelian groups (

    So limits of finite discrete groups vs colimits

    Generalizes $ G $ isomorphic to its character group

- What is $ ({\operatorname{U}}_1)_{\operatorname{tors}} $?

    $ {\mathbf{Q}}/{\mathbf{Z}} $, the group of all roots of unity.

- How does one interpret $ K^{\times}/(K^{\times})^n $.

    $ K^{\times}/(K^{\times})^n \cong g_K^{{\operatorname{ab}}, n} $ the Galois group of the maximal abelian extension of $ K $ with exponent $ n $.

- What is the issue with Kummer theory?

    In positive characteristic $ p $, need $ n $ prime to $ p $ to consider $ H^1(k; \mu_n) $.

    Need

- What is Artin-Schreir theory?

    Characteristic $ p $ analogue of Kummer theory.

    Want an analogue for cyclic extensions of prime power order $ p^k $, AS works for $ k=1 $.

- How is Artin-Schrier theory expressed cohomologicallly?

    Take $ \phi \coloneqq\operatorname{Frob}- 1 $ so $ \phi(x) = x^p-x $, this is an isogeny of $ {\mathbf{G}}_a $ so get a SES $ { \mathbf{F} }_p\hookrightarrow k^{ {}^{ \operatorname{sep} } } \xrightarrow[]{\phi} { \mathrel{\mkern-16mu}\rightarrow }\,  k^{ {}^{ \operatorname{sep} } } $.

    Take LES, use additive Hilbert 90 to get $ \mathop{\mathrm{Hom}}(g_k, { \mathbf{F} }_p) \cong k/\phi(k) $.

    This says $ (g_k^{{\operatorname{ab}}, p}) {}^{ \vee }= k/\phi(k) $.

    Generalizes to $ (g_k^{{\operatorname{ab}}, p^n}) = W_n(k)/ \phi(W_n(k)) $ for $ W_n $ the length $ n $ Witt vectors.

- What is $ W_n(k) $?

    As a scheme, $ {\mathbf{G}}_a{ {}^{ \scriptscriptstyle\times^{n} }  } $, but what a twisted group law.

- What is the relative Brauer group?

    $ \mathrm{Br}(L/K) \coloneqq H^2({ \mathsf{Gal}}(L/K); L^{\times}) $.

- What is $ \operatorname{cohdim}G $?

    $ \sup_{p \in \operatorname{Spec}{\mathbf{Z}}} \operatorname{cohdim}_p G $ where $ \operatorname{cohdim}_p G $ is the least $ d $ such that for all $ n\geq d $ and for all discrete torsion $ A\in   {}_{G}{\mathsf{Mod}} $, one has $ H^n(G; A[p^\infty]) = 0 $.

- What is $ \operatorname{cohdim}C_p $?

    $ \operatorname{cohdim}_\ell C_p =0 $ if $ p\neq \ell $ and $ \infty $ if $ p=\ell $, so $ \operatorname{cohdim}C_p = \infty $.

- DIscuss $ \operatorname{cohdim}G $ for $ G $ a pro$ {\hbox{-}}p $ group.

    $ \operatorname{cohdim}_p G \leq n \iff H^{n+1}(G; C_p) = 0 $.

- Write $ \mathsf{pro}{\mathbf{Z}} $ as a product.

    $$\mathsf{pro}{\mathbf{Z}}= \cocolim C_n = \cocolim \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} \cocolim C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} { {\mathbf{Z}}_{\widehat{p}} }$$

- What is $ {\operatorname{Syl}}_p (\mathsf{pro}{\mathbf{Z}}) $?

    Uniquely $ { {\mathbf{Z}}_{\widehat{p}} } $.

- What is $ \operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} } $?

    $ \operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} }= 1 $.

    Why: $ H^2({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = 0 $ and $ H^1({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = \mathop{\mathrm{Hom}}({ {\mathbf{Z}}_{\widehat{p}} }, C_p) = C_p $.

- What is $ \operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}}) $?

    $ \operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}}) = 1 $ since $ \operatorname{cohdim}_p({ {\mathbf{Z}}_{\widehat{p}} }) = 1 $ for all primes $ p $ and $ \operatorname{cohdim}_p G = \operatorname{cohdim}_p G_p $ for $ G_p $ a Sylow $ p{\hbox{-}} $subgroup.

- Compare $ G_L $ and $ G_K $ for $ L/K $ an extension.

    $ G_L\hookrightarrow G_K $ as a closed subgroup.

- What is the inflation/restriction sequence for Brauer groups?

    $ \mathrm{Br}(L/K)\xhookrightarrow{\mathrm{inflation}} \mathrm{Br}(K) \xrightarrow{\mathrm{restriction}} \mathrm{Br}(L)^{{ \mathsf{Gal}}(L/K)} $.

- How do you interpret $ \mathrm{Br}(L/K) $?

    Elements of $ \mathrm{Br}(K) $ that are annihilated by restriction to $ \mathrm{Br}(L) $.

- What is $ H^2(K; \mu_n) $?

    $ H^2(K; \mu_n) = \mathrm{Br}(K)[n] $.

- What is an etale group scheme?

    Idea: for $ G $, lose no information by considering $ G(k^{ {}^{ \operatorname{sep} } })\in   {}_{G_k}{\mathsf{Mod}} $.

- What is $ \mathrm{Br}({\mathbf{R}}) $? Sketch a proof.

    Classified finite dimensional central simple division algebras.

    $ \mathrm{Br}({\mathbf{R}}) \cong C_2 \left\langle{{\mathbf{R}}, {\mathbb{H}}}\right\rangle $ where $ \dim_{\mathbf{R}}{\mathbb{H}}= 4 $ is the Hamilton quaterions.

    Proof: $ \mathrm{Br}({\mathbf{R}}) = \widehat{H}^0(\mathop{\mathrm{Aut}}({\mathbf{C}}/{\mathbf{R}}); {\mathbf{C}}^{\times}) = {\mathbf{R}}^{\times}/N{\mathbf{C}}^{\times}= {\mathbf{R}}^{\times}/{\mathbf{R}}_{\gt 0} = C_2 $.

- Describe $ \operatorname{Nm}: { \mathbf{F} }_{q^n} \to { \mathbf{F} }_q $.

    $ \operatorname{Nm}(x) = x \cdot x^q \cdot x^{q^2}\cdots x^{q^{n-1}} = x^{[n]_q} $, the q-binomial $ [n]_q \coloneqq{q^n-1\over q-1} $.

- What is $ \mathrm{Br}({ \mathbf{F} }_q) $? What is the interpretation?

    $ \mathrm{Br}({ \mathbf{F} }_q) = 0 $; every finite division algebra is a field.

    True because inflations are injective, $ { \mathsf{Gal}}({ \mathbf{F} }_{q^n}/{ \mathbf{F} }_q) = \left\langle{\operatorname{Frob}_q}\right\rangle $, and $ \widehat{H}^0(\left\langle{\operatorname{Frob}_q}\right\rangle; { \mathbf{F} }_{q^n}^{\times}) = { \mathbf{F} }_q^{\times}/N{ \mathbf{F} }_{q^n}^{\times}= 0 $ since the norm is surjective on finite fields.

- Characterize procyclic groups.

    Quotients of $ \mathsf{pro}{\mathbf{Z}} $ by closed subgroups.

- What is a $ C_1 $ field?

    All homogeneous polynomials $ f\in k[x_1,\cdots, x_n] $ of degree $ d < n $ have a nonzero root in $ k $.

- What is the Chevalley-Warring theorem?

    $ { \mathbf{F} }_q $ is a $ C_1 $ field.

- What is Tsen's theorem?

    If $ k ={ \overline{k} } $ and $ {\mathrm{trdeg}}(L/k)=1 $ then $ L $ is a $ C_1 $ field.

    In particular, $ k(C) $ the function field of a curve over $ k={ \overline{k} } $ is $ C_1 $.

- What is Lang's theorem?

    Is $ K $ is a complete discretely valued field with algebraically closed residue field, then $ K $ is a $ C_1 $ field.

- What is $ \mathrm{Br}(K) $ for $ K $ a $ C_1 $ field?

    $ \mathrm{Br}(K) = 0 $.

- Discuss the decomposition of $ \mathrm{Br}(K) $ for $ K $ a CDVR with perfect residue field $ k $.

    $ \mathrm{Br}(K) = \mathrm{Br}(k) \oplus \mathop{\mathrm{Hom}}(g_k, {\mathbf{Q}}/{\mathbf{Z}}) $.

    If $ k $ is finite, $ \mathrm{Br}(K) = {\mathbf{Q}}/{\mathbf{Z}} $.

- Discuss limits of $ C_n $.

    $ \colim C_n = {\mathbf{Q}}/{\mathbf{Z}} $

    $ \cocolim C_n = \mathsf{pro}{\mathbf{Z}} $.

- What is the characteristic property of unramified extensions?

    For $ L/K $ with residue fields $ l/k $, $ { \mathsf{Gal}}(L/K)\twoheadrightarrow{ \mathsf{Gal}}(l/k) $ is an isomorphism.

- For a decreasing filtration $ M_1 \supseteq M_2\supseteq\cdots $, what does it mean for $ M_1 $ to be complete and separated for the $ M_i{\hbox{-}} $adic topology?

    $ M_1\to \cocolim M_1/M_n $ is an isomorphism, realizing $ M_1 $ as an adic completion wrt the quotients.

- What is a residual extension?

    For $ L/K $ with residue fields $ l $ and $ k $ respectively, the extension of residue fields $ l/k $.

- What are the higher unit groups of a local field $ L $?

    $ U^n(L) \coloneqq\left\{{x\in R(L) {~\mathrel{\Big\vert}~}v(x-1)\geq n}\right\} $ where $ R(L) $ is the valuation ring.

    Can write as $ 1 + {\mathfrak{m}}^n $.

- What is the profinite index of $ H\leq G $ a closed subgroup of a profinite group

    $ [G: H] = \operatorname{lcm}_{U\supseteq H \text{ open}} [G:U] $.

- What is the virtual cohomology dimension?

    $ \mathrm{vcohdim}_p(G) \coloneqq\inf_{U \leq G \text{ open}}\operatorname{cohdim}_p(U) $, and $ \mathrm{vcohdim}(G) \coloneqq\sup_p \mathrm{vcohdim}_p(G) $.

- What explains $ \mathrm{vcohdim}_p G < \infty $ but $ \operatorname{cohdim}_p G = \infty $?

    The presence of elements of finite order $ p $.

    Theorem of Serre: if $ G $ is profinite with no elements of order $ p $, for all $ U\leq G $ open, $ \operatorname{cohdim}_p U = \operatorname{cohdim}_p G $.

- What is a virtually torsionfree group?

    $ \exists U\leq G $ open (thus finite index) which is torsionfree.

- What does "virtually" having a property $ P $ mean?

    Admitting some finite index subgroup which has property $ P $.

- When is $ M\in {\mathsf{Fin}} {}_{{\mathbf{Z}}}{\mathsf{Mod}} $ a product of its Sylow subgroups?

    Iff nilpotent.

- What is the structure theory of $ \mathsf{pro}{\mathsf{Ab}}{\mathsf{Grp}}^{{\mathsf{Top}}{\hbox{-}}{\mathrm{fg}}} $?

    $ G = \prod G_p $ is a product of Sylow $ p{\hbox{-}} $subgroups.

    If $ G $ is pro$ {\hbox{-}}p $, then $ G\cong { {\mathbf{Z}}_{\widehat{p}} }{ {}^{ \scriptscriptstyle\oplus^{\mathrm{v}\operatorname{cohdim}(G)} }  } \oplus G_{\operatorname{tors}} $ where $ {\sharp}G_{{\operatorname{tors}}} < \infty $.

- Define a local field.

    Complete DVR, a field, with finite residue field.

- What is the valuation ring of a DVF $ K $?

    $ R(K) = v^{-1}([0, \infty]) $

- Give equivalent conditions for a field $ K $ to be a DVF

    $ K $ is locally compact.

    The valuation ring $ R(K) $ is compact.

    $ {\mathbf{G}}_a(R(K)) $ is a profinite group (since compact and totally disconnected).

    $ K $ is complete and the residue field $ \kappa(K) \coloneqq R(K)/{\mathfrak{m}} $ is a finite field.

- Discuss characteristic zero local fields $ K $.

    $ K \in   {}_{{ {\mathbf{Q}}_p }}{\mathsf{Mod}}^{\mathrm{fd}} $ canonically

    $ {\mathbf{Q}}\hookrightarrow K $ with $ { \operatorname{cl}}^{\mathsf{Top}}_K({\mathbf{Q}}) ={ {\mathbf{Q}}_p } $ and $ [K: { {\mathbf{Q}}_p }] = e\cdot f $ where...

    $ \kappa = { \mathbf{F} }_{p^f} $ is the residual degree

    $ e = e(K/{ {\mathbf{Q}}_p }) = v(p) $ where $ p\coloneqq\operatorname{ch}\kappa $.

- Give an example of a totally ramified extension.

    $ { \mathbf{F} }_q(\hspace{-0.25em}( t^{1\over n} )\hspace{-0.22em})  $ over $ { \mathbf{F} }_q(\hspace{-0.25em}( t )\hspace{-0.22em})  $.

- Discuss the Galois theory of $ { \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k) $ for $ k $ local of positive characteristic $ p $.

    $ k^{\scriptscriptstyle\mathrm{un}}/k $ has ramification index 1, so unramified extensions correspond to extensions of the residue field, and so $ { \mathsf{Gal}}(k^{\scriptscriptstyle\mathrm{un}}/k) \cong { \mathsf{Gal}}(\overline{{ \mathbf{F} }}_q/{ \mathbf{F} }_q) \cong \mathsf{pro}{\mathbf{Z}} $.

    $ k^{\mathrm{tame}} $ has ramification indices all prime to $ p $, $ k^{\mathrm{tame}}/k^{\scriptscriptstyle\mathrm{un}} $ corresponds to taking $ \pi^{1\over n} $.

    $ I \coloneqq\mathop{\mathrm{Aut}}(k^{ {}^{ \operatorname{sep} } }/k^{\scriptscriptstyle\mathrm{un}}) = \ker(g_k \twoheadrightarrow g_{{ \mathbf{F} }_q}) $ is the inertia group

    $ I_p $ is the wild ramification, the Sylow $ p{\hbox{-}} $subgroup of of $ I $.

- Define the higher unit groups.

    For $ R $ the valuation ring, define $ r_n: R\twoheadrightarrow R/{\mathfrak{m}}^n $.

    In this special case, the induced map $ r_n^{\times}: R^{\times}\to (R/{\mathfrak{m}}^n)^{\times} $ is surjective

    Define $ U_n \coloneqq\ker r_n^{\times}= 1 + {\mathfrak{m}}^n $, so units that are trivial modulo $ {\mathfrak{m}}^n $.

    Can use $ p{\hbox{-}} $adic logarithm to get an isomorphism $ U_n { \, \xrightarrow{\sim}\, }{\mathfrak{m}}^n $.

- What does local class field theory say about the maximal abelian extension of a local field $ K $?

    Isomorphic to $ \mathsf{pro}{\mathbf{G}}_m(K) \cong \mathsf{pro}{\mathbf{Z}}\times U(K) $, so the unit group gives most of the information.

- What is the normal basis theorem?

    For $ L/K $ Galois, $ {\exists}\alpha\in L $ such that $ L = \left\langle{G_{L/K}.\alpha}\right\rangle_K \in   {}_{K}{\mathsf{Mod}} $.

    Equivalently, $ {\mathbf{G}}_a(K) \cong K[G] \in   {}_{K[G]}{\mathsf{Mod}} $ for $ G\coloneqq{ \mathsf{Gal}}(L/K) $.

- For $ G = \mathop{\mathrm{Aut}}(L/K)\in{\mathsf{Fin}}{\mathsf{Grp}} $ cyclic, what is $ K^{\times}/N L^{\times} $?

    $ {\sharp}K^{\times}/N L^{\times}= [L: K] $.

- What is $ { \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K) $?

    $ { \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K)\cong { \mathsf{Gal}}(\overline{\kappa}/\kappa) = \mathsf{pro}{\mathbf{Z}} $.

- What is the unit group SES?

    $ U\hookrightarrow K^{\times} \xrightarrow[]{v} { \mathrel{\mkern-16mu}\rightarrow }\,  {\mathbf{Z}} $.

- What is the invariant map?

    $ \mathrm{inv}_K: \mathrm{Br}(K)  { \, \xrightarrow{\sim}\, }{\mathbf{Q}}/{\mathbf{Z}} $ for $ K $ a local field.

- For $ L/K $, what is the induced restriction map on Brauer groups? Corestriction?

    $ \mathrm{Res}^{K}_{L}: \mathrm{Br}(K) \to \mathrm{Br}(L) $ is $ \cdot n: {\mathbf{Q}}/{\mathbf{Z}}\to {\mathbf{Q}}/{\mathbf{Z}} $ where $ n \coloneqq[L: K] $.

    Corestrictionis the identity.

- What is $ \mathrm{Br}(L/K) $ for $ L/K $ a finite extension?

    $ \mathrm{Br}(L/K) = \mathrm{Br}(K)[n] $ for $ n\coloneqq[L: K] $.

- What is the fundamental class? What is its significance?

    $ v_{L/K}\in \mathrm{Br}(L/K) = H^2(G_{L/K}; {\mathbf{G}}_m(L)) $ the unique class where

    $$\mathrm{inv}_K(v_{L/K}) = {1\over n} + {\mathbf{Z}}\in \qty{{1\over n} {\mathbf{Z}}}/{\mathbf{Z}}\subseteq {\mathbf{Q}}/{\mathbf{Z}}$$

    Apply Tate-Nakayama to get

    $$G^{\operatorname{ab}}= \widehat{H}^{-2}(G; {\mathbf{Z}}) \underset{{-}\smile v_{L/K}}{ { \, \xrightarrow{\sim}\, }} \widehat{H}^0(G; {\mathbf{G}}_m(L)) =K^{\times}/N L^{\times}$$

    Yields $ \omega_{L/K}: K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G^{\operatorname{ab}} $, so e.g. the norm map is surjective iff $ G = G^{\operatorname{ab}} $ is abelian.

    Alternatively, for abelian extensions, $ { \mathsf{Gal}}(L/K)  { \, \xrightarrow{\sim}\, }\operatorname{coker}N $.

- Discuss the signifiance of $ \omega $.

    Isomorphisms of $ \omega_{L/K} $ assemble into a compatible inverse system.

    Yields $ \omega: K^{\times}\to\cocolim_{L/K \text{ fin. ab}}K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G_K^{\operatorname{ab}} $, so is this injective? Is it the profinite completion of $ K^{\times} $?

    Equivalently, are there enough finite abelian extensions to be cofinal in the system of all finite index subgroups of $ K^{\times} $?

    $ \omega(K^{\times}) \subseteq G_K^{\operatorname{ab}} $ is dense.

- What is $ I_K^{\operatorname{ab}} $?

    $ I_K^{\operatorname{ab}}= \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}})\subseteq \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K) $.

- What is a projective profinite group?

    $ P $ is projective iff $ \forall \pi: G\twoheadrightarrow P $ there is a section $ \pi\circ s = \operatorname{id}_P $.

    $ \iff \operatorname{cohdim}P \leq 1 $.

    $ \iff G_p $ is a free pro $ p{\hbox{-}} $group.

- Describe $ \mathsf{pro}K^{\times} $.

    $ K^{\times}= U_K \times {\mathbf{Z}} $ since everything is a unit times a uniformizer, so

    $ \mathsf{pro}K^{\times}= U_K \times \mathsf{pro}{\mathbf{Z}} $.

- What is the reciprocity map?

    $ \omega:\mathsf{pro}(K^{\times})\to G_K^{\operatorname{ab}} $; restricts to $ U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}} $.

- What is $ N L^{\times} $ for $ L/K $ unramified?

    $ U_K \subseteq NL^{\times}= \left\{{x\in K^{\times}{~\mathrel{\Big\vert}~}n\mathrel{\Big|}v(x)}\right\} $.

- What is a proper map of profinite groups?

    $ f:X\to Y $ where $ f\times \operatorname{id}_Z: X\times Z\to Y\times Z $ is closed for every $ Z $.

    $ \iff f $ is closed with quasicompact fibers.

    For $ X $ Hausdorff and $ Y $ locally compact, $ \iff $ primage of compact is compact.

- What is the Galois correspondence induced by the reciprocity map?

    Subextensions of $ L/K $ $ \rightleftharpoons $ open subgroups of $ K^{\times} $ containing $ NL^{\times} $ where $ \omega^{-1}(M) \coloneqq N M^{\times} $ for such a subgroup $ M $.

- Interpret $ \mathop{\mathrm{Hom}}(G, C_n) $.

    The character group $ \chi(\tilde G) $ where $ \tilde G = G^{\operatorname{ab}}/(G^{\operatorname{ab}})^n $ is the maximal abelian quotient of exponent $ n $.

- What is the norm residue symbol / Hilbert symbol?

    $ (a, b)_n \coloneqq b \smile\delta(\chi_a)\in H^2(K; {\mathbf{G}}_m) = \mathrm{Br}(K) $ for $ a,b\in K^{\times} $.

    Here $ \delta: K^{\times}/(K^{\times})^n  { \, \xrightarrow{\sim}\, }H^1(K; \mu_n) $ is the coboundary, which is an isomorphism by Kummer theory.

    Yields a perfect pairing $ ({-}, {-})_n: (K^{\times}/ (K^{\times})^n){ {}^{ \scriptstyle\otimes_{}^{2} }  } \to {\mathbf{Q}}/{\mathbf{Z}} $.

- What is the Steinberg relation?

    $ (a, 1-a)_n = 0 $.

- What is the existence theorem for $ p{\hbox{-}} $adic fields?

    If $ U\leq K^{\times} $ is finite index then $ \exists ! L $ a subextension of $ \overline{K}/K $ such that $ U = \operatorname{Nm}_{L/K} L^{\times} $.

- What is the main result concerning LCFT for $ p{\hbox{-}} $adic fields?

    $ \widehat{\omega}: \mathsf{pro}K^{\times} { \, \xrightarrow{\sim}\, }g_K^{\operatorname{ab}} $ is an isomorphism

    $ \omega: U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}}= { \mathsf{Gal}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}}) $, so we understand the totally ramified piece of $ K^{ {}^{ \operatorname{sep} } }/K $.

- Discuss Lubin-Tate theory.

    A generalization of complex multiplication to local fields.

    Constructs $ K^{\operatorname{ab}}= K^{\scriptscriptstyle\mathrm{un}}(\cdots) $ where one adjoins torsion points of FGLs.

- What is CFT?

    Given a field $ K $, find a topological group $ G $ and an isomorphism $ \mathsf{pro}G\to G_K $.

- What is local CFT?

    The reciprocity map $ \omega: {\mathbf{G}}_m(K) \to G_K^{\operatorname{ab}} $ beomes an isomorphism after passing to the profinite completion.

- What is eplicit class field theory?

    Since $ K^{\operatorname{ab}}/K $ is a countably infinite degree algebraic extension, produce a sequence of algebraic numbers $ a_n $ such that $ K^{\operatorname{ab}}= \colim(K[a_1]\hookrightarrow K[a_1, a_2]\hookrightarrow\cdots) $.

- State Kronecker-Weber.

    $ {\mathbf{Q}}^{\operatorname{ab}}= {\mathbf{Q}}(\zeta_n {~\mathrel{\Big\vert}~}n\in {\mathbf{Z}}_{\geq 0}) $.

- What is the mod $ n $ cyclotomic character?

    $ \chi_n: G_K\to C_n^{\times} $ induced by $ G_K\curvearrowright K(\zeta_n) $, take inverse limit to obtain $ \chi: G_K \to (\mathsf{pro}{\mathbf{Z}})^{\times} $.

    The kernel always yields an abelian extension of $ K $, the maximal cyclotomic extension (obtained by adjoining all roots of unity)

- Discuss explicit CFT for imaginary quadratics.

    For $ E/k $ with $ {\mathcal{O}}_K{\hbox{-}} $CM, get $ \rho_N: G_K \to \mathop{\mathrm{Aut}}E[N] \cong \operatorname{GL}_1(C_N) $.

    Completes to $ \rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathbf{Z}}) $.

    Check $ E[N] $ is a rank 2 $ C_N $ module but a rank 1 $ {\mathcal{O}}_K/N $ module.

    Get $ \rho_N: G_K \to \operatorname{GL}_1({\mathcal{O}}_K/N) $ which completes to $ \rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathcal{O}}_K) $.

    Take $ \psi: G_K \to \mathsf{pro}{\mathcal{O}}_K^{\times}\to \mathsf{pro}{\mathcal{O}}_K^{\times}/{\mathcal{O}}_K^{\times} $ to get $ K^{\ker \psi} = K^{\operatorname{ab}} $.

    So for $ K $, write down $ E/K $ with CM by $ {\mathcal{O}}_K $ and get $ K^{\operatorname{ab}}= K(x(p) {~\mathrel{\Big\vert}~}p\in E[{\operatorname{tors}}]) $, the $ x{\hbox{-}} $coordinates of torsion points.

- For $ R $ the valuation ring of $ K $, $ U $ doesn't give $ K^{\operatorname{ab}} $. Why? What does?

    $ \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K) = U \times\mathsf{pro}{\mathbf{Z}} $, so $ U $ only gives the totally ramified part.

- What does $ f = g + { \mathsf{O}}(k) $ mean?

    $ f\equiv g \in k{\llbracket x_1,\cdots, x_n \rrbracket  }/\left\langle{x_1,\cdots,x_n}\right\rangle^k $, so equal up to terms of order $ k $.

- When can power series but substituted into each other?

    When the constant term is zero, e.g. $ e^{e^x} $ has infinitely many contant terms.

- What is a formal group law?

    Associativity: $ F(F(x,y), z) = F(x, F(y,z)) $

    Identities: $ F(x, 0) = x $ and $ F(0, y) = y $.

    Inverses: $ \exists !\iota \in R{\llbracket t \rrbracket  } $ such that $ F(x, \iota(x)) = 0 $.

- How does one get an honest group from a FGL?

    Take $ (R, {\mathfrak{m}}) $ complete local, then $ R { \, \xrightarrow{\sim}\, }\cocolim_n R/{\mathfrak{m}}^n $ so $ x+y \coloneqq F(x,y) $ converges in the $ {\mathfrak{m}}{\hbox{-}} $adic topology.

- What is the multiplicative formal group?

    $ F(x,y) = x + y + xy = (x+1)(y+1) - 1 $.

- What is a formal $ R{\hbox{-}} $module?

    A ring morphism $ R\to { \operatorname{End} }_{\fgl}(F) $ for $ F $ a formal group.

- What is $ [n](T) $ for $ {\mathbf{G}}_a $ and $ {\mathbf{G}}_m $, where $ [n] \in { \operatorname{End} }_{\fgl}(F) $ is $ 1 \oplus_F 1\oplus_F \cdots \oplus_F 1 $?

    $ [n](T) =nT $ for $ {\mathbf{G}}_a $.

    $ [n](T) = (T+1)^n - 1 $ for $ {\mathbf{G}}_m $.

- What is $ \operatorname{ht}{\mathbf{G}}_m $ in characteristic zero?

    Height 1

- What is $ \operatorname{ht}{\mathbf{G}}_a $ in characteristic $ p $?

    Height $ \infty $.

- What are the torsion points on $ {\mathbf{G}}_m $?

    Roots of unity.

- What is $ F_\pi $? Give an example of $ f\in F_\pi $.

    $ F_\pi \coloneqq\left\{{ f\in R{\llbracket T \rrbracket  } {~\mathrel{\Big\vert}~}f(T) = \pi T + { \mathsf{O}}(T^2) ,\,\, f\equiv T^q \operatorname{mod}\pi}\right\} $.

    For $ K = { {\mathbf{Q}}_p } $, take $ f(T) = (1+T)^p - 1 = T^p + {p\choose p-1}T^{p-1} + \cdots + pT $, so $ f = [p] $ on $ {\mathbf{G}}_m $.

- What are the key properties of $ F_\pi $?

    For $ f,g\in F_\pi $ and $ \phi_1 \in R{\llbracket x_1,\cdots, x_n \rrbracket  } $, $ \exists ! \phi \in R{\llbracket x_1,\cdots, x_n \rrbracket  } $ st $ \phi = \phi_1 + { \mathsf{O}}(x^2) $ and $ f\circ \phi = \phi \circ \Delta_g $, i.e.$ f(\phi(x_1,\cdots, x_n)) = \phi(g(x_1), \cdots, g(x_n)) $.

- What is the Lubin-Tate FGL attached to $ f\in F_\pi $?

    The unique FGL $ F_f\in R{\llbracket x,y \rrbracket  } $ st $ f\in { \operatorname{End} }_{\fgl} F_f $ canonically, so $ f(F_f(x,y)) = F_f(f(x), f(y)) $.

- What do we know about field extensions generated by Eisenstein polynomials?

    - Totally ramified.

- How are an ramified and a totally ramified extension related?

    - Disjoint

- How is $ \overline{{ \mathbf{F} }_{q}} $ obtained from $ {{ \mathbf{F} }_{q}} $?

    - Adjoin all roots of unity.
