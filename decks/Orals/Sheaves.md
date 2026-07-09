---
title: "Orals::Sheaves"
---

- What is a **presheaf**?

    A functor $ F: {\mathsf{Open}}(X)^{\operatorname{op}}\to \mathsf{CRing} $ (say) preserving terminal obejcts, i.e. for each open $ U \subseteq X $ a ring $ F(U) $ where $ F(\emptyset) = 0 $, for every $ U\hookrightarrow V $ a restriction $ \mathop{\mathrm{Res}}_{V< U}: F(V)\to F(U) $, where $ \mathop{\mathrm{Res}}_{U, U} = \operatorname{id}_U $ and $ U\hookrightarrow V\hookrightarrow W \leadsto \mathop{\mathrm{Res}}_{VU} \circ \mathop{\mathrm{Res}}_{WV} = \mathop{\mathrm{Res}}_{WU} $.

- What is a **sheaf**?

    A presheaf satisfying unique gluing: given $ \left\{{\phi_i \in F(U_i)}\right\} $ with $ { \left.{{\phi_i}} \right|_{{U_{ij}}} } = { \left.{{\phi_j}} \right|_{{U_{ij}}} } $ there exists a unique $ \Phi\in F(\bigcup_i U_i) $ such that $ { \left.{{\Phi}} \right|_{{U_i}} } = \phi_i $ for all $ i $.

- Give an example of a presheaf that is not a sheaf.

    Any presheaf of constant functions, since functions can be constant on disjoint open sets (thus agreeing on overlaps trivially) without being globally constant (jump discontinuities)

- What is the **equalizer characterization** of a sheaf?

    $$F(U) \rightarrow \prod_{i} F(U_i) {{{} \atop \longrightarrow}\atop{\longrightarrow \atop {}}} \prod_{i, j} F(U_i \cap U_j)$$

    where the maps are the restrictions $ U_i \to U_{ij} $ and $ U_j\to U_{ij} $.

- What is the **sheafification** of a presheaf?

    For $ {\mathcal{F}} $ a presheaf, define $ {\mathcal{F}}^+(U) \coloneqq{\mathsf{Top}}(U, \amalg_{x\in X} {\mathcal{F}}_x) $ as the functions $ s $ where $ s(p) \in {\mathcal{F}}_p $ and for each $ p\in U $ there is a neighborhood $ V $ and $ t\in {\mathcal{F}}(V) $ such that $ \forall q\in V,\,\, t\mathrel{\Big|}_q = s(q) $.

- What is a **morphism of presheaves**? Of sheaves?

    $ \phi: {\mathcal{F}}\to {\mathcal{G}} $ is a collection $ \phi_U: {\mathcal{F}}(U) \to {\mathcal{G}}(U) $ fitting into commuting squares with restrictions.

- What is a **germ**?

    Elements in the stalk $ {\mathcal{F}}_p $ are germs of sections of $ {\mathcal{F}} $ over $ p $.

- What is the **stalk** of a sheaf?

    $ {\mathcal{F}}_p \coloneqq\colim_{U\ni p} {\mathcal{F}}(U) $.

- What is the **kernel sheaf**?

    $ U\mapsto \ker \phi(U) $, which is already a sheaf.

- What is the **image sheaf**?

    Sheafify $ U\mapsto \operatorname{im}\phi(U) $.

- Give an example to show that the image presheaf is not necessarily a sheaf.

    Problem: may fail existence. Take $ 0\to \underline{{\mathbf{Z}}}\xrightarrow{2\pi i} {\mathcal{O}}_X \xrightarrow{\exp} {\mathcal{O}}_X^{\times}\to 0 $; this is exact as a sequence of sheaves since it's exact on stalks, but not exact as a sequence of presheaves, showing that $ \operatorname{im}_{{\mathsf{pre}}} \exp \neq (\operatorname{im}_{\mathsf{pre}}\exp)^+ $ (where $ {\mathcal{F}}= {\mathcal{F}}^+ $ for any sheaf). Cover $ {\mathbf{C}}^{\times} $ by contractible $ U_i $, then take sections $ f_i \coloneqq\operatorname{id}_{U_i} \in {\mathcal{O}}_X^{\times} $; then $ f_i\in (\operatorname{im}\exp)^- $ since $ \log(z) $ exists on each $ U_i $. The sectors glue to $ {\mathbf{C}}^{\times} $, but there is no global $ \log(z) $. So $ \operatorname{id}_{{\mathbf{C}}^{\times}} \not\in (\operatorname{im}\exp)^- $, so it fails the gluing axiom.

- What is the **cokernel sheaf**?

    For $ \phi: {\mathcal{F}}\to {\mathcal{G}} $, sheafify $ U\mapsto \operatorname{coker}\phi(U) \coloneqq{\mathcal{G}}/ \operatorname{im}\phi(U) $.

- Give an example to show that the cokernel presheaf is not a sheaf.

    Problem: may fail uniqueness. Let $ {\mathcal{G}}\leq \mathop{\mathrm{Hol}}({\mathbf{C}}, {\mathbf{C}}) $ be the sheaf of nonvanishing holomorphic functions and take $ \exp: \mathop{\mathrm{Hol}}({\mathbf{C}}, {\mathbf{C}})\to {\mathcal{G}} $ and $ U = {\mathbf{C}}\setminus\left\{{0}\right\} $. Set $ f(z) = z $, then $ f\in {\mathcal{G}}(U) $ since it's nonvanishing. Cover $ U $ by sectors $ U_i $, then $ f\in \operatorname{im}{ \left.{{\exp}} \right|_{{U_i}} } $ for all $ i $ since $ \log f $ exists and $ \exp(\log f) = f $, so $ f = 0 $ in $ \operatorname{coker}{ \left.{{\exp}} \right|_{{U_i}} } $ for all $ i $. But $ f\not\in \operatorname{im}\exp $ since there is no global logarithm, so $ f\neq 0\in \operatorname{coker}\exp $ as a morphism of presheaves.

- What is the **pullback/pushforward** (inverse/direct images) of a sheaf?

    For $ f:X\to Y $, $ {\mathcal{F}}\in {\mathsf{Sh}}(X), {\mathcal{G}}\in {\mathsf{Sh}}(Y) $. Pushforward/direct image: already a sheaf

    $$f_*{\mathcal{F}}(U) ={\mathcal{F}}(f^{-1}(U)),\qquad f_*{\mathcal{F}}\in {\mathsf{Sh}}(Y)$$

    Pullback/inverse image: **sheafify**

    $$f^{-1}{\mathcal{G}}(U) \coloneqq\colim_{V\supseteq f(U)} {\mathcal{G}}(V)$$

    For $ f: X\to Y $ an inclusion, $ f^{-1}{\mathcal{G}}(U) = { \left.{{{\mathcal{G}}}} \right|_{{\operatorname{im}(f)}} }(U) = {\mathcal{G}}(U) $, so denote $ f^{-1}{\mathcal{G}}\coloneqq{ \left.{{{\mathcal{F}}}} \right|_{{X}} } $

- What is the **structure sheaf** of a scheme?

    Part of the definition of a scheme as a locally ringed space $ (X, {\mathcal{O}}_X) $; $ {\mathcal{O}}_X $ is the structure sheaf.

- What is a **constant sheaf**?

    For $ A\in {\mathsf{Ab}}{\mathsf{Grp}} $, $ \underline{A} \coloneqq C^0({-}, A^{{\operatorname{disc}}}) $. On connected sets $ U $, $ \underline{A}(U) = A $. This is the sheaf of locally constant functions, i.e. constant on every connected component. Stalks are all $ A $.

- What is the **skyscraper sheaf**? Its stalks? Its adjoint characterization?

    For the inclusion $ \iota: \left\{{p}\right\} \hookrightarrow X $, and $ \underline{A} $ the constant sheaf on $ \left\{{p}\right\} $, the direct image $ \iota_*\underline{A} $. Assigns $ U\mapsto \underline{A}(U) \chi_{p\in U} $, stalks are $ A $ at each point in $ { \operatorname{cl}}_X(p) $ and 0 elsewhere. Adjoint to taking stalks: $ {\mathsf{Set}}({\mathcal{F}}_x, A)  { \, \xrightarrow{\sim}\, }{\mathsf{Sh}}(X)({\mathcal{F}}, (\iota_x)_* A) $.

- What is the **canonical sheaf**?

    $ \omega_{X/S} \coloneqq\operatorname{det}\Omega_{X/k} \coloneqq\bigwedge\nolimits^n \Omega_{X/S} $ where $ n\coloneqq\dim X $.

- What is the **dualizing sheaf**?

    For $ X $ proper over a field, $ \omega_X^\circ\in {\mathsf{Coh}}(X) $ together with a trace $ \operatorname{tr}: H^n(X; \omega_X^\circ)\to k $ such that $ \forall {\mathcal{F}}\in {\mathsf{Coh}}(X) $, the composition

    $$H^n(X; {\mathcal{F}}) \times \mathop{\mathrm{Hom}}({\mathcal{F}}, \omega_X^\circ) \to H^n(X, \omega_X^\circ) \xrightarrow{{\mathrm{tr}}}k$$

    yields an isomorphism $ \mathop{\mathrm{Hom}}({\mathcal{F}}, \omega_X^\circ)  { \, \xrightarrow{\sim}\, }H^n(X; {\mathcal{F}}) {}^{ \vee } $ and more generally $  \operatorname{Ext}^i({\mathcal{F}}, \omega_X^\circ) \cong H^{n-i}(X; {\mathcal{F}}) {}^{ \vee } $. Exists for any projective scheme, not always equal to $ \operatorname{det}\Omega_{X/k} $.

- What is an **ideal sheaf**?

    For $ \iota:Y\to X $ the inclusion of a closed subscheme, $ {\mathcal{I}}_Y \coloneqq\ker({\mathcal{O}}_X \xrightarrow{\iota^\sharp} {\mathcal{O}}_{Y}) $.

- What is a **local system**?

    A locally constant sheaf, i.e. a sheaf such that every $ x\in X $ admits a neighborhood $ U\ni x $ such that $ { \left.{{{\mathcal{F}}}} \right|_{{U}} } $ is a constant sheaf.

- What is an **invertible sheaf**?

    $ {\mathcal{L}}\in {\mathsf{Sh}}(X) $ such that $ \exists {\mathcal{L}}^{-1}\in {\mathsf{Sh}}(X) $ with $ {\mathcal{L}}\otimes_{{\mathcal{O}}_X} {\mathcal{L}}^{-1}\cong {\mathcal{O}}_X $.

    Equivalently, every $ x\in X $ admits a neighborhood $ U\ni x $ such that $ { \left.{{{\mathcal{F}}}} \right|_{{U}} } \cong {\mathcal{O}}_U $.

    Equivalently, a locally free $ {\mathcal{O}}_X{\hbox{-}} $module of rank 1.

- Discuss invertible sheaves on affine schemes.

    $ {\mathcal{F}}\in \operatorname{Pic}(\operatorname{Spec}A)\implies {\mathcal{F}} $ corresponds to $ M\in  {}_{A}{\mathsf{Mod}} $ which is finite projective locally free of rank 1 and thus flat and finitely presented. Every invertible sheaf on $ {\mathbf{A}}^2_{/ {k}} $ is trivial.

- What is a **vector bundle** over a scheme?

    For $ {\mathcal{E}} $ a locally free sheaf on $ Y $, the associated geometric vector bundle is $ \mathbf{V}({\mathcal{E}})\coloneqq\operatorname{Spec}\operatorname{Sym}({\mathcal{E}}) $.

    More plainly: for $ Y\in{\mathsf{Sch}} $, a geometric vector bundle of rank $ n $ over $ Y $ is a scheme $ X $ with a morphism $ f:X\to Y $ along with the data of $ {\mathcal{U}}\rightrightarrows Y $ and isomorphism $ \psi_i: f^{-1}(U_i)\to{\mathbf{A}}^n_{/ {U_i}} $ such that for any $ \operatorname{Spec}A \subseteq U_{ij} $ each $ \psi_{ij} \coloneqq\psi_j\circ \psi_i^{-1}\in \mathop{\mathrm{Aut}}({\mathbf{A}}^n_{/ {\operatorname{Spec}A}}) $ is given by a linear automorphism $ \theta \in \mathop{\mathrm{Aut}}_{  {}_{A}{\mathsf{Mod}}}(A[x_1,\cdots ,x_n]) $, so $ \theta(a) = a $ for $ a\in A $ and $ \theta(x_i) = \sum a_{ij} x_j $.

- What is a **constructible sheaf**?

    $ {\mathcal{F}}\in {\mathsf{Sh}}(X) $ is constructible iff $ \exists \left\{{i_{Y_i}: Y_i\hookrightarrow X}\right\}_{i\leq N} $ with $ X = \bigcup_{i\leq N}Y_i $, i.e. $ Y $ is a finite union of locally closed subschemes, such that $ { \left.{{{\mathcal{F}}}} \right|_{{Y_i}} } \coloneqq\iota_{Y_i}^* {\mathcal{F}} $ is a finite locally constant sheaf.

- What is a **free sheaf**?

    $ {\mathcal{F}}\cong {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  } $ for some $ n $.

- What is a **locally free sheaf**?

    Each stalk $ {\mathcal{F}}_x $ is a free $ {\mathcal{O}}_{X, x}{\hbox{-}} $module. Equivalently, $ \exists {\mathcal{U}}\rightrightarrows X $ such that each $ { \left.{{{\mathcal{F}}}} \right|_{{U_i}} } $ is a free $ { \left.{{{\mathcal{O}}_X}} \right|_{{U}} }{\hbox{-}} $module.

- What is the **sheaf of rational functions** on a scheme?

    Define the function field of $ X $ to be $ K\coloneqq{\mathcal{O}}_{X, \eta_X} $, the stalk at the generic point, and define $ {\mathcal{K}}_X \coloneqq\underline{K} $, the constant sheaf associated to this field. Equivalently, sheafify $ U\to \operatorname{ff}({\mathcal{O}}_X(U)) $.

- What is the fundamental exact sequence involving the tangent sheaf for $ {\mathbf{P}}^n $?

    $ 0\to {\mathcal{O}}_X \to {\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\to {\mathcal{T}}_X\to 0 $.

- Define the **twisting sheaf** on $ {\mathbf{P}}^n_{/ {Y}} $.

    $ {\mathcal{O}}_{{\mathbf{P}}^n_{/ {Y}}}(1) \coloneqq g^* {\mathcal{O}}_{{\mathbf{P}}^n_{/ {{\mathbf{Z}}}}}(1) $ where $ g: {\mathbf{P}}^n_{/ {Y}}\to {\mathbf{P}}^n_{/ {{\mathbf{Z}}}} $.

- Define the **twisting sheaf** on $ \mathop{\mathrm{Proj}}S $ for $ S $ a graded ring.

    $ {\mathcal{O}}_X(n) \coloneqq S[n]\tilde{} $, and the twisting sheaf is $ {\mathcal{O}}_X(1) $.

- What does it mean to **twist a sheaf**?

    $ {\mathcal{F}}(n) \coloneqq{\mathcal{F}}\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n) $.

- Characterize coherent sheaves over $ \operatorname{Spec}A $ for $ A $ Noetherian.

    $ {\mathcal{F}}\in {\mathsf{Coh}}(\operatorname{Spec}A)\implies \exists \bigoplus_{i\in I} {\mathcal{O}}(n_i) \twoheadrightarrow{\mathcal{F}} $, i.e. always a quotient of a free sheaf. Easy proof: $ {\mathcal{F}}(n) $ is globally generated for some $ n $, so $ \exists \bigoplus_{i\leq N} {\mathcal{O}}_X \twoheadrightarrow{\mathcal{F}}(n) $, now twist this exact sequence by $ -n $.

- What is the **six functor formalism**?

    Direct image (pushforward) and inverse image (pullback), extension by zero (lower shriek) and exceptional image (upper shriek), internal tensor and internal hom.

- How is the **inverse image sheaf** defined? What are its stalks?

    $ f^{-1}{\mathcal{G}}(U) \coloneqq\colim_{V\supseteq f(U)} {\mathcal{G}}(V) $. Stalks: $ {\mathcal{G}}_p  { \, \xrightarrow{\sim}\, }(f^{-1}{\mathcal{G}})_p $.

- What is the **extension by zero** sheaf? What are its stalks?

    Sheafify $ U\mapsto \chi_{V\subseteq U}{\mathcal{F}}(V) $ to get $ \iota_! {\mathcal{F}} $ for $ \iota: U \subseteq X $. Stalks are $ {\mathcal{F}}_p \chi_{p\in U} $.

    Alternatively take $ \iota_* {\mathcal{F}} $.

- How is the pushforward sheaf defined? What are its stalks?

    $ f_*{\mathcal{F}}(V) \coloneqq{\mathcal{F}}(f^{-1}(V)) $. Can't say much in general about its stalks.

- What is the restriction of a sheaf?

    For $ \iota: X\hookrightarrow Y $, $ { \left.{{{\mathcal{G}}}} \right|_{{X}} } \coloneqq\iota^{-1}{\mathcal{F}} $, same stalks as $ {\mathcal{G}} $.

- What is a **flasque sheaf**?

    $ U\hookrightarrow V \implies {\mathcal{F}}(V) \twoheadrightarrow{\mathcal{F}}(U) $.

- Discuss flasque sheaves.

    $ H^{\geq 1}(X; {\mathcal{F}}) = 0 $ for any flasque sheaf on any topological space, so are $ \Gamma{\hbox{-}} $acyclic.

- What is **Grothendieck vanishing**?

    For $ X $ a noetherian topological space, for all $ {\mathcal{F}}\in {\mathsf{Sh}}(X, {\mathsf{Ab}}{\mathsf{Grp}}) $, one has

    $$H^{i\geq \dim X+1}(X; {\mathcal{F}}) = 0.$$

    How to remember: $ \mathrm{cd}(X) \leq \dim X $.

- Is a morphism of sheaves injective if injective on sections? Surjective?

    Injective: yes, surjective: no.
