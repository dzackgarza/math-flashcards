---
title: "Number Theory::Algebraic Number Theory"
---

::: {.front card-id="card-b54646603b961630" tags="definition"}
Definition: Ideal Class Group of an algebraic number field $K$
:::

::: {.back card-id="card-b54646603b961630"}
The group of fractional ideals of the ring of integers of $K$ mod the subgroup of principal ideals.
Trivial iff all ideals are principal.
:::

::: {.front card-id="card-0c9125c6959114e2" tags="definition"}
Definition: Global Field
:::

::: {.back card-id="card-0c9125c6959114e2"}
A global field is either a finite extension of $\mathbb{Q}$ or a finite extension of $\mathbb{F}_q(t)$ for some finite field $\mathbb{F}_q$.
:::

::: {.front card-id="card-f49d31897f3519a4"}
Define a DVR
:::

::: {.back card-id="card-f49d31897f3519a4"}
A PID with a unique nonzero prime, and thus a uniformizer: any $\pi$ with $v(\pi) = 1$.
:::

::: {.front card-id="card-8827e1fd9b908673"}
Give an example of a local ring which is not a DVR.
:::

::: {.back card-id="card-8827e1fd9b908673"}
$R = k\fps{x^2, x^3}$ is local with $\mfm_R = \left\langle{x^2, x^3}\right\rangle$, so not a PID.
:::

::: {.front card-id="card-bb3f3bb4b22f2656"}
What is the valuation ring of a DVF $K$?
:::

::: {.back card-id="card-bb3f3bb4b22f2656"}
$R = R(K) = \left\{{x\in K \st v(x) \geq 0}\right\} = v^{-1}([0, \infty])$

Has unique maximal ideal $\mfm_R = \left\{{x\in K \st v(x) > 0}\right\} = \left\langle{\pi}\right\rangle$ for $\pi$ a uniformizer with $v(\pi) = 1$.

Always a DVR, in particular a PID, and $\operatorname{Spec}R = \left\{{0, \mfm_R}\right\}$.
:::

::: {.front card-id="card-08ec6e5ee4856726"}
Define a Dedekind domain.
:::

::: {.back card-id="card-08ec6e5ee4856726"}
Noetherian, integral, integrally closed, with $\operatorname{Spec}R = \operatorname{mSpec}R$.

Implies every localization is a DVR.
:::

::: {.front card-id="card-0f2a03765a311122"}
Why are complete DVRs $K$ with valuation ring $A$ great?
:::

::: {.back card-id="card-0f2a03765a311122"}
Every $x\in \operatorname{ff}(A)$ is of the form $\sum_{n\geq n_0} s_n \pi^n$ with $s_n\in S\subset A$ a set of representatives of $A/\mfm$.

Compare to $x = \sum a_n p^n$ with $0\leq a_n\leq p-1$ for ${ \ZZ_{\widehat{p}} }$.

If $[L: \operatorname{ff}(A)] = n$ then $B \coloneqq \operatorname{cl}^{\mathrm{int}}_L(A)$ is a DVR and $B \in   {}_{A}\Mod^{\free, \operatorname{rank}=n}$ and complete wrt the topology induced by $B$.
:::

::: {.front card-id="card-151ffc95e91ee105"}
Define ${\left\lvert {a\over b} \right\rvert}_p$.
:::

::: {.back card-id="card-151ffc95e91ee105"}
$\qty{1\over p}^{v_p(a/b)}$.
:::

::: {.front card-id="card-44373c857d915532"}
What is the ultrametric triangle inequality?
:::

::: {.back card-id="card-44373c857d915532"}
${\left\lvert {x+y} \right\rvert}_p \leq \max\left\{{{\left\lvert {x} \right\rvert}_p, {\left\lvert {y} \right\rvert}_p}\right\}\leq {\left\lvert {x} \right\rvert}_p + {\left\lvert {y} \right\rvert}_p$.

$v_p(x+y) \geq \min\left\{{v_p(x), v_p(y)}\right\}$.
:::

::: {.front card-id="card-9747412906f697be"}
Describe ${ \ZZ_{\widehat{p}} }$ in terms of valuations.
:::

::: {.back card-id="card-9747412906f697be"}
$\left\{{x\in \QQ\st v_p(x) \geq 0}\right\}$ or $\left\{{x\in \QQ\st{\left\lvert {x} \right\rvert}_p \leq 1}\right\}$.

Explicitly ${ \ZZ_{\widehat{p}} }\coloneqq\left\{{{a\over b} \in \QQ\st p\nmid b}\right\} = \ZZ { \left[ \scriptstyle {{1\over \ell} \st\ell \neq p} \right] }$.
:::

::: {.front card-id="card-68553d646b8bf636"}
Discuss ring-theoretic properties of ${ \ZZ_{\widehat{p}} }$.
:::

::: {.back card-id="card-68553d646b8bf636"}
Has maximal ideal $\left\langle{p}\right\rangle = \left\{{{a\over b} \st p\nmid a}\right\}$

Every element in ${ \ZZ_{\widehat{p}} }\setminus\left\langle{p}\right\rangle$ is a unit, so this is a local ring with residue field ${ \mathbf{F} }_p$.

Take completion to get ${ \ZZ_{\widehat{p}} }$.
:::

::: {.front card-id="card-748d1c56cf6a74c5"}
Explicitly describe elements in ${ \ZZ_{\widehat{p}} }$.
:::

::: {.back card-id="card-748d1c56cf6a74c5"}
${ \ZZ_{\widehat{p}} }= \left\{{\sum a_i p^i \st0 \leq a_i \leq p-1}\right\}$

Equivalently ${ \ZZ_{\widehat{p}} }= \projectivelim_n \ZZ/\left\langle{p^n}\right\rangle$ which contains sequences $\mathbf{a} = {\left[ {a_0, a_0 + a_1 p, a_0 + a_1 p + a_2 p^2, \cdots} \right]}$ of partial sums so that $\mathbf{a}_n \operatorname{mod}p^n \cong \mathbf{a}_{n-1}$.
:::

::: {.front card-id="card-4fe3dcc31ba40502"}
For a DVR $A$, setting ${\left\lvert {{-}} \right\rvert}_v \coloneqq a^{v_p({-})}$, why should one choose $a \coloneqq 1/q$ for $q \coloneqq{\sharp}A/p$?
:::

::: {.back card-id="card-4fe3dcc31ba40502"}
For the Haar measure, satisfies $\mu(xT) = {\left\lvert {x} \right\rvert} \mu(T)$.
:::

::: {.front card-id="card-7946ed914bd0b978"}
Interpret local fields geometrically.
:::

::: {.back card-id="card-7946ed914bd0b978"}
For $X$ a variety with coordinate ring $R$, points $p\in X$ correspond to $p\in \operatorname{Spec}R$ and localizing $L_p R$ yields the ring of functions with no pole at $p$.

E.g. $L_3 \ZZ$ allows fractions with no 3 in the denominator.
:::

::: {.front card-id="card-4adb1bcf42e5b94c"}
Discuss the AKLB setup when $L/K$ is finite and $B = \operatorname{cl}^{\mathrm{int}}_L(A)$ is a DVR.
:::

::: {.back card-id="card-4adb1bcf42e5b94c"}
The extension satisfies $\mfm_A B = \mfm_B^e$ with $[\kappa_B : \kappa_A] = f$ and $n \coloneqq[L: K] = ef$. Two extreme cases:

If $e=1, f=n$ (so no ramification) and $\kappa_B = \kappa_A(\overline{\alpha})$ is simple (e.g. if the residue field extension is separable) then $B$ is monogenic: $B\cong A[x]/\left\langle{f}\right\rangle$ where $f$ is the minimal polynomial over $K$ of a lift of $\overline{\alpha}$ to $B$.

If $e=n, f=1$ then $B = A[x]/\left\langle{f}\right\rangle$ where $f$ is the minimal polynomial of $\pi_B$

Useful: rings of integers of extensions become much easier to express! Ramification and splitting is simpler because of the single prime.
:::

::: {.front card-id="card-f344e33aa0fd216b"}
What is the decomposition group?
:::

::: {.back card-id="card-f344e33aa0fd216b"}
For $L/K$ Galois and $p\in \operatorname{Spec}A$, write $pB = \prod_{i\leq g} q_i^e$ where $q_i\in \operatorname{Spec}B$, all $e$ the same since Galois, and $f \coloneqq[B/b_i : A/p]$. Then $D_{q_i}\coloneqq\Stab_{\Gal(L/K)}(q_i)$, elements of Galois fixing $q_i$.

All $D_{q_i}$ are conjugate in $\Gal(L/K)$ and thus the corresponding fields $K_{D_{q_i}}$ are isomorphic.

Not necessarily normal.
:::

::: {.front card-id="card-e6b7cd7509584028"}
Why is the decomposition group useful?
:::

::: {.back card-id="card-e6b7cd7509584028"}
Have $n=efg$ and $[\Gal(L/K): D_{q_i}] = g \implies [K_{D_{q_i}} : K] = g$.

All conjugate, so suffices to consider a single $P\mathrel{\Big|}p$ and the tower:

Precisely the condition to induce a map on residue fields: $\sigma \in D\implies \overline{\sigma}: B/P\to B/P$ where $b+P\mapsto \sigma(b) + P$, well-defined since $\sigma$ fixed $P$.

Also fixes $A$, so descends to the local Galois group, yielding a group morphism $D\twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B / \kappa_A)$.
:::

::: {.front card-id="card-ff3d529b614a599f"}
What is the inertia group?
:::

::: {.back card-id="card-ff3d529b614a599f"}
$T_P \coloneqq\ker\qty{D_P\twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B/\kappa_A)}$.

Idea: elements in Galois that make sense on residue fields and satisfy $\sigma(b) = b \operatorname{mod}P$ for all $b\in B$.
:::

::: {.front card-id="card-b42059015056b43d"}
Discuss the inertia/decomposition SES.
:::

::: {.back card-id="card-b42059015056b43d"}
$T_P \hookrightarrow D_P \twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B/\kappa_A)$.
:::

::: {.front card-id="card-ef181922d775519f"}
Why care about inertia/decomposition groups?
:::

::: {.back card-id="card-ef181922d775519f"}
Factors $L/K$ into a tower of extensions where all splitting happens first and all ramification happens last:
:::

::: {.front card-id="card-78a6e1f24e6c7d1e"}
Describe the filtration on $D/T \cong \Gal(\widehat{L} / \widehat{K})$.
:::

::: {.back card-id="card-78a6e1f24e6c7d1e"}
$\sigma\in G_i \iff \sigma$ is the identity on $\widehat{B}/P^{i+1}$.

What this is doing: write $B\ni b = \sum b_i \pi^i$, then

$\sigma \in T = G_0 \iff \sigma(b) = b_0 + { \mathsf{O}}(\pi)$

$\sigma\in G_1\iff \sigma(b) = b_0 + b_1\pi + { \mathsf{O}}(\pi^2)$

Allowed to change coefficients $k\geq i+1$.

Terminates, so $1 = G_i \normal\cdots \normal G_1 \normal G_0 = D$.
:::

::: {.front card-id="card-3b503d303e16a541"}
Describe tame and wild ramification
:::

::: {.back card-id="card-3b503d303e16a541"}
For a finite extension of discretely valued fields with residue characteristic $p$, ramification is tame if the ramification index is prime to $p$ and the residue extension is separable; otherwise it is wild. For a finite extension of global fields, test this condition at each nonarchimedean place. The extension is tamely ramified if it is tame at every such place; wild ramification occurs at a place whose local extension is wild.
:::

::: {.front card-id="card-b76e28f88edd3c0a"}
What are $\overline{\ZZ}$ and $\overline{\QQ}$?
:::

::: {.back card-id="card-b76e28f88edd3c0a"}
$\exists p\in \ZZ[x]$ (resp $\QQ[x]$) such that $p(\alpha) = 0$.
:::

::: {.front card-id="card-769eb6d4be5614ca"}
Give an example of a $\alpha\not\in \overline{\ZZ}$.
:::

::: {.back card-id="card-769eb6d4be5614ca"}
$\alpha \coloneqq i/2$, since its minimal polynomial is $x^2 + {1\over 4}\not\in\ZZ[x]$.
:::

::: {.front card-id="card-e8159a7f6128abef"}
What is the cardinality of $\overline{\ZZ}$?
:::

::: {.back card-id="card-e8159a7f6128abef"}
Countable
:::

::: {.front card-id="card-e947251c74d7b3a3"}
Why is $\ZZ[i]$ Euclidean?
:::

::: {.back card-id="card-e947251c74d7b3a3"}
For $a,b\in \ZZ[i]$, take $a/b\in \CC$ and round to the nearest lattice point.

Distance is ${r\over b} \coloneqq d \leq {1\over \sqrt 2}< 1$, so yields ${a\over b} = q + {r\over b}\implies a=qb+r$ where ${\left\lvert {r} \right\rvert} < {\left\lvert {b} \right\rvert}$.
:::

::: {.front card-id="card-b6e53d61128e517f"}
Describe the Euclidean algorithm.
:::

::: {.back card-id="card-b6e53d61128e517f"}
$r_0 = a$

$r_1 = b$

$r_2$ is the remainder of $r_0/r_1$

$r_3$ is the remainder of $r_1/r_2$

Then $(a,b) =(r_0, r_1) = (r_1, r_2) = \cdots = (r_{k-1}, 0) = r_{k-1}$ since $r_0 - r_2 = \ell r_1$.
:::

::: {.front card-id="card-11c8132e96202948"}
What are the units in $\ZZ[i]$?
:::

::: {.back card-id="card-11c8132e96202948"}
$\left\{{\pm 1,\pm i}\right\} = \left\{{x\in \ZZ[i] \st N(x) = 1}\right\}$.
:::

::: {.front card-id="card-03c134fde94e176b"}
What are the primes in $\ZZ[i]$?
:::

::: {.back card-id="card-03c134fde94e176b"}
$1+i$

$a+bi$ where $N(a+bi) = p \equiv 1\operatorname{mod}4$.

$p$ where $p \equiv 3 \operatorname{mod}4$.

Follows because $N(\alpha) = p$ prime forces $\alpha$ to be prime.
:::

::: {.front card-id="card-dea31e3c48e1270b"}
Which primes are sums of two squares?
:::

::: {.back card-id="card-dea31e3c48e1270b"}
$p\equiv 1 \operatorname{mod}4$ and $p=2$.
:::

::: {.front card-id="card-225666a623557146"}
Give a congruence for $(p-1)!$.
:::

::: {.back card-id="card-225666a623557146"}
$(p-1)! \equiv -1 \operatorname{mod}p \iff p$ is prime.
:::

::: {.front card-id="card-72019e428160edc8"}
Discuss properties of $\ZZ[i]$.
:::

::: {.back card-id="card-72019e428160edc8"}
PID

Euclidean domain
:::

::: {.front card-id="card-56e493ba165bd2b5"}
What is $\zeta_3$ in rectangular coordinates?
:::

::: {.back card-id="card-56e493ba165bd2b5"}
$\zeta_3 = {1\over 2}(-1 + \sqrt{3} i)$.
:::

::: {.front card-id="card-ac71ebcb5893417e"}
What is $\operatorname{ff}\ZZ[\zeta_3]$?
:::

::: {.back card-id="card-ac71ebcb5893417e"}
$\QQ(\zeta_3) = \QQ(\sqrt{-3})$.
:::

::: {.front card-id="card-f368978938324492"}
What are the units in $\ZZ[\zeta_3]$?
:::

::: {.back card-id="card-f368978938324492"}
$\left\{{\pm 1, \pm \zeta_3, \pm\zeta_3^2}\right\}$.
:::

::: {.front card-id="card-9bbba6dc9000abd2"}
What are the primes in $\ZZ[\zeta_3]$?
:::

::: {.back card-id="card-9bbba6dc9000abd2"}
$1-\zeta_3$ with norm 3

$N(a+b\zeta_3) = p \equiv 1\operatorname{mod}3$

$p\equiv 2 \operatorname{mod}3$.
:::

::: {.front card-id="card-ca276716883c90d1"}
For $K = \QQ(\sqrt{-D})$, what is $\ZZ_K$?
:::

::: {.back card-id="card-ca276716883c90d1"}
$\ZZ_K = \ZZ { \left[ \scriptstyle {\sqrt{-D}} \right] }$ if $D\not\equiv 1 \operatorname{mod}4$.

$\ZZ_K = \ZZ { \left[ \scriptstyle {1 + \sqrt{D} \over 2} \right] }$ if $D\equiv 1 \operatorname{mod}4$.
:::

::: {.front card-id="card-fc96cc5c2a31d0c5"}
Which imaginary quadratic fields are PIDs? Which are EDs?
:::

::: {.back card-id="card-fc96cc5c2a31d0c5"}
Only 9 cases: $-1,-2,-3,-7,-11,-19,-43,-67,-163$.

EDs: the first five.

Note: only finitely many units.
:::

::: {.front card-id="card-0540230a0d326223"}
Which real quadratic fields are PIDS? EDs?
:::

::: {.back card-id="card-0540230a0d326223"}
EDs: Finitely many.

PIDs: unknown, conjecturally infinitely many.

Infinitely many units: $a^2-b^2D=1$ is the Pell equation and has infinitely many solutions.
:::

::: {.front card-id="card-8e90336120d7bd50"}
Give an example of failure of unique factorization.
:::

::: {.back card-id="card-8e90336120d7bd50"}
$6 = (2)(3) = (1+\sqrt{-5})(1-\sqrt{-5})\in \ZZ { \left[ \scriptstyle {\sqrt{-5}} \right] }$, all factors are irreducible.
:::

::: {.front card-id="card-bf54130388c9cc35"}
What is a CM field?
:::

::: {.back card-id="card-bf54130388c9cc35"}
$K$ a purely imaginary quadratic extension of a totally real field, so $K = K_0(\sqrt\alpha)$ with $\sigma(\alpha)\in {\mathbf{R}}_{\gt 0}$ for every embedding $\sigma: K_0 \hookrightarrow\CC$.
:::

::: {.front card-id="card-2d28b0bf69a069dc" tags="definition"}
Absolute value
:::

::: {.back card-id="card-2d28b0bf69a069dc"}
An absolute value on a field $K$ is a map $|\cdot|:K\to\mathbb{R}_{\ge0}$ such that $|x|=0\iff x=0$, $|xy|=|x||y|$, and $|x+y|\le|x|+|y|$. It is nonarchimedean if the stronger ultrametric inequality $|x+y|\le\max(|x|,|y|)$ holds.
:::

::: {.front card-id="card-af7bae7d937f70bd" tags="definition"}
Adele
:::

::: {.back card-id="card-af7bae7d937f70bd"}
The adele ring of a number field $K$ is the restricted product $\mathbb{A}_K = \prod'_v K_v$ over all places $v$, consisting of tuples $(x_v)$ with $x_v \in \mathcal{O}_v$ for all but finitely many finite places $v$.
:::

::: {.front card-id="card-593b0079222b3884" tags="definition"}
Algebraic integer
:::

::: {.back card-id="card-593b0079222b3884"}
An algebraic integer is a complex number $\alpha$ that is a root of a monic polynomial in $\mathbb{Z}[x]$. Equivalently, $\alpha\in\mathcal{O}_K$ for some number field $K$; the algebraic integers form the ring $\overline{\mathbb{Z}}$.
:::

::: {.front card-id="card-8fff4f5d5697c42e" tags="definition"}
Discrete valuation
:::

::: {.back card-id="card-8fff4f5d5697c42e"}
A discrete valuation on a field $K$ is a surjective map $v:K^\times\to\mathbb{Z}$ such that $v(xy)=v(x)+v(y)$ and $v(x+y)\ge\min(v(x),v(y))$, extended by $v(0)=+\infty$. Its valuation ring is $R=\{x:v(x)\ge0\}$, a DVR.
:::

::: {.front card-id="card-047d16c894b48d59" tags="definition"}
Discriminant
:::

::: {.back card-id="card-047d16c894b48d59"}
For a number field $K$ of degree $n$ with integral basis $\omega_1, \dots, \omega_n$, the discriminant is $\mathrm{disc}(K) = \det(\mathrm{Tr}_{K/\mathbb{Q}}(\omega_i \omega_j))$; it is independent of the choice of integral basis.
:::

::: {.front card-id="card-6815a6dd71de1f6e" tags="definition"}
Field norm
:::

::: {.back card-id="card-6815a6dd71de1f6e"}
For a finite extension $L/K$ and $\alpha\in L$, the norm $N_{L/K}(\alpha)$ is the determinant of the $K$-linear map $m_\alpha:L\to L$, $x\mapsto\alpha x$. If $L/K$ is separable, $N_{L/K}(\alpha)=\prod_{\sigma}\sigma(\alpha)$, the product over all $K$-embeddings $L\hookrightarrow\overline{K}$.
:::

::: {.front card-id="card-fc530cec796f5c41" tags="definition"}
Fractional ideal
:::

::: {.back card-id="card-fc530cec796f5c41"}
A fractional ideal of a Dedekind domain $R$ with fraction field $K$ is a nonzero $R$-submodule $I\subseteq K$ such that $dI\subseteq R$ for some $d\in K^\times$. Equivalently, $I$ is a finitely generated $R$-submodule of $K$. Fractional ideals form a group under multiplication.
:::

::: {.front card-id="card-b1187e80e54b164f" tags="definition"}
Haar measure
:::

::: {.back card-id="card-b1187e80e54b164f"}
A Haar measure on a locally compact topological group $G$ is a nonzero Radon measure $\mu$ that is left-invariant: $\mu(gA)=\mu(A)$ for all $g\in G$ and Borel sets $A$. It is unique up to a positive scalar; for a local field, $\mu(xA)=|x|\mu(A)$ for a suitable normalization.
:::

::: {.front card-id="card-2cba500e0cb7eed2" tags="definition"}
Higher ramification group
:::

::: {.back card-id="card-2cba500e0cb7eed2"}
For a finite Galois extension $L/K$ of local fields with valuation ring $B$ and maximal ideal $\mathfrak{P}$, the $i$-th ramification group is $G_i=\{\sigma\in\mathrm{Gal}(L/K):\sigma(b)\equiv b\pmod{\mathfrak{P}^{i+1}}\ \forall b\in B\}$. Thus $G_0$ is the inertia group and $G_1$ is the wild inertia subgroup.
:::

::: {.front card-id="card-212923cbca48045d" tags="definition"}
Ideal class group
:::

::: {.back card-id="card-212923cbca48045d"}
The ideal class group of a number field $K$ is $\mathrm{Cl}(K) = I_K/P_K$, the group of fractional ideals modulo the subgroup of principal fractional ideals; it is finite, with order the class number $h_K$.
:::

::: {.front card-id="card-3df6254a6558c806" tags="definition"}
Idele
:::

::: {.back card-id="card-3df6254a6558c806"}
The idele group $\mathbb{A}_K^\times$ is the group of invertible elements of the adele ring; equivalently, it is the restricted product of the groups $K_v^\times$ with respect to the subgroups $\mathcal{O}_v^\times$.
:::

::: {.front card-id="card-108828f81fb41881" tags="definition"}
Local ring
:::

::: {.back card-id="card-108828f81fb41881"}
A commutative ring $R$ is local if it has a unique maximal ideal $\mathfrak{m}$. Equivalently, the nonunits of $R$ form an ideal, namely $\mathfrak{m}$; then $R\setminus\mathfrak{m}=R^\times$.
:::

::: {.front card-id="card-4c9ec3a063e850d2" tags="definition"}
Localization
:::

::: {.back card-id="card-4c9ec3a063e850d2"}
For a commutative ring $R$ and a multiplicative subset $S\subseteq R$, the localization $S^{-1}R$ is the ring of fractions $r/s$ with $r\in R$, $s\in S$, modulo the usual equivalence. For a prime ideal $\mathfrak{p}$, $R_{\mathfrak{p}}=(R\setminus\mathfrak{p})^{-1}R$ is the local ring at $\mathfrak{p}$.
:::

::: {.front card-id="card-c6455b6f0a43fb96" tags="definition"}
Monogenic
:::

::: {.back card-id="card-c6455b6f0a43fb96"}
An extension of rings $A\subseteq B$ is monogenic if $B=A[x]$ for some $x\in B$. A field extension $L/K$ is monogenic if $L=K(\alpha)$ for some $\alpha\in L$; in characteristic zero every finite extension is monogenic by the primitive element theorem.
:::

::: {.front card-id="card-33dae75b9e742d28" tags="definition"}
Nonarchimedean place
:::

::: {.back card-id="card-33dae75b9e742d28"}
A nonarchimedean place of a number field $K$ is an equivalence class of nonarchimedean absolute values on $K$; equivalently, a prime ideal $\mathfrak{p}$ of $\mathcal{O}_K$, with absolute value $|x|_{\mathfrak{p}}=c^{v_{\mathfrak{p}}(x)}$ for a fixed $0<c<1$. Its completion is a nonarchimedean local field.
:::

::: {.front card-id="card-e3e945677e8fbf36" tags="definition"}
Number field
:::

::: {.back card-id="card-e3e945677e8fbf36"}
A number field is a field $K$ that is a finite extension of $\mathbb{Q}$. Equivalently, $K=\mathbb{Q}(\alpha)$ for some algebraic number $\alpha$; its degree is $[K:\mathbb{Q}]$.
:::

::: {.front card-id="card-beb08e0117d2699b" tags="definition"}
P-adic valuation
:::

::: {.back card-id="card-beb08e0117d2699b"}
For a prime $p$ and $x\in\mathbb{Q}^\times$, the $p$-adic valuation $v_p(x)$ is the exponent of $p$ in the prime factorization of $x$; set $v_p(0)=+\infty$. It extends to $\mathbb{Q}_p$ and satisfies $v_p(x+y)\ge\min(v_p(x),v_p(y))$.
:::

::: {.front card-id="card-279f332765419d20" tags="definition"}
Pell equation
:::

::: {.back card-id="card-279f332765419d20"}
The Pell equation is $x^2-Dy^2=1$ for a positive nonsquare integer $D$. Its integer solutions form an infinite abelian group under multiplication in $\mathbb{Z}[\sqrt{D}]$, namely the units of norm $1$; the fundamental solution generates the group modulo torsion $\{\pm1\}$.
:::

::: {.front card-id="card-bb3b3bb6397d494e" tags="definition"}
Principal ideal
:::

::: {.back card-id="card-bb3b3bb6397d494e"}
An ideal $I$ of a ring $R$ is principal if $I=(a)=aR$ for some $a\in R$. In a Dedekind domain the principal fractional ideals form a subgroup of the group of fractional ideals; the quotient is the ideal class group.
:::

::: {.front card-id="card-8496d525c2680387" tags="definition"}
Ramification
:::

::: {.back card-id="card-8496d525c2680387"}
A prime $\mathfrak{p}$ of a number field $K$ ramifies in an extension $L/K$ if $\mathfrak{p}\mathcal{O}_L$ has a repeated prime factor, equivalently if some ramification index $e(\mathfrak{P}\mid\mathfrak{p})>1$. For a finite extension of local fields, ramification is the failure of the residue field extension to capture the full degree, i.e. $e>1$.
:::

::: {.front card-id="card-2036691235c5bd8e" tags="definition"}
Residue characteristic
:::

::: {.back card-id="card-2036691235c5bd8e"}
The residue characteristic of a valued field $(K,v)$ is the characteristic of its residue field $\kappa=R/\mathfrak{m}$. For a local field it is the prime $p$ with $v(p)>0$.
:::

::: {.front card-id="card-66b4106ad5234330" tags="definition"}
Residue degree
:::

::: {.back card-id="card-66b4106ad5234330"}
For an extension of Dedekind domains $A\subseteq B$ and a prime $\mathfrak{P}\mid\mathfrak{p}$, the residue degree is $f(\mathfrak{P}/\mathfrak{p})=[\kappa(\mathfrak{P}):\kappa(\mathfrak{p})]$, where $\kappa(\mathfrak{p})=A_{\mathfrak{p}}/\mathfrak{p}A_{\mathfrak{p}}$. For a finite extension of local fields, $[L:K]=ef$ with $e$ the ramification index.
:::

::: {.front card-id="card-e93f565d0bb95844" tags="definition"}
Ring of integers
:::

::: {.back card-id="card-e93f565d0bb95844"}
The ring of integers $\mathcal{O}_K$ of a number field $K$ is the integral closure of $\mathbb{Z}$ in $K$, i.e. the set of $\alpha\in K$ that are roots of a monic polynomial in $\mathbb{Z}[x]$. It is a Dedekind domain with fraction field $K$.
:::

::: {.front card-id="card-a1c67652bd548793" tags="definition"}
Splitting of a prime
:::

::: {.back card-id="card-a1c67652bd548793"}
A prime $\mathfrak{p}$ of $K$ splits completely in a finite extension $L/K$ if $\mathfrak{p}\mathcal{O}_L=\mathfrak{P}_1\cdots\mathfrak{P}_n$ with $n=[L:K]$ distinct primes, equivalently $e(\mathfrak{P}_i\mid\mathfrak{p})=f(\mathfrak{P}_i\mid\mathfrak{p})=1$ for all $i$.
:::

::: {.front card-id="card-ce80871430f96599" tags="definition"}
Uniformizer
:::

::: {.back card-id="card-ce80871430f96599"}
A uniformizer of a discrete valuation ring $R$ with maximal ideal $\mathfrak{m}$ is an element $\pi\in R$ with $v(\pi)=1$, equivalently a generator of $\mathfrak{m}$. Every nonzero element of the fraction field is $u\pi^n$ with $u\in R^\times$ and $n\in\mathbb{Z}$.
:::
