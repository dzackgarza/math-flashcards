---
title: "Number Theory::Class Field Theory"
---

::: {.front card-id="card-095230d6aa734d77"}
What is $H^q(K; M)$ for $K\in \mathsf{Field}$?
:::

::: {.back card-id="card-095230d6aa734d77"}
$H^q({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); M)$ the profinite group cohomology.
:::

::: {.front card-id="card-63e5e2b2fef8dfc0"}
What is the Weil-Chatelet group $\mathrm{WC}(A/K)$?
:::

::: {.back card-id="card-63e5e2b2fef8dfc0"}
For $A\in{\mathsf{Grp}}{\mathsf{Sch}}$ commutative, or $A$ any commutative group, $H^1(K; A)\coloneqq H^1({ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k); A(k^{ {}^{ \operatorname{sep} } }))$.
:::

::: {.front card-id="card-6ed7fecddc2418ed"}
What is the relative Galois cohomology $H^n(L/K; A)$?
:::

::: {.back card-id="card-6ed7fecddc2418ed"}
$\ker\qty{H^n(K; M) \to H^n(L; M)}$.
:::

::: {.front card-id="card-fe6430fdbe903e0a"}
Define a Galois extension.
:::

::: {.back card-id="card-fe6430fdbe903e0a"}
Algebraic, normal, separable.
:::

::: {.front card-id="card-570ae19fe569a383"}
What is $H^n({ \mathsf{Gal}}(L/K); L)$?
:::

::: {.back card-id="card-570ae19fe569a383"}
Zero for $n\geq 1$; "additive" Hilbert 90 since $\implies H^n(K; {\mathbf{G}}_a) = 0$.
:::

::: {.front card-id="card-228e5547c91384fb"}
What is the normal basis theorem?
:::

::: {.back card-id="card-228e5547c91384fb"}
For $L/K$ finite Galois, $\exists \alpha\in L$ such that $G_{L/K}.\alpha$ generates $L\in   {}_{K}{\mathsf{Mod}}$, i.e. $L = \left\langle{G_{L/K}.\alpha}\right\rangle_K$. Since ${\sharp}G_{L/K} = [L: K]$, the conjugates of $\alpha$ are a $K$-basis of $L$.

For $G\coloneqq G_{L/K}$, iff ${\mathbf{G}}_a(L) = L \cong K[G] \in   {}_{K[G]}{\mathsf{Mod}}$, so rank 1 with generator $\alpha$.

Iff $L\cong {\mathbf{Z}}[G]\otimes_{\mathbf{Z}}K \in   \mods{\ZZ[G]}$, so $L$ is induced.
:::

::: {.front card-id="card-2fc69737d44e07a9"}
What is Hilbert 90?
:::

::: {.back card-id="card-2fc69737d44e07a9"}
For $L/K$ Galois, $G = { \mathsf{Gal}}(L/K)$,
$$H^1(G; L^{\times}) = 0$$
This is false for $q\gt 1$!

Think of this as $H^1(G; {\mathbf{G}}_m) = 0$.
:::

::: {.front card-id="card-27a39505ab4a8c1b"}
What is $\mathrm{Br}(K)$?
:::

::: {.back card-id="card-27a39505ab4a8c1b"}
$\mathrm{Br}(K) \coloneqq H^2(K; {\mathbf{G}}_m)$.
:::

::: {.front card-id="card-dfccee2093478cfd"}
What is classical Hilbert 90?
:::

::: {.back card-id="card-dfccee2093478cfd"}
For $L/K$ finite cyclic Galois with $G_{L/K} = \left\langle{\sigma}\right\rangle$,

For $\alpha\in L$, $\operatorname{Trace}_{L/K}(\alpha) = 0 \iff \exists \lambda\in L$ such that $\alpha = \lambda - \sigma(\lambda)$.

Why: $0 = H^1(G;L) = \widehat{H}^{-1}(G; L) = \widehat{H}_0(G; L) = \ker(N: L\to K)/(\sigma - 1)L$ but here $N$ is the sum of Galois conjugates, hence the trace

$\operatorname{Nm}_{L/K}(\alpha) = 1 \iff \exists \lambda \in L$ such that $\alpha = \lambda/\sigma(\lambda)$.

Why: $0 = H^1(G; L^{\times}) = \widehat{H}^{-1}(G; L^{\times})=\ker(N)/ (\sigma-1)L^{\times}$ multiplicatively.
:::

::: {.front card-id="card-19dda55760e13c46"}
Discuss Kummer theory for ${\mathbf{G}}_m$.
:::

::: {.back card-id="card-19dda55760e13c46"}
Set $\mu_n = (k^{ {}^{ \operatorname{sep} } })^{\times}[n]$, then $H^1(k; \mu_n) = k^{\times}/(k^{\times})^n$, where these are $n$th powers.

Proof: LES for $\mu_n\hookrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times}\twoheadrightarrow(k^{ {}^{ \operatorname{sep} } })^{\times}$ and apply Hilbert 90.

If $K$ contains an $n$th root of unity, $\mu_n = C_n$ has trivial $G_K{\hbox{-}}$ action and $H^1(K; \mu_n) = \mathop{\mathrm{Hom}}(g_K, C_n)$.
:::

::: {.front card-id="card-53eab47f7ef628ba"}
What is the Pontryagin dual?
:::

::: {.back card-id="card-53eab47f7ef628ba"}
$G {}^{ \vee }\coloneqq{\mathsf{Top}}(G, {\operatorname{U}}_1)$ with the compact-open topology, for $G$ a locally compact abelian topological group.

Duality: profinite abelian groups $\rightleftharpoons$ discrete torsion abelian groups (

So limits of finite discrete groups vs colimits

Generalizes $G$ isomorphic to its character group
:::

::: {.front card-id="card-af6028d38b5cb858"}
What is $({\operatorname{U}}_1)_{\operatorname{tors}}$?
:::

::: {.back card-id="card-af6028d38b5cb858"}
${\mathbf{Q}}/{\mathbf{Z}}$, the group of all roots of unity.
:::

::: {.front card-id="card-a5d289a805257b70"}
How does one interpret $K^{\times}/(K^{\times})^n$.
:::

::: {.back card-id="card-a5d289a805257b70"}
$K^{\times}/(K^{\times})^n \cong g_K^{{\operatorname{ab}}, n}$ the Galois group of the maximal abelian extension of $K$ with exponent $n$.
:::

::: {.front card-id="card-3b96ac4266574cb6"}
What is the issue with Kummer theory?
:::

::: {.back card-id="card-3b96ac4266574cb6"}
In positive characteristic $p$, need $n$ prime to $p$ to consider $H^1(k; \mu_n)$.

Need
:::

::: {.front card-id="card-2d0a3d1a30e63ef3"}
What is Artin-Schreier theory?
:::

::: {.back card-id="card-2d0a3d1a30e63ef3"}
Characteristic $p$ analogue of Kummer theory.

Want an analogue for cyclic extensions of prime power order $p^k$, AS works for $k=1$.
:::

::: {.front card-id="card-9f8fd98a972d6eaf"}
How is Artin-Schreier theory expressed cohomologically?
:::

::: {.back card-id="card-9f8fd98a972d6eaf"}
Take $\phi \coloneqq\operatorname{Frob}- 1$ so $\phi(x) = x^p-x$, this is an isogeny of ${\mathbf{G}}_a$ so get a SES ${ \mathbf{F} }_p\hookrightarrow k^{ {}^{ \operatorname{sep} } } \xrightarrow[]{\phi} { \mathrel{\mkern-16mu}\rightarrow }\,  k^{ {}^{ \operatorname{sep} } }$.

Take LES, use additive Hilbert 90 to get $\mathop{\mathrm{Hom}}(g_k, { \mathbf{F} }_p) \cong k/\phi(k)$.

This says $(g_k^{{\operatorname{ab}}, p}) {}^{ \vee }= k/\phi(k)$.

Generalizes to $(g_k^{{\operatorname{ab}}, p^n}) = W_n(k)/ \phi(W_n(k))$ for $W_n$ the length $n$ Witt vectors.
:::

::: {.front card-id="card-c9837b1d36c43ff6"}
What is $W_n(k)$?
:::

::: {.back card-id="card-c9837b1d36c43ff6"}
As a scheme, ${\mathbf{G}}_a{ {}^{ \scriptscriptstyle\times^{n} }  }$, but what a twisted group law.
:::

::: {.front card-id="card-56812a42bf98ef46"}
What is the relative Brauer group?
:::

::: {.back card-id="card-56812a42bf98ef46"}
$\mathrm{Br}(L/K) \coloneqq H^2({ \mathsf{Gal}}(L/K); L^{\times})$.
:::

::: {.front card-id="card-8961c453a837af89"}
What is $\operatorname{cohdim}G$?
:::

::: {.back card-id="card-8961c453a837af89"}
$\sup_{p \in \operatorname{Spec}{\mathbf{Z}}} \operatorname{cohdim}_p G$ where $\operatorname{cohdim}_p G$ is the least $d$ such that for all $n\geq d$ and for all discrete torsion $A\in   {}_{G}{\mathsf{Mod}}$, one has $H^n(G; A[p^\infty]) = 0$.
:::

::: {.front card-id="card-3886538b2e514584"}
What is $\operatorname{cohdim}C_p$?
:::

::: {.back card-id="card-3886538b2e514584"}
$\operatorname{cohdim}_\ell C_p =0$ if $p\neq \ell$ and $\infty$ if $p=\ell$, so $\operatorname{cohdim}C_p = \infty$.
:::

::: {.front card-id="card-0bd0a971ed2aeda5"}
Discuss $\operatorname{cohdim}G$ for $G$ a pro${\hbox{-}}p$ group.
:::

::: {.back card-id="card-0bd0a971ed2aeda5"}
$\operatorname{cohdim}_p G \leq n \iff H^{n+1}(G; C_p) = 0$.
:::

::: {.front card-id="card-1f3689519ae590a6"}
Write $\mathsf{pro}{\mathbf{Z}}$ as a product.
:::

::: {.back card-id="card-1f3689519ae590a6"}
$$\mathsf{pro}{\mathbf{Z}}= \projectivelim C_n = \projectivelim \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} \projectivelim C_{p_i^{k_i}} = \prod_{p\in \operatorname{Spec}{\mathbf{Z}}} { {\mathbf{Z}}_{\widehat{p}} }$$
:::

::: {.front card-id="card-65cd3d53082ae059"}
What is ${\operatorname{Syl}}_p (\mathsf{pro}{\mathbf{Z}})$?
:::

::: {.back card-id="card-65cd3d53082ae059"}
Uniquely ${ {\mathbf{Z}}_{\widehat{p}} }$.
:::

::: {.front card-id="card-b06e08a3e7103026"}
What is $\operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} }$?
:::

::: {.back card-id="card-b06e08a3e7103026"}
$\operatorname{cohdim}{ {\mathbf{Z}}_{\widehat{p}} }= 1$.

Why: $H^2({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = 0$ and $H^1({ {\mathbf{Z}}_{\widehat{p}} }; C_p) = \mathop{\mathrm{Hom}}({ {\mathbf{Z}}_{\widehat{p}} }, C_p) = C_p$.
:::

::: {.front card-id="card-e3b30a624c45bf53"}
What is $\operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}})$?
:::

::: {.back card-id="card-e3b30a624c45bf53"}
$\operatorname{cohdim}(\mathsf{pro}{\mathbf{Z}}) = 1$ since $\operatorname{cohdim}_p({ {\mathbf{Z}}_{\widehat{p}} }) = 1$ for all primes $p$ and $\operatorname{cohdim}_p G = \operatorname{cohdim}_p G_p$ for $G_p$ a Sylow $p{\hbox{-}}$subgroup.
:::

::: {.front card-id="card-388130dd5c67f1b1"}
Compare $G_L$ and $G_K$ for $L/K$ an extension.
:::

::: {.back card-id="card-388130dd5c67f1b1"}
$G_L\hookrightarrow G_K$ as a closed subgroup.
:::

::: {.front card-id="card-9533eaca3452aa02"}
What is the inflation/restriction sequence for Brauer groups?
:::

::: {.back card-id="card-9533eaca3452aa02"}
$\mathrm{Br}(L/K)\xhookrightarrow{\mathrm{inflation}} \mathrm{Br}(K) \xrightarrow{\mathrm{restriction}} \mathrm{Br}(L)^{{ \mathsf{Gal}}(L/K)}$.
:::

::: {.front card-id="card-cc76cd508bd43e53"}
How do you interpret $\mathrm{Br}(L/K)$?
:::

::: {.back card-id="card-cc76cd508bd43e53"}
Elements of $\mathrm{Br}(K)$ that are annihilated by restriction to $\mathrm{Br}(L)$.
:::

::: {.front card-id="card-ae492cb6a89e0aa8"}
What is $H^2(K; \mu_n)$?
:::

::: {.back card-id="card-ae492cb6a89e0aa8"}
$H^2(K; \mu_n) = \mathrm{Br}(K)[n]$.
:::

::: {.front card-id="card-07975ce6c91081cd"}
What is an etale group scheme?
:::

::: {.back card-id="card-07975ce6c91081cd"}
Idea: for $G$, lose no information by considering $G(k^{ {}^{ \operatorname{sep} } })\in   {}_{G_k}{\mathsf{Mod}}$.
:::

::: {.front card-id="card-0fa66696121a93e0"}
What is $\mathrm{Br}({\mathbf{R}})$? Sketch a proof.
:::

::: {.back card-id="card-0fa66696121a93e0"}
Classified finite dimensional central simple division algebras.

$\mathrm{Br}({\mathbf{R}}) \cong C_2 \left\langle{{\mathbf{R}}, {\mathbb{H}}}\right\rangle$ where $\dim_{\mathbf{R}}{\mathbb{H}}= 4$ is the Hamilton quaternions.

Proof: $\mathrm{Br}({\mathbf{R}}) = \widehat{H}^0(\mathop{\mathrm{Aut}}({\mathbf{C}}/{\mathbf{R}}); {\mathbf{C}}^{\times}) = {\mathbf{R}}^{\times}/N{\mathbf{C}}^{\times}= {\mathbf{R}}^{\times}/{\mathbf{R}}_{\gt 0} = C_2$.
:::

::: {.front card-id="card-d7379378881c9532"}
Describe $\operatorname{Nm}: { \mathbf{F} }_{q^n} \to { \mathbf{F} }_q$.
:::

::: {.back card-id="card-d7379378881c9532"}
$\operatorname{Nm}(x) = x \cdot x^q \cdot x^{q^2}\cdots x^{q^{n-1}} = x^{[n]_q}$, the q-binomial $[n]_q \coloneqq{q^n-1\over q-1}$.
:::

::: {.front card-id="card-ed6fc5f2467c56da"}
What is $\mathrm{Br}({ \mathbf{F} }_q)$? What is the interpretation?
:::

::: {.back card-id="card-ed6fc5f2467c56da"}
$\mathrm{Br}({ \mathbf{F} }_q) = 0$; every finite division algebra is a field.

True because inflations are injective, ${ \mathsf{Gal}}({ \mathbf{F} }_{q^n}/{ \mathbf{F} }_q) = \left\langle{\operatorname{Frob}_q}\right\rangle$, and $\widehat{H}^0(\left\langle{\operatorname{Frob}_q}\right\rangle; { \mathbf{F} }_{q^n}^{\times}) = { \mathbf{F} }_q^{\times}/N{ \mathbf{F} }_{q^n}^{\times}= 0$ since the norm is surjective on finite fields.
:::

::: {.front card-id="card-ff081ebce96f915a"}
Characterize procyclic groups.
:::

::: {.back card-id="card-ff081ebce96f915a"}
Quotients of $\mathsf{pro}{\mathbf{Z}}$ by closed subgroups.
:::

::: {.front card-id="card-692232f75a34b981"}
What is a $C_1$ field?
:::

::: {.back card-id="card-692232f75a34b981"}
All homogeneous polynomials $f\in k[x_1,\cdots, x_n]$ of degree $d < n$ have a nonzero root in $k$.
:::

::: {.front card-id="card-68e86873bda3a8fc"}
What is the Chevalley-Warning theorem?
:::

::: {.back card-id="card-68e86873bda3a8fc"}
${ \mathbf{F} }_q$ is a $C_1$ field.
:::

::: {.front card-id="card-af37691e18301572"}
What is Tsen's theorem?
:::

::: {.back card-id="card-af37691e18301572"}
If $k ={ \overline{k} }$ and ${\mathrm{trdeg}}(L/k)=1$ then $L$ is a $C_1$ field.

In particular, $k(C)$ the function field of a curve over $k={ \overline{k} }$ is $C_1$.
:::

::: {.front card-id="card-6c6248f50912e197"}
What is Lang's theorem?
:::

::: {.back card-id="card-6c6248f50912e197"}
Is $K$ is a complete discretely valued field with algebraically closed residue field, then $K$ is a $C_1$ field.
:::

::: {.front card-id="card-7a6c44e233582a4d"}
What is $\mathrm{Br}(K)$ for $K$ a $C_1$ field?
:::

::: {.back card-id="card-7a6c44e233582a4d"}
$\mathrm{Br}(K) = 0$.
:::

::: {.front card-id="card-8e2cb08e735bc212"}
Discuss the decomposition of $\mathrm{Br}(K)$ for $K$ a CDVR with perfect residue field $k$.
:::

::: {.back card-id="card-8e2cb08e735bc212"}
$\mathrm{Br}(K) = \mathrm{Br}(k) \oplus \mathop{\mathrm{Hom}}(g_k, {\mathbf{Q}}/{\mathbf{Z}})$.

If $k$ is finite, $\mathrm{Br}(K) = {\mathbf{Q}}/{\mathbf{Z}}$.
:::

::: {.front card-id="card-766c454787487177"}
Discuss limits of $C_n$.
:::

::: {.back card-id="card-766c454787487177"}
$\colim C_n = {\mathbf{Q}}/{\mathbf{Z}}$

$\projectivelim C_n = \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-10d1272606dd6f30"}
What is the characteristic property of unramified extensions?
:::

::: {.back card-id="card-10d1272606dd6f30"}
For $L/K$ with residue fields $l/k$, ${ \mathsf{Gal}}(L/K)\twoheadrightarrow{ \mathsf{Gal}}(l/k)$ is an isomorphism.
:::

::: {.front card-id="card-8fd920f18e320d3c"}
For a decreasing filtration $M_1 \supseteq M_2\supseteq\cdots$, what does it mean for $M_1$ to be complete and separated for the $M_i{\hbox{-}}$adic topology?
:::

::: {.back card-id="card-8fd920f18e320d3c"}
$M_1\to \projectivelim M_1/M_n$ is an isomorphism, realizing $M_1$ as an adic completion wrt the quotients.
:::

::: {.front card-id="card-ecbf81a3501e47c7"}
What is a residual extension?
:::

::: {.back card-id="card-ecbf81a3501e47c7"}
For $L/K$ with residue fields $l$ and $k$ respectively, the extension of residue fields $l/k$.
:::

::: {.front card-id="card-9b48c86ec18ac71d"}
What are the higher unit groups of a local field $L$?
:::

::: {.back card-id="card-9b48c86ec18ac71d"}
$U^n(L) \coloneqq\left\{{x\in R(L) {~\mathrel{\Big\vert}~}v(x-1)\geq n}\right\}$ for $n\geq 1$, where $R(L)$ is the valuation ring with maximal ideal ${\mathfrak{m}}$.

Can write as $1 + {\mathfrak{m}}^n$: for $r_n: R\twoheadrightarrow R/{\mathfrak{m}}^n$, the induced map $r_n^{\times}: R^{\times}\to (R/{\mathfrak{m}}^n)^{\times}$ is surjective since $R$ is local, and $U^n = \ker r_n^{\times}= 1 + {\mathfrak{m}}^n$, the units that are trivial modulo ${\mathfrak{m}}^n$.

In characteristic zero, the $p{\hbox{-}}$adic logarithm gives an isomorphism $U^n { \, \xrightarrow{\sim}\, }{\mathfrak{m}}^n$ for $n > e/(p-1)$, where $e \coloneqq v(p)$.
:::

::: {.front card-id="card-fce84017162b3b45"}
What is the profinite index of $H\leq G$ a closed subgroup of a profinite group
:::

::: {.back card-id="card-fce84017162b3b45"}
$[G: H] = \operatorname{lcm}_{U\supseteq H \text{ open}} [G:U]$.
:::

::: {.front card-id="card-62ca6a4845ff33f7"}
What is the virtual cohomology dimension?
:::

::: {.back card-id="card-62ca6a4845ff33f7"}
$\mathrm{vcohdim}_p(G) \coloneqq\inf_{U \leq G \text{ open}}\operatorname{cohdim}_p(U)$, and $\mathrm{vcohdim}(G) \coloneqq\sup_p \mathrm{vcohdim}_p(G)$.
:::

::: {.front card-id="card-04eb0883ac6aed5c"}
What explains $\mathrm{vcohdim}_p G < \infty$ but $\operatorname{cohdim}_p G = \infty$?
:::

::: {.back card-id="card-04eb0883ac6aed5c"}
The presence of elements of finite order $p$.

Theorem of Serre: if $G$ is profinite with no elements of order $p$, for all $U\leq G$ open, $\operatorname{cohdim}_p U = \operatorname{cohdim}_p G$.
:::

::: {.front card-id="card-4618648279592873"}
What is a virtually torsionfree group?
:::

::: {.back card-id="card-4618648279592873"}
$\exists U\leq G$ open (thus finite index) which is torsionfree.
:::

::: {.front card-id="card-ace67f214e73cf15"}
What does "virtually" having a property $P$ mean?
:::

::: {.back card-id="card-ace67f214e73cf15"}
Admitting some finite index subgroup which has property $P$.
:::

::: {.front card-id="card-5f4e3322c228111a"}
When is $M\in {\mathsf{Fin}} {}_{{\mathbf{Z}}}{\mathsf{Mod}}$ a product of its Sylow subgroups?
:::

::: {.back card-id="card-5f4e3322c228111a"}
Iff nilpotent.
:::

::: {.front card-id="card-58c10e687053fd85"}
What is the structure theory of $\mathsf{pro}{\mathsf{Ab}}{\mathsf{Grp}}^{{\mathsf{Top}}{\hbox{-}}{\mathrm{fg}}}$?
:::

::: {.back card-id="card-58c10e687053fd85"}
$G = \prod G_p$ is a product of Sylow $p{\hbox{-}}$subgroups.

If $G$ is pro${\hbox{-}}p$, then $G\cong { {\mathbf{Z}}_{\widehat{p}} }{ {}^{ \scriptscriptstyle\oplus^{\mathrm{v}\operatorname{cohdim}(G)} }  } \oplus G_{\operatorname{tors}}$ where ${\sharp}G_{{\operatorname{tors}}} < \infty$.
:::

::: {.front card-id="card-eb8e491195492d06"}
Define a local field.
:::

::: {.back card-id="card-eb8e491195492d06"}
Complete DVR, a field, with finite residue field.
:::

::: {.front card-id="card-aa139882c510b936"}
Give equivalent conditions for a field $K$ to be a DVF
:::

::: {.back card-id="card-aa139882c510b936"}
$K$ is locally compact.

The valuation ring $R(K)$ is compact.

${\mathbf{G}}_a(R(K))$ is a profinite group (since compact and totally disconnected).

$K$ is complete and the residue field $\kappa(K) \coloneqq R(K)/{\mathfrak{m}}$ is a finite field.
:::

::: {.front card-id="card-1109d37fbb1e4a7b"}
Discuss characteristic zero local fields $K$.
:::

::: {.back card-id="card-1109d37fbb1e4a7b"}
$K \in   {}_{{ {\mathbf{Q}}_p }}{\mathsf{Mod}}^{\mathrm{fd}}$ canonically

${\mathbf{Q}}\hookrightarrow K$ with ${ \operatorname{cl}}^{\mathsf{Top}}_K({\mathbf{Q}}) ={ {\mathbf{Q}}_p }$ and $[K: { {\mathbf{Q}}_p }] = e\cdot f$ where...

$\kappa = { \mathbf{F} }_{p^f}$ is the residual degree

$e = e(K/{ {\mathbf{Q}}_p }) = v(p)$ where $p\coloneqq\operatorname{ch}\kappa$.
:::

::: {.front card-id="card-aa39b93824571d7c"}
Give an example of a totally ramified extension.
:::

::: {.back card-id="card-aa39b93824571d7c"}
${ \mathbf{F} }_q(\hspace{-0.25em}( t^{1\over n} )\hspace{-0.22em})$ over ${ \mathbf{F} }_q(\hspace{-0.25em}( t )\hspace{-0.22em})$.
:::

::: {.front card-id="card-8bb26ae43d3b8576"}
Discuss the Galois theory of ${ \mathsf{Gal}}(k^{ {}^{ \operatorname{sep} } }/k)$ for $k$ local of positive characteristic $p$.
:::

::: {.back card-id="card-8bb26ae43d3b8576"}
$k^{\scriptscriptstyle\mathrm{un}}/k$ has ramification index 1, so unramified extensions correspond to extensions of the residue field, and so ${ \mathsf{Gal}}(k^{\scriptscriptstyle\mathrm{un}}/k) \cong { \mathsf{Gal}}(\overline{{ \mathbf{F} }}_q/{ \mathbf{F} }_q) \cong \mathsf{pro}{\mathbf{Z}}$.

$k^{\mathrm{tame}}$ has ramification indices all prime to $p$, $k^{\mathrm{tame}}/k^{\scriptscriptstyle\mathrm{un}}$ corresponds to taking $\pi^{1\over n}$.

$I \coloneqq\mathop{\mathrm{Aut}}(k^{ {}^{ \operatorname{sep} } }/k^{\scriptscriptstyle\mathrm{un}}) = \ker(g_k \twoheadrightarrow g_{{ \mathbf{F} }_q})$ is the inertia group

$I_p$ is the wild ramification, the Sylow $p{\hbox{-}}$subgroup of $I$.
:::

::: {.front card-id="card-1f124014b7ebda6c"}
What does local class field theory say about the maximal abelian extension of a local field $K$?
:::

::: {.back card-id="card-1f124014b7ebda6c"}
The reciprocity map $\omega: {\mathbf{G}}_m(K) \to G_K^{\operatorname{ab}}$ becomes an isomorphism after passing to the profinite completion:
$$\widehat{\omega}: \mathsf{pro}K^{\times} { \, \xrightarrow{\sim}\, }g_K^{\operatorname{ab}} = { \mathsf{Gal}}(K^{\operatorname{ab}}/K)$$
So ${ \mathsf{Gal}}(K^{\operatorname{ab}}/K) \cong \mathsf{pro}{\mathbf{G}}_m(K) \cong \mathsf{pro}{\mathbf{Z}}\times U(K)$, and the unit group gives most of the information.

$\omega$ restricts to $U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}}= { \mathsf{Gal}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}})$, so we understand the totally ramified piece of $K^{\operatorname{ab}}/K$.
:::

::: {.front card-id="card-54368a00e14742d7"}
For $G = \mathop{\mathrm{Aut}}(L/K)\in{\mathsf{Fin}}{\mathsf{Grp}}$ cyclic, what is $K^{\times}/N L^{\times}$?
:::

::: {.back card-id="card-54368a00e14742d7"}
${\sharp}K^{\times}/N L^{\times}= [L: K]$.
:::

::: {.front card-id="card-66baf534cd2f7009"}
What is ${ \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K)$?
:::

::: {.back card-id="card-66baf534cd2f7009"}
${ \mathsf{Gal}}(K^{\scriptscriptstyle\mathrm{un}}/K)\cong { \mathsf{Gal}}(\overline{\kappa}/\kappa) = \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-14239b3b335fdb91"}
What is the unit group SES?
:::

::: {.back card-id="card-14239b3b335fdb91"}
$U\hookrightarrow K^{\times} \xrightarrow[]{v} { \mathrel{\mkern-16mu}\rightarrow }\,  {\mathbf{Z}}$.
:::

::: {.front card-id="card-3db412aa9ca534fb"}
What is the invariant map?
:::

::: {.back card-id="card-3db412aa9ca534fb"}
$\mathrm{inv}_K: \mathrm{Br}(K)  { \, \xrightarrow{\sim}\, }{\mathbf{Q}}/{\mathbf{Z}}$ for $K$ a local field.
:::

::: {.front card-id="card-63d9dec15c450fea"}
For $L/K$, what is the induced restriction map on Brauer groups? Corestriction?
:::

::: {.back card-id="card-63d9dec15c450fea"}
$\mathrm{Res}^{K}_{L}: \mathrm{Br}(K) \to \mathrm{Br}(L)$ is $\cdot n: {\mathbf{Q}}/{\mathbf{Z}}\to {\mathbf{Q}}/{\mathbf{Z}}$ where $n \coloneqq[L: K]$.

Corestriction is the identity.
:::

::: {.front card-id="card-523977123bb2324a"}
What is $\mathrm{Br}(L/K)$ for $L/K$ a finite extension?
:::

::: {.back card-id="card-523977123bb2324a"}
For $K$ a local field, $\mathrm{Br}(L/K) = \mathrm{Br}(K)[n]$ for $n\coloneqq[L: K]$, since restriction $\mathrm{Br}(K)\to \mathrm{Br}(L)$ is multiplication by $n$ on ${\mathbf{Q}}/{\mathbf{Z}}$.
:::

::: {.front card-id="card-153e8ee23c511946"}
What is the fundamental class? What is its significance?
:::

::: {.back card-id="card-153e8ee23c511946"}
$v_{L/K}\in \mathrm{Br}(L/K) = H^2(G_{L/K}; {\mathbf{G}}_m(L))$ the unique class where
$$\mathrm{inv}_K(v_{L/K}) = {1\over n} + {\mathbf{Z}}\in \qty{{1\over n} {\mathbf{Z}}}/{\mathbf{Z}}\subseteq {\mathbf{Q}}/{\mathbf{Z}}$$
Apply Tate-Nakayama to get
$$G^{\operatorname{ab}}= \widehat{H}^{-2}(G; {\mathbf{Z}}) \underset{{-}\smile v_{L/K}}{ { \, \xrightarrow{\sim}\, }} \widehat{H}^0(G; {\mathbf{G}}_m(L)) =K^{\times}/N L^{\times}$$
Yields $\omega_{L/K}: K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G^{\operatorname{ab}}$, so e.g. the norm map is surjective iff $G = G^{\operatorname{ab}}$ is abelian.

Alternatively, for abelian extensions, ${ \mathsf{Gal}}(L/K)  { \, \xrightarrow{\sim}\, }\operatorname{coker}N$.
:::

::: {.front card-id="card-6153b701f329a586"}
Discuss the significance of $\omega$.
:::

::: {.back card-id="card-6153b701f329a586"}
Isomorphisms of $\omega_{L/K}$ assemble into a compatible inverse system.

Yields $\omega: K^{\times}\to\projectivelim_{L/K \text{ fin. ab}}K^{\times}/NL^{\times} { \, \xrightarrow{\sim}\, }G_K^{\operatorname{ab}}$, so is this injective? Is it the profinite completion of $K^{\times}$?

Equivalently, are there enough finite abelian extensions to be cofinal in the system of all finite index subgroups of $K^{\times}$?

$\omega(K^{\times}) \subseteq G_K^{\operatorname{ab}}$ is dense.
:::

::: {.front card-id="card-d2c81ce19310d677"}
What is $I_K^{\operatorname{ab}}$?
:::

::: {.back card-id="card-d2c81ce19310d677"}
$I_K^{\operatorname{ab}}= \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K^{\scriptscriptstyle\mathrm{un}})\subseteq \mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K)$.
:::

::: {.front card-id="card-5f3ac63317a6e4d6"}
What is a projective profinite group?
:::

::: {.back card-id="card-5f3ac63317a6e4d6"}
$P$ is projective iff $\forall \pi: G\twoheadrightarrow P$ there is a section $\pi\circ s = \operatorname{id}_P$.

$\iff \operatorname{cohdim}P \leq 1$.

$\iff G_p$ is a free pro $p{\hbox{-}}$group.
:::

::: {.front card-id="card-79a859109812a9d2"}
Describe $\mathsf{pro}K^{\times}$.
:::

::: {.back card-id="card-79a859109812a9d2"}
$K^{\times}= U_K \times {\mathbf{Z}}$ since everything is a unit times a uniformizer, so

$\mathsf{pro}K^{\times}= U_K \times \mathsf{pro}{\mathbf{Z}}$.
:::

::: {.front card-id="card-365de60e896eb42f"}
What is the reciprocity map?
:::

::: {.back card-id="card-365de60e896eb42f"}
$\omega:\mathsf{pro}(K^{\times})\to G_K^{\operatorname{ab}}$; restricts to $U_K { \, \xrightarrow{\sim}\, }I_K^{\operatorname{ab}}$.
:::

::: {.front card-id="card-d0d01d2c0a99e93f"}
What is $N L^{\times}$ for $L/K$ unramified?
:::

::: {.back card-id="card-d0d01d2c0a99e93f"}
$U_K \subseteq NL^{\times}= \left\{{x\in K^{\times}{~\mathrel{\Big\vert}~}n\mathrel{\Big|}v(x)}\right\}$.
:::

::: {.front card-id="card-e565bc3ee54ccd7a"}
What is a proper map of profinite groups?
:::

::: {.back card-id="card-e565bc3ee54ccd7a"}
$f:X\to Y$ where $f\times \operatorname{id}_Z: X\times Z\to Y\times Z$ is closed for every $Z$.

$\iff f$ is closed with quasicompact fibers.

For $X$ Hausdorff and $Y$ locally compact, $\iff$ preimage of compact is compact.
:::

::: {.front card-id="card-16426ec4249da425"}
What is the Galois correspondence induced by the reciprocity map?
:::

::: {.back card-id="card-16426ec4249da425"}
Subextensions of $L/K$ $\rightleftharpoons$ open subgroups of $K^{\times}$ containing $NL^{\times}$ where $\omega^{-1}(M) \coloneqq N M^{\times}$ for such a subgroup $M$.
:::

::: {.front card-id="card-8ee9b56e0afe4adb"}
Interpret $\mathop{\mathrm{Hom}}(G, C_n)$.
:::

::: {.back card-id="card-8ee9b56e0afe4adb"}
The character group $\chi(\tilde G)$ where $\tilde G = G^{\operatorname{ab}}/(G^{\operatorname{ab}})^n$ is the maximal abelian quotient of exponent $n$.
:::

::: {.front card-id="card-94b46fb9af7d6bf3"}
What is the norm residue symbol / Hilbert symbol?
:::

::: {.back card-id="card-94b46fb9af7d6bf3"}
$(a, b)_n \coloneqq b \smile\delta(\chi_a)\in H^2(K; {\mathbf{G}}_m) = \mathrm{Br}(K)$ for $a,b\in K^{\times}$.

Here $\delta: K^{\times}/(K^{\times})^n  { \, \xrightarrow{\sim}\, }H^1(K; \mu_n)$ is the coboundary, which is an isomorphism by Kummer theory.

Yields a perfect pairing $({-}, {-})_n: (K^{\times}/ (K^{\times})^n){ {}^{ \scriptstyle\otimes_{}^{2} }  } \to {\mathbf{Q}}/{\mathbf{Z}}$.
:::

::: {.front card-id="card-0989d534d9332209"}
What is the Steinberg relation?
:::

::: {.back card-id="card-0989d534d9332209"}
$(a, 1-a)_n = 0$.
:::

::: {.front card-id="card-e5a0051674920341"}
What is the existence theorem for $p{\hbox{-}}$adic fields?
:::

::: {.back card-id="card-e5a0051674920341"}
If $U\leq K^{\times}$ is finite index then $\exists ! L$ a subextension of $\overline{K}/K$ such that $U = \operatorname{Nm}_{L/K} L^{\times}$.
:::

::: {.front card-id="card-dce455f2aa934948"}
Discuss Lubin-Tate theory.
:::

::: {.back card-id="card-dce455f2aa934948"}
A generalization of complex multiplication to local fields.

Constructs $K^{\operatorname{ab}}= K^{\scriptscriptstyle\mathrm{un}}(\cdots)$ where one adjoins torsion points of FGLs.
:::

::: {.front card-id="card-4502c07a8c557b29"}
What is CFT?
:::

::: {.back card-id="card-4502c07a8c557b29"}
Given a field $K$, find a topological group $G$ and an isomorphism $\mathsf{pro}G\to G_K^{\operatorname{ab}}$.
:::

::: {.front card-id="card-2594d9e0a9390842"}
What is explicit class field theory?
:::

::: {.back card-id="card-2594d9e0a9390842"}
Since $K^{\operatorname{ab}}/K$ is a countably infinite degree algebraic extension, produce a sequence of algebraic numbers $a_n$ such that $K^{\operatorname{ab}}= \colim(K[a_1]\hookrightarrow K[a_1, a_2]\hookrightarrow\cdots)$.
:::

::: {.front card-id="card-ee8cd8706a6bd8a0"}
State Kronecker-Weber.
:::

::: {.back card-id="card-ee8cd8706a6bd8a0"}
${\mathbf{Q}}^{\operatorname{ab}}= {\mathbf{Q}}(\zeta_n {~\mathrel{\Big\vert}~}n\in {\mathbf{Z}}_{\geq 0})$.
:::

::: {.front card-id="card-259f06e97092cb5e"}
What is the mod $n$ cyclotomic character?
:::

::: {.back card-id="card-259f06e97092cb5e"}
$\chi_n: G_K\to C_n^{\times}$ induced by $G_K\curvearrowright K(\zeta_n)$, take inverse limit to obtain $\chi: G_K \to (\mathsf{pro}{\mathbf{Z}})^{\times}$.

The kernel always yields an abelian extension of $K$, the maximal cyclotomic extension (obtained by adjoining all roots of unity)
:::

::: {.front card-id="card-f6cdbc638824fec6"}
Discuss explicit CFT for imaginary quadratics.
:::

::: {.back card-id="card-f6cdbc638824fec6"}
For $E/k$ with ${\mathcal{O}}_K{\hbox{-}}$CM, get $\rho_N: G_K \to \mathop{\mathrm{Aut}}E[N] \cong \operatorname{GL}_1(C_N)$.

Completes to $\rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathbf{Z}})$.

Check $E[N]$ is a rank 2 $C_N$ module but a rank 1 ${\mathcal{O}}_K/N$ module.

Get $\rho_N: G_K \to \operatorname{GL}_1({\mathcal{O}}_K/N)$ which completes to $\rho: G_K \to \operatorname{GL}_1(\mathsf{pro}{\mathcal{O}}_K)$.

Take $\psi: G_K \to \mathsf{pro}{\mathcal{O}}_K^{\times}\to \mathsf{pro}{\mathcal{O}}_K^{\times}/{\mathcal{O}}_K^{\times}$ to get $K^{\ker \psi} = K^{\operatorname{ab}}$.

So for $K$, write down $E/K$ with CM by ${\mathcal{O}}_K$ and get $K^{\operatorname{ab}}= K(x(p) {~\mathrel{\Big\vert}~}p\in E[{\operatorname{tors}}])$, the $x{\hbox{-}}$coordinates of torsion points.
:::

::: {.front card-id="card-8c5d2b136e0764af"}
For $R$ the valuation ring of $K$, $U$ doesn't give $K^{\operatorname{ab}}$. Why? What does?
:::

::: {.back card-id="card-8c5d2b136e0764af"}
$\mathop{\mathrm{Aut}}(K^{\operatorname{ab}}/K) = U \times\mathsf{pro}{\mathbf{Z}}$, so $U$ only gives the totally ramified part.
:::

::: {.front card-id="card-30d9359488c1df16"}
What does $f = g + { \mathsf{O}}(k)$ mean?
:::

::: {.back card-id="card-30d9359488c1df16"}
$f\equiv g \in k{[\![  x_1,\cdots, x_n ]\!]  }/\left\langle{x_1,\cdots,x_n}\right\rangle^k$, so equal up to terms of order $k$.
:::

::: {.front card-id="card-f33d6daf6119c6ba"}
When can power series be substituted into each other?
:::

::: {.back card-id="card-f33d6daf6119c6ba"}
When the constant term is zero, e.g. $e^{e^x}$ has infinitely many constant terms.
:::

::: {.front card-id="card-9c31c990452572db"}
What is a formal group law?
:::

::: {.back card-id="card-9c31c990452572db"}
Associativity: $F(F(x,y), z) = F(x, F(y,z))$

Identities: $F(x, 0) = x$ and $F(0, y) = y$.

Inverses: $\exists !\iota \in R{[\![  t ]\!]  }$ such that $F(x, \iota(x)) = 0$.
:::

::: {.front card-id="card-6ab20a703009190d"}
How does one get an honest group from a FGL?
:::

::: {.back card-id="card-6ab20a703009190d"}
Take $(R, {\mathfrak{m}})$ complete local, then $R { \, \xrightarrow{\sim}\, }\projectivelim_n R/{\mathfrak{m}}^n$ so $x+y \coloneqq F(x,y)$ converges in the ${\mathfrak{m}}{\hbox{-}}$adic topology.
:::

::: {.front card-id="card-37578c7420249421"}
What is the multiplicative formal group?
:::

::: {.back card-id="card-37578c7420249421"}
$F(x,y) = x + y + xy = (x+1)(y+1) - 1$.
:::

::: {.front card-id="card-054429efc3a37b22"}
What is a formal $R{\hbox{-}}$module?
:::

::: {.back card-id="card-054429efc3a37b22"}
A ring morphism $R\to { \operatorname{End} }_{\FGL}(F)$ for $F$ a formal group.
:::

::: {.front card-id="card-ad2d11d11ca5cd23"}
What is $[n](T)$ for ${\mathbf{G}}_a$ and ${\mathbf{G}}_m$, where $[n] \in { \operatorname{End} }_{\FGL}(F)$ is $1 \oplus_F 1\oplus_F \cdots \oplus_F 1$?
:::

::: {.back card-id="card-ad2d11d11ca5cd23"}
$[n](T) =nT$ for ${\mathbf{G}}_a$.

$[n](T) = (T+1)^n - 1$ for ${\mathbf{G}}_m$.
:::

::: {.front card-id="card-e9e25b1747d58f6c"}
What is $\operatorname{ht}{\mathbf{G}}_m$ in characteristic zero?
:::

::: {.back card-id="card-e9e25b1747d58f6c"}
Height 1
:::

::: {.front card-id="card-904751811797f1ac"}
What is $\operatorname{ht}{\mathbf{G}}_a$ in characteristic $p$?
:::

::: {.back card-id="card-904751811797f1ac"}
Height $\infty$.
:::

::: {.front card-id="card-530f8b7d350ac21b"}
What are the torsion points on ${\mathbf{G}}_m$?
:::

::: {.back card-id="card-530f8b7d350ac21b"}
Roots of unity.
:::

::: {.front card-id="card-5496190b1d9e0cc4"}
What is $F_\pi$? Give an example of $f\in F_\pi$.
:::

::: {.back card-id="card-5496190b1d9e0cc4"}
$F_\pi \coloneqq\left\{{ f\in R{[\![  T ]\!]  } {~\mathrel{\Big\vert}~}f(T) = \pi T + { \mathsf{O}}(T^2) ,\,\, f\equiv T^q \operatorname{mod}\pi}\right\}$.

For $K = { {\mathbf{Q}}_p }$, take $f(T) = (1+T)^p - 1 = T^p + {p\choose p-1}T^{p-1} + \cdots + pT$, so $f = [p]$ on ${\mathbf{G}}_m$.
:::

::: {.front card-id="card-1b6f81d13cff9302"}
What are the key properties of $F_\pi$?
:::

::: {.back card-id="card-1b6f81d13cff9302"}
For $f,g\in F_\pi$ and $\phi_1 \in R{[\![  x_1,\cdots, x_n ]\!]  }$, $\exists ! \phi \in R{[\![  x_1,\cdots, x_n ]\!]  }$ st $\phi = \phi_1 + { \mathsf{O}}(x^2)$ and $f\circ \phi = \phi \circ \Delta_g$, i.e.$f(\phi(x_1,\cdots, x_n)) = \phi(g(x_1), \cdots, g(x_n))$.
:::

::: {.front card-id="card-9065d30f1cc7ba3c"}
What is the Lubin-Tate FGL attached to $f\in F_\pi$?
:::

::: {.back card-id="card-9065d30f1cc7ba3c"}
The unique FGL $F_f\in R{[\![  x,y ]\!]  }$ st $f\in { \operatorname{End} }_{\FGL} F_f$ canonically, so $f(F_f(x,y)) = F_f(f(x), f(y))$.
:::

::: {.front card-id="card-f8c7dd23d0446e5a"}
What do we know about field extensions generated by Eisenstein polynomials?
:::

::: {.back card-id="card-f8c7dd23d0446e5a"}
- Totally ramified.
:::

::: {.front card-id="card-e94fbcf6815d8767"}
How are an unramified and a totally ramified extension related?
:::

::: {.back card-id="card-e94fbcf6815d8767"}
- Disjoint
:::

::: {.front card-id="card-9c6ca18eb9036a9f"}
How is $\overline{{ \mathbf{F} }_{q}}$ obtained from ${{ \mathbf{F} }_{q}}$?
:::

::: {.back card-id="card-9c6ca18eb9036a9f"}
- Adjoin all roots of unity.
:::
