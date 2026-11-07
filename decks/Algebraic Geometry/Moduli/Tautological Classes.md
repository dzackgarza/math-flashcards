---
title: "Algebraic Geometry::Moduli::Tautological Classes"
---

::: {.front card-id="tautological-universal-curve" tags="definition"}
For $2g-2+n>0$, describe the universal curve over the complex moduli stack $\overline{\mathcal M}_{g,n}$ and its marked sections.
:::

::: {.back card-id="tautological-universal-curve"}
$$\pi:\mathcal C_{g,n}\to\overline{\mathcal M}_{g,n},\qquad s_i:\overline{\mathcal M}_{g,n}\to\mathcal C_{g,n}.$$
Its fiber is the stable marked curve itself. The total stack identifies with $\overline{\mathcal M}_{g,n+1}$, with $\pi$ forgetting the last mark and stabilizing. A new mark colliding with a mark or node is represented by inserting a rational component.
:::

::: {.front card-id="tautological-psi" tags="definition"}
Let $\pi:\mathcal C_{g,n}\to\overline{\mathcal M}_{g,n}$ be the universal stable curve over $\mathbb C$, with sections $s_i$. Define $L_i$ and $\psi_i$.
:::

::: {.back card-id="tautological-psi"}
$$L_i=s_i^*\omega_\pi,\qquad (L_i)_{[C,p_1,\ldots,p_n]}=T_{p_i}^*C,\qquad
\psi_i=c_1(L_i)\in\operatorname{CH}^1(\overline{\mathcal M}_{g,n})_{\mathbb Q}.$$
:::

::: {.front card-id="tautological-lambda" tags="definition"}
Let $\pi:\mathcal C_{g,n}\to\overline{\mathcal M}_{g,n}$ be the universal stable curve over $\mathbb C$. Define the Hodge bundle $\mathbb E$ and its classes $\lambda_j$.
:::

::: {.back card-id="tautological-lambda"}
$$\mathbb E=\pi_*\omega_\pi,\qquad
\mathbb E_{[C,p_1,\ldots,p_n]}=H^0(C,\omega_C),\qquad
\operatorname{rank}\mathbb E=g.$$
Its Chern classes are
$$\lambda_j=c_j(\mathbb E)\in\operatorname{CH}^j(\overline{\mathcal M}_{g,n})_{\mathbb Q},
\qquad\lambda_0=1,\qquad\lambda_j=0\quad(j>g).$$
:::

::: {.front card-id="tautological-kappa" tags="definition"}
For the forgetful morphism $f:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$, define $\kappa_a$ for $a\ge0$.
:::

::: {.back card-id="tautological-kappa"}
$$\kappa_a=f_*(\psi_{n+1}^{a+1})\in\operatorname{CH}^a(\overline{\mathcal M}_{g,n})_{\mathbb Q}.$$
Equivalently, on the universal curve with section divisors $D_i$,
$$\kappa_a=\pi_*\bigl(c_1(\omega_\pi(D_1+\cdots+D_n))^{a+1}\bigr).$$
:::

::: {.front card-id="tautological-kappa-tilde" tags="formula"}
For the universal stable curve $\pi:\mathcal C_{g,n}\to\overline{\mathcal M}_{g,n}$ and $a\ge0$, define $\widetilde\kappa_a$ and relate it to the logarithmic class $\kappa_a$.
:::

::: {.back card-id="tautological-kappa-tilde"}
$$\widetilde\kappa_a=\pi_*(c_1(\omega_\pi)^{a+1}),\qquad
\kappa_a=\widetilde\kappa_a+\sum_{i=1}^n\psi_i^a.$$
Here $\psi_i^0=1$.
:::

::: {.front card-id="tautological-kappa-zero" tags="formula"}
Compute $\kappa_0$ and $\widetilde\kappa_0$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-kappa-zero"}
$$\kappa_0=(2g-2+n)\,1,\qquad\widetilde\kappa_0=(2g-2)\,1.$$
They are the fiber degrees of the logarithmic and untwisted dualizing bundles.
:::

::: {.front card-id="tautological-mmm" tags="definition"}
Let $\pi:E\to B$ be a smooth oriented bundle of closed genus-$g$ surfaces. Define the Miller–Morita–Mumford classes using the vertical tangent bundle.
:::

::: {.back card-id="tautological-mmm"}
For $a\ge0$,
$$T_\pi E=\ker(d\pi),\qquad
e_a(\pi)=\pi_!\bigl(e(T_\pi E)^{a+1}\bigr)\in H^{2a}(B,\mathbb Z).$$
Here $\pi_!:H^{2a+2}(E,\mathbb Z)\to H^{2a}(B,\mathbb Z)$ is integration along the fibers. For $f:B'\to B$, naturality gives $e_a(f^*\pi)=f^*e_a(\pi)$.
:::

::: {.front card-id="tautological-mmm-sign" tags="formula"}
For a smooth family of complex curves, compare $e_a=\pi_!(e(T_\pi)^{a+1})$ with the cotangent convention $\widetilde\kappa_a=\pi_!(c_1(\omega_\pi)^{a+1})$.
:::

::: {.back card-id="tautological-mmm-sign"}
$$c_1(\omega_\pi)=-e(T_\pi),\qquad\widetilde\kappa_a=(-1)^{a+1}e_a.$$
Thus $e_0=2-2g$, $\widetilde\kappa_0=2g-2$, and $e_1=\widetilde\kappa_1$. Marked logarithmic $\kappa_a$ has the additional $\psi$-class terms.
:::

::: {.front card-id="tautological-generalized-mmm" tags="definition"}
Define a generalized MMM class for an oriented smooth bundle $\pi:E\to B$ with closed $d$-dimensional fibers and $c\in H^m(BSO(d),\mathbb Q)$.
:::

::: {.back card-id="tautological-generalized-mmm"}
$$\kappa_c(\pi)=\pi_!(c(T_\pi E))\in H^{m-d}(B,\mathbb Q).$$
For surface bundles, powers of the Euler class recover the ordinary MMM classes.
:::

::: {.front card-id="tautological-grading" tags="definition"}
State the cycle map for $\overline{\mathcal M}_{g,n}$ over $\mathbb C$, including its grading and coefficients. How do stabilizers enter stack integration?
:::

::: {.back card-id="tautological-grading"}
$$\operatorname{cl}:\operatorname{CH}^a(\overline{\mathcal M}_{g,n})_{\mathbb Q}
\longrightarrow H^{2a}(\overline{\mathcal M}_{g,n}^{\mathrm{an}},\mathbb Q).$$
A residual gerbe $BG$ for a finite group $G$ has degree $1/|G|$. These stabilizer factors enter intersection numbers on the stack; descent to the coarse space can require rational coefficients.
:::

::: {.front card-id="tautological-gluing" tags="definition"}
Describe the separating and nonseparating gluing maps for stable marked curves.
:::

::: {.back card-id="tautological-gluing"}
For $I\sqcup J=\{1,\ldots,n\}$, glue the extra marks in
$$\overline{\mathcal M}_{h,|I|+1}\times\overline{\mathcal M}_{g-h,|J|+1}\longrightarrow\overline{\mathcal M}_{g,n}.$$
For nonseparating gluing, identify the last two marks in
$$\overline{\mathcal M}_{g-1,n+2}\longrightarrow\overline{\mathcal M}_{g,n}.$$
All source factors must be stable.
:::

::: {.front card-id="tautological-boundary" tags="definition"}
Define the boundary divisor classes $\delta_{\mathrm{irr}}$ and $\delta_{h,I}$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-boundary"}
They are the fundamental classes of the closures of the one-node loci: respectively an irreducible curve with a nonseparating node, and a separating node with genus-$h$ component carrying marks $I$. Identify $\delta_{h,I}=\delta_{g-h,I^c}$. The total reduced boundary class $\delta$ sums each divisor once.
:::

::: {.front card-id="tautological-graphs" tags="formula"}
For a stable graph $\Gamma$, describe its gluing map and the class of its boundary-stratum closure.
:::

::: {.back card-id="tautological-graphs"}
$$\xi_\Gamma:\prod_{v\in V(\Gamma)}\overline{\mathcal M}_{g(v),n(v)}\to\overline{\mathcal M}_{g,n},\qquad
[\overline{\mathcal M}_\Gamma]=\frac1{|\operatorname{Aut}\Gamma|}\xi_{\Gamma*}(1).$$
Legs carry the marking labels, edges give nodes, $g=\sum_vg(v)+b_1(\Gamma)$, and the stratum has codimension $|E(\Gamma)|$.
:::

::: {.front card-id="tautological-ring" tags="definition"}
Define the tautological rings $R^*(\overline{\mathcal M}_{g,n})$ and describe their additive generators.
:::

::: {.back card-id="tautological-ring"}
They form the smallest system of unital subalgebras
$$R^*(\overline{\mathcal M}_{g,n})\subseteq\operatorname{CH}^*(\overline{\mathcal M}_{g,n})_{\mathbb Q}$$
containing the $\psi$-classes and closed under forgetful pushforwards and gluing pushforwards of external products.
Additive generators are decorated boundary strata
$$\xi_{\Gamma*}\left(\prod_{v\in V(\Gamma)}\alpha_v\right),$$
where each $\alpha_v$ is a monomial in $\psi$- and $\kappa$-classes on the factor indexed by $v$.
:::

::: {.front card-id="tautological-open-ring" tags="definition"}
For $j:\mathcal M_{g,n}\hookrightarrow\overline{\mathcal M}_{g,n}$ over $\mathbb C$, define the open tautological Chow ring and the tautological cohomology ring.
:::

::: {.back card-id="tautological-open-ring"}
$$R^*(\mathcal M_{g,n})=\operatorname{im}\left(j^*:R^*(\overline{\mathcal M}_{g,n})\to\operatorname{CH}^*(\mathcal M_{g,n})_{\mathbb Q}\right),$$
and
$$RH^{2*}(\mathcal M_{g,n})=\operatorname{cl}\bigl(R^*(\mathcal M_{g,n})\bigr)\subseteq H^{2*}(\mathcal M_{g,n},\mathbb Q).$$
Boundary-supported classes lie in $\ker j^*$. The kernel and cokernel of the restricted cycle map measure the difference between tautological Chow classes and cohomology.
:::

::: {.front card-id="tautological-psi-forgetting" tags="formula"}
Let $f:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$ forget the last marking. For $i\le n$, express $\psi_i^{(n+1)}$ in terms of $f^*\psi_i^{(n)}$.
:::

::: {.back card-id="tautological-psi-forgetting"}
$$\psi_i^{(n+1)}=f^*\psi_i^{(n)}+[D_{i,n+1}],$$
where $D_{i,n+1}$ parametrizes curves with a rational tail carrying marks $i,n+1$ and the attaching node. The morphism $f$ contracts this tail.
:::

::: {.front card-id="tautological-kappa-forgetting" tags="formula"}
Let $f:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$ forget the last marking. State the pullback formula for logarithmic $\kappa_a$, $a\ge0$.
:::

::: {.back card-id="tautological-kappa-forgetting"}
$$\kappa_a^{(n+1)}=f^*\kappa_a^{(n)}+\psi_{n+1}^a.$$
:::

::: {.front card-id="tautological-mumford-relation" tags="formula"}
State the relation between $\lambda_1$, $\widetilde\kappa_1$, the logarithmic $\kappa_1$, and the total reduced boundary class on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-mumford-relation"}
$$12\lambda_1=\widetilde\kappa_1+\delta,\qquad
\kappa_1=12\lambda_1-\delta+\sum_{i=1}^n\psi_i.$$
On $\mathcal M_g$, for $g\ge2$, this reduces to $\kappa_1=12\lambda_1$.
:::

::: {.front card-id="tautological-descendants" tags="definition"}
Define the descendant number $\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g$ for stable $(g,n)$ and state its dimension condition.
:::

::: {.back card-id="tautological-descendants"}
$$\langle\tau_{d_1}\cdots\tau_{d_n}\rangle_g=
\int_{\overline{\mathcal M}_{g,n}}\prod_i\psi_i^{d_i}.$$
A top-degree integral requires $d_i\ge0$ and $\sum_i d_i=3g-3+n$; descendant numbers in other degrees are set to zero.
:::

::: {.front card-id="tautological-genus-zero" tags="formula"}
Compute all top $\psi$-intersections on $\overline{\mathcal M}_{0,n}$ for $n\ge3$.
:::

::: {.back card-id="tautological-genus-zero"}
$$\int_{\overline{\mathcal M}_{0,n}}\prod_i\psi_i^{d_i}
=\frac{(n-3)!}{\prod_i d_i!}\qquad\left(\sum_i d_i=n-3\right).$$
:::

::: {.front card-id="tautological-elliptic-integrals" tags="formula"}
Compute $\int_{\overline{\mathcal M}_{1,1}}\psi_1$ and $\int_{\overline{\mathcal M}_{1,1}}\lambda_1$. Why can these be fractional?
:::

::: {.back card-id="tautological-elliptic-integrals"}
$$\psi_1=\lambda_1,\qquad
\int_{\overline{\mathcal M}_{1,1}}\psi_1=\int_{\overline{\mathcal M}_{1,1}}\lambda_1=\frac1{24}.$$
Integration is over the moduli stack and includes stabilizer weights.
:::

::: {.front card-id="tautological-string" tags="formula"}
State the string equation for descendant intersections, with stable target $(g,n)$.
:::

::: {.back card-id="tautological-string"}
$$\left\langle\tau_0\prod_{i=1}^n\tau_{d_i}\right\rangle_g
=\sum_{\substack{1\le j\le n\\d_j>0}}
\left\langle\tau_{d_j-1}\prod_{i\ne j}\tau_{d_i}\right\rangle_g.$$
:::

::: {.front card-id="tautological-dilaton" tags="formula"}
State the dilaton equation for descendant intersections, with stable target $(g,n)$.
:::

::: {.back card-id="tautological-dilaton"}
$$\left\langle\tau_1\prod_{i=1}^n\tau_{d_i}\right\rangle_g
=(2g-2+n)\left\langle\prod_{i=1}^n\tau_{d_i}\right\rangle_g.$$
:::

::: {.front card-id="tautological-examples" tags="application"}
Compute $\int_{\overline{\mathcal M}_{0,5}}\psi_1\psi_2$ and $\int_{\overline{\mathcal M}_{1,2}}\psi_1\psi_2$.
:::

::: {.back card-id="tautological-examples"}
The genus-zero formula gives
$$\int_{\overline{\mathcal M}_{0,5}}\psi_1\psi_2=\frac{2!}{1!\,1!}=2.$$
The dilaton equation gives
$$\int_{\overline{\mathcal M}_{1,2}}\psi_1\psi_2
=(2\cdot1-2+1)\int_{\overline{\mathcal M}_{1,1}}\psi_1=\frac1{24}.$$
:::

::: {.front card-id="tautological-sign-example" tags="application"}
For a smooth family of genus-three complex curves, compare $e_0$ and $\widetilde\kappa_0$. With two marked sections, what is logarithmic $\kappa_0$?
:::

::: {.back card-id="tautological-sign-example"}
$$e_0=-4,\qquad\widetilde\kappa_0=4,\qquad\kappa_0=6.$$
:::

::: {.front card-id="tautological-stable-mumford" tags="theorem"}
State the Madsen–Weiss theorem for the stable rational cohomology of the mapping class group.
:::

::: {.back card-id="tautological-stable-mumford"}
$$H^*(\Gamma_\infty,\mathbb Q)\cong\mathbb Q[e_1,e_2,\ldots],\qquad\deg e_i=2i,$$
where $e_i$ are the Miller–Morita–Mumford classes.
:::

