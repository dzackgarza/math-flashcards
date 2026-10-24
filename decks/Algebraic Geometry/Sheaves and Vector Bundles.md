---
title: "Algebraic Geometry::Sheaves and Vector Bundles"
---

::: {.front card-id="card-c30e1b1de3ce90bd" tags="definition"}
What is a **derivation**?
:::

::: {.back card-id="card-c30e1b1de3ce90bd"}
$d\in \mathop{\mathrm{Der}}_A(B, M) \iff d$ is additive and $d(b_1b_2) = d(b_1)b_2 + b_1d(b_2)$ where $d(a) = 0$ for all $a\in A$.
:::

::: {.front card-id="card-9fcd3600930c58fb"}
What is the **sheaf of differentials** or **relative differential forms**?
:::

::: {.back card-id="card-9fcd3600930c58fb"}
For $f:X\to Y$, embed $X$ as a locally closed subscheme $X\hookrightarrow W \coloneqq\Delta_{X/Y}$ with sheaf of ideals $\mci$ and define $\Omega_{X/Y} \coloneqq\Delta^*(\mci/\mci^2) \in \QCoh(X)$. The local derivations glue to $d:{\mathcal{O}}_X\to \Omega_{X/Y}$.
:::

::: {.front card-id="card-8c48673ca22f6b18"}
What are the two exact sequences for sheaves (modules) of differentials?
:::

::: {.back card-id="card-8c48673ca22f6b18"}
The composition exact sequence: for $X \xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \rightarrow \Omega_{X / Y} \rightarrow 0.$$
For modules: for $A\to B\to C$,
$$\Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow \Omega_{C / B} \rightarrow 0 \in   {}_{C}\Mod$$
The "conormal" exact sequence: for $X\to Y$ and $Z\leq X$ a closed subscheme with ideal sheaf $\mci$,
$$\mathscr{I} / \mathscr{I}^2 \stackrel{\delta}{\rightarrow} \Omega_{X / Y} \otimes \mathcal{O}_Z \rightarrow \Omega_{Z / Y} \rightarrow 0.$$
For modules: for $B\in  \mathsf{Alg}_{A}, I\normal B, C\coloneqq B/I$,
$$I / I^2 \stackrel{\delta}{\rightarrow} \Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow 0\in   {}_{C}\Mod$$
:::

::: {.front card-id="card-1f21f65d8810cd17"}
What is the **conormal exact sequence**, e.g. for an immersion $C\hookrightarrow S$?
:::

::: {.back card-id="card-1f21f65d8810cd17"}
How to derive: for a closed immersion $j: X\hookrightarrow Y$ of smooth varieties,
$${\mathbf{T}}_X \hookrightarrow j^*{\mathbf{T}}_Y \twoheadrightarrow N_{X/Y} \quad\underset{\text{dualize}}{\leadsto}\quad N_{X/Y} {}^{ \vee }\to j^*\Omega_{Y/Z} \twoheadrightarrow\Omega_{X/Z}\to 0.$$
At the level of sheaves on $C$, for $\iota: C\hookrightarrow S$,
$$N_{C/S} {}^{ \vee }\to \iota^*\Omega_{S/k} \twoheadrightarrow\Omega_{C/k}\to 0 \qquad \in \Sh(C)$$
where $N_{C/S} {}^{ \vee }\coloneqq I_C/I_C^2$ (the first map is injective when $C$ and $S$ are smooth). This is a sheaf version of: if $B\in  \mathsf{Alg}_{R}$ and $I \normal B$,
$$I/I^2 \to \Omega_{B/R}\otimes_B B/I \twoheadrightarrow\Omega_{(B/I)/R}\to 0 \qquad\in  {}_{B/I}\Mod$$
For $C \subseteq S$ a closed subscheme and $f:S\to T$, can rewrite this as
$$ \mci_C / \mci_C^2 \to \Omega_{S/T} \otimes{\mathcal{O}}_C \twoheadrightarrow\Omega_{C/T}\to 0 \qquad \in \Sh_C$$
:::

::: {.front card-id="card-25c14144c18e5ef3"}
What is the **Euler exact sequence**?
:::

::: {.back card-id="card-25c14144c18e5ef3"}
For $X \coloneqq{\mathbf{P}}^n _{/ {A}}$, dualize ${\mathcal{O}}_X\hookrightarrow{\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathbf{T}}_X$ to get the sequence
$$\Omega^1_{X}\hookrightarrow{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathcal{O}}_X$$
:::

::: {.front card-id="card-884b60a5d4ee268a"}
What is the composition exact sequence for $X\to Y\to Z$?
:::

::: {.back card-id="card-884b60a5d4ee268a"}
At the level of sheaves,
$$f^* \Omega_{Y/Z} \to \Omega_{X/Z} \to \Omega_{X/Y} \to 0 \qquad \in \Sh_X$$
How to remember:
:::

::: {.front card-id="card-a85d85454b4f4984"}
Discuss relative differentials?
:::

::: {.back card-id="card-a85d85454b4f4984"}
For $f: M\to S$, $\Omega^*_M / \left\langle{f^* \Omega^1_S}\right\rangle$, a quotient of a sheaf of dg ${\mathcal{O}}_M\dash$algebras.

Fiber over $s\in S$ is the de Rham sheaf complex of the fiber $M_s$.

Resolves $f^{-1}{\mathcal{O}}_S$ by coherent ${\mathcal{O}}_M$ modules
:::

::: {.front card-id="card-8df45a95ad038e48" tags="definition"}
What is an ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-8df45a95ad038e48"}
A sheaf $\mcf$ of abelian groups on $X$ where each $\mcf(U)\in   {}_{{\mathcal{O}}_X(U)}\Mod$ and the restriction maps respect scalar multiplication: $(rm)\mathrel{\Big|}_V = { \left.{{r}} \right|_{{V}} } { \left.{{m}} \right|_{{V}} }$.
:::

::: {.front card-id="card-ba56128ca287831c"}
What is the **tensor product** of two ${\mathcal{O}}_X\dash$modules?
:::

::: {.back card-id="card-ba56128ca287831c"}
Sheafify $U\mapsto \mcf(U) \otimes_{{\mathcal{O}}_X(U)} \mcg(U)$.
:::

::: {.front card-id="card-7e9dc536db4d8267"}
What is a **free** ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-7e9dc536db4d8267"}
Isomorphic to a direct sum $\bigoplus_{i\in I}{\mathcal{O}}_X$ of copies of ${\mathcal{O}}_X$; it has rank $n$ if ${\sharp}I = n < \infty$, i.e. $\mcf\cong{\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  }$.
:::

::: {.front card-id="card-f5daaf777e5093e5"}
What is a **locally free** ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-f5daaf777e5093e5"}
Admits an open cover $\left\{{U_i}\right\}$ of $X$ where each ${ \left.{{\mcf}} \right|_{{U_i}} }$ is a free ${\mathcal{O}}_{U_i}\dash$module. It is locally free of rank $n$ if there are ${\mathcal{O}}_{U_i}$-module isomorphisms $\rho_i: { \left.{{\mcf}} \right|_{{U_i}} } \cong {\mathcal{O}}_{U_i}{ {}^{ \scriptscriptstyle\oplus^{n} }  }$.

Then each stalk $\mcf_x$ is a free ${\mathcal{O}}_{X, x}\dash$module. The converse holds for $\mcf$ of finite presentation (e.g. coherent on a locally Noetherian scheme), but not in general.
:::

::: {.front card-id="card-7ea20bc415140836"}
What is the **rank** of an ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-7ea20bc415140836"}
If locally free, on some open set, the $n$ appearing in ${ \left.{{\mcf}} \right|_{{U}} }_i \cong {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  }$.
:::

::: {.front card-id="card-041465065808b2ca"}
What is an **ideal sheaf** (sheaf of ideals) on $X$?
:::

::: {.back card-id="card-041465065808b2ca"}
An ${\mathcal{O}}_X\dash$submodule $\mci\leq {\mathcal{O}}_X$, so each $\mci(U) \normal{\mathcal{O}}_X(U)$.

For $\iota: Y\hookrightarrow X$ the inclusion of a closed subscheme, its ideal sheaf is $\mci_Y \coloneqq\ker\qty{{\mathcal{O}}_X \xrightarrow{\iota^\sharp}\iota_* {\mathcal{O}}_Y}$. It is always a quasi-coherent sheaf of ideals on $X$, and every quasi-coherent sheaf of ideals is $\mci_Y$ for a unique closed subscheme $Y$.
:::

::: {.front card-id="card-a0b5fb9f7c4c63c9" tags="definition"}
What is the **sheaf hom**?
:::

::: {.back card-id="card-a0b5fb9f7c4c63c9"}
For ${\mathcal{O}}_X\dash$modules $\mcf, \mcg$, the sheaf $\mathop{\mathcal{H}\! \mathit{om}}_{{\mathcal{O}}_X}(\mcf, \mcg)$ given by $U\mapsto \mathop{\mathrm{Hom}}_{{ \left.{{{\mathcal{O}}_X}} \right|_{{U}} }}({ \left.{{\mcf}} \right|_{{U}} }, { \left.{{\mcg}} \right|_{{U}} })$ (no need to sheafify). It is again an ${\mathcal{O}}_X\dash$module.
:::

::: {.front card-id="card-1c0674319a19d9fa"}
What is the **direct image** in ${}_{{\mathcal{O}}_X}\Mod$?
:::

::: {.back card-id="card-1c0674319a19d9fa"}
For $f: X\to Y$ in ringed spaces and $\mcf\in   {}_{{\mathcal{O}}_X}\Mod$, take $f_* \mcf\in   {}_{{\mathcal{O}}_Y}\Mod$
:::

::: {.front card-id="card-26737bcb87ae4726"}
What is the **inverse image** in ${}_{{\mathcal{O}}_X}\Mod$?
:::

::: {.back card-id="card-26737bcb87ae4726"}
For $f:X\to Y$ and $\mcg\in   {}_{{\mathcal{O}}_Y}\Mod$, $f^* \mcg\coloneqq f^{-1}\mcg\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X$. I.e. base change $f^{-1}G$ from $f^{-1}{\mathcal{O}}_Y$ to ${\mathcal{O}}_X$.
:::

::: {.front card-id="card-2f0923dae6d93520"}
What is the ${\mathcal{O}}_X\dash$module associated to $M\in {}_{A}\Mod$?
:::

::: {.back card-id="card-2f0923dae6d93520"}
$\tilde M \in \Sh(\operatorname{Spec}A)$ where $\tilde M(U)$ is the set of functions $s: U\to \amalg_{p\in U} M_p$ such that $s(p)\in M_p$ and $s$ is locally a fraction $m/f$ with $m\in M, f\in A$. The stalks are the localizations, $\tilde M_p = M_p$, and the global sections are $M$.

More precisely: for each $p\in U$ there exists $p\in V \subset U$ and $m\in M, f\in A$ such that for each $q\in V$, $f\not \in q$ and $s(q) = m/f$ in $M_q$.
:::

::: {.front card-id="card-70da298d7eaf3e5c"}
What is a **quasicoherent sheaf**/${\mathcal{O}}_X\dash$module? :
:::

::: {.back card-id="card-70da298d7eaf3e5c"}
An ${\mathcal{O}}_X\dash$module which is locally of the form $\tilde M$, where $\tilde M$ is the sheaf associated to $M$.

Admits an affine open cover $\operatorname{Spec}A_i\rightrightarrows X$ where $\exists M_i\in  {}_{A_i}\Mod$ with ${ \left.{{\mcf}} \right|_{{\tilde M_i}} }$.

Equivalently, by a theorem of Serre, **locally** $\exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow\mcf$.
:::

::: {.front card-id="card-d64ff182851952ed"}
What is a **coherent sheaf**/ ${\mathcal{O}}_X\dash$module? :
:::

::: {.back card-id="card-d64ff182851952ed"}
Quasicoherent where $\operatorname{Spec}A_i\rightrightarrows X$ and each $M_i \in   {}_{A_i}\Mod^\fg$.

Equivalently, by a theorem of Serre, $\exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow\mcf$ with ${\sharp}I, {\sharp}J < \infty$.
:::

::: {.front card-id="card-01c0cd5b5e6565ed"}
Give an example of a sheaf that is not quasicoherent.
:::

::: {.back card-id="card-01c0cd5b5e6565ed"}
For $Y\leq X$ a closed subscheme, ${ \left.{{{\mathcal{O}}_X}} \right|_{{Y}} }$.
:::

::: {.front card-id="card-7b0a991f2503ff89"}
Give an example of a sheaf that is not coherent.
:::

::: {.back card-id="card-7b0a991f2503ff89"}
Take $f:{\mathbf{A}}^1_{/ {k}}\to \operatorname{Spec}k$ and $f_* {\mathcal{O}}_{{\mathbf{A}}^1_{/ {k}}}$ has global sections $k[t]\not\in   {}_{k}\Mod^\fg$.
:::

::: {.front card-id="card-d1af342442df2ccd"}
Give an example of a quasicoherent but not coherent ${\mathcal{O}}_X\dash$module.
:::

::: {.back card-id="card-d1af342442df2ccd"}
The constant sheaf $\underline{\mck}$ where $U\mapsto K(X)$, the rational function field of $X$.
:::

::: {.front card-id="card-c07a818203520df1"}
What is a consequence of an ${\mathcal{O}}_X\dash$module being quasicoherent?
:::

::: {.back card-id="card-c07a818203520df1"}
For $X$ affine, global sections is exact on sequences $\mcf\hookrightarrow\bullet\twoheadrightarrow\bullet$ when $\mcf\in \QCoh(X)$.

Kernels, cokernels, images, extensions, pullbacks, and pushforwards along qcs are again quasicoherent.
:::

::: {.front card-id="card-dab506d58c11eaf9"}
What is ${\mathcal{O}}_X(n)$?
:::

::: {.back card-id="card-dab506d58c11eaf9"}
For $S$ a graded ring and $X \coloneqq\mathop{\mathrm{Proj}}S$, ${\mathcal{O}}_X(n)\coloneqq S(n)\tilde{}$ (the sheaf associated to a module), where $S(n)$ (also written $S[n]$) is the shifted graded module with $S(n)_d = S_{n+d}$.

${\mathcal{O}}_X(1)$ is Serre's twisting sheaf, and if $\mcf\in   {}_{{\mathcal{O}}_X}\Mod$ then $\mcf(n) \coloneqq\mcf\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n)$.
:::

::: {.front card-id="card-c5f79fa6fffa2efc"}
For $S$ a graded ring, $X = \mathop{\mathrm{Proj}}S$, and $\mcf\in {}_{{\mathcal{O}}_X}\Mod$, what is the graded $S\dash$module associated to $\mcf$?
:::

::: {.back card-id="card-c5f79fa6fffa2efc"}
${{\Gamma}\qty{X; \mcf} } \coloneqq\bigoplus_{n\in \ZZ} {{\Gamma}\qty{X; \mcf(n)} }$.
:::

::: {.front card-id="card-0993d61182a2d5f4"}
What is the **twisting sheaf** ${\mathcal{O}}(1)$ on ${\mathbf{P}}^n_{/ {Y}}$?
:::

::: {.back card-id="card-0993d61182a2d5f4"}
${\mathcal{O}}_{{\mathbf{P}}^n_{/ {Y}}}(1) \coloneqq g^* {\mathcal{O}}_{{\mathbf{P}}^n_{/ {\ZZ}}}(1)$ where $g:{\mathbf{P}}^n_{/ {Y}} \to {\mathbf{P}}^n_{/ {\ZZ}}$ is the projection.
:::

::: {.front card-id="card-996db5f3b6601367"}
What is a **very ample** invertible sheaf?
:::

::: {.back card-id="card-996db5f3b6601367"}
For $X$ over $Y$, $\mcl\in \operatorname{Pic}(X)$ is very ample relative to $Y$ iff there is an immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ over $Y$ for some $n$ such that $\iota^* {\mathcal{O}}(1) \cong \mcl$. For $Y = \operatorname{Spec}A$, this is equivalent to the existence of sections $\left\{{s_0,\cdots, s_n}\right\}\subseteq H^0(X; \mcl)$ generating $\mcl$ such that $x\mapsto {\left[ {s_0(x): \cdots : s_n(x)} \right]}$ is an immersion.
:::

::: {.front card-id="card-6434f1ec713aa932"}
Why is a scheme $X$ over a Noetherian scheme $Y$ projective iff it is proper and admits a very ample invertible sheaf relative to $Y$?
:::

::: {.back card-id="card-6434f1ec713aa932"}
Projective implies proper since ${\mathbf{P}}^n_{/ {Y}}\to Y$ is proper and closed immersions are proper; a closed immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ gives $\iota^* {\mathcal{O}}(1)\in \operatorname{Pic}(X)^\mathrm{va}$.

Conversely if proper, take $\mcl\in \operatorname{Pic}(X)^{\mathrm{va}}$ to get $\mcl\cong \iota^* {\mathcal{O}}(1)$ for some immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ for some $n$ -- but $\iota(X)$ is closed, so $\iota$ is a *closed* immersion, making $X$ projective.

Proper alone does not imply projective: Hironaka constructed smooth proper threefolds over $\CC$ that are not projective.
:::

::: {.front card-id="card-5c26a4c9e18c5228"}
What does it mean for an ${\mathcal{O}}_X$ module to be **globally generated** (or **generated by global sections**)?
:::

::: {.back card-id="card-5c26a4c9e18c5228"}
There exists a family of sections $\left\{{s_i}\right\}_{i\in I} \subseteq {{\Gamma}\qty{X; \mcf} }$ where for each $x\in X$ the images of $s_i$ in $\mcf_x$ generate that stalk as an ${\mathcal{O}}_{X, x}\dash$module.

Equivalently, $\mcf$ is the quotient of a free sheaf: $\exists \bigoplus_{i\in I}{\mathcal{O}}_X\twoheadrightarrow\mcf$.

For $\mcl\in \operatorname{Pic}(X)$: for every $x\in X$ there is a section $s\in H^0(X; \mcl)$ not vanishing at $x$, i.e. $\mcl$ is base-point free.
:::

::: {.front card-id="card-6078c0a2248b7c1b"}
Give examples of globally generated sheaves.
:::

::: {.back card-id="card-6078c0a2248b7c1b"}
Example: any $\mcf\in \QCoh(\operatorname{Spec}A)$ -- write $\mcf\cong M\tilde{}$ and take any set of generators for $M\in  {}_{A}\Mod$.
:::

::: {.front card-id="card-36e874ed79b4bec1"}
What is a major result regarding global generation?
:::

::: {.back card-id="card-36e874ed79b4bec1"}
For $X$ projective over a Noetherian scheme $A$, ${\mathcal{O}}(1)$ a very ample invertible sheaf on $X$, $\mcf\in \Coh(X)$, there exists some $N_0$ such that $\mcf(n)$ is globally generated by a finite number of sections for all $n\geq N_0$.
:::

::: {.front card-id="card-a335a1700d07eb09"}
What is the **Euler characteristic** of an ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-a335a1700d07eb09"}
$\chi(X; \mcf) \coloneqq\sum_i (-1)^i h^i(X; \mcf)$.
:::

::: {.front card-id="card-c1ffa65f50144241"}
What is the **Hilbert polynomial** of an ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-c1ffa65f50144241"}
Using that $\chi(X; \mcf(n))$ is some polynomial $p(n)$ in $n$, take $p$ to be the Hilbert polynomial.
:::

::: {.front card-id="card-37be5dabde736ed0" tags="definition"}
What is: Quasi-coherent and coherent sheaves,
:::

::: {.back card-id="card-37be5dabde736ed0"}
An $\mathcal O_X$-module $F$ is quasi-coherent if every point has an affine neighborhood $U=\operatorname{Spec}A$ with $F|_U\cong\widetilde M$ for an $A$-module $M$. On a locally Noetherian scheme, $F$ is coherent if locally $M$ is a finite $A$-module.
:::

::: {.front card-id="card-eeb89ede8813d491" tags="definition"}
What is: Construction of $\mathcal{O}_X$-modules,
:::

::: {.back card-id="card-eeb89ede8813d491"}
For an $A$-module $M$ on $U=\operatorname{Spec}A$, the associated sheaf $\widetilde M$ is determined by $\widetilde M(D(f))=M_f$. More general $\mathcal O_X$-modules are obtained by gluing modules on open subsets with compatible isomorphisms on overlaps.
:::

::: {.front card-id="card-4cd160edee37a085" tags="definition"}
What is: Invertible sheaves and vector bundles
:::

::: {.back card-id="card-4cd160edee37a085"}
An invertible sheaf is an $\mathcal O_X$-module locally isomorphic to $\mathcal O_X$; it is a locally free sheaf of rank one. A vector bundle of rank $r$ is a scheme over $X$ locally isomorphic to $\mathbb A_X^r$ with linear transition maps; it corresponds to a locally free sheaf of rank $r$.
:::

::: {.front card-id="card-cbfb24232131f375" tags="definition"}
What is: module of relative differential forms
:::

::: {.back card-id="card-cbfb24232131f375"}
The module of Kähler differentials $\Omega_{A/R}$ is generated by symbols $da$ subject to additivity, $d(ab)=a\,db+b\,da$, and $dr=0$ for $r\in R$. Its universal property is $\operatorname{Hom}_A(\Omega_{A/R},M)\cong\operatorname{Der}_R(A,M)$.
:::

::: {.front card-id="card-28213da6a96eb9ed" tags="definition"}
What is: Tangent sheaf
:::

::: {.back card-id="card-28213da6a96eb9ed"}
For $f:X\to S$, the relative tangent sheaf is $\mathcal T_{X/S}=\mathcal Hom_{\mathcal O_X}(\Omega^1_{X/S},\mathcal O_X)$. Its local sections are $\mathcal O_S$-linear derivations of $\mathcal O_X$.

For a smooth $n$-dimensional variety over a field, the tangent sheaf is locally free of rank $n$.
:::

::: {.front card-id="card-1af69ef40541b9cb" tags="definition"}
What is: Algebraic differential forms;
:::

::: {.back card-id="card-1af69ef40541b9cb"}
Algebraic differential $p$-forms are sections of $\Omega^p_{X/S}=\bigwedge^p\Omega^1_{X/S}$. The exterior derivative $d:\Omega^p_{X/S}\to\Omega^{p+1}_{X/S}$ satisfies $d^2=0$ and the graded Leibniz rule.
:::

::: {.front card-id="card-136accbe28d1a749" tags="definition"}
What is: The (co)normal sheaf,
:::

::: {.back card-id="card-136accbe28d1a749"}
For a closed immersion $i:Z\hookrightarrow X$ with ideal sheaf $I$, the conormal sheaf is $I/I^2$. Its dual $\mathcal Hom_{\mathcal O_Z}(I/I^2,\mathcal O_Z)$ is the normal sheaf. For smooth $Z$ and $X$, the conormal sequence is $I/I^2\to i^*\Omega_X^1\to\Omega_Z^1\to0$.

For a closed immersion of smooth varieties, the normal and conormal sheaves are locally free of rank equal to the codimension.
:::

::: {.front card-id="card-c5cef00e4330d7da"}
What is a geometric vector bundle over a scheme?
:::

::: {.back card-id="card-c5cef00e4330d7da"}
A geometric vector bundle of rank $n$ over $X$ is a scheme $f: Z \rightarrow X$ together with an open cover $\left\{U_i\right\}$ of $X$ and isomorphisms $\psi_i: f^{-1}\left(U_i\right) \rightarrow \mathbf{A}_{U_i}^n \coloneqq U_i\times_\ZZ {\mathbf{A}}^n_\ZZ$ over $U_i$ such that, for any $i, j$ and any open affine $V=\operatorname{Spec}(R) \subseteq U_i \cap U_j$, the automorphism $\psi=\psi_j \circ \psi_i^{-1}$ of $\mathbf{A}_V^n = \operatorname{Spec}R[x_1,\cdots,x_n]$ is linear: it is given by an $R$-algebra automorphism $\theta$ with $\theta(x_i) = \sum_j a_{ij} x_j$ and $(a_{ij})\in\operatorname{GL}_n(R)$.

For $\mce$ a locally free sheaf of rank $n$ on $X$, $\mathbf{V}(\mce)\coloneqq\operatorname{Spec}\operatorname{Sym}(\mce)$ is a geometric vector bundle of rank $n$ whose sheaf of sections is $\mce^{\vee}$.
:::

::: {.front card-id="card-013129f0821e1e9e"}
What is the geometric vector bundle associated to a locally free sheaf?
:::

::: {.back card-id="card-013129f0821e1e9e"}
$V(\mce) \coloneqq\operatorname{Spec}\operatorname{Sym}\mce$, where $\operatorname{Sym}\mce$ is the sheafy symmetric algebra so ${ \left.{{\qty{\operatorname{Sym}\mce}}} \right|_{{U_i}} } \cong \operatorname{Sym}\qty{{ \left.{{\mce}} \right|_{{U_i}} }}$ over ${\mathcal{O}}_{U_i}$, and where one takes the sheaf-theoretic spectrum.
:::

::: {.front card-id="card-de688f4ab8bf69dd"}
What are the exact sequences associated with relative differentials?
:::

::: {.back card-id="card-de688f4ab8bf69dd"}
For $f:X\to Y$ and $Z \leq X$ closed with ideal sheaf $\mci_Z$, the sequence
$$\mci_Z/\mci_Z^2\to \Omega_{X/Y}\otimes{\mathcal{O}}_Z \twoheadrightarrow\Omega_{Z/Y}$$
If $Y=k$, this is exact iff $Z$ is smooth.

For $X\xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \twoheadrightarrow\Omega_{X / Y}$$
:::

::: {.front card-id="card-14008e56d2fec738" tags="definition"}
What is a **presheaf**?
:::

::: {.back card-id="card-14008e56d2fec738"}
A functor $F: \Open(X)^{\operatorname{op}}\to \mathsf{CRing}$ (say; or sets, abelian groups, ...) preserving terminal objects, i.e. for each open $U \subseteq X$ a ring $F(U)$ where $F(\emptyset) = 0$, for every $U\hookrightarrow V$ a restriction $\mathop{\mathrm{Res}}_{V< U}: F(V)\to F(U)$, where $\mathop{\mathrm{Res}}_{U, U} = \operatorname{id}_{F(U)}$ and $U\hookrightarrow V\hookrightarrow W \leadsto \mathop{\mathrm{Res}}_{VU} \circ \mathop{\mathrm{Res}}_{WV} = \mathop{\mathrm{Res}}_{WU}$.

A sheaf also satisfies gluing and uniqueness for compatible local sections.
:::

::: {.front card-id="card-c59fe5bb7a144af8"}
What is a **sheaf**?
:::

::: {.back card-id="card-c59fe5bb7a144af8"}
A presheaf satisfying unique gluing: given $\left\{{\phi_i \in F(U_i)}\right\}$ with ${ \left.{{\phi_i}} \right|_{{U_{ij}}} } = { \left.{{\phi_j}} \right|_{{U_{ij}}} }$ there exists a unique $\Phi\in F(\bigcup_i U_i)$ such that ${ \left.{{\Phi}} \right|_{{U_i}} } = \phi_i$ for all $i$.
:::

::: {.front card-id="card-d11a1c7edb702d31"}
Give an example of a presheaf that is not a sheaf.
:::

::: {.back card-id="card-d11a1c7edb702d31"}
Any presheaf of constant functions, since functions can be constant on disjoint open sets (thus agreeing on overlaps trivially) without being globally constant (jump discontinuities)
:::

::: {.front card-id="card-7a8067f2aeb0cca8"}
What is the **equalizer characterization** of a sheaf?
:::

::: {.back card-id="card-7a8067f2aeb0cca8"}
$$F(U) \rightarrow \prod_{i} F(U_i) {{{} \atop \longrightarrow}\atop{\longrightarrow \atop {}}} \prod_{i, j} F(U_i \cap U_j)$$
where the maps are the restrictions $U_i \to U_{ij}$ and $U_j\to U_{ij}$.
:::

::: {.front card-id="card-82b98ea9b3cb0231" tags="definition"}
What is the **sheafification** of a presheaf?
:::

::: {.back card-id="card-82b98ea9b3cb0231"}
For $\mcf$ a presheaf, define $\mcf^+(U)$ as the functions $s: U\to \amalg_{x\in U} \mcf_x$ where $s(p) \in \mcf_p$ and for each $p\in U$ there is a neighborhood $V\subseteq U$ of $p$ and $t\in \mcf(V)$ such that $\forall q\in V,\,\, t_q = s(q)$ (equivalently, continuous sections of the étalé space of $\mcf$).

There is a map $\mcf\to\mcf^+$ inducing isomorphisms on all stalks, and every map from $\mcf$ to a sheaf factors uniquely through $\mcf^+$.
:::

::: {.front card-id="card-ea14df10f5014961" tags="definition"}
What is a **morphism of presheaves**? Of sheaves?
:::

::: {.back card-id="card-ea14df10f5014961"}
A morphism $\phi: \mcf\to \mcg$ of presheaves is a collection $\phi_U: \mcf(U) \to \mcg(U)$ fitting into commuting squares with restrictions, i.e. commuting with every restriction map. A morphism of sheaves is a morphism of the underlying presheaves.
:::

::: {.front card-id="card-a8dbd6c1552876cc"}
What is a **germ**?
:::

::: {.back card-id="card-a8dbd6c1552876cc"}
Elements in the stalk $\mcf_p$ are germs of sections of $\mcf$ over $p$.
:::

::: {.front card-id="card-903e35430d43d1de"}
What is the **stalk** of a sheaf?
:::

::: {.back card-id="card-903e35430d43d1de"}
$\mcf_p \coloneqq\colim_{U\ni p} \mcf(U)$.
:::

::: {.front card-id="card-29db92d857211565"}
What is the **kernel sheaf**?
:::

::: {.back card-id="card-29db92d857211565"}
$U\mapsto \ker \phi(U)$, which is already a sheaf.
:::

::: {.front card-id="card-e37a62e39fa49064"}
What is the **image sheaf**?
:::

::: {.back card-id="card-e37a62e39fa49064"}
Sheafify $U\mapsto \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-eca54149334d9622"}
Give an example to show that the image presheaf is not necessarily a sheaf.
:::

::: {.back card-id="card-eca54149334d9622"}
Problem: may fail existence. Take $0\to \underline{\ZZ}\xrightarrow{2\pi i} {\mathcal{O}}_X \xrightarrow{\exp} {\mathcal{O}}_X^{\times}\to 0$; this is exact as a sequence of sheaves since it's exact on stalks, but not exact as a sequence of presheaves, showing that $\operatorname{im}_{{\mathsf{pre}}} \exp \neq (\operatorname{im}_{\mathsf{pre}}\exp)^+$ (where $\mcf= \mcf^+$ for any sheaf). Cover $\CC^{\times}$ by contractible $U_i$, then take sections $f_i \coloneqq\operatorname{id}_{U_i} \in {\mathcal{O}}_X^{\times}$; then $f_i\in (\operatorname{im}\exp)^-$ since $\log(z)$ exists on each $U_i$. The sectors glue to $\CC^{\times}$, but there is no global $\log(z)$. So $\operatorname{id}_{\CC^{\times}} \not\in (\operatorname{im}\exp)^-$, so it fails the gluing axiom.
:::

::: {.front card-id="card-199b042d968cba02"}
What is the **cokernel sheaf**?
:::

::: {.back card-id="card-199b042d968cba02"}
For $\phi: \mcf\to \mcg$, sheafify $U\mapsto \operatorname{coker}\phi(U) \coloneqq\mcg/ \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-b4ef69e82c4e525c"}
Give an example to show that the cokernel presheaf is not a sheaf.
:::

::: {.back card-id="card-b4ef69e82c4e525c"}
Problem: may fail uniqueness. Let $\mcg\leq \mathop{\mathrm{Hol}}(\CC, \CC)$ be the sheaf of nonvanishing holomorphic functions and take $\exp: \mathop{\mathrm{Hol}}(\CC, \CC)\to \mcg$ and $U = \CC\setminus\left\{{0}\right\}$. Set $f(z) = z$, then $f\in \mcg(U)$ since it's nonvanishing. Cover $U$ by sectors $U_i$, then $f\in \operatorname{im}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$ since $\log f$ exists and $\exp(\log f) = f$, so $f = 0$ in $\operatorname{coker}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$. But $f\not\in \operatorname{im}\exp$ since there is no global logarithm, so $f\neq 0\in \operatorname{coker}\exp$ as a morphism of presheaves.
:::

::: {.front card-id="card-79c3642c37f8ed12" tags="definition"}
What is the **pullback/pushforward** (inverse/direct images) of a sheaf?
:::

::: {.back card-id="card-79c3642c37f8ed12"}
For $f:X\to Y$, $\mcf\in \Sh(X), \mcg\in \Sh(Y)$. Pushforward/direct image: already a sheaf
$$f_*\mcf(U) =\mcf(f^{-1}(U)),\qquad f_*\mcf\in \Sh(Y)$$
Pullback/inverse image: **sheafify**
$$f^{-1}\mcg(U) \coloneqq\colim_{V\supseteq f(U)} \mcg(V)$$
For $f: X\hookrightarrow Y$ the inclusion of an open subset, $f^{-1}\mcg(U) = \mcg(U)$, so denote $f^{-1}\mcg\coloneqq{ \left.{{\mcg}} \right|_{{X}} }$.

For modules on ringed spaces, $f^*\mcg\coloneqq f^{-1}\mcg\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X$.
:::

::: {.front card-id="card-e8e12fcc8b9e24a2" tags="definition"}
What is a **constant sheaf**?
:::

::: {.back card-id="card-e8e12fcc8b9e24a2"}
For $A\in \Ab\Grp$, $\underline{A}$ is the sheafification of the constant presheaf $U\mapsto A$. Equivalently, $\underline{A} \coloneqq C^0({-}, A^{{\operatorname{disc}}})$, the sheaf of locally constant functions to $A$. On nonempty connected sets $U$, $\underline{A}(U) = A$; on locally connected $U$, sections are the functions constant on every connected component. Stalks are all $A$.
:::

::: {.front card-id="card-0ccf704bc953a261" tags="definition"}
What is the **skyscraper sheaf**? Its stalks? Its adjoint characterization?
:::

::: {.back card-id="card-0ccf704bc953a261"}
For a point $p\in X$, the inclusion $\iota_p: \left\{{p}\right\} \hookrightarrow X$, and an abelian group $A$ (the constant sheaf $\underline{A}$ on $\left\{{p}\right\}$), the skyscraper sheaf is the direct image $(\iota_p)_*\underline{A}$. It assigns $U\mapsto A$ if $p\in U$ and $U\mapsto 0$ otherwise, with restrictions the identity or zero maps. Stalks are $A$ at each point in $\cl_X(p)$ and 0 elsewhere. Adjoint to taking stalks: $\Ab(\mcf_p, A)  { \, \xrightarrow{\sim}\, }\Sh(X)(\mcf, (\iota_p)_* A)$.
:::

::: {.front card-id="card-0859e1c888527f03"}
What is the **canonical sheaf**?
:::

::: {.back card-id="card-0859e1c888527f03"}
For $X$ smooth over $S$ of relative dimension $n$, $\omega_{X/S} \coloneqq\operatorname{det}\Omega_{X/S} \coloneqq\bigwedge\nolimits^n \Omega_{X/S}$, a line bundle. Over a field $k$, $\omega_X \coloneqq\operatorname{det}\Omega_{X/k}$ with $n\coloneqq\dim X$.
:::

::: {.front card-id="card-9535c31c3ca2f51d"}
What is the **dualizing sheaf**?
:::

::: {.back card-id="card-9535c31c3ca2f51d"}
For $X$ proper over a field, $\omega_X^\circ\in \Coh(X)$ together with a trace $\operatorname{tr}: H^n(X; \omega_X^\circ)\to k$ such that $\forall \mcf\in \Coh(X)$, the composition
$$H^n(X; \mcf) \times \mathop{\mathrm{Hom}}(\mcf, \omega_X^\circ) \to H^n(X, \omega_X^\circ) \xrightarrow{{\mathrm{tr}}}k$$
yields an isomorphism $\mathop{\mathrm{Hom}}(\mcf, \omega_X^\circ)  { \, \xrightarrow{\sim}\, }H^n(X; \mcf) {}^{ \vee }$ and more generally $\operatorname{Ext}^i(\mcf, \omega_X^\circ) \cong H^{n-i}(X; \mcf) {}^{ \vee }$. Exists for any projective scheme, not always equal to $\operatorname{det}\Omega_{X/k}$.
:::

::: {.front card-id="card-0c6c3a54e08bf4fb"}
What is a **local system**?
:::

::: {.back card-id="card-0c6c3a54e08bf4fb"}
A locally constant sheaf, i.e. a sheaf such that every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{\mcf}} \right|_{{U}} }$ is a constant sheaf.
:::

::: {.front card-id="card-2a19d4bf210f5449"}
What is an **invertible sheaf**?
:::

::: {.back card-id="card-2a19d4bf210f5449"}
$\mcl\in \Sh(X)$ such that $\exists \mcl^{-1}\in \Sh(X)$ with $\mcl\otimes_{{\mathcal{O}}_X} \mcl^{-1}\cong {\mathcal{O}}_X$.

Equivalently, every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{\mcf}} \right|_{{U}} } \cong {\mathcal{O}}_U$.

Equivalently, a locally free ${\mathcal{O}}_X\dash$module of rank 1.
:::

::: {.front card-id="card-09446192b8f9ece5"}
Discuss invertible sheaves on affine schemes.
:::

::: {.back card-id="card-09446192b8f9ece5"}
$\mcf\in \operatorname{Pic}(\operatorname{Spec}A)\implies \mcf$ corresponds to $M\in  {}_{A}\Mod$ which is finite projective locally free of rank 1 and thus flat and finitely presented. Every invertible sheaf on ${\mathbf{A}}^2_{/ {k}}$ is trivial.
:::

::: {.front card-id="card-e8e690603a360318"}
What is a **constructible sheaf**?
:::

::: {.back card-id="card-e8e690603a360318"}
$\mcf\in \Sh(X)$ is constructible iff $\exists \left\{{i_{Y_i}: Y_i\hookrightarrow X}\right\}_{i\leq N}$ with $X = \bigcup_{i\leq N}Y_i$, i.e. $Y$ is a finite union of locally closed subschemes, such that ${ \left.{{\mcf}} \right|_{{Y_i}} } \coloneqq\iota_{Y_i}^* \mcf$ is a finite locally constant sheaf.
:::

::: {.front card-id="card-45174c1167af9df9"}
What is the **sheaf of rational functions** on a scheme?
:::

::: {.back card-id="card-45174c1167af9df9"}
Define the function field of $X$ to be $K\coloneqq{\mathcal{O}}_{X, \eta_X}$, the stalk at the generic point, and define $\mck_X \coloneqq\underline{K}$, the constant sheaf associated to this field. Equivalently, sheafify $U\to \operatorname{ff}({\mathcal{O}}_X(U))$.
:::

::: {.front card-id="card-0b18a6dfa59ccde0"}
What is the fundamental exact sequence involving the tangent sheaf for ${\mathbf{P}}^n$?
:::

::: {.back card-id="card-0b18a6dfa59ccde0"}
$0\to {\mathcal{O}}_X \to {\mathcal{O}}_X(1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\to \mct_X\to 0$.
:::

::: {.front card-id="card-aac019483de7ed9e"}
What does it mean to **twist a sheaf**?
:::

::: {.back card-id="card-aac019483de7ed9e"}
$\mcf(n) \coloneqq\mcf\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n)$.
:::

::: {.front card-id="card-4d2fa6a3304404c6"}
Characterize coherent sheaves over $\operatorname{Spec}A$ for $A$ Noetherian.
:::

::: {.back card-id="card-4d2fa6a3304404c6"}
$\mcf\in \Coh(\operatorname{Spec}A)\implies \exists \bigoplus_{i\in I} {\mathcal{O}}(n_i) \twoheadrightarrow\mcf$, i.e. always a quotient of a free sheaf. Easy proof: $\mcf(n)$ is globally generated for some $n$, so $\exists \bigoplus_{i\leq N} {\mathcal{O}}_X \twoheadrightarrow\mcf(n)$, now twist this exact sequence by $-n$.
:::

::: {.front card-id="card-c5e1189afc267094"}
What is the **six functor formalism**?
:::

::: {.back card-id="card-c5e1189afc267094"}
Direct image (pushforward) and inverse image (pullback), extension by zero (lower shriek) and exceptional image (upper shriek), internal tensor and internal hom.
:::

::: {.front card-id="card-5fb0674e6ef318ad"}
How is the **inverse image sheaf** defined? What are its stalks?
:::

::: {.back card-id="card-5fb0674e6ef318ad"}
$f^{-1}\mcg(U) \coloneqq\colim_{V\supseteq f(U)} \mcg(V)$. Stalks: $\mcg_p  { \, \xrightarrow{\sim}\, }(f^{-1}\mcg)_p$.
:::

::: {.front card-id="card-7253757c78a0c001"}
What is the **extension by zero** sheaf? What are its stalks?
:::

::: {.back card-id="card-7253757c78a0c001"}
Sheafify $U\mapsto \chi_{V\subseteq U}\mcf(V)$ to get $\iota_! \mcf$ for $\iota: U \subseteq X$. Stalks are $\mcf_p \chi_{p\in U}$.

Alternatively take $\iota_* \mcf$.
:::

::: {.front card-id="card-c15fc4f7707b0b75"}
How is the pushforward sheaf defined? What are its stalks?
:::

::: {.back card-id="card-c15fc4f7707b0b75"}
$f_*\mcf(V) \coloneqq\mcf(f^{-1}(V))$. Can't say much in general about its stalks.
:::

::: {.front card-id="card-77682f622e066702"}
What is the restriction of a sheaf?
:::

::: {.back card-id="card-77682f622e066702"}
For $\iota: X\hookrightarrow Y$, ${ \left.{{\mcg}} \right|_{{X}} } \coloneqq\iota^{-1}\mcf$, same stalks as $\mcg$.
:::

::: {.front card-id="card-42718a4202cf6938"}
What is a flasque (flabby) sheaf?
:::

::: {.back card-id="card-42718a4202cf6938"}
$U\hookrightarrow V \implies \mcf(V) \twoheadrightarrow\mcf(U)$.
:::

::: {.front card-id="card-29a3dfbf0b8411fd"}
What is the higher cohomology of a flasque sheaf?
:::

::: {.back card-id="card-29a3dfbf0b8411fd"}
$H^{\geq 1}(X; \mcf) = 0$ for any flasque sheaf on any topological space, so are $\Gamma\dash$acyclic.
:::

::: {.front card-id="card-51fc917eb022892e"}
Is a morphism of sheaves injective if injective on sections? Surjective?
:::

::: {.back card-id="card-51fc917eb022892e"}
Injective: yes, surjective: no.
:::

::: {.front card-id="card-b5dfbf872b61db5b" tags="definition"}
What is: sheaf kernel/cokernel
:::

::: {.back card-id="card-b5dfbf872b61db5b"}
The kernel of $F\to G$ is the subsheaf $U\mapsto\ker(F(U)\to G(U))$. The cokernel is the sheafification of $U\mapsto\operatorname{coker}(F(U)\to G(U))$; a section of the sheaf cokernel need only have local representatives.
:::
