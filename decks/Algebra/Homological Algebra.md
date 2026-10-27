---
title: "Algebra::Homological Algebra"
---

::: {.front card-id="card-887eb293af765b9b"}
What is a dga?
:::

::: {.back card-id="card-887eb293af765b9b"}
$C$ a dg ${}_{k}\Mod$ where for $x \in C_i, y\in C_j$,
$$d(xy) = d(x)y + (-1)^i x d(y)$$
:::

::: {.front card-id="card-d5255a76032d4622"}
What is a dgla?
:::

::: {.back card-id="card-d5255a76032d4622"}
$C$ a dg ${\mathsf{Lie}\dash \mathsf{Alg}}$ where for $x\in C_i, y\in C_j$,
$$d([xy]) = [d(x) y] + (-1)^i[x d(y)]$$
:::

::: {.front card-id="card-1de7eb2881dd4cc1"}
What is a counital dg coalgebra?
:::

::: {.back card-id="card-1de7eb2881dd4cc1"}
$C$ a graded coalgebra, so $\exists \Delta: C\to C\otimes_k C$ coassociative $(\Delta\otimes 1)\Delta = (1\otimes\Delta)\Delta$ with
$$(d\otimes 1 + 1\otimes d)\Delta = \Delta d$$
Counital if $\exists {\varepsilon}: C\to k$ with
$$({\varepsilon}\otimes 1)\Delta = 1 = (1\otimes{\varepsilon})\Delta$$
:::

::: {.front card-id="card-e0d7794924e1b89c"}
What is a formula for the pushout of module morphisms $\alpha: Y\to A$ and $\beta: Y\to B$?
:::

::: {.back card-id="card-e0d7794924e1b89c"}
A quotient module:
$$A\oplus B\twoheadrightarrow A{ \amalg_{Y} } B \cong { A\oplus B  \over  \left\langle{ (\,-\alpha(y)\,, \beta(y)\, ) \st y\in Y}\right\rangle }$$
:::

::: {.front card-id="card-f0b59e92a8661d8f"}
What is a formula for the pullback of module morphisms $\phi: A\to X$ and $\psi: B\to X$?
:::

::: {.back card-id="card-f0b59e92a8661d8f"}
A submodule:
$$A \underset{\scriptscriptstyle {X} }{\times} B = \left\langle{(a,b) \in A\oplus B \st\phi(a) = \psi(b)}\right\rangle \subseteq A\oplus B$$
:::

::: {.front card-id="card-122cfadc82a23528"}
Describe limits and colimits in terms of quotients and submodules.
:::

::: {.back card-id="card-122cfadc82a23528"}
Colimits $\sim$ quotients, e.g. pushouts (glue by equivalence)

Limits $\sim$ submodules, e.g. pullbacks (impose equality)
:::

::: {.front card-id="card-e72e37c7022186ec"}
What is a (left) hereditary ring? Give an example.
:::

::: {.back card-id="card-e72e37c7022186ec"}
Every (left) ideal is projective as a submodule, or $\mathrm{gldim}_{\mathrm{left}} R \leq 1$.

$k[x]$ is hereditary, since $\mathrm{gldim}_{\mathrm{left}} k[x_1, \cdots, x_{n}]= n$ by the Hilbert syzygy theorem.
:::

::: {.front card-id="card-7f29b2e7218b076a"}
What is the left global dimension of a ring?
:::

::: {.back card-id="card-7f29b2e7218b076a"}
$$\mathrm{gldim}_{\mathrm{left}} R \coloneqq\sup_{M\in   {}_{R}\Mod} \mathrm{projdim}_R M$$
where the projective dimension is the smallest length of a projective resolution.
:::

::: {.front card-id="card-e2723fb6229838a4"}
What is the variance/contravariance of homs?
:::

::: {.back card-id="card-e2723fb6229838a4"}
$[P_1\to P_0, N] = [P_0, N] \to [P_1, N]$, so $\mathop{\mathrm{Hom}}({-}, N)$ is contravariant (like a dual module $V {}^{ \vee }$)

$[M, I_1\to I_0] = [M, I_0]\to [M, I_1]$, so $\mathop{\mathrm{Hom}}(M, {-})$ is covariant.
:::

::: {.front card-id="card-b169e529fd51786f"}
How do you compute $\operatorname{Ext}_R^*(M, N)$?
:::

::: {.back card-id="card-b169e529fd51786f"}
$H_*(\mathop{\mathrm{Hom}}_R(P_M, N))$ where $P_M\rightrightarrows M$ is a projective resolution.

$H_*(\mathop{\mathrm{Hom}}_R(M, I_N))$ where $N\hookrightarrow I_N$ is an injective resolution.
:::

::: {.front card-id="card-b0292b48ca4ae9f0"}
How do you compute $\operatorname{Tor}^R_*(M, N)$?
:::

::: {.back card-id="card-b0292b48ca4ae9f0"}
$H_*(M\otimes_R P_N)$ where $P_N\rightrightarrows N$ is a projective resolution.
:::

::: {.front card-id="card-5f25fa26b584c6bc" tags="math"}
What is the Kunneth theorem?
:::

::: {.back card-id="card-5f25fa26b584c6bc"}
Theorem A.5.2 (Kunneth Theorem). Let $C_\bullet$ and $D_\bullet$ be complexes of right and left $R$-modules, respectively, for which $C_n$ and $d\left(C_n\right)$ are flat $R$-modules for all $n \in \mathbb{Z}$. Then for all $n \in \mathbb{Z}$, there is a short exact sequence:
$$\begin{aligned} 0 \longrightarrow \bigoplus_{i+j=n} \mathrm{H}_i(C) \otimes_R \mathrm{H}_j(D) \longrightarrow & \mathrm{H}_n\left(C \otimes_R D\right) \longrightarrow \\ & \bigoplus_{i+j=n-1} \operatorname{Tor}_1^R\left(\mathrm{H}_i(C), \mathrm{H}_j(D)\right) \longrightarrow 0 \end{aligned}$$
Topological case: for $R$ a PID, singular chains $C_n(X;R)$ and their boundaries are free, and $C_*(X\times Y;R)\simeq C_*(X;R)\otimes_R C_*(Y;R)$ by Eilenberg-Zilber, so
$$0\to \bigoplus_{i+j=k}H_{i}(X;R)\otimes _{R}H_{j}(Y;R)\to H_{k}(X\times Y;R)\to \bigoplus_{i+j=k-1}{\mathrm  {Tor}}_{R}^{1}(H_{i}(X;R),H_{j}(Y;R))\to 0$$
:::

::: {.front card-id="card-e77e1d0a0faf351c" tags="math"}
UCT: Change of Coefficients SES
:::

::: {.back card-id="card-e77e1d0a0faf351c"}
Theorem A.5.4 (Universal Coefficients Theorem). Let $C$ be a complex of right $R$-modules in which all $C_n, d\left(C_n\right)$ are flat, and let $M$ be a left $R$ module. There is a short exact sequence
$$0 \longrightarrow \mathrm{H}_n(C) \otimes_R M \longrightarrow \mathrm{H}_n\left(C \otimes_R M\right) \longrightarrow \operatorname{Tor}_1^R\left(\mathrm{H}_{n-1}(C), M\right) \longrightarrow 0 .$$
Topological case: take $C = C_*(X;\mathbb{Z})$ and $M = A$ an abelian group:
$${\displaystyle 0\to \mathrm{Tor}_\mathbb{Z}^0 (H_{i}(X;\mathbb{Z}), A)\,{\to }\,H_{i}(X;A)\to \mathrm{Tor}_\mathbb{Z}^1 (H_{i-1}(X;\mathbb{Z} ),A)\to 0}$$
:::

::: {.front card-id="card-81fb53c268cdadd4"}
What is the enveloping algebra $A^e$ of $A\in {}_{k} \mathsf{Alg}$?
:::

::: {.back card-id="card-81fb53c268cdadd4"}
$A\otimes_k A^{^{\operatorname{op}}}$ where $(a_1\otimes b_1)\cdot (a_2\otimes b_2) = (a_1a_2)\otimes(b_2b_1)$.
:::

::: {.front card-id="card-556641b0ddf5827b"}
How are enveloping algebras related to bimodules?
:::

::: {.back card-id="card-556641b0ddf5827b"}
$({A}, {A})\dash\mathsf{biMod}  { \, \xrightarrow{\sim}\, }  {}_{A^e}\Mod$ where if $M\in ({A}, {A})\dash\mathsf{biMod}$ is sent to $M$ with $(a\otimes b).m = amb$.
:::

::: {.front card-id="card-dfa7b43cbe30fede"}
What is the ${}_{A^e}\Mod$ structure on $A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} } }$?
:::

::: {.back card-id="card-dfa7b43cbe30fede"}
Act on the first and last components:
$$(a \otimes b) \cdot\left(c_1 \otimes c_2 \otimes \cdots \otimes c_{n-1} \otimes c_n\right)=a c_1 \otimes c_2 \otimes \cdots \otimes c_{n-1} \otimes c_n b$$
:::

::: {.front card-id="card-068c74b6ed822f99"}
How is the bar complex of $A\in {}_{A^e}\Mod$ defined?
:::

::: {.back card-id="card-068c74b6ed822f99"}
$B(A): A^{\otimes\bullet}  \xrightarrow[]{\pi} { \mathrel{\mkern-16mu}\rightarrow }\,  A$ where $\pi(a\otimes b) = ab$, $d_1(a\otimes b\otimes c) = ab\otimes c - a\otimes bc$ and the general differential is a sum over collapses:
$$d_n\left(a_0 \otimes a_1 \otimes \cdots \otimes a_{n+1}\right)=\sum_{i=0}^n(-1)^i a_0 \otimes a_1 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_{n+1}$$
If $A\in   {}_{k}\Mod^\free$ then $B(A)$ is an exact free resolution of $A$ with $H^*(B(A)) = A \cdot t^0$.
:::

::: {.front card-id="card-46e9248eadcfe408"}
How are Hochschild chains and homology defined?
:::

::: {.back card-id="card-46e9248eadcfe408"}
For $M\in   {}_{A^e}\Mod$, write
$$C_*(A; M) = \bigoplus_{n\geq 0} M\otimes_{A^e} B_n(A) \cong \bigoplus_{n\geq 0} M\otimes_k A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  }$$
I.e. apply ${-}\otimes_{A^e} M$ to $B(A)$ levelwise, with differential $\operatorname{id}_M \otimes d_n$.

Then ${\operatorname{HH}}(A; M) = H^*(C_*(A; M))$, i.e. ${\operatorname{HH}}_n(A; M) = H_n(M\otimes A^{\otimes\bullet})$.
:::

::: {.front card-id="card-1e0d7faba0fee952"}
What are cycles? Boundaries?
:::

::: {.back card-id="card-1e0d7faba0fee952"}
Cycles $=\ker d_n$, boundaries $=\operatorname{im}d_{n}$.
:::

::: {.front card-id="card-32367aae38d053c3"}
How are Hochschild cochains and cohomology defined?
:::

::: {.back card-id="card-32367aae38d053c3"}
Apply ${}_{A^e}\Mod({-}, M)$ to $B(A)$, has differentials $d_n^*(f) \coloneqq fd_n$ for $f\in   {}_{A^e}\Mod(A{ {}^{ \scriptscriptstyle\otimes_{k}^{n+1} }  }\to M )$, ${\operatorname{HH}}^*(A; M)$ is its homology.
:::

::: {.front card-id="card-b8ba88be9708d92f"}
How is ${\operatorname{HH}}_*(A)$ defined?
:::

::: {.back card-id="card-b8ba88be9708d92f"}
Regard $A\in  {}_{A^e}\Mod$ and take ${\operatorname{HH}}_*(A; A)$.

Equivalently, ${\operatorname{HH}}_n(A)$ is the homology of the cyclic bar complex, $H_n(C_\bullet(A))$, or by Dold-Kan, $\pi_n { {\left\lvert {B_\bullet^{\mathrm{cyc}}(A)} \right\rvert} }$, the geometric realization of a simplicial object.
:::

::: {.front card-id="card-df010058af0a8f40"}
Discuss functoriality of ${\operatorname{HH}}^*({-})$.
:::

::: {.back card-id="card-df010058af0a8f40"}
Not a functor! Instead $(A, M)\mapsto {\operatorname{HH}}^*(A, M)$ defines a bifunctor equivalent to $\operatorname{Ext}_{A^e}^*({-}, {-})$ which is contravariant in $A$ and covariant in $M$.
:::

::: {.front card-id="card-012e4b7d9a0fdc26"}
How are ${\operatorname{HH}}_*$ and ${\operatorname{HH}}^*$ related to ext and tor?
:::

::: {.back card-id="card-012e4b7d9a0fdc26"}
$\operatorname{HH}_n(A, M) \cong \operatorname{Tor}_n^{A^e}(M, A) \text { and } \operatorname{HH}^n(A, M) \cong \operatorname{Ext}_{A^e}^n(A, M)$

First iso holds when $A\in  {}_{k}\Mod^\flat$ and second when $A\in   {}_{k}\Mod^{\mathop{\mathrm{proj}}}$.
:::

::: {.front card-id="card-811a973fb1984bb5"}
What is the reduced/normalized bar resolution?
:::

::: {.back card-id="card-811a973fb1984bb5"}
$\overline{B}_n(A) = A\otimes(A/k){ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  } \otimes A$.
:::

::: {.front card-id="card-fad01e3229c41ef1"}
What is ${\operatorname{HH}}^*(k[x])$?
:::

::: {.back card-id="card-fad01e3229c41ef1"}
${\operatorname{HH}}^*(k[x]) = k[x] t^0 \oplus k[x] t^1$, using the resolution $0\to R{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  }\xrightarrow{\otimes 1 - 1\otimes x} R{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  } \xrightarrow{\pi} R\to 0$ where $R\coloneqq k[x]$ and applying $\mathop{\mathrm{Hom}}_{R^e}({-}, R)$, using $\mathop{\mathrm{Hom}}_{R^e}(R\otimes R, R) \cong R$ in this case by $f\mapsto f(1\otimes 1)$.

Can write as a ring:
$${\operatorname{HH}}^*(k[x]) \cong k[x, t]/\left\langle{t^2}\right\rangle,\qquad {\left\lvert {x} \right\rvert} = 0, {\left\lvert {t} \right\rvert} = 1$$
:::

::: {.front card-id="card-b8860dff0c00259f"}
What is ${\operatorname{HH}}(k[x]/x^n)$?
:::

::: {.back card-id="card-b8860dff0c00259f"}
See example 1.1.21: set $A\coloneqq k[x]/x^n$. One gets ${\operatorname{HH}}^*(A) \cong \bigoplus_{i\geq 0} A t^i$ if $\operatorname{ch}k \mathrel{\Big|}n$, otherwise
$${\mathbb{H}}^*(A) = At^0 + \bigoplus_{m\geq 0} \left\langle{x}\right\rangle t^{2m + 1} + \bigoplus_{m\geq 0} A/\left\langle{ x^{n-1} }\right\rangle t^{2m}$$
:::

::: {.front card-id="card-0e206c68c41550b4"}
What are the interpretations of ${\operatorname{HH}}^n(A)$ for small $n$?
:::

::: {.back card-id="card-0e206c68c41550b4"}
$n=0$: $Z(A)$

$n=1$: $\mathop{\mathrm{Out}}\mathop{\mathrm{Der}}_k(A)$, which equals $\mathop{\mathrm{Der}}_k(A)$ when $A$ is commutative since the only inner derivation is zero.

$n=2$: Infinitesimal deformations of $A$

$n=3$: obstructions to lifting deformations to formal deformations.
:::

::: {.front card-id="card-754fc11281da8118"}
What are the interpretations of ${\operatorname{HH}}^n(A; M)$ for small $n$?
:::

::: {.back card-id="card-754fc11281da8118"}
$n=0$: $Z_M(A) \coloneqq\left\{{m\in M\st am=ma \, \forall a\in A}\right\}$.

$n=1$: $\mathop{\mathrm{Out}}\mathop{\mathrm{Der}}_k(A\to M) \coloneqq\mathop{\mathrm{Der}}_k(A\to M)/\mathop{\mathrm{Inn}}\mathop{\mathrm{Der}}_k(A\to M)$.

$n=2$: Infinitesimal deformations of $A$

$n=3$: obstructions to lifting deformations to formal deformations.
:::

::: {.front card-id="card-5329f321596e0d74"}
What is a Hochschild 2-cocycle? 2-coboundary?
:::

::: {.back card-id="card-5329f321596e0d74"}
Functions $f\in \mathop{\mathrm{Hom}}_{A^e}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{2} }  } \to M)$ which satisfy
$$a f(b \otimes c)+f(a \otimes b c)=f(a b \otimes c)+f(a \otimes b) c$$
These define ${ {}_{A}  \mathsf{Alg}}$ structures on $A\oplus M$, i.e. square-zero extensions.

Coboundaries are deformations isomorphic to the original algebra.
:::

::: {.front card-id="card-bcaafd6a9ca451ce"}
What are orthogonal central idempotents?
:::

::: {.back card-id="card-bcaafd6a9ca451ce"}
Each $e_j\in Z(A)$ and $e_j e_\ell = \delta_{j, \ell} e_j$.
:::

::: {.front card-id="card-d1c0c39d3e10012e"}
What is the cup product on ${\operatorname{HH}}^*$?
:::

::: {.back card-id="card-d1c0c39d3e10012e"}
$$\begin{align} \smile: \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m} }  }\to A) \otimes_k \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  }\to A) &\to \mathop{\mathrm{Hom}}_k(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m+n} }  }\to A) \\ (f \smile g)\left(a_1 \otimes \cdots \otimes a_{m+n}\right)&=(-1)^{m n} f\left(a_1 \otimes \cdots \otimes a_m\right) g\left(a_{m+1} \otimes \cdots \otimes a_{m+n}\right)\end{align}$$
This makes $C^*(A, A)$ into a dga.
:::

::: {.front card-id="card-e5448063a31dcb39"}
What is a consequence of ${\operatorname{HH}}^1(A; M) = 0$?
:::

::: {.back card-id="card-e5448063a31dcb39"}
Every derivation $A\to M$ is inner.
:::

::: {.front card-id="card-9d7da2c6912f809a"}
How do deformations of $A$ arise?
:::

::: {.back card-id="card-9d7da2c6912f809a"}
From noncommutative Poisson structures: elements $x\in {\operatorname{HH}}^2(A)$ with $\left\{{a, a}\right\} = 0$.
:::

::: {.front card-id="card-f9f24f8589e6554e"}
What is the circle product?
:::

::: {.back card-id="card-f9f24f8589e6554e"}
$$\begin{aligned}& (f \circ g)\left(a_1 \otimes \cdots \otimes a_{m+n-1}\right) \\ & =\sum_{i=1}^m(-1)^u f\left(a_1 \otimes \cdots \otimes a_{i-1} \otimes g\left(a_i \otimes \cdots \otimes a_{i+n-1}\right) \otimes a_{i+n} \otimes \cdots \otimes a_{m+n-1}\right) \end{aligned}$$
:::

::: {.front card-id="card-bd9252c40d15b8a6"}
How is the Gerstenhaber bracket defined?
:::

::: {.back card-id="card-bd9252c40d15b8a6"}
$$\begin{align} [{-}, {-}]: \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m} }  } \to A) \otimes_k \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{n} }  } \to A) &\to \mathop{\mathrm{Hom}}(A{ {}^{ \scriptscriptstyle\otimes_{k}^{m+n-1} }  }\to A) \\ [f, g]& =f \circ g-(-1)^{(m-1)(n-1)} g \circ f\end{align}$$
:::

::: {.front card-id="card-c8c54bff10c46b9b"}
What is a Gerstenhaber algebra?
:::

::: {.back card-id="card-c8c54bff10c46b9b"}
Definition 1.4.8. A Gerstenhaber algebra $(H, \smile,[]$,$) is a free \mathbb{Z}$-graded $k$-module $H$ for which $(H, \smile)$ is a graded commutative associative algebra, $(H,[]$,$) is a graded Lie algebra with bracket [$,$] of degree -1$ and corresponding degree shift by $-1$ on elements, and
$$[\gamma, \alpha \smile \beta]=[\gamma, \alpha] \smile \beta+(-1)^{|\alpha|(|\gamma|-1)} \alpha \smile[\gamma, \beta]$$
for all homogeneous $\alpha, \beta, \gamma$ in $H$.
:::

::: {.front card-id="card-77134e102a877ceb"}
What is the cap product?
:::

::: {.back card-id="card-77134e102a877ceb"}
$$\begin{align} \frown: \mathrm{HH}_n(A) \otimes \mathrm{HH}^m(A) &\longrightarrow\mathrm{HH}_{n-m}(A) \\ \left(a_0 \otimes a_1 \otimes \cdots \otimes a_n\right) \frown f&=(-1)^{m(n-m)} a_0 f\left(a_1 \otimes \cdots \otimes a_m\right) \otimes a_{m+1} \otimes \cdots \otimes a_n\end{align}$$
:::

::: {.front card-id="card-ae9f2a47958e0a0f"}
What is a $(p, q)$ shuffle?
:::

::: {.back card-id="card-ae9f2a47958e0a0f"}
For nonnegative integers $p$ and $q$, a $(p, q)$-shuffle is an element $\sigma$ of the symmetric group $S_{p+q}$ for which $\sigma(i)<\sigma(j)$ whenever $1 \leq i<j \leq p$ or $p+1 \leq i<j \leq p+q$.

Let $S_{p, q}$ denote the subset of $S_{p+q}$ consisting of all $(p, q)$-shuffles.
:::

::: {.front card-id="card-8aa43ace4a3debfd"}
What is the shuffle product?
:::

::: {.back card-id="card-8aa43ace4a3debfd"}
Makes ${\operatorname{HH}}_*(A)$ a graded commutative ${}_{k}  \mathsf{Alg}$,
$$\begin{aligned}
& \left(a_0 \otimes a_1 \otimes \cdots \otimes a_p\right) \cdot\left(a_0^{\prime} \otimes a_{p+1} \otimes \cdots \otimes a_{p+q}\right) \\
& =\sum_{\sigma \in S_{p, q}}(\operatorname{sgn} \sigma) a_0 a_0^{\prime} \otimes a_{\sigma^{-1}(1)} \otimes \cdots \otimes a_{\sigma^{-1}(p+q)}
\end{aligned}$$
:::

::: {.front card-id="card-79c26df340177b2c"}
What is a map $f: V\to W$ of graded vector spaces?
:::

::: {.back card-id="card-79c26df340177b2c"}
$\exists m$ such that $f(V_n) \subseteq V_{n+m}$ for all $n$; say ${\left\lvert {f} \right\rvert} = m$ is its degree.
:::

::: {.front card-id="card-ea262115759029c5"}
For $V, W$ graded vector spaces and $f:V\to V', g:W\to W'$, what is $f\otimes g$?
:::

::: {.back card-id="card-ea262115759029c5"}
$v\otimes w\mapsto (-1)^{{\left\lvert {g} \right\rvert}{\left\lvert {v} \right\rvert}} f(v)\otimes g(w) \in V'\otimes W'$.
:::

::: {.front card-id="card-3401788769da2a76"}
What is the Yoneda splice of $f\in {\operatorname{HH}}^n(A)$ and $g\in {\operatorname{HH}}^m(A)$?
:::

::: {.back card-id="card-3401788769da2a76"}
Identify $\operatorname{HH}^n(A)=\operatorname{Ext}_{A^e}^n(A,A)$. Represent $f$ and $g$ by exact $n$- and $m$-extensions of $A$ by $A$. Their Yoneda splice joins the terminal $A$ of one extension to the initial $A$ of the other, producing an $(n+m)$-extension. Its class is the cup product $f\smile g$ (with order fixed by the composition convention).
:::

::: {.front card-id="card-f4cf8157c4893998"}
What is the "base ring" action on Ext?
:::

::: {.back card-id="card-f4cf8157c4893998"}
${\operatorname{HH}}^*(A) \curvearrowright \operatorname{Ext}_A^*(M, N)$ for any $M, N \in   {}_{A}\Mod$, making it a graded ${\operatorname{HH}}^*(A)\dash$module.
:::

::: {.front card-id="card-f124527da918b109"}
What is the graded center of a graded algebra?
:::

::: {.back card-id="card-f124527da918b109"}
$Z_{\mathsf{gr}\,}(B) = \left\{{a\in B^ \homog\st ab = (-1)^{{\left\lvert {a} \right\rvert}{\left\lvert {b} \right\rvert}} ba \,\,\forall b\in B^ \homog}\right\}$.
:::

::: {.front card-id="card-7194c45516cb5d48"}
Why is the graded center important?
:::

::: {.back card-id="card-7194c45516cb5d48"}
The map
$${\operatorname{HH}}^*(A) \to  \operatorname{Ext}_A^*(M, M)$$
where $f\mapsto f\otimes\operatorname{id}_M$ is a ring morphism with image contained in $Z_{\mathsf{gr}\,}( \operatorname{Ext}_A^*(M, M))$.
:::

::: {.front card-id="card-2323068b9bef2e60"}
Give a free resolution of $k\in {}_{A}\Mod$ using ${\varepsilon}: A\to k$ where $A = k[x]/x^n$.
:::

::: {.back card-id="card-2323068b9bef2e60"}
$$\cdots \longrightarrow A \stackrel{x^{n-1}}{\longrightarrow} A \stackrel{x \cdot}{\longrightarrow} A \stackrel{x^{n-1}}{\longrightarrow} A \stackrel{x \cdot}{\longrightarrow} A \stackrel{\varepsilon}{\longrightarrow} k \longrightarrow 0 .$$
:::

::: {.front card-id="card-eef589b96f0a8d8e"}
What is $\operatorname{Ext}_A^*(k, k)$?
:::

::: {.back card-id="card-eef589b96f0a8d8e"}
$$ \operatorname{Ext}_A^*(k, k) = k[y]\cdot t^2 + \bigoplus_{n\neq 2} {k[y,z]\over y^2}\cdot t^n$$
:::

::: {.front card-id="card-0a2b571ba3db3475"}
Prove $\mathop{\mathrm{Hom}}_R(R, A) \cong A$.
:::

::: {.back card-id="card-0a2b571ba3db3475"}
Take the map $\Phi$ where $f\mapsto f(1)$,

Surjects by defining $f_a(1) \coloneqq a$ for any $a\in A$ and extending by $f_a(n) \coloneqq na$

Injects: if $f(1) = g(1) = a$ then $f(n) \coloneqq na$ and $g(n) \coloneqq na$ so $f\equiv g$.
:::

::: {.front card-id="card-a44f627c5535dc10"}
Which resolutions can be used for $\operatorname{Tor}$ and $\operatorname{Ext}$?
:::

::: {.back card-id="card-a44f627c5535dc10"}
$\operatorname{Tor}(A, B)$: a projective resolution of either argument

$\operatorname{Ext}(A, B)$: a projective resolution of $A$ or an injective resolution of $B$.
:::

::: {.front card-id="card-83626d3f3af8c6cd"}
When do functors preserve injectives/projectives?
:::

::: {.back card-id="card-83626d3f3af8c6cd"}
Has an exact left adjoint $\implies$ preserves injectives.

Has an exact right adjoint $\implies$ preserves projectives.
:::

::: {.front card-id="card-66cb45fc8793ff61"}
Characterize projectives/injectives using Hom.
:::

::: {.back card-id="card-66cb45fc8793ff61"}
$\mathop{\mathrm{Hom}}(P, {-})\iff$projective

$\mathop{\mathrm{Hom}}({-}, I) \iff$injective
:::

::: {.front card-id="card-c7e254871b94cd3c"}
When does flat coincide with torsionfree?
:::

::: {.back card-id="card-c7e254871b94cd3c"}
Modules over a PID.
:::

::: {.front card-id="card-75b0cf56e062765b"}
What is an **abelian category**?
:::

::: {.back card-id="card-75b0cf56e062765b"}
$\mathsf{C}(A, B) \in \Ab\Grp$ and composition is a group morphism,

All Finite direct sums

All kernels and cokernels

Mono = $\ker(\operatorname{coker})$.

Epi $= \operatorname{coker}(\ker)$.

Epi-mono factorization for all morphisms
:::

::: {.front card-id="card-089cfeaeedd8d036"}
What is a **delta functor**?
:::

::: {.back card-id="card-089cfeaeedd8d036"}
A collection $T^n$ ($T^{> 0}$ are *satellite functors*) and for each $A\hookrightarrow B\twoheadrightarrow C$ a collection of morphisms $\delta^n: T^n(C) \to T^n(A)$ fitting into a LES, and for each morphism of SESs $\xi_1\to \xi_1$ the $\delta^n$ fit into commuting squares.
:::

::: {.front card-id="card-f2225028df666042"}
What is a **universal delta functor**?
:::

::: {.back card-id="card-f2225028df666042"}
$\delta = (T^n)$ is universal iff for any other delta functor $(S^n)$ and any morphism $f^0: T^0\to S^0$ of functors there exist lifts $f^i: T^i \to S^i$ which commute with the $\delta^i$.
:::

::: {.front card-id="card-84dafb6fde17d894"}
What is a **homotopy** between maps $f,g: A\to B$ of complexes?
:::

::: {.back card-id="card-84dafb6fde17d894"}
A morphism $k: A \to B[1]$, so $k^i: A^i\to B^{i-1}$, with $f-g = dk + kd$.
:::

::: {.front card-id="card-2c05ae67c19d8075"}
What is a **left exact functor**?
:::

::: {.back card-id="card-2c05ae67c19d8075"}
Additive and $A\hookrightarrow B\twoheadrightarrow C \leadsto FA \hookrightarrow FB \to FC \to \cdots$.
:::

::: {.front card-id="card-9a24470a30061150"}
What are the variance and exactness of hom functors?
:::

::: {.back card-id="card-9a24470a30061150"}
Both are left-exact (just remember $\mathop{\mathrm{\mathbb{R}Hom}}$), $\mathsf{C}(A, {-})$ is covariant and $\mathsf{C}({-}, A)$ is contravariant.
:::

::: {.front card-id="card-d4171256cc976c1e"}
What is an **injective resolution** of $A$?
:::

::: {.back card-id="card-d4171256cc976c1e"}
$A \xrightarrow{{\varepsilon}} I^0 \to I^1 \to \cdots$ an exact complex with $I^j$ injective objects
:::

::: {.front card-id="card-d51a653fa3481330"}
What is an **injective object**?
:::

::: {.back card-id="card-d51a653fa3481330"}
Remembering injectives and projectives:

\begin{tikzcd}
	&&&& P \\
	\\
	A && B && C \\
	\\
	I
	\arrow["{\exists \iff C \text{ projective}}"', dashed, from=1-5, to=3-3]
	\arrow[from=1-5, to=3-5]
	\arrow[hook, from=3-1, to=3-3]
	\arrow[from=3-1, to=5-1]
	\arrow[two heads, from=3-3, to=3-5]
	\arrow["{\exists \iff A \text{ injective}}", dashed, from=3-3, to=5-1]
\end{tikzcd}

:::

::: {.front card-id="card-e37ad2148e34f1cb"}
What is a **(co)effaceable functor**?
:::

::: {.back card-id="card-e37ad2148e34f1cb"}
For each $A$ there is a mono $u: A\to I$ with $F(u) = 0$. Coeffaceable if there is an epi $u: P\to A$ with $F(u) = 0$.
:::

::: {.front card-id="card-6fd5f64c060e98bb"}
Discuss **effaceable functors**.
:::

::: {.back card-id="card-6fd5f64c060e98bb"}
If $T$ is a delta functor and each $T^i$ is effaceable then $T$ is universal. Derived functors computed via injective resolutions form a universal $\delta$ functor.
:::

::: {.front card-id="card-7a05add3225ee133"}
Characterize injective objects in ${}_{\ZZ}\Mod$.
:::

::: {.back card-id="card-7a05add3225ee133"}
Divisible groups. Generally need Baer's criterion.
:::

::: {.front card-id="card-6af26ae228ea633a" tags="math"}
Hom Table
:::

::: {.back card-id="card-6af26ae228ea633a"}
$$
\begin{array}{c|c|c|c}
Hom & Z_m & Z & Q \\\hline
Z_n  & Z_d & 0 & 0 \\\hline
Z   & Z_m & Z & Q \\\hline
Q   & 0  & 0 & Q
\end{array}
$$
:::

::: {.front card-id="card-205ac8f4c3a11ce3" tags="math"}
Tor Table
:::

::: {.back card-id="card-205ac8f4c3a11ce3"}
Rows give the first argument and columns the second; $d \coloneqq \gcd(m, n)$ and $\operatorname{Tor}(A, B) = \operatorname{Tor}(B, A)$.
$$
\begin{array}{c|c|c|c}
\operatorname{Tor}_1 & Z_m & Z & Q \\\hline
Z_n  & Z_d & 0 & 0 \\\hline
Z   & 0  & 0 & 0 \\\hline
Q   & 0  & 0 & 0
\end{array}
$$
The full complex $\operatorname{Tor}_*^\ZZ(V, H) = (V\otimes_\ZZ H) + \operatorname{Tor}_1^\ZZ(V, H)\, t$, e.g. the top-left entry is $\operatorname{Tor}_*^\ZZ(C_n, C_m)$:
$$
\begin{array}{c|c|c|c}
\operatorname{Tor}_*^\ZZ & C_m & \ZZ & \QQ \\\hline
C_n & C_m/nC_m \oplus C_m[n]t = C_d \oplus C_d t & \ZZ/n\ZZ\oplus \ZZ[n]t = C_n \oplus 0t & \QQ/n\QQ\oplus \QQ[n]t = 0\oplus 0t \\\hline
\ZZ & C_m + 0t & \ZZ+ 0t & \QQ+ 0t \\\hline
\QQ & 0 + 0t & \QQ+ 0t & \QQ + 0t
\end{array}
$$
First row: $C_n\otimes_\ZZ A = A/nA$ and $\operatorname{Tor}_1^\ZZ(C_n, A) = A[n]$.

Second row: $\ZZ\otimes_\ZZ A = A$ and $\operatorname{Tor}_1^\ZZ(\ZZ, A) = 0$ since $\ZZ$ is projective.

Third row: $G\otimes_\ZZ\QQ= \QQ\otimes_\ZZ G = 0$ for $G$ a torsion group, $\QQ\otimes_\ZZ\QQ = \QQ$, and $\operatorname{Tor}_1^\ZZ(\QQ, A) = 0$ since $\QQ$ is torsionfree, hence flat.
:::

::: {.front card-id="card-c935c4621c362acc" tags="math"}
Ext Table
:::

::: {.back card-id="card-c935c4621c362acc"}
$$
\begin{array}{c|c|c|c}
Ext & Z_m & Z    & Q \\\hline
Z_n  & Z_d & Z_n   & 0 \\\hline
Z   & 0  & 0    & 0 \\\hline
Q   & 0  & A_p/Q & 0
\end{array}
$$
:::

::: {.front card-id="card-455916a5a5f17b7d"}
The tor complex between $C_n$ and $A$.
:::

::: {.back card-id="card-455916a5a5f17b7d"}
$$\operatorname{Tor}^\ZZ_*(C_n, A) = (A/nA)\cdot t^0 \oplus A[n]\cdot t^1 \oplus \cdots$$
:::

::: {.front card-id="card-9bf5130224135f26"}
The ext complex between $C_n$ and $A$.
:::

::: {.back card-id="card-9bf5130224135f26"}
$$ \operatorname{Ext}^*_\ZZ(C_n, A) = A[n]\cdot t^0 \oplus (A/nA) \cdot t^1 \oplus \cdots$$
:::
