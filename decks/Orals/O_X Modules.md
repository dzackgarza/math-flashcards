---
title: "Orals::O_X Modules"
---

::: {.front card-id="card-8df45a95ad038e48"}
What is an $ O_X{\hbox{-}} $modules? :
:::

::: {.back card-id="card-8df45a95ad038e48"}
$ {\mathcal{F}}\in {\mathsf{Sh}}(X) $ where $ {\mathcal{F}}(U)\in   {}_{{\mathcal{O}}_X(U)}{\mathsf{Mod}} $ with compatible restrictions $ (rm)\mathrel{\Big|}_V = { \left.{{r}} \right|_{{V}} } { \left.{{m}} \right|_{{V}} } $.
:::

::: {.front card-id="card-ba56128ca287831c"}
What is the **tensor product** of two $ {\mathcal{O}}_X{\hbox{-}} $modules?
:::

::: {.back card-id="card-ba56128ca287831c"}
Sheafify $ U\mapsto {\mathcal{F}}(U) \otimes_{{\mathcal{O}}_X(U)} {\mathcal{G}}(U) $.
:::

::: {.front card-id="card-7e9dc536db4d8267"}
What is a **free** $ {\mathcal{O}}_X{\hbox{-}} $module?
:::

::: {.back card-id="card-7e9dc536db4d8267"}
Isomorphic to $ {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  } $ for some $ n $.
:::

::: {.front card-id="card-f5daaf777e5093e5"}
What is a **locally free** $ {\mathcal{O}}_X $ module?
:::

::: {.back card-id="card-f5daaf777e5093e5"}
Admits an open cover where $ { \left.{{{\mathcal{F}}}} \right|_{{U_i}} } $ is free.
:::

::: {.front card-id="card-7ea20bc415140836"}
What is the **rank** of an $ {\mathcal{O}}_X{\hbox{-}} $module?
:::

::: {.back card-id="card-7ea20bc415140836"}
If locally free, on some open set, the $ n $ appearing in $ { \left.{{{\mathcal{F}}}} \right|_{{U}} }_i \cong {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  } $.
:::

::: {.front card-id="card-041465065808b2ca"}
What is a **sheaf of ideals** on $ X $?
:::

::: {.back card-id="card-041465065808b2ca"}
An $ {\mathcal{O}}_X{\hbox{-}} $module $ {\mathcal{I}} $ where $ {\mathcal{I}}\leq {\mathcal{O}}_X $ is a subsheaf, so each $ {\mathcal{I}}(U) {~\trianglelefteq~}{\mathcal{O}}(U) $.
:::

::: {.front card-id="card-a0b5fb9f7c4c63c9"}
What is the **sheaf hom**?
:::

::: {.back card-id="card-a0b5fb9f7c4c63c9"}
For $ {\mathcal{F}}, {\mathcal{G}}\in {\mathsf{Sh}}(X, \mathsf{C}) $, the sheaf $ U\mapsto \mathop{\mathrm{Hom}}_{{ \left.{{{\mathcal{O}}_X}} \right|_{{U}} }}({ \left.{{{\mathcal{F}}}} \right|_{{U}} }, { \left.{{{\mathcal{G}}}} \right|_{{U}} }) $ (no need to sheafify).
:::

::: {.front card-id="card-1c0674319a19d9fa"}
What is the **direct image** in $ {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $?
:::

::: {.back card-id="card-1c0674319a19d9fa"}
For $ f: X\to Y $ in ringed spaces and $ {\mathcal{F}}\in   {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, take $ f_* {\mathcal{F}}\in   {}_{{\mathcal{O}}_Y}{\mathsf{Mod}} $
:::

::: {.front card-id="card-26737bcb87ae4726"}
What is the **inverse image** in $ {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $?
:::

::: {.back card-id="card-26737bcb87ae4726"}
For $ f:X\to Y $ and $ {\mathcal{G}}\in   {}_{{\mathcal{O}}_Y}{\mathsf{Mod}} $, $ f^* {\mathcal{G}}\coloneqq f^{-1}{\mathcal{G}}\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X $. I.e. base change $ f^{-1}G $ from $ f^{-1}{\mathcal{O}}_Y $ to $ {\mathcal{O}}_X $.
:::

::: {.front card-id="card-2f0923dae6d93520"}
What is the $ {\mathcal{O}}_X{\hbox{-}} $module associated to $ M\in {}_{A}{\mathsf{Mod}} $?
:::

::: {.back card-id="card-2f0923dae6d93520"}
$ \tilde M \in {\mathsf{Sh}}(\operatorname{Spec}A) $ where $ \tilde M(U) $ is the set of functions $ s: U\to \amalg_{p\in U} M_p $ such that $ s(p)\in M_p $ and $ s $ is locally a fraction $ m/f $ with $ m\in M, f\in A $. The stalks are the localizations, $ \tilde M_p = M_p $, and the global sections are $ M $.

More precisely: for each $ p\in U $ there exists $ p\in V \subset U $ and $ m\in M, f\in A $ such that for each $ q\in V $, $ f\not \in q $ and $ s(q) = m/f $ in $ M_q $.
:::

::: {.front card-id="card-70da298d7eaf3e5c"}
What is a **quasicoherent sheaf**/$ {\mathcal{O}}_X{\hbox{-}} $module? :
:::

::: {.back card-id="card-70da298d7eaf3e5c"}
An $ {\mathcal{O}}_X{\hbox{-}} $module which is locally of the form $ \tilde M $, where $ \tilde M $ is the sheaf associated to $ M $.

Admits an affine open cover $ \operatorname{Spec}A_i\rightrightarrows X $ where $ \exists M_i\in  {}_{A_i}{\mathsf{Mod}} $ with $ { \left.{{{\mathcal{F}}}} \right|_{{\tilde M_i}} } $.

Equivalently, by a theorem of Serre, **locally** $ \exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow{\mathcal{F}} $.
:::

::: {.front card-id="card-d64ff182851952ed"}
What is a **coherent sheaf**/ $ {\mathcal{O}}_X{\hbox{-}} $module? :
:::

::: {.back card-id="card-d64ff182851952ed"}
Quasicoherent where $ \operatorname{Spec}A_i\rightrightarrows X $ and each $ M_i \in   {}_{A_i}{\mathsf{Mod}}^{\mathrm{fg}} $.

Equivalently, by a theorem of Serre, $ \exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow{\mathcal{F}} $ with $ {\sharp}I, {\sharp}J < \infty $.
:::

::: {.front card-id="card-01c0cd5b5e6565ed"}
Give an example of a sheaf that is not quasicoherent.
:::

::: {.back card-id="card-01c0cd5b5e6565ed"}
For $ Y\leq X $ a closed subscheme, $ { \left.{{{\mathcal{O}}_X}} \right|_{{Y}} } $.
:::

::: {.front card-id="card-7b0a991f2503ff89"}
Give an example of a sheaf that is not coherent.
:::

::: {.back card-id="card-7b0a991f2503ff89"}
Take $ f:{\mathbf{A}}^1_{/ {k}}\to \operatorname{Spec}k $ and $ f_* {\mathcal{O}}_{{\mathbf{A}}^1_{/ {k}}} $ has global sections $ k[t]\not\in   {}_{k}{\mathsf{Mod}}^{\mathrm{fg}} $.
:::

::: {.front card-id="card-d1af342442df2ccd"}
Give an example of a quasicoherent but not coherent $ {\mathcal{O}}_X{\hbox{-}} $module.
:::

::: {.back card-id="card-d1af342442df2ccd"}
The constant sheaf $ \underline{{\mathcal{K}}} $ where $ U\mapsto K(X) $, the rational function field of $ X $.
:::

::: {.front card-id="card-c07a818203520df1"}
What is a consequence of an $ {\mathcal{O}}_X{\hbox{-}} $module being quasicoherent?
:::

::: {.back card-id="card-c07a818203520df1"}
For $ X $ affine, global sections is exact on sequences $ {\mathcal{F}}\hookrightarrow\bullet\twoheadrightarrow\bullet $ when $ {\mathcal{F}}\in {\mathsf{QCoh}}(X) $.

Kernels, cokernels, images, extensions, pullbacks, and pushforwards along qcs are again quasicoherent.
:::

::: {.front card-id="card-9b52dcea83c960e1"}
What is the **ideal sheaf**?
:::

::: {.back card-id="card-9b52dcea83c960e1"}
For $ Y\leq X $ a closed subscheme with $ \iota: Y\hookrightarrow X $, defined by $ {\mathcal{I}}_Y \coloneqq\ker\qty{{\mathcal{O}}_X \xrightarrow{i^\sharp}i_* {\mathcal{O}}_Y} $. Always a qcoh sheaf of ideals on $ X $, and all such ideals arise this way.
:::

::: {.front card-id="card-dab506d58c11eaf9"}
What is $ {\mathcal{O}}_X(n) $?
:::

::: {.back card-id="card-dab506d58c11eaf9"}
For $ S $ a graded ring and $ X \coloneqq\mathop{\mathrm{Proj}}S $, $ {\mathcal{O}}_X(n)\coloneqq S(n)\tilde{} $ (the sheaf associated to a module).

$ {\mathcal{O}}_X(1) $ is Serre's twisting sheaf, and if $ {\mathcal{F}}\in   {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $ then $ {\mathcal{F}}(n) \coloneqq{\mathcal{F}}\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n) $.
:::

::: {.front card-id="card-c5f79fa6fffa2efc"}
For $ S $ a graded ring, $ X = \mathop{\mathrm{Proj}}S $, and $ {\mathcal{F}}\in {}_{{\mathcal{O}}_X}{\mathsf{Mod}} $, what is the graded $ S{\hbox{-}} $module associated to $ {\mathcal{F}} $?
:::

::: {.back card-id="card-c5f79fa6fffa2efc"}
$ {{\Gamma}\qty{X; {\mathcal{F}}} } \coloneqq\bigoplus_{n\in {\mathbf{Z}}} {{\Gamma}\qty{X; {\mathcal{F}}(n)} } $.
:::

::: {.front card-id="card-0993d61182a2d5f4"}
What is the **twisting sheaf** $ {\mathcal{O}}(1) $ on $ {\mathbf{P}}^n_{/ {Y}} $?
:::

::: {.back card-id="card-0993d61182a2d5f4"}
Take $ g^*({\mathcal{O}}(1)) $ where $ g:{\mathbf{P}}^n_{/ {Y}} \to {\mathbf{P}}^n_{/ {{\mathbf{Z}}}} $.
:::

::: {.front card-id="card-996db5f3b6601367"}
What is a **very ample** invertible sheaf?
:::

::: {.back card-id="card-996db5f3b6601367"}
For $ X $ over $ Y $, $ {\mathcal{L}}\in \operatorname{Pic}(X) $ is very ample iff $ \exists \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ such that $ \iota^* {\mathcal{O}}(1) \cong {\mathcal{L}} $.
:::

::: {.front card-id="card-6434f1ec713aa932"}
Why is a scheme $ X $ over $ Y $ projective iff proper?
:::

::: {.back card-id="card-6434f1ec713aa932"}
Projective implies proper: take a closed immersion $ \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ to get $ \iota^* {\mathcal{O}}(1)\in \operatorname{Pic}(X)^\mathrm{va} $.

Conversely if proper, take $ {\mathcal{L}}\in \operatorname{Pic}(X)^{\mathrm{va}} $ to get $ {\mathcal{L}}\cong \iota^* {\mathcal{O}}(1) $ for some immersion $ \iota: X\to {\mathbf{P}}^n_{/ {Y}} $ for some $ n $ -- but $ \iota(X) $ is closed, so $ \iota $ is a *closed* immersion, making $ X $ projective.
:::

::: {.front card-id="card-5c26a4c9e18c5228"}
What does it mean for an $ {\mathcal{O}}_X $ module to be **globally generated** (or **generated by global sections**)?
:::

::: {.back card-id="card-5c26a4c9e18c5228"}
There exists a family of sections $ \left\{{s_i}\right\}_{i\in I} \subseteq {{\Gamma}\qty{X; {\mathcal{F}}} } $ where for each $ x\in X $ the images of $ s_i $ in $ {\mathcal{F}}_x $ generate that stalk as an $ {\mathcal{O}}_{X, x}{\hbox{-}} $module.

Equivalently, $ {\mathcal{F}} $ is the quotient of a free sheaf: $ \exists \bigoplus_{i\in I}{\mathcal{O}}_X\twoheadrightarrow{\mathcal{F}} $.
:::

::: {.front card-id="card-6078c0a2248b7c1b"}
Give examples of globally generated sheaves.
:::

::: {.back card-id="card-6078c0a2248b7c1b"}
Example: any $ {\mathcal{F}}\in {\mathsf{QCoh}}(\operatorname{Spec}A) $ -- write $ {\mathcal{F}}\cong M\tilde{} $ and take any set of generators for $ M\in  {}_{A}{\mathsf{Mod}} $.
:::

::: {.front card-id="card-36e874ed79b4bec1"}
What is a major result regarding global generation?
:::

::: {.back card-id="card-36e874ed79b4bec1"}
For $ X $ projective over a Noetherian scheme $ A $, $ {\mathcal{O}}(1) $ a very ample invertible sheaf on $ X $, $ {\mathcal{F}}\in {\mathsf{Coh}}(X) $, there exists some $ N_0 $ such that $ {\mathcal{F}}(n) $ is globally generated by a finite number of sections for all $ n\geq N_0 $.
:::

::: {.front card-id="card-a335a1700d07eb09"}
What is the **Euler characteristic** of an $ {\mathcal{O}}_X $ module?
:::

::: {.back card-id="card-a335a1700d07eb09"}
$ \chi(X; {\mathcal{F}}) \coloneqq\sum_i (-1)^i h^i(X; {\mathcal{F}}) $.
:::

::: {.front card-id="card-c1ffa65f50144241"}
What is the **Hilbert polynomial** of an $ {\mathcal{O}}_X $ module?
:::

::: {.back card-id="card-c1ffa65f50144241"}
Using that $ \chi(X; {\mathcal{F}}(n)) $ is some polynomial $ p(n) $ in $ n $, take $ p $ to be the Hilbert polynomial.
:::
