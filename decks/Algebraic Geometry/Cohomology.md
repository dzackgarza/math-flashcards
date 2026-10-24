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

::: {.front card-id="card-847e440e17d15caf"}
When is an invertible sheaf ample?
:::

::: {.back card-id="card-847e440e17d15caf"}
For $A$ Noetherian and $X\in \Sch_{/ {A}}$ proper, $\mcl$ is ample $\iff \forall \mcf\in \Coh(X)$ one has $H^i(\mcf\otimes\mcl^n) = 0$ for $n\gg 0$ and every $i > 0$.
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

::: {.front card-id="card-69f6f29eb7bd975c"}
Give a sufficient condition for the Leray spectral sequence to degenerate.
:::

::: {.back card-id="card-69f6f29eb7bd975c"}
$f:X\to Y$ smooth projective, by Deligne, as a consequence of Hard Lefschetz.
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

::: {.front card-id="card-610ae6d59c072f6d"}
Discuss $H^*({\mathbf{P}}^n; {\mathcal{O}}(d))$.
:::

::: {.back card-id="card-610ae6d59c072f6d"}
$k[x_0,\cdots, x_n]_d$ for $*=0$,

zero for $*=1,\cdots, n-1$, and

$\qty{\prod_{i=1}^n x_i }^{-1}k[x_0^{-1}, \cdots, x_n^{-1}]$ for $*=n$.
:::

::: {.front card-id="card-096a65dfbddd6a03"}
What is **Grothendieck vanishing**?
:::

::: {.back card-id="card-096a65dfbddd6a03"}
For $X$ a noetherian topological space, for all $\mcf\in \Sh(X, \Ab\Grp)$, one has
$$H^{i\geq \dim X+1}(X; \mcf) = 0.$$
How to remember: $\mathrm{cd}(X) \leq \dim X$.
:::

::: {.front card-id="card-87f4808bdfeea791"}
What is the Hirzebruch-Riemann-Roch theorem?
:::

::: {.back card-id="card-87f4808bdfeea791"}
$\chi(\mcf) = \int {\mathrm{ch}}(\mcf)\operatorname{Td}(X) = {\mathrm{ch}}_2(\mcf) + 2\operatorname{rank}(\mcf)$.
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
