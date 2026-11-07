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
Define the cotangent-line bundle and $\psi_i$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-psi"}
$$L_i=s_i^*\omega_\pi,\qquad \psi_i=c_1(L_i)\in\operatorname{CH}^1(\overline{\mathcal M}_{g,n})_{\mathbb Q}.$$
At $[C,p_1,\ldots,p_n]$, its fiber is $T_{p_i}^*C$. The markings lie in the smooth locus, even when $C$ is nodal.
:::

::: {.front card-id="tautological-lambda" tags="definition"}
Define the Hodge bundle and the classes $\lambda_j$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-lambda"}
$$\mathbb E=\pi_*\omega_\pi,\qquad\operatorname{rank}\mathbb E=g,\qquad\lambda_j=c_j(\mathbb E)\in\operatorname{CH}^j(\overline{\mathcal M}_{g,n})_{\mathbb Q}.$$
The fiber is $H^0(C,\omega_C)$. Here $\lambda_0=1$ and $\lambda_j=0$ for $j>g$.
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
Define $\widetilde\kappa_a$ using the untwisted relative dualizing sheaf. Compare it with $\kappa_a$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-kappa-tilde"}
$$\widetilde\kappa_a=\pi_*(c_1(\omega_\pi)^{a+1}),\qquad
\kappa_a=\widetilde\kappa_a+\sum_{i=1}^n\psi_i^a.$$
For $a=0$, interpret $\psi_i^0=1$. The two conventions agree when there are no markings.
:::

::: {.front card-id="tautological-kappa-zero" tags="formula"}
Compute $\kappa_0$ and $\widetilde\kappa_0$ on $\overline{\mathcal M}_{g,n}$.
:::

::: {.back card-id="tautological-kappa-zero"}
$$\kappa_0=(2g-2+n)\,1,\qquad\widetilde\kappa_0=(2g-2)\,1.$$
They are the fiber degrees of the logarithmic and untwisted dualizing bundles.
:::

::: {.front card-id="tautological-mmm" tags="definition"}
For a smooth oriented bundle $\pi:E\to B$ of closed genus-$g$ surfaces, define the tangent-convention Miller–Morita–Mumford class $e_a$.
:::

::: {.back card-id="tautological-mmm"}
$$T_\pi E=\ker(d\pi),\qquad e_a=\pi_!\bigl(e(T_\pi E)^{a+1}\bigr)\in H^{2a}(B,\mathbb Z).$$
Fiber integration lowers real cohomological degree by $2$. These characteristic classes are natural under pullback of surface bundles.
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
Where do algebraic tautological classes and their topological cycle classes live? What degree corresponds to codimension $a$?
:::

::: {.back card-id="tautological-grading"}
Use $\operatorname{CH}^a(\overline{\mathcal M}_{g,n})_{\mathbb Q}$ and its cycle map to $H^{2a}(\overline{\mathcal M}_{g,n}^{\mathrm{an}},\mathbb Q)$. Algebraic codimension $a$ corresponds to real cohomological degree $2a$. Stack intersection numbers include automorphism weights; integral stack classes need not descend integrally to the coarse space.
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
Define the system of tautological rings $R^*(\overline{\mathcal M}_{g,n})$.
:::

::: {.back card-id="tautological-ring"}
It is the smallest system of unital $\mathbb Q$-subalgebras of the Chow rings containing the $\psi$-classes and closed under pushforward by forgetful maps and gluing maps, using external products on gluing sources. Equivalently, it is additively spanned by gluing pushforwards of monomials in $\psi$- and $\kappa$-classes on vertex factors.
:::

::: {.front card-id="tautological-open-ring" tags="definition"}
How is $R^*(\mathcal M_{g,n})$ related to the compactified tautological ring? Must tautological Chow classes exhaust cohomology?
:::

::: {.back card-id="tautological-open-ring"}
It is the image of $R^*(\overline{\mathcal M}_{g,n})$ under restriction to the smooth-curve locus. Boundary-supported classes restrict to zero. The tautological cohomology ring is the image under the cycle map; neither equality with all cohomology nor injectivity of that map is part of the definition.
:::

::: {.front card-id="tautological-psi-forgetting" tags="formula"}
For $f:\overline{\mathcal M}_{g,n+1}\to\overline{\mathcal M}_{g,n}$, compare the upstairs $\psi_i$ with $f^*\psi_i$, for $i\le n$.
:::

::: {.back card-id="tautological-psi-forgetting"}
$$\psi_i^{(n+1)}=f^*\psi_i^{(n)}+[D_{i,n+1}].$$
The divisor $D_{i,n+1}$ has a rational tail carrying exactly marks $i,n+1$ and its attaching node; that tail is contracted by $f$.
:::

::: {.front card-id="tautological-kappa-forgetting" tags="formula"}
State the pullback formula for the logarithmic $\kappa_a$ under forgetting the last mark.
:::

::: {.back card-id="tautological-kappa-forgetting"}
$$\kappa_a^{(n+1)}=f^*\kappa_a^{(n)}+\psi_{n+1}^a.$$
For $a=0$, this increases $2g-2+n$ by one.
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
$$\int_{\overline{\mathcal M}_{0,5}}\psi_1\psi_2=2,\qquad
\int_{\overline{\mathcal M}_{1,2}}\psi_1\psi_2=\frac1{24}.$$
Use the genus-zero factorial formula and the dilaton equation, respectively.
:::

::: {.front card-id="tautological-sign-example" tags="application"}
For a smooth family of genus-three complex curves, compare $e_0$ and $\widetilde\kappa_0$. With two marked sections, what is logarithmic $\kappa_0$?
:::

::: {.back card-id="tautological-sign-example"}
$$e_0=-4,\qquad\widetilde\kappa_0=4,\qquad\kappa_0=6.$$
:::

::: {.front card-id="tautological-stable-mumford" tags="theorem"}
What does the Madsen–Weiss theorem imply for the stable rational cohomology of the mapping class group?
:::

::: {.back card-id="tautological-stable-mumford"}
$$H^*(\Gamma_\infty,\mathbb Q)=\mathbb Q[e_1,e_2,\ldots],\qquad\deg e_i=2i.$$
The classes are MMM classes. This stable statement does not assert that the finite-genus compactified moduli stack has a freely generated tautological ring.
:::

