---
title: "Orals::O_X Modules"
---

- What is an $ O_X{\hbox{-}} $modules? :

    $ {\mathcal{F}}\in {\mathsf{Sh}}(X) $ where $ {\mathcal{F}}(U)\in   {}_{{\mathcal{O}}_X(U)}{\mathsf{Mod}} $ with compatible restrictions $ (rm)\mathrel{\Big|}_V = { \left.{{r}} \right|_{{V}} } { \left.{{m}} \right|_{{V}} } $.

- What is the **tensor product** of two $ {\mathcal{O}}_X{\hbox{-}} $modules?

    Sheafify $ U\mapsto {\mathcal{F}}(U) \otimes_{{\mathcal{O}}_X(U)} {\mathcal{G}}(U) $.

- What is a **free** $ {\mathcal{O}}_X{\hbox{-}} $module?

    Isomorphic to $ {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  } $ for some $ n $.

- What is a **locally free** $ {\mathcal{O}}_X $ module?

    Admits an open cover where $ { \left.{{{\mathcal{F}}}} \right|_{{U_i}} } $ is free.

- What is the **rank** of an $ {\mathcal{O}}_X{\hbox{-}} $module?

    If locally free, on some open set, the $ n $ appearing in $ { \left.{{{\mathcal{F}}}} \right|_{{U}} }_i \cong {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  } $.

- What is a **sheaf of ideals** on $ X $?

    An $ {\mathcal{O}}_X{\hbox{-}} $module $ {\mathcal{I}} $ where $ {\mathcal{I}}\leq {\mathcal{O}}_X $ is a subsheaf, so each $ {\mathcal{I}}(U) {~\trianglelefteq~}{\mathcal{O}}(U) $.

- What is the **sheaf hom**?

    For $ {\mathcal{F}}, {\mathcal{G}}\in {\mathsf{Sh}}(X, \mathsf{C}) $, the sheaf $ U\mapsto \mathop{\mathrm{Hom}}_{{ \left.{{{\mathcal{O}}_X}} \right|_{{U}} }}({ \left.{{{\mathcal{F}}}} \right|_{{U}} }, { \left.{{{\mathcal{G}}}} \right|_{{U}} }) $ (no need to sheafify).

- What is the **direct image** in $ {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $?

    For $ f: X\to Y $ in ringed spaces and $ {\mathcal{F}}\in   {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, take $ f_* {\mathcal{F}}\in   {}_{{\mathcal{O}}_Y}{\mathsf{Mod}} $

- What is the **inverse image** in $ {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $?

    For $ f:X\to Y $ and $ {\mathcal{G}}\in   {}_{{\mathcal{O}}_Y}{\mathsf{Mod}} $, $ f^* {\mathcal{G}}\coloneqq f^{-1}{\mathcal{G}}\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X $. I.e. base change $ f^{-1}G $ from $ f^{-1}{\mathcal{O}}_Y $ to $ {\mathcal{O}}_X $.

- What is the $ {\mathcal{O}}_X{\hbox{-}} $module associated to $ M\in {}_{A}{\mathsf{Mod}} $?

    $ \tilde M \in {\mathsf{Sh}}(\operatorname{Spec}A) $ where $ \tilde M(U) $ is the set of functions $ s: U\to \amalg_{p\in U} M_p $ such that $ s(p)\in M_p $ and $ s $ is locally a fraction $ m/f $ with $ m\in M, f\in A $. The stalks are the localizations, $ \tilde M_p = M_p $, and the global sections are $ M $.

    More precisely: for each $ p\in U $ there exists $ p\in V \subset U $ and $ m\in M, f\in A $ such that for each $ q\in V $, $ f\not \in q $ and $ s(q) = m/f $ in $ M_q $.

- What is a **quasicoherent sheaf**/$ {\mathcal{O}}_X{\hbox{-}} $module? :

    An $ {\mathcal{O}}_X{\hbox{-}} $module which is locally of the form $ \tilde M $, where $ \tilde M $ is the sheaf associated to $ M $.

    Admits an affine open cover $ \operatorname{Spec}A_i\rightrightarrows X $ where $ \exists M_i\in  {}_{A_i}{\mathsf{Mod}} $ with $ { \left.{{{\mathcal{F}}}} \right|_{{\tilde M_i}} } $.

    Equivalently, by a theorem of Serre, **locally** $ \exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow{\mathcal{F}} $.

- What is a **coherent sheaf**/ $ {\mathcal{O}}_X{\hbox{-}} $module? :

    Quasicoherent where $ \operatorname{Spec}A_i\rightrightarrows X $ and each $ M_i \in   {}_{A_i}{\mathsf{Mod}}^{\mathrm{fg}} $.

    Equivalently, by a theorem of Serre, $ \exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow{\mathcal{F}} $ with $ {\sharp}I, {\sharp}J < \infty $.

- Give an example of a sheaf that is not quasicoherent.

    For $ Y\leq X $ a closed subscheme, $ { \left.{{{\mathcal{O}}_X}} \right|_{{Y}} } $.

- Give an example of a sheaf that is not coherent.

    Take $ f:{\mathbf{A}}^1_{/ {k}}\to \operatorname{Spec}k $ and $ f_* {\mathcal{O}}_{{\mathbf{A}}^1_{/ {k}}} $ has global sections $ k[t]\not\in   {}_{k}{\mathsf{Mod}}^{\mathrm{fg}} $.

- Give an example of a quasicoherent but not coherent $ {\mathcal{O}}_X{\hbox{-}} $module.

    The constant sheaf $ \underline{{\mathcal{K}}} $ where $ U\mapsto K(X) $, the rational function field of $ X $.

- What is a consequence of an $ {\mathcal{O}}_X{\hbox{-}} $module being quasicoherent?

    For $ X $ affine, global sections is exact on sequences $ {\mathcal{F}}\hookrightarrow\bullet\twoheadrightarrow\bullet $ when $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $.

    Kernels, cokernels, images, extensions, pullbacks, and pushforwards along qcs are again quasicoherent.

- What is the **ideal sheaf**?

    For $ Y\leq X $ a closed subscheme with $ \iota: Y\hookrightarrow X $, defined by $ {\mathcal{I}}_Y \coloneqq\ker\qty{{\mathcal{O}}_X \xrightarrow{i^\sharp}i_* {\mathcal{O}}_Y} $. Always a qcoh sheaf of ideals on $ X $, and all such ideals arise this way.

- What is $ {\mathcal{O}}_X(n) $?

    For $ S $ a graded ring and $ X \coloneqq\mathop{\mathrm{Proj}}S $, $ {\mathcal{O}}_X(n)\coloneqq S(n)\tilde{} $ (the sheaf associated to a module).

    $ {\mathcal{O}}_X(1) $ is Serre's twisting sheaf, and if $ {\mathcal{F}}\in   {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $ then $ {\mathcal{F}}(n) \coloneqq{\mathcal{F}}\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n) $.

- For $ S $ a graded ring, $ X = \mathop{\mathrm{Proj}}S $, and $ {\mathcal{F}}\in {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, what is the graded $ S{\hbox{-}} $module associated to $ {\mathcal{F}} $?

    $ {{\Gamma}\qty{X; {\mathcal{F}}} } \coloneqq\bigoplus_{n\in {\mathbf{Z}}} {{\Gamma}\qty{X; {\mathcal{F}}(n)} } $.

- What is the **twisting sheaf** $ {\mathcal{O}}(1) $ on $ {\mathbf{P}}^n_{/ {Y}} $?

    Take $ g^*({\mathcal{O}}(1)) $ where $ g:{\mathbf{P}}^n_{/ {Y}} \to {\mathbf{P}}^n_{/ {{\mathbf{Z}}}} $.

- What is a **very ample** invertible sheaf?

    For $ X $ over $ Y $, $ {\mathcal{L}}\in \operatorname{Pic}(X) $ is very ample iff $ \exists \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ such that $ \iota^* {\mathcal{O}}(1) \cong {\mathcal{L}} $.

- Why is a scheme $ X $ over $ Y $ projective iff proper?

    Projective implies proper: take a closed immersion $ \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ to get $ \iota^* {\mathcal{O}}(1)\in \operatorname{Pic}(X)^\mathrm{va} $.

    Conversely if proper, take $ {\mathcal{L}}\in \operatorname{Pic}(X)^{\mathrm{va}} $ to get $ {\mathcal{L}}\cong \iota^* {\mathcal{O}}(1) $ for some immersion $ \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ for some $ n $ -- but $ \iota(X) $ is closed, so $ \iota $ is a *closed* immersion, making $ X $ projective.

- What does it mean for an $ {\mathcal{O}}_X $ module to be **globally generated** (or **generated by global sections**)?

    There exists a family of sections $ \left\{{s_i}\right\}_{i\in I} \subseteq {{\Gamma}\qty{X; {\mathcal{F}}} } $ where for each $ x\in X $ the images of $ s_i $ in $ {\mathcal{F}}_x $ generate that stalk as an $ {\mathcal{O}}_{X, x}{\hbox{-}} $module.

    Equivalently, $ {\mathcal{F}} $ is the quotient of a free sheaf: $ \exists \bigoplus_{i\in I}{\mathcal{O}}_X\twoheadrightarrow{\mathcal{F}} $.

- Give examples of globally generated sheaves.

    Example: any $ {\mathcal{F}}\in {\mathsf{QCoh}}(\operatorname{Spec}A) $ -- write $ {\mathcal{F}}\cong M\tilde{} $ and take any set of generators for $ M\in  {}_{A}{\mathsf{Mod}} $.

- What is a major result regarding global generation?

    For $ X $ projective over a Noetherian scheme $ A $, $ {\mathcal{O}}(1) $ a very ample invertible sheaf on $ X $, $ {\mathcal{F}}\in {\mathsf{Coh}}(X) $, there exists some $ N_0 $ such that $ {\mathcal{F}}(n) $ is globally generated by a finite number of sections for all $ n\geq N_0 $.

- What is the **Euler characteristic** of an $ {\mathcal{O}}_X $ module?

    $ \chi(X; {\mathcal{F}}) \coloneqq\sum_i (-1)^i h^i(X; {\mathcal{F}}) $.

- What is the **Hilbert polynomial** of an $ {\mathcal{O}}_X $ module?

    Using that $ \chi(X; {\mathcal{F}}(n)) $ is some polynomial $ p(n) $ in $ n $, take $ p $ to be the Hilbert polynomial.
