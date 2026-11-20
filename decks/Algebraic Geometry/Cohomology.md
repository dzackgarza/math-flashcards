---
title: "Algebraic Geometry::Cohomology"
---

::: {.front card-id="sequence-supports-localization" tags="formula application"}
State the cohomology-with-supports sequence for $Z\subset X$ closed and $U=X\setminus Z$. Compute it for $X=\operatorname{Spec}k[t]$, $Z=(t)$, and $F=\mathcal O_X$.
:::

::: {.back card-id="sequence-supports-localization"}
For an abelian sheaf $F$, $\Gamma_Z(X,F)=\ker(\Gamma(X,F)\to\Gamma(U,F))$ and $H_Z^i$ are its right derived functors. The sequence is
$$\cdots\to H_Z^i(X,F)\to H^i(X,F)\to H^i(U,F|_U)\to H_Z^{i+1}(X,F)\to\cdots.$$
Here $X,U$ are affine and $t$ is a nonzerodivisor, so
$$H_Z^0(X,\mathcal O)=0,\qquad
H_Z^1(X,\mathcal O)=k[t,t^{-1}]/k[t],\qquad H_Z^{i\ge2}(X,\mathcal O)=0.$$
The quotient records principal parts supported at the origin, not ordinary higher cohomology of the affine scheme.
:::

::: {.front card-id="sequence-sheaf-mayer-vietoris" tags="formula application"}
State sheaf-cohomological Mayer–Vietoris for $X=U\cup V$. Use the two standard affine charts to recover $H^1(\mathbb P^1,\mathcal O(-2))$.
:::

::: {.back card-id="sequence-sheaf-mayer-vietoris"}
For an abelian sheaf $F$,
$$\cdots\to H^i(X,F)\to H^i(U,F)\oplus H^i(V,F)\xrightarrow{\mathrm{res}_U-\mathrm{res}_V}H^i(U\cap V,F)\to H^{i+1}(X,F)\to\cdots.$$
Use $U=(x_0\ne0)$, $z=x_1/x_0$, and $V=(x_1\ne0)$. With frames $e_U=x_0^{-2}$ and $e_V=x_1^{-2}=z^{-2}e_U$,
$$H^1(\mathbb P^1,\mathcal O(-2))=
\frac{k[z,z^{-1}]}{k[z]+z^{-2}k[z^{-1}]}=k\cdot z^{-1}.$$
Affineness of the charts and their intersection kills the higher cohomology needed for this Čech computation.
:::

::: {.front card-id="formula-coherent-kunneth" tags="formula application"}
State coherent Künneth over a field. Compute all cohomology of $\mathcal O(2,-2)$ on $\mathbb P^1\times\mathbb P^1$, and $H^1(\mathcal O)$ on a product of curves.
:::

::: {.back card-id="formula-coherent-kunneth"}
For proper $k$-schemes $X,Y$ and coherent $F,G$,
$$H^n(X\times_kY,F\boxtimes G)
\cong\bigoplus_{p+q=n}H^p(X,F)\otimes_k H^q(Y,G),$$
where $F\boxtimes G=p_X^*F\otimes p_Y^*G$. Over a general base ring, derived tensor products and Tor terms replace this field formula.

For $\mathcal O(2,-2)$, the only nonzero group is $H^1\cong k^3$: $h^0(\mathcal O(2))=3$, $h^1(\mathcal O(-2))=1$. For smooth geometrically connected projective curves $C,D$,
$$H^1(C\times D,\mathcal O)=H^1(C,\mathcal O_C)\oplus H^1(D,\mathcal O_D),\qquad q(C\times D)=g(C)+g(D).$$
:::

::: {.front card-id="duality-torsion-sheaf-example" tags="application comparison"}
On a smooth projective curve $C/k$ with rational point $p$, compute $\mathcal H om(k(p),\omega_C)$ and $\operatorname{Ext}^1_C(k(p),\omega_C)$. Which Serre-duality formulation applies?
:::

::: {.back card-id="duality-torsion-sheaf-example"}
$$\mathcal H om(k(p),\omega_C)=0,\qquad
\operatorname{Ext}^1_C(k(p),\omega_C)\cong H^0(C,k(p))^\vee\cong k.$$
The first vanishes because $\omega_C$ is torsion-free. Locally resolve $k(p)$ by multiplication by a uniformizer on $\mathcal O_C$; dualizing gives a one-dimensional sheaf Ext at $p$.

The vector-bundle formula with $k(p)^\vee\otimes\omega_C$ would give zero and is inapplicable. Global Ext supplies the correct dual of $H^0(C,k(p))$.
:::

::: {.front card-id="vanishing-selection-table" tags="comparison application"}
For coherent cohomology, compare the hypotheses and outputs of affine acyclicity, Serre vanishing, Kodaira vanishing, Kawamata–Viehweg vanishing, and Kodaira–Akizuki–Nakano vanishing. What prevents using each without checking positivity or characteristic?
:::

::: {.back card-id="vanishing-selection-table"}
| Setting | Conclusion |
| --- | --- |
| $X$ affine, $F$ quasi-coherent | $H^{i>0}(X,F)=0$ |
| $X/k$ projective, $A$ ample, $F$ coherent | $\exists m_0(F,A)$: $H^{i>0}(X,F\otimes A^m)=0$ for every $m\ge m_0$ |
| $X/\mathbb C$ smooth projective, $A$ ample | $H^{i>0}(X,\omega_X\otimes A)=0$ |
| $X/\mathbb C$ smooth projective, $L$ nef and big | $H^{i>0}(X,\omega_X\otimes L)=0$ |
| $X/\mathbb C$ smooth projective of dimension $n$, $A$ ample | $H^q(X,\Omega_X^p\otimes A)=0$ for $p+q>n$ |

Serre gives no universal small twist. Kodaira and Kawamata–Viehweg concern canonical twists; they do not assert $H^{>0}(L)=0$ for every positive $L$. Nakano's boundary $p+q=n$ is excluded: $H^0(\mathbb P^1,\Omega^1(2))=k$. An elliptic curve has $H^1(\mathcal O)=k$, so replacing ample or nef-and-big by nef alone fails. Positive-characteristic Kodaira needs additional hypotheses.
:::

::: {.front card-id="application-projective-hypersurface-restriction" tags="application"}
Let $X=V(F_d)\subset\mathbb P^n_k$ be a degree-$d$ hypersurface, with $n\ge2$ and $d\ge1$. Does every section of $\mathcal O_X(m)$ extend to $\mathbb P^n$? Compute $h^0(X,\mathcal O_X(m))$ for $m\ge0$, and specialize to $m=2$ on a quartic surface.
:::

::: {.back card-id="application-projective-hypersurface-restriction"}
Use
$$0\longrightarrow\mathcal O_{\mathbb P^n}(m-d)\xrightarrow{\cdot F_d}\mathcal O_{\mathbb P^n}(m)\longrightarrow\mathcal O_X(m)\longrightarrow0.$$
Since $H^1(\mathbb P^n,\mathcal O(m-d))=0$ for $n\ge2$, restriction on sections is surjective for every integer $m$. Its kernel is $F_d$ times the degree-$(m-d)$ forms. For $m\ge0$,
$$h^0(X,\mathcal O_X(m))=\binom{n+m}{n}-\begin{cases}\binom{n+m-d}{n}&m\ge d,\\0&m<d.\end{cases}$$
For a quartic surface and $m=2$, the answer is $\binom52=10$.
:::

::: {.front card-id="application-projective-extension-obstruction" tags="application"}
Let $Z$ consist of four distinct points of $\mathbb P^1_{\mathbb C}$. Does every section of $\mathcal O_Z(1)$ extend to a section of $\mathcal O_{\mathbb P^1}(1)$? Identify the obstruction group and its dimension.
:::

::: {.back card-id="application-projective-extension-obstruction"}
The sequence
$$0\longrightarrow\mathcal O_{\mathbb P^1}(-3)\longrightarrow\mathcal O_{\mathbb P^1}(1)\longrightarrow\mathcal O_Z(1)\longrightarrow0$$
gives
$$0\longrightarrow\mathbb C^2\longrightarrow\mathbb C^4\longrightarrow H^1(\mathbb P^1,\mathcal O(-3))\longrightarrow0.$$
The obstruction space has dimension two. Only the image of the evaluation map extends. The vanishing used for hypersurfaces in $\mathbb P^n$ with $n\ge2$ fails here.
:::

::: {.front card-id="application-projective-complete-intersection-sections" tags="application"}
Let $C\subset\mathbb P^3_{\mathbb C}$ be a smooth complete intersection of a quadric and a cubic. Compute $h^0(C,\mathcal O_C(2))$ and $h^0(C,\mathcal O_C(3))$ by restricting ambient forms. What relations must be subtracted?
:::

::: {.back card-id="application-projective-complete-intersection-sections"}
The ideal has Koszul resolution
$$0\longrightarrow\mathcal O(-5)\longrightarrow\mathcal O(-2)\oplus\mathcal O(-3)\longrightarrow\mathcal I_C\longrightarrow0.$$
Intermediate cohomology of line bundles on $\mathbb P^3$ vanishes, so $H^1(\mathcal I_C(m))=0$ and restriction is surjective. In degree two the only relation is the defining quadric, giving $10-1=9$ sections. In degree three the relations are its four linear multiples and the defining cubic, giving $20-4-1=15$.
:::

::: {.front card-id="formula-bott-projective-differentials" tags="formula" cite="[@Mov21, Theorem 7.1]"}
For $n\ge1$, $0\le p\le n$, and $k\in\mathbb Z$, compute $h^q(\mathbb P^n_{\mathbb C},\Omega^p(k))$. Which twists have cohomology?
:::

::: {.back card-id="formula-bott-projective-differentials"}
Bott's formula is
$$h^q(\mathbb P^n,\Omega^p(k))=
\begin{cases}
\binom{n+k-p}{k}\binom{k-1}{p}&q=0,\ k>p,\\
1&q=p,\ k=0,\\
\binom{p-k}{-k}\binom{-k-1}{n-p}&q=n,\ k<p-n,\\
0&\text{otherwise}.
\end{cases}$$
For example, $\Omega^1_{\mathbb P^3}(1)$ is acyclic, $h^0(\Omega^1_{\mathbb P^3}(2))=6$, and $h^1(\Omega^1_{\mathbb P^3})=1$.
:::

::: {.front card-id="card-dc50c39867acc702"}
Why does ${}_{{\mathcal{O}}_X}\Mod$ have enough injectives?
:::

::: {.back card-id="card-dc50c39867acc702"}
For $\mcf\in   {}_{{\mathcal{O}}_X}\Mod$, the stalk $\mcf_{x} \in   {}_{{\mathcal{O}}_{X, x}}\Mod$ and module categories have enough injectives. So find $\mcf_x \hookrightarrow I_x$, let $j^x: \left\{{x}\right\} \hookrightarrow X$ and set $\mci\coloneqq\prod_{x\in x} j^x_*(I_x)$; claim this is injective. Check
$$\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}(\mcg, \mci) = \prod_{x\in X} \mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}(\mcg, j^x_* I_x) = \prod_{x\in X} \mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}(\mcg_x, I_x)$$
So one gets a sheaf morphism $\mcf\to \mci$ induced by $\mcf_x \to \mci_x$ which is injective. Claim: $\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({-}, \mci)$ is exact. Use that it is $\prod_{x\in X}({-})_x$, the product of stalk functors (which is exact) followed by $\mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}({-}, I_x)$ (which is exact). I.e. it's a composition of exact functors:
$$\mathop{\mathrm{Hom}}_{{\mathcal{O}}_X}({-}, \mci) = \mathop{\mathrm{Hom}}_{{\mathcal{O}}_{X, x}}({-}, I_x) \circ \prod_{x\in X} ({-})_x$$
:::

::: {.front card-id="card-6ebf3e3244b6ee35"}
What is the **higher direct image**?
:::

::: {.back card-id="card-6ebf3e3244b6ee35"}
Idea: for a family $f:X\to Y$, a form of relative cohomology of $X$ over $Y$ or cohomology along the fibers of $f$. $f_*: \Sh(X; \Ab\Grp)\to\Sh(Y; \Ab\Grp)$ left exact, so take right-derived functors. Can be computed using flasque resolutions.\
:::

::: {.front card-id="card-7c74fccd355ba8a2"}
Discuss **higher direct images**.
:::

::: {.back card-id="card-7c74fccd355ba8a2"}
If ${\mathbf{R}}^i f_* \mcf= 0$ for $i>0$ then $H^i(X; \mcf) { \, \xrightarrow{\sim}\, }H^i(Y, f_* \mcf)$. ${\mathbf{R}}^if_*(\mcf)$ is the sheafification of $V\mapsto H^i(f^{-1}(V); { \left.{{\mcf}} \right|_{{f^{-1}(V)}} })$.
:::

::: {.front card-id="card-8e70c9d4c2c1b1b1"}
Discuss higher direct images for morphisms $f:X\to \operatorname{Spec}A$.
:::

::: {.back card-id="card-8e70c9d4c2c1b1b1"}
Let $M_i \coloneqq H^i(X; \mcf)$, then ${\mathbf{R}}^i f_* \mcf= \tilde M_i$.
:::

::: {.front card-id="card-29097df5554a634a"}
Give examples of flasque sheaves.
:::

::: {.back card-id="card-29097df5554a634a"}
$\tilde M \in \QCoh(\operatorname{Spec}A)$ for $M\in   {}_{A}\Mod$ an injective object.
:::

::: {.front card-id="card-8e4c415bc760a4cd"}
What is a **fine** sheaf?
:::

::: {.back card-id="card-8e4c415bc760a4cd"}
Sheaves admitting a partition of unity: for any $\mcu\rightrightarrows X$ there exist $\phi_i: \mcf(U_i) \to \mcf(U)$ where for all $s\in\mcf(U)$ one has $\mathop{\mathrm{supp}}(s(U_i)) \subseteq U_i$ and $\sum_i \phi_i({ \left.{{s}} \right|_{{U_i}} }) = s$.

Equivalently: for every two disjoint $A, B\subseteq X$, there exists $f\in { \operatorname{End} }(\mcf)$ such that ${ \left.{{f}} \right|_{{A}} } = \operatorname{id}$ and ${ \left.{{f}} \right|_{{B}} } = 0$.

More generally, for all $\mcu\rightrightarrows X, \exists 1=\sum f_i$ subordinate to the cover.

Fine implies soft.
:::

::: {.front card-id="card-2578e6e4881e953d"}
What is the **geometric genus** for smooth and singular complex projective varieties?
:::

::: {.back card-id="card-2578e6e4881e953d"}
For $X$ smooth projective of dimension $n$ over $\mathbb C$, $p_g(X)\coloneqq h^{n,0}(X)=h^0(X,\omega_X)$, the number of linearly independent global top forms.

For $X$ singular integral projective over $\mathbb C$, its birational geometric genus is $p_g(\widetilde X)=h^0(\widetilde X,\omega_{\widetilde X})$ on a smooth projective resolution; this is independent of the resolution. It need not equal $h^0(X,\omega_X)$ for the dualizing sheaf. An integral nodal cubic has normalization $\mathbb P^1$ and geometric genus zero, while its dualizing sheaf is trivial and has a one-dimensional space of sections.
:::

::: {.front card-id="card-213db50f27de0ed0"}
What is **Cech cohomology**?
:::

::: {.back card-id="card-213db50f27de0ed0"}
For an open cover $\mcu\rightrightarrows X$, define
$$C^p(\mcu; \mcf) \coloneqq\prod_{I \coloneqq i_0 < \cdots < i_p} \mcf(U_{I}),\qquad U_{I} \coloneqq U_{i_1}\cap\cdots \cap U_{i_p}$$
with boundary map
$$(d\alpha)_{I} \coloneqq\sum_{0\leq k\leq p+1} (-1)^k \alpha_{I\setminus i_k}\mathrel{\Big|}_{U_I}$$
More explicitly,
$$C^p(\mcu; \mcf) = \prod_{i_1 < \cdots < i_p} \mcf(U_{i_1} \cap\cdots \cap U_{i_p})$$
So a $p\dash$chain is a collection of elements $\alpha_{i_1,\cdots, i_p} \in \mcf(U_{i_1\cdots i_p})$ for each $(p+1)\dash$tuple of elements $i_1 < \cdots < i_p$ in $I$ where $\mcu\coloneqq\left\{{U_i}\right\}_{i\in I}$. The boundary map is
$$(d \alpha)_{i_0, \ldots, i_{p+1}}=\sum_{k=0}^{p+1}(-1)^k \alpha_{i_0}, \ldots, \widehat{i}_k, \ldots, i_{p+1} \mathrel{\Big|}_{U_{i_0, \ldots, i_{p+1}}}$$
:::

::: {.front card-id="card-e0452aa13f84cac6"}
Give an example of a computation with Cech cohomology.
:::

::: {.back card-id="card-e0452aa13f84cac6"}
See example 4.0.3 on page 219 and example 4.0.4 for $S^1$.

$H^*({\mathbf{P}}^1; \Omega_{{\mathbf{P}}^1/k})$ over $k$: let $\mcu= \left\{{H_0, H_\infty}\right\}$ with coordinates $x$ and $1/x$, then:
$$\begin{align} 0 \to C^0 &\to C^1\to 0 \\ 0 \to {{\Gamma}\qty{H_0; \Omega} } \times {{\Gamma}\qty{H_\infty;\Omega} } &\to {{\Gamma}\qty{H_0\cap H_\infty;\Omega} } \\ 0 \to k[x]\,dx\times k[y]\,dy&\xrightarrow{d: x\mapsto x, y\mapsto 1/x, dy\mapsto -x^{-2}\,dx} k[x, x^{-1}]\,dx\to 0\end{align}$$
Then $\ker d = \left\langle{f(x)\,dx, g(y)\,dy}\right\rangle$ such that $f(x) = -x^{-2} g(x^{-1}) \implies f=g=0$ since one side is a polynomial in $x$ and the other is a polynomial in $1/x$ with no constant term, so $H^0 = 0$.

For $H^1$, check that $\operatorname{im}d = \left\langle{f(x) + x^{-2} g(x^{-1})\,dx}\right\rangle$ where $f,g$ are polynomials. This is the subspace of $k[x,x^{-1}]\,dx$ generated by $x^n\,dx$ for $n\in \ZZ\setminus\left\{{ -1 }\right\}$, so $H^1 = \left\langle{x^{-1}\,dx}\right\rangle$ is 1-dimensional.

The circle:
:::

::: {.front card-id="card-b3dc6977ff83178a"}
When does Cech cohomology compute sheaf cohomology?
:::

::: {.back card-id="card-b3dc6977ff83178a"}
For $X$ a Noetherian separated scheme and $\mcf\in \QCoh(X)$. Alternatively, whenever $\mcf$ has no cohomology on any open in a cover $\mcu$.
:::

::: {.front card-id="card-7b0ae0c2f2899228"}
What is **Serre's vanishing** characterization of affine schemes among Noetherian schemes?
:::

::: {.back card-id="card-7b0ae0c2f2899228"}
For $X\in \Sch$ Noetherian, $X$ is affine $\iff H^{i\geq 1}(X; \mcf) = 0$ for all $\mcg\in \QCoh(X)$ $\iff H^1(X; \mci) = 0$ for all coherent sheaves of ideals $\mci$.

Equivalently, $X$ is affine $\iff \mathrm{cd}(X) = 0$; this is the *cohomological dimension*, the least $n$ such that $H^i(\mcf) = 0$ for all $i> n$ and for all $\mcf\in \QCoh(X)$.

Another **Serre vanishing**: for $X \in \Sch_{/ {A}}$ projective and $A$ Noetherian with ${\mathcal{O}}_X(1)$ very ample over $\operatorname{Spec}A$, if $\mcf\in \Coh(X)$ then $H^i(\mcf(n)) = 0$ for $n\gg 0$ and every $i>0$.
:::

::: {.front card-id="card-9f661756ec76f08d"}
Discuss cohomology for $\QCoh(\operatorname{Spec}A)$.
:::

::: {.back card-id="card-9f661756ec76f08d"}
$H^{i\geq 1}(\operatorname{Spec}A, \mcf) = 0$ for any $\mcf\in \QCoh(\operatorname{Spec}A)$. Why: let $M = {{\Gamma}\qty{X; \mcf} }$ and take $M\hookrightarrow I$ an injective resolution in ${}_{A}\Mod$ to get an exact sequence $\tilde M \hookrightarrow\tilde I \in \QCoh(X)$. Check $\mcf\cong \tilde M$ by an early result and each $\tilde I^i$ is flasque thus $\Gamma\dash$acyclic, so use it to compute cohomology. Apply ${{\Gamma}\qty{X; {-}} }$ to $0\to \tilde M\to \tilde I$ to get $0\to M\to I\in   {}_{A}\Mod$ and thus $H^0(\mcf) = M$ and $H^i(\mcf) = 0$ for $i\geq 1$.
:::

::: {.front card-id="card-81d3dee3bf3d5a16" cite="[@The25, tag 01XS]"}
What is $H^i(X;\mathcal O_X(n))$ for $X\coloneqq\mathbb P^r_A$, with $r\ge1$?
:::

::: {.back card-id="card-81d3dee3bf3d5a16"}
Write $\Gamma_*(\mathcal O_X)\coloneqq\bigoplus_{n\ge0}H^0(X;\mathcal O_X(n))$ for the section ring. Then $A[x_0,\ldots,x_r]\xrightarrow{\sim}\Gamma_*(\mathcal O_X)$ as graded rings. So $H^0(X;\mathcal O_X(n))\cong A[x_0,\ldots,x_r]_n$, the degree-$n$ homogeneous polynomials over $A$; it is zero for $n<0$. In degree zero this gives $\Gamma(X,\mathcal O_X)=A$.

$H^i(X;\mathcal O_X(n))=0$ for $0<i<r$ and every $n$.

$H^r(X;\mathcal O_X(-(r+1)))=A$. More generally, $H^r(X;\mathcal O_X(n))=0$ for $n>-r-1$; otherwise it is free over $A$ with basis
$$x_0^{-a_0}\cdots x_r^{-a_r},\qquad a_i\ge1,\quad\sum_i a_i=-n.$$
Thus $\operatorname{rank}_A H^r(X;\mathcal O_X(n))=\binom{-n-1}{r}$ for $n\le-r-1$, and $H^i(X;\mathcal O_X(n))=0$ for $i>r$.
:::

::: {.front card-id="card-847e440e17d15caf" tags="theorem"}
For a line bundle $L$ on a proper scheme $X$ over a Noetherian affine base, state Serre's cohomological and global-generation criteria for ampleness.
:::

::: {.back card-id="card-847e440e17d15caf"}
The following are equivalent:

- $L$ is ample.
- For every coherent $\mathcal F$, $H^i(X,\mathcal F\otimes L^m)=0$ for $i>0$ and all sufficiently large $m$.
- For every coherent $\mathcal F$, the sheaf $\mathcal F\otimes L^m$ is globally generated for all sufficiently large $m$.
:::

::: {.front card-id="card-24f0f5d5999e4fbf" tags="definition"}
What is **Serre duality**? What is the dualizing sheaf?
:::

::: {.back card-id="card-24f0f5d5999e4fbf"}
For a smooth proper connected curve $X/k$, the dualizing sheaf is $\omega_X=\Omega^1_{X/k}$; for $X$ smooth proper of dimension $n$ it is $\mck = \omega_X = \Omega^n_{X/k}$.

For $X/k$ smooth proper of pure dimension $n$, with $H^0(X,\mathcal O_X)=k$, and $\mcl$ finite locally free there is a perfect pairing
$$ H^i(X;\mcl) \otimes H^{n-i}(X; \mck\otimes\mcl {}^{ \vee }) \to H^n(X;\mck) \cong k\implies H^i(X;\mcl) \cong H^{n-i}(X; \mck\otimes\mcl {}^{ \vee }) {}^{ \vee }$$
For $\mcf\in \Coh(X)$ in general, it pairs $H^i(X,\mcf)$ with $\operatorname{Ext}^{n-i}_X(\mcf,\omega_X)$. Without $H^0(X,\mathcal O_X)=k$, compose the cup product with the trace $H^n(X,\omega_X)\to k$; do not identify that cohomology group with $k$.

For curves and every invertible sheaf $L$,
$$H^0(C; \mcl) \cong H^1(C; \mck\otimes\mcl {}^{ \vee }) {}^{ \vee }, \qquad H^1(C,L)^\vee\cong H^0(C,\omega_C\otimes L^{-1}).$$
Consequence for dimensions:
$$h^i(X; \mcl) = h^{n-i}(X; \mck\otimes\mcl {}^{ \vee }),\qquad \chi(X; \mcl) = (-1)^n \chi(X; \mck\otimes\mcl {}^{ \vee })$$
:::

::: {.front card-id="card-69f8989719a40f16"}
How is $\operatorname{Pic}(X)$ related to cohomology?
:::

::: {.back card-id="card-69f8989719a40f16"}
$\operatorname{Pic}(X) \cong H^1(X; {\mathcal{O}}_X^{\times})$. Idea: use Cech cohomology, pick $\mcl\in \operatorname{Pic}(X)$, restrict to opens where ${ \left.{{\mcl}} \right|_{{U_i}} }$ is free, fix isos $\phi_i: {\mathcal{O}}_{U_i} { \, \xrightarrow{\sim}\, }{ \left.{{\mcl}} \right|_{{U_i}} }$, check that on $U_{ij}$ one gets isomorphisms $\phi_i^{-1}\phi_j: {\mathcal{O}}_{U_{ij}}{\circlearrowleft}$ which give an element in $\cechH(\mcu; {\mathcal{O}}_X^{\times})$, take a limit over all coverings.
:::

::: {.front card-id="card-822818bff1088759"}
What is the **exponential exact sequence**?
:::

::: {.back card-id="card-822818bff1088759"}
$$2\pi i \ZZ\hookrightarrow{\mathcal{O}}_X \twoheadrightarrow{\mathcal{O}}_X^{\times}$$
Since $H^1({\mathcal{O}}_X^{\times}) = \operatorname{Pic}(X)$, $\delta^1 = c_1({-}) \in H^2(2\pi i \ZZ)$ is the first Chern class.
:::

::: {.front card-id="card-1ad7a8deaabeb009"}
What is $\omega_{X/A}$ for $X=\mathbb P^n_A$? Derive it.
:::

::: {.back card-id="card-1ad7a8deaabeb009"}
Take determinants in the relative Euler exact sequence
$$0\longrightarrow\Omega^1_{X/A}\longrightarrow\mathcal O_X(-1)^{\oplus(n+1)}\longrightarrow\mathcal O_X\longrightarrow0$$
to get
$$\det\bigl(\mathcal O_X(-1)^{\oplus(n+1)}\bigr)
\cong\det\Omega^1_{X/A}\otimes\mathcal O_X
=\omega_{X/A}\otimes\mathcal O_X
\cong\omega_{X/A}.$$
The determinant on the left is the tensor product of $n+1$ copies of $\mathcal O_X(-1)$, so $\omega_{X/A}\cong\mathcal O_X(-(n+1))$.
:::

::: {.front card-id="card-00941d78f8260900"}
Compute the canonical sheaf for $Y$ a smooth hypersurface of degree $d$ in ${\mathbf{P}}^n$ for $n\geq 2$.
:::

::: {.back card-id="card-00941d78f8260900"}
Use that for $Y\hookrightarrow X$ one has $\omega_Y = \omega_X \otimes\operatorname{det}N_{Y/X} = \omega_X \otimes{\mathcal{O}}_X(Y) \otimes{\mathcal{O}}_Y$ for codimension 1 and $X = {\mathbf{P}}^n \implies \omega_X = {\mathcal{O}}_X(-n-1)$ and so
$$\omega_Y = {\mathcal{O}}_X(-n-1) \otimes{\mathcal{O}}_{{\mathbf{P}}^n}(Y) \otimes{\mathcal{O}}_Y = {\mathcal{O}}_Y(-n-1+d)$$
:::

::: {.front card-id="card-65cfb8efb1626b1d" tags="definition"}
What is: relation to the canonical sheaf
:::

::: {.back card-id="card-65cfb8efb1626b1d"}
On a smooth $n$-dimensional variety over a field, the canonical sheaf is $\omega_X=\bigwedge^n\Omega^1_{X/k}$, which is also the dualizing sheaf. On a singular scheme the dualizing object need not be an invertible sheaf.
:::

::: {.front card-id="card-66eb03a60b9bcd39"}
What is the Leray spectral sequence?
:::

::: {.back card-id="card-66eb03a60b9bcd39"}
For a continuous map $f:X\to Y$ and an abelian sheaf $F$ on $X$,
$$E_2^{p,q}=H^p(Y,R^qf_*F)\Longrightarrow H^{p+q}(X,F).$$
For schemes this applies to the underlying Zariski sheaves, including quasi-coherent modules. For complex varieties and $F=\mathbb Q$, use the analytic topology:
$$H^p(Y,R^qf_*\mathbb Q)\Longrightarrow H^{p+q}(X,\mathbb Q).$$
:::

::: {.front card-id="card-69f6f29eb7bd975c" tags="theorem"}
For a smooth projective morphism $f:X\to Y$ of complex varieties, at which page does the rational singular-cohomology Leray spectral sequence degenerate?
:::

::: {.back card-id="card-69f6f29eb7bd975c"}
Deligne's theorem gives degeneration at $E_2$ for
$$E_2^{p,q}=H^p(Y,R^qf_*\mathbb Q)\Longrightarrow H^{p+q}(X,\mathbb Q).$$
:::

::: {.front card-id="card-7a13c1f152bea481"}
What is **Serre vanishing**?
:::

::: {.back card-id="card-7a13c1f152bea481"}
For $X$ a Noetherian scheme, $X$ is affine $\iff H^{i>0}(X; \mcf) = 0$ for all $\mcf\in \QCoh(X) \iff H^1(X; \mci) = 0$ for all coherent sheaves of ideals on $X$.
:::

::: {.front card-id="card-2629a4068afdc432"}
Discuss $H^0({\mathbf{P}}^m; {\mathcal{O}}(n))$ for $n\in \ZZ$.
:::

::: {.back card-id="card-2629a4068afdc432"}
The section ring is given by $\bigoplus_{n\geq 0} H^0({\mathbf{P}}^m; {\mathcal{O}}(n)) \cong k[x_0,\cdots, x_m]$ as graded rings. Thus $H^0({\mathcal{O}}) = k$ and $H^0({\mathcal{O}}(n))$ are degree $n$ polynomials, so is generated by the monomials of total degree $n$ -- this is a stars and bars argument; the number of monomials in $R[x_1,\cdots, x_N]$ of degree $D$ is ${N+D-1\choose D}$. Here $N = m+1$ and $D = n$, so we get ${m+d\choose d}$.

How this count goes: represent as $a^3b^2d^2e \leadsto \bullet \bullet \bullet \mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\mathrel{\Big|}\bullet \bullet \mathrel{\Big|}\bullet$. Note that there are no sections for $n < 0$. In general, ${\mathcal{O}}(n)$ corresponds to the $n\dash$uple/Veronese embedding ${\mathbf{P}}^n \to {\mathbf{P}}^N$.
:::

::: {.front card-id="card-938f2d52c80bd08e"}
Prove that if $X$ is a projective variety, $H^0(X; {\mathcal{O}}_X) = k$
:::

::: {.back card-id="card-938f2d52c80bd08e"}
Since ${\mathbf{P}}^n$ is proper, $X\subseteq {\mathbf{P}}^n$ is proper as a closed subvariety. So $s\in H^0(X; {\mathcal{O}}_X)$ is the same as a regular map $s: X\to {\mathbf{A}}^1$.

By properness, $\operatorname{im}s \subseteq {\mathbf{A}}^1$ is closed and thus a finite set of points since ${\mathbf{A}}^1$ has the cofinite topology.

By irreducibility, it must be one point, so $s$ is a constant map $s(x) = \lambda$ for some $\lambda \in k$, so sections biject with elements of $k$.
:::


::: {.front card-id="card-096a65dfbddd6a03"}
What is **Grothendieck vanishing**?
:::

::: {.back card-id="card-096a65dfbddd6a03"}
For $X$ a noetherian topological space, for all $\mcf\in \Sh(X, \Ab\Grp)$, one has
$$H^{i\geq \dim X+1}(X; \mcf) = 0.$$
How to remember: $\mathrm{cd}(X) \leq \dim X$.
:::

::: {.front card-id="card-87f4808bdfeea791" tags="formula"}
For a vector bundle $E$ on a smooth projective complex variety $X$, compute $\chi(X,E)$ by Hirzebruch–Riemann–Roch.
:::

::: {.back card-id="card-87f4808bdfeea791"}
$$\chi(X,E)=\int_X\operatorname{ch}(E)\operatorname{td}(T_X).$$
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
No. Raynaud constructs smooth projective surfaces in positive characteristic with an ample $L$ and $H^1(X,\omega_X\otimes L)\ne0$; this is an existence result, not a claim about every surface. Singular examples, such as normal surfaces in Mumford's work, do not by themselves disprove the smooth theorem.

A sufficient condition (Deligne–Illusie): $X/k$ smooth projective over a perfect field of characteristic $p$, $\dim X<p$, and $X$ lifts smoothly to $W_2(k)$. Then Kodaira vanishing holds. K3 surfaces admit such lifts; this criterion applies to them for $p>2$. The inequality excludes characteristic two for surfaces, so it cannot settle that case.
:::






::: {.front card-id="theorem-proper-coherence" tags="theorem"}
Let $f:X\to Y$ be proper between locally Noetherian schemes and $\mathcal F$ coherent on $X$. State Grothendieck's coherence theorem.
:::

::: {.back card-id="theorem-proper-coherence"}
Every higher direct image $R^if_*\mathcal F$ is coherent, for $i\ge0$.
:::

::: {.front card-id="theorem-cohomology-semicontinuity" tags="theorem"}
Let $f:X\to S$ be proper, with $S$ locally Noetherian, and let $\mathcal F$ be coherent and flat over $S$. State the variation of fiber cohomology dimensions and Euler characteristics.
:::

::: {.back card-id="theorem-cohomology-semicontinuity"}
For each $i$, the function $s\mapsto h^i(X_s,\mathcal F_s)$ is upper semicontinuous, so
$$\{s:h^i(X_s,\mathcal F_s)\ge r\}$$
is closed for every $r$. The function $s\mapsto\chi(X_s,\mathcal F_s)$ is locally constant.
:::

::: {.front card-id="theorem-cohomology-base-change" tags="theorem"}
Let $f:X\to S$ be proper, $S$ locally Noetherian, and $\mathcal F$ coherent and flat over $S$. What does surjectivity of the fiber base-change map $\beta_s^i$ imply?
:::

::: {.back card-id="theorem-cohomology-base-change"}
For the canonical map
$$\beta_s^i:(R^if_*\mathcal F)\otimes\kappa(s)\longrightarrow H^i(X_s,\mathcal F_s),$$
surjectivity implies that $\beta_s^i$ is an isomorphism. After restricting to a neighborhood of $s$, formation of $R^if_*\mathcal F$ commutes with base change in degree $i$.
:::

::: {.front card-id="theorem-grauert-local-freeness" tags="theorem"}
Let $f:X\to S$ be proper, $S$ reduced and locally Noetherian, and $\mathcal F$ coherent and flat over $S$. If $h^i(X_s,\mathcal F_s)$ is locally constant, what follows? Does fiber-dimension constancy alone suffice on a nonreduced base?
:::

::: {.back card-id="theorem-grauert-local-freeness"}
The sheaf $R^if_*\mathcal F$ is locally free and its formation commutes with base change. On a nonreduced base, constancy of the dimensions on residue-field fibers alone does not imply these conclusions.
:::

::: {.front card-id="theorem-formal-functions" tags="theorem"}
Let $A$ be Noetherian, $I\subset A$ an ideal, $X\to\operatorname{Spec}A$ proper, and $\mathcal F$ coherent. State the theorem on formal functions.
:::

::: {.back card-id="theorem-formal-functions"}
There is a natural isomorphism
$$H^i(X,\mathcal F)^\wedge_I\cong\varprojlim_n H^i(X,\mathcal F/I^n\mathcal F).$$
Applied over a local base, this computes the completed stalk of $R^if_*\mathcal F$ from the infinitesimal neighborhoods of the fiber.
:::

::: {.front card-id="theorem-grothendieck-duality" tags="theorem"}
For a proper morphism $f:X\to Y$ of Noetherian schemes in the Grothendieck-duality setting, state the adjunction and internal derived-Hom identity for $F\in D^b_{\mathrm{coh}}(X)$ and $G\in D^+_{\mathrm{qc}}(Y)$.
:::

::: {.back card-id="theorem-grothendieck-duality"}
The functor $f^!$ is right adjoint to $Rf_*$. Under these duality hypotheses,
$$R\mathcal Hom_Y(Rf_*F,G)\simeq Rf_*R\mathcal Hom_X(F,f^!G).$$
:::

::: {.front card-id="theorem-relative-serre-duality" tags="theorem"}
For a smooth proper morphism $f:X\to Y$ of relative dimension $n$ between Noetherian schemes, compute $f^!\mathcal O_Y$. State relative Serre duality for a vector bundle $E$ when the relevant direct images are locally free and commute with base change.
:::

::: {.back card-id="theorem-relative-serre-duality"}
One has
$$f^!\mathcal O_Y\simeq\omega_{X/Y}[n],\qquad (R^if_*E)^\vee\cong R^{n-i}f_*(E^\vee\otimes\omega_{X/Y}).$$
:::

::: {.front card-id="theorem-kodaira-vanishing" tags="theorem"}
Let $X$ be a smooth complex projective variety and $L$ an ample line bundle. State Kodaira vanishing.
:::

::: {.back card-id="theorem-kodaira-vanishing"}
One has
$$H^i(X,\omega_X\otimes L)=0\qquad(i>0).$$
:::

::: {.front card-id="theorem-kawamata-viehweg" tags="theorem"}
Let $(X,\Delta)$ be a projective klt pair over $\mathbb C$ and $D$ an integral Cartier divisor with $D-(K_X+\Delta)$ nef and big. State Kawamata–Viehweg vanishing.
:::

::: {.back card-id="theorem-kawamata-viehweg"}
One has
$$H^i(X,\mathcal O_X(D))=0\qquad(i>0).$$
:::

::: {.front card-id="theorem-nadel-vanishing" tags="theorem"}
Let $X$ be smooth complex projective, $L$ an integral divisor, and $D$ an effective $\mathbb Q$-divisor with $L-D$ nef and big. State Nadel vanishing using the multiplier ideal $\mathcal J(X,D)$.
:::

::: {.back card-id="theorem-nadel-vanishing"}
One has
$$H^i\left(X,\mathcal O_X(K_X+L)\otimes\mathcal J(X,D)\right)=0\qquad(i>0).$$
:::

::: {.front card-id="theorem-kollar-torsion-free" tags="theorem"}
Let $f:X\to Y$ be a surjective projective morphism of complex varieties, with $X$ smooth projective and $Y$ normal. State Kollár's torsion-freeness theorem and its implication for sections supported on proper closed subsets.
:::

::: {.back card-id="theorem-kollar-torsion-free"}
Each $R^if_*\omega_X$ is torsion-free. Thus a section of this sheaf that vanishes at the generic point is zero; a nonzero section cannot be supported on a proper closed subset.
:::

::: {.front card-id="theorem-kollar-vanishing" tags="theorem"}
Let $f:X\to Y$ be surjective and projective over $\mathbb C$, with $X$ smooth projective and $Y$ normal. For an ample line bundle $A$ on $Y$, state Kollár vanishing.
:::

::: {.back card-id="theorem-kollar-vanishing"}
For every $i\ge0$,
$$H^j(Y,R^if_*\omega_X\otimes A)=0\qquad(j>0).$$
:::

::: {.front card-id="theorem-grauert-riemenschneider" tags="theorem"}
For a projective birational morphism $f:X\to Y$ of complex varieties, with $X$ smooth and $Y$ normal, state Grauert–Riemenschneider vanishing.
:::

::: {.back card-id="theorem-grauert-riemenschneider"}
One has
$$R^if_*\omega_X=0\qquad(i>0).$$
:::

::: {.front card-id="theorem-derived-projection-formula" tags="theorem"}
Let $f:X\to Y$ be proper between Noetherian schemes, $F\in D_{\mathrm{qc}}(X)$, and $G$ a perfect complex on $Y$. State the derived projection formula.
:::

::: {.back card-id="theorem-derived-projection-formula"}
There is a natural isomorphism
$$Rf_*(F\otimes^{\mathbf L}Lf^*G)\simeq Rf_*F\otimes^{\mathbf L}G.$$
:::

::: {.front card-id="theorem-grothendieck-riemann-roch" tags="theorem"}
For a proper morphism $f:X\to Y$ between smooth complex varieties and $E\in K_0(X)$, state Grothendieck–Riemann–Roch in the rational Chow ring.
:::

::: {.back card-id="theorem-grothendieck-riemann-roch"}
With $f_!$ the alternating sum of higher direct images,
$$\operatorname{ch}(f_!E)\operatorname{td}(T_Y)=f_*\left(\operatorname{ch}(E)\operatorname{td}(T_X)\right).$$
:::

::: {.front card-id="application-curve-vanishing-boundary" tags="application"}
Let $C$ be a smooth connected projective complex curve of genus $g\ge2$. Compare $H^1(C,L)$ for $\deg L=2g-1$ with $H^1(C,K_C)$. Choose a method that detects the boundary case.
:::

::: {.back card-id="application-curve-vanishing-boundary"}
Serre duality gives $h^1(L)=h^0(K_C\otimes L^{-1})$. For $\deg L=2g-1$, the latter line bundle has degree $-1$, so $h^1(L)=0$. For $L=K_C$, it is $\mathcal O_C$, so $h^1(K_C)=1$. Positivity of $\deg K_C$ itself does not give vanishing for $K_C$.
:::

::: {.front card-id="application-kodaira-ample-twist" tags="application"}
Let $X$ be a smooth projective complex variety and $A$ ample. Which theorem computes $H^i(X,K_X+2A)$ for $i>0$, and which positivity condition must be checked?
:::

::: {.back card-id="application-kodaira-ample-twist"}
Kodaira vanishing gives $H^i(X,\mathcal O_X(K_X+2A))=0$ for $i>0$, since $2A$ is ample. The positive bundle is the twist $2A$ of the canonical bundle; no positivity of $K_X+2A$ itself is required.
:::

::: {.front card-id="application-vanishing-nef-big-blowup" tags="application"}
On $S=\operatorname{Bl}_p\mathbb P^2_{\mathbb C}$ let $H$ be the pullback of a line and $E$ the exceptional curve. Determine $H^i(S,\mathcal O_S(-2H+E))$ for $i>0$. Choose a vanishing theorem and explain why Kodaira's ample-twist hypothesis does not apply directly.
:::

::: {.back card-id="application-vanishing-nef-big-blowup"}
Here $K_S=-3H+E$, so $-2H+E=K_S+H$. The class $H$ is nef and big, since it is pulled back from an ample class by a birational map and $H^2=1$. It is not ample because $HE=0$. Kawamata–Viehweg vanishing, with boundary zero, therefore gives $H^i(S,\mathcal O_S(-2H+E))=0$ for $i>0$.
:::

::: {.front card-id="application-nadel-restriction-surjectivity" tags="application"}
Let $X$ be smooth complex projective, $D$ an effective $\mathbb Q$-divisor, and $L$ an integral divisor with $L-D$ nef and big. Suppose $\mathcal J(X,D)=\mathcal I_Z$ for a zero-dimensional subscheme $Z$. Can every section of $\mathcal O_Z(K_X+L)$ be extended to $X$? Choose a theorem and the exact-sequence step needed.
:::

::: {.back card-id="application-nadel-restriction-surjectivity"}
Nadel vanishing gives $H^1(X,\mathcal O_X(K_X+L)\otimes\mathcal I_Z)=0$. The long exact sequence of
$$0\to\mathcal O_X(K_X+L)\otimes\mathcal I_Z\to\mathcal O_X(K_X+L)\to\mathcal O_Z(K_X+L)\to0$$
therefore makes $H^0(X,\mathcal O_X(K_X+L))\to H^0(Z,\mathcal O_Z(K_X+L))$ surjective.
:::

::: {.front card-id="application-cohomology-jump-degree-zero" tags="application"}
Fix an elliptic curve $E/\mathbb C$. As $L$ varies in $\operatorname{Pic}^0(E)$, compute $h^0(E,L)$ and $h^1(E,L)$. Does their variation violate semicontinuity or constancy of Euler characteristic?
:::

::: {.back card-id="application-cohomology-jump-degree-zero"}
For $L\ne\mathcal O_E$, a nonzero section would give an effective divisor of degree zero and hence trivialize $L$, so $h^0(L)=0$. Serre duality and $K_E\cong\mathcal O_E$ give $h^1(L)=0$. At $\mathcal O_E$, both dimensions are one. They jump up on a closed subset, as upper semicontinuity permits; $\chi(L)=0$ throughout.
:::

::: {.front card-id="application-grauert-positive-degree" tags="application"}
Let $f:\mathcal C\to S$ be a smooth projective family of connected genus-$g$ complex curves over a reduced locally Noetherian base. Let $\mathcal L$ have degree $d>2g-2$ on every fiber. Determine the rank of $f_*\mathcal L$ and whether its fibers are the spaces of sections.
:::

::: {.back card-id="application-grauert-positive-degree"}
Fiberwise Serre duality gives $H^1(\mathcal C_s,\mathcal L_s)=0$, and Riemann–Roch gives $h^0(\mathcal L_s)=d+1-g$. Grauert's theorem makes $f_*\mathcal L$ locally free of rank $d+1-g$, with
$$f_*\mathcal L\otimes\kappa(s)\cong H^0(\mathcal C_s,\mathcal L_s).$$
Its formation commutes with base change.
:::

::: {.front card-id="application-relative-duality-curves" tags="application"}
For a smooth projective family $f:\mathcal C\to S$ of connected complex curves of genus $g$, the sheaf $f_*\omega_{\mathcal C/S}$ is locally free. Identify the vector bundle dual to it and its rank. Which theorem supplies the pairing?
:::

::: {.back card-id="application-relative-duality-curves"}
Relative Serre duality supplies the perfect pairing and gives
$$R^1f_*\mathcal O_{\mathcal C}\cong(f_*\omega_{\mathcal C/S})^\vee.$$
Both bundles have rank $g$, and the fiber pairing is $H^1(C_s,\mathcal O_{C_s})\times H^0(C_s,K_{C_s})\to\kappa(s)$.
:::

::: {.front card-id="application-kollar-leray-twist" tags="application"}
Let $f:X\to Y$ be a surjective projective morphism of complex projective varieties, with $X$ smooth and $Y$ normal. If $A$ is ample on $Y$, express $H^k(X,\omega_X\otimes f^*A)$ using a single higher direct image on $Y$. Explain why the Leray spectral sequence has only one contributing term.
:::

::: {.back card-id="application-kollar-leray-twist"}
The projection formula identifies $R^if_*(\omega_X\otimes f^*A)$ with $R^if_*\omega_X\otimes A$. Kollár vanishing kills $H^j(Y,R^if_*\omega_X\otimes A)$ for every $j>0$. Thus the Leray spectral sequence gives
$$H^k(X,\omega_X\otimes f^*A)\cong H^0(Y,R^kf_*\omega_X\otimes A).$$
:::

::: {.front card-id="application-birational-canonical-direct-images" tags="application"}
Let $f:X\to Y$ be projective birational over $\mathbb C$, with $X$ smooth and $Y$ normal. Must the sheaves $R^if_*\omega_X$ vanish for $i>0$, or are they only torsion-free? Choose the result that uses birationality.
:::

::: {.back card-id="application-birational-canonical-direct-images"}
Grauert–Riemenschneider vanishing gives $R^if_*\omega_X=0$ for $i>0$. Kollár's theorem supplies torsion-freeness in the more general surjective projective setting. Birationality permits the stronger conclusion here.
:::

::: {.front card-id="application-formal-functions-vanishing" tags="application"}
Let $f:X\to\operatorname{Spec}A$ be proper, with $(A,\mathfrak m)$ Noetherian local, and $\mathcal F$ coherent. Suppose $H^1(X,\mathcal F/\mathfrak m^n\mathcal F)=0$ for every $n\ge1$. Must $H^1(X,\mathcal F)$ vanish? Explain both the completion step and the finiteness step.
:::

::: {.back card-id="application-formal-functions-vanishing"}
Formal functions gives
$$\widehat{H^1(X,\mathcal F)}\cong\varprojlim_n H^1(X,\mathcal F/\mathfrak m^n\mathcal F)=0.$$
Proper coherence makes $M=H^1(X,\mathcal F)$ a finite $A$-module. Nakayama gives $\widehat M=0\Rightarrow M/\mathfrak mM=0\Rightarrow M=0$.
:::

::: {.front card-id="application-grr-finite-etale-curves" tags="application"}
Let $f:C\to B$ be a finite étale map of degree $d$ between smooth connected projective complex curves. Use Grothendieck–Riemann–Roch for $f$ to compute $\operatorname{ch}(f_*\mathcal O_C)$ and then relate the genera.
:::

::: {.back card-id="application-grr-finite-etale-curves"}
Since $f$ is finite, higher direct images vanish; since it is étale, $T_C=f^*T_B$. GRR and the projection formula give
$$\operatorname{ch}(f_*\mathcal O_C)\operatorname{td}(T_B)=f_*f^*\operatorname{td}(T_B)=d\,\operatorname{td}(T_B).$$
The Todd class is invertible, so $\operatorname{ch}(f_*\mathcal O_C)=d$: the bundle has rank $d$ and degree zero. Curve Riemann–Roch yields $1-g(C)=d(1-g(B))$.
:::

::: {.front card-id="theorem-castelnuovo-mumford-regularity" tags="theorem"}
For a coherent sheaf $\mathcal F$ on $\mathbb P^n_k$, state the cohomological criterion for $m$-regularity and the Castelnuovo–Mumford consequences for generation and multiplication of sections.
:::

::: {.back card-id="theorem-castelnuovo-mumford-regularity"}
The criterion is $H^i(\mathbb P^n,\mathcal F(m-i))=0$ for every $i>0$. It implies that $\mathcal F(m)$ is globally generated, that $\mathcal F$ is $(m+j)$-regular for all $j\ge0$, and that
$$H^0(\mathcal F(m+j))\otimes_k H^0(\mathcal O_{\mathbb P^n}(1))\longrightarrow H^0(\mathcal F(m+j+1))$$
is surjective for every $j\ge0$.
:::

::: {.front card-id="application-regularity-plane" tags="application"}
A coherent sheaf $\mathcal F$ on $\mathbb P^2_k$ satisfies $H^1(\mathcal F(2))=H^2(\mathcal F(1))=0$. What follows for $\mathcal F(3)$ and for multiplication of sections in twists at least three?
:::

::: {.back card-id="application-regularity-plane"}
These are the conditions for $3$-regularity. Thus $\mathcal F(3)$ is globally generated, and
$$H^0(\mathcal F(t))\otimes H^0(\mathcal O(1))\twoheadrightarrow H^0(\mathcal F(t+1))\qquad(t\ge3).$$
All higher twists remain regular in their corresponding degrees.
:::

::: {.front card-id="theorem-flat-base-change-qcoh" tags="theorem" cite="[@The25, tag 02KH]"}
Let $f:X\to S$ be quasi-compact and quasi-separated, $g:S'\to S$ flat, and $\mathcal F$ quasi-coherent. Set $X'=X\times_S S'$ with projections $g':X'\to X$ and $f':X'\to S'$. State flat base change.
:::

::: {.back card-id="theorem-flat-base-change-qcoh"}
The natural maps are isomorphisms for all $i\ge0$:
$$g^*R^if_*\mathcal F\xrightarrow{\sim}R^if'_*g'^*\mathcal F.$$
For $S=\operatorname{Spec}A$ and $S'=\operatorname{Spec}B$, this gives $H^i(X,\mathcal F)\otimes_A B\simeq H^i(X',g'^*\mathcal F)$.
:::

::: {.front card-id="application-base-change-localization-or-fiber" tags="application"}
Let $f:X\to\operatorname{Spec}A$ be quasi-compact and quasi-separated, and $\mathcal F$ quasi-coherent. Compare base change of $R^if_*\mathcal F$ along $A\to A_a$ and along $A\to A/\mathfrak m$. Which comparison is automatically an isomorphism?
:::

::: {.back card-id="application-base-change-localization-or-fiber"}
Localization is flat, so its comparison map is an isomorphism in every degree. A residue-field quotient need not be flat, so the same conclusion does not follow for the fiber. For a proper morphism with a coherent, base-flat sheaf, cohomology and base change gives a separate criterion using surjectivity of the fiber comparison map.
:::

::: {.front card-id="theorem-relative-kawamata-viehweg" tags="theorem"}
Let $f:X\to S$ be a projective morphism of complex varieties with $X$ smooth. State relative Kawamata–Viehweg vanishing for an $f$-nef and $f$-big Cartier divisor $D$. Give the klt-pair formulation.
:::

::: {.back card-id="theorem-relative-kawamata-viehweg"}
One has
$$R^if_*\mathcal O_X(K_X+D)=0\qquad(i>0).$$
More generally, if $(X,\Delta)$ is klt and $L$ is Cartier with $L-(K_X+\Delta)$ $f$-nef and $f$-big, then $R^if_*\mathcal O_X(L)=0$ for $i>0$.
:::

::: {.front card-id="card-8fbc1391d742152d" tags="definition"}
What is the definition of Boundary map?
:::

::: {.back card-id="card-8fbc1391d742152d"}
(1) The differential $d^p:C^p\to C^{p+1}$ of a cochain complex, satisfying $d^{p+1}d^p=0$. For a cover $\mathcal U$, the Cech boundary is $(d\alpha)_{i_0\cdots i_{p+1}}=\sum_{k=0}^{p+1}(-1)^k\alpha_{i_0\cdots\widehat{i_k}\cdots i_{p+1}}|_{U_{i_0\cdots i_{p+1}}}$. (2) The connecting homomorphism $\delta:H^i(X;A)\to H^{i+1}(X;B)$ in the long exact cohomology sequence associated to a short exact sequence $0\to A\to C\to B\to0$ of sheaves or complexes.
:::

::: {.front card-id="card-cbb51ea779e62068" tags="definition"}
What is the definition of Cochain complex?
:::

::: {.back card-id="card-cbb51ea779e62068"}
A sequence $\cdots\to C^{p-1}\xrightarrow{d^{p-1}}C^p\xrightarrow{d^p}C^{p+1}\to\cdots$ with $d^p\circ d^{p-1}=0$. Its cohomology is $H^p=\ker d^p/\operatorname{im}d^{p-1}$.
:::

::: {.front card-id="card-292a7ed29c8d5ef7" tags="definition"}
What is the definition of Coherent cohomology?
:::

::: {.back card-id="card-292a7ed29c8d5ef7"}
The sheaf cohomology $H^i(X,\mathcal F)$ of a coherent sheaf $\mathcal F$. If $X$ is proper over a field $k$, each $H^i(X,\mathcal F)$ is a finite-dimensional $k$-vector space and vanishes for $i>\dim X$.
:::

::: {.front card-id="card-f393f575f3af05fc" tags="definition"}
What is the definition of Cohomological dimension?
:::

::: {.back card-id="card-f393f575f3af05fc"}
$\operatorname{cd}(X)=\sup\{i:H^i(X,\mathcal F)\ne 0\text{ for some }\mathcal F\in\QCoh(X)\}$, the least $n$ with $H^i(X,\mathcal F)=0$ for all $i>n$ and all quasi-coherent $\mathcal F$. A Noetherian scheme is affine iff $\operatorname{cd}(X)=0$, and $\operatorname{cd}(X)\le\dim X$.
:::

::: {.front card-id="card-debc17b90ede1af4" tags="definition"}
What is the definition of Cohomology?
:::

::: {.back card-id="card-debc17b90ede1af4"}
For a sheaf of abelian groups $\mathcal F$ on a topological space or site $X$, the right derived functors $H^i(X,\mathcal F)=R^i\Gamma(X,\mathcal F)$ of the global-sections functor. On a ringed space one takes the derived functors on $\mathcal O_X$-modules.
:::

::: {.front card-id="card-6c6ea1b06a591184" tags="definition"}
What is the definition of Derived category?
:::

::: {.back card-id="card-6c6ea1b06a591184"}
The localization $D(\mathcal A)$ of the category of cochain complexes in an abelian category $\mathcal A$ at quasi-isomorphisms. $D^+(\mathcal A)$ and $D^b(\mathcal A)$ denote bounded-below and bounded complexes; $D^b_{\mathrm{coh}}(X)$ is the bounded derived category of coherent $\mathcal O_X$-modules.
:::

::: {.front card-id="card-26755feeae63650a" tags="definition"}
What is the definition of Derived functor?
:::

::: {.back card-id="card-26755feeae63650a"}
For a left exact additive functor $F$ and an object $A$, choose an injective resolution $0\to A\to I^0\to I^1\to\cdots$ and set $R^iF(A)=H^i(F(I^\bullet))$; this is independent of the resolution. For $F=\Gamma(X,-)$ these are sheaf cohomology, and for $F=f_*$ they are higher direct images.
:::

::: {.front card-id="card-1b12dca96188a8d0" tags="definition"}
What is the definition of Derived tensor product?
:::

::: {.back card-id="card-1b12dca96188a8d0"}
The left derived functor of $\otimes$: $A\otimes^{\mathbf L}B$ is computed by replacing one complex by a complex of flat (or locally free) objects and taking the total tensor product. It defines a symmetric monoidal structure on the derived category.
:::

::: {.front card-id="card-f2a8b1dc3e6c159c" tags="definition"}
What is the definition of Exceptional inverse image?
:::

::: {.back card-id="card-f2a8b1dc3e6c159c"}
The functor $f^!:\mathcal D^+(\mathcal O_Y)\to\mathcal D^+(\mathcal O_X)$ right adjoint to $Rf_*$. For smooth proper $f$ of relative dimension $n$, $f^!(-)\cong f^*(-)\otimes\omega_{X/Y}[n]$; it is the derived form of the dualizing sheaf.
:::

::: {.front card-id="card-0e0e8171f106c2e4" tags="definition"}
What is the definition of Ext group?
:::

::: {.back card-id="card-0e0e8171f106c2e4"}
$\operatorname{Ext}^i_{\mathcal O_X}(\mathcal F,\mathcal G)=R^i\operatorname{Hom}_{\mathcal O_X}(\mathcal F,\mathcal G)$. If $\mathcal F$ is locally free, $\operatorname{Ext}^i(\mathcal F,\mathcal G)\cong H^i(X,\mathcal F^\vee\otimes\mathcal G)$; Serre duality pairs $H^i(X,\mathcal F)$ with $\operatorname{Ext}^{n-i}(\mathcal F,\omega_X)$.
:::

::: {.front card-id="card-054789bf4f93a9c2" tags="definition"}
What is the definition of First chern class?
:::

::: {.back card-id="card-054789bf4f93a9c2"}
For a line bundle $L$, $c_1(L)\in H^2(X,\mathbb Z)$ is the image of $[L]$ under the connecting map of $0\to 2\pi i\mathbb Z\to\mathcal O_X\to\mathcal O_X^\times\to 0$. For a divisor $D$, $c_1(\mathcal O_X(D))=[D]$.
:::

::: {.front card-id="card-b9494859d64b64cc" tags="definition"}
What is the definition of Kodaira vanishing?
:::

::: {.back card-id="card-b9494859d64b64cc"}
If $X$ is a smooth projective variety over a field of characteristic zero and $L$ is an ample line bundle, then $H^i(X,\omega_X\otimes L)=0$ for all $i>0$.
:::

::: {.front card-id="card-019bda55018f2843" tags="definition"}
What is the definition of Relative canonical sheaf?
:::

::: {.back card-id="card-019bda55018f2843"}
For a smooth morphism $f:X\to Y$ of relative dimension $n$, $\omega_{X/Y}=\det\Omega^1_{X/Y}$. If $X,Y$ are smooth over a common field, $\omega_{X/Y}\cong\omega_X\otimes f^*\omega_Y^{-1}$. In the Grothendieck-duality setting, $f^!\mathcal O_Y\cong\omega_{X/Y}[n]$.
:::

::: {.front card-id="card-88b7b071a0ca4f33" tags="definition"}
What is the definition of Serre duality?
:::

::: {.back card-id="card-88b7b071a0ca4f33"}
For $X/k$ smooth proper of pure dimension $n$ and $\mathcal F$ finite locally free, cup product followed by trace gives a perfect pairing
$$H^i(X,\mathcal F)\otimes H^{n-i}(X,\mathcal F^\vee\otimes\omega_X)\to H^n(X,\omega_X)\xrightarrow{\operatorname{tr}}k.$$
Thus $H^i(X,\mathcal F)^\vee\cong H^{n-i}(X,\mathcal F^\vee\otimes\omega_X)$. For coherent $\mathcal F$, replace the right factor by global $\operatorname{Ext}^{n-i}_X(\mathcal F,\omega_X)$. The trace is an isomorphism when $H^0(X,\mathcal O_X)=k$, for example when $X$ is geometrically connected.
:::

::: {.front card-id="card-96d703b5df7fceea" tags="definition"}
What is the definition of Sheaf cohomology?
:::

::: {.back card-id="card-96d703b5df7fceea"}
The cohomology $H^i(X,\mathcal F)=R^i\Gamma(X,\mathcal F)$ of an $\mathcal O_X$-module $\mathcal F$, computed from an injective resolution $0\to\mathcal F\to I^0\to I^1\to\cdots$ as $H^i(\Gamma(X,I^\bullet))$.
:::

::: {.front card-id="card-f233125835acf997" tags="definition"}
What is the definition of Soft sheaf?
:::

::: {.back card-id="card-f233125835acf997"}
A sheaf $\mathcal F$ for which every section over a closed subset $A\subset X$ extends to a neighborhood of $A$, equivalently $\mathcal F(X)\to\mathcal F(A)$ is surjective for every closed $A$. Fine sheaves are soft, and soft sheaves are $\Gamma$-acyclic.
:::

::: {.front card-id="card-434a8b44fd60b9cd" tags="definition"}
What is the definition of Trace map?
:::

::: {.back card-id="card-434a8b44fd60b9cd"}
(1) The map $\operatorname{tr}:Rf_*\omega_{X/Y}[n]\to\mathcal O_Y$, equivalently $H^n(X,\omega_X)\to k$ for proper smooth $X/k$, that defines the Serre duality pairing $H^i(X,L)\times H^{n-i}(X,\omega_X\otimes L^\vee)\to k$. (2) For a dualizable object $M$, the composite $1\to M\otimes M^\vee\cong M^\vee\otimes M\to 1$, which yields traces of endomorphisms of $M$.
:::
