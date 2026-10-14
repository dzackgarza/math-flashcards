---
title: "Research::K3 Surfaces"
---

::: {.front card-id="card-34fab36bd27bc9e8"}
What is the Torelli theorem for K3s?
:::

::: {.back card-id="card-34fab36bd27bc9e8"}
Isomorphisms $\sigma: X^{\prime} \rightarrow X$ are in bijection with the isometries $\sigma^*: H^2(X, \mathbb{Z}) \rightarrow H^2\left(X^{\prime}, \mathbb{Z}\right)$ satisfying $\sigma^*\left(H^{2,0}(X)\right)=H^{2,0}\left(X^{\prime}\right)$ and $\sigma^*\left(\mathcal{K}_X\right)=\mathcal{K}_{X^{\prime}}$.

So a Hodge isometry is induced by an isomorphism exactly when it is effective, i.e. maps the Kahler cone to the Kahler cone; e.g. $-\operatorname{id}$ is a Hodge isometry that is not induced by an automorphism.

Strong Torelli for polarized K3s: if $(X, L)$ and $(X', L')$ are polarized K3s and $\varphi: H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }H^2(X';\ZZ)$ is a Hodge isometry with $\varphi(c_1(L)) = c_1(L')$, then $\varphi = f^*$ for a unique isomorphism $f:X' { \, \xrightarrow{\sim}\, }X$.
:::

::: {.front card-id="card-5bb9c6a0085b74b6"}
Discuss the number of fixed points of a symplectic automorphism with finite order $n$.
:::

::: {.back card-id="card-5bb9c6a0085b74b6"}
Computed by Mukai using the Lefschetz fixed point formula: $n\leq 8$, and ${\sharp} \mathrm{Fix}(\sigma) = 8, 6, 4, 4, 2, 3, 2$ for $n = 2, 3, 4, 5, 6, 7, 8$.

Sketch for $n = p$ prime: take $X\twoheadrightarrow X/\sigma$ and resolve its $A_{p-1}$ singularities to get $Y$.

Write $X' \coloneqq X\setminus \mathrm{Fix}(\sigma)$ and $Y' \coloneqq Y\setminus\widetilde{ \mathrm{Fix}}(\sigma)$, where $\widetilde{ \mathrm{Fix}}(\sigma)$ are the corresponding rational curves. Then $X'\to Y'$ is an unramified $p\dash$to-$1$ cover, so $\chi(X') = p\chi(Y')$.

Each fixed point gives a chain of $p-1$ copies of ${\mathbf{P}}^1$ meeting at $p-2$ points, with $\chi = 2(p-1) - (p-2) = p$.

Combine these to get
$$\chi(X) - {\sharp} \mathrm{Fix}(\sigma) = p\cdot \chi(Y)- p^2\cdot {\sharp} \mathrm{Fix}(\sigma) \implies {\sharp} \mathrm{Fix}(\sigma) = {24\over p+1}$$
since $Y$ is also a K3 and thus $\chi(X) = \chi(Y) = 24$.
:::

::: {.front card-id="card-ae6984def8dbe005"}
Discuss the classification of symplectic actions.
:::

::: {.back card-id="card-ae6984def8dbe005"}
Abelian $G\curvearrowright X$ symplectically (Nikulin), 14 possibilities:

$C_n$ where $n=2,\cdots, 8$.

$C_n^2$ where $n=2,3,4$.

$C_2\times C_n$ where $n=4,6$.

$C_2^3$

$C_2^4$.

Arbitrary finite $G\curvearrowright X$ symplectically (Mukai): $G$ is a subgroup of the Mathieu group $M_{23}$ with at least 5 orbits on $\left\{{1, \cdots, 24}\right\}$, so ${\sharp}G \leq 960$, with equality if $G = M_{20}$.

Xiao: 80 possible groups, maximal size of 960.
:::

::: {.front card-id="card-24176e569cb28a19"}
Give $\dim {\mathbf{P}}(V)$ in terms of $\dim V$.
:::

::: {.back card-id="card-24176e569cb28a19"}
$\dim {\mathbf{P}}(V) = \dim V - 1$.
:::

::: {.front card-id="card-4c8504ee4f1a1bdb"}
Why does every K3 contain a rational curve?
:::

::: {.back card-id="card-4c8504ee4f1a1bdb"}
Bogomolov-Mumford: degenerate to a Kummer which is a product of two special elliptic curves

Construct a configuration of rational curves there

Use irreducibility of $F_{2d}$ to deform to the general K3, possibly making it reducible, but has at least one irreducible.

Use one of the irreducible curves, then specialize to any K3 in $F_{2d}$, the curve can only break into rational curves.
:::

::: {.front card-id="card-303566e8177e0ec5"}
Discuss rational curves on K3s.
:::

::: {.back card-id="card-303566e8177e0ec5"}
Always has at least one.

Any nonzero $D\in \operatorname{Pic}(X)^\mathsf{eff}$ satisfies $D\sim \sum R_i$ for some rational curves.

Over $k=\CC$ $X$ is never uniruled, i.e. no rational curves move.

Conjecture: $X/\overline{k}$ has infinitely many rational curves.
:::

::: {.front card-id="card-d6ef2e2a6407833d"}
What is a Kummer surface?
:::

::: {.back card-id="card-d6ef2e2a6407833d"}
$\widetilde{T/\iota}$ where $T = \CC^2/\Lambda$ is a torus and $\iota$ is an involution with 16 ordinary double point singularities of type $A_1$.
:::

::: {.front card-id="card-2eef1a10735a855d"}
What is the moduli space of all K3s vs projective K3s?
:::

::: {.back card-id="card-2eef1a10735a855d"}
All K3s, including non-projective: $\dcosetr{\Omega}{{\operatorname{O}}(\Lambda_{\mathrm{K3}})}$, 20-dimensional. Its points are the isomorphism classes of K3s, but the quotient is not Hausdorff, since ${\operatorname{O}}(\Lambda_{\mathrm{K3}})$ does not act properly discontinuously on $\Omega$.

Algebraic (projective) K3s: 19-dimensional, since one has to vary periods in the orthogonal complement of an ample class.
:::

::: {.front card-id="card-a3226206edbadebd"}
What are the dimensions of moduli of all and just algebraic Kummer surfaces?
:::

::: {.back card-id="card-a3226206edbadebd"}
All: 4-dimensional

Algebraic: 3-dimensional.
:::

::: {.front card-id="card-8ac3fbe77305abd9"}
What is the dimension of moduli of Enriques surfaces?
:::

::: {.back card-id="card-8ac3fbe77305abd9"}
10-dimensional.
:::

::: {.front card-id="card-d6c6e17a7277bdb7"}
What is the exceptional curve of a blowup of a point in a surface?
:::

::: {.back card-id="card-d6c6e17a7277bdb7"}
A rational $(-1)\dash$curve, so $E^2 = -1$ with $E\cong {\mathbf{P}}^1$.
:::

::: {.front card-id="card-552f2fab724f8aa8"}
What is a minimal surface?
:::

::: {.back card-id="card-552f2fab724f8aa8"}
No rational $(-1)\dash$curves
:::

::: {.front card-id="card-d5bebb5d7791f258"}
What is a ruled surface?
:::

::: {.back card-id="card-d5bebb5d7791f258"}
$\exists S\dashrightarrow C\times {\mathbf{P}}^1$ with $g(C) \geq 0$.
:::

::: {.front card-id="card-f6c1f8a6683ecb7a"}
What is an abelian surface?
:::

::: {.back card-id="card-f6c1f8a6683ecb7a"}
$\CC^2/\Lambda \hookrightarrow{\mathbf{P}}^N$ with $\Lambda$ a rank 4 lattice.
:::

::: {.front card-id="card-4ede286dfe44fe0c"}
What is an Enriques surface?
:::

::: {.back card-id="card-4ede286dfe44fe0c"}
Exactly quotients of K3s by fixed point free involutions.

Smooth projective $Y$ with $2K_Y \sim 0$ and $h^1({\mathcal{O}}_Y) = h^2({\mathcal{O}}_Y) = 0$; the canonical induces an unramified 2-to-1 cover $X\to Y$ for $X$ a K3.
:::

::: {.front card-id="card-2983289eb3e5ba5b"}
What are bielliptic surfaces?
:::

::: {.back card-id="card-2983289eb3e5ba5b"}
Quotients of $E\times E'$ elliptic curves.
:::

::: {.front card-id="card-117b11cbf23727bc"}
What is a special fact about proper elliptic surfaces?
:::

::: {.back card-id="card-117b11cbf23727bc"}
Always have an elliptic fibration.
:::

::: {.front card-id="card-e0924526d2ecf9d1"}
Classify surfaces by $\kappa(S)$.
:::

::: {.back card-id="card-e0924526d2ecf9d1"}
$-\infty$: Rational or ruled.

$0$: Four types; abelian, K3s, Enriques, bielliptic.

$1:$ Proper elliptic.

$2$: General type.
:::

::: {.front card-id="card-db418b0ec438a9a3"}
What's the etymology of K3?
:::

::: {.back card-id="card-db418b0ec438a9a3"}
Named after K2 mountains

Or Kummer, Kahler, Kodaira.
:::

::: {.front card-id="card-a0c53897863d4619"}
Let $X_4$ be the Fermat quartic, what is $K_{X_4}$?
:::

::: {.back card-id="card-a0c53897863d4619"}
By adjunction, $K_{X_4} = (K_{{\mathbf{P}}^3} + X_4)\mathrel{\Big|}_{X_4} = (-4H + 4H)\mathrel{\Big|}_{X_4} = 0$.
:::

::: {.front card-id="card-fffe378c18f2e57c"}
What is the irregularity of $S$?
:::

::: {.back card-id="card-fffe378c18f2e57c"}
$q(S) \coloneqq h^1({\mathcal{O}}_S)$ or $h^0(\Omega^1)$, so $h^{1, 0}$ or $h^{0, 1}$.
:::

::: {.front card-id="card-c4fe37e7e21f6d02"}
What is the geometric genus of $S$?
:::

::: {.back card-id="card-c4fe37e7e21f6d02"}
$h^{0}(\Omega^2)$, so $h^{2, 0}$.
:::

::: {.front card-id="card-a974a6a357f3c50a"}
What is $\pi_1(X_4)$?
:::

::: {.back card-id="card-a974a6a357f3c50a"}
By Lefschetz, $\pi_1(X_4) = \pi_1({\mathbf{P}}^3) = 1$.
:::

::: {.front card-id="card-4dbd0152fa065638"}
Compute $q(X_4)$.
:::

::: {.back card-id="card-4dbd0152fa065638"}
$H_1(X; \ZZ) = \pi_1(X)_\ab= 1$ so $1 = H^1(X;\CC) = H^{0,1 } \oplus H^{1, 0}$ so $q(X_4) = 0$.
:::

::: {.front card-id="card-a83a6fcf30b32ed7"}
Give a birational definition of a K3.
:::

::: {.back card-id="card-a83a6fcf30b32ed7"}
A compact complex surface with $K_S \sim 0$ and $q(S) = 0$.
:::

::: {.front card-id="card-d8dece29c26816e2"}
How does one show a surface is K3?
:::

::: {.back card-id="card-d8dece29c26816e2"}
Show $q(S) = 0$, e.g. using Lefschetz, and show $K_S \sim 0$ e.g. using adjunction.
:::

::: {.front card-id="card-d4ca0d9726924b5c"}
Give several examples of K3s.
:::

::: {.back card-id="card-d4ca0d9726924b5c"}
Any smooth quartic in ${\mathbf{P}}^3$, e.g. $x_0^4 + \cdots + x_3^4\subset {\mathbf{P}}^3$ when $\operatorname{ch}k \neq 2$.

A smooth complete intersection of type $(d_1,\cdots, d_n) \subset {\mathbf{P}}^{n+2}$ with all $d_i\geq 2$ and $\sum d_i = n+3$: the quartic and the types $(2,3)$ and $(2,2,2)$.

Kummer surfaces: the quotient of an abelian surface by the involution $x\mapsto -x$ after resolving 16 singular points.

A double plane: a double cover $X\to {\mathbf{P}}^2$ branched along a smooth curve $C$ of degree 6, using $\pi_* {\mathcal{O}}_X \cong {\mathcal{O}}_{{\mathbf{P}}^2} \oplus {\mathcal{O}}(-3) \implies H^1({\mathcal{O}}_X) = 0$ and $\omega_X \cong \pi^*(\omega_{{\mathbf{P}}^2} \otimes{\mathcal{O}}(3)) \cong {\mathcal{O}}_X$.
:::

::: {.front card-id="card-c9537c6e8b69fd2a"}
Show that the double plane is K3.
:::

::: {.back card-id="card-c9537c6e8b69fd2a"}
Check $K_S = \pi^* K_{{\mathbf{P}}^2} + R$ where $\pi_*(R) = C_6$ and $\pi_*(C_6) = 2R$, use $K_{{\mathbf{P}}^2} = -3H$ and $C_6 = 6H$ to get
$$2K_S = \pi^*(2K_{{\mathbf{P}}^2}) + 2R = \pi^*(2K_{{\mathbf{P}}^2}) + \pi^*(C_6) = \pi^*(-6H) + \pi^*(6H) = 0$$
If $K_S\neq 0$ but $2K_S = 0$, note $h^0(K_S) = 0$.

Check
$$\chi(S) = 2(\chi({\mathbf{P}}^2) - \chi(C_6)) + \chi(R) = 2(3+18)-18 =24$$
using that $\chi(C_6) = 2\cdot 2g$.

Check $\chi({\mathcal{O}}_S) = 2$ and use Noether to conclude $1-h^1({\mathcal{O}}_S) = 2$, a contradiction.
:::

::: {.front card-id="card-f1472e5407f22cc4"}
What is the Noether formula?
:::

::: {.back card-id="card-f1472e5407f22cc4"}
HRR for ${\mathcal{O}}_X$ on a surface $X$:
$$\chi({\mathcal{O}}_X) = {1\over 12}(K_X^2 + \chi(X)) = {1\over 12}(c_1^2 + c_2)$$
where $\chi(X) = c_2$ is the topological Euler characteristic.
:::

::: {.front card-id="card-87f15ed99f31bbce"}
Give an equation for the double plane.
:::

::: {.back card-id="card-87f15ed99f31bbce"}
$S: t^2 = f_6(x_0, x_1, x_2) \subseteq {\mathbf{P}}(3,1,1,1)$ where $C_6 = V(f_6)$.
:::

::: {.front card-id="card-96d7a76cd22ee066"}
What is the involution on an abelian surface? What are its fixed points?
:::

::: {.back card-id="card-96d7a76cd22ee066"}
$A = \CC^2/\Lambda$ with $\operatorname{rank}_\ZZ\Lambda = 4$, take $(x,y)\mapsto (-x,y)$ on $\CC^2$ to get $2(x,y)\in \Lambda$, there are 16 such points and thus 16 $A_1$ singularities in $A/\iota$.
:::

::: {.front card-id="card-862154888a8bb22d"}
What does an $A_1$ singularity look like?
:::

::: {.back card-id="card-862154888a8bb22d"}
Locally the vertex of a cone, rational double points.
:::

::: {.front card-id="card-bc593360b0b42e7f"}
If $A{\circlearrowleft}_\iota$ is the involute on an abelian surface, what is the induced involution on the blowup at the 16 fixed points?
:::

::: {.back card-id="card-bc593360b0b42e7f"}
Write $\left\{{{\left[ { x_0: x_1} \right]}, {\left[ {x, y} \right]} \in {\mathbf{P}}^1 \times \CC^2 \st x_0 y = x_1 x}\right\}$ and send ${\left[ {x_0, x_1} \right]}, {\left[ {x, y} \right]}\mapsto {\left[ { x_0: x_1} \right]}, {\left[ {-x, -y} \right]}$.
:::

::: {.front card-id="card-df4853bcf54d4927"}
What type of curve is the resolution of an $A_1$ singularity?
:::

::: {.back card-id="card-df4853bcf54d4927"}
$D\cong {\mathbf{P}}^1$ with $D^2 = -2$.
:::

::: {.front card-id="card-af30b3367d559ae0"}
What is $\chi({\mathsf{K}}3)$?
:::

::: {.back card-id="card-af30b3367d559ae0"}
$\chi({\mathsf{K}}3) = 24$, all diffeomorphic to the Fermat quartic.
:::

::: {.front card-id="card-941b89a280b25084"}
Describe the lattice $\Lambda_{{\mathsf{K}}3}$.
:::

::: {.back card-id="card-941b89a280b25084"}
The lattice associated to a K3 $X$ is $H^2(X; \ZZ)$ with the intersection pairing
$$\begin{align*}H^2(X; \ZZ){ {}^{ \scriptstyle\otimes_{\ZZ}^{2} }  } &\to \ZZ\\ \alpha\otimes\beta &\mapsto \int_X \alpha\wedge \beta\end{align*}$$
which is nondegenerate and unimodular by Poincare duality. $\Lambda_{{\mathsf{K}}3}$ denotes this lattice structure on (all of) $H^2({\mathsf{K}}3; \ZZ)$:

Rank $22$

Signature $(3, 19)$

Even, unimodular

Isometric to $U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  }$ where

$U = H = \qty{\ZZ^2, \left(\begin{array}{ll}0 & 1 \\1 & 0\end{array}\right)}$ is the hyperbolic plane,

$E_8(-1) =$ unique even unimodular negative-definite lattice of rank 8.
:::

::: {.front card-id="card-e198deda38cb0b29"}
What is the rank of $\Lambda_{{\mathsf{K}}3}$? Proof?
:::

::: {.back card-id="card-e198deda38cb0b29"}
$\chi({\mathsf{K}}3) = 24$ and $p_{{\mathsf{K}}3}(t) = 1 + b_2 t^2 + t^4$ since $b_1 = b_3 = 0$ from $\pi_1({\mathsf{K}}3) = 1$ and $b_0 = b_4 = 1$ from connectedness, thus $\beta_2 = 22$.
:::

::: {.front card-id="card-4f61f550123f13e4"}
Why is $H^2({\mathsf{K}}3; \ZZ)$ torsionfree?
:::

::: {.back card-id="card-4f61f550123f13e4"}
By UCT, $H^2({\mathsf{K}}3;\ZZ)_\tors\cong H_2({\mathsf{K}}3; \ZZ)_\tors$. If $m\tau = 0$ in the latter, construct an unramified cover $i: \tilde S\to S$ with $\chi(\tilde S) = m\chi(S) = 24m$.

Since $i$ is unramified, pulling back a top form yields $K_{\tilde S} \sim 0$.

Noether formula: $\chi({\mathcal{O}}_{\tilde S}) = {1\over 12} (K_{\tilde S}^2 + \chi(\tilde S)) = 2m$.

The LHS is $2-h^1({\mathcal{O}}_{\tilde S}) \leq 2$, the RHS is $\geq 2$, so $m=1$.
:::

::: {.front card-id="card-f64f587ee4649484"}
What is $\operatorname{sgn}\Lambda_{\mathrm{K3}}$?
:::

::: {.back card-id="card-f64f587ee4649484"}
$\operatorname{sgn}\Lambda_{\mathrm{K3}} = \operatorname{sgn}H^2(X; \ZZ) = (3, 19)$.

Proof: write $\operatorname{sgn}\Lambda_{{\mathsf{K}}3} = (s_+, s_-)$, where $s_+ + s_- = b_2(X) = 22$. By the Thom-Hirzebruch index theorem,
$$s_+- s_- = {1\over 3}p_1(X) = {1\over 3}(c_1^2  -2c_2) = {1\over 3}(0-2\cdot24)= -16$$
where $c_1 = c_1({\mathbf{T}}X) = -K_X = 0$ and $c_2 = \chi(X) = 24$.

Combine $s_+ + s_- = 22$ and $s_+ - s_- = -16$ to solve for $(s_+, s_-) = (3, 19)$.
:::

::: {.front card-id="card-6098bf6e2115e6a2"}
Why is $\Lambda_{\mathrm{K3}}$ even?
:::

::: {.back card-id="card-6098bf6e2115e6a2"}
Take an irreducible curve $C\subseteq X$ and use the genus formula:
$$g(C) = 1 + {1\over 2}\qty{C.K_X + C^2} \implies C^2 = 2g-2 \in 2\ZZ$$
:::

::: {.front card-id="card-a11f16d91f65c85e"}
Discuss Milnor's classification.
:::

::: {.back card-id="card-a11f16d91f65c85e"}
Let $\Lambda$ be an indefinite lattice of signature $(s_+, s_-)$ where $s_+,\, s_- > 0$.

If $\Lambda$ is odd the $\Lambda \cong (1){ {}^{ \scriptscriptstyle\oplus^{n} }  } \oplus (-1){ {}^{ \scriptscriptstyle\oplus^{n} }  }$ where $n>0$.

If $\Lambda$ is even then $\Lambda \cong U{ {}^{ \scriptscriptstyle\oplus^{h} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{k} }  }$ where $h > 0$ and $k\geq 0$.
:::

::: {.front card-id="card-2dce7321f873d95b"}
Discuss positivity of $\beta_{{\mathsf{K}}3}({-}, {-})$ on $\omega_X$.
:::

::: {.back card-id="card-2dce7321f873d95b"}
$$\beta(\omega_X, \overline{\omega}_X)=\int_S \omega_X \wedge \overline{\omega}_X = \int_X {\left\lvert {f} \right\rvert}\,dz_1\wedge\,dz_2 \wedge\overline{\,dz_1} \wedge \overline{\,dz_2} > 0$$
Similarly $\beta(\omega_X, \omega_X) = 0$.

If $\beta(\omega_X, H^{1, 1}) = 0$ so $H^{1, 1} \perp_\beta (H^{2, 0} \oplus H^{0,2})$
:::

::: {.front card-id="card-e5204c524e5af7fb"}
Define the period domain $\mathbb{D}$. What is its dimension?
:::

::: {.back card-id="card-e5204c524e5af7fb"}
$$\mathbb{D} = \Omega \coloneqq\left\{{[\omega]\in {\mathbf{P}}(\Lambda_{{\mathsf{K}}3}\otimes_\ZZ\CC) \st\omega^2 = 0,\,\, \omega.\overline{\omega }> 0}\right\}$$
In coordinates that diagonalize the form on $\Lambda_{\mathrm{K3}}\otimes{\mathbf{R}}$ with signature $(3, 19)$,
$$\Omega \cong \left\{{{\left[ {z_0:\cdots:z_{21}} \right]}\in {\mathbf{P}}^{21}\st z_0^2+z_1^2 + z_2^2 - z_3^2 -\cdots - z_{21}^2 = 0,\, {\left\lvert {z_0} \right\rvert}^2 + {\left\lvert {z_1} \right\rvert}^2 + {\left\lvert {z_2} \right\rvert}^2 - {\left\lvert {z_3} \right\rvert}^2 - \cdots - {\left\lvert {z_{21}} \right\rvert}^2 > 0}\right\}$$
which is an open subset of a quadric in ${\mathbf{P}}^{21}$ and thus a 20-dimensional $\CC\dash$manifold.

For a marking $\Phi: H^2(X;\ZZ)\to \Lambda_{\mathrm{K3}}$, the period of $(X, \Phi)$ is $\Phi(\CC\omega_X) \in \Omega$, where $\CC\omega_X = H^{2,0}(X) \in {\mathbf{P}}H^2(X;\CC)$. Surjectivity of the period map (Todorov, Looijenga, Siu): every point of $\Omega$ is the period of some marked K3.

For a marked polarized K3 $(X, \phi)$, drops 1 dimension:
$$\mathbb{D}_{2k} \coloneqq\left\{{[\omega]\in \mathbb{D}\st\omega.h = 0}\right\}$$
where $h\in \Lambda_{{\mathsf{K}}3}$ is a fixed primitive class with $h^2 = 2k$ and $\phi^{-1}(h)\in \NS(X)^\amp$. It is 19-dimensional, with two connected components, each a bounded symmetric domain of type IV.
:::

::: {.front card-id="card-a7590df0a74c3577"}
What is a marking of a K3?
:::

::: {.back card-id="card-a7590df0a74c3577"}
Let $X$ be a K3 surface. A marking is an isometry $\phi: H^2(X; \ZZ) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3}$, where $\Lambda_{{\mathsf{K}}3}$ (also written $L$) is the K3 lattice $U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  }$.
:::

::: {.front card-id="card-2f94dbd7c0c5c56e"}
What is $\dim {\mathbf{P}}^n$.
:::

::: {.back card-id="card-2f94dbd7c0c5c56e"}
$\dim {\mathbf{P}}^n = n$, locally $n$ degrees of freedom: $p \sim {\left[ {1: x_1/x_0:\cdots :x_n/x_0} \right]}$.
:::

::: {.front card-id="card-4bf015e09e65996f"}
What is the dimension of quartics in ${\mathbf{P}}^3$? Up to coordinate changes?
:::

::: {.back card-id="card-4bf015e09e65996f"}
$h^0({\mathcal{O}}_{{\mathbf{P}}^3}(4)) = {4+3\choose 4} = 35$ and its projective dimension is 34.

$\dim \operatorname{PGL}_4(\CC) = 16-1 = 15$

So $34-15 = 19$ moduli.
:::

::: {.front card-id="card-6086a8ffbca5205b"}
What is $h^0({\mathcal{O}}_{{\mathbf{P}}^n}(m))$?
:::

::: {.back card-id="card-6086a8ffbca5205b"}
${m+n\choose m}$.
:::

::: {.front card-id="card-93c8159957201abb"}
What is $\dim \operatorname{PGL}_n(\CC)$?
:::

::: {.back card-id="card-93c8159957201abb"}
$n^2 - 1$.
:::

::: {.front card-id="card-feb6d5dd0d9fef49"}
What are the dimensions of moduli for $S_{2,3}, S_{2,2,2}$, and the double plane $S\to {\mathbf{P}}^2$?
:::

::: {.back card-id="card-feb6d5dd0d9fef49"}
All 19.
:::

::: {.front card-id="card-fed03351b6881aaa"}
What is the ample divisor associated to an embedding?
:::

::: {.back card-id="card-fed03351b6881aaa"}
If $\phi: S\hookrightarrow{\mathbf{P}}^n$, take the hyperplane section $L = \phi(S) \cap H$ for $H$ any hyperplane.
:::

::: {.front card-id="card-cae2e5effcd67939"}
What is the degree of a projective K3?
:::

::: {.back card-id="card-cae2e5effcd67939"}
$L^2 = 2d$ for $L$ a hyperplane section of its projective embedding.

Even since $L = \phi(S) \cap H \in H^2(S; \ZZ) \cap H^{1, 1}(S)$ which is an even lattice.
:::

::: {.front card-id="card-2d755f3e60381c7b"}
What is $L^\perp$?
:::

::: {.back card-id="card-2d755f3e60381c7b"}
$L^\perp \coloneqq\left\{{v\in \Lambda_{\mathrm{K3}}\st{\left\langle {v},~{x} \right\rangle} = 0 \, \forall x\in L}\right\}$.
:::

::: {.front card-id="card-d298f04cbf91b770"}
Describe $[\omega_S]$.
:::

::: {.back card-id="card-d298f04cbf91b770"}
$$[\omega_S]\in \left\{{[\omega] \in {\mathbf{P}}(L^\perp\otimes\CC) \st{\left\lvert {\omega} \right\rvert} > 0,\, \omega^2 = 0 }\right\}$$
Here $\dim L = 1$ so $\dim L^\perp = 20-1 = 19$.
:::

::: {.front card-id="card-4bd67f251195c762"}
What is the degree of $F_4$?
:::

::: {.back card-id="card-4bd67f251195c762"}
Embed $F_4\hookrightarrow{\mathbf{P}}^3$ and slice by a hyperplane to get 4 points, so $L^2 = 4$ and $d=2$.
:::

::: {.front card-id="card-dc1fb84c7694aa1f"}
Describe $c_1(L)$ for a K3 and its relation to $\operatorname{Pic}$ and $\NS$.
:::

::: {.back card-id="card-dc1fb84c7694aa1f"}
Take the exponential SES $\ZZ\hookrightarrow{\mathcal{O}}_S \twoheadrightarrow{\mathcal{O}}_S^{\times}$ to get $\delta^1: H^1(S; {\mathcal{O}}_S^{\times}) \to H^2(S; \ZZ)$, identify $H^1$ with $\operatorname{Pic}$ and $c_1 = \delta^1$.

Get $\operatorname{Pic}^0(S) = \ker c_1$ and $\operatorname{Pic}(S)/\operatorname{Pic}^0(S)\cong \operatorname{im}c_1 = \NS(X)$.
:::

::: {.front card-id="card-8a1535e682e731af"}
Discuss $\NS(X)$ for $X$ a K3.
:::

::: {.back card-id="card-8a1535e682e731af"}
$\operatorname{Pic}^0(X) = 0$ so $\operatorname{Pic}(X) \cong \NS(X)$, the sublattice of $H^{2}(X; \ZZ)$ generated by algebraic cycles. By Lefschetz $(1, 1)$,
$$\operatorname{Pic}(X) = \NS(X) = H^{2, 0}(X)^\perp \cap H^2(X; \ZZ) \subseteq H^2(X; \CC)$$
$\NS(X)\hookrightarrow H^2(X; \ZZ)$ is an even primitive sublattice of $\Lambda_{\mathrm{K3}}$, of rank $\rho(X)$, the Picard number.

If $X$ is projective, $\NS(X)$ is nondegenerate of signature $(1, \rho(X) - 1)$.

$T_X \coloneqq\NS(X)^\perp$ is also a lattice (transcendental).
:::

::: {.front card-id="card-e8ee05a2704a0cc0"}
Describe $\NS(X)$ and $\operatorname{Pic}(X)$ in terms of divisors.
:::

::: {.back card-id="card-e8ee05a2704a0cc0"}
$\NS(X) = \operatorname{CDiv}(X)/\sim$ modulo algebraic equivalence.

$\operatorname{Pic}(X) = \operatorname{CDiv}(X)/\sim$ modulo linear equivalence.

$\CH_k(X) = Z_k(X)/\sim$ modulo rational equivalence
:::

::: {.front card-id="card-e21fb5304f2bb38b"}
What is the Lefschetz 1-1 theorem?
:::

::: {.back card-id="card-e21fb5304f2bb38b"}
There is a surjection $c_1: \operatorname{Pic}(X) \twoheadrightarrow H^{1,1} \cap H^2(X; \ZZ)$.
:::

::: {.front card-id="card-4a998156627e92cf"}
How is the Lefschetz 1-1 theorem used for K3s?
:::

::: {.back card-id="card-4a998156627e92cf"}
$\NS(X) = \operatorname{Pic}(X) = H^{1, 1}(X) \cap H^2(X; \ZZ) = \omega_S^\perp \cap H^2(X;\ZZ)$.
:::

::: {.front card-id="card-8ea4c5bc81520a4a"}
What is the Picard number $\rho(X)$?
:::

::: {.back card-id="card-8ea4c5bc81520a4a"}
$\rho(X) \coloneqq\operatorname{rank}_\ZZ\NS(X)$, where $\NS(X) \coloneqq\operatorname{coker}(\operatorname{Pic}^0(X) \hookrightarrow\operatorname{Pic}(X))$; also written $p(X)$.

For $X$ compact complex,
$$\rho(X) = \operatorname{rank}_\ZZ\operatorname{im}(c_1: \operatorname{Pic}(X) \to H^2(X; \ZZ))$$
If $X$ is Kahler, Lefschetz $(1,1)$ gives $\rho(X) = \operatorname{rank}_\ZZ(H^{1,1}(X) \cap H^2(X; \ZZ))$, so $\rho(X)\leq h^{1,1}(X)$.

For a K3, $\rho(X) = \operatorname{rank}_\ZZ\operatorname{Pic}(X) = \operatorname{rank}_\ZZ\NS(X)$. Since $\NS(X) \leq H^{1, 1}(X)$, there is a bound $\rho(X) \leq 20$ over $\CC$.
:::

::: {.front card-id="card-4179669dbcacc189"}
Discuss $\operatorname{sgn}\NS(X)$ and $\operatorname{sgn}T_X$.
:::

::: {.back card-id="card-4179669dbcacc189"}
$\operatorname{sgn}\NS(X) = (a, b)$ where $a\leq 1$: $\operatorname{sgn}H^2(X;\ZZ) = (3, 19)$, and $H^{2, 0} \oplus H^{0, 2} = \CC\omega_X \oplus \CC\overline{\omega_X}$ gives a real 2-dimensional space $V = \left\langle{\omega_X + \overline{\omega}_X, i(\omega_X - \overline{\omega}_X)}\right\rangle$ where both generators have positive square, and $V\subseteq (H^{1,1})^\perp$.

For $X$ projective, an ample class $L$ with $L^2 > 0$ yields
$$\operatorname{sgn}S_X = \operatorname{sgn}\NS(X) = (1, \rho(X) - 1) \implies \operatorname{sgn}T_X = (2, 20-\rho(X))$$
since they must add up to $(3, 19)$.
:::

::: {.front card-id="card-c4ebdb920576685f"}
What is the transcendental lattice? Its signature?
:::

::: {.back card-id="card-c4ebdb920576685f"}
$T(X) = T_X \coloneqq\NS(X)^\perp \subseteq H^2(X; \ZZ)$, the orthogonal complement of Neron-Severi, where $\NS(X) \simeq \operatorname{Pic}(X) \simeq H^{1,1}(X) \cap H^2(X, \mathbf{Z})$. It is usually considered as an integral Hodge structure.

$T_X \otimes\CC\supseteq H^{2, 0} \oplus H^{0, 2}$, so the periods move in $T_X$: for a polarization $L$, $[\omega_X] \in \left\{{ {\mathbf{P}}(T_X^L\otimes\CC) \st\omega^2 = 0, \omega.\overline{\omega} > 0}\right\}$ where $T_X^L = L^\perp$.

If $X$ is projective:

$\NS(X)$ is nondegenerate, and $T(X)$ is the smallest primitive sublattice of $H^2(X; \ZZ)$ whose complexification contains $H^{2, 0}(X)$.

Signature $(2, 20-\rho(X))$.

$T(X)$ is a polarizable irreducible Hodge structure.

For nonprojective K3s, $T(X) + \NS(X) \subseteq H^2(X; \ZZ)$ need not be direct and $T(X)$ need not be irreducible nor polarizable.
:::

::: {.front card-id="card-9bab5774b88b5564"}
Discuss $\operatorname{Pic}(X)$ for a generic projective K3.
:::

::: {.back card-id="card-9bab5774b88b5564"}
Generically $\operatorname{Pic}(X) = \left\langle{L}\right\rangle_\ZZ$ for $L$ associated to the hyperplane section.
:::

::: {.front card-id="card-cf4969638484b2a6"}
Discuss projective models of K3s.
:::

::: {.back card-id="card-cf4969638484b2a6"}
Saint-Donat 74: if $\mcl\in \operatorname{Pic}(X)$ with $\mcl^2 > 0$ with no base components (so bpf), then the induced embedding $\phi_{{\left\lvert {\mcl} \right\rvert}}:X\to {\mathbf{P}}^N$ where $N = h^0({\mathcal{O}}_X(\mcl)) - 1 = {1\over 2}\mcl^2 -1$ is either

Hyperelliptic: 2-to-1 cover and $\deg \operatorname{im}\phi_{{\left\lvert {\mcl} \right\rvert}} = {1\over 2}\mcl^2$, or

Non-hyperelliptic: birational with $\deg \operatorname{im}\phi_{{\left\lvert {\mcl} \right\rvert}} = \mcl^2$.

$\mcl^2 = 2$ is the double plane.

$\mcl^2 = 4$ non-hyperelliptic is $X\to {\mathbf{P}}^3$ a quartic

$\mcl^2 = 6$ non-hyperelliptic is $X\to {\mathbf{P}}^4$ a complete intersection $(2, 3)$

$\mcl^2 = 8$ non-hyperelliptic is $X\to {\mathbf{P}}^5$ a complete intersection $(2, 2, 2)$
:::

::: {.front card-id="card-dfe46593dd91df51"}
Discuss $\mathop{\mathrm{Aut}}(X)$.
:::

::: {.back card-id="card-dfe46593dd91df51"}
Torelli induces $\mathop{\mathrm{Aut}}(X) \hookrightarrow{\operatorname{O}}(H^2(X; \ZZ))$

Image is effective Hodge isometries: preserves 2-forms and Kahler cones.

Discrete and finitely generated.

Generically trivial when $\operatorname{Pic}(X) = \left\langle{L}\right\rangle_\ZZ$ for $d\neq 1$.

If $\sigma$ preserves an ample class then it must have finite order.
:::

::: {.front card-id="card-9689dd1d644fe056"}
What is a symplectic automorphism?
:::

::: {.back card-id="card-9689dd1d644fe056"}
$\sigma^* \omega_X = \omega_X$, i.e. preserves the symplectic form.

If $\sigma$ has finite order $n > 1$, the coinvariant lattice $(H^2(X;\mathbf{Z})^{\sigma})^\perp$ is negative definite of rank at least $8$ and lies in $\operatorname{NS}(X)$ (Nikulin). For an involution it is $E_8(-2)$. So $\rho(X) \geq 8$, and $\rho(X) \geq 9$ if $X$ is projective, since an invariant ample class is orthogonal to it.
:::

::: {.front card-id="card-bdae5781e53151dc"}
What is the SES involving the symplectic automorphisms of $G\leq \mathop{\mathrm{Aut}}(X)$ a finite subgroup?
:::

::: {.back card-id="card-bdae5781e53151dc"}
$G\curvearrowright H^{2, 0}(X) = \CC\omega_X$ gives $\alpha: G\to \CC^{\times}$, $f\mapsto \alpha(f)$, where $f^* \omega_X = \alpha(f)\omega_X$.

Restrict to its image $\mu_m \subseteq {\CC^{\times}}$ to get a SES
$$G_0 \hookrightarrow G\twoheadrightarrow\mu_m, \qquad G_0 \coloneqq\left\{{f\in G\st f^*\omega_X = \omega_X}\right\}$$
and $G$ is nonsymplectic if $G\ne G_0$.
:::

::: {.front card-id="card-536dcb7d2a4f75ae"}
What are symplectic, non-symplectic, and purely non-symplectic automorphisms?
:::

::: {.back card-id="card-536dcb7d2a4f75ae"}
Let $\omega_X \in H^{2, 0}(X)$ be a nonzero 2-form. An automorphism $g$ of finite order acts by $g^*\omega_X = \alpha(g)\omega_X$ for a root of unity $\alpha(g)$.

Symplectic: $g^*\omega_X = \omega_X$

Non-symplectic: $g^*\omega_X = \alpha(g)\omega_X$ where $\alpha(g)\neq 1$.

Purely non-symplectic: $g^* \omega_X = \alpha(g)\omega_X$ where $\alpha(g) = \zeta_m$ is a *primitive* root of unity of order $m={\left\lvert {g} \right\rvert}$. Some authors call such $\sigma$ of order $n > 1$, with $\sigma^*(\omega_X) = \zeta_n \omega_X$ for a primitive root of unity $\zeta_n$, a non-symplectic automorphism of order $n$.
:::

::: {.front card-id="card-1d14a89c5a2ec472"}
Why are non-symplectic automorphisms important? (Proof sketch)
:::

::: {.back card-id="card-1d14a89c5a2ec472"}
If $X$ admits a finite order non-symplectic automorphism, $X$ is automatically projective.

Proof idea: use Kodaira embedding, find a rational Kahler class.

Use that $H^2(X;\QQ)\hookrightarrow H^2(X;{\mathbf{R}})$ is dense and $\mck$ is open in $H^{1, 1}\otimes{\mathbf{R}}$.

Find $c\in H^2(X; \QQ)$, decompose into $c_{2,0} + c_{1,1} + c_{0, 2}$ in $H^2(X;\CC)$ where $c_{1,1}$ is a real Kahler form, and kill $c_{2,0}, c_{0, 2}$ using the automorphism:

Average to define $h \coloneqq\sum_{i=0}^{{\left\lvert {g} \right\rvert} - 1}(g^*)^i c$ which is $g\dash$invariant.

Use that $g$ respects the Hodge decomposition, and $h_{1,1} = h\in H^2(X;\QQ)$ since $H^{2,0}, H^{0, 2}$ does not contain $g\dash$invariant elements.

By Kodaira embedding, some multiple of $h$ gives the embedding.
:::

::: {.front card-id="card-dff409395fc9e167"}
Give examples of automorphisms of K3s.
:::

::: {.back card-id="card-dff409395fc9e167"}
$\iota: F_4\to F_4$ where ${\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:-x_2:-x_3} \right]}$, symplectic, $\mathrm{Fix}(\iota)$ is 8 points.

$\iota: F_4\to F_4$ where ${\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:\zeta_4 x_2: \zeta_4 x_3} \right]}$.

Set $\omega\coloneqq({\partial}_0 f_4)^{-1}\,dx_2 \wedge \,dx_3$, then $\omega\mapsto -\omega$, so non-symplectic but not purely non-symplectic.
:::

::: {.front card-id="card-6ebe9be6d49b919e"}
Describe symplectic automorphisms locally.
:::

::: {.back card-id="card-6ebe9be6d49b919e"}
Can find local coordinates where $\sigma \in \operatorname{GL}_2(\CC)$ is of the form ${ \begin{bmatrix} {\lambda } & {0}  \\ {0} & {\overline{\lambda}} \end{bmatrix} }$ with $\lambda$ an $n$th root of unity where $n={\left\lvert {\sigma} \right\rvert}$.

Has only isolated fixed points, at most 8.

Nikulin counts ${\sharp} \mathrm{Fix}(\sigma)$ when ${\left\lvert {\sigma} \right\rvert}$ has small prime order.

Quotient has only type $A$ singularities.
:::

::: {.front card-id="card-a464f8a5173c47ca"}
Describe the Lefschetz number of a symplectic automorphism.
:::

::: {.back card-id="card-a464f8a5173c47ca"}
$L(\sigma) \coloneqq\sum (-1)^i \operatorname{Tr}(\sigma^* \curvearrowright H^i({\mathcal{O}}_S) )$.

$L(\sigma)\neq 0 \implies  \mathrm{Fix}(\sigma)\neq\emptyset$

$L(\sigma) = 2$ for a symplectic automorphism.
:::

::: {.front card-id="card-f12fcae19855ecbf"}
Why are symplectic automorphisms important?
:::

::: {.back card-id="card-f12fcae19855ecbf"}
Quotients are again K3.

Not the case for non-symplectic automorphisms!
:::

::: {.front card-id="card-3c62ffad76035cd6"}
What is the Kodaira embedding theorem?
:::

::: {.back card-id="card-3c62ffad76035cd6"}
If $X$ is compact Kahler and $\mcl\in \operatorname{Pic}(X)$ then $\mcl> 0 \iff \mcl\in \operatorname{Pic}(X)^\amp$.

$\impliedby$: if $\mcl{ {}^{ \scriptstyle\otimes_{}^{n} }  } = {\mathcal{O}}_{{\mathbf{P}}^N}(1)\mathrel{\Big|}_X$, the hyperplane bundle is positive since its curvature is the Fubini-Study form.

Positive: $\mcl> 0 \iff \mcl$ admits a metric $h$ such that the associated curvature $\sqrt{-1}\Theta(\mcl, h)$ is a positive 1-1 form.

Comes from the Chern connection induced by ${ \overline{{\partial}}}:\mcl\to \mcl\otimes H^{0, 1}(M)$, namely $\nabla^{0, 1} = { \overline{{\partial}}}$.
:::

::: {.front card-id="card-67d5703c9df61496"}
Give an example of how having too many rational curves can be used in a proof.
:::

::: {.back card-id="card-67d5703c9df61496"}
If ${\left\lvert {\sigma} \right\rvert} = p = 11$ then ${\sharp} \mathrm{Fix}(\sigma) = 2$ yields 2 $A_{10}$ singularities, thus 20 independent $(-2)\dash$curves in $H^2(X; \ZZ)$ which generate a sublattice of signature $(0, 20)$.

This contradicts $\operatorname{sgn}H^2 = (3, 19)$.
:::

::: {.front card-id="card-4afe15399d883416"}
What is an elliptic fibration?
:::

::: {.back card-id="card-4afe15399d883416"}
Proper morphism, connected fibers are smooth genus 1 algebraic curves.

Equivalently, by proper base change, the generic fiber is a smooth genus 1 curve.

E.g. any product of elliptic curves, surfaces with $\kappa(X) = 1$, Enriques surfaces
:::

::: {.front card-id="card-d03dc5ca2d69bd48"}
Discuss $G\in \Fin\Grp\curvearrowright X$ not necessarily symplectically.
:::

::: {.back card-id="card-d03dc5ca2d69bd48"}
Kondo: ${\sharp}G \leq 3840$, proved using isometries of lattices.

Equality if $M_{20}\hookrightarrow G\twoheadrightarrow C_4$.
:::

::: {.front card-id="card-6872241e3d971a34"}
What is the Mathieu group?
:::

::: {.back card-id="card-6872241e3d971a34"}
$M_{20} = A_5\rtimes C_2^4$, order 960.
:::

::: {.front card-id="card-28e56ae7eceebe8f"}
What are the possible orders of CM on an elliptic curve?
:::

::: {.back card-id="card-28e56ae7eceebe8f"}
$2,3,4,6$.
:::

::: {.front card-id="card-74d6b0fc728a1f0c"}
Give an example of an elliptic curve with CM.
:::

::: {.back card-id="card-74d6b0fc728a1f0c"}
$y^2 = x^3 + x$ has CM by $\zeta_3$.
:::

::: {.front card-id="card-0c2e9f05f3de4898"}
Define the invariant lattice.
:::

::: {.back card-id="card-0c2e9f05f3de4898"}
$$H^2(X; \ZZ)^\sigma \coloneqq\left\{{x\in H^2(X;\ZZ) \st\sigma.x = x}\right\}$$
:::

::: {.front card-id="card-7c60a27942fbbd02"}
Give an example of a K3 with maximal Picard rank.
:::

::: {.back card-id="card-7c60a27942fbbd02"}
$X = \mathrm{Kummer}(E_3{ {}^{ \scriptscriptstyle\times^{2} }  })$ where $E_3$ is an elliptic curve with CM by $\zeta_3$.

Satisfies $\rho(X) = 20$.

Given by $X\hookrightarrow{\mathbf{P}}^3$ by $\sum x_i^4 - 12\prod x_i$.
:::

::: {.front card-id="card-4213492c4d415591"}
Discuss $(H^2(X; \ZZ)^\sigma)^\perp$.
:::

::: {.back card-id="card-4213492c4d415591"}
$$(H^2(X; \ZZ)^\sigma)^\perp \subseteq \NS(X) \implies H^2(X;\ZZ)^\sigma \subseteq T_X$$
Nikulin shows $(H^2(X;\ZZ)^\sigma)^\perp$ is a negative definite lattice.
:::

::: {.front card-id="card-764bc15a3a2a3fc6"}
Compute $\operatorname{rank}_\ZZ(H^2(X; \ZZ)^\sigma)^\perp$.
:::

::: {.back card-id="card-764bc15a3a2a3fc6"}
Start with $\operatorname{rank}_\ZZ(H^2(X;\ZZ))^\perp = m(p-1)$.
$$\begin{align*}{\sharp} \mathrm{Fix}(\sigma) &= \chi( \mathrm{Fix}(\sigma)) \\ &= \sum_{i=0}^4 (-1)^i \operatorname{Tr}(\sigma \curvearrowright H^i(X;\ZZ)) \\ &= 2 + \operatorname{Tr}(\sigma \curvearrowright H^2(X;\ZZ)^\sigma) + \operatorname{Tr}(\sigma \curvearrowright( H^2(X;\ZZ)^\sigma) ^\perp) \\ &= 2 + (22 - m(p-1)) - m \\&\implies m = {24\over p+1}\end{align*}$$
using that $\sum_{i=1}^{m-1}\zeta_m^i = -1$.
:::

::: {.front card-id="card-7f7b0e69e329f6b1"}
Give lower bounds on $\rho(X)$ when $\zeta_p\curvearrowright X$.
:::

::: {.back card-id="card-7f7b0e69e329f6b1"}
For a complex projective K3 surface with a symplectic automorphism of prime order $p$, the coinvariant lattice lies in $\operatorname{NS}(X)$, and averaging an ample class gives an additional invariant algebraic class. Hence $\rho(X)\geq1+\operatorname{rank}(H^2(X,\mathbb Z)^{\sigma})^\perp$: for $p=2,3,5,7$, the respective bounds are $9,13,17,19$.
:::

::: {.front card-id="card-ff30a885bc572a3d"}
Why are K3s with automorphisms special?
:::

::: {.back card-id="card-ff30a885bc572a3d"}
Gives a lower bound on $\rho(X)$.
:::

::: {.front card-id="card-b5a57050c6bdb637"}
Compute the dimension of moduli of K3s with an order 3 symplectic automorphism.
:::

::: {.back card-id="card-b5a57050c6bdb637"}
For algebraic complex K3 surfaces, the dimension is $7$. An order-three symplectic automorphism has six fixed points. The Lefschetz formula gives $6=2+\operatorname{tr}(\sigma^*|H^2)$; with eigenvalue multiplicities $a$ for $1$ and $b$ for each primitive cube root, $a-b=4$ and $a+2b=22$. Thus $a=10$, $b=6$, and the coinvariant lattice has rank $12$ in $\operatorname{NS}(X)$. An invariant ample class raises the generic Picard rank to $13$, leaving $20-13=7$ moduli. Families attain this bound (Garbagnati–Sarti, *Symplectic automorphisms of prime order on K3 surfaces*, §5).
:::

::: {.front card-id="card-f729e40766440d54"}
Discuss $\NS(X)$ when $X$ has an order 3 automorphism.
:::

::: {.back card-id="card-f729e40766440d54"}
Always get the Coxeter-Todd lattice, whose points give highest density sphere packing in dimension 12.
:::

::: {.front card-id="card-86474595d92d88df"}
How is a variety defined scheme-theoretically?
:::

::: {.back card-id="card-86474595d92d88df"}
Separated geometrically integral scheme of finite type over $k$.
:::

::: {.front card-id="card-d91e16405fc0a206"}
What is a geometric point?
:::

::: {.back card-id="card-d91e16405fc0a206"}
A morphism $\operatorname{Spec}k \to X$ where $k=\kbar$.
:::

::: {.front card-id="card-3154955e247dbc25"}
What is a geometric fiber?
:::

::: {.back card-id="card-3154955e247dbc25"}
The fiber over a geometric point, i.e. for $f:X\to Y$, the fiber product with $p_i: \operatorname{Spec}k \to Y$ given by $X \underset{\scriptscriptstyle {Y} }{\times}\operatorname{Spec}k$.
:::

::: {.front card-id="card-2290d9ce19976340"}
What is a geometrically integral scheme?
:::

::: {.back card-id="card-2290d9ce19976340"}
Idea: prevents becoming reduced or reducible after a field extension.

The structure morphism $f: X\to \operatorname{Spec}k$ is geometrically integral, i.e.for all geometric points $p_i: \operatorname{Spec}L \to \operatorname{Spec}k$ the fiber $X \underset{\scriptscriptstyle {\operatorname{Spec}k} }{\times} \operatorname{Spec}L$ is integral.

Thm: geometrically integral iff geometrically reduced and geometrically irreducible.
:::

::: {.front card-id="card-26a43a92a834b431"}
When is a variety smooth?
:::

::: {.back card-id="card-26a43a92a834b431"}
If $\Omega_{X}$ is locally free of rank $\dim X$

Equivalently, $X \underset{\scriptscriptstyle {k} }{\times}\kbar$ is a regular scheme.
:::

::: {.front card-id="card-dec2dfa1d9efa061"}
What is an **algebraic** K3 surface?
:::

::: {.back card-id="card-dec2dfa1d9efa061"}
Smooth complete variety $X$ over a field $k$, $\dim X = 2$, where $\omega_{X/k}\cong {\mathcal{O}}_X$ and $H^1({\mathcal{O}}_X) = 0$.

Interpret $q(X) \coloneqq h^{0, 1}(X) = h^1({\mathcal{O}}_X)$ as the irregularity, so the last condition is $q(X) = 0$.
:::

::: {.front card-id="card-b314c9e25a945fe6"}
Discuss the cotangent sheaf of a K3.
:::

::: {.back card-id="card-b314c9e25a945fe6"}
Locally free of rank 2, $\Omega_X^2 = \operatorname{det}\Omega_X = \omega_X \cong {\mathcal{O}}_X$.

Carries an algebraic symplectic structure $(\Omega_X){ {}^{ \scriptscriptstyle\times^{2} }  } \to {\mathcal{O}}_X$ inducing an isomorphism ${\mathbf{T}}_X\cong \Omega_X {}^{ \vee }\coloneqq\mathop{\mathcal{H}\! \mathit{om}}(\Omega_X, {\mathcal{O}}_X) \cong \Omega_X$.
:::

::: {.front card-id="card-6f292d586b8e981e"}
When is a K3 surface projective?
:::

::: {.back card-id="card-6f292d586b8e981e"}
Always: any smooth complete surface is projective.
:::

::: {.front card-id="card-e3ada979046f3479"}
Why is a smooth quartic a K3?
:::

::: {.back card-id="card-e3ada979046f3479"}
If $X \subseteq {\mathbf{P}}^3$ then take the LES for ${\mathcal{O}}_{{\mathbf{P}}^3}(-4) \hookrightarrow{\mathcal{O}}_{{\mathbf{P}}^3} \twoheadrightarrow{\mathcal{O}}_X$ and use that $H^1({\mathcal{O}}_{{\mathbf{P}}^3}) = H^2({\mathcal{O}}_{{\mathbf{P}}^3}(-4)) = 0$ to conclude $H^1({\mathcal{O}}_X) = 0$.

The adjunction formula yields $\omega_X = \omega_{{\mathbf{P}}^3}\otimes{\mathcal{O}}(4)\mathrel{\Big|}_X \cong {\mathcal{O}}_X$.
:::

::: {.front card-id="card-23af48fd70c389b1"}
For $L_1, L_2\in \operatorname{Pic}X$, define $L_1.L_2$.
:::

::: {.back card-id="card-23af48fd70c389b1"}
The coefficient of $ab$ in $\chi(L_1^1\otimes L_2^b)$.
:::

::: {.front card-id="card-19a2b52a40458ae7"}
Compute $L_1.{\mathcal{O}}(C)$ for $C$ an integral curve.
:::

::: {.back card-id="card-19a2b52a40458ae7"}
$\deg L_2 \mathrel{\Big|}_C$.
:::

::: {.front card-id="card-82d6364cd4704d94"}
Compute ${\mathcal{O}}(C_1).{\mathcal{O}}(C_2)$ for $C_1, C_2$ integral curves intersecting at finitely many points.
:::

::: {.back card-id="card-82d6364cd4704d94"}
$$\sum_{i=x \in C_1 \pitchfork C_2} \dim_k {{\mathcal{O}}_{X, x}\over \left\langle{f_{1, x}, f_{2, x}}\right\rangle }$$
:::

::: {.front card-id="card-1575109157d00592"}
Discuss $L.{\mathcal{O}}(C)$ when $L$ is ample.
:::

::: {.back card-id="card-1575109157d00592"}
Always positive: $L_1.C = \deg L_1\mathrel{\Big|}_C > 0$.
:::

::: {.front card-id="card-dcbe851d26a74ffa"}
What is Riemann-Roch for line bundles on surfaces?
:::

::: {.back card-id="card-dcbe851d26a74ffa"}
$\chi(L) - \chi({\mathcal{O}}_X) = {1\over 2} (L.L \otimes\omega_X {}^{ \vee })$.
:::

::: {.front card-id="card-aa5478294141e3a4"}
Define the Neron-Severi group.
:::

::: {.back card-id="card-aa5478294141e3a4"}
$S_X \coloneqq\NS(X) \coloneqq\operatorname{Pic}(X) / \operatorname{Pic}^0(X) = \operatorname{coker}(\operatorname{Pic}^0(X) \hookrightarrow\operatorname{Pic}(X))$: line bundles modulo those algebraically equivalent to zero.

For $X$ compact Kahler, $c_1$ identifies $\NS(X)$ with $\operatorname{im}c_1 \subseteq H^2(X; \ZZ)$, and by Lefschetz $(1,1)$ this image is the set of integral classes of type $(1,1)$. For a K3, $H^2(X;\ZZ)$ is torsionfree, so
$$\NS(X) = H^{1, 1}(X) \cap H^{2}(X; \ZZ)\subseteq H^2(X; \CC)$$
:::

::: {.front card-id="card-4f556cf6edfaace8"}
What does it mean for a line bundle $L$ to be numerically trivial?
:::

::: {.back card-id="card-4f556cf6edfaace8"}
$L. \mcl= 0$ for all $\mcl\in \operatorname{Pic}(X)$, e.g. any $L\in \operatorname{Pic}^0(X)$.
:::

::: {.front card-id="card-95620d7653e21270"}
What is $\mathrm{Num}(X)$?
:::

::: {.back card-id="card-95620d7653e21270"}
$\operatorname{Pic}(X)/\operatorname{Pic}(X)^\tau$. quotienting by the subgroup of numerically trivial line bundles.

A ${}_{\ZZ}\Mod$ with a nondegenerate symmetric integral pairing.
:::

::: {.front card-id="card-3036ebb4d8e6a374"}
What is the signature of the intersection form on $\operatorname{Num}(X)$?
:::

::: {.back card-id="card-3036ebb4d8e6a374"}
$(1, p(X) - 1)$ for $p(X)$ the Picard number, so its real form diagonalizes to $(1, -1,\cdots, -1)$.
:::

::: {.front card-id="card-788afed38cc8d30e"}
What is $\chi({\mathcal{O}}_X)$ for a K3?
:::

::: {.back card-id="card-788afed38cc8d30e"}
2: $h^0({\mathcal{O}}_X) = h^1({\mathcal{O}}_X) = 0$ by definition, and by Serre duality $h^2({\mathcal{O}}_X) = h^0(\omega_X) = 1$.
:::

::: {.front card-id="card-91364e66978ac689"}
What is $\pi_1^\text{ét}(X)$ for a K3?
:::

::: {.back card-id="card-91364e66978ac689"}
Trivial: if $Y\to X$ is an irreducible finite etale cover of degree $d$ then $Y$ is a smooth complete surface, $\omega_Y \cong{\mathcal{O}}_Y$, and $\chi({\mathcal{O}}_Y) = d\chi({\mathcal{O}}_X) =2d$ with $h^0({\mathcal{O}}_Y) = h^2({\mathcal{O}}_Y) = 1$.

Thus $2-h^1({\mathcal{O}}_Y) = 2d \implies d=1$.
:::

::: {.front card-id="card-04741fc87ffccbcc"}
What is the statement of RR for $L\in \operatorname{Pic}(X)$ for $X$ a K3? How does this change if $L$ is ample?
:::

::: {.back card-id="card-04741fc87ffccbcc"}
$\chi(L) = {1\over 2}L^2 + 2$.

If $L$ is ample then $H^1(L) = 0$ so the LHS is $h^0(L)$.
:::

::: {.front card-id="card-97124755dd1c9baa"}
Give an equivalent characterization of when a line bundle is trivial.
:::

::: {.back card-id="card-97124755dd1c9baa"}
Both $H^0(L)$ and $H^0(L {}^{ \vee })$ are nontrivial.
:::

::: {.front card-id="card-87f4808bdfeea791"}
What is the Hirzebruch-Riemann-Roch theorem?
:::

::: {.back card-id="card-87f4808bdfeea791"}
$\chi(\mcf) = \int {\mathrm{ch}}(\mcf)\operatorname{Td}(X) = {\mathrm{ch}}_2(\mcf) + 2\operatorname{rank}(\mcf)$.
:::

::: {.front card-id="card-8416a0db82d96015"}
What is $c_2(X)$ for a K3?
:::

::: {.back card-id="card-8416a0db82d96015"}
24 by the Noether formula.
:::

::: {.front card-id="card-dca3b01c137d5f80"}
What is the Hodge diamond of a K3?
:::

::: {.back card-id="card-dca3b01c137d5f80"}
For a complex K3 surface, $q=0$, $p_g=1$, and $h^{1,1}=20$.

$h^{p, q}(X) = 1$ for the corners: $h^{0,0} = h^{2,2} = 1$ and $h^{2,0} = h^{0,2} = 1$ since $\Omega^2_X\cong{\mathcal{O}}_X$. $h^{0, 1}(X) = h^{1,0}(X) = 0$, and $h^{2,1} = h^{1,2} = 0$ by Serre duality.

By HRR, Serre duality, and $\Omega_X \cong {\mathbf{T}}_X$,
$$2 h^0\left(\Omega_X\right)-h^1\left(\Omega_X\right)=\operatorname{ch}_2\left(\Omega_X\right)+4=4-\mathrm{c}_2\left(\Omega_X\right)=-20$$
so $h^1(\Omega_X) = 20$ since $h^0(\Omega_X) = h^{1,0}(X) = 0$. The Hodge diamond is
$$\begin{matrix}&&1&&\\&0&&0&\\1&&20&&1\\&0&&0&\\&&1&&\end{matrix}.$$
:::

::: {.front card-id="card-758927d12fcaa059"}
Discuss $h^0({\mathbf{T}}_X)$ for $X$ a K3.
:::

::: {.back card-id="card-758927d12fcaa059"}
$h^0({\mathbf{T}}_X) = h^0(\Omega_X)= 0$ using the isomorphism ${\mathbf{T}}_X\cong \Omega_X$. So no global vector fields.
:::

::: {.front card-id="card-10b63f4aeb034057"}
Discuss GAGA
:::

::: {.back card-id="card-10b63f4aeb034057"}
To any $X\in\Sch^{\mathrm{ft}}_{/ {\CC}}$ there exist $X^\an\to X$ a morphism of ringed spaces from an analytic space where the points of $X^\an$ correspond to the closed points of $X$ and there is an induced equivalence $\Coh(X) { \, \xrightarrow{\sim}\, }\Coh(X^\an)$.
:::

::: {.front card-id="card-cadd5037b23ac4b9"}
What is a **complex** K3 surface?
:::

::: {.back card-id="card-cadd5037b23ac4b9"}
A compact connected complex manifold, $\dim X = 2$, with $\Omega^2_X \cong {\mathcal{O}}_X$ and $h^1({\mathcal{O}}_X) = 0$.

If $X$ is an algebraic K3 then $X^\an$ is a (projective) complex K3.
:::

::: {.front card-id="card-8d81d919296f7a7a"}
Why is $X^\an$ projective when $X$ is an algebraic K3?
:::

::: {.back card-id="card-8d81d919296f7a7a"}
GAGA: the ideal sheaf $I$ of $X\subseteq {\mathbf{P}}^n$ is coherent analytic and thus isomorphic to an algebraic ideal sheaf.
:::

::: {.front card-id="card-ed2a3b29ee9828a1"}
Are all complex K3s projective?
:::

::: {.back card-id="card-ed2a3b29ee9828a1"}
No: most complex tori $X=\CC^2/\Gamma$ are not.
:::

::: {.front card-id="card-f863478d0d916b41"}
Discuss $H^*_\sing(X)$ for a K3.
:::

::: {.back card-id="card-f863478d0d916b41"}
Take the LES $H^1(X;\ZZ) \to H^1(X;{\mathcal{O}})\to H^1(X;{\mathcal{O}}^{\times})$ to show $H^1(X;\ZZ) = H^3(X;\ZZ) = 0$ mod torsion and $H^0(X;\ZZ) = H^4(X;\ZZ) = \ZZ$. The only other nontrivial group is $H^2(X; \ZZ)$.
:::

::: {.front card-id="card-c9d0de8eb14f950a"}
Discuss $H^2(X; \ZZ)$
:::

::: {.back card-id="card-c9d0de8eb14f950a"}
Torsionfree, since $0\to \operatorname{Pic}(X) \to H^2(X;\ZZ) \to H^2(X; {\mathcal{O}})$ using $\operatorname{Pic}(X)\cong H^1(X; {\mathcal{O}}^{\times})$; since $H^2(X;{\mathcal{O}})\cong \CC$ and $\operatorname{Pic}(X)$ are torsionfree, so is $H^2$. The intersection form on $\operatorname{Pic}(X)$ corresponds to the intersection form on $H^2$ under this embedding.

$\operatorname{rank}_\ZZ H^2 = 22$ since $e(X) = c_2(X) = 24$ and $b_2(X) = 22$, and this defines a unimodular lattice ${\mathbf{E}}_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  } \oplus U{ {}^{ \scriptscriptstyle\oplus^{3} }  }$.
:::

::: {.front card-id="card-17d51c123ac377f3"}
What is the Hodge-Frolicher spectral sequence?
:::

::: {.back card-id="card-17d51c123ac377f3"}
$$H^q(X; \Omega^p_X) \Rightarrow H^{p+q}(X; \CC)$$
:::

::: {.front card-id="card-535af4290aac8dee"}
Discuss bounds on $p(X)$.
:::

::: {.back card-id="card-535af4290aac8dee"}
By Lefschetz $(1,1)$ one has $\operatorname{Pic}(X) \cong H^2(X;\ZZ)\cap H^{1, 1}(X)$ and $(H^2(X;\ZZ)\cap H^{1, 1}(X))\otimes\CC\subseteq H^1(\Omega_X)$ which is a 20-dimensional space, so $p(X) \leq 20$. Each $0\leq i\leq 20$ is obtained.
:::

::: {.front card-id="card-4878049257d25b28"}
Give a bundle-theoretic condition for projectivity of surfaces.
:::

::: {.back card-id="card-4878049257d25b28"}
If $X$ is a smooth compact complex surface, $X$ is projective iff $\exists L\in \operatorname{Pic}(X)$ with $L^2 > 0$.
:::

::: {.front card-id="card-e9df1180e0586b98"}
How is $\rho(X)\leq 22$ proved for K3s over positive characteristic fields?
:::

::: {.back card-id="card-e9df1180e0586b98"}
Take the LES in $H^*_\text{ét}$ for the Kummer sequence $\mu_n\hookrightarrow{\mathbf{G}}_m\twoheadrightarrow{\mathbf{G}}_m$ for $n$ prime to $p$, use $\operatorname{Pic}(X) \cong H^1(X;{\mathbf{G}}_m)$ to show $H^1_\text{ét}(X; \mu_n) = k^{\times}/(k^{\times})^n$.

Use $k$ separably closed and duality to get $H^1_\text{ét}(X; { \ZZ_{\widehat{\ell}} }) = H^3(X;{ \ZZ_{\widehat{\ell}} }) = 0$.

Use $c_2(X) = 24$ to conclude $\operatorname{rank}_\ZZ H^2_\text{ét}(X; { \ZZ_{\widehat{\ell}} }) = 22$.
:::

::: {.front card-id="card-3617dcb5de3156d3"}
How is $c_1$ realized as a morphism:
:::

::: {.back card-id="card-3617dcb5de3156d3"}
$c_1: \operatorname{Pic}(X) \to H^2_\text{ét}(X; { \ZZ_{\widehat{\ell}} }(1))$.
:::

::: {.front card-id="card-e1c263264e18ad22"}
What is an elliptic surface?
:::

::: {.back card-id="card-e1c263264e18ad22"}
$\pi:X\to {\mathbf{P}}^1$ surjective with generic fiber a smooth elliptic curve. Admit Weierstrass normal forms.
:::

::: {.front card-id="card-f0ed65710f2df6a3"}
Define the linear system ${\left\lvert {L} \right\rvert}$ for $L\in \operatorname{Pic}(X)$.
:::

::: {.back card-id="card-f0ed65710f2df6a3"}
${\mathbf{P}}H^0(L)$ or all $L'\in \operatorname{Div}(X)^\mathsf{eff}$ with $L'\sim L$ linearly equivalent.
:::

::: {.front card-id="card-40db4f8dd3f0114c"}
Define the base locus $\mathrm{Bs}{\left\lvert {L} \right\rvert}$.
:::

::: {.back card-id="card-40db4f8dd3f0114c"}
The maximal closed subscheme of $X$ contained in every $D\in {\left\lvert {L} \right\rvert}$.

Equivalently
$$\mathrm{Bs}{\left\lvert {L} \right\rvert} = \bigcap_{s\in H^0(L)} Z(s)$$
:::

::: {.front card-id="card-bee54f0820921fff"}
When does $L$ induce a rational map?
:::

::: {.back card-id="card-bee54f0820921fff"}
If $h^0(L) > 1$, inducing $\phi_L: X\dashrightarrow{\mathbf{P}}H^0(L) {}^{ \vee }$ regular on $X\setminus\mathrm{Bs}{\left\lvert {L} \right\rvert}$.
:::

::: {.front card-id="card-8516e525f30da86c"}
What is the fixed-mobile decomposition $L = M + F$ for $L\in \operatorname{Pic}(X)$?
:::

::: {.back card-id="card-8516e525f30da86c"}
$F$ is the 1-dimensional part of $\mathrm{Bs}{\left\lvert {L} \right\rvert}$.

$M\coloneqq L(-F)$ is the mobile part, is nef, satisfies $M^2 \geq 0$. Has a finite set of base points, contains the zero-dimensional locus of $\mathrm{Bs}{\left\lvert {L} \right\rvert}$.
:::

::: {.front card-id="card-8a3313b45abc3005"}
What is a hyperelliptic curve in the context of K3s?
:::

::: {.back card-id="card-8a3313b45abc3005"}
$C$ with a degree 2 morphism $C\to {\mathbf{P}}^1$.

Usually $g(C) \geq 2$, $\omega_C$ is bpf, and the canonical embedding $\phi_{\omega_C}$ is non-constant.
:::

::: {.front card-id="card-ddfdea50da4dc550"}
Are there hyperelliptic curves $C$ with $g(C) > 2$?
:::

::: {.back card-id="card-ddfdea50da4dc550"}
Yes, and $C$ is hyperelliptic iff $\omega_C$ is not hyperelliptic.
:::

::: {.front card-id="card-ded86dc8399712bb"}
What is a projectively normal morphism?
:::

::: {.back card-id="card-ded86dc8399712bb"}
The restriction $H^0\left(\mathbf{P}^{g-1}, \mathcal{O}(k)\right) \longrightarrow H^0\left(C, \omega_C^k\right)$ is surjective for all $k$.
:::

::: {.front card-id="card-413f20af833422e3"}
What is the adjunction formula for a curve $C$ on a surface $X$?
:::

::: {.back card-id="card-413f20af833422e3"}
$\omega_C = (\omega_X \otimes{\mathcal{O}}(C))\mathrel{\Big|}_C$.
:::

::: {.front card-id="card-6123728edc5fc074"}
What is the geometric genus of a reduced curve?
:::

::: {.back card-id="card-6123728edc5fc074"}
$g(\tilde C)$ where $\nu:\tilde C\to C$ is the normalization.
:::

::: {.front card-id="card-0386f3f67ba2881f"}
How are geometric and arithmetic genus related for a reduced curve?
:::

::: {.back card-id="card-0386f3f67ba2881f"}
$p_a(C) = g(C) + h^0(\nu_* {\mathcal{O}}_{\tilde C}/{\mathcal{O}}_C)$ where the latter sheaf is concentrated on $C^\sing$.
:::

::: {.front card-id="card-696f61d1ecfeb96a"}
Give a lower bound for $C^2$ for an integral curve on a K3.
:::

::: {.back card-id="card-696f61d1ecfeb96a"}
$C^2 \geq -2$, using
$$2 p_a(C)-2=\left(C . \omega_X \otimes \mathcal{O}(C)\right)\implies 2 p_a(C)-2=(C)^2$$
and $p_a(C) \geq 0$.
:::

::: {.front card-id="card-d659e54d9492db61"}
Discuss curves on a K3.
:::

::: {.back card-id="card-d659e54d9492db61"}
By adjunction, $C^2\geq -2$. Automatically smooth, since $g(C) \leq p_a(G)$ with equality iff $C$ is smooth, and here $p_a(C) = p_g(C) = 0$. Any $(-2)\dash$curve is integral.
:::

::: {.front card-id="card-ee039062cee28f38"}
When is a line bundle on a K3 ample?
:::

::: {.back card-id="card-ee039062cee28f38"}
$L$ is ample iff $L\in \mcc_X \subset \NS(X)_{\mathbf{R}}$ (the positive cone) and $(L.C) > 0$ for every smooth rational curve $C\cong {\mathbf{P}}^1 \subseteq X$.
:::

::: {.front card-id="card-34840685843858f5"}
What is a nef line bundle $L$ for a complete variety $X$?
:::

::: {.back card-id="card-34840685843858f5"}
$(L.C) > 0$ for all closed curves.
:::

::: {.front card-id="card-701972d5f4fef18e"}
What does it mean for a line bundle on a surface to be big and nef? Why care?
:::

::: {.back card-id="card-701972d5f4fef18e"}
$L^2 > 0$ and $L$ is nef.

Weaker than ample, but results for ample often still hold for just big and nef. Note that $L^2 > 0$ is not quite the right definition of "big" alone.

Big and nef on a K3 implies effective.
:::

::: {.front card-id="card-6b6592219edcf96d"}
What is the generalization of Kodaira vanishing for projective surfaces (Kodaira-Ramanujam vanishing theorem)?
:::

::: {.back card-id="card-6b6592219edcf96d"}
For $X$ a smooth projective surface over $\operatorname{ch}k = 0$, if $L$ is big and nef then
$$H^{> 0}(L\otimes\omega_X) = 0$$
Since $H^1(\omega_X\otimes L) {}^{ \vee }\cong H^1(L {}^{ \vee })$ by Serre duality, this is a vanishing theorem for $L {}^{ \vee }$ with sufficient "positivity".
:::

::: {.front card-id="card-ff488447828ff571"}
Does Kodaira vanishing hold in positive characteristic?
:::

::: {.back card-id="card-ff488447828ff571"}
Generally no, see Mumford's normal projective surface as a counterexample, or Raynaud finds for any smooth projective surface $X$ over $k=\kbar$ an $L\in \operatorname{Pic}(X)$ with $H^1(L\otimes\omega_X) \neq 0$.

However it *does* hold for K3s, using $H^1({\mathcal{O}}_X) = 0$ and any big and nef $L$ on a K3 is effective. This is explained by Deligne-Illusie for surfaces that lift to characteristic zero (which K3s do).
:::

::: {.front card-id="card-38e09a8919b928e1"}
Discuss $L^2$ and $h^0(L)$ for $L = {\mathcal{O}}_X(C)$, $C$ a curve on a K3 $X$.
:::

::: {.back card-id="card-38e09a8919b928e1"}
Let $L= {\mathcal{O}}_X(C)$ for $C\subseteq X$ a smooth irreducible curve of genus $g$ on a K3 $X$, then
$$L^2 = 2g-2,\qquad h^0(L) = g+1$$
Use adjunction to prove the first, and RR + Serre duality + $H^0({ \left.{{L}} \right|_{{C}} }) \cong H^0(\omega_C)$ and the SES $H^0(X; {\mathcal{O}}_X) \hookrightarrow H^0(X; L)\twoheadrightarrow H^0(C; { \left.{{L}} \right|_{{C}} })$.
:::

::: {.front card-id="card-f155d869dc3cff26"}
Discuss projective embeddings of curves in K3s.
:::

::: {.back card-id="card-f155d869dc3cff26"}
For $C\subseteq X$ smooth irreducible with $g(C) \geq 1$, $L\coloneqq{\mathcal{O}}(C)$ is bpf and $\phi_L: X\to {\mathbf{P}}^g$ restricts to the canonical embedding $C\to {\mathbf{P}}^{g-1}$.

For $g=2$, $C$ is hyperelliptic so $C\to {\mathbf{P}}^1$ is degree 2. Since $L^2 = 2$ and $L = \phi_L^* {\mathcal{O}}(1)$, $\phi_L$ is degree 2, so $X$ is a double cover of ${\mathbf{P}}^2$ over a degree 6 curve.
:::

::: {.front card-id="card-a289e10e50b64ad3"}
Discuss the analog of Noether's theorem on projective normality of non-hyperelliptic curves.
:::

::: {.back card-id="card-a289e10e50b64ad3"}
For $C\subseteq X$ irreducible smooth non-hyperelliptic with $g(C) > 2$ on a K3 $X$, $L\coloneqq{\mathcal{O}}(C)$ is projectively normal, so $\phi_L^*$ defines surjections $H^0({\mathbf{P}}^g; {\mathcal{O}}(k)) \twoheadrightarrow H^0(X; L^k)$ for all $k$.
:::

::: {.front card-id="card-3cc4412c0c60050d"}
Discuss ampleness of line bundles on abelian varieties.
:::

::: {.back card-id="card-3cc4412c0c60050d"}
If $L\in \operatorname{Pic}(A)$ is ample in any characteristic, $L^k$ is very ample for $k\geq 3$ independent of $\dim A$.
:::

::: {.front card-id="card-6c6d0f89580f2dfc"}
Discuss projective embeddings of K3s in arbitrary characteristic.
:::

::: {.back card-id="card-6c6d0f89580f2dfc"}
If $C\subseteq X$ is smooth irreducible and $L\coloneqq{\mathcal{O}}(C)$, then for $k\geq 2, g>2$ or $k\geq 3, g=2$ the induced embedding $\phi_{L^k}:X\to {\mathbf{P}}^n, n= k^2(g-1)+1$ is birational onto its image.
:::

::: {.front card-id="card-44659fa94f8ffffe"}
What is Fujita's conjecture?
:::

::: {.back card-id="card-44659fa94f8ffffe"}
For $L\in \operatorname{Pic}(X)^\amp$ for $X$ smooth projective over $\CC$, $L^k\otimes\omega_X$ is

Globally generated for $k\geq \dim(X) + 1$ and

Very ample for $k\geq \dim(X) + 2$.

True for surfaces, a stronger version is true for K3s.
:::

::: {.front card-id="card-504dac3b1ca18677"}
Discuss $\operatorname{Pic}(X)^\vamp$ for $X$ a K3.
:::

::: {.back card-id="card-504dac3b1ca18677"}
If $L$ is ample and bpf, the $L^k$ is very ample for $k\geq 3$.

Consequence of a general result of Mumford, see 439.Thm.3.
:::

::: {.front card-id="card-b2f808dcef295d55"}
Discuss big and nef line bundles $L$ on a K3.
:::

::: {.back card-id="card-b2f808dcef295d55"}
$H^1(L) = 0$ by the Kodaira-Ramanujam vanishing theorem.

If $C$ is an irreducible curve with $C^2 > 0$, then ${\mathcal{O}}(C)$ is big and nef.

Decompose $L = M + F$ into its mobile and fixed parts. If $M$ is big, then $L$ is bpf and $F$ is trivial.

If $L$ is not bpf then $L = {\mathcal{O}}(mE + C)$ with $E$ smooth elliptic, $C\cong{\mathbf{P}}^1$, $E.C = 1$, and $m\geq 2$.
:::

::: {.front card-id="card-7eed0c440c3acc28"}
What is Ramanujam's lemma?
:::

::: {.back card-id="card-7eed0c440c3acc28"}
If $C$ is 1-connected and $H^1({\mathcal{O}}_X) = 0$, then $H^1({\mathcal{O}}_X(-C)) =0$.

In characteristic zero, can drop $H^1({\mathcal{O}}_X) = 0$ assumption.
:::

::: {.front card-id="card-b87e35a4eb78f2b0"}
Let $L\in \operatorname{Pic}(X)$ be big and nef. Show that ${\left\lvert {L} \right\rvert}$ is bpf.
:::

::: {.back card-id="card-b87e35a4eb78f2b0"}
Decompose $L = M + F$.

Mobile $\implies$ effective $\implies$ nef, so $M^2 \geq 0$.

If $M^2 > 0$, then $M$ is big and nef so $L$ has at most isolated base points.

Check $H^1(X; M) = 0 = H^1(X; L)$ so $\chi(M) = h^0(M) = h^0(L) = \chi(L)$.

By RR, $M^2 = L^2$, so $2(M.F) + F^2 = 0$

$L$ nef $\implies (M.F) + F^2 = L.F\geq 0 \implies M.F = F^2 = 0$

By RR on $F\neq 0$, reach a contradiction $1 = h^0(F) \geq \chi(F)$, so $F=0$.|
:::

::: {.front card-id="card-3cb9dc2bc3da922a"}
What is the Base Point Free theorem?
:::

::: {.back card-id="card-3cb9dc2bc3da922a"}
If $L\in \operatorname{Pic}(X)$ is big and nef, then $L^n$ is globally generated for some $n$.

Holds for smooth projective varieties over $\CC$ when $L\otimes\omega_X {}^{ \vee }$ is big and nef.
:::

::: {.front card-id="card-e0bfd516a3578177"}
Discuss when $L\in \operatorname{Pic}(X)$ for $X$ a K3 is bpf.
:::

::: {.back card-id="card-e0bfd516a3578177"}
Sufficient condition: $L^2 > 0$ and ${\left\lvert {L} \right\rvert}$ contains an irreducible curve.
:::

::: {.front card-id="card-53e67332f7d85a65"}
Discuss irreducible curves on a K3 in $\operatorname{ch}k \neq 2$.
:::

::: {.back card-id="card-53e67332f7d85a65"}
Always have $C^2 > 0$, ${\left\lvert {{\mathcal{O}}_X(C)} \right\rvert}$ is bpf, its generic member $C'$ is smooth.

Either $C'$ is hyperelliptic (so $\deg \phi = 2$) or not (then $\deg \phi = 1$ is birational)
:::

::: {.front card-id="card-7de6f6849a5d455d"}
Discuss curves with $C^2 = 0$ on a K3.
:::

::: {.back card-id="card-7de6f6849a5d455d"}
If $L \in \operatorname{Pic}(X)^\mathrm{nef}$ is nontrivial and $L^2=0$ then $L$ is bpf.

Away from characteristics 2 and 3, $\exists E$ a smooth irreducible elliptic curve with $mE \in {\left\lvert {L} \right\rvert}$ for some $m$.

If $L.C \geq 0$ for all $C\cong {\mathbf{P}}^1$ then $L\cong {\mathcal{O}}(m E)$ for some $m$.
:::

::: {.front card-id="card-4490be94e7ce9bad"}
Does the Fermat quartic contain any lines?
:::

::: {.back card-id="card-4490be94e7ce9bad"}
Yes: ${\left[ {x_0, \zeta_8 x_0, x_2, \zeta_8 x_2} \right]}$.
:::

::: {.front card-id="card-324108ea57273d0b"}
When is a K3 surface elliptic?
:::

::: {.back card-id="card-324108ea57273d0b"}
$X$ is elliptic $\iff \exists L\in \operatorname{Pic}(X)$ with $L^2 =0$ away from characteristic 2,3.

Idea: pass from $L$ with $L^2 = 0$ to a nef $L'$ with $(L')^2 = 0$ through a series of reflections $L\mapsto L + (L.C)C$ for $C$ a $(-2)\dash$curve with $L.C < 0$.
:::

::: {.front card-id="card-a772d749c355f1fe"}
Discuss base points of complete linear systems on a K3.
:::

::: {.back card-id="card-a772d749c355f1fe"}
$\operatorname{Bs}{\left\lvert {L} \right\rvert} = F$, i.e. ${\left\lvert {L} \right\rvert}$ has no base points outside of its fixed part.
:::

::: {.front card-id="card-7a25c38d96ac8312"}
What is a polarized K3 of degree $2d$?
:::

::: {.back card-id="card-7a25c38d96ac8312"}
A pair $(X, L)$ with $X$ a projective K3 and $L\in \operatorname{Pic}(X)^\amp = \NS(X)^\amp$ primitive with $L^2 = 2d$.
:::

::: {.front card-id="card-045aecc61162ab8a"}
What is the genus of a polarized K3?
:::

::: {.back card-id="card-045aecc61162ab8a"}
Write $2d = 2g-2$, then $g = g(C)$ for any $C\in {\left\lvert {L} \right\rvert}$, we say $(X, L)$ is a polarized K3 of genus $g$.
:::

::: {.front card-id="card-63450e6157a4c6bd"}
Do there exist K3s of arbitrary degree over $k=\kbar$?
:::

::: {.back card-id="card-63450e6157a4c6bd"}
Yes, for $g\geq 3$ over $k=\kbar$ there exists K3s of degree $2g-2$ in ${\mathbf{P}}^g$.

Idea: for $g=3k$, take a generic quartic $X$ in ${\mathbf{P}}^3$ containing a line $\ell$.

Let $H$ be the hyperplane section and consider ${\left\lvert {H-\ell} \right\rvert}$

This defines an elliptic pencil ${\left\lvert {E} \right\rvert}$.

Consider $L_k \coloneqq H + (k-1)E \in \operatorname{Pic}(X)^\vamp$, for generic $X$ it is primitive.

Yields a polarized K3 of degree $L_k^2 = 6k-2$.
:::

::: {.front card-id="card-920ffb5ecda68daf"}
Do there exist K3s of arbitrary degree over $k\neq \kbar$?
:::

::: {.back card-id="card-920ffb5ecda68daf"}
No: for $k={ \mathbf{F} }_q$, the degree of a polarized K3 defined over $k$ is bounded.

Related to questions about rational points on the moduli of K3s.
:::

::: {.front card-id="card-7f793df47dd67483"}
Discuss $\operatorname{Pic}(X)^\amp\subseteq \operatorname{Pic}(X)$.
:::

::: {.back card-id="card-7f793df47dd67483"}
An open subspace, i.e. ampleness is an open property.
:::

::: {.front card-id="card-719758760811ef26"}
What is the Zariski decomposition of an effective divisor?
:::

::: {.back card-id="card-719758760811ef26"}
$D = P + N$ where $P, N \in \NS(X)_\QQ$ with $P\in \operatorname{Nef}(X)$ the positive part and $N = \sum a_i C_i$ effective (with $a_i \in \QQ_{\gt 0})$ where $P.C_i = 0$ for all $i$ and the intersection matrix $(C_i . C_j)$ is negative definite.
:::

::: {.front card-id="card-7ee99fa7712a9959"}
Discuss finite generation of the section ring $R(X; L)$ for $L\in \operatorname{Pic}(X)$.
:::

::: {.back card-id="card-7ee99fa7712a9959"}
If $X$ is a smooth surface and $L$ is big, then $R(X; L)$ is finitely generated iff $P$ is semiample.

$R(; L)$ is finitely generated for any $L\in \operatorname{Pic}(X)$ whatsoever for a K3.
:::

::: {.front card-id="card-51c365f7745a9990"}
What is a Hodge structure of weight $n$?
:::

::: {.back card-id="card-51c365f7745a9990"}
For $V\in   {}_{\CC}\Mod$, a Hodge structure of weight $n \in \mathbf{Z}$ on $V$ is given by a direct sum decomposition of the complex vector space $V_\CC$
$$V_\CC=\bigoplus_{p+q=n} V^{p, q} \quad\text{such that} \quad \overline{V^{p, q}}=V^{q, p}$$
:::

::: {.front card-id="card-26e2d214ce1626dc"}
What are isogenous Hodge structures?
:::

::: {.back card-id="card-26e2d214ce1626dc"}
$V, W$ with integral Hodge structures are isogenous iff $V_\QQ\cong W_\QQ$.
:::

::: {.front card-id="card-49d969d85716f30f"}
What are Hodge classes?
:::

::: {.back card-id="card-49d969d85716f30f"}
For $V$ a Hodge structure of even weight $2k$, the intersection $V\cap V^{k, k}$.
:::

::: {.front card-id="card-caf733a4c2c79137"}
What are $\ZZ(1), \QQ(1)$?
:::

::: {.back card-id="card-caf733a4c2c79137"}
The Tate Hodge structure $\mathbf{Z}(1)$ is the Hodge structure of weight $-2$ given by the free $\mathbf{Z}$-module of rank one $(2 \pi i) \mathbf{Z}$ (as a submodule of $\mathbf{C}$ ) such that $\mathbf{Z}(1)^{-1,-1}$ is one-dimensional. Similarly, one defines the rational Tate Hodge structure $\mathbf{Q}(1)$.
:::

::: {.front card-id="card-c952a01568be3371"}
What is $\ZZ(k)$ for $k\in \ZZ$?
:::

::: {.back card-id="card-c952a01568be3371"}
$\ZZ(-1) = \ZZ(1) {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}_{  {}_{ \CC}\Mod}(V_\CC, \CC)$ and $\ZZ(k) \coloneqq\ZZ(1){ {}^{ \scriptstyle\otimes_{\CC}^{k} }  }$ whose underlying module is $(2\pi i )^k \ZZ$.

$\ZZ(0)$ is the trivial Hodge structure of weight zero and rank one.
:::

::: {.front card-id="card-a87ff15477fb9227"}
What is the Tate twist $V(k)$ for $V$ a Hodge structure of weight $n$?
:::

::: {.back card-id="card-a87ff15477fb9227"}
$V(k) \coloneqq V\otimes_\CC\ZZ(k)$, so $V(k)^{p, q} = V^{p+k, q+k}$ which is weight $n-2k$.
:::

::: {.front card-id="card-3f0ae58e29b77281"}
What is the Hodge filtration?
:::

::: {.back card-id="card-3f0ae58e29b77281"}
$\Fil^i V_\CC\coloneqq\bigoplus_{p\geq i} V^{p, q}_\CC$, satisfies $\Fil^p V_\CC\oplus\overline{\Fil^q V_\CC} = V_\CC$ for all $p+q=n+1$.
:::

::: {.front card-id="card-9b71bf87ceb9944f"}
What is the Hodge structure associated to an arbitrary Hodge filtration?
:::

::: {.back card-id="card-9b71bf87ceb9944f"}
For $\Fil^* V$ a Hodge filtration, define $V^{p, n-p} \coloneqq\Fil^p V \cap\overline{\Fil^{n-p} V}$.
:::

::: {.front card-id="card-7157bd1d4cfece5d"}
Discuss the Hodge conjecture.
:::

::: {.back card-id="card-7157bd1d4cfece5d"}
The even part $\bigoplus H^{2 k}(X, \mathbf{Q})$ contains all algebraic classes, i.e. classes obtained as fundamental classes $[Z]$ of subvarieties $Z \subset X$. It is not difficult to see that $[Z]$ is an integral class, i.e. that it comes from an element in $H^{2 k}(X, \mathbf{Z})$, and that it is contained in $H^{k, k}(X)$.

The Hodge conjecture asserts that the space spanned by those is determined entirely by the Hodge structure itself.

(Hodge conjecture). For a smooth projective variety $X$ over $\mathbf{C}$ the subspace of $H^{2 k}(X, \mathbf{Q})$ spanned by all algebraic classes $[Z]$ coincides with the space of Hodge classes, i.e.
$$H^{2 k}(X; \mathbf{Q}) \cap H^{k, k}(X)=\left\langle{[Z] \st Z \subset X}\right\rangle_\QQ$$
:::

::: {.front card-id="card-9274e5ea0d527d5d"}
Discuss the status of the Hodge conjecture.
:::

::: {.back card-id="card-9274e5ea0d527d5d"}
Can fail for nonprojective hyperkahlers, integral version known not to hold.

Known for $(1, 1)\dash$classes and $(\dim X-1, \dim X - 1)\dash$classes.

Known for K3s, but not for products of K3s.
:::

::: {.front card-id="card-05d87cb60a83a6a1"}
What is a polarization and a polarized Hodge structure?
:::

::: {.back card-id="card-05d87cb60a83a6a1"}
A polarization of a rational Hodge structure $V$ of weight $n$ is a morphism of Hodge structures $\psi: V \otimes V \rightarrow \mathbf{Q}(-n)$ such that its $\mathbf{R}$-linear extension yields a positive definite symmetric form $(v, w) \longmapsto \psi(v, C w)$ on the real part of $V^{p, q} \oplus V^{q, p}$. Then $(V, \psi)$ is called a polarized Hodge structure.
:::

::: {.front card-id="card-875031744b580783"}
What is a Hodge isometry?
:::

::: {.back card-id="card-875031744b580783"}
For polarized Hodge structures $(V_1,q_1)$ and $(V_2,q_2)$, a Hodge isometry is an isomorphism $f:V_1\xrightarrow{\sim}V_2$ of Hodge structures such that $q_2(fx,fy)=q_1(x,y)$ for all $x,y\in V_1$.
:::

::: {.front card-id="card-f684c22e4863facf"}
What is the Hodge-Riemann pairing?
:::

::: {.back card-id="card-f684c22e4863facf"}
Consider a rational (or integral) Kahler class $\omega \in H^2(X, \mathbf{Q})$ on a smooth projective manifold $X$. Then define on $H^n(X, \mathbf{Q})$ with $n \leq d=\operatorname{dim}_\CC X$ the following pairing:
$$(v, w) \longmapsto(-1)^{n(n-1) / 2} \int_X v \wedge w \wedge \omega^{d-n}$$
:::

::: {.front card-id="card-03a80a562416ba95"}
What is the primitive part of cohomology with respect to a rational Kahler class $\omega\in H^2(X; \QQ)$?
:::

::: {.back card-id="card-03a80a562416ba95"}
$$H^n(X, \mathbf{Q})_{\mathrm{p}}:=\operatorname{Ker}\left(\wedge \omega^{d-n+1}: H^n(X; \mathbf{Q}) \longrightarrow H^{2 d-n+2}(X; \mathbf{Q})\right)$$
The Hodge-Riemann pairing on this defines a polarization, so primitive cohomology of a smooth complex projective variety over $\CC$ is always polarizable.
:::

::: {.front card-id="card-6d7de03bbbdaa923"}
How can one interpret Hodge structures as representations of the Deligne torus?
:::

::: {.back card-id="card-6d7de03bbbdaa923"}
Given $V$ a Hodge structure of weight $n$, define
$$\begin{align}
\rho: \CC^{\times}&\to \operatorname{GL}(V_{\mathbf{R}}) \quad \in \Grp\
z &\mapsto (v\mapsto z^p \overline{z}^q\cdot v), \quad v\in V^{p, q}
.\end{align}$$
$\QQ\dash$Hodge structures of weight $n$ biject with algebraic representations $\rho$ with an ${\mathbf{R}}^{\times}$ action defined by $\rho(t).v\coloneqq t^n.v$.

The inverse construction sends $\rho$ to $V^{p, q}:=\left\{v \in V_\CC \mathrel{\Big|}\rho_\CC(z)(v)=\left(z^p \overline{z}^q\right) \cdot v \text { for all } z \in \mathbf{C}^*\right\}$ where $\rho_\CC: \CC^{\times}\to \operatorname{GL}(V_\CC)$ is a $\CC\dash$linear extension.

Then $\rho_\CC$ splits into a sum of characters and $V_\CC= \bigoplus V^{p, q}$.
:::

::: {.front card-id="card-0017cf000246c23c"}
What is the Deligne torus?
:::

::: {.back card-id="card-0017cf000246c23c"}
$T\coloneqq\mathop{\mathrm{Res}}_{\CC/{\mathbf{R}}} {\mathbf{G}}_m(\CC)$, the real algebraic group where $T(A) \coloneqq(A\otimes_{\mathbf{R}}\CC)^{\times}$ for $A\in{ {}_{{\mathbf{R}}}  \mathsf{Alg}}$.
:::

::: {.front card-id="card-dfcbd23d66336108"}
What is the Tate Hodge structure, and what representation does it correspond to?\
:::

::: {.back card-id="card-dfcbd23d66336108"}
- $\QQ(1)$ which corresponds to
$$\begin{align}
\CC^{\times}&\to {\mathbf{R}}^{\times}\
z &\mapsto (z\overline{z})^{-1}
.\end{align}$$
:::

::: {.front card-id="card-76f5190528e2c617"}
What does the Kummer construction do?
:::

::: {.back card-id="card-76f5190528e2c617"}
The Kummer construction allows one to pass from Hodge structures of weight one of a two-dimensional torus to the Hodge structure of weight two of its associated Kummer surface.
:::

::: {.front card-id="card-41bbe9b420b7f0c1"}
Discuss bijections for Hodge structures of weight one.
:::

::: {.back card-id="card-41bbe9b420b7f0c1"}
All of geometric origin, using that projective tori are abelian varieties:
$$\begin{align}
\left\{{T/\CC\text{ tori}}\right\} &\rightleftharpoons\ZZ\operatorname{HS}^1 \\
\left\{{T/\CC\text{ abelian varieties}}\right\} &\rightleftharpoons\left\{{V\in \ZZ\operatorname{HS}^1 \text{ polarizable}}\right\} \\
\left\{{T/\CC\text{ polarized abelian varieties}}\right\} &\rightleftharpoons\left\{{V\in \ZZ\operatorname{HS}^1 \text{ polarized}}\right\}
.\end{align}$$
:::

::: {.front card-id="card-09a7b9bdcd167808"}
What is the global Torelli theorem for curves?
:::

::: {.back card-id="card-09a7b9bdcd167808"}
Two smooth compact complex curves $C$ and $C^{\prime}$ are isomorphic if and only if there exists an isomorphism $H^1(C, \mathbf{Z}) \simeq H^1\left(C^{\prime}, \mathbf{Z}\right)$ of integral Hodge structures respecting the intersection pairing (i.e. the polarization).
:::

::: {.front card-id="card-e7187787287eaf85"}
What is a Hodge structure of K3 type?
:::

::: {.back card-id="card-e7187787287eaf85"}
Weight 2 with
$$\operatorname{dim}_\CC\left(V^{2,0}\right)=1 \text { and } V^{p, q}=0 \text { for }|p-q|>2$$
:::

::: {.front card-id="card-2532873a2539c45d"}
Is the Hodge structure on a K3 polarizable?
:::

::: {.back card-id="card-2532873a2539c45d"}
If algebraic, always. If not, there are counterexamples.
:::

::: {.front card-id="card-a75c71cf2709c1cd"}
What is the transcendental part of a Hodge structure of K3 type?
:::

::: {.back card-id="card-a75c71cf2709c1cd"}
For an integral or rational Hodge structure of K3 type $V$ one defines the transcendental lattice or transcendental part $T$ as the minimal primitive sub-Hodge structure
$$\begin{align}T \subset V \text { with } V^{2,0}=T^{2,0} \subset T_\CC\end{align}$$
The primitivity, i.e. the condition that $V / T$ is torsion free, has to be added for integral Hodge structures, as otherwise minimality cannot be achieved.
:::

::: {.front card-id="card-14234c9dd775e812"}
What is the lattice for $H^1(\CC^2/\Gamma; \ZZ)$?
:::

::: {.back card-id="card-14234c9dd775e812"}
$U{ {}^{ \scriptscriptstyle\oplus^{3} }  }$; always has a Hodge structure of K3 type.
:::

::: {.front card-id="card-7df71f32322ce16a"}
What is the Kummer lattice?
:::

::: {.back card-id="card-7df71f32322ce16a"}
The unique even negative definite rank 16 lattice of discriminant $2^{16}$.
:::

::: {.front card-id="card-5113f1d6f8452d78"}
Describe the Hodge isometries of $T(X)$ for a K3.
:::

::: {.back card-id="card-5113f1d6f8452d78"}
Finite cyclic; any $\alpha: T(X) { \, \xrightarrow{\sim}\, }T(X)$ satisfies $\alpha^n=\operatorname{id}$ for some $n$.

If $\rho(X)$ is odd, then $T(X) = \left\{{\pm \operatorname{id}}\right\} \cong C_2$.
:::

::: {.front card-id="card-bf54130388c9cc35"}
What is a CM field?
:::

::: {.back card-id="card-bf54130388c9cc35"}
$K$ a purely imaginary quadratic extension of a totally real field, so $K = K_0(\sqrt\alpha)$ with $\sigma(\alpha)\in {\mathbf{R}}_{\gt 0}$ for every embedding $\sigma: K_0 \hookrightarrow\CC$.
:::

::: {.front card-id="card-e809a4d4414318c1"}
Discuss $K\coloneqq K(T) \coloneqq{ \operatorname{End} }_{\mathbf{Q}\kern-0.5pt\operatorname{HS}}(T)$ for a K3.
:::

::: {.back card-id="card-e809a4d4414318c1"}
Always a number field. If $T\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ is polarized irreducible of K3 type, the $K$ is either totally real or a CM field.

If CM, $K = \QQ(\eta)$ for some Hodge isometry $\eta$.

Any totally real field is realized as $K(T)$ for $T\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ polarized of K3 type.
:::

::: {.front card-id="card-eb58491fe6b0d0bb"}
What are the Hodge and Mumford-Tate groups of $V\in \mathbf{Q}\kern-0.5pt\operatorname{HS}$ polarizable?
:::

::: {.back card-id="card-eb58491fe6b0d0bb"}
Identifying the Hodge structure with a representation $\rho: {\mathbb{S}}\to \operatorname{GL}(V_{\mathbf{R}})$, the smallest algebraic subgroups of $\operatorname{GL}(V)/\QQ$ with
$$\begin{align}
\rho(\mathbb{U}({\mathbf{R}})) \subseteq \Hodge(V)({\mathbf{R}}) \qquad \rho({\mathbb{S}}({\mathbf{R}})) \subseteq \operatorname{MT}(V)({\mathbf{R}})
.\end{align}$$
where $\mathbb{U}\coloneqq\ker\qty{{\mathbb{S}}\xrightarrow{\operatorname{Nm}} {\mathbf{G}}_m({\mathbf{R}})} = \left\{{z\in {\mathbb{S}}({\mathbf{R}}) \st z\overline{z} = 1}\right\}$.

Related by a morphism
$$\begin{align}
\Hodge(V)\times {\mathbf{G}}_m &\to\operatorname{MT}(V) \
(g, \mu) &\mapsto g\mu
.\end{align}$$
What does it mean for a K3 surface to have CM?

$\Hodge(T)$ is commutative, equivalently $\dim_K(T) = 1$. Implies that $K$ is a CM field.
:::

::: {.front card-id="card-c4f19ff090c4318b"}
What is the $\ell\dash$adic algebraic monodromy group?
:::

::: {.back card-id="card-c4f19ff090c4318b"}
For $X\in {\mathsf{sm}}\Var^{\mathop{\mathrm{proj}}}_{/ {k}}$ with $k$ finitely-generated of characteristic zero, the Zariski closure of the image of the Galois representation
$$\begin{align}
\rho*\ell: G*k &\to \operatorname{GL}(V), \qquad V = H^2*\text{ét}(X; { \QQ*\ell }(1))
.\end{align}$$
:::

::: {.front card-id="card-4137a8b3bad51d35"}
What is the Mumford-Tate conjecture?
:::

::: {.back card-id="card-4137a8b3bad51d35"}
Under the isomorphism $H^2_\text{ét}(X; { \QQ_\ell }(1)) { \, \xrightarrow{\sim}\, }H^2(X(\CC); \QQ) \otimes{ \QQ_\ell }(1)$, the identity component of the $\ell\dash$adic monodromy group, $\overline{\operatorname{im}\rho_\ell}^0$, bijects with the Mumford-Tate group $\operatorname{MT}(X)$.

Proved for K3s over number fields.
:::

::: {.front card-id="card-b895e365a3b35d5b"}
What is the Hodge diamond for a surface?
:::

::: {.back card-id="card-b895e365a3b35d5b"}
For a smooth projective complex surface, the Hodge diamond is
$$\begin{matrix}&&1&&\\&q&&q&\\p_g&&h^{1,1}&&p_g\\&q&&q&\\&&1&&\end{matrix}$$
where $q=h^{1,0}=h^1(\mathcal O_X)$ and $p_g=h^{2,0}=h^0(\omega_X)$.
:::

::: {.front card-id="card-3b4ed3689f8e94d9"}
What is $\kappa(X)$ for $X$ a K3?
:::

::: {.back card-id="card-3b4ed3689f8e94d9"}
$\kappa(X) = 0$, one of four such classes of minimal surfaces.
:::

::: {.front card-id="card-277ec0b2ed591534"}
Where do K3s fit into the classification of surfaces?
:::

::: {.back card-id="card-277ec0b2ed591534"}
Positively curved: del Pezzo

Flat: K3s (generally CYs and hyperkahlers)

Negatively curved: general type.
:::

::: {.front card-id="card-8ace99975d2c209d"}
What are $q(X), p_g(X), \beta^+(X), \chi(X), c_1^2(X), c_2(X)$ for a K3?
:::

::: {.back card-id="card-8ace99975d2c209d"}
$q(X) = 0$

$p_g(X) = 1$

$\beta^+(X) = 3$

$\chi(X) = 2$

$c_1^2(X) = 0$

$c^2(X) =24$.
:::

::: {.front card-id="card-3669e4b341b8e820"}
Describe the period map of a single K3.
:::

::: {.back card-id="card-3669e4b341b8e820"}
Pick $\omega\in H^{2, 0}(X) \subseteq H^2(X;\CC)$ a nonvanishing holomorphic 2-form.

Check the cup product satisfies $\omega^2 = 0$ and $\omega.\overline{\omega }> 0$.

Extend a marking $\phi$ to $\phi_\CC: H^2(X;\CC)\to \Lambda_{{\mathsf{K}}3}\otimes_\ZZ\CC$.

Check $\operatorname{im}\phi_\CC= \mathop{\mathrm{span}}_\CC\left\{{\phi_\CC(\omega)}\right\}$ is a line through the origin

Thus $\operatorname{im}\phi \in \mathbb{D}$.
:::

::: {.front card-id="card-5123fd7566ad8ab0"}
How is $\mathbb{D}$ related to moduli of K3s?
:::

::: {.back card-id="card-5123fd7566ad8ab0"}
Weak Torelli: $X { \, \xrightarrow{\sim}\, }X' \iff$ there is an isometry $H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }H^2(X';\ZZ)$ whose $\CC\dash$linear extension preserves Hodge decompositions. So two K3s are isomorphic iff they admit markings defining the same point in $\mathbb{D}$.

Local Torelli: for a marked K3 $(X, \phi)$, the period map from the versal deformation space to $\mathbb{D}$ is a local isomorphism.

Surjectivity: every $d\in \mathbb{D}$ is a period point for some marked K3.

Thus almost a coarse moduli space: families $\mcx\to B$ yield $B\to \mathbb{D}$ and points correspond to iso classes, but quotienting by change-of-marking yields a non-Hausdorff quotient since it does not act properly discontinuously.
:::

::: {.front card-id="card-95ea8d364c6151bd"}
Describe the period map of a family of K3s.
:::

::: {.back card-id="card-95ea8d364c6151bd"}
Let $f:\mcx\to B$ be a flat family with fiber $X$.

Choosing a marking $\phi: H^2(X;\ZZ) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3}$ extends to a sheaf morphism $\phi_B: {\mathbf{R}}^2 f_*\underline{\ZZ}\to\underline{\Lambda_{{\mathsf{K}}3}}$ where the latter is a constant sheaf.

Yields a holomorphic map $B\to \mathbb{D}$.
:::

::: {.front card-id="card-b4c7696af026d814"}
What are the two most widely studied classes of K3s?
:::

::: {.back card-id="card-b4c7696af026d814"}
Sextic double planes: birational to $X\to {\mathbf{P}}^1$ a degree 2 cover branched over a sextic curve (equivalently a sextic hypersurface in $\WP(1,1,1,3)$.)

Quartic hypersurfaces:

$X\subseteq {\mathbf{P}}^3$ a quartic hypersurface

$X\to {\mathbf{P}}^1 \times {\mathbf{P}}^1$ a double cover branched over a bidegree $(4, 4)$ curve.

$X\to C$ an elliptic fibration over the twisted cubic.
:::

::: {.front card-id="card-31b8cfe1587ec0da"}
What is a semistable degeneration?
:::

::: {.back card-id="card-31b8cfe1587ec0da"}
$\pi:\mcx\to \Delta$ with $\mcx$ smooth and central fiber reduced normal crossings.
:::

::: {.front card-id="card-75f1921216084ec3"}
What is the dual graph of a degeneration?
:::

::: {.back card-id="card-75f1921216084ec3"}
Let $S_0=\bigcup V_i$ be the central fibre in a semistable degeneration. Define the dual graph $\Gamma$ of $S_0$ as follows: $\Gamma$ is a simplicial complex whose vertices $P_1, \ldots, P_r$ correspond to the components $V_1, \ldots, V_r$ of $S_0$; the $k$-simplex $\left\langle P_{i_0}, \ldots, P_{i_k}\right\rangle$ belongs to $\Gamma$ if and only if $V_{i_0} \cap \cdots \cap V_{i_k} \neq \emptyset$.
:::

::: {.front card-id="card-4e90b1d8184c7c0a"}
Why is lattice theory important in the study of K3s?
:::

::: {.back card-id="card-4e90b1d8184c7c0a"}
For $X$ a smooth K3, $H^2(X; \ZZ) \cong L_{{\mathsf{K}}3} \coloneqq H{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{2} }  }$.
:::

::: {.front card-id="card-cd0d75cdabdfde40"}
Discuss $H^{2, 0}(X)$ for $X$ a K3.
:::

::: {.back card-id="card-cd0d75cdabdfde40"}
$H^{2, 0}(X) = \CC\omega_X$ for some nowhere vanishing holomorphic 2-form $\omega_X$
:::

::: {.front card-id="card-f366077ef99eafd5"}
What is the Kahler cone $\mck_X$?
:::

::: {.back card-id="card-f366077ef99eafd5"}
$\mck_X \subseteq H^{1, 1}(X; {\mathbf{R}})$ the set of Kahler forms, forms an open convex cone.
:::
