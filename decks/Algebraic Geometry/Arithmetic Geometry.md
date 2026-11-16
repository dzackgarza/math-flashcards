---
title: "Algebraic Geometry::Arithmetic Geometry"
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
A Hermitian manifold is a smooth manifold $M$ with a Riemannian metric $g$ and a complex structure $J$ such that $g(Jx,Jy)=g(x,y)$. It is Hermitian symmetric if every point is an isolated fixed point of an involutive holomorphic isometry. A Hermitian symmetric domain is a connected simply connected Hermitian symmetric space of noncompact type. Its sectional curvature is nonpositive, not necessarily negative: a product has zero-curvature mixed tangent planes.

Every Hermitian symmetric domain decomposes as a product of irreducible Hermitian symmetric domains. For each irreducible factor, the identity component of the holomorphic automorphism group is a noncompact simple adjoint real Lie group.
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

::: {.front card-id="card-dbf562814c8f40d6" tags="definition"}
What is the definition of Adele ring?
:::

::: {.back card-id="card-dbf562814c8f40d6"}
For a global field $k$, the restricted direct product $\mathbb A_k=\prod_v' k_v$ over all places $v$, with respect to the local rings of integers $\mathcal O_v$; for $k=\mathbb Q$, $\mathbb A=\widehat{\mathbb Z}\otimes\mathbb Q\times\mathbb R$.
:::

::: {.front card-id="card-f33b4442e360e507" tags="definition"}
What is the definition of Arithmetic scheme?
:::

::: {.back card-id="card-f33b4442e360e507"}
A scheme $X$ equipped with a structure morphism to an arithmetic base such as $\operatorname{Spec}\mathbb Z$ or $\operatorname{Spec}\mathcal O_K$; its fibres over primes are schemes over finite fields and its generic fibre is a variety over $\mathbb Q$ or a number field.
:::

::: {.front card-id="card-5ebb84b5f9c09f0b" tags="definition"}
What is the definition of Cofibrant replacement?
:::

::: {.back card-id="card-5ebb84b5f9c09f0b"}
In a model category, a functorial factorization of an object $X$ as a cofibration $QX\to X$ from a cofibrant object $QX$; it is used to compute derived functors, for example $\mathbf L F(X)=F(QX)$.
:::

::: {.front card-id="card-b41b486b9c834ef7" tags="definition"}
What is the definition of Divided power thickening?
:::

::: {.back card-id="card-b41b486b9c834ef7"}
A thickening $A\to B$ (a surjection with nilpotent kernel) together with divided power structures on the kernel compatible with the PD structure on $p$; the universal $p$-adically complete PD thickening of $\mathcal O_K$ over $\mathbb Z_p$ is $A_{\mathrm{crys}}$.
:::

::: {.front card-id="card-4d752f5b42d7bc7a" tags="definition"}
What is the definition of Finite adeles?
:::

::: {.back card-id="card-4d752f5b42d7bc7a"}
The ring $\mathbb A_f=\prod_{v\text{ finite}}' k_v$ of finite adeles, the restricted direct product over the non-Archimedean places; for $\mathbb Q$, $\mathbb A_f=\widehat{\mathbb Z}\otimes_{\mathbb Z}\mathbb Q$.
:::

::: {.front card-id="card-53ea801e2b02e4e9" tags="definition"}
What is the definition of Frobenius endomorphism?
:::

::: {.back card-id="card-53ea801e2b02e4e9"}
For a ring or scheme of characteristic $p$, the endomorphism $\operatorname{Frob}:R\to R$, $x\mapsto x^p$; for $X$ over $\mathbb F_p$ it gives a morphism $X\to X^{(p)}$ to the Frobenius twist, and the relative Frobenius is $F_{X/k}:X\to X^{(p)}$.
:::

::: {.front card-id="card-aa406a897b09b179" tags="definition"}
What is the definition of Hermitian space?
:::

::: {.back card-id="card-aa406a897b09b179"}
In the manifold sense: a smooth $M$ with a Riemannian metric $g$ and an integrable complex structure $J$ such that $g(Jx,Jy)=g(x,y)$. Hermitian symmetric means each point is an isolated fixed point of an involutive holomorphic isometry. A Hermitian symmetric domain is connected, simply connected, and of noncompact type; its invariant metric has nonpositive sectional curvature.
:::

::: {.front card-id="card-b35d040a5a028195" tags="definition"}
What is the definition of Homotopy fixed point?
:::

::: {.back card-id="card-b35d040a5a028195"}
For a group $G$ acting on a space $X$, the homotopy fixed points $X^{hG}=\operatorname{Map}^G(EG,X)$, the space of $G$-equivariant maps from a contractible free $G$-space $EG$ to $X$.
:::

::: {.front card-id="card-1f242f1dd4b0c491" tags="definition"}
What is the definition of Hyperbolic curve?
:::

::: {.back card-id="card-1f242f1dd4b0c491"}
A smooth projective curve of genus $g\ge2$ over a field $k$; more generally a curve with negative Euler characteristic. Over a number field it has finitely many $k$-points by Faltings, and its étale fundamental group is anabelian.
:::

::: {.front card-id="card-feb9a5bc48b07ccb" tags="definition"}
What is the definition of Hypercover?
:::

::: {.back card-id="card-feb9a5bc48b07ccb"}
A simplicial object $U_\bullet\to X$ in a site such that, for every $n$, the canonical map from $U_n$ to the $n$-th matching object (the fiber product of the previous stages) is a cover; it generalizes the Čech nerve and computes cohomology when arbitrary covers cannot be refined by a single cover.
:::

::: {.front card-id="card-5354a04ea6eeff20" tags="definition"}
What is the definition of Negative sectional curvature?
:::

::: {.back card-id="card-5354a04ea6eeff20"}
A Riemannian manifold has negative sectional curvature if $K(\sigma)<0$ for every tangent $2$-plane $\sigma$. Hermitian symmetric domains have nonpositive sectional curvature, and negative sectional curvature only in rank one.
:::

::: {.front card-id="card-e5250a461a00338c" tags="definition"}
What is the definition of P-adically complete?
:::

::: {.back card-id="card-e5250a461a00338c"}
A ring $R$ is $p$-adically complete if the natural map $R\to\varprojlim_n R/p^nR$ is an isomorphism; equivalently $R$ is complete for the $p$-adic topology.
:::

::: {.front card-id="card-23fc31f061e1fa53" tags="definition"}
What is the definition of Perfect ring?
:::

::: {.back card-id="card-23fc31f061e1fa53"}
A ring $R$ of characteristic $p$ is perfect if its Frobenius $x\mapsto x^p$ is bijective; equivalently every element has a unique $p$-th root. A perfect field is a field $k$ with $k=k^p$.
:::

::: {.front card-id="card-6f080b42d2b1ce48" tags="definition"}
What is the definition of Pro-infinitesimal?
:::

::: {.back card-id="card-6f080b42d2b1ce48"}
A map of formal schemes or rings that is an inverse limit of infinitesimal thickenings; equivalently each finite-level quotient is an infinitesimal thickening. The map $\theta:\mathbf A_{\inf}(S)\to S$ in perfectoid theory is pro-infinitesimal.
:::

::: {.front card-id="card-307493a661302070" tags="definition"}
What is the definition of Pro-space?
:::

::: {.back card-id="card-307493a661302070"}
An object of the pro-category $\mathsf{pro}(\mathsf{Spaces})$, i.e. a filtered inverse system of spaces, with $\operatorname{Hom}(\{X_i\},\{Y_j\})=\varprojlim_j\varinjlim_i\operatorname{Hom}(X_i,Y_j)$; the étale homotopy type is a pro-space.
:::

::: {.front card-id="card-a3593c88b3d5b54e" tags="definition"}
What is the definition of Restricted direct topology?
:::

::: {.back card-id="card-a3593c88b3d5b54e"}
The topology on a restricted direct product $\prod_v' G_v$ in which a basis of neighborhoods of the identity consists of products $\prod_v U_v$ with $U_v\subset G_v$ open and $U_v=G_v$ for all but finitely many $v$.
:::

::: {.front card-id="card-ae2cd3772c8f5089" tags="definition"}
What is the definition of Semisimple lie group?
:::

::: {.back card-id="card-ae2cd3772c8f5089"}
A Lie group whose Lie algebra is semisimple, i.e. a direct sum of simple Lie algebras with no nonzero solvable ideal; equivalently its Killing form is nondegenerate. Connected semisimple Lie groups have finite centre.
:::

::: {.front card-id="elliptic-weierstrass-invariants" tags="construction formula"}
For an elliptic curve over a field, give a Weierstrass equation valid in every characteristic, its invariant differential, and $b_i,c_i,\Delta,j$. How do the invariants change under rescaling?
:::

::: {.back card-id="elliptic-weierstrass-invariants"}
With origin $O=[0:1:0]$:
$$y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6,\qquad
\omega=\frac{dx}{2y+a_1x+a_3}.$$
The differential extends regularly and never vanishes on the smooth projective curve. Put
$$\begin{aligned}
b_2&=a_1^2+4a_2,&b_4&=a_1a_3+2a_4,&b_6&=a_3^2+4a_6,\\
b_8&=a_1^2a_6+4a_2a_6-a_1a_3a_4+a_2a_3^2-a_4^2,\\
c_4&=b_2^2-24b_4,&c_6&=-b_2^3+36b_2b_4-216b_6,\\
\Delta&=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6,&j&=c_4^3/\Delta.
\end{aligned}$$
Smoothness is $\Delta\ne0$; $c_4^3-c_6^2=1728\Delta$. Admissible changes have $x=u^2x'+r$, $y=u^3y'+u^2sx'+t$, $u\ne0$. Then $c_4=u^4c'_4$, $c_6=u^6c'_6$, $\Delta=u^{12}\Delta'$, so $j=j'$.

Reference: Silverman, *The Arithmetic of Elliptic Curves*, III.1.
:::

::: {.front card-id="elliptic-rr-weierstrass" tags="construction"}
How does Riemann–Roch construct a Weierstrass cubic from a smooth projective genus-one curve with a rational point $O$? Where is the group law in this construction?
:::

::: {.back card-id="elliptic-rr-weierstrass"}
$h^0(nO)=n$ for $n\ge1$. Choose $x$ with pole order two and $y$ with pole order three at $O$. The sections $1,x,y$ embed by $|3O|$ into $\mathbb P^2$.

In $H^0(6O)$, the seven functions $1,x,y,x^2,xy,x^3,y^2$ satisfy a relation, yielding the generalized Weierstrass equation after scaling. The point at infinity is $O$ and its tangent has intersection divisor $3O$.

$P\mapsto\mathcal O(P-O)$ identifies the curve with $\operatorname{Pic}^0$. Collinear $P,Q,R$, counted with multiplicity, satisfy $P+Q+R=O$. A genus-one curve without a rational point has a Jacobian but no choice of origin making it an elliptic curve over that field.
:::

::: {.front card-id="elliptic-group-law-computation" tags="formula application"}
Give the chord-and-tangent formulas on $y^2=x^3+Ax+B$ in characteristic different from $2,3$. On $y^2=x^3-2$, double $P=(3,5)$ and test whether $P$ could be torsion over $\mathbb Q$.
:::

::: {.back card-id="elliptic-group-law-computation"}
For $Q\ne\pm P$, $\lambda=(y_Q-y_P)/(x_Q-x_P)$; for $Q=P$ with $y_P\ne0$, $\lambda=(3x_P^2+A)/(2y_P)$. Then
$$x_{P+Q}=\lambda^2-x_P-x_Q,\qquad y_{P+Q}=\lambda(x_P-x_{P+Q})-y_P.$$
$-P=(x_P,-y_P)$, $P+(-P)=O$, and $2P=O$ if $y_P=0$.

For $(3,5)$, $\lambda=27/10$, hence
$$2P=\left(\frac{129}{100},-\frac{383}{1000}\right).$$
Lutz–Nagell: rational torsion points on a nonsingular integral short Weierstrass equation have integral coordinates. Since $2P$ is not integral, it is not torsion; therefore $P$ has infinite order.
:::

::: {.front card-id="elliptic-twists-j-classification" tags="definition application"}
Over a field of characteristic different from $2,3$, what does equality of $j$ classify? Describe quadratic twists and distinguish geometric isomorphism from isomorphism over the ground field.
:::

::: {.back card-id="elliptic-twists-j-classification"}
$j(E)=j(E')$ iff $E_{\bar k}\cong E'_{\bar k}$ as pointed curves. For $E:y^2=x^3+Ax+B$ and $d\in k^\times$:
$$E^{(d)}:y^2=x^3+d^2Ax+d^3B.$$
Over $k(\sqrt d)$, $(x,y)\mapsto(x/d,y/d^{3/2})$ gives $E^{(d)}\cong E$. The discriminant changes by $d^6$, but $j$ does not.

For $j\ne0,1728$, quadratic twists are classified by $k^\times/(k^\times)^2$. At $j=1728$ and $0$, quartic and sextic twists also occur. Over $\bar k$, origin-preserving automorphism groups have orders $2,4,6$ for generic $j$, $1728$, and $0$ respectively.

Example: $y^2=x^3-x$ and $y^2=x^3+x$ both have $j=1728$, but are not isomorphic over $\mathbb R$: their real loci have two and one connected components.
:::

::: {.front card-id="elliptic-isogeny-dual-torsion" tags="definition theorem comparison"}
Relate isogenies, finite subgroup schemes, dual isogenies, and multiplication maps on elliptic curves. State the prime-to-characteristic torsion structure.
:::

::: {.back card-id="elliptic-isogeny-dual-torsion"}
An isogeny $\phi:E\to E'$ is a nonconstant morphism sending $O$ to $O'$; it is a finite surjective group homomorphism. Its degree equals the length of its kernel group scheme. Each finite subgroup scheme $G\subset E$ defines the quotient isogeny $E\to E/G$.
$$\widehat\phi\phi=[\deg\phi]_E,\qquad\phi\widehat\phi=[\deg\phi]_{E'},\qquad\deg\widehat\phi=\deg\phi.$$
For $n\ne0$, $\deg[n]=n^2$. If $\operatorname{char}k\nmid n$, $[n]$ is étale and $E[n](\bar k)\cong(\mathbb Z/n)^2$. In characteristic $p$, degrees still count scheme length, not just geometric points; $[p]$ is inseparable.

Example: on $y^2=x^3-x$, $O,(0,0),(1,0),(-1,0)$ are the full geometric $2$-torsion. Quotienting by $\{O,(0,0)\}$ gives a degree-two isogeny, whereas $[2]$ has degree four.
:::

::: {.front card-id="elliptic-two-isogeny-example" tags="application construction"}
For $E:y^2=x^3+ax^2+bx$ over a field of characteristic different from two, with $b(a^2-4b)\ne0$, construct the quotient by $(0,0)$. Specialize to $y^2=x^3-x$.
:::

::: {.back card-id="elliptic-two-isogeny-example"}
$$E':Y^2=X^3-2aX^2+(a^2-4b)X,$$
with degree-two isogeny
$$X=x+a+\frac bx=\frac{y^2}{x^2},\qquad Y=y\left(1-\frac b{x^2}\right).$$
The rational formulas extend over $x=0$ and infinity; the kernel is $\{O,(0,0)\}$. Substitution verifies the equation of $E'$.

For $a=0,b=-1$, the quotient is $Y^2=X^3+4X$, with $X=x-1/x$, $Y=y(1+1/x^2)$. The dual composed with this map is $[2]$, not the identity.
:::

::: {.front card-id="elliptic-weil-pairing-galois" tags="definition theorem application"}
State the properties of the Weil pairing and their consequences for elliptic torsion fields and the determinant of the Tate-module representation.
:::

::: {.back card-id="elliptic-weil-pairing-galois"}
For $n$ prime to $\operatorname{char}k$,
$$e_n:E[n]\times E[n]\to\mu_n$$
is bilinear, alternating, perfect, and Galois equivariant. A basis $P,Q$ has $e_n(P,Q)$ a primitive $n$th root, so full rational $n$-torsion forces $\mu_n\subset k$.

For $\ell\ne\operatorname{char}k$, $T_\ell E=\varprojlim E[\ell^r](\bar k)$ is free of rank two. The compatible pairings identify
$$\bigwedge^2T_\ell E\cong\mathbb Z_\ell(1),\qquad\det\rho_{E,\ell}=\chi_\ell.$$
Thus an elliptic curve over $\mathbb Q$ cannot have full rational $3$-torsion: $\mathbb Q$ does not contain a primitive cube root of unity.
:::

::: {.front card-id="elliptic-finite-field-frobenius" tags="theorem formula application"}
Relate point counts, Frobenius, the Hasse bound, and the zeta function for $E/\mathbb F_q$. Compute the counts over $\mathbb F_5$ and $\mathbb F_{25}$ for $y^2=x^3-x$.
:::

::: {.back card-id="elliptic-finite-field-frobenius"}
Put $a=q+1-\#E(\mathbb F_q)$. Frobenius has polynomial $T^2-aT+q$ on $T_\ell E$, with roots $\alpha,\beta$ of complex absolute value $\sqrt q$.
$$|a|\le2\sqrt q,\qquad\#E(\mathbb F_{q^r})=q^r+1-\alpha^r-\beta^r,\qquad
Z(E,t)=\frac{1-at+qt^2}{(1-t)(1-qt)}.$$
For $x=0,1,2,3,4$ over $\mathbb F_5$, the numbers of $y$ are $1,1,2,2,1$. Including $O$ gives $8$, so $a=-2$.
$$\alpha^2+\beta^2=a^2-2q=-6,\qquad\#E(\mathbb F_{25})=26-(-6)=32.$$
:::

::: {.front card-id="elliptic-ordinary-supersingular-endomorphisms" tags="definition comparison application"}
Compare ordinary and supersingular elliptic curves in characteristic $p$, and compare their geometric endomorphism algebras with characteristic zero. Test $y^2=x^3-x$ over $\mathbb F_5$ and $\mathbb F_7$.
:::

::: {.back card-id="elliptic-ordinary-supersingular-endomorphisms"}
| Case | Geometric $p$-torsion points | $\operatorname{End}(E_{\bar k})\otimes\mathbb Q$ |
| --- | --- | --- |
| Ordinary over $\overline{\mathbb F}_p$ | $\mathbb Z/p$ | Imaginary quadratic field |
| Supersingular over $\overline{\mathbb F}_p$ | Only $O$ | Quaternion algebra ramified at $p$ and infinity |
| Characteristic zero | Prime-to-characteristic torsion has rank two | $\mathbb Q$ or an imaginary quadratic field (CM) |

In both characteristic-$p$ cases the group scheme $E[p]$ has length $p^2$. For $E/\mathbb F_p$, ordinary iff $p\nmid a_p$.

For $y^2=x^3-x$, $\#E(\mathbb F_5)=8$ gives $a_5=-2$, ordinary. Over $\mathbb F_7$ the affine point counts by $x$ are $1,1,0,0,2,2,1$; adding $O$ gives $8$, so $a_7=0$, supersingular. Over $\mathbb C$ the map $(x,y)\mapsto(-x,iy)$ gives CM by $\mathbb Z[i]$.
:::

::: {.front card-id="elliptic-local-reduction-invariants" tags="definition theorem comparison"}
For an elliptic curve over a finite extension $K/\mathbb Q_p$, compare good, multiplicative, and additive reduction using a minimal integral Weierstrass equation. State the Néron–Ogg–Shafarevich criterion.
:::

::: {.back card-id="elliptic-local-reduction-invariants"}
Minimal means $v(\Delta)$ is least among integral Weierstrass equations for $E$.

| Reduction | Minimal invariants | Geometric identity group in the Néron special fiber |
| --- | --- | --- |
| Good | $v(\Delta)=0$ | Elliptic curve |
| Multiplicative | $v(\Delta)>0$, $v(c_4)=0$ | $\mathbb G_m$ |
| Additive | $v(\Delta)>0$, $v(c_4)>0$ | $\mathbb G_a$ |

Multiplicative reduction is split iff the node's tangent directions are rational over the residue field. Semistable reduction means good or multiplicative. For $\ell\ne p$, good reduction iff inertia acts trivially on $T_\ell E$ (Néron–Ogg–Shafarevich). Potential good reduction iff $j(E)$ is integral. A smooth generic fiber does not imply good reduction of a chosen integral equation.
:::

::: {.front card-id="elliptic-local-model-worked" tags="application"}
At $p=5$, classify $y^2=x^3-x$ and $y^2=x^3+x+1$. Explain how rescaling can give a nonminimal equation for the first curve.
:::

::: {.back card-id="elliptic-local-model-worked"}
For $y^2=x^3-x$, $\Delta=64$ is a $5$-adic unit: good reduction. Substituting $x=X/25$, $y=Y/125$ gives $Y^2=X^3-625X$, whose discriminant is $5^{12}\cdot64$. Its singular reduction describes a nonminimal equation, not bad reduction of the curve.

For $y^2=x^3+x+1$, $\Delta=-496$ is also a $5$-adic unit: good reduction. At $p=31$ instead, $v_{31}(\Delta)=1$ and $c_4=-48$ is a unit: multiplicative reduction of type $I_1$. The discriminant valuation one forces minimality, since integral rescaling could only decrease it by a positive multiple of twelve.
:::

::: {.front card-id="elliptic-tate-curve-conductor" tags="theorem formula comparison"}
Describe a Tate curve over a nonarchimedean local field of characteristic zero. Relate its parameter to reduction, the component group, and conductor; distinguish conductor from minimal discriminant.
:::

::: {.back card-id="elliptic-tate-curve-conductor"}
For $q\in K^\times$ with $v(q)>0$, the Tate curve has analytic uniformization
$$E_q(\bar K)=\bar K^\times/q^{\mathbb Z},\qquad j(q)=q^{-1}+744+196884q+\cdots.$$
Every split multiplicative elliptic curve is a Tate curve. Its minimal discriminant satisfies $v(\Delta)=v(q)=n$; the Kodaira type is $I_n$ and the geometric component group is $\mathbb Z/n$.

The conductor is the Artin conductor of $T_\ell E\otimes\mathbb Q_\ell$, $\ell\ne p$. Its local exponent is zero for good reduction, one for multiplicative reduction, and two for additive reduction when $p\ge5$. Wild terms can increase the additive exponent at $p=2,3$. Thus type $I_n$ has discriminant exponent $n$ but conductor exponent one.
:::

::: {.front card-id="elliptic-global-mordell-weil-height" tags="theorem formula"}
State Mordell–Weil and the properties of the canonical height over a number field. How do heights enter the passage from weak Mordell–Weil to finite generation?
:::

::: {.back card-id="elliptic-global-mordell-weil-height"}
For a number field $K$,
$$E(K)\cong\mathbb Z^r\oplus E(K)_{\mathrm{tors}},\qquad
\widehat h(P)=\frac12\lim_{n\to\infty}4^{-n}h(x([2^n]P)).$$
Use absolute logarithmic height and set $h(x(O))=0$. Then
$$\widehat h([m]P)=m^2\widehat h(P),\quad \widehat h(P)=\tfrac12h(x(P))+O(1),\quad
\widehat h(P)=0\iff P\text{ torsion}.$$
The associated bilinear pairing is positive definite on $E(K)/E(K)_{\mathrm{tors}}$. Weak Mordell–Weil gives finiteness of $E(K)/mE(K)$ for $m\ge2$; descent in height plus Northcott finiteness of bounded-height $K$-points yields finite generation. A list of independent points gives a lower bound for $r$, not an upper bound or a saturated basis.
:::

::: {.front card-id="elliptic-selmer-sha-descent" tags="definition theorem application"}
Define the $n$-Selmer group and Tate–Shafarevich group of $E/K$ for a number field. What rank bound follows from a computed Selmer dimension?
:::

::: {.back card-id="elliptic-selmer-sha-descent"}
The Kummer sequence gives $E(K)/nE(K)\hookrightarrow H^1(K,E[n])$. Define
$$\operatorname{Sel}_n(E/K)=\{c\in H^1(K,E[n]):c_v\in\operatorname{im}(E(K_v)/nE(K_v))\text{ for every place }v\},$$
$$\operatorname{Sha}(E/K)=\ker\left(H^1(K,E)\to\prod_vH^1(K_v,E)\right).$$
Thus $\operatorname{Sha}$ classifies everywhere locally soluble torsors, and
$$0\to E(K)/nE(K)\to\operatorname{Sel}_n(E/K)\to\operatorname{Sha}(E/K)[n]\to0.$$
For prime $\ell$, $r\le\dim_{\mathbb F_\ell}\operatorname{Sel}_\ell-\dim_{\mathbb F_\ell}E(K)[\ell]$. If these dimensions are three and two, respectively, then $r\le1$. One independent point proves $r=1$; local solubility alone does not prove a torsor has a rational point.
:::

::: {.front card-id="elliptic-rational-torsion-blackboxes" tags="theorem application"}
State Mazur's rational torsion theorem and the good-reduction test for torsion. Use point counts to determine the torsion of $y^2=x^3-x$ over $\mathbb Q$.
:::

::: {.back card-id="elliptic-rational-torsion-blackboxes"}
For $E/\mathbb Q$, the torsion group is one of
$$\mathbb Z/n\ (1\le n\le10\text{ or }n=12),\qquad
\mathbb Z/2\times\mathbb Z/2m\ (1\le m\le4).$$
At a prime of good reduction $p$, prime-to-$p$ rational torsion injects into $E(\mathbb F_p)$.

For $E:y^2=x^3-x$, good primes $3,5$ give point counts $4,8$. The count at $5$ excludes rational $3$-primary torsion; the count at $3$ excludes $5$-primary torsion. Every other primary part injects at both primes, so the torsion order divides four. The visible points $O,(0,0),(1,0),(-1,0)$ therefore give exactly $(\mathbb Z/2)^2$. This argument does not compute the rank.
:::

::: {.front card-id="elliptic-complex-uniformization-j" tags="construction formula"}
Relate complex elliptic curves, lattices, the Weierstrass $\wp$-function, modular forms, and the modular $j$-function.
:::

::: {.back card-id="elliptic-complex-uniformization-j"}
$$E(\mathbb C)\cong\mathbb C/\Lambda,\qquad
z\mapsto(\wp_\Lambda(z),\wp'_\Lambda(z)),\qquad
(\wp')^2=4\wp^3-g_2\wp-g_3.$$
Lattices give isomorphic pointed curves iff they are homothetic. Writing $\Lambda=\mathbb Z+\mathbb Z\tau$, $\operatorname{Im}\tau>0$, changes of oriented basis act by $\operatorname{SL}_2(\mathbb Z)$.
$$j(\tau)=1728\frac{g_2^3}{g_2^3-27g_3^2}
=\frac{E_4(\tau)^3}{\Delta_{\mathrm{mod}}(\tau)},\qquad
\Delta_{\mathrm{mod}}=\frac{E_4^3-E_6^2}{1728}.$$
For $q=e^{2\pi i\tau}$, $j=q^{-1}+744+196884q+\cdots$. It is a weight-zero modular function, holomorphic on the upper half-plane with a simple pole at the cusp. This analytic function evaluates to the algebraic invariant of the associated cubic; $\Delta_{\mathrm{mod}}$ is not an unnormalized polynomial discriminant.
:::

::: {.front card-id="elliptic-moduli-stack-j-line" tags="definition comparison"}
Describe $\mathcal M_{1,1}$, its coarse moduli space, stabilizers, and compactification over $\mathbb C$. Why is the $j$-line not a fine moduli space?
:::

::: {.back card-id="elliptic-moduli-stack-j-line"}
$\mathcal M_{1,1}(S)$ is the groupoid of elliptic schemes over $S$, with origin-preserving isomorphisms. Using short equations:
$$\mathcal M_{1,1}\cong[\{(A,B):4A^3+27B^2\ne0\}/\mathbb G_m],\qquad
u\cdot(A,B)=(u^4A,u^6B).$$
Its coarse space is $\mathbb A^1_j$. Stabilizers are $\mu_2$ generically, $\mu_4$ at $j=1728$, and $\mu_6$ at $j=0$. Nontrivial automorphisms prevent the coarse space from representing the moduli functor with a universal family.

$\overline{\mathcal M}_{1,1}\cong\mathbb P(4,6)$ as a weighted projective stack; it adds the stable one-pointed nodal rational curve. Its coarse space is $\mathbb P^1_j$, with the added point $j=\infty$. A cuspidal cubic is not a stable boundary curve.
:::

::: {.front card-id="elliptic-modular-curves-level" tags="definition comparison"}
Over $\mathbb C$, distinguish $Y(N)$, $Y_1(N)$, and $Y_0(N)$ by their moduli problems and congruence groups. What is added in $X(N)$, $X_1(N)$, and $X_0(N)$?
:::

::: {.back card-id="elliptic-modular-curves-level"}
Fix a primitive $N$th root of unity for the full-level component.

| Curve | Elliptic data | Group in $\operatorname{SL}_2(\mathbb Z)$ |
| --- | --- | --- |
| $Y(N)$ | Basis $(P,Q)$ of $E[N]$ with fixed Weil pairing | $\Gamma(N):\gamma\equiv I\pmod N$ |
| $Y_1(N)$ | Point $P$ of exact order $N$ | $\Gamma_1(N):a=d=1,c=0\pmod N$ |
| $Y_0(N)$ | Cyclic subgroup $C$ of order $N$ | $\Gamma_0(N):c=0\pmod N$ |

Analytically these are quotients of the upper half-plane; compactification adds cusps, the orbits of $\mathbb P^1(\mathbb Q)$. Cusps represent degenerating generalized elliptic curves, not smooth elliptic curves. Full level $N\ge3$ kills automorphisms and gives a fine moduli problem. Forgetting level gives finite maps to the $j$-line; $Y_0(N)$ also records $j(E/C)$.
:::

::: {.front card-id="elliptic-modular-legendre-example" tags="construction application"}
Describe the Legendre family and its $j$-map. Identify its singular parameters and explain why a generic $j$ has several Legendre parameters.
:::

::: {.back card-id="elliptic-modular-legendre-example"}
$$E_\lambda:y^2=x(x-1)(x-\lambda),\qquad\lambda\in\mathbb C\setminus\{0,1\},$$
$$\Delta=16\lambda^2(1-\lambda)^2,\qquad
j=256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}.$$
The parameters $0,1,\infty$ are cusps of $X(2)\cong\mathbb P^1_\lambda$. Permuting the nonzero $2$-torsion points gives
$$\lambda,\ 1-\lambda,\ 1/\lambda,\ 1/(1-\lambda),\ \lambda/(\lambda-1),\ (\lambda-1)/\lambda.$$
These are generically distinct and have the same $j$. At $\lambda=-1,2,1/2$, $j=1728$. Level two still has the automorphism $[-1]$, so this coarse parameter curve is not a fine moduli space for all families with level-two structure.
:::

::: {.front card-id="elliptic-l-function-bsd" tags="definition conjecture theorem"}
For $E/\mathbb Q$, define its local Euler factors and analytic rank. Separate modularity from the rank assertion of Birch–Swinnerton-Dyer.
:::

::: {.back card-id="elliptic-l-function-bsd"}
$$L(E,s)=\prod_pL_p(p^{-s})^{-1},\qquad
L_p(T)=\begin{cases}1-a_pT+pT^2&\text{good},\\1-T&\text{split multiplicative},\\1+T&\text{nonsplit multiplicative},\\1&\text{additive},\end{cases}$$
where $a_p=p+1-\#E(\mathbb F_p)$ at good primes. Modularity is a theorem: $L(E,s)=L(f,s)$ for a weight-two newform of level equal to the conductor. It gives analytic continuation and the functional equation.

The analytic rank is $\operatorname{ord}_{s=1}L(E,s)$. The BSD rank conjecture asserts equality with $\operatorname{rank}E(\mathbb Q)$; this equality is not a formal consequence of modularity. The refined conjecture also predicts the leading coefficient using periods, regulator, Tamagawa factors, torsion, and the finite order of $\operatorname{Sha}$.
:::
