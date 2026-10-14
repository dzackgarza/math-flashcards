---
title: "Algebraic Geometry::Etale Cohomology"
---

::: {.front card-id="card-75daadffbb2d6b1d"}
What is the sheaf-theoretic definition of a DM stack?
:::

::: {.back card-id="card-75daadffbb2d6b1d"}
An etale sheaf $F\in \Sh_\text{ét}$ which admits a surjective etale morphism ${\textstyle\coprod}\operatorname{Spec}R_i\to F$.
:::

::: {.front card-id="card-852653ad701afe6d"}
What is an etale sheaf?
:::

::: {.back card-id="card-852653ad701afe6d"}
A full subcategory $\Sh_\text{ét}\coloneqq\Sh_\text{ét}(\mathsf{CAlg}_{/ {\ZZ}}) \leq \Fun(\mathsf{CAlg}_{/ {\ZZ}}, \Spaces)$ where if $R\to S$ is etale and faithfully flat, there is a weak equivalence $F(R) \to \Tot F(S{ {}^{ \scriptstyle\otimes_{R}^{\bullet} }  })$.
:::

::: {.front card-id="card-a3ae8ea6c8023dc0"}
What is ${\mathsf{G}\dash\mathsf{Torsors}}_{/ {X}}$?
:::

::: {.back card-id="card-a3ae8ea6c8023dc0"}
Schemes $Y\to X$ with a fiberwise $G\dash$action which etale-locally looks like $G\times X$ with $G\curvearrowright G$ by right-translation, and morphisms are $G\dash$equivariant morphisms over $X$.
:::

::: {.front card-id="card-e02f999b03b66a35"}
What is an **etale morphism**?
:::

::: {.back card-id="card-e02f999b03b66a35"}
$\pi: R\to S\in \mathsf{CAlg}_{/ {\ZZ}}$ is etale iff

$\pi$ is flat

${\partial}_2: S{ {}^{ \scriptstyle\otimes_{R}^{2} }  }\to S$ is flat (i.e. $\pi$ is unramified, given finite presentation).

$S$ is finitely presented over $R$

Equivalently: flat and unramified (and locally of finite presentation).

Formally etale and of finite presentation, where $f\in \mathsf{CRing}(A, B)$ is formally etale iff ${\mathbb{L}}_{B/A} \simeq 0$.

For varieties over $k = \kbar$: a local isomorphism on completed local rings, $\widehat{{\mathcal{O}}}_{Y, f(x)} { \, \xrightarrow{\sim}\, }\widehat{{\mathcal{O}}}_{X, x}$ for all closed points $x$.
:::

::: {.front card-id="card-bee224ddfaf88c1f"}
Discuss how etaleness is related to smoothness.
:::

::: {.back card-id="card-bee224ddfaf88c1f"}
Etale $\implies$ smooth.

Smooth and $\Omega_{S/R} = 0 \implies$ etale.
:::

::: {.front card-id="card-2b4839f683449cdd"}
Is an isogeny etale?
:::

::: {.back card-id="card-2b4839f683449cdd"}
Not always
:::

::: {.front card-id="card-5953f5a347af9d87"}
What are some examples of etale morphisms?
:::

::: {.back card-id="card-5953f5a347af9d87"}
$\cdot n$ on an elliptic curve if $n$ is invertible in the base field.

$t\mapsto t^m$ as a map ${\mathbf{G}}_m{\circlearrowleft}$ if $m$ is prime to the characteristic.

${\mathbf{G}}_m\hookrightarrow{\mathbf{A}}^1$: lfp since $k[t, t^{-1}] = k[t][t^{-1}]$, flat since a Zariski open embedding, and $\Omega^1_{{\mathbf{A}}^1/{\mathbf{G}}_m} = 0$ for the same reason.

Any Zariski open embedding
:::

::: {.front card-id="card-ba72f2bcfd142a9e"}
Give an example of an etale morphism that is not finite onto its image.
:::

::: {.back card-id="card-ba72f2bcfd142a9e"}
$t\mapsto t^2$ on ${\mathbf{G}}_m\setminus\left\{{ 1 }\right\}\to {\mathbf{G}}_m$, not proper so not finite etale.
:::

::: {.front card-id="card-c5569232ab56012f"}
Give an example of a non-etale morphism
:::

::: {.back card-id="card-c5569232ab56012f"}
The normalization of $k[x,y]/xy$, since it is not flat.
:::

::: {.front card-id="card-4892333bbbd29cf0"}
Give an example of a finite flat map that is not etale
:::

::: {.back card-id="card-4892333bbbd29cf0"}
$t\mapsto t^2$ on ${\mathbf{A}}^1{\circlearrowleft}$ since it's ramified at zero: $\Omega^1_f = k[t]\,dt/d(t^2)$ but $2t\,dt$ doesn't generate $k[t]\,dt$. Note the relative differentials are torsion.
:::

::: {.front card-id="card-e7c8df911d1413e9"}
Give an example of a morphism that is not etale, but is finite flat where $\Omega^1_{X/Y}$ is not torsion?
:::

::: {.back card-id="card-e7c8df911d1413e9"}
Take the relative Frobenius $\operatorname{Frob}:{\mathbf{A}}^1\to {\mathbf{A}}^1$ over ${ \mathbf{F} }_p$, then $\Omega^1_{\operatorname{Frob}} = k[t]\,dt/d(t^p) = k[t]\,dt$ which is a line bundle and thus not torsion.
:::

::: {.front card-id="card-dbf8eab901f70ca1"}
Where is a map $F:{\mathbf{A}}^m{\circlearrowleft}$ etale?
:::

::: {.back card-id="card-dbf8eab901f70ca1"}
$F$ is given by $f_1,\cdots, f_n$, and the etale locus is where $\operatorname{Jac}_f$ is a unit.
:::

::: {.front card-id="card-cc6b8833571f5c80"}
What is a formally etale morphism?
:::

::: {.back card-id="card-cc6b8833571f5c80"}
Uniqueness of lifts through nilpotent quotients: for $I$ nilpotent,

Idea: tangent vectors lift
:::

::: {.front card-id="card-d09c4ef4014a45e1"}
Discuss the image of a flat morphism.
:::

::: {.back card-id="card-d09c4ef4014a45e1"}
Always open.
:::

::: {.front card-id="card-638d8935335741a9"}
What are the preservation properties of etale morphisms?
:::

::: {.back card-id="card-638d8935335741a9"}
Any open immersion is etale

Compositions of etale are etale

Base change of etale are etale

2 out of 3 property: $\phi \circ \psi, \phi$ etale $\implies \psi$ etale.
:::

::: {.front card-id="card-bf867cccfe5fbec8"}
What is a site?
:::

::: {.back card-id="card-bf867cccfe5fbec8"}
$\left\{{X_\alpha\to X}\right\}\rightrightarrows X$ in $\mathsf{C}$ a covering family where

Intersections exist: $X_\alpha  \underset{\scriptscriptstyle {X} }{\times} Y$ exists in $\mathsf{C}$ for any $Y\to X$

Intersecting with a cover is a cover: $\left\{{X_\alpha \underset{\scriptscriptstyle {X} }{\times} Y}\right\}\rightrightarrows Y$.

Closed under compositions: if $\left\{{X_{\alpha\beta} \to X_\alpha}\right\}_{\alpha, \beta} \rightrightarrows X_\alpha$ then $\left\{{X_{\alpha_\beta} \to X_\alpha \to X}\right\}_{\alpha, \beta} \rightrightarrows X$.

Isos are always covers.
:::

::: {.front card-id="card-e4c9e1e2c517072d"}
What are the small and big etale sites?
:::

::: {.back card-id="card-e4c9e1e2c517072d"}
**Small**: $X_\text{ét}\subset \Sch_{/ {X}}$ consisting of all etale morphisms over $X$, and families $\left\{{f_\alpha}\right\}$ cover if $\cup\operatorname{im}f_\alpha = X$.

**Big**: $X_\text{Ét}= \Sch_{/ {X}}$ all schemes over $X$ where covering families $f_\alpha$ all etale with $\cup\operatorname{im}f_\alpha = X$.
:::

::: {.front card-id="card-9ad181d2b0fd9497"}
What is the fppf topology?
:::

::: {.back card-id="card-9ad181d2b0fd9497"}
$X_\fppf\subset \Sch_{/ {X}}$ with faithfully flat and finite presentation structure morphisms, covers are covers as in $X_\text{ét}$.
:::

::: {.front card-id="card-acb72a04359f7331"}
What are $X_\zar$ and $X_\Zar$?
:::

::: {.back card-id="card-acb72a04359f7331"}
Small: the site associated to ${\left\lvert {X} \right\rvert}\in\Top$.

Big: $X_\Zar= \Sch_{/ {X}}$ with Zariski-open embeddings and jointly surjective images.
:::

::: {.front card-id="card-9e0087ee732aaf24"}
What is a sheaf on a site?
:::

::: {.back card-id="card-9e0087ee732aaf24"}
$F\in \Fun(\mathsf{C}, \mathsf{D})$ where $F(U) \hookrightarrow\prod_i F(U_i) \rightrightarrows\prod_{i, j} F(U_{ij})$ is an equalizer for all covering families.

Exactness in the middle is gluing, exactness at the beginning is uniqueness.

So $F(U) = \lim \prod F(U_i) \twoheadrightarrow\prod F(U_{ij})$.
:::

::: {.front card-id="card-3c1044a72f3373c0"}
Give an example of a sheaf on $X_\text{Ét}$
:::

::: {.back card-id="card-3c1044a72f3373c0"}
Any representable functor.

$\mu_n$, since represented by $k[t]/t^n-1$ with sections $U\mapsto \left\{{f\in H^0({\mathcal{O}}_U) \st f^n=1}\right\}$.

$U\mapsto H^0({\mathcal{O}}_U)$, since it's represented by ${\mathbf{A}}^1_{/ {X}}$.

$\underline{C_\ell}$ represented by the $C_\ell  \underset{\scriptscriptstyle {k} }{\times} X$ where $C_\ell$ is the constant group scheme, so the underlying set is $X{ {}^{ \scriptscriptstyle\coprod^{\ell} }  }$. This has sections $U\mapsto \Top({\left\lvert {U} \right\rvert}, C_\ell)$.

${\mathbf{G}}_m$ represented by ${\mathbf{G}}_{m_{/ {X}}} = \operatorname{Spec}\ZZ[t, t^{-1}] \underset{\scriptscriptstyle {\ZZ} }{\times} X$, sending $U\mapsto H^0({\mathcal{O}}_U)^{\times}$.

${\mathbf{P}}^n$ represented by $\mathop{\mathrm{Hom}}({-}, {\mathbf{P}}^n_{/ {X}})$, written as a functor sending $U$ to $\mcl\in \operatorname{Pic}(U)$ with $f_U: {\mathcal{O}}(U){ {}^{ \scriptscriptstyle\oplus^{n} }  } \twoheadrightarrow\mcl$.
:::

::: {.front card-id="card-b1c8baa9b8474d0a"}
What is a morphism of sites?
:::

::: {.back card-id="card-b1c8baa9b8474d0a"}
$f\in \mathop{\mathrm{Hom}}(T_1, T_2) \iff f\in \Fun(T_2, T_1)$ which preserves fiber products and covering families.

Compare to $f\in \Top(X, Y)$ inducing $f: \Open(Y)\to \Open(X)$ where $U\mapsto f^{-1}(U)$.
:::

::: {.front card-id="card-da52366be94fb190"}
How are the various sites for a scheme related?
:::

::: {.back card-id="card-da52366be94fb190"}
$X_\fppf\to X_\text{Ét}\to X_\text{ét}\to X_\zar$.
:::

::: {.front card-id="card-264f2a49da65a7ac"}
Give examples of sheaves on $X_\fppf$
:::

::: {.back card-id="card-264f2a49da65a7ac"}
$\Sch_{/ {X}}({-}, Y)$ for any $Y\in \Sch_{/ {X}}$.

$(Z\xrightarrow{f} X) \mapsto H^0(Z, f^* \mcf)$ for any $\mcf\in \Coh(X)$.
:::

::: {.front card-id="card-92995ae2c8714f03"}
What is $\fpqc$?
:::

::: {.back card-id="card-92995ae2c8714f03"}
Finitely presented and quasicompact.
:::

::: {.front card-id="card-d593b091659d56f5"}
What is descent data for $\mcf\in \QCoh(U_{/ {X}})$?
:::

::: {.back card-id="card-d593b091659d56f5"}
$\mcf\in \QCoh(U)$ and $f: U\to X$

Gluing data: $\mathop{\mathrm{proj}}_1^* \mcf\underset{\phi}{ { \, \xrightarrow{\sim}\, }} \mathop{\mathrm{proj}}_2^* \mcf$ where $\mathop{\mathrm{proj}}_i: U \underset{\scriptscriptstyle {X} }{\times} U\to U$.

Cocycle condition: for $\mathop{\mathrm{proj}}_{ij}U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{3} }  }\to U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{2} }  }$, $\mathop{\mathrm{proj}}_{23}^* \phi \circ \mathop{\mathrm{proj}}_{12}^* \phi = \mathop{\mathrm{proj}}_{13}^*\phi$.
:::

::: {.front card-id="card-533776b4ddd31fed"}
What is effective descent?
:::

::: {.back card-id="card-533776b4ddd31fed"}
The pullback $f^*$ induces an equivalence of categories.
:::

::: {.front card-id="card-3e96d99ed7dd0190"}
What is (fppf) descent for $\QCoh(X)$?
:::

::: {.back card-id="card-3e96d99ed7dd0190"}
If $f: U\to X$ is an fppf cover, then $f^*: \QCoh(X)  { \, \xrightarrow{\sim}\, }\mathsf{Descent}(U_{/ {X}})$ is an equivalence of categories, where $\mcf\in \QCoh(X)$ is sent to $f^* \mcf\in \QCoh(U)$ with descent data $(f\circ \mathop{\mathrm{proj}}_1)^* \mcf { \, \xrightarrow{\sim}\, }(f\circ \mathop{\mathrm{proj}}_2)^*\mcf$ an isomorphism on $U \underset{\scriptscriptstyle {X} }{\times} U$ induced by pulling back the identity.
:::

::: {.front card-id="card-5bdf53cb5c2d7bbe"}
What is a quasicoherent sheaf on $\operatorname{Spec}L$ for $L$ a field?
:::

::: {.back card-id="card-5bdf53cb5c2d7bbe"}
An $L\dash$vector space.
:::

::: {.front card-id="card-55f039b56726aa90"}
What is the sheaf-theoretic definition of a scheme?
:::

::: {.back card-id="card-55f039b56726aa90"}
A sheaf on the Zariski site which is locally representable.
:::

::: {.front card-id="card-d5613e3208f138cd"}
What is an algebraic space (sheaf-theoretic definition)?
:::

::: {.back card-id="card-d5613e3208f138cd"}
A sheaf on the big etale site of schemes (over $S$) which need not be representable by a scheme but is locally representable in the etale topology: its diagonal is representable by schemes and there is a scheme $U$ with an etale surjection $U\to X$.

Equivalently, descent data relative to an etale cover $U_{/ {X}}$: $X$ is the quotient sheaf $U/R$ of an etale equivalence relation $R = U \underset{\scriptscriptstyle {X} }{\times} U \rightrightarrows U$.
:::

::: {.front card-id="card-1f48ca5c2b65cddc"}
Give a sufficient condition for the Amitsur complex to be exact.
:::

::: {.back card-id="card-1f48ca5c2b65cddc"}
$R\to S$ faithfully flat, $N\in   {}_{R}\Mod$, and forming the complex from $({-})\otimes_R S$.
:::

::: {.front card-id="card-55f0d671f2cf8cde"}
For $\mcf\in \QCoh(X)$, describe $\mcf^\text{ét}$.
:::

::: {.back card-id="card-55f0d671f2cf8cde"}
$\mcf^\text{ét}(U\xrightarrow{\pi} X) \coloneqq\pi^* \mcf(U)$.
:::

::: {.front card-id="card-af220488b6b891c9"}
Why is the presheaf $\mcf^\text{ét}$ a sheaf?
:::

::: {.back card-id="card-af220488b6b891c9"}
For $U\to V$ an etale cover, need $\mcf(V) \to \mcf(U) \rightrightarrows\mcf(U \underset{\scriptscriptstyle {V} }{\times} U)$.

Use the equalizer $\mathop{\mathrm{Hom}}_X(\mcf_1, \mcf_2) \to \mathop{\mathrm{Hom}}_U(f^* \mcf_1, f^* \mcf_2) \rightrightarrows\mathop{\mathrm{Hom}}_{U \underset{\scriptscriptstyle {X} }{\times} U}(\mathop{\mathrm{proj}}_1 f^* \mcf_1, \mathop{\mathrm{proj}}_1 f^* \mcf_2)$ with $\mcf_2 = \mcf, \mcf_1 = {\mathcal{O}}$.
:::

::: {.front card-id="card-5e9bbb0604ec9e4f"}
Describe ${\mathcal{O}}_X^\text{ét}$.
:::

::: {.back card-id="card-5e9bbb0604ec9e4f"}
$U\to X$ an etale cover maps to $H^0(U; {\mathcal{O}}_U)$.
:::

::: {.front card-id="card-05f86f0a1a83e371"}
Describe faithfully flat descent along $\operatorname{Frob}: X\to X^{(p)}$ over ${ \mathbf{F} }_p$.
:::

::: {.back card-id="card-05f86f0a1a83e371"}
Vector bundles on $X^{(p)}$ are equivalent to descent data for vector bundles on $X^{(p)}$, described as vector bundles $\mce$ on $X$ with a flat connection $\nabla:\mce\to \mce\otimes\Omega^1_{X}$ with $p\dash$curvature zero.
:::

::: {.front card-id="card-c024cb955d1ceca5"}
What is a polarized scheme?
:::

::: {.back card-id="card-c024cb955d1ceca5"}
$(X, \mcl)$ a scheme with an ample line bundle.
:::

::: {.front card-id="card-510b87a25a0f3ea1"}
What is an etale cover of $\operatorname{Spec}k$? Give an example.
:::

::: {.back card-id="card-510b87a25a0f3ea1"}
$Y \coloneqq{\textstyle\coprod}_{i\in I} \operatorname{Spec}L_i$ with each $L_i/k$ a finite separable extension; for $I$ finite, $Y = \operatorname{Spec}A$ for $A = \prod_i L_i$ an etale $k\dash$algebra.

Example: $\operatorname{Spec}L$ where $L/k$ is a finite separable extension.
:::

::: {.front card-id="card-42277796b15d7f27"}
Describe $\Sh(\operatorname{Spec}k)$ for $k=\kbar$.
:::

::: {.back card-id="card-42277796b15d7f27"}
$\Sh(\operatorname{Spec}k) = \Sets$.
:::

::: {.front card-id="card-bc16d6c1d8576f57"}
What is the (etale) skyscraper sheaf for $\mcf\in \Sh(\operatorname{Spec}k)$?
:::

::: {.back card-id="card-bc16d6c1d8576f57"}
For $\overline{x} = \operatorname{Spec}k \xhookrightarrow{\iota_{\overline{x}}} X$, take $(\iota_{\overline{x}})_* \mcf(U\to X) \mcf(U \underset{\scriptscriptstyle {X} }{\times}\overline{x}) = \mcf({\textstyle\coprod}_i \operatorname{Spec}k) = \prod_i \mcf(\operatorname{Spec}k)$ where $i\in I$ with ${\sharp}I$ the number of preimages of $\overline{x}$.
:::

::: {.front card-id="card-3bc2c8cd6c8b9e12"}
What is the stalk (pullback to a geometric point $\overline{x}$) of $\mcf\in \Sh(X_\text{ét})$?
:::

::: {.back card-id="card-3bc2c8cd6c8b9e12"}
$\mcf_{\overline{x}} \coloneqq\iota_{\overline{x}}^*\mcf=\colim_{(U, \overline{u})} \mcf(U)$, a colimit over etale neighborhoods: $U\to X$ is etale and $\overline{u}\to U$ is a lift of $\overline{x}\to X$.
:::

::: {.front card-id="card-188c59bcb8252ddf"}
What is $(\iota_{\overline{x}})^*{\mathcal{O}}_X^\text{ét}$?
:::

::: {.back card-id="card-188c59bcb8252ddf"}
The strict henselization ${\mathcal{O}}_{X, x}^{\mathrm{sh}}$ of the local ring at $\overline{x}$.
:::

::: {.front card-id="card-73bed8df92025557"}
What is a Henselian ring? Strictly Henselian?
:::

::: {.back card-id="card-73bed8df92025557"}
Where Hensel's lemma is true: given a monic polynomial that factors in the residue field, that factorization lifts to the entire ring.

Strict: Henselian with algebraically closed residue field.
:::

::: {.front card-id="card-518717a8c3c22979"}
Show that $\mcf\twoheadrightarrow\mcg\implies \mcf_{x} \twoheadrightarrow\mcg_x$.
:::

::: {.back card-id="card-518717a8c3c22979"}
If not, let $\Lambda = \operatorname{coker}(\mcf_x \to \mcg_x) \neq 0$ at an $x$ where it fails, then let $\mch\coloneqq(\iota_x)_* \Lambda$ be the skyscraper sheaf.

Get an equalizer $\mcf\to \mcg\rightrightarrows^{0}_f \mch$ where $f$ sends a section to its stalk; the composition is zero, forcing $\Lambda = 0$, a contradiction.
:::

::: {.front card-id="card-e883386cd04c22b7"}
Describe global sections as a pushforward
:::

::: {.back card-id="card-e883386cd04c22b7"}
Let $\pi:X\to \operatorname{Spec}k$ be the structure map, then if $k=\kbar$ one has $H^0(\operatorname{Spec}k; \pi_* \mcf) = H^0(X; \mcf)$.
:::

::: {.front card-id="card-8b0c5b096f362767"}
What is the espace etale for $\mcf$?
:::

::: {.back card-id="card-8b0c5b096f362767"}
Write $\text{Ét}(\mcf) \coloneqq\prod_{\overline{x}}(\iota_{\overline{x}})_*\mcf_{\overline{x}}$ where $\overline{x}$ is a geometric point lying over every $x\in X$.

Define $\mcf^a \leq \text{Ét}(\mcf)$ the subsheaf generated by $\mcf$, where $\mcf^a(U)$ are sections $s\in \text{Ét}(\mcf)(U)$ where are locally in the image of the natural map $\mcf\to \text{Ét}(\mcf)$ sending sections to their germs at all points.
:::

::: {.front card-id="card-a0fb3efe2844b83f"}
When do colimits exist in $\underset{ \mathsf{pre}} \Sh(\mathsf{C}, \mathsf{D})$?
:::

::: {.back card-id="card-a0fb3efe2844b83f"}
A sufficient condition: colimits exist in $\mathsf{D}$, since you can compute them pointwise.
:::

::: {.front card-id="card-05c29200f1aa2b91"}
Why do colimits exist in $\Sh(X_\text{ét})$?
:::

::: {.back card-id="card-05c29200f1aa2b91"}
Presheaves over cocomplete categories are cocomplete, and LAPC (left adjoints preserve colimits, left adjoints are easy to map *out* of).
:::

::: {.front card-id="card-74c0dafcd7ad4bc3"}
Discuss adjointness of sheafification.
:::

::: {.back card-id="card-74c0dafcd7ad4bc3"}
Left adjoint to the forgetful functor $\Sh(X_\text{ét})\to  \underset{ \mathsf{pre}} \Sh(X_\text{ét})$ (left adjoints are a mapping out property).
:::

::: {.front card-id="card-2da95491aaa69f35"}
Why is $\Sh(X_\text{ét})$ abelian?
:::

::: {.back card-id="card-2da95491aaa69f35"}
Limits: computed pointwise, over a complete category

Cokernels: a colimit.

$\operatorname{im}= \operatorname{coim}$ can be checked on stalks.
:::

::: {.front card-id="card-7a05add3225ee133"}
Characterize injective objects in ${}_{\ZZ}\Mod$.
:::

::: {.back card-id="card-7a05add3225ee133"}
Divisible groups. Generally need Baer's criterion.
:::

::: {.front card-id="card-88d001160cff1c9a"}
How do you map into or out of a product?
:::

::: {.back card-id="card-88d001160cff1c9a"}
Into: map into each component.
:::

::: {.front card-id="card-72ae81b6c3284eda"}
Describe pullbacks in terms of homs for representable functors.
:::

::: {.back card-id="card-72ae81b6c3284eda"}
If $\mcf= \mathop{\mathrm{Hom}}_X({-}, Z)$, then $f^* \mcf= \mathop{\mathrm{Hom}}_Y({-}, Y \underset{\scriptscriptstyle {X} }{\times} Z)$.
:::

::: {.front card-id="card-d503f5dea206e3f0"}
When does Cech cohomology compute etale cohomology?
:::

::: {.back card-id="card-d503f5dea206e3f0"}
If $X$ is qc and every finite subset is contained in an affine, e.g. if $X$ is quasiprojective.
:::

::: {.front card-id="card-7934c7a9421685ad"}
Write global sections as a hom and cohomology as an ext
:::

::: {.back card-id="card-7934c7a9421685ad"}
${{\Gamma}\qty{X;\mcf} } = \Sh(X)(\underline{\ZZ}\to \mcf)$, so $H^i(\mcf) =  \operatorname{Ext}_{\Sh(X)}(\underline{\ZZ}, \mcf)$.

For $\mcf\in    {}_{{\mathcal{O}}_X}\Mod$, ${{\Gamma}\qty{X;\mcf} } = \QCoh(X)({\mathcal{O}}_X, \mcf)$.
:::

::: {.front card-id="card-4b16e357cf3391ff"}
What is $H^*_\text{ét}({\mathbf{P}}^n; {\mathcal{O}})$?
:::

::: {.back card-id="card-4b16e357cf3391ff"}
$k\cdot t^0$.
:::

::: {.front card-id="card-81cb4768d124a61d"}
What is $H^*(X; \underline{{ \mathbf{F} }_p})$ for $X\in \Sch_{/ {{ \mathbf{F} }_p}}$ quasiprojective?
:::

::: {.back card-id="card-81cb4768d124a61d"}
Use ${\mathbf{G}}_a \coloneqq\mathop{\mathrm{Hom}}({-}, {\mathbf{A}}^1)$ where $U\mapsto {\mathcal{O}}_U(U)$ and the Artin-Schreier exact sequence
$$\underline{{ \mathbf{F} }_p} \hookrightarrow{\mathbf{G}}_a  \xrightarrow[]{x^p-x} { \mathrel{\mkern-16mu}\rightarrow }\, {\mathbf{G}}_a$$
:::

::: {.front card-id="card-c810df3c6a681107"}
Is ${\mathbf{G}}_a \xrightarrow{x^p-x}{\mathbf{G}}_a$ an etale morphism over ${ \mathbf{F} }_p$?
:::

::: {.back card-id="card-c810df3c6a681107"}
Yes: ${\frac{\partial }{\partial x}\,}(x^p-x) = -1$ which is invertible.
:::

::: {.front card-id="card-9a0ac67ff3514017"}
Why is $H_\text{ét}(X; { \mathbf{F} }_p)$ poorly behaved?
:::

::: {.back card-id="card-9a0ac67ff3514017"}
Expect a functorial assignment to ${}_{\ZZ}\Mod^\fg$, but e.g. even on affines on gets $H^0(X;{ \mathbf{F} }_p)\hookrightarrow{\mathcal{O}}_X(X) \xrightarrow{\mathrm{AS}: t^p-t} {\mathcal{O}}_X(X)\twoheadrightarrow H^1(X; { \mathbf{F} }_p)$ where $\operatorname{coker}\mathrm{AS}$ is not finitely generated.
:::

::: {.front card-id="card-53abacdf4c2019ba"}
What is a $G\dash$torsor?
:::

::: {.back card-id="card-53abacdf4c2019ba"}
Idea: $\mcf\in \Sh(X_\text{ét},\Sets)$ where $G\curvearrowright\mcf$ simply transitively on every fiber.

Precisely: for $G\in \Sh(X, \Grp)$ and $\mcf\in \Sh(X, \Sets)$, an action $G\times \mcf\xrightarrow{\alpha} \mcf$ which is simply transitive, i.e. an isomorphism $G\times \mcf\xrightarrow{\alpha \times \mathop{\mathrm{proj}}_2}\mcf\times \mcf$
:::

::: {.front card-id="card-be55e054cca39a3d"}
What is $A\times B$ in terms of fiber products?
:::

::: {.back card-id="card-be55e054cca39a3d"}
$A \underset{\scriptscriptstyle {T} }{\times} B$ where $T$ is the terminal object.
:::

::: {.front card-id="card-698bc728422cf6da"}
Describe ${\mathsf{G}\dash\mathsf{Torsors}}$ for $G\in \Fin\Grp$.
:::

::: {.back card-id="card-698bc728422cf6da"}
A finite etale cover with Galois group $G$.

E.g. for $X$ a smooth curve: an extension $L/K(X)$ with $\Gal(L/K(X)) = G$ which is everywhere unramified.
:::

::: {.front card-id="card-7e1e3edfeee61088"}
What is the representing object for ${\mathbf{G}}_m$?
:::

::: {.back card-id="card-7e1e3edfeee61088"}
$\mathop{\mathrm{Hom}}_X({-}, \operatorname{Spec}k[t, t^{-1}])$.
:::

::: {.front card-id="card-150ff4585743a877"}
Describe ${\mathsf{{\mathbf{G}}_m}\dash\mathsf{Torsors}}$
:::

::: {.back card-id="card-150ff4585743a877"}
A line bundle $\mcl\setminus\left\{{0}\right\}$ with the zero section deleted.

Send $\mcl\to \underline{ \operatorname{Spec}} _X \bigoplus_{n\in \ZZ}\mcl{ {}^{ \scriptstyle\otimes_{}^{n} }  }$.
:::

::: {.front card-id="card-a1cabc515b4610ba"}
Describe ${\mathsf{\operatorname{GL}_n}\dash\mathsf{Torsors}}$?
:::

::: {.back card-id="card-a1cabc515b4610ba"}
Vector bundles of rank $n$, sending a bundle $\mce\to \mathop{\mathrm{Frame}}(\mce) \coloneqq\mathop\Isom_{X_\text{ét}}({\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  }, \mce)$ with inverse $T\mapsto (T\times {\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  })/ \operatorname{GL}_n$, using that $\operatorname{GL}_n = \underline{\mathop{\mathrm{Aut}}}({\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  })$.
:::

::: {.front card-id="card-78f1fdc931f88e02"}
What is a splitting of a $G\dash$torsor?
:::

::: {.back card-id="card-78f1fdc931f88e02"}
Locally trivial: $T\in{\mathsf{G}\dash\mathsf{Torsors}}$ is split by an etale cover $U\to X$ if ${ \left.{{T}} \right|_{{U}} }  { \, \xrightarrow{\sim}\, }{ \left.{{G}} \right|_{{U}} }$ as a torsor.
:::

::: {.front card-id="card-6a85c4c2d825fc10"}
Describe $\mathop{\mathrm{Aut}}(T)$ for $T\in{\mathsf{G}\dash\mathsf{Torsors}}$ trivial.
:::

::: {.back card-id="card-6a85c4c2d825fc10"}
An element of $G$ -- look at $G\dash$torsors over a point.
:::

::: {.front card-id="card-cda28f9377fc6d47"}
Describe $H^1_\text{ét}(\tau; \mcf)$ for $\tau$ a site.
:::

::: {.back card-id="card-cda28f9377fc6d47"}
Locally trivial $\mcf\dash$torsors.
:::

::: {.front card-id="card-980dedd9047e6da6"}
What is Hilbert 90? How is it proved?
:::

::: {.back card-id="card-980dedd9047e6da6"}
$$\cechH^1(X_\zar; \underline{\operatorname{GL}_n})  { \, \xrightarrow{\sim}\, }\cechH^1(X_\text{ét}; \underline{\operatorname{GL}_n})  { \, \xrightarrow{\sim}\, }\cechH^1(X_\fppf; \underline{\operatorname{GL}_n})$$
Use bijection with locally split $\operatorname{GL}_n\dash$torsors, use this to get descent data for a vector bundle, use fppf descent.

Alternative statement: $H^1(\Gal(k^s/k), \overline{k}^{\times})$.
:::

::: {.front card-id="card-063fa523755a2553"}
Describe how to parameterize $n\dash$dimensional vector bundles on $X$.
:::

::: {.back card-id="card-063fa523755a2553"}
$H^1_\text{ét}(X_\tau; \operatorname{GL}_n)$ where $\tau$ is any site appearing in Hilbert 90.
:::

::: {.front card-id="card-d43b6704b847d2cd"}
Are all $G\dash$torsors represented by an $X\dash$scheme?
:::

::: {.back card-id="card-d43b6704b847d2cd"}
Yes.
:::

::: {.front card-id="card-2839fdf678b48b16"}
If $T\in{\mathsf{G}\dash\mathsf{Torsors}}$, does fppf-locally trivial imply etale locally trivial?
:::

::: {.back card-id="card-2839fdf678b48b16"}
No in general, yes if $G$ is smooth.

Take $\ker \operatorname{Frob}$ on ${\mathbf{G}}_a$ or ${\mathbf{G}}_m$, so $\alpha_p$ or $\mu_p$, in characteristic $p$.

In general, any positive dimensional affine group scheme.
:::

::: {.front card-id="card-4d12ad5a7a670008"}
What is $H^1_\text{ét}(\operatorname{Spec}k; {\mathbf{G}}_m)?$
:::

::: {.back card-id="card-4d12ad5a7a670008"}
Line bundles on a point are trivial: $H^1_\text{ét}(\operatorname{Spec}k, {\mathbf{G}}_m) = 0 = H^1(\Gal(k^s/k), \overline{k}^{\times})$.
:::

::: {.front card-id="card-e9704f16792da6d7"}
What is $H^1(X_\text{ét}; {\mathbf{G}}_m)$?
:::

::: {.back card-id="card-e9704f16792da6d7"}
$\operatorname{Pic}(X)$.
:::

::: {.front card-id="card-0f4208d6b758a315"}
What is $H^1(X_\text{ét}; \mu_\ell)$ with $\ell$ invertible in $X$.
:::

::: {.back card-id="card-0f4208d6b758a315"}
Use the Kummer SES $\mu_\ell \hookrightarrow{\mathbf{G}}_m  \xrightarrow[]{z\mapsto z^\ell} { \mathrel{\mkern-16mu}\rightarrow }\,  {\mathbf{G}}_m$.
:::

::: {.front card-id="card-2d37db581653b7f6"}
How do you explicitly write down a cover corresponding to an element in $H^1(X_\text{ét}; { \mathbf{F} }_p)$?
:::

::: {.back card-id="card-2d37db581653b7f6"}
Write $H^1 = \operatorname{coker}({\mathcal{O}}_X \xrightarrow{x^p - x}{\mathcal{O}}_X) \ni f$ and take $Y = \left\{{y^p-y = f}\right\}$.
:::

::: {.front card-id="card-0e183972b0079b4a"}
How do you explicitly write down a cover corresponding to an element in $H^1(X_\text{ét}; \mu_\ell)$?
:::

::: {.back card-id="card-0e183972b0079b4a"}
Write $H^1 = \operatorname{coker}({\mathcal{O}}_X^{\times}\xrightarrow{x\mapsto x^\ell}{\mathcal{O}}_X^{\times})\ni f$ and take $Y = \left\{{z^\ell = f}\right\}$.

Needs $\operatorname{Pic}(X) = 0$.
:::

::: {.front card-id="card-9e06c52c835ebde1"}
Describe $H^*_\text{ét}(X; {\mathbf{G}}_m)$ for $X$ a smooth curve over $k=\kbar$.
:::

::: {.back card-id="card-9e06c52c835ebde1"}
$H^0 = {\mathcal{O}}_X(X)^{\times}$, $H^1 = \operatorname{Pic}(X)$, and $H^i = 0$ for $i\geq 2$. As a Poincare series: ${\mathcal{O}}_X(X)^{\times}t^0+ \operatorname{Pic}(X) t$.
:::

::: {.front card-id="card-85f90d33b9543c8d"}
Describe $H_\text{ét}(X; \mu_\ell)$ for $X$ a smooth proper curve over $k=\kbar$.
:::

::: {.back card-id="card-85f90d33b9543c8d"}
$C_{\ell^n} + \operatorname{Pic}[\ell^n]t + C_\ell t^2$ where $\operatorname{Pic}(\ell^n) \cong C_{\ell^n}^{2g}$, using the Kummer sequence and that $\operatorname{Pic}^0(X) \cong \operatorname{Jac}(X)$ is divisible and $\NS(X) = \ZZ$.
:::

::: {.front card-id="card-6020cd9b5e82b1ea"}
For $f\in \Sch(X, Y)$, how is $f_* \in [\Sh(X_\text{ét}), \Sh(Y_\text{ét})]$ defined?
:::

::: {.back card-id="card-6020cd9b5e82b1ea"}
$f_*\mcf(U\to X)\coloneqq\mcf(U \underset{\scriptscriptstyle {Y} }{\times} X)$.
:::

::: {.front card-id="card-2220fcfe78518e2f"}
What is the interpretation of ${\mathbf{R}}^* f_*$?
:::

::: {.back card-id="card-2220fcfe78518e2f"}
Cohomology of fibers, sometimes -- obstructed by non-commuting with base change.

Sheafification of $V\mapsto H^i(f^{-1}(V); \mcf)$.
:::

::: {.front card-id="card-d9f56d50a848f341"}
Give an example where $\tau_{\geq 1}{\mathbf{R}}f_* = 0$.
:::

::: {.back card-id="card-d9f56d50a848f341"}
$f$ a finite morphism, e.g. a closed immersion. Show $f_*$ is right exact by checking on stalks $\bigoplus_{\overline{x}\in f^{-1}(\overline{y})}\mcf_{\overline{x}}$.
:::

::: {.front card-id="card-0b69073c020351c0"}
Why does $f_*$ preserve injectives?
:::

::: {.back card-id="card-0b69073c020351c0"}
True for any functor with an exact left adjoint, here take $f^*$, exact since filtered colimits and sheafification are exact (or check on stalks).
:::

::: {.front card-id="card-fa84f0f582a734a4"}
What is $H_\Gal(k; V)$ for $k$ a finite field and $V\in {}_{k}\Mod$?
:::

::: {.back card-id="card-fa84f0f582a734a4"}
$V^G t^0 + V_G t^1$.
:::

::: {.front card-id="card-eb7119e95217b99e"}
Is a sequence of presheaves exact iff exact on all sections?
:::

::: {.back card-id="card-eb7119e95217b99e"}
True! Just not true for sheaves.
:::

::: {.front card-id="card-9f4ecc81ca613738"}
For $X$ integral and $\iota:\eta \hookrightarrow X$ a generic point, what are the stalks of ${\mathbf{R}}\iota_* \mcf$?
:::

::: {.back card-id="card-9f4ecc81ca613738"}
Write $K_X \coloneqq\operatorname{ff}({\mathcal{O}}_X)$, use that stalks agree on sheaves vs presheaves to get
$$\colim_{u\hookrightarrow U} H^i(U_\eta; { \left.{{\mcf}} \right|_{{U_\eta}} }) = H^i(K_{X, \overline{x}}; { \left.{{\mcf}} \right|_{{K_{X, \overline{x}}}} })$$
at $\overline{x}\hookrightarrow X$ a geometric point.
:::

::: {.front card-id="card-098b965608d950da"}
What is the point pushforward SES?
:::

::: {.back card-id="card-098b965608d950da"}
If $\iota:\eta \hookrightarrow X$ for $X$ a regular variety,
$${\mathbf{G}}_m \hookrightarrow\eta_*{\mathbf{G}}_m\twoheadrightarrow\bigoplus_{Z\leq X \,\, \operatorname{codim}_X(Z) = 1} \iota_* \underline{\ZZ}$$
where the last term is the divisor sheaf.

The first map is restriction to $\eta$, the second is taking the associated divisor.
:::

::: {.front card-id="card-b14cffe05a0fd671"}
How is an integral domain related to all of its localizations?
:::

::: {.back card-id="card-b14cffe05a0fd671"}
$A = \bigcap_{p\in \operatorname{Spec}(A)^{\operatorname{ht}= 1}} A_p$.
:::

::: {.front card-id="card-11edab857d7d6bd6"}
Define the cohomological Brauer group $\Brauer^{\mathrm{coh}}(X)$.
:::

::: {.back card-id="card-11edab857d7d6bd6"}
$\Brauer^{\mathrm{coh}}(X) \coloneqq H^2_\text{ét}(X; {\mathbf{G}}_m)_\tors$.

Compare: the Brauer group $\Brauer(X)$ is $\operatorname{im}\qty{\bigcup_n \mcp_n \xrightarrow{\delta} H^2_\text{ét}(X; {\mathbf{G}}_m)}$ where $\mcp_n$ is the set of all etale locally trivial $\operatorname{PGL}_n\dash$torsors over $X$, which is the boundary map coming from ${\mathbf{G}}_m\hookrightarrow\operatorname{GL}_n\twoheadrightarrow\operatorname{PGL}_n$. It is contained in $\Brauer^{\mathrm{coh}}(X)$, with equality e.g. for $X$ quasi-projective over a field (Gabber).
:::

::: {.front card-id="card-a58311cd6c6d2d24"}
What does $H^1$ classify? $H^2$?
:::

::: {.back card-id="card-a58311cd6c6d2d24"}
$H^1$: torsors. $H^2$: gerbes.
:::

::: {.front card-id="card-c175b0a96cd47db3"}
What is the interpretation of $\delta([T])$?
:::

::: {.back card-id="card-c175b0a96cd47db3"}
For $T\in H^i(X_\text{ét}; \operatorname{PGL}_n)$, the obstruction to lifting $T$ to a $\operatorname{GL}_n\dash$torsor.

Equivalently: the Brauer class of $T$.
:::

::: {.front card-id="card-68554af369489477"}
Describe how to relate $G\dash$torsors and forms.
:::

::: {.back card-id="card-68554af369489477"}
For $T = \Sh(X_\text{ét}, \Sets)$ and $G = \mathop{\mathrm{Aut}}(X)$, locally split $G\dash$torsors $\rightleftharpoons$ forms of $T$.

Forms $F$ map to $\mathop\Isom(F, T)$.

Torsors $\tau$ map to the sheaf quotient $(T\times \tau)/G$.
:::

::: {.front card-id="card-5bfa89790017c57c"}
What is a Severi-Brauer $X\dash$scheme?
:::

::: {.back card-id="card-5bfa89790017c57c"}
Forms of ${\mathbf{P}}^n_X$; for $X=\operatorname{Spec}k$ these are Severi-Brauer varieties.
:::

::: {.front card-id="card-18e4be89c3949cb8"}
What is an Azumaya algebra?
:::

::: {.back card-id="card-18e4be89c3949cb8"}
Forms of $\operatorname{Mat}_{n\times n} = { \operatorname{End} }_{\mathcal{O}}({\mathcal{O}}{ {}^{ \scriptscriptstyle\oplus^{n} }  })$.
:::

::: {.front card-id="card-e6bc33ed322c0a72"}
What is $\QCoh(X, \alpha)$?
:::

::: {.back card-id="card-e6bc33ed322c0a72"}
For $U\to X$ an etale cover, $\alpha\in H^0(U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{3} }  }; {\mathbf{G}}_m)$ representing $[\alpha]\in H^2_\text{ét}(X; {\mathbf{G}}_m)$, a sheaf $\mcf\in \QCoh(X)$ with an isomorphism $\phi: \mathop{\mathrm{proj}}_1 \mcf { \, \xrightarrow{\sim}\, }\mathop{\mathrm{proj}}_2\mcf$ for $\mathop{\mathrm{proj}}_i: U{ {}^{ \scriptscriptstyle \underset{\scriptscriptstyle {X} }{\times}^{2} }  }\to U$ satisfying a twisted cocycle condition
$$\pi_{23}^* \phi \circ \pi_{12}^* \phi = \alpha \cdot \pi_{13}^* \phi$$
Morphisms are sheaf morphisms commuting with $\phi$.
:::

::: {.front card-id="card-bd2ee1846d1bd8f8"}
State etale descent in terms of $\alpha\dash$twisted sheaves.
:::

::: {.back card-id="card-bd2ee1846d1bd8f8"}
$\QCoh(X, 1) = \QCoh(X)$ canonically.
:::

::: {.front card-id="card-32f74646eb291916"}
Describe homs, tensors, and symmetric powers on $\QCoh(X, \alpha)$.
:::

::: {.back card-id="card-32f74646eb291916"}
$$\begin{align*}\mathop{\mathrm{Hom}}: \QCoh(X,\alpha_1) \times \QCoh(X,\alpha_2) &\to \QCoh(X,\alpha_1 \cdot \alpha_2^{-1}) \\ \otimes: \QCoh(X,\alpha_1) \times \QCoh(X,\alpha_2) &\to \QCoh(X,\alpha_1\cdot \alpha_2) \\ \operatorname{Sym}^n, \bigwedge^n: \QCoh(X,\alpha_1) &\to \QCoh(X,n \cdot \alpha_1)\end{align*}$$
:::

::: {.front card-id="card-83d3a99ae264e33d"}
Discuss when a 2-cocycle $[\alpha]$ for ${\mathbf{G}}_m$ relates to Brauer classes.
:::

::: {.back card-id="card-83d3a99ae264e33d"}
$[\alpha]\in \Brauer(X) \iff \exists \mce$ and $\alpha\dash$twisted vector bundle.

The forward direction corresponds to $\delta([\alpha])$, the reverse is projectivizing a bundle to get a form of ${\mathbf{P}}^n$.
:::

::: {.front card-id="card-c9ac4e103c3026eb"}
Why is $\Brauer(X)$ a group?
:::

::: {.back card-id="card-c9ac4e103c3026eb"}
For $\alpha_1\cdot \alpha_2$, take $\mce_1\otimes\mce_2$ for the corresponding twisted vector bundles.

For $\alpha_1^{-1}$, take $\mce_1 {}^{ \vee }$.
:::

::: {.front card-id="card-8b92910aa25d644d"}
How can one check when $[\alpha]$ is trivial?
:::

::: {.back card-id="card-8b92910aa25d644d"}
$[\alpha] = 1 \iff \exists \mcl$ an $\alpha\dash$twisted line bundle.

Forward: take $\mcl= {\mathcal{O}}_X$, reverse: use descent data to get $\beta$ with $\delta(\beta) = \alpha$.
:::

::: {.front card-id="card-342c02b96e33dd3b"}
What does $\mce$ an $\alpha\dash$twisted vector bundle of rank $n$ correspond to in $\Brauer(X)$?
:::

::: {.back card-id="card-342c02b96e33dd3b"}
$\alpha\in H^2(X_\text{ét}; {\mathbf{G}}_m)[n]$, $n\dash$torsion.

Proof: take $\operatorname{det}\mce$ to get an $\alpha^n\dash$twisted line bundle, implies $1 = [\alpha^n] = [\alpha]^n$.

Warning: $n\dash$torsion elements do not generally yield rank $n$ bundles.
:::

::: {.front card-id="card-256b401a60ea80e5"}
Give an example of a twisted form of ${\mathbf{P}}^1$.
:::

::: {.back card-id="card-256b401a60ea80e5"}
$x^2+y^2+z^2 = 0$ over ${\mathbf{R}}$, a smooth conic with no rational points. By projection, a rational point induces an isomorphism to ${\mathbf{P}}^1$, and this acquires points after base-changing to $\CC$.
:::

::: {.front card-id="card-27bb4a89f446569b"}
What is the generator of $\Brauer({\mathbf{R}})$?
:::

::: {.back card-id="card-27bb4a89f446569b"}
Hamilton quaternions: central division algebra, hence Azumaya.
:::

::: {.front card-id="card-1150011a3e0ae7d8"}
How are twisted sheaves related to Severi-Brauers and Azumaya algebras?
:::

::: {.back card-id="card-1150011a3e0ae7d8"}
${\mathbf{P}}(\mce)$ is SB.

${ \operatorname{End} }(\mce)$ is Azumaya.
:::

::: {.front card-id="card-be9b047c3ed3af5f"}
What is $\Brauer({ \QQ_p })$?
:::

::: {.back card-id="card-be9b047c3ed3af5f"}
$\Brauer({ \QQ_p }) = \QQ/\ZZ$.
:::

::: {.front card-id="card-5eff17526136d40b"}
What is the SES involving $\Brauer(\QQ)$?
:::

::: {.back card-id="card-5eff17526136d40b"}
$$\Brauer(\QQ) \hookrightarrow\bigoplus_{p\in \Places{\QQ}} \Brauer({ \QQ_p }) \twoheadrightarrow\QQ/\ZZ$$
:::

::: {.front card-id="card-43ff4cf1d119ff4f"}
What is the period-index question?
:::

::: {.back card-id="card-43ff4cf1d119ff4f"}
Given $\alpha\in \Brauer(X)$, what is the minimal rank of an $\alpha\dash$twisted vector bundle?

Over a field, for 2-torsion one can always find $\operatorname{rank}\mce= 2$.
:::

::: {.front card-id="card-416a6f110d125a53"}
What is an $A\dash$algebra $B$?
:::

::: {.back card-id="card-416a6f110d125a53"}
A ring $B$ equipped with a ring morphism $A\to B$.
:::

::: {.front card-id="card-cccaf33fd51690b0"}
What is the trace of a module?
:::

::: {.back card-id="card-cccaf33fd51690b0"}
Realized as a morphism
$$\operatorname{Tr}:   {}_{A}\Mod(M, M) \to A$$
of $A\dash$modules for $M\in   {}_{A}\Mod^\fg$. For $M\in { {}_{A}  \mathsf{Alg}} \cap  {}_{B}\Mod^{\fg, \free}$, define
$$\operatorname{Tr}_{B/A}(b) \coloneqq\operatorname{Tr}(x\mapsto bx) \in   {}_{A}\Mod$$
which satisfies $\operatorname{Tr}(a) = \operatorname{rank}_A(B)\cdot a$ for $a\in A$.
:::

::: {.front card-id="card-7adc79376091ce58"}
What is a separable algebra?
:::

::: {.back card-id="card-7adc79376091ce58"}
When the following natural map is an iso:
$$\begin{align}\phi: B &\to   {}_{A}\Mod(B, A) \\ x &\mapsto \operatorname{Tr}(x\cdot)\end{align}$$
:::

::: {.front card-id="card-38043113129283c0"}
What are the free separable $k\dash$algebras $L$ over $k$ a field?
:::

::: {.back card-id="card-38043113129283c0"}
$L = \prod_{i=1}^t B_i$ where each $B_i/k$ is a finite separable extension and $t>0$.
:::

::: {.front card-id="card-a46fceff1ee22bd9"}
What is a finite etale morphism $f:Y\to X$?
:::

::: {.back card-id="card-a46fceff1ee22bd9"}
$\exists \operatorname{Spec}A_i \rightrightarrows Y$ where each $f^{-1}(\operatorname{Spec}A_i) = \operatorname{Spec}B_i$ is affine and $B_i/A_i$ is a free separable $A_i\dash$algebra.

In particular, $f$ is a finite morphism, so each $B_i\in   {}_{A_i}\Mod^{\fg}$ which need not be free, but turns out to always be projective.
:::

::: {.front card-id="card-1f05bbd2c82a121f"}
What are the finite etale covers $Y\to \operatorname{Spec}\ZZ_K$, the ring of integers of an algebraic number field $K$?
:::

::: {.back card-id="card-1f05bbd2c82a121f"}
$Y\to X$ where $Y \cong {\textstyle\coprod}_{i=1}^t \operatorname{Spec}A_i$ where $t\geq 0$ and each $A_i = \ZZ_{K_i}$ where $K_i/K$ is a finite extension unramified at all $\mfp\in \operatorname{Spec}(A_i)\setminus\left\{{0}\right\}$.
:::

::: {.front card-id="card-c7eb78fa3f812b46"}
What is the fundamental theorem of Galois theory for schemes?
:::

::: {.back card-id="card-c7eb78fa3f812b46"}
Let $X$ be a connected scheme. Then there exists a profinite group $\pi$, uniquely determined up to isomorphism, such that the category $\mathbf{F E t}_X$ of finite etale coverings of $X$ is equivalent to the category $\pi$-sets of finite sets on which $\pi$ acts continuously.
:::

::: {.front card-id="card-3a960b65293975d0"}
What is $\pi_1^\text{ét}\operatorname{Spec}\ZZ$?
:::

::: {.back card-id="card-3a960b65293975d0"}
Trivial: every finite etale cover is the free separable $\ZZ\dash$algebra $\ZZ^n$ (and there are not others).
:::

::: {.front card-id="card-abce709063f217b0"}
What is $\pi_1^\text{ét}\operatorname{Spec}k$ for $k=\kbar$?
:::

::: {.back card-id="card-abce709063f217b0"}
Trivial: the only covers are $k^n$.
:::

::: {.front card-id="card-4a00f38d56568ada"}
What is $\pi_1^\text{ét}\operatorname{Spec}k$ in general?
:::

::: {.back card-id="card-4a00f38d56568ada"}
$\Gal(k^{ {}^{ \operatorname{sep} } }/k)$.
:::

::: {.front card-id="card-a4595b81ac3f6346"}
What is $\pi_1^\text{ét}\operatorname{Spec}{ \mathbf{F} }_q$?
:::

::: {.back card-id="card-a4595b81ac3f6346"}
$\widehat{\ZZ}$
:::

::: {.front card-id="card-17ed51b5c64ddd99"}
What is $\pi_1^\text{ét}\operatorname{Spec}\ZZ_K$ for $K$ an algebraic number field?
:::

::: {.back card-id="card-17ed51b5c64ddd99"}
$\Gal(M/K)$ where $M$ is the maximal algebraic extension unramified over $\operatorname{Spec}(\ZZ_K)\setminus\left\{{0}\right\}$.
:::

::: {.front card-id="card-604889e7fbd1e9a0"}
What is $\pi_1^\text{ét}\operatorname{Spec}{\ZZ_K} { \left[ { \scriptstyle \frac{1}{a} } \right] }$ for $a\in \ZZ_K\setminus\left\{{0}\right\}$ for $K$ a number field?
:::

::: {.back card-id="card-604889e7fbd1e9a0"}
$\Gal(M_a/K)$ where $M_a$ is the maximal extension unramified at all primes not dividing $a$.
:::

::: {.front card-id="card-aa331a90c96ed6ac"}
What is $\pi_1^\text{ét}\operatorname{Spec}{ \ZZ_{\widehat{p}} }$?
:::

::: {.back card-id="card-aa331a90c96ed6ac"}
$\widehat{\ZZ}$.
:::

::: {.front card-id="card-d9953327ca35f95c"}
What is $\pi_1^\text{ét}{\mathbf{P}}^1_{/ {k}}$ for $k$ a field?
:::

::: {.back card-id="card-d9953327ca35f95c"}
$\pi_1^\text{ét}\operatorname{Spec}k = \Gal(k^{ {}^{ \operatorname{sep} } }/k)$.
:::
