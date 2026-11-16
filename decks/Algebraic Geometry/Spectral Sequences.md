---
title: "Algebraic Geometry::Spectral Sequences"
---

::: {.front card-id="spectral-weight-open-variety" tags="formula application"}
State the weight spectral sequence for the complement of an SNC divisor in a smooth projective complex variety. Explain degeneration by weights and compute $H^1(\mathbb G_m,\mathbb Q)$ from $\mathbb P^1\setminus\{0,\infty\}$.
:::

::: {.back card-id="spectral-weight-open-variety"}
Let $U=X\setminus D$, $D=\bigcup_iD_i$, and let $D^{(p)}$ be the disjoint union of the $p$-fold intersections of distinct components, with $D^{(0)}=X$. Then
$$E_1^{-p,q}=H^{q-2p}(D^{(p)},\mathbb Q)(-p)\Longrightarrow H^{q-p}(U,\mathbb Q).$$
The $d_1$ is an alternating sum of Gysin maps. Each term is pure of weight $q$; $E_2$ retains this purity. For $r\ge2$, the target has weight $q-r+1\ne q$, so $d_r=0$. Thus the sequence degenerates at $E_2$, not generally at $E_1$.

For $U=\mathbb G_m$, the relevant map is
$$H^0(\{0,\infty\},\mathbb Q)(-1)=\mathbb Q(-1)^2
\xrightarrow{(a,b)\mapsto a+b}H^2(\mathbb P^1,\mathbb Q)=\mathbb Q(-1).$$
Its kernel gives $H^1(U,\mathbb Q)=\mathbb Q(-1)$ of weight two, despite having cohomological degree one.
:::

::: {.front card-id="spectral-leray-geometric-degeneration" tags="theorem comparison application"}
State geometric degeneration of rational Leray for a smooth projective morphism of complex varieties. How does it differ from a coherent Leray collapse? Compute the Betti numbers of a product of two smooth projective curves.
:::

::: {.back card-id="spectral-leray-geometric-degeneration"}
For smooth projective $f:X\to Y$,
$$E_2^{p,q}=H^p(Y,R^qf_*\mathbb Q)\Longrightarrow H^{p+q}(X,\mathbb Q)$$
degenerates at $E_2$ (Deligne). This uses analytic rational cohomology; it does not say that coherent Leray for every sheaf degenerates, or provide a canonical splitting. Relative hard Lefschetz yields a derived decomposition after choices.

For $C_g\times C_h\to C_g$, the local systems are constant, so
$$\sum b_kt^k=(1+2gt+t^2)(1+2ht+t^2).$$
Thus $b_1=b_3=2g+2h$, $b_2=2+4gh$, and $b_0=b_4=1$. Here the product structure supplies the Künneth decomposition explicitly.
:::

::: {.front card-id="spectral-pages-convergence" tags="definition comparison"}
Fix cohomological indexing. Define the pages, differentials, convergence, and degeneration of a first-quadrant spectral sequence. What does $E_\infty$ determine, and what remains to recover the abutment?
:::

::: {.back card-id="spectral-pages-convergence"}
$$d_r:E_r^{p,q}\to E_r^{p+r,q-r+1},\qquad
E_{r+1}^{p,q}=\frac{\ker(d_r:E_r^{p,q}\to E_r^{p+r,q-r+1})}{\operatorname{im}(d_r:E_r^{p-r,q+r-1}\to E_r^{p,q})}.$$
Convergence to $H^n$ means a finite decreasing filtration with
$$E_\infty^{p,n-p}\cong F^pH^n/F^{p+1}H^n.$$
First-quadrant support makes each diagonal finite. Degeneration at $E_r$ means all $d_s=0$ for $s\ge r$; it does not choose splittings of the filtration.

Over a field, a finite filtration splits noncanonically. Over $\mathbb Z$, associated graded $\mathbb Z/2\oplus\mathbb Z/2$ permits both $\mathbb Z/4$ and $(\mathbb Z/2)^2$. A spectral sequence does not include convergence automatically; unbounded filtrations require a separate convergence argument.
:::

::: {.front card-id="spectral-filtered-complex-double" tags="construction formula"}
Construct the spectral sequence of a bounded filtered cochain complex and the two spectral sequences of a first-quadrant double complex. State a total-differential convention.
:::

::: {.back card-id="spectral-filtered-complex-double"}
For a decreasing filtration preserved by $d$,
$$E_0^{p,q}=\operatorname{gr}_F^pK^{p+q},\qquad
E_1^{p,q}=H^{p+q}(\operatorname{gr}_F^pK),\qquad E_\infty^{p,q}=\operatorname{gr}_F^pH^{p+q}(K).$$
Assume the filtration is finite in each degree and bounded in the range used for convergence.

For $d_hd_v=d_vd_h$ on $C^{p,q}$, use $d_{\mathrm{Tot}}=d_h+(-1)^p d_v$. Filtering by columns gives
$$E_1^{p,q}=H_v^q(C^{p,\bullet}),\qquad E_2^{p,q}=H_h^pH_v^q(C),$$
while filtering by rows takes horizontal cohomology first. Both converge to $H^{p+q}(\operatorname{Tot}C)$ in the first quadrant. For $d_hd_v=-d_vd_h$, use $d_{\mathrm{Tot}}=d_h+d_v$.
:::

::: {.front card-id="spectral-five-term-edges" tags="formula application"}
State the edge maps and five-term exact sequence of a first-quadrant cohomological spectral sequence starting at $E_2$. Specialize to Leray.
:::

::: {.back card-id="spectral-five-term-edges"}
Edge maps: $E_2^{n,0}\to H^n$ and $H^n\to E_2^{0,n}$. The low-degree sequence is
$$0\to E_2^{1,0}\to H^1\to E_2^{0,1}\xrightarrow{d_2}E_2^{2,0}\to H^2.$$
For $f:X\to Y$ and an abelian sheaf $F$,
$$0\to H^1(Y,f_*F)\to H^1(X,F)\to H^0(Y,R^1f_*F)
\xrightarrow{d_2}H^2(Y,f_*F)\to H^2(X,F).$$
A section of $R^1f_*F$ lifts to global $H^1(X,F)$ precisely when its transgression $d_2$ vanishes. The five-term sequence alone does not make the last displayed map surjective.
:::

::: {.front card-id="spectral-grothendieck-composition" tags="theorem comparison"}
State Grothendieck's spectral sequence for a composition of left exact functors. Explain the acyclicity hypothesis and recover Leray.
:::

::: {.back card-id="spectral-grothendieck-composition"}
Let $F:\mathcal A\to\mathcal B$, $G:\mathcal B\to\mathcal C$ be additive left exact functors between abelian categories; $\mathcal A,\mathcal B$ have enough injectives. Assume $F(I)$ is $G$-acyclic for every injective $I\in\mathcal A$. Then
$$E_2^{p,q}=R^pG(R^qF(A))\Longrightarrow R^{p+q}(G\circ F)(A).$$
The hypothesis means $R^{p>0}G(F(I))=0$; left exactness alone is insufficient to identify the derived composite.

Take $F=f_*$ and $G=\Gamma(Y,-)$ on abelian sheaves. Since $f^{-1}$ is exact, $f_*$ preserves injectives, so the hypothesis holds and yields Leray.

Reference: [Stacks, Grothendieck spectral sequence](https://stacks.math.columbia.edu/tag/015N).
:::

::: {.front card-id="spectral-hypercohomology-pair" tags="formula comparison application"}
State the two hypercohomology spectral sequences for a bounded complex of sheaves $K^\bullet$ in nonnegative degrees. Distinguish cohomology of its terms from cohomology sheaves. Give collapse criteria.
:::

::: {.back card-id="spectral-hypercohomology-pair"}
$${}'E_1^{p,q}=H^q(X,K^p)\Longrightarrow\mathbb H^{p+q}(X,K^\bullet),$$
$${}''E_2^{p,q}=H^p(X,\mathcal H^q(K^\bullet))\Longrightarrow\mathbb H^{p+q}(X,K^\bullet).$$
The first uses the differential of $K$ on $E_1$; the second first computes its kernels modulo images as sheaves.

If every $K^p$ is $\Gamma$-acyclic, the first has only $q=0$ and gives $\mathbb H^n=H^n(\Gamma(X,K^\bullet))$. If every $\mathcal H^q(K)$ is acyclic, the second gives $\mathbb H^n=\Gamma(X,\mathcal H^n(K))$.

For $K=[\mathcal O_{\mathbb A^1}\xrightarrow{t}\mathcal O_{\mathbb A^1}]$ in degrees $0,1$, the only cohomology sheaf is $k(0)$ in degree one. Both methods give $\mathbb H^1=k$ and all other groups zero.
:::

::: {.front card-id="spectral-cech-derived" tags="formula application"}
State the Čech-to-sheaf-cohomology spectral sequence. When does a cover compute cohomology by its Čech complex? Contrast a standard affine cover with the one-open-set cover of $\mathbb P^1$.
:::

::: {.back card-id="spectral-cech-derived"}
For a finite open cover $\{U_i\}$ and abelian sheaf $F$,
$$E_1^{p,q}=\prod_{i_0<\cdots<i_p}H^q(U_{i_0}\cap\cdots\cap U_{i_p},F)
\Longrightarrow H^{p+q}(X,F).$$
If all nonempty finite intersections are $F$-acyclic, only $q=0$ remains and Čech cohomology computes sheaf cohomology. A finite affine cover of a separated scheme has affine intersections, so this applies to quasi-coherent $F$.

For $\mathcal O(-2)$ on $\mathbb P^1$, the two affine charts compute $H^1=k$. The cover consisting of $\mathbb P^1$ alone has zero Čech $H^1$, but its $E_1^{0,1}=H^1(\mathbb P^1,\mathcal O(-2))=k$ survives. A cover is not automatically acyclic.
:::

::: {.front card-id="spectral-local-global-ext" tags="formula application"}
State local-to-global Ext for coherent sheaves on a smooth projective variety. Give its five-term sequence and compute extensions between line bundles on $\mathbb P^1$.
:::

::: {.back card-id="spectral-local-global-ext"}
$$E_2^{p,q}=H^p(X,\mathcal E xt_X^q(F,G))\Longrightarrow\operatorname{Ext}^{p+q}_X(F,G).$$
In low degrees,
$$0\to H^1(\mathcal H om(F,G))\to\operatorname{Ext}^1(F,G)\to H^0(\mathcal E xt^1(F,G))
\to H^2(\mathcal H om(F,G))\to\operatorname{Ext}^2(F,G).$$
If $F$ is locally free, $\mathcal E xt^{q}(F,G)=0$ for $q>0$, so $\operatorname{Ext}^n(F,G)=H^n(F^\vee\otimes G)$; global higher Ext need not vanish.

For $F=\mathcal O(1)$, $G=\mathcal O(-1)$ on $\mathbb P^1$,
$$\operatorname{Ext}^1(F,G)=H^1(\mathcal O(-2))=k.$$
The Euler sequence $0\to\mathcal O(-1)\to\mathcal O^2\to\mathcal O(1)\to0$ is a nonsplit extension, although it splits locally.
:::

::: {.front card-id="spectral-hochschild-serre-geometric" tags="formula application"}
State Hochschild–Serre for étale cohomology over a field and Cartan–Leray for a finite étale Galois cover. What collapse follows when the finite group order is invertible in the coefficient field?
:::

::: {.back card-id="spectral-hochschild-serre-geometric"}
For $X/k$, separable closure $k^s$, $G_k=\operatorname{Gal}(k^s/k)$, and a torsion abelian étale sheaf $F$,
$$H^p_{\mathrm{cont}}(G_k,H^q_{\mathrm{\acute et}}(X_{k^s},F))\Longrightarrow H^{p+q}_{\mathrm{\acute et}}(X,F).$$
For a finite étale $G$-torsor $\pi:Y\to X$,
$$H^p(G,H^q_{\mathrm{\acute et}}(Y,\pi^*F))\Longrightarrow H^{p+q}_{\mathrm{\acute et}}(X,F).$$
If $F$ takes values in a field in which $|G|$ is invertible, averaging makes invariants exact, so
$$H^n_{\mathrm{\acute et}}(X,F)=H^n_{\mathrm{\acute et}}(Y,\pi^*F)^G.$$
For coefficients of characteristic dividing $|G|$, averaging is unavailable and higher group cohomology may survive. The same Cartan–Leray formula applies to a regular covering of spaces and pulled-back local coefficients.
:::

::: {.front card-id="spectral-degeneration-tests" tags="comparison theorem"}
Give sufficient degeneration tests for a convergent spectral sequence of finite-dimensional vector spaces. Distinguish support, parity, dimension, weights, and a splitting of the underlying complex.
:::

::: {.back card-id="spectral-degeneration-tests"}
| Test | Sufficient condition |
| --- | --- |
| Support | For all $s\ge r,p,q$, $E_s^{p,q}=0$ or $E_s^{p+s,q-s+1}=0$ (cohomological convention) |
| One row or column at $E_2$ | All later differentials have zero source or target |
| Parity | At one page, all nonzero entries have even total degree (or all odd); $d_s$ raises total degree by one |
| Dimensions | For every $n$, $\sum_{p+q=n}\dim E_r^{p,q}=\dim H^n$, with finite diagonals and convergence |
| Weights | Differentials are morphisms of pure Hodge structures with unequal source and target weights |
| Splitting | A compatible derived decomposition into cohomology objects eliminates the connecting maps producing differentials |

For example, if $E_r^{p,q}$ is pure of weight $p+q$ and every later differential respects Hodge structures, source and target weights differ by one, forcing degeneration. Purity of unrelated groups without compatibility does not suffice.

Two adjacent rows alone do not force degeneration at $E_2$: $d_2^{p,1}:E_2^{p,1}\to E_2^{p+2,0}$ may survive. Equality of Euler characteristics alone cannot detect this cancellation.
:::

::: {.front card-id="spectral-leray-collapse-practice" tags="application comparison"}
Compare coherent Leray for a morphism to an affine base, for an affine morphism, and for projection $p:\mathbb P^1\times\mathbb P^1\to\mathbb P^1$ with $F=\mathcal O(2,-2)$. State the hypotheses used in each collapse.
:::

::: {.back card-id="spectral-leray-collapse-practice"}
For quasi-compact quasi-separated morphisms of schemes and quasi-coherent $F$, the $R^qf_*F$ are quasi-coherent.

| Situation | Collapse |
| --- | --- |
| $Y$ affine | $p>0$ columns vanish: $H^n(X,F)=\Gamma(Y,R^nf_*F)$ |
| $f$ affine | $q>0$ rows vanish: $H^n(X,F)=H^n(Y,f_*F)$ |
| Projection and $F=\mathcal O(2,-2)$ | $R^0p_*F=0$, $R^1p_*F=\mathcal O(2)$: $H^1(X,F)=k^3$, all other groups zero |

Affineness of the base does not imply $R^{q>0}f_*F=0$: $\mathbb P^1\to\operatorname{Spec}k$ with $F=\mathcal O(-2)$ has $R^1f_*F=k$.
:::

::: {.front card-id="spectral-hodge-degeneration-hypotheses" tags="comparison theorem"}
Compare Hodge–de Rham degeneration in the compact Kähler, characteristic-zero algebraic, and Deligne–Illusie settings. Does degeneration alone canonically split the Hodge filtration?
:::

::: {.back card-id="spectral-hodge-degeneration-hypotheses"}
$$E_1^{p,q}=H^q(X,\Omega_X^p)\Longrightarrow H_{\mathrm{dR}}^{p+q}(X).$$
Sufficient hypotheses for $E_1$ degeneration:

- $X$ a compact Kähler manifold (analytic sheaves).
- $X$ smooth proper over a characteristic-zero field (algebraic de Rham cohomology).
- $X$ smooth proper over a perfect field $k$ of characteristic $p$, $\dim X<p$, with a smooth lift to $W_2(k)$ (Deligne–Illusie).

In the last case the truncated Frobenius-pushforward de Rham complex splits; the dimension bound covers the whole complex. A lift without the dimension bound is not this full-degeneration criterion.

Degeneration gives $\operatorname{gr}_F^pH^n\cong H^{n-p}(\Omega_X^p)$ and equality of dimensions. The canonical complex Hodge decomposition in the compact Kähler case uses the additional opposed complex-conjugate filtration; it does not follow from formal degeneration alone.

Reference: Deligne–Illusie, *Relèvements modulo $p^2$ et décomposition du complexe de de Rham* (1987).
:::

::: {.front card-id="spectral-elliptic-hodge-example" tags="application comparison"}
Compute the Hodge–de Rham spectral sequence of a smooth projective elliptic curve over $\mathbb C$. Which differential could occur on $E_1$? What does the filtration on $H^1$ say?
:::

::: {.back card-id="spectral-elliptic-hodge-example"}
$$\begin{array}{c|cc}
q\backslash p&0&1\\\hline
1&\mathbb C&\mathbb C\\
0&\mathbb C&\mathbb C
\end{array}$$
The $d_1$ maps are horizontal. On global functions it is zero because functions are constant; $E_1$ degeneration also kills the map $H^1(\mathcal O)\to H^1(\Omega^1)$. Higher differentials have no possible targets.
$$0\to H^0(\Omega^1_E)\to H^1_{\mathrm{dR}}(E)\to H^1(\mathcal O_E)\to0,\qquad (b_0,b_1,b_2)=(1,2,1).$$
Complex conjugation supplies the analytic Hodge splitting. The displayed exact sequence alone does not choose an algebraic complement to $H^0(\Omega^1_E)$.
:::

::: {.front card-id="spectral-nondegenerate-hopf" tags="application counterexample"}
In the rational Leray–Serre spectral sequence of the Hopf fibration $S^1\to S^3\to S^2$, determine the nonzero differential. What does it show about two-row arguments for degeneration?
:::

::: {.back card-id="spectral-nondegenerate-hopf"}
The base is simply connected, so $E_2^{p,q}=H^p(S^2,\mathbb Q)\otimes H^q(S^1,\mathbb Q)$ is $\mathbb Q$ at $(0,0),(2,0),(0,1),(2,1)$ and zero elsewhere.
$$d_2^{0,1}:\mathbb Q\xrightarrow{\sim}\mathbb Q=E_2^{2,0}.$$
It is the Euler class of the circle bundle, a generator of $H^2(S^2,\mathbb Z)$ up to orientation. Equivalently, convergence to $H^1(S^3)=H^2(S^3)=0$ forces this map to be an isomorphism. Only total degrees zero and three survive. Two nonzero rows do not imply collapse.
:::
