---
title: "Algebraic Geometry::O_X-Modules"
---

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

::: {.front card-id="card-f9e01cd1f2afecc6" tags="definition"}
What is: Derivations
:::

::: {.back card-id="card-f9e01cd1f2afecc6"}
A $k$-derivation $D:A\to M$ is $k$-linear and satisfies $D(ab)=aD(b)+bD(a)$. It kills the image of $k$ in $A$.
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
:::

::: {.front card-id="card-006c2199efa06a65" tags="definition"}
What is: Regular immersions and local complete intersections;
:::

::: {.back card-id="card-006c2199efa06a65"}
A closed immersion $Z\hookrightarrow X$ is regular of codimension $c$ if its ideal is locally generated by a regular sequence of length $c$; then $I/I^2$ is locally free of rank $c$. A local complete intersection morphism factors locally as a regular immersion followed by a smooth morphism.
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
