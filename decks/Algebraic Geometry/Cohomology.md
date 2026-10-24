---
title: "Algebraic Geometry::Cohomology"
---

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
What is the **geometric genus** in full generality?
:::

::: {.back card-id="card-2578e6e4881e953d"}
$p_g(X) \coloneqq h^{n, 0}(X) \coloneqq h^0(\omega_X)$, the number of linearly-independent top forms.
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
For $X$ a Noetherian separated scheme and $\mcf\in \QCoh(X)$. (Thm 4.5) Alternatively, whenever $\mcf$ has no cohomology on any open in a cover $\mcu$.
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

::: {.front card-id="card-81d3dee3bf3d5a16"}
What is $H^i(X; {\mathcal{O}}_X(n))$ for $X \coloneqq{\mathbf{P}}^r_{/ {A}}$?
:::

::: {.back card-id="card-81d3dee3bf3d5a16"}
Write $\Gamma^*(\mcf) \coloneqq\bigoplus_{n\geq 0} H^0(X; {\mathcal{O}}_X(n))$ for the section ring, then $A[x_0,\cdots, x_r]  { \, \xrightarrow{\sim}\, }\Gamma({\mathcal{O}}_X)$ as graded rings. So $H^0(X; {\mathcal{O}}_X(n)) \cong A[x_0, \cdots, x_r]_n$, degree $n$ homogeneous polynomials over $A$.

$H^i(X; {\mathcal{O}}_X(n)) = 0$ for $0<i<r$ and every $n$.

$H^r(X; {\mathcal{O}}_X(-(r+1))) = A$.
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

For $X$ smooth proper of dimension $n$ and $\mcl$ locally free there is a perfect pairing
$$ H^i(X;\mcl) \otimes H^{n-i}(X; \mck\otimes\mcl {}^{ \vee }) \to H^n(X;\mck) \cong k\implies H^i(X;\mcl) \cong H^{n-i}(X; \mck\otimes\mcl {}^{ \vee }) {}^{ \vee }$$
For $\mcf\in \Coh(X)$ in general, it pairs $H^i(X,\mcf)$ with $\operatorname{Ext}^{n-i}(\mcf,\omega_X)$.

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
What is $\omega_X$ for $X = {\mathbf{P}}^n_{/ {A}}$? Derive it.
:::

::: {.back card-id="card-1ad7a8deaabeb009"}
Take determinants in the Euler exact sequence $\Omega^1_{X}\hookrightarrow{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  }\twoheadrightarrow{\mathcal{O}}_X$ to get $\operatorname{det}{\mathcal{O}}_X(-1){ {}^{ \scriptscriptstyle\oplus^{n+1} }  } = \omega_X \otimes{\mathcal{O}}_X = \omega_X$ and so $\omega_X = {\mathcal{O}}_X(-(n+1))$.
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
For $f:X\to Y$,
$$H^p\left(Y, {\mathbf{R}}^q f_* \mathbb{Q}\right) \Rightarrow H^{p+q}(X, \mathbb{Q})$$
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

::: {.front card-id="card-610ae6d59c072f6d" tags="formula"}
For $n\ge1$ and $d\in\mathbb Z$, compute every $h^i(\mathbb P^n_{\mathbb C},\mathcal O(d))$.
:::

::: {.back card-id="card-610ae6d59c072f6d"}
$$h^i(\mathbb P^n,\mathcal O(d))=\begin{cases}\binom{n+d}{n}&i=0,\ d\ge0,\\\binom{-d-1}{n}&i=n,\ d\le-n-1,\\0&\text{otherwise}.\end{cases}$$
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
Generally no, see Mumford's normal projective surface as a counterexample, or Raynaud finds for any smooth projective surface $X$ over $k=\kbar$ an $L\in \operatorname{Pic}(X)$ with $H^1(L\otimes\omega_X) \neq 0$.

However it *does* hold for K3s, using $H^1({\mathcal{O}}_X) = 0$ and any big and nef $L$ on a K3 is effective. This is explained by Deligne-Illusie for surfaces that lift to characteristic zero (which K3s do).
:::

::: {.front card-id="formula-projective-euler-polynomial" tags="formula"}
For $d\in\mathbb Z$ and $n\ge1$, compute $\chi(\mathbb P^n_{\mathbb C},\mathcal O(d))$ using a polynomial binomial coefficient.
:::

::: {.back card-id="formula-projective-euler-polynomial"}
$$\chi(\mathbb P^n,\mathcal O(d))=\binom{n+d}{n}.$$
:::

::: {.front card-id="formula-hilbert-leading-coefficients" tags="formula"}
For a smooth projective complex $n$-fold, $n\ge2$, and an ample divisor $H$, compute the leading two terms of $\chi(\mathcal O_X(mH))$.
:::

::: {.back card-id="formula-hilbert-leading-coefficients"}
$$\chi(\mathcal O_X(mH))=\frac{H^n}{n!}m^n-\frac{K_XH^{n-1}}{2(n-1)!}m^{n-1}+O(m^{n-2}).$$
:::

::: {.front card-id="formula-threefold-riemann-roch" tags="formula"}
For a divisor $D$ on a smooth projective complex threefold $X$, compute $\chi(\mathcal O_X(D))$.
:::

::: {.back card-id="formula-threefold-riemann-roch"}
$$\chi(\mathcal O_X(D))=\frac{D^3}{6}-\frac{K_XD^2}{4}+\frac{D(K_X^2+c_2(X))}{12}-\frac{K_Xc_2(X)}{24}.$$
:::

::: {.front card-id="formula-threefold-structure-euler" tags="formula"}
For a smooth projective complex threefold $X$, compute $\chi(\mathcal O_X)$ from its characteristic numbers.
:::

::: {.back card-id="formula-threefold-structure-euler"}
$$\chi(\mathcal O_X)=-\frac{K_Xc_2(X)}{24}.$$
:::

::: {.front card-id="formula-trivial-canonical-threefold-rr" tags="formula"}
For a divisor $D$ on a smooth projective complex threefold with $K_X\sim0$, compute $\chi(\mathcal O_X(D))$.
:::

::: {.back card-id="formula-trivial-canonical-threefold-rr"}
$$\chi(\mathcal O_X(D))=\frac{D^3}{6}+\frac{c_2(X)D}{12}.$$
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
