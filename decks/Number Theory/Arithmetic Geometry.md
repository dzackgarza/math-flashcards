---
title: "Number Theory::Arithmetic Geometry"
---

::: {.front card-id="card-cba9b3434509cac6"}
What are Witt vectors?
:::

::: {.back card-id="card-cba9b3434509cac6"}
For a $K\in { {}_{{ \mathbf{F} }_p}  \mathsf{Alg}}^\perf$, the unique lift $W(K)\in { {}_{{ \ZZ_{\widehat{p}} }}  \mathsf{Alg}}$ which is $p\dash$adically complete and $p\dash$torsionfree.

$W({ \mathbf{F} }_p) = { \ZZ_{\widehat{p}} }$.
:::

::: {.front card-id="card-3e5dc56ada4e1e06"}
What is the ghost map for Witt vectors?
:::

::: {.back card-id="card-3e5dc56ada4e1e06"}
$w: W_r(A)\to A{ {}^{ \scriptscriptstyle\times^{r} }  }$ where $\mathbf{x}\mapsto {\left[ {w_0(x_0), w_1(x_0, x_1) \cdots, w_{r-1}(x_0,\cdots, x_{r-1})} \right]}$ where $w_i(x_0,\cdots, x_n) \coloneqq x_0^{p^n} + p x_1^{p^{n-1}} + \cdots + p^n x_n$.
:::

::: {.front card-id="card-e1df0dc2c8cac23f"}
What is tilting?
:::

::: {.back card-id="card-e1df0dc2c8cac23f"}
For $A\in {}_{\ZZ}  \mathsf{Alg}$ $\pi\dash$adically complete for some $\pi\mathrel{\Big|}p$, the tilt is $A^\flat \coloneqq\projectivelim_{\operatorname{Frob}} A/pA$ where $\operatorname{Frob}: A/pA \to A/pA$.

Always have $A^\flat \in { {}_{{ \mathbf{F} }_p}  \mathsf{Alg}}^\perf$.

Think of $\mathbf{x}\in A^\flat \cong \projectivelim_{x\mapsto x^p} A$ as $x_{i+1}^p =x_i$.
:::

::: {.front card-id="card-54f12bcb8d79c20f"}
What is ${\mathbf{A}}_\inf(A)$?
:::

::: {.back card-id="card-54f12bcb8d79c20f"}
${\mathbf{A}}_\inf(A) \coloneqq W(A^\flat)$.

Interpolates between characteristic zero geometry of $A$ and characteristic $p$ geometry of $A^\flat$.

$A$ may not have a Frobenius, but ${\mathbf{A}}_\inf(A)$ does.
:::

::: {.front card-id="card-676f75baf8ef9695"}
What is a perfectoid ring $S$?
:::

::: {.back card-id="card-676f75baf8ef9695"}
$S$ is $\pi\dash$adically complete for some $\pi\in S$ with $\pi^p \mathrel{\Big|}p$

$\operatorname{Frob}: S/pS \to S/pS$ is surjective.

$\ker \qty{{\mathbf{A}}_\inf(S) \xrightarrow{\theta }S} = \left\langle{\xi}\right\rangle$ is principal.

Precisely the rings so that $\theta$ is a pro-infinitesimal 1-parameter degeneration, deforming $S$ in a preferred $\xi$ direction.

If $S$ is characteristic $p$, then $S$ is perfect iff perfectoid.
:::

::: {.front card-id="card-905e3693341d235d"}
What is $A_{\crys}$?
:::

::: {.back card-id="card-905e3693341d235d"}
Setup: $K = { \CC_p }, S\coloneqq{\mathcal{O}}_K, A_\inf \coloneqq{\mathbf{A}}_\inf({\mathcal{O}}_K)$.

$A_\crys$ is the $p\dash$adic completion of the subalgebra $\left\langle{\xi^m/m!}\right\rangle \leq A_\inf{ \left[ { \scriptstyle \frac{1}{p} } \right] }$ .

Universal $p\dash$adically complete divided power thickening of ${\mathcal{O}}_K$ over ${ \ZZ_{\widehat{p}} }$.
:::

::: {.front card-id="card-ae412126be38c441"}
What is $B_\crys$ and $B_\crys^+$? $B_\mathrm{dR}$?
:::

::: {.back card-id="card-ae412126be38c441"}
$B^+_\crys\coloneqq A_\crys{ \left[ { \scriptstyle \frac{1}{p} } \right] }$ and $B_\crys= B_\crys^+{ \left[ { \scriptstyle \frac{1}{\mu} } \right] }$

$B_\mathrm{dR}^+$ is the $\xi\dash$adic completion of $B^+_\crys$ and $B_\mathrm{dR}= \operatorname{ff}B^+_\mathrm{dR}$.

$B^+_\mathrm{dR}$ is a DVR with residue field ${ \CC_p }$.
:::

::: {.front card-id="card-91c27264b0ed0ce1"}
What is the etale homotopy type of a scheme $X$?
:::

::: {.back card-id="card-91c27264b0ed0ce1"}
For $X$ quasiprojective, ${\mathsf{ho}}\text{Ét}(X) \coloneqq\left\{{\pi_0 { {\left\lvert {{ \mathcal{N}({\mcu}) }} \right\rvert} }}\right\}_{\mcu\in X_\text{ét}} \in \mathsf{pro}\Spaces$

For general $X$, replace ${ \mathcal{N}({\mcu}) }$ by hypercovers, and $X_\text{ét}$ only provides a left-filtering category up to homotopy, so generally in ${\mathsf{ho}}\mathsf{pro}\Spaces$.

Since $\left\{{{ {\left\lvert {{ \mathcal{N}({\mcu}) }} \right\rvert} }}\right\}_{\mcu\in X_\text{ét}}$ is a cofibrant replacement, ${\mathsf{ho}}\text{Ét}({-}) = {\mathbf{L}}\pi_0({-})$ is a derived functor.
:::

::: {.front card-id="card-c0543af4c9aff8b5"}
What is the section conjecture?
:::

::: {.back card-id="card-c0543af4c9aff8b5"}
For $X$ smooth hyperbolic and proper over $k$, there is a set bijection
$$X(k)  { \, \xrightarrow{\sim}\, }\pi_0 \mathsf{pro}\Spaces_{/ {\operatorname{Spec}k}}(\text{Ét}(\operatorname{Spec}k) \to \text{Ét}(X))  { \, \xrightarrow{\sim}\, }\text{Ét}(X_{\overline{k}})^{h G_k},$$
regarding the RHS as homotopy classes of morphisms.

Thus conjecturally $X(k) { \, \xrightarrow{\sim}\, }\text{Ét}(X_{\overline{k}})^{h G_k}$ can be recovered from homotopy fixed points.

This is a section since morphisms are triangles over $\text{Ét}(\operatorname{Spec}k)$, so such maps are sections to the structure morphism $\text{Ét}(X)\to \text{Ét}(\operatorname{Spec}k)$.
:::

::: {.front card-id="card-4ade8c1c7594ae11"}
What inspires the anabelian conjectures?
:::

::: {.back card-id="card-4ade8c1c7594ae11"}
For $K\coloneqq\QQ(\sqrt a), L\coloneqq\QQ(\sqrt b)$,
$$\Gal(K) \cong \Gal(L) \iff K\cong L \iff a=b\in \QQ^{\times}/{ {\QQ^{\times}}_{\scriptscriptstyle \square} }$$
so $\Sch(\operatorname{Spec}L  { \, \xrightarrow{\sim}\, }\operatorname{Spec}K) \cong {\mathsf{ho}}\mathsf{pro}\Spaces(\text{Ét}(L) { \, \xrightarrow{\sim}\, }\text{Ét}(K))$.

For $K, L\in \mathsf{Field}_{/ {\QQ}}$, $\mathsf{Field}_{/ {\QQ}}(K  { \, \xrightarrow{\sim}\, }L) \cong \Top\Grp(G_K { \, \xrightarrow{\sim}\, }_{\mathop{\mathrm{Out}}} G_L)$.
:::

::: {.front card-id="card-978ea3e5e7123eb1"}
What are the anabelian conjectures?
:::

::: {.back card-id="card-978ea3e5e7123eb1"}
Existence of $\mathsf{An}_k \leq \Sch_{/ {k}}$ a full subcategory including smooth hyperbolic curves, closed under taking fibrations with base and fiber in $\mathsf{An}_k$, and
$$\Sch(X_1\to X_2 \st\text{open image}) \cong \Top\Grp_{/ {G_k}}(\pi_1 X_1 \to \pi_1 X_2 \st\text{open morphisms})$$
:::

::: {.front card-id="card-71b306da0e579252"}
What is a symmetric domain?
:::

::: {.back card-id="card-71b306da0e579252"}
Let $G$ be a semisimple group over $\mathbb{Q}$. A subgroup $\Gamma \subseteq G(\mathbb{Q})$ is called congruence if there exists an embedding $G \hookrightarrow \mathrm{GL}_n$ such that $\Gamma$ contains
$$\operatorname{ker}\left(\mathrm{GL}_n(\mathbb{Z}) \rightarrow \mathrm{GL}_n(\mathbb{Z} / N \mathbb{Z})\right) \cap G(\mathbb{Q})$$
for some $N \geqslant 1$. Set $X_G^{+}=X^{+}:=G(\mathbb{R})^{+} / C$. Then, a space of the form $\Gamma^{+} \backslash X^{+}$is called a symmetric space for $G$ (here $\Gamma^{+}=\Gamma \cap G(\mathbb{R})^{+}$).

This is generally an orbifold since $\Gamma$ may contain torsion.
:::

::: {.front card-id="card-323c8a1d1fa7cc8a"}
What is a locally symmetric space?
:::

::: {.back card-id="card-323c8a1d1fa7cc8a"}
Let $G$ be a reductive group over $\mathbb{Q}$. Let us fix a maximal compact subgroup $K_{\infty}^{\max }$ of $G(\mathbb{R})$ and let $C:=\left(K_{\infty}^{\max }\right)^{\circ}$. Let us then fix/denote:

- $K_{\infty}$ to be a compact subgroup of $G(\mathbb{R})$ such that $C \subseteq K_{\infty} \subseteq K_{\infty}^{\max }$
- $A_G$ is the maximal $\mathbb{Q}$-split subtorus of $Z(G)$. Then, for any compact open subgroup $K_f \subseteq G\left(\mathbb{A}_f\right)$ we set
$$S_G\left(K_f\right):=G(\mathbb{Q}) \backslash G(\mathbb{A}) /\left(K_{\infty} K_f A_G(\mathbb{R})^{+}\right)$$
A space of the form $S_G\left(K_f\right)$ is called a locally symmetric space for $G$. Here we are denoting by $\mathbb{A}=\left(\widehat{\mathbb{Z}} \otimes_{\mathbb{Z}} \mathbb{Q}\right) \times \mathbb{R}$ the adele ring for $\mathbb{Q}$ and by $\mathbb{A}_f$ its subring of finite adeles $\widehat{\mathbb{Z}} \otimes \mathbb{\mathbb { Z }} \mathbb{Q}$. We topologize this by the restricted direct topology and topologize $G(\mathbb{A})$ and $G\left(\mathbb{A}_f\right)$ in the usual way (e.g. see \[Con12\]).
:::

::: {.front card-id="card-5c5663f6f10fe152"}
What is a Hermitian symmetric domain?
:::

::: {.back card-id="card-5c5663f6f10fe152"}
A hermitian space is a smooth manifold $M$ endowed with a riemannian structure $g$ and a complex structure $J$ that are compatible in the sense that $g(J x, J y)=g(x, y)$ for all $m \in M$ and all $x, y \in T_m M$. $^6$ A hermitian space is symmetric if every point is an isolated fixed point of an involution. A hermitian symmetric domain is a hermitian symmetric space with negative (sectional) curvature.

Every hermitian symmetric domain decomposes as a product of simple (irreducible) hermitian symmetric domains $D$ whose automorphism groups $\operatorname{Hol}(D)$ are simple Lie groups.
:::

::: {.front card-id="card-6e62b7a6104572a1"}
What is a Shimura variety?
:::

::: {.back card-id="card-6e62b7a6104572a1"}
Let $D$ be a hermitian symmetric domain, and let $\operatorname{Hol}(D)^{+}$be the identity component of $\operatorname{Hol}(D)$. Then $\operatorname{Hol}(D)^{+}$is a connected semisimple Lie group with trivial centre. Consider a simply connected semisimple algebraic group $G$ over $\mathbb{Q}$ and a surjective homomorphism
$$G(\mathbb{R}) \rightarrow \operatorname{Hol}(D)^{+}$$
with compact kernel (such pairs always exist, and are classified). Let $\Gamma$ be a congruence subgroup in $G(\mathbb{Q})$ whose image $\overline{\Gamma}$ in $\operatorname{Aut}(D)^{+}$is torsion-free. Then $\overline{\Gamma}$ acts freely $D$, and so the quotient $\overline{\Gamma} \backslash D$ is a complex manifold. We'll see shortly that it is, in fact, an algebraic variety.

The Shimura varieties are the algebraic varieties that arise in this way. In other words, an algebraic variety over $\mathbb{C}$ is a Shimura variety if its universal covering space (in the topological sense) is a hermitian symmetric domain, and its fundamental group is the image of a congruence group as above.
:::
