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
$R = k{\llbracket x^2, x^3 \rrbracket  }$ is local with ${\mathfrak{m}}_R = \left\langle{x^2, x^3}\right\rangle$, so not a PID.
:::

::: {.front card-id="card-bb3f3bb4b22f2656"}
What is the valuation ring of a DVF $K$?
:::

::: {.back card-id="card-bb3f3bb4b22f2656"}
$R = R(K) = \left\{{x\in K {~\mathrel{\Big\vert}~}v(x) \geq 0}\right\} = v^{-1}([0, \infty])$

Has unique maximal ideal ${\mathfrak{m}}_R = \left\{{x\in K {~\mathrel{\Big\vert}~}v(x) > 0}\right\} = \left\langle{\pi}\right\rangle$ for $\pi$ a uniformizer with $v(\pi) = 1$.

Always a DVR, in particular a PID, and $\operatorname{Spec}R = \left\{{0, {\mathfrak{m}}_R}\right\}$.
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
Every $x\in \operatorname{ff}(A)$ is of the form $\sum_{n\geq n_0} s_n \pi^n$ with $s_n\in S\subset A$ a set of representatives of $A/{\mathfrak{m}}$.

Compare to $x = \sum a_n p^n$ with $0\leq a_n\leq p-1$ for ${ {\mathbf{Z}}_{\widehat{p}} }$.

If $[L: \operatorname{ff}(A)] = n$ then $B \coloneqq \operatorname{cl}^{\mathrm{int}}_L(A)$ is a DVR and $B \in   {}_{A}{\mathsf{Mod}}^{{\mathrm{free}}, \operatorname{rank}=n}$ and complete wrt the topology induced by $B$.
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
Describe ${ {\mathbf{Z}}_{\widehat{p}} }$ in terms of valuations.
:::

::: {.back card-id="card-9747412906f697be"}
$\left\{{x\in {\mathbf{Q}}{~\mathrel{\Big\vert}~}v_p(x) \geq 0}\right\}$ or $\left\{{x\in {\mathbf{Q}}{~\mathrel{\Big\vert}~}{\left\lvert {x} \right\rvert}_p \leq 1}\right\}$.

Explicitly ${ {\mathbf{Z}}_{\widehat{p}} }\coloneqq\left\{{{a\over b} \in {\mathbf{Q}}{~\mathrel{\Big\vert}~}p\nmid b}\right\} = {\mathbf{Z}} { \left[ \scriptstyle {{1\over \ell} {~\mathrel{\Big\vert}~}\ell \neq p} \right] }$.
:::

::: {.front card-id="card-68553d646b8bf636"}
Discuss ring-theoretic properties of ${ {\mathbf{Z}}_{\widehat{p}} }$.
:::

::: {.back card-id="card-68553d646b8bf636"}
Has maximal ideal $\left\langle{p}\right\rangle = \left\{{{a\over b} {~\mathrel{\Big\vert}~}p\nmid a}\right\}$

Every element in ${ {\mathbf{Z}}_{\widehat{p}} }\setminus\left\langle{p}\right\rangle$ is a unit, so this is a local ring with residue field ${ \mathbf{F} }_p$.

Take completion to get ${ {\mathbf{Z}}_{\widehat{p}} }$.
:::

::: {.front card-id="card-748d1c56cf6a74c5"}
Explicitly describe elements in ${ {\mathbf{Z}}_{\widehat{p}} }$.
:::

::: {.back card-id="card-748d1c56cf6a74c5"}
${ {\mathbf{Z}}_{\widehat{p}} }= \left\{{\sum a_i p^i {~\mathrel{\Big\vert}~}0 \leq a_i \leq p-1}\right\}$

Equivalently ${ {\mathbf{Z}}_{\widehat{p}} }= \cocolim_n {\mathbf{Z}}/\left\langle{p^n}\right\rangle$ which contains sequences $\mathbf{a} = {\left[ {a_0, a_0 + a_1 p, a_0 + a_1 p + a_2 p^2, \cdots} \right]}$ of partial sums so that $\mathbf{a}_n \operatorname{mod}p^n \cong \mathbf{a}_{n-1}$.
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

E.g. $L_3 {\mathbf{Z}}$ allows fractions with no 3 in the denominator.
:::

::: {.front card-id="card-4adb1bcf42e5b94c"}
Discuss the AKLB setup when $L/K$ is finite and $B = \operatorname{cl}^{\mathrm{int}}_L(A)$ is a DVR.
:::

::: {.back card-id="card-4adb1bcf42e5b94c"}
The extension satisfies ${\mathfrak{m}}_A B = {\mathfrak{m}}_B^e$ with $[\kappa_B : \kappa_A] = f$ and $n \coloneqq[L: K] = ef$. Two extreme cases:

If $e=1, f=n$ (so no ramification) and $\kappa_B = \kappa_A(\overline{\alpha})$ is simple (e.g. if the residue field extension is separable) then $B$ is monogenic: $B\cong A[x]/\left\langle{f}\right\rangle$ where $f$ is the minimal polynomial over $K$ of a lift of $\overline{\alpha}$ to $B$.

If $e=n, f=1$ then $B = A[x]/\left\langle{f}\right\rangle$ where $f$ is the minimal polynomial of $\pi_B$

Useful: rings of integers of extensions become much easier to express! Ramification and splitting is simpler because of the single prime.
:::

::: {.front card-id="card-f344e33aa0fd216b"}
What is the decomposition group?
:::

::: {.back card-id="card-f344e33aa0fd216b"}
For $L/K$ Galois and $p\in \operatorname{Spec}A$, write $pB = \prod_{i\leq g} q_i^e$ where $q_i\in \operatorname{Spec}B$, all $e$ the same since Galois, and $f \coloneqq[B/b_i : A/p]$. Then $D_{q_i}\coloneqq{\operatorname{Stab}}_{{ \mathsf{Gal}}(L/K)}(q_i)$, elements of Galois fixing $q_i$.

All $D_{q_i}$ are conjugate in ${ \mathsf{Gal}}(L/K)$ and thus the corresponding fields $K_{D_{q_i}}$ are isomorphic.

Not necessarily normal.
:::

::: {.front card-id="card-e6b7cd7509584028"}
Why is the decomposition group useful?
:::

::: {.back card-id="card-e6b7cd7509584028"}
Have $n=efg$ and $[{ \mathsf{Gal}}(L/K): D_{q_i}] = g \implies [K_{D_{q_i}} : K] = g$.

All conjugate, so suffices to consider a single $P\mathrel{\Big|}p$ and the tower:

Precisely the condition to induce a map on residue fields: $\sigma \in D\implies \overline{\sigma}: B/P\to B/P$ where $b+P\mapsto \sigma(b) + P$, well-defined since $\sigma$ fixed $P$.

Also fixes $A$, so descends to the local Galois group, yielding a group morphism $D\twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B / \kappa_A)$.
:::

::: {.front card-id="card-0ba81c7dd4f84621"}
What is a **normal** extension $L/K$?
:::

::: {.back card-id="card-0ba81c7dd4f84621"}
If $\alpha\in L$ then all Galois conjugates are again in $L$, so $L$ contains all roots of ${\operatorname{minpoly}}_K(\alpha)$.
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
Describe the filtration on $D/T \cong { \mathsf{Gal}}(\widehat{L} / \widehat{K})$.
:::

::: {.back card-id="card-78a6e1f24e6c7d1e"}
$\sigma\in G_i \iff \sigma$ is the identity on $\widehat{B}/P^{i+1}$.

What this is doing: write $B\ni b = \sum b_i \pi^i$, then

$\sigma \in T = G_0 \iff \sigma(b) = b_0 + { \mathsf{O}}(\pi)$

$\sigma\in G_1\iff \sigma(b) = b_0 + b_1\pi + { \mathsf{O}}(\pi^2)$

Allowed to change coefficients $k\geq i+1$.

Terminates, so $1 = G_i {~\trianglelefteq~}\cdots {~\trianglelefteq~}G_1 {~\trianglelefteq~}G_0 = D$.
:::

::: {.front card-id="card-3b503d303e16a541"}
Describe tame and wild ramification
:::

::: {.back card-id="card-3b503d303e16a541"}
For a finite extension of discretely valued fields with residue characteristic $p$, ramification is tame if the ramification index is prime to $p$ and the residue extension is separable; otherwise it is wild. For a finite extension of global fields, test this condition at each nonarchimedean place. The extension is tamely ramified if it is tame at every such place; wild ramification occurs at a place whose local extension is wild.
:::

::: {.front card-id="card-b76e28f88edd3c0a"}
What are $\overline{{\mathbf{Z}}}$ and $\overline{{\mathbf{Q}}}$?
:::

::: {.back card-id="card-b76e28f88edd3c0a"}
$\exists p\in {\mathbf{Z}}[x]$ (resp ${\mathbf{Q}}[x]$) such that $p(\alpha) = 0$.
:::

::: {.front card-id="card-769eb6d4be5614ca"}
Give an example of a $\alpha\not\in \overline{{\mathbf{Z}}}$.
:::

::: {.back card-id="card-769eb6d4be5614ca"}
$\alpha \coloneqq i/2$, since its minimal polynomial is $x^2 + {1\over 4}\not\in{\mathbf{Z}}[x]$.
:::

::: {.front card-id="card-e8159a7f6128abef"}
What is the cardinality of $\overline{{\mathbf{Z}}}$?
:::

::: {.back card-id="card-e8159a7f6128abef"}
Countable
:::

::: {.front card-id="card-e947251c74d7b3a3"}
Why is ${\mathbf{Z}}[i]$ Euclidean?
:::

::: {.back card-id="card-e947251c74d7b3a3"}
For $a,b\in {\mathbf{Z}}[i]$, take $a/b\in {\mathbf{C}}$ and round to the nearest lattice point.

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
What are the units in ${\mathbf{Z}}[i]$?
:::

::: {.back card-id="card-11c8132e96202948"}
$\left\{{\pm 1,\pm i}\right\} = \left\{{x\in {\mathbf{Z}}[i] {~\mathrel{\Big\vert}~}N(x) = 1}\right\}$.
:::

::: {.front card-id="card-03c134fde94e176b"}
What are the primes in ${\mathbf{Z}}[i]$?
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
Discuss properties of ${\mathbf{Z}}[i]$.
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
What is $\operatorname{ff}{\mathbf{Z}}[\zeta_3]$?
:::

::: {.back card-id="card-ac71ebcb5893417e"}
${\mathbf{Q}}(\zeta_3) = {\mathbf{Q}}(\sqrt{-3})$.
:::

::: {.front card-id="card-f368978938324492"}
What are the units in ${\mathbf{Z}}[\zeta_3]$?
:::

::: {.back card-id="card-f368978938324492"}
$\left\{{\pm 1, \pm \zeta_3, \pm\zeta_3^2}\right\}$.
:::

::: {.front card-id="card-9bbba6dc9000abd2"}
What are the primes in ${\mathbf{Z}}[\zeta_3]$?
:::

::: {.back card-id="card-9bbba6dc9000abd2"}
$1-\zeta_3$ with norm 3

$N(a+b\zeta_3) = p \equiv 1\operatorname{mod}3$

$p\equiv 2 \operatorname{mod}3$.
:::

::: {.front card-id="card-ca276716883c90d1"}
For $K = {\mathbf{Q}}(\sqrt{-D})$, what is ${\mathbf{Z}}_K$?
:::

::: {.back card-id="card-ca276716883c90d1"}
${\mathbf{Z}}_K = {\mathbf{Z}} { \left[ \scriptstyle {\sqrt{-D}} \right] }$ if $D\not\equiv 1 \operatorname{mod}4$.

${\mathbf{Z}}_K = {\mathbf{Z}} { \left[ \scriptstyle {1 + \sqrt{D} \over 2} \right] }$ if $D\equiv 1 \operatorname{mod}4$.
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
$6 = (2)(3) = (1+\sqrt{-5})(1-\sqrt{-5})\in {\mathbf{Z}} { \left[ \scriptstyle {\sqrt{-5}} \right] }$, all factors are irreducible.
:::
