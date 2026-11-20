---
title: "Algebraic Geometry::Sheaves and Vector Bundles"
---

::: {.front card-id="sequence-relative-tangent-kodaira-spencer" tags="formula construction application"}
For a smooth morphism $f:X\to S$ of smooth complex varieties, state the relative cotangent and tangent sequences. How does restriction to a proper fiber define the Kodaira–Spencer map? Compare a product family with a varying family of elliptic curves.
:::

::: {.back card-id="sequence-relative-tangent-kodaira-spencer"}
$$0\to f^*\Omega_S^1\to\Omega_X^1\to\Omega_{X/S}^1\to0,\qquad
0\to T_{X/S}\to T_X\to f^*T_S\to0.$$
The cotangent quotient is locally free, so dualization remains exact. On a proper fiber $X_s$, the connecting homomorphism gives
$$T_sS\longrightarrow H^1(X_s,T_{X_s}),$$
by sending $v$ to the boundary of the constant section $1\otimes v$ of $\mathcal O_{X_s}\otimes T_sS$. It measures the first-order variation of complex structure.

For $X=C\times S$, the sequences split and this map is zero. For a smooth elliptic family where $dj_s\ne0$ and $j(s)\notin\{0,1728\}$, the Kodaira–Spencer map is nonzero: the coarse $j$-coordinate is a local deformation parameter there. At the special automorphism values, $dj=0$ alone does not prove infinitesimal triviality.
:::

::: {.front card-id="sequence-cotangent-complex-transitivity" tags="formula comparison"}
State cotangent-complex transitivity and explain how it corrects the ordinary conormal sequence. Give a singular hypersurface example where the left conormal map is injective.
:::

::: {.back card-id="sequence-cotangent-complex-transitivity"}
For $X\xrightarrow fY\to S$,
$$Lf^*L_{Y/S}\to L_{X/S}\to L_{X/Y}\to Lf^*L_{Y/S}[1].$$
For a regular closed immersion $i:Z\hookrightarrow X$ with $X/S$ smooth,
$$L_{Z/S}\simeq[I/I^2\xrightarrow{d}\Omega^1_{X/S}|_Z]$$
in degrees $-1,0$. Its degree-zero cohomology is $\Omega^1_{Z/S}$; its degree-minus-one cohomology is the kernel of the conormal map.

For the cusp $Z=(y^2-x^3)\subset\mathbb A^2_{\mathbb C}$,
$$\mathcal O_Z\longrightarrow\mathcal O_Z\,dx\oplus\mathcal O_Z\,dy,\qquad
1\longmapsto-3x^2dx+2y\,dy$$
is injective because $\mathcal O_Z$ is a domain. Yet $Z$ is singular at the origin: $\Omega_Z^1$ is not locally free there. Left injectivity does not characterize smoothness.
:::

::: {.front card-id="sequence-ideal-divisor-tor" tags="formula comparison application"}
State the ideal-sheaf and effective-Cartier-divisor sequences. What happens after tensoring by a coherent sheaf $F$? Test restriction to the divisor itself.
:::

::: {.back card-id="sequence-ideal-divisor-tor"}
For $i:Z\hookrightarrow X$ with ideal $I_Z$,
$$0\to I_Z\to\mathcal O_X\to i_*\mathcal O_Z\to0.$$
For an effective Cartier divisor $D$, $I_D=\mathcal O_X(-D)$, hence
$$0\to\mathcal T or_1^X(F,\mathcal O_D)\to F(-D)\to F\to i_*i^*F\to0.$$
The Tor term vanishes if the local equation of $D$ acts injectively on $F$, in particular if $F$ is locally free. For $F=\mathcal O_D$, that multiplication map is zero and
$$\mathcal T or_1^X(\mathcal O_D,\mathcal O_D)\cong\mathcal O_D(-D).$$
Thus tensoring a short exact sequence need not preserve its left injection.
:::

::: {.front card-id="sequence-koszul-regular-section" tags="construction application"}
Construct the Koszul resolution of the zero scheme of a regular section of a rank-$r$ vector bundle. What fails for a nonregular sequence? Recover a complete-intersection canonical bundle.
:::

::: {.back card-id="sequence-koszul-regular-section"}
For $s\in H^0(X,E)$ whose local components form a regular sequence, with zero scheme $Z$,
$$0\to\bigwedge^rE^\vee\to\cdots\to E^\vee\xrightarrow{s}\mathcal O_X\to\mathcal O_Z\to0.$$
The differential is contraction by $s$. A nonregular sequence can have nonzero Koszul homology: for $(x,x)$ in $k[x]$, the cycle $(1,-1)$ is not a boundary, since boundaries are multiples of $(x,-x)$.

For a smooth complete intersection of degrees $d_1,\ldots,d_r$ in $\mathbb P^n$,
$$N_{Z/\mathbb P^n}=\bigoplus_j\mathcal O_Z(d_j),\qquad
\omega_Z=\mathcal O_Z\left(\sum_jd_j-n-1\right).$$
A smooth $(2,3)$ curve in $\mathbb P^3$ has $\omega_C=\mathcal O_C(1)$ and $2g-2=6$, hence $g=4$.
:::

::: {.front card-id="sequence-evaluation-modification" tags="construction application"}
Define the evaluation sequence of a globally generated line bundle and an elementary modification of a vector bundle on a smooth curve. Compute examples on $\mathbb P^1$.
:::

::: {.back card-id="sequence-evaluation-modification"}
For a globally generated line bundle $L$ on a proper $k$-scheme,
$$0\to M_L\to H^0(X,L)\otimes_k\mathcal O_X\xrightarrow{\mathrm{ev}}L\to0.$$
The kernel is locally free of rank $h^0(L)-1$, with $\det M_L=L^{-1}$. For $L=\mathcal O_{\mathbb P^1}(1)$, $M_L=\mathcal O(-1)$; for a basepoint-free pencil $V\subset H^0(L)$, the same rank-one kernel is $L^{-1}$ after choosing a basis of $V$.

On a smooth curve, a quotient $E\twoheadrightarrow k(p)$ gives
$$0\to E'\to E\to k(p)\to0,\qquad
\operatorname{rk}E'=\operatorname{rk}E,\quad\deg E'=\deg E-[k(p):k].$$
Locally at $p$, $E'\cong\mathfrak m_p\oplus\mathcal O^{r-1}$, hence is locally free. For projection of $\mathcal O_{\mathbb P^1}^{\oplus2}$ onto the first fiber at a rational point, $E'=\mathcal O(-1)\oplus\mathcal O$.
:::

::: {.front card-id="sequence-residue-logarithmic" tags="formula application"}
State the residue sequence for a smooth divisor $i:D\hookrightarrow X$ in a smooth complex variety. Give its local map and compute logarithmic differentials on $\mathbb P^1$ with two marked points.
:::

::: {.back card-id="sequence-residue-logarithmic"}
For $p\ge1$,
$$0\to\Omega_X^p\to\Omega_X^p(\log D)\xrightarrow{\operatorname{Res}}i_*\Omega_D^{p-1}\to0.$$
Locally $D=(z_1=0)$: $\operatorname{Res}((dz_1/z_1)\wedge\alpha+\beta)=\alpha|_D$, with $\alpha,\beta$ regular. In top degree this gives
$$0\to\omega_X\to\omega_X(D)\to i_*\omega_D\to0.$$
For an SNC divisor $D=\sum D_j$, the $p=1$ quotient is $\bigoplus_j\mathcal O_{D_j}$.

On $(\mathbb P^1,\{0,\infty\})$, $\Omega^1(\log D)=\mathcal O$, generated by $dz/z$, with residues $(1,-1)$. The connecting map $k^2\to H^1(\Omega^1)\cong k$ is the sum of residues, under the residue normalization of the trace.
:::

::: {.front card-id="sequence-principal-parts" tags="definition construction application"}
Define the first-principal-parts bundle $P^1(L)$ of a line bundle on a smooth $k$-variety, and state its exact sequence. What does splitting mean? Evaluate jets of $\mathcal O_{\mathbb P^1}(d)$.
:::

::: {.back card-id="sequence-principal-parts"}
For the diagonal ideal $I_\Delta\subset\mathcal O_{X\times_kX}$ and projections $p_1,p_2$,
$$P^1(L)=p_{1*}\big((\mathcal O_{X\times X}/I_\Delta^2)\otimes p_2^*L\big),\qquad
0\to\Omega_X^1\otimes L\to P^1(L)\to L\to0.$$
A splitting as $\mathcal O_X$-modules is equivalent to an algebraic connection on $L$. Over $\mathbb C$, the extension class is the Atiyah class, represented by $d\log$ of the transition functions, up to the chosen Čech sign convention.

The fiber at a rational point records value and first derivatives. For $\mathbb P^1$, $d\ge1$,
$$H^0(\mathcal O(d))\twoheadrightarrow P^1(\mathcal O(d))_p,\qquad
\dim\ker=d-1.$$
The kernel is $H^0(\mathcal O(d)(-2p))$. Constants ($d=0$) cannot prescribe an arbitrary first derivative.
:::

::: {.front card-id="sheaf-adjunction-formula-table" tags="formula comparison"}
For a morphism of ringed spaces $f:X\to Y$, state pullback–pushforward and tensor–Hom adjunctions. Distinguish sheaf Hom from global Hom and their derived versions.
:::

::: {.back card-id="sheaf-adjunction-formula-table"}
For modules $E$ on $Y$ and $F,G,H$ on $X$,
$$\operatorname{Hom}_X(f^*E,F)=\operatorname{Hom}_Y(E,f_*F),\qquad
\mathcal H om_X(F\otimes G,H)=\mathcal H om_X(F,\mathcal H om_X(G,H)).$$
Global Hom is $\Gamma(X,\mathcal H om_X(F,G))$. For finite locally free $F$,
$$\mathcal H om_X(F,G)=F^\vee\otimes G;$$
this formula is not valid for arbitrary coherent $F$.

In derived categories of modules,
$$\operatorname{Hom}_{D(X)}(Lf^*E,F)=\operatorname{Hom}_{D(Y)}(E,Rf_*F),$$
$$R\mathcal H om(F\otimes^{\mathbf L}G,H)
\simeq R\mathcal H om(F,R\mathcal H om(G,H)).$$
For perfect $F$, $R\mathcal H om(F,G)=F^\vee\otimes^{\mathbf L}G$, where $F^\vee=R\mathcal H om(F,\mathcal O_X)$.
:::

::: {.front card-id="sheaf-exactness-tensor-dual" tags="comparison application"}
Which of inverse image, module pullback, pushforward, tensor, and sheaf Hom preserve exact sequences? Explain the Tor and Ext corrections using a point on $\mathbb A^1$.
:::

::: {.back card-id="sheaf-exactness-tensor-dual"}
| Functor | Exactness |
| --- | --- |
| $f^{-1}$ on abelian sheaves | Exact |
| $f^*$ on modules | Right exact; exact for flat $f$ |
| $f_*$ on abelian sheaves | Left exact |
| $f_*$ on quasi-coherent modules for affine $f$ | Exact |
| $F\otimes-$ | Right exact; exact for flat $F$ |
| $\mathcal H om(F,-)$ | Left exact; exact for finite locally free $F$ |

Tensoring $0\to A\to B\to C\to0$ adds $\mathcal T or_1(C,F)$ on the left. Applying $\mathcal H om(-,\mathcal O)$ gives
$$0\to C^\vee\to B^\vee\to A^\vee\to\mathcal E xt^1(C,\mathcal O).$$
Over $R=k[t]$, dualizing $0\to R\xrightarrow{t}R\to k\to0$ gives $\operatorname{Hom}_R(k,R)=0$ and $\operatorname{Ext}^1_R(k,R)=k$. Tensoring it with $k$ makes the map $k\xrightarrow{t}k$ zero and gives $\operatorname{Tor}_1^R(k,k)=k$.
:::

::: {.front card-id="sheaf-projection-classical" tags="formula application"}
State the ordinary and higher-direct-image projection formulas with a vector bundle on the base. Compute $R^q p_*\mathcal O(a,b)$ for $p:\mathbb P^1\times\mathbb P^1\to\mathbb P^1$ the first projection.
:::

::: {.back card-id="sheaf-projection-classical"}
For a morphism of schemes $f:X\to Y$, a finite locally free $E$ on $Y$, and an $\mathcal O_X$-module $F$,
$$R^qf_*(F\otimes f^*E)\cong R^qf_*F\otimes E\qquad(q\ge0).$$
The $q=0$ map sends $s\otimes e$ to $s\otimes f^*e$. For nonflat factors use the derived formula with its hypotheses; ordinary tensor products can lose Tor terms.

Over a field $k$,
$$R^qp_*\mathcal O(a,b)=\mathcal O(a)\otimes_k H^q(\mathbb P^1,\mathcal O(b)).$$
Thus $p_*\mathcal O(2,-2)=0$, $R^1p_*\mathcal O(2,-2)=\mathcal O(2)$, and $h^1(\mathbb P^1\times\mathbb P^1,\mathcal O(2,-2))=3$.
:::

::: {.front card-id="definition-sheaf-degree-slope" tags="definition application"}
Define degree and slope for a torsion-free sheaf on a polarized smooth projective variety. How does the choice of polarization enter?
:::

::: {.back card-id="definition-sheaf-degree-slope"}
Let $X$ have dimension $n\ge1$, let $H$ be an ample divisor, and let $E$ be torsion-free of positive rank $r$. Its determinant is $(\bigwedge^rE)^{**}$, a line bundle on smooth $X$. Define
$$\deg_H(E)=c_1(E)\cdot H^{n-1},\qquad \mu_H(E)=\frac{\deg_H(E)}r.$$
On a curve this is the usual determinant degree and requires no polarization. In higher dimension $c_1(E)$ is a class, and intersecting with $H^{n-1}$ turns it into a number.

On $\mathbb P^1\times\mathbb P^1$, with $H=\mathcal O(a,b)$ and $a,b>0$, the degree of $\mathcal O(u,v)$ is $ub+va$. Thus changing $H$ can change slope comparisons. Rank-zero sheaves do not have a slope under this definition.
:::

::: {.front card-id="definition-reduced-hilbert-stability" tags="definition application"}
Define the reduced Hilbert polynomial and explain how it enters Gieseker stability. How does it compare with slope stability?
:::

::: {.back card-id="definition-reduced-hilbert-stability"}
For a nonzero coherent sheaf $E$ on a polarized projective scheme, write
$$P_E(m)=a_dm^d+\cdots+a_0,\qquad a_d>0.$$
Its reduced Hilbert polynomial is $p_E=P_E/a_d$ in the monic convention. Dividing instead by the multiplicity $d!a_d$ is another convention; for fixed dimension it gives the same comparisons.

A pure sheaf $E$ is Gieseker semistable if every nonzero proper subsheaf $F$ satisfies $p_F(m)\le p_E(m)$ for all sufficiently large $m$; stability uses strict inequality. Compare coefficients starting with the highest degree where they differ.

For torsion-free sheaves on a smooth polarized projective variety, the first nonconstant comparison after the common leading term is slope. Hence slope stable implies Gieseker stable, and Gieseker semistable implies slope semistable. On curves the two notions agree. On surfaces equal slopes can leave different constant terms, involving $c_2$ through Riemann–Roch.
:::

::: {.front card-id="application-slope-p1-splitting" tags="application"}
For $E=\mathcal O_{\mathbb P^1}(a)\oplus\mathcal O_{\mathbb P^1}(b)$ with $a\ge b$, compute rank, degree, slope, and reduced Hilbert polynomial. When is $E$ semistable?
:::

::: {.back card-id="application-slope-p1-splitting"}
The invariants are
$$\operatorname{rk}E=2,\qquad\det E=\mathcal O(a+b),\qquad\deg E=a+b,\qquad \mu(E)=\frac{a+b}{2},\qquad
P_E(m)=2m+a+b+2,\qquad p_E(m)=m+1+\frac{a+b}{2}.$$
The summand $\mathcal O(a)$ destabilizes when $a>b$. When $a=b$, every line subsheaf $L\subset E$ has $\deg L\le a$, so $E$ is semistable, but not stable because a summand has equal slope. Thus $E$ semistable $\iff a=b$.
:::

::: {.front card-id="application-projective-morphism-sections" tags="application" cite="[@The25, tag 01ND]"}
How do an invertible sheaf $L$ and sections $s_0,\ldots,s_n$ on a $k$-scheme $X$ define a morphism $f:X\to\mathbb P^n_k$? What condition must hold everywhere, and how do you recover $L$ from $f$?
:::

::: {.back card-id="application-projective-morphism-sections"}
The sections must generate $L$ at every point, giving a surjection $\mathcal O_X^{n+1}\to L$. Locally trivialize $L$ and send $x$ to $[s_0(x):\cdots:s_n(x)]$; changes of trivialization multiply all coordinates by the same unit, so these maps glue. Then $L\cong f^*\mathcal O(1)$ and $s_i=f^*x_i$ under that isomorphism. Isomorphic line bundles with the corresponding ordered sections give the same morphism.

Generation gives a morphism; a closed immersion requires the chosen linear system to be very ample. For homogeneous forms of the same degree on projective space, the generation condition is that they have no common geometric zero.
:::

::: {.front card-id="application-projective-plane-pencil-basepoint" tags="application"}
Why does $[x:y:z]\mapsto[x:y]$ fail to define a morphism $\mathbb P^2_{\mathbb C}\to\mathbb P^1_{\mathbb C}$? Can a different choice of forms give a nonconstant morphism between these spaces?
:::

::: {.back card-id="application-projective-plane-pencil-basepoint"}
Both coordinates vanish at $[0:0:1]$. More generally, a morphism would give $L=f^*\mathcal O_{\mathbb P^1}(1)=\mathcal O_{\mathbb P^2}(d)$ generated by two sections. A nonconstant map requires $d>0$, but two positive-degree plane forms have a common zero: with no common component, Bézout gives intersection number $d^2>0$; with a common component, they vanish along it. Thus every morphism $\mathbb P^2\to\mathbb P^1$ is constant.
:::

::: {.front card-id="application-projective-endomorphism-degree" tags="application"}
Let $n\ge1$ and let $F_0,\ldots,F_n$ be degree-$d$ forms over $\mathbb C$, with $d\ge1$ and no common projective zero. For the resulting $f:\mathbb P^n\to\mathbb P^n$, compute $f^*H$ and $\deg f$. When is $f$ an automorphism?
:::

::: {.back card-id="application-projective-endomorphism-degree"}
The forms give $f^*\mathcal O(1)=\mathcal O(d)$, so $f^*H=dH$. A positive-dimensional projective fiber would contain a curve on which this ample line bundle has degree zero, which is impossible. Hence $f$ is finite and surjective, and the projection formula gives
$$\deg f=(f^*H)^n=d^n.$$
It is an automorphism exactly when $d=1$, when the forms give an invertible linear map modulo scalar. Every automorphism arises this way, so $\operatorname{Aut}(\mathbb P^n)=\operatorname{PGL}_{n+1}(\mathbb C)$.
:::

::: {.front card-id="application-euler-twisted-differentials" tags="application"}
Compute $H^q(\mathbb P^3_{\mathbb C},\Omega^1(1))$ for all $q$, and compute $h^0(\mathbb P^3,\Omega^1(2))$. Identify the map on sections that makes the Euler sequence useful.
:::

::: {.back card-id="application-euler-twisted-differentials"}
Twisting Euler gives
$$0\longrightarrow\Omega^1(k)\longrightarrow\mathcal O(k-1)^{\oplus4}\xrightarrow{(s_i)\mapsto\sum x_is_i}\mathcal O(k)\longrightarrow0.$$
For $k=1$, the map on sections identifies $\mathbb C^4$ with the linear forms, so all cohomology of $\Omega^1(1)$ vanishes. For $k=2$, multiplication surjects from a space of dimension $16$ onto the quadratic forms of dimension $10$, giving $h^0(\Omega^1(2))=6$. Its sections are the linear syzygies among the coordinates.
:::

::: {.front card-id="application-projective-tangent-rigidity" tags="application"}
For $n\ge1$, compute $h^0(\mathbb P^n_{\mathbb C},T_{\mathbb P^n})$ and $H^1(\mathbb P^n,T_{\mathbb P^n})$. What do these say about infinitesimal automorphisms and deformations?
:::

::: {.back card-id="application-projective-tangent-rigidity"}
The tangent Euler sequence gives
$$H^0(T_{\mathbb P^n})\cong\operatorname{End}(\mathbb C^{n+1})/\mathbb C\,\mathrm{id},\qquad h^0(T_{\mathbb P^n})=(n+1)^2-1.$$
Line-bundle cohomology also gives $H^1(T_{\mathbb P^n})=0$. Thus the infinitesimal automorphisms form the Lie algebra of $\operatorname{PGL}_{n+1}$, and $\mathbb P^n$ has no nontrivial first-order deformations.
:::

::: {.front card-id="application-projective-line-normal-bundle" tags="application"}
Let $\ell\cong\mathbb P^1$ be a line in $\mathbb P^n_{\mathbb C}$, with $n\ge2$. Compute $N_{\ell/\mathbb P^n}$, $T_{\mathbb P^n}|_\ell$, and the tangent and obstruction spaces for embedded deformations of $\ell$.
:::

::: {.back card-id="application-projective-line-normal-bundle"}
The ideal of $\ell$ is generated by $n-1$ independent linear equations, so
$$N_{\ell/\mathbb P^n}\cong\mathcal O_{\mathbb P^1}(1)^{\oplus(n-1)}.$$
The tangent-normal sequence splits because $\operatorname{Ext}^1(\mathcal O(1),\mathcal O(2))=H^1(\mathcal O(1))=0$. Hence
$$T_{\mathbb P^n}|_\ell\cong\mathcal O(2)\oplus\mathcal O(1)^{\oplus(n-1)}.$$
The embedded deformation tangent space is $H^0(N)$ of dimension $2n-2$, and $H^1(N)=0$. This agrees with the dimension of the Grassmannian of lines.
:::

::: {.front card-id="application-adjunction-ci-normal-deformations" tags="application"}
Let $C\subset\mathbb P^3_{\mathbb C}$ be a smooth $(2,3)$ complete-intersection curve. Compute its normal bundle, canonical bundle, and embedded deformation tangent-space dimension. Is the standard obstruction group zero?
:::

::: {.back card-id="application-adjunction-ci-normal-deformations"}
The regular sequence of defining equations gives
$$N_{C/\mathbb P^3}\cong\mathcal O_C(2)\oplus\mathcal O_C(3).$$
Adjunction yields $\omega_C=\mathcal O_C(-4+2+3)=\mathcal O_C(1)$. Since $\deg C=6$, one has $g(C)=4$. Riemann–Roch and Serre duality give $h^0(\mathcal O_C(2))=9$, $h^0(\mathcal O_C(3))=15$, and vanishing $H^1$ for both. Thus $h^0(N)=24$ and $H^1(N)=0$, so embedded deformations are unobstructed.
:::

::: {.front card-id="card-c30e1b1de3ce90bd" tags="definition"}
What is a **derivation**?
:::

::: {.back card-id="card-c30e1b1de3ce90bd"}
$d\in \mathop{\mathrm{Der}}_A(B, M) \iff d$ is additive and $d(b_1b_2) = d(b_1)b_2 + b_1d(b_2)$ where $d(a) = 0$ for all $a\in A$.
:::

::: {.front card-id="card-9fcd3600930c58fb"}
What is the **sheaf of differentials** or **relative differential forms**?
:::

::: {.back card-id="card-9fcd3600930c58fb"}
For $f:X\to Y$, embed $X$ as a locally closed subscheme $X\hookrightarrow W \coloneqq\Delta_{X/Y}$ with sheaf of ideals $\mci$ and define $\Omega_{X/Y} \coloneqq\Delta^*(\mci/\mci^2) \in \QCoh(X)$. The local derivations glue to $d:{\mathcal{O}}_X\to \Omega_{X/Y}$.
:::

::: {.front card-id="card-8c48673ca22f6b18"}
What are the two exact sequences for sheaves (modules) of differentials?
:::

::: {.back card-id="card-8c48673ca22f6b18"}
The composition exact sequence: for $X \xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \rightarrow \Omega_{X / Y} \rightarrow 0.$$
For modules: for $A\to B\to C$,
$$\Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow \Omega_{C / B} \rightarrow 0 \in   {}_{C}\Mod$$
The "conormal" exact sequence: for $X\to Y$ and $Z\leq X$ a closed subscheme with ideal sheaf $\mci$,
$$\mathscr{I} / \mathscr{I}^2 \stackrel{\delta}{\rightarrow} \Omega_{X / Y} \otimes \mathcal{O}_Z \rightarrow \Omega_{Z / Y} \rightarrow 0.$$
For modules: for $B\in  \mathsf{Alg}_{A}, I\normal B, C\coloneqq B/I$,
$$I / I^2 \stackrel{\delta}{\rightarrow} \Omega_{B / A} \otimes_B C \rightarrow \Omega_{C / A} \rightarrow 0\in   {}_{C}\Mod$$
:::

::: {.front card-id="card-1f21f65d8810cd17"}
What is the **conormal exact sequence**, e.g. for an immersion $C\hookrightarrow S$?
:::

::: {.back card-id="card-1f21f65d8810cd17"}
How to derive: for a closed immersion $j: X\hookrightarrow Y$ of smooth varieties,
$${\mathbf{T}}_X \hookrightarrow j^*{\mathbf{T}}_Y \twoheadrightarrow N_{X/Y} \quad\underset{\text{dualize}}{\leadsto}\quad N_{X/Y} {}^{ \vee }\to j^*\Omega_{Y/Z} \twoheadrightarrow\Omega_{X/Z}\to 0.$$
At the level of sheaves on $C$, for $\iota: C\hookrightarrow S$,
$$N_{C/S} {}^{ \vee }\to \iota^*\Omega_{S/k} \twoheadrightarrow\Omega_{C/k}\to 0 \qquad \in \Sh(C)$$
where $N_{C/S} {}^{ \vee }\coloneqq I_C/I_C^2$ (the first map is injective when $C$ and $S$ are smooth). This is a sheaf version of: if $B\in  \mathsf{Alg}_{R}$ and $I \normal B$,
$$I/I^2 \to \Omega_{B/R}\otimes_B B/I \twoheadrightarrow\Omega_{(B/I)/R}\to 0 \qquad\in  {}_{B/I}\Mod$$
For $C \subseteq S$ a closed subscheme and $f:S\to T$, can rewrite this as
$$ \mci_C / \mci_C^2 \to \Omega_{S/T} \otimes{\mathcal{O}}_C \twoheadrightarrow\Omega_{C/T}\to 0 \qquad \in \Sh_C$$
:::

::: {.front card-id="card-25c14144c18e5ef3"}
What is the **Euler exact sequence**?
:::

::: {.back card-id="card-25c14144c18e5ef3"}
For $X=\mathbb P^n_A$, dualize the tangent Euler sequence
$$0\longrightarrow\mathcal O_X\xrightarrow{(x_0,\ldots,x_n)}\mathcal O_X(1)^{\oplus(n+1)}\longrightarrow T_{X/A}\longrightarrow0$$
to get the cotangent sequence
$$0\longrightarrow\Omega^1_{X/A}\longrightarrow\mathcal O_X(-1)^{\oplus(n+1)}\xrightarrow{(x_0,\ldots,x_n)}\mathcal O_X\longrightarrow0.$$
The terms are locally free, so dualizing preserves exactness: $T_{X/A}^{\vee}=\Omega^1_{X/A}$ and $\mathcal O_X(1)^{\vee}=\mathcal O_X(-1)$.
:::

::: {.front card-id="card-884b60a5d4ee268a"}
What is the composition exact sequence for $X\to Y\to Z$?
:::

::: {.back card-id="card-884b60a5d4ee268a"}
At the level of sheaves,
$$f^* \Omega_{Y/Z} \to \Omega_{X/Z} \to \Omega_{X/Y} \to 0 \qquad \in \Sh_X$$
How to remember:
:::

::: {.front card-id="card-a85d85454b4f4984"}
Discuss relative differentials?
:::

::: {.back card-id="card-a85d85454b4f4984"}
For $f: M\to S$, $\Omega^*_M / \left\langle{f^* \Omega^1_S}\right\rangle$, a quotient of a sheaf of dg ${\mathcal{O}}_M\dash$algebras.

Fiber over $s\in S$ is the de Rham sheaf complex of the fiber $M_s$.

Resolves $f^{-1}{\mathcal{O}}_S$ by coherent ${\mathcal{O}}_M$ modules
:::

::: {.front card-id="card-8df45a95ad038e48" tags="definition"}
What is an ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-8df45a95ad038e48"}
A sheaf $\mcf$ of abelian groups on $X$ where each $\mcf(U)\in   {}_{{\mathcal{O}}_X(U)}\Mod$ and the restriction maps respect scalar multiplication: $(rm)\mathrel{\Big|}_V = { \left.{{r}} \right|_{{V}} } { \left.{{m}} \right|_{{V}} }$.
:::

::: {.front card-id="card-ba56128ca287831c"}
What is the **tensor product** of two ${\mathcal{O}}_X\dash$modules?
:::

::: {.back card-id="card-ba56128ca287831c"}
Sheafify $U\mapsto \mcf(U) \otimes_{{\mathcal{O}}_X(U)} \mcg(U)$.
:::

::: {.front card-id="card-7e9dc536db4d8267"}
What is a **free** ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-7e9dc536db4d8267"}
Isomorphic to a direct sum $\bigoplus_{i\in I}{\mathcal{O}}_X$ of copies of ${\mathcal{O}}_X$; it has rank $n$ if ${\sharp}I = n < \infty$, i.e. $\mcf\cong{\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{n} }  }$.
:::

::: {.front card-id="card-f5daaf777e5093e5"}
What is a **locally free** ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-f5daaf777e5093e5"}
Admits an open cover $\left\{{U_i}\right\}$ of $X$ where each ${ \left.{{\mcf}} \right|_{{U_i}} }$ is a free ${\mathcal{O}}_{U_i}\dash$module. It is locally free of rank $n$ if there are ${\mathcal{O}}_{U_i}$-module isomorphisms $\rho_i: { \left.{{\mcf}} \right|_{{U_i}} } \cong {\mathcal{O}}_{U_i}{ {}^{ \scriptscriptstyle\oplus^{n} }  }$.

Then each stalk $\mcf_x$ is a free ${\mathcal{O}}_{X, x}\dash$module. The converse holds for $\mcf$ of finite presentation (e.g. coherent on a locally Noetherian scheme), but not in general.
:::

::: {.front card-id="card-7ea20bc415140836"}
What is the **rank** of an ${\mathcal{O}}_X\dash$module?
:::

::: {.back card-id="card-7ea20bc415140836"}
If locally free, on an open set $U$ the rank is the integer $r$ in $\mathcal F|_U\cong\mathcal O_U^{\oplus r}$; it is locally constant.

More generally, on an integral scheme with generic point $\eta$, a coherent sheaf has generic rank
$$\operatorname{rk}\mathcal F=\dim_{K(X)}\mathcal F_\eta.$$
A torsion sheaf has rank zero. On a reducible scheme, record the ranks at the generic points of its components. Fiber dimension $\dim_{\kappa(x)}(\mathcal F\otimes\kappa(x))$ can jump where $\mathcal F$ is not locally free.
:::

::: {.front card-id="card-041465065808b2ca"}
What is an **ideal sheaf** (sheaf of ideals) on $X$?
:::

::: {.back card-id="card-041465065808b2ca"}
An ${\mathcal{O}}_X\dash$submodule $\mci\leq {\mathcal{O}}_X$, so each $\mci(U) \normal{\mathcal{O}}_X(U)$.

For $\iota: Y\hookrightarrow X$ the inclusion of a closed subscheme, its ideal sheaf is $\mci_Y \coloneqq\ker\qty{{\mathcal{O}}_X \xrightarrow{\iota^\sharp}\iota_* {\mathcal{O}}_Y}$. It is always a quasi-coherent sheaf of ideals on $X$, and every quasi-coherent sheaf of ideals is $\mci_Y$ for a unique closed subscheme $Y$.
:::

::: {.front card-id="card-a0b5fb9f7c4c63c9" tags="definition"}
What is the **sheaf hom**?
:::

::: {.back card-id="card-a0b5fb9f7c4c63c9"}
For ${\mathcal{O}}_X\dash$modules $\mcf, \mcg$, the sheaf $\mathop{\mathcal{H}\! \mathit{om}}_{{\mathcal{O}}_X}(\mcf, \mcg)$ given by $U\mapsto \mathop{\mathrm{Hom}}_{{ \left.{{{\mathcal{O}}_X}} \right|_{{U}} }}({ \left.{{\mcf}} \right|_{{U}} }, { \left.{{\mcg}} \right|_{{U}} })$ (no need to sheafify). It is again an ${\mathcal{O}}_X\dash$module.
:::

::: {.front card-id="card-1c0674319a19d9fa"}
What is the **direct image** in ${}_{{\mathcal{O}}_X}\Mod$?
:::

::: {.back card-id="card-1c0674319a19d9fa"}
For $f: X\to Y$ in ringed spaces and $\mcf\in   {}_{{\mathcal{O}}_X}\Mod$, take $f_* \mcf\in   {}_{{\mathcal{O}}_Y}\Mod$
:::

::: {.front card-id="card-26737bcb87ae4726"}
What is the **inverse image** in ${}_{{\mathcal{O}}_X}\Mod$?
:::

::: {.back card-id="card-26737bcb87ae4726"}
For $f:X\to Y$ and $\mcg\in   {}_{{\mathcal{O}}_Y}\Mod$, $f^* \mcg\coloneqq f^{-1}\mcg\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X$. I.e. base change $f^{-1}G$ from $f^{-1}{\mathcal{O}}_Y$ to ${\mathcal{O}}_X$.
:::

::: {.front card-id="card-2f0923dae6d93520"}
What is the ${\mathcal{O}}_X\dash$module associated to $M\in {}_{A}\Mod$?
:::

::: {.back card-id="card-2f0923dae6d93520"}
$\tilde M \in \Sh(\operatorname{Spec}A)$ where $\tilde M(U)$ is the set of functions $s: U\to \amalg_{p\in U} M_p$ such that $s(p)\in M_p$ and $s$ is locally a fraction $m/f$ with $m\in M, f\in A$. The stalks are the localizations, $\tilde M_p = M_p$, and the global sections are $M$.

More precisely: for each $p\in U$ there exists $p\in V \subset U$ and $m\in M, f\in A$ such that for each $q\in V$, $f\not \in q$ and $s(q) = m/f$ in $M_q$.
:::

::: {.front card-id="card-70da298d7eaf3e5c"}
What is a **quasicoherent sheaf**/${\mathcal{O}}_X\dash$module? :
:::

::: {.back card-id="card-70da298d7eaf3e5c"}
An ${\mathcal{O}}_X\dash$module which is locally of the form $\tilde M$, where $\tilde M$ is the sheaf associated to $M$.

Admits an affine open cover $\operatorname{Spec}A_i\rightrightarrows X$ where $\exists M_i\in  {}_{A_i}\Mod$ with ${ \left.{{\mcf}} \right|_{{\tilde M_i}} }$.

Equivalently, by a theorem of Serre, **locally** $\exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow\mcf$.
:::

::: {.front card-id="card-d64ff182851952ed"}
What is a **coherent sheaf**/ ${\mathcal{O}}_X\dash$module? :
:::

::: {.back card-id="card-d64ff182851952ed"}
Quasicoherent where $\operatorname{Spec}A_i\rightrightarrows X$ and each $M_i \in   {}_{A_i}\Mod^\fg$.

Equivalently, by a theorem of Serre, $\exists {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{J} }  } \to {\mathcal{O}}_X{ {}^{ \scriptscriptstyle\oplus^{I} }  }\twoheadrightarrow\mcf$ with ${\sharp}I, {\sharp}J < \infty$.
:::

::: {.front card-id="card-01c0cd5b5e6565ed"}
Give an example of a sheaf that is not quasicoherent.
:::

::: {.back card-id="card-01c0cd5b5e6565ed"}
For $Y\leq X$ a closed subscheme, ${ \left.{{{\mathcal{O}}_X}} \right|_{{Y}} }$.
:::

::: {.front card-id="card-7b0a991f2503ff89"}
Give an example of a sheaf that is not coherent.
:::

::: {.back card-id="card-7b0a991f2503ff89"}
Take $f:{\mathbf{A}}^1_{/ {k}}\to \operatorname{Spec}k$ and $f_* {\mathcal{O}}_{{\mathbf{A}}^1_{/ {k}}}$ has global sections $k[t]\not\in   {}_{k}\Mod^\fg$.
:::

::: {.front card-id="card-d1af342442df2ccd"}
Give an example of a quasicoherent but not coherent ${\mathcal{O}}_X\dash$module.
:::

::: {.back card-id="card-d1af342442df2ccd"}
The constant sheaf $\underline{\mck}$ where $U\mapsto K(X)$, the rational function field of $X$.
:::

::: {.front card-id="card-c07a818203520df1"}
What is a consequence of an ${\mathcal{O}}_X\dash$module being quasicoherent?
:::

::: {.back card-id="card-c07a818203520df1"}
For $X$ affine, global sections is exact on sequences $\mcf\hookrightarrow\bullet\twoheadrightarrow\bullet$ when $\mcf\in \QCoh(X)$.

Kernels, cokernels, images, extensions, pullbacks, and pushforwards along qcs are again quasicoherent.
:::

::: {.front card-id="card-dab506d58c11eaf9"}
What is ${\mathcal{O}}_X(n)$?
:::

::: {.back card-id="card-dab506d58c11eaf9"}
For $S$ a graded ring and $X \coloneqq\mathop{\mathrm{Proj}}S$, ${\mathcal{O}}_X(n)\coloneqq S(n)\tilde{}$ (the sheaf associated to a module), where $S(n)$ (also written $S[n]$) is the shifted graded module with $S(n)_d = S_{n+d}$.

${\mathcal{O}}_X(1)$ is Serre's twisting sheaf, and if $\mcf\in   {}_{{\mathcal{O}}_X}\Mod$ then $\mcf(n) \coloneqq\mcf\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n)$.
:::

::: {.front card-id="card-c5f79fa6fffa2efc"}
For $S$ a graded ring, $X = \mathop{\mathrm{Proj}}S$, and $\mcf\in {}_{{\mathcal{O}}_X}\Mod$, what is the graded $S\dash$module associated to $\mcf$?
:::

::: {.back card-id="card-c5f79fa6fffa2efc"}
${{\Gamma}\qty{X; \mcf} } \coloneqq\bigoplus_{n\in \ZZ} {{\Gamma}\qty{X; \mcf(n)} }$.
:::

::: {.front card-id="card-0993d61182a2d5f4"}
What is the **twisting sheaf** ${\mathcal{O}}(1)$ on ${\mathbf{P}}^n_{/ {Y}}$?
:::

::: {.back card-id="card-0993d61182a2d5f4"}
${\mathcal{O}}_{{\mathbf{P}}^n_{/ {Y}}}(1) \coloneqq g^* {\mathcal{O}}_{{\mathbf{P}}^n_{/ {\ZZ}}}(1)$ where $g:{\mathbf{P}}^n_{/ {Y}} \to {\mathbf{P}}^n_{/ {\ZZ}}$ is the projection.
:::

::: {.front card-id="card-996db5f3b6601367"}
What is a **very ample** invertible sheaf?
:::

::: {.back card-id="card-996db5f3b6601367"}
For $X$ over $Y$, $\mcl\in \operatorname{Pic}(X)$ is very ample relative to $Y$ iff there is an immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ over $Y$ for some $n$ such that $\iota^* {\mathcal{O}}(1) \cong \mcl$. For $Y = \operatorname{Spec}A$, this is equivalent to the existence of sections $\left\{{s_0,\cdots, s_n}\right\}\subseteq H^0(X; \mcl)$ generating $\mcl$ such that $x\mapsto {\left[ {s_0(x): \cdots : s_n(x)} \right]}$ is an immersion.
:::

::: {.front card-id="card-6434f1ec713aa932" cite="[@Har77, Appendix B, Example 3.4.1]"}
Why is a scheme $X$ over a Noetherian scheme $Y$ projective iff it is proper and admits a very ample invertible sheaf relative to $Y$?
:::

::: {.back card-id="card-6434f1ec713aa932"}
Projective implies proper since ${\mathbf{P}}^n_{/ {Y}}\to Y$ is proper and closed immersions are proper; a closed immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ gives $\iota^* {\mathcal{O}}(1)\in \operatorname{Pic}(X)^\mathrm{va}$.

Conversely if proper, take $\mcl\in \operatorname{Pic}(X)^{\mathrm{va}}$ to get $\mcl\cong \iota^* {\mathcal{O}}(1)$ for some immersion $\iota: X\to {\mathbf{P}}^n_{/ {Y}}$ for some $n$ -- but $\iota(X)$ is closed, so $\iota$ is a *closed* immersion, making $X$ projective.

Proper alone does not imply projective: Hironaka constructed smooth proper threefolds over $\CC$ that are not projective.
:::

::: {.front card-id="card-5c26a4c9e18c5228"}
What does it mean for an ${\mathcal{O}}_X$ module to be **globally generated** (or **generated by global sections**)?
:::

::: {.back card-id="card-5c26a4c9e18c5228"}
There exists a family of sections $\left\{{s_i}\right\}_{i\in I} \subseteq {{\Gamma}\qty{X; \mcf} }$ where for each $x\in X$ the images of $s_i$ in $\mcf_x$ generate that stalk as an ${\mathcal{O}}_{X, x}\dash$module.

Equivalently, $\mcf$ is the quotient of a free sheaf: $\exists \bigoplus_{i\in I}{\mathcal{O}}_X\twoheadrightarrow\mcf$.

For $\mcl\in \operatorname{Pic}(X)$: for every $x\in X$ there is a section $s\in H^0(X; \mcl)$ not vanishing at $x$, i.e. $\mcl$ is base-point free.
:::

::: {.front card-id="card-6078c0a2248b7c1b"}
Give examples of globally generated sheaves.
:::

::: {.back card-id="card-6078c0a2248b7c1b"}
Example: any $\mcf\in \QCoh(\operatorname{Spec}A)$ -- write $\mcf\cong M\tilde{}$ and take any set of generators for $M\in  {}_{A}\Mod$.
:::

::: {.front card-id="card-36e874ed79b4bec1"}
What is a major result regarding global generation?
:::

::: {.back card-id="card-36e874ed79b4bec1"}
For $X$ projective over a Noetherian scheme $A$, ${\mathcal{O}}(1)$ a very ample invertible sheaf on $X$, $\mcf\in \Coh(X)$, there exists some $N_0$ such that $\mcf(n)$ is globally generated by a finite number of sections for all $n\geq N_0$.
:::

::: {.front card-id="card-a335a1700d07eb09"}
What is the **Euler characteristic** of an ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-a335a1700d07eb09"}
For a coherent sheaf $\mathcal F$ on a proper scheme $X$ over a field $k$,
$$\chi(X,\mathcal F)=\sum_i(-1)^i\dim_k H^i(X,\mathcal F).$$
Properness and coherence ensure finite-dimensional cohomology, with only finitely many nonzero terms. This is a coherent Euler characteristic; for $\mathcal F=\mathcal O_X$ it need not equal the topological Euler characteristic of $X(\mathbb C)$.
:::

::: {.front card-id="card-c1ffa65f50144241"}
What is the **Hilbert polynomial** of an ${\mathcal{O}}_X$ module?
:::

::: {.back card-id="card-c1ffa65f50144241"}
Fix an ample line bundle $H$ on a projective scheme $X$ and a coherent sheaf $\mathcal F$. Using that
$$P_{\mathcal F,H}(m)=\chi(X,\mathcal F\otimes H^{\otimes m})$$
is a polynomial in $m$, take this to be the Hilbert polynomial. For $m\gg0$, higher cohomology vanishes, so it equals $h^0(X,\mathcal F\otimes H^{\otimes m})$. Its degree is $\dim\operatorname{Supp}\mathcal F$ when $\mathcal F\ne0$. It depends on the polarization; replacing $H$ by $H^{\otimes a}$ replaces $P(m)$ by $P(am)$.
:::

::: {.front card-id="card-37be5dabde736ed0" tags="definition"}
What is: Quasi-coherent and coherent sheaves,
:::

::: {.back card-id="card-37be5dabde736ed0"}
An $\mathcal O_X$-module $F$ is quasi-coherent if every point has an affine neighborhood $U=\operatorname{Spec}A$ with $F|_U\cong\widetilde M$ for an $A$-module $M$. On a locally Noetherian scheme, $F$ is coherent if locally $M$ is a finite $A$-module.
:::

::: {.front card-id="card-eeb89ede8813d491" tags="definition"}
What is: Construction of $\mathcal{O}_X$-modules,
:::

::: {.back card-id="card-eeb89ede8813d491"}
For an $A$-module $M$ on $U=\operatorname{Spec}A$, the associated sheaf $\widetilde M$ is determined by $\widetilde M(D(f))=M_f$. More general $\mathcal O_X$-modules are obtained by gluing modules on open subsets with compatible isomorphisms on overlaps.
:::

::: {.front card-id="card-4cd160edee37a085" tags="definition"}
What is: Invertible sheaves and vector bundles
:::

::: {.back card-id="card-4cd160edee37a085"}
An invertible sheaf is an $\mathcal O_X$-module locally isomorphic to $\mathcal O_X$; it is a locally free sheaf of rank one. A vector bundle of rank $r$ is a scheme over $X$ locally isomorphic to $\mathbb A_X^r$ with linear transition maps; it corresponds to a locally free sheaf of rank $r$.
:::

::: {.front card-id="card-cbfb24232131f375" tags="definition"}
What is: module of relative differential forms
:::

::: {.back card-id="card-cbfb24232131f375"}
The module of Kähler differentials $\Omega_{A/R}$ is generated by symbols $da$ subject to additivity, $d(ab)=a\,db+b\,da$, and $dr=0$ for $r\in R$. Its universal property is $\operatorname{Hom}_A(\Omega_{A/R},M)\cong\operatorname{Der}_R(A,M)$.
:::

::: {.front card-id="card-28213da6a96eb9ed" tags="definition"}
What is: Tangent sheaf
:::

::: {.back card-id="card-28213da6a96eb9ed"}
For $f:X\to S$, the relative tangent sheaf is $\mathcal T_{X/S}=\mathcal Hom_{\mathcal O_X}(\Omega^1_{X/S},\mathcal O_X)$. Its local sections are $\mathcal O_S$-linear derivations of $\mathcal O_X$.

For a smooth $n$-dimensional variety over a field, the tangent sheaf is locally free of rank $n$.
:::

::: {.front card-id="card-1af69ef40541b9cb" tags="definition"}
What is: Algebraic differential forms;
:::

::: {.back card-id="card-1af69ef40541b9cb"}
Algebraic differential $p$-forms are sections of $\Omega^p_{X/S}=\bigwedge^p\Omega^1_{X/S}$. The exterior derivative $d:\Omega^p_{X/S}\to\Omega^{p+1}_{X/S}$ satisfies $d^2=0$ and the graded Leibniz rule.
:::

::: {.front card-id="card-136accbe28d1a749" tags="definition"}
What is: The (co)normal sheaf,
:::

::: {.back card-id="card-136accbe28d1a749"}
For a closed immersion $i:Z\hookrightarrow X$ with ideal sheaf $I$, the conormal sheaf is $I/I^2$. Its dual $\mathcal Hom_{\mathcal O_Z}(I/I^2,\mathcal O_Z)$ is the normal sheaf. For smooth $Z$ and $X$, the conormal sequence is $I/I^2\to i^*\Omega_X^1\to\Omega_Z^1\to0$.

For a closed immersion of smooth varieties, the normal and conormal sheaves are locally free of rank equal to the codimension.
:::

::: {.front card-id="card-c5cef00e4330d7da"}
What is a geometric vector bundle over a scheme?
:::

::: {.back card-id="card-c5cef00e4330d7da"}
A geometric vector bundle of rank $n$ over $X$ is a scheme $f: Z \rightarrow X$ together with an open cover $\left\{U_i\right\}$ of $X$ and isomorphisms $\psi_i: f^{-1}\left(U_i\right) \rightarrow \mathbf{A}_{U_i}^n \coloneqq U_i\times_\ZZ {\mathbf{A}}^n_\ZZ$ over $U_i$ such that, for any $i, j$ and any open affine $V=\operatorname{Spec}(R) \subseteq U_i \cap U_j$, the automorphism $\psi=\psi_j \circ \psi_i^{-1}$ of $\mathbf{A}_V^n = \operatorname{Spec}R[x_1,\cdots,x_n]$ is linear: it is given by an $R$-algebra automorphism $\theta$ with $\theta(x_i) = \sum_j a_{ij} x_j$ and $(a_{ij})\in\operatorname{GL}_n(R)$.

For $\mce$ a locally free sheaf of rank $n$ on $X$, $\mathbf{V}(\mce)\coloneqq\operatorname{Spec}\operatorname{Sym}(\mce)$ is a geometric vector bundle of rank $n$ whose sheaf of sections is $\mce^{\vee}$.
:::

::: {.front card-id="card-013129f0821e1e9e"}
What is the geometric vector bundle associated to a locally free sheaf?
:::

::: {.back card-id="card-013129f0821e1e9e"}
$V(\mce) \coloneqq\operatorname{Spec}\operatorname{Sym}\mce$, where $\operatorname{Sym}\mce$ is the sheafy symmetric algebra so ${ \left.{{\qty{\operatorname{Sym}\mce}}} \right|_{{U_i}} } \cong \operatorname{Sym}\qty{{ \left.{{\mce}} \right|_{{U_i}} }}$ over ${\mathcal{O}}_{U_i}$, and where one takes the sheaf-theoretic spectrum.
:::

::: {.front card-id="card-de688f4ab8bf69dd"}
What are the exact sequences associated with relative differentials?
:::

::: {.back card-id="card-de688f4ab8bf69dd"}
For $f:X\to Y$ and $Z \leq X$ closed with ideal sheaf $\mci_Z$, the sequence
$$\mci_Z/\mci_Z^2\to \Omega_{X/Y}\otimes{\mathcal{O}}_Z \twoheadrightarrow\Omega_{Z/Y}$$
This is right exact for every closed immersion. If $Z\to Y$ is smooth, the left map is injective and the sequence is locally split. Exactness alone does not characterize smoothness: the identity immersion of a singular $k$-scheme has conormal sequence $0\to\Omega_{Z/k}\xrightarrow{1}\Omega_{Z/k}\to0$.

For $X\xrightarrow{f} Y \xrightarrow{g} Z$,
$$f^* \Omega_{Y / Z} \rightarrow \Omega_{X / Z} \twoheadrightarrow\Omega_{X / Y}$$
This is right exact; if $f$ is smooth, it is short exact and locally split.
:::

::: {.front card-id="card-14008e56d2fec738" tags="definition"}
What is a **presheaf**?
:::

::: {.back card-id="card-14008e56d2fec738"}
A functor $F: \Open(X)^{\operatorname{op}}\to \mathsf{CRing}$ (say; or sets, abelian groups, ...) preserving terminal objects, i.e. for each open $U \subseteq X$ a ring $F(U)$ where $F(\emptyset) = 0$, for every $U\hookrightarrow V$ a restriction $\mathop{\mathrm{Res}}_{V< U}: F(V)\to F(U)$, where $\mathop{\mathrm{Res}}_{U, U} = \operatorname{id}_{F(U)}$ and $U\hookrightarrow V\hookrightarrow W \leadsto \mathop{\mathrm{Res}}_{VU} \circ \mathop{\mathrm{Res}}_{WV} = \mathop{\mathrm{Res}}_{WU}$.

A sheaf also satisfies gluing and uniqueness for compatible local sections.
:::

::: {.front card-id="card-c59fe5bb7a144af8"}
What is a **sheaf**?
:::

::: {.back card-id="card-c59fe5bb7a144af8"}
A presheaf satisfying unique gluing: given $\left\{{\phi_i \in F(U_i)}\right\}$ with ${ \left.{{\phi_i}} \right|_{{U_{ij}}} } = { \left.{{\phi_j}} \right|_{{U_{ij}}} }$ there exists a unique $\Phi\in F(\bigcup_i U_i)$ such that ${ \left.{{\Phi}} \right|_{{U_i}} } = \phi_i$ for all $i$.
:::

::: {.front card-id="card-d11a1c7edb702d31"}
Give an example of a presheaf that is not a sheaf.
:::

::: {.back card-id="card-d11a1c7edb702d31"}
Any presheaf of constant functions, since functions can be constant on disjoint open sets (thus agreeing on overlaps trivially) without being globally constant (jump discontinuities)
:::

::: {.front card-id="card-7a8067f2aeb0cca8"}
What is the **equalizer characterization** of a sheaf?
:::

::: {.back card-id="card-7a8067f2aeb0cca8"}
$$F(U) \rightarrow \prod_{i} F(U_i) {{{} \atop \longrightarrow}\atop{\longrightarrow \atop {}}} \prod_{i, j} F(U_i \cap U_j)$$
where the maps are the restrictions $U_i \to U_{ij}$ and $U_j\to U_{ij}$.
:::

::: {.front card-id="card-82b98ea9b3cb0231" tags="definition"}
What is the **sheafification** of a presheaf?
:::

::: {.back card-id="card-82b98ea9b3cb0231"}
For $\mcf$ a presheaf, define $\mcf^+(U)$ as the functions $s: U\to \amalg_{x\in U} \mcf_x$ where $s(p) \in \mcf_p$ and for each $p\in U$ there is a neighborhood $V\subseteq U$ of $p$ and $t\in \mcf(V)$ such that $\forall q\in V,\,\, t_q = s(q)$ (equivalently, continuous sections of the étalé space of $\mcf$).

There is a map $\mcf\to\mcf^+$ inducing isomorphisms on all stalks, and every map from $\mcf$ to a sheaf factors uniquely through $\mcf^+$.
:::

::: {.front card-id="card-ea14df10f5014961" tags="definition"}
What is a **morphism of presheaves**? Of sheaves?
:::

::: {.back card-id="card-ea14df10f5014961"}
A morphism $\phi: \mcf\to \mcg$ of presheaves is a collection $\phi_U: \mcf(U) \to \mcg(U)$ fitting into commuting squares with restrictions, i.e. commuting with every restriction map. A morphism of sheaves is a morphism of the underlying presheaves.
:::

::: {.front card-id="card-a8dbd6c1552876cc"}
What is a **germ**?
:::

::: {.back card-id="card-a8dbd6c1552876cc"}
Elements in the stalk $\mcf_p$ are germs of sections of $\mcf$ over $p$.
:::

::: {.front card-id="card-903e35430d43d1de"}
What is the **stalk** of a sheaf?
:::

::: {.back card-id="card-903e35430d43d1de"}
$\mcf_p \coloneqq\colim_{U\ni p} \mcf(U)$.
:::

::: {.front card-id="card-29db92d857211565"}
What is the **kernel sheaf**?
:::

::: {.back card-id="card-29db92d857211565"}
$U\mapsto \ker \phi(U)$, which is already a sheaf.
:::

::: {.front card-id="card-e37a62e39fa49064"}
What is the **image sheaf**?
:::

::: {.back card-id="card-e37a62e39fa49064"}
Sheafify $U\mapsto \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-eca54149334d9622"}
Give an example to show that the image presheaf is not necessarily a sheaf.
:::

::: {.back card-id="card-eca54149334d9622"}
Problem: may fail existence. Take $0\to \underline{\ZZ}\xrightarrow{2\pi i} {\mathcal{O}}_X \xrightarrow{\exp} {\mathcal{O}}_X^{\times}\to 0$; this is exact as a sequence of sheaves since it's exact on stalks, but not exact as a sequence of presheaves, showing that $\operatorname{im}_{{\mathsf{pre}}} \exp \neq (\operatorname{im}_{\mathsf{pre}}\exp)^+$ (where $\mcf= \mcf^+$ for any sheaf). Cover $\CC^{\times}$ by contractible $U_i$, then take sections $f_i \coloneqq\operatorname{id}_{U_i} \in {\mathcal{O}}_X^{\times}$; then $f_i\in (\operatorname{im}\exp)^-$ since $\log(z)$ exists on each $U_i$. The sectors glue to $\CC^{\times}$, but there is no global $\log(z)$. So $\operatorname{id}_{\CC^{\times}} \not\in (\operatorname{im}\exp)^-$, so it fails the gluing axiom.
:::

::: {.front card-id="card-199b042d968cba02"}
What is the **cokernel sheaf**?
:::

::: {.back card-id="card-199b042d968cba02"}
For $\phi: \mcf\to \mcg$, sheafify $U\mapsto \operatorname{coker}\phi(U) \coloneqq\mcg/ \operatorname{im}\phi(U)$.
:::

::: {.front card-id="card-b4ef69e82c4e525c"}
Give an example to show that the cokernel presheaf is not a sheaf.
:::

::: {.back card-id="card-b4ef69e82c4e525c"}
Problem: may fail uniqueness. Let $\mcg\leq \mathop{\mathrm{Hol}}(\CC, \CC)$ be the sheaf of nonvanishing holomorphic functions and take $\exp: \mathop{\mathrm{Hol}}(\CC, \CC)\to \mcg$ and $U = \CC\setminus\left\{{0}\right\}$. Set $f(z) = z$, then $f\in \mcg(U)$ since it's nonvanishing. Cover $U$ by sectors $U_i$, then $f\in \operatorname{im}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$ since $\log f$ exists and $\exp(\log f) = f$, so $f = 0$ in $\operatorname{coker}{ \left.{{\exp}} \right|_{{U_i}} }$ for all $i$. But $f\not\in \operatorname{im}\exp$ since there is no global logarithm, so $f\neq 0\in \operatorname{coker}\exp$ as a morphism of presheaves.
:::

::: {.front card-id="card-79c3642c37f8ed12" tags="definition"}
What is the **pullback/pushforward** (inverse/direct images) of a sheaf?
:::

::: {.back card-id="card-79c3642c37f8ed12"}
For $f:X\to Y$, $\mcf\in \Sh(X), \mcg\in \Sh(Y)$. Pushforward/direct image: already a sheaf
$$f_*\mcf(U) =\mcf(f^{-1}(U)),\qquad f_*\mcf\in \Sh(Y)$$
Pullback/inverse image: **sheafify**
$$f^{-1}\mcg(U) \coloneqq\colim_{V\supseteq f(U)} \mcg(V)$$
For $f: X\hookrightarrow Y$ the inclusion of an open subset, $f^{-1}\mcg(U) = \mcg(U)$, so denote $f^{-1}\mcg\coloneqq{ \left.{{\mcg}} \right|_{{X}} }$.

For modules on ringed spaces, $f^*\mcg\coloneqq f^{-1}\mcg\otimes_{f^{-1}{\mathcal{O}}_Y}{\mathcal{O}}_X$.
:::

::: {.front card-id="card-e8e12fcc8b9e24a2" tags="definition"}
What is a **constant sheaf**?
:::

::: {.back card-id="card-e8e12fcc8b9e24a2"}
For $A\in \Ab\Grp$, $\underline{A}$ is the sheafification of the constant presheaf $U\mapsto A$. Equivalently, $\underline{A} \coloneqq C^0({-}, A^{{\operatorname{disc}}})$, the sheaf of locally constant functions to $A$. On nonempty connected sets $U$, $\underline{A}(U) = A$; on locally connected $U$, sections are the functions constant on every connected component. Stalks are all $A$.
:::

::: {.front card-id="card-0ccf704bc953a261" tags="definition"}
What is the **skyscraper sheaf**? Its stalks? Its adjoint characterization?
:::

::: {.back card-id="card-0ccf704bc953a261"}
For a point $p\in X$, the inclusion $\iota_p: \left\{{p}\right\} \hookrightarrow X$, and an abelian group $A$ (the constant sheaf $\underline{A}$ on $\left\{{p}\right\}$), the skyscraper sheaf is the direct image $(\iota_p)_*\underline{A}$. It assigns $U\mapsto A$ if $p\in U$ and $U\mapsto 0$ otherwise, with restrictions the identity or zero maps. Stalks are $A$ at each point in $\cl_X(p)$ and 0 elsewhere. Adjoint to taking stalks: $\Ab(\mcf_p, A)  { \, \xrightarrow{\sim}\, }\Sh(X)(\mcf, (\iota_p)_* A)$.
:::

::: {.front card-id="card-0859e1c888527f03"}
What is the **canonical sheaf**?
:::

::: {.back card-id="card-0859e1c888527f03"}
For $X$ smooth over $S$ of relative dimension $n$, $\omega_{X/S} \coloneqq\operatorname{det}\Omega_{X/S} \coloneqq\bigwedge\nolimits^n \Omega_{X/S}$, a line bundle. Over a field $k$, $\omega_X \coloneqq\operatorname{det}\Omega_{X/k}$ with $n\coloneqq\dim X$.
:::

::: {.front card-id="card-9535c31c3ca2f51d"}
What is the **dualizing sheaf**?
:::

::: {.back card-id="card-9535c31c3ca2f51d"}
For $X$ proper over a field, $\omega_X^\circ\in \Coh(X)$ together with a trace $\operatorname{tr}: H^n(X; \omega_X^\circ)\to k$ such that $\forall \mcf\in \Coh(X)$, the composition
$$H^n(X; \mcf) \times \mathop{\mathrm{Hom}}(\mcf, \omega_X^\circ) \to H^n(X, \omega_X^\circ) \xrightarrow{{\mathrm{tr}}}k$$
yields an isomorphism $\mathop{\mathrm{Hom}}(\mcf, \omega_X^\circ)  { \, \xrightarrow{\sim}\, }H^n(X; \mcf) {}^{ \vee }$ and more generally $\operatorname{Ext}^i(\mcf, \omega_X^\circ) \cong H^{n-i}(X; \mcf) {}^{ \vee }$. Exists for any projective scheme, not always equal to $\operatorname{det}\Omega_{X/k}$.
:::

::: {.front card-id="card-0c6c3a54e08bf4fb"}
What is a **local system**?
:::

::: {.back card-id="card-0c6c3a54e08bf4fb"}
A locally constant sheaf, i.e. a sheaf such that every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{\mcf}} \right|_{{U}} }$ is a constant sheaf.
:::

::: {.front card-id="card-2a19d4bf210f5449"}
What is an **invertible sheaf**?
:::

::: {.back card-id="card-2a19d4bf210f5449"}
$\mcl\in \Sh(X)$ such that $\exists \mcl^{-1}\in \Sh(X)$ with $\mcl\otimes_{{\mathcal{O}}_X} \mcl^{-1}\cong {\mathcal{O}}_X$.

Equivalently, every $x\in X$ admits a neighborhood $U\ni x$ such that ${ \left.{{\mcf}} \right|_{{U}} } \cong {\mathcal{O}}_U$.

Equivalently, a locally free ${\mathcal{O}}_X\dash$module of rank 1.
:::

::: {.front card-id="card-09446192b8f9ece5"}
Discuss invertible sheaves on affine schemes.
:::

::: {.back card-id="card-09446192b8f9ece5"}
$\mcf\in \operatorname{Pic}(\operatorname{Spec}A)\implies \mcf$ corresponds to $M\in  {}_{A}\Mod$ which is finite projective locally free of rank 1 and thus flat and finitely presented. Every invertible sheaf on ${\mathbf{A}}^2_{/ {k}}$ is trivial.
:::

::: {.front card-id="card-e8e690603a360318"}
What is a **constructible sheaf**?
:::

::: {.back card-id="card-e8e690603a360318"}
$\mcf\in \Sh(X)$ is constructible iff $\exists \left\{{i_{Y_i}: Y_i\hookrightarrow X}\right\}_{i\leq N}$ with $X = \bigcup_{i\leq N}Y_i$, i.e. $Y$ is a finite union of locally closed subschemes, such that ${ \left.{{\mcf}} \right|_{{Y_i}} } \coloneqq\iota_{Y_i}^* \mcf$ is a finite locally constant sheaf.
:::

::: {.front card-id="card-45174c1167af9df9"}
What is the **sheaf of rational functions** on a scheme?
:::

::: {.back card-id="card-45174c1167af9df9"}
Define the function field of $X$ to be $K\coloneqq{\mathcal{O}}_{X, \eta_X}$, the stalk at the generic point, and define $\mck_X \coloneqq\underline{K}$, the constant sheaf associated to this field. Equivalently, sheafify $U\to \operatorname{ff}({\mathcal{O}}_X(U))$.
:::

::: {.front card-id="card-0b18a6dfa59ccde0"}
What is the fundamental exact sequence involving the tangent sheaf for ${\mathbf{P}}^n$?
:::

::: {.back card-id="card-0b18a6dfa59ccde0"}
For $X=\mathbb P^n_k$ over a field $k$,
$$0\longrightarrow\mathcal O_X\xrightarrow{(x_0,\ldots,x_n)}\mathcal O_X(1)^{\oplus(n+1)}\longrightarrow T_{X/k}\longrightarrow0.$$
:::

::: {.front card-id="card-aac019483de7ed9e"}
What does it mean to **twist a sheaf**?
:::

::: {.back card-id="card-aac019483de7ed9e"}
$\mcf(n) \coloneqq\mcf\otimes_{{\mathcal{O}}_X} {\mathcal{O}}_X(n)$.
:::

::: {.front card-id="card-4d2fa6a3304404c6"}
Characterize coherent sheaves over $\operatorname{Spec}A$ for $A$ Noetherian.
:::

::: {.back card-id="card-4d2fa6a3304404c6"}
$\mcf\in \Coh(\operatorname{Spec}A)\implies \exists \bigoplus_{i\in I} {\mathcal{O}}(n_i) \twoheadrightarrow\mcf$, i.e. always a quotient of a free sheaf. Easy proof: $\mcf(n)$ is globally generated for some $n$, so $\exists \bigoplus_{i\leq N} {\mathcal{O}}_X \twoheadrightarrow\mcf(n)$, now twist this exact sequence by $-n$.
:::

::: {.front card-id="card-c5e1189afc267094"}
What is the **six functor formalism**?
:::

::: {.back card-id="card-c5e1189afc267094"}
Direct image (pushforward) and inverse image (pullback), extension by zero (lower shriek) and exceptional image (upper shriek), internal tensor and internal hom.
:::

::: {.front card-id="card-5fb0674e6ef318ad"}
How is the **inverse image sheaf** defined? What are its stalks?
:::

::: {.back card-id="card-5fb0674e6ef318ad"}
For $f:X\to Y$, sheafify the presheaf $U\mapsto\operatorname*{colim}_{V\supseteq f(U)}\mathcal G(V)$, where $V$ runs through open subsets of $Y$. At $x\in X$,
$$(f^{-1}\mathcal G)_x\cong\mathcal G_{f(x)}.$$
:::

::: {.front card-id="card-7253757c78a0c001"}
What is the **extension by zero** sheaf? What are its stalks?
:::

::: {.back card-id="card-7253757c78a0c001"}
Sheafify $U\mapsto \chi_{V\subseteq U}\mcf(V)$ to get $\iota_! \mcf$ for $\iota: U \subseteq X$. Stalks are $\mcf_p \chi_{p\in U}$.

Alternatively take $\iota_* \mcf$.
:::

::: {.front card-id="card-c15fc4f7707b0b75"}
How is the pushforward sheaf defined? What are its stalks?
:::

::: {.back card-id="card-c15fc4f7707b0b75"}
$f_*\mcf(V) \coloneqq\mcf(f^{-1}(V))$. Can't say much in general about its stalks.
:::

::: {.front card-id="card-77682f622e066702"}
What is the restriction of a sheaf?
:::

::: {.back card-id="card-77682f622e066702"}
For an inclusion $\iota:X\hookrightarrow Y$, topological restriction is $\iota^{-1}\mathcal G$, with stalk $(\iota^{-1}\mathcal G)_x=\mathcal G_x$.

For an $\mathcal O_Y$-module and a subscheme $X$, restriction as an $\mathcal O_X$-module means
$$\iota^*\mathcal G=\iota^{-1}\mathcal G\otimes_{\iota^{-1}\mathcal O_Y}\mathcal O_X.$$
For an open immersion the two agree. For a closed immersion with ideal $I$, $(\iota^*\mathcal G)_x=\mathcal G_x/I_x\mathcal G_x$. At a closed point $p$ of a smooth curve, $\iota^{-1}\mathcal O_Y=\mathcal O_{Y,p}$ whereas $\iota^*\mathcal O_Y=k(p)$.
:::

::: {.front card-id="card-42718a4202cf6938"}
What is a flasque (flabby) sheaf?
:::

::: {.back card-id="card-42718a4202cf6938"}
$U\hookrightarrow V \implies \mcf(V) \twoheadrightarrow\mcf(U)$.
:::

::: {.front card-id="card-29a3dfbf0b8411fd"}
What is the higher cohomology of a flasque sheaf?
:::

::: {.back card-id="card-29a3dfbf0b8411fd"}
$H^{\geq 1}(X; \mcf) = 0$ for any flasque sheaf on any topological space, so are $\Gamma\dash$acyclic.
:::

::: {.front card-id="card-51fc917eb022892e"}
Is a morphism of sheaves injective if injective on sections? Surjective?
:::

::: {.back card-id="card-51fc917eb022892e"}
Injective: yes, surjective: no.
:::

::: {.front card-id="card-b5dfbf872b61db5b" tags="definition"}
What is: sheaf kernel/cokernel
:::

::: {.back card-id="card-b5dfbf872b61db5b"}
The kernel of $F\to G$ is the subsheaf $U\mapsto\ker(F(U)\to G(U))$. The cokernel is the sheafification of $U\mapsto\operatorname{coker}(F(U)\to G(U))$; a section of the sheaf cokernel need only have local representatives.
:::









::: {.front card-id="formula-subvariety-adjunction" tags="formula"}
For a smooth closed subvariety $Y$ of a smooth complex variety $X$, express $\omega_Y$ using $\omega_X$ and the normal bundle.
:::

::: {.back card-id="formula-subvariety-adjunction"}
$$\omega_Y\cong(\omega_X|_Y)\otimes\det N_{Y/X}.$$
:::



::: {.front card-id="formula-projective-bundle-direct-images" tags="formula"}
Let $\pi:\mathbb P(E)=\operatorname{Proj}(\operatorname{Sym}E)\to X$ use the quotient convention for a vector bundle $E$. Compute $\pi_*\mathcal O(m)$ and its higher direct images for $m\ge0$.
:::

::: {.back card-id="formula-projective-bundle-direct-images"}
$$\pi_*\mathcal O_{\mathbb P(E)}(m)=\operatorname{Sym}^mE,\qquad R^i\pi_*\mathcal O_{\mathbb P(E)}(m)=0\quad(i>0).$$
:::


::: {.front card-id="theorem-reflexive-hartogs" tags="theorem"}
Let $X$ be a normal integral Noetherian scheme and $j:U\hookrightarrow X$ an open immersion with $\operatorname{codim}_X(X\setminus U)\ge2$. State Hartogs extension for functions, reflexive coherent sheaves, and their morphisms.
:::

::: {.back card-id="theorem-reflexive-hartogs"}
There are natural isomorphisms
$$\mathcal O_X\cong j_*\mathcal O_U,\qquad \mathcal F\cong j_*(\mathcal F|_U)$$
for reflexive coherent $\mathcal F$. For reflexive coherent $\mathcal F,\mathcal G$, restriction gives
$$\operatorname{Hom}_X(\mathcal F,\mathcal G)\cong\operatorname{Hom}_U(\mathcal F|_U,\mathcal G|_U).$$
:::

::: {.front card-id="theorem-grothendieck-existence" tags="theorem"}
Let $A$ be Noetherian and $I$-adically complete, and $X\to\operatorname{Spec}A$ proper. With $X_n=X\times_A A/I^{n+1}$, state Grothendieck existence for coherent sheaves.
:::

::: {.back card-id="theorem-grothendieck-existence"}
Completion induces an equivalence
$$\operatorname{Coh}(X)\simeq\varprojlim_n\operatorname{Coh}(X_n).$$
The right side consists of coherent sheaves with compatible restriction isomorphisms. Each such system algebraizes, uniquely up to a unique isomorphism compatible with the given formal identification; morphisms algebraize as well.
:::

::: {.front card-id="theorem-krull-schmidt-bundles" tags="theorem"}
State Krull–Schmidt for vector bundles on a proper complex variety.
:::

::: {.back card-id="theorem-krull-schmidt-bundles"}
Every vector bundle is a finite direct sum of indecomposable vector bundles. The indecomposable summands are unique up to isomorphism and permutation.
:::

::: {.front card-id="application-hartogs-punctured-plane" tags="application"}
Let $U=\mathbb A^2_{\mathbb C}\setminus\{0\}$. Must every regular function on $U$ extend to $\mathbb A^2$? Must every morphism between restrictions of reflexive coherent sheaves extend? Identify the hypotheses that decide both questions.
:::

::: {.back card-id="application-hartogs-punctured-plane"}
Yes, uniquely in both cases. The ambient plane is normal and the missing point has codimension two. Hartogs extension gives $\mathcal O_{\mathbb A^2}=j_*\mathcal O_U$, hence $\Gamma(U,\mathcal O_U)=\mathbb C[x,y]$. Reflexive extension gives $\mathcal F=j_*(\mathcal F|_U)$ and the corresponding equality of Hom groups for reflexive $\mathcal F,\mathcal G$.
:::

::: {.front card-id="application-hartogs-punctured-line" tags="application"}
Does the function $x^{-1}$ on $\mathbb A^1_{\mathbb C}\setminus\{0\}$ extend regularly to $\mathbb A^1$? Which Hartogs hypothesis distinguishes this case from the punctured plane?
:::

::: {.back card-id="application-hartogs-punctured-line"}
It does not extend: a polynomial $p(x)$ with $p(x)=x^{-1}$ on $D(x)$ would satisfy $xp(x)=1$ in $\mathbb C[x]$, impossible at $x=0$. The line is normal, but the missing point has codimension one. Hartogs extension requires codimension at least two.
:::

::: {.front card-id="application-formal-algebraization" tags="application"}
Let $X$ be proper over $\mathbb C[[t]]$ and $X_n=X\times\operatorname{Spec}\mathbb C[t]/(t^{n+1})$. Given coherent sheaves $\mathcal F_n$ with compatible restriction isomorphisms on all $X_n$, can they come from a coherent sheaf on $X$? Which result gives existence rather than merely computing cohomology?
:::

::: {.back card-id="application-formal-algebraization"}
Grothendieck existence algebraizes the compatible system to a coherent sheaf $\mathcal F$ on $X$. Completion is an equivalence of categories, so morphisms also algebraize uniquely and $\mathcal F$ is unique up to the isomorphism specified by the compatible system. Formal functions instead computes completed cohomology of a sheaf already given.
:::

::: {.front card-id="application-bundles-same-chern-different" tags="application"}
On $\mathbb P^1_{\mathbb C}$, compare $E=\mathcal O\oplus\mathcal O(2)$ and $F=\mathcal O(1)^{\oplus2}$. They have the same rank and degree. Are they isomorphic? Give a cohomological test and explain the role of indecomposable summands.
:::

::: {.back card-id="application-bundles-same-chern-different"}
They are not isomorphic:
$$h^0(E(-2))=h^0(\mathcal O(-2))+h^0(\mathcal O)=1,\qquad h^0(F(-2))=2h^0(\mathcal O(-1))=0.$$
Their line-bundle summands are indecomposable. Krull–Schmidt also distinguishes the multisets $\{\mathcal O,\mathcal O(2)\}$ and $\{\mathcal O(1),\mathcal O(1)\}$; rank and degree alone do not determine a bundle.
:::

::: {.front card-id="theorem-birkhoff-grothendieck" tags="theorem"}
State the Birkhoff–Grothendieck classification of vector bundles on $\mathbb P^1_k$, including its uniqueness assertion.
:::

::: {.back card-id="theorem-birkhoff-grothendieck"}
Every rank-$r$ vector bundle has a splitting
$$E\simeq\bigoplus_{i=1}^r\mathcal O_{\mathbb P^1}(a_i),$$
where the multiset of integers $\{a_1,\ldots,a_r\}$ is unique. The isomorphism giving the splitting need not be unique.
:::

::: {.front card-id="application-splitting-cohomology-p1" tags="application"}
For $E=\mathcal O(2)\oplus\mathcal O\oplus\mathcal O(-2)$ on $\mathbb P^1_k$, compute $h^0(E)$ and $h^1(E)$. Is $E$ globally generated?
:::

::: {.back card-id="application-splitting-cohomology-p1"}
Using $h^0(\mathcal O(a))=\max\{a+1,0\}$ and $h^1(\mathcal O(a))=\max\{-a-1,0\}$ gives $h^0(E)=4$ and $h^1(E)=1$. It is not globally generated because its quotient $\mathcal O(-2)$ has no global sections.
:::

::: {.front card-id="theorem-bogomolov-discriminant" tags="theorem"}
Let $E$ be a torsion-free sheaf of rank $r$ on a smooth complex projective surface, slope-semistable for an ample polarization. State Bogomolov's inequality.
:::

::: {.back card-id="theorem-bogomolov-discriminant"}
The degree of its discriminant is nonnegative:
$$\Delta(E)=2r\,c_2(E)-(r-1)c_1(E)^2\ge0.$$
Here Chern classes of degree four are evaluated on the surface.
:::

::: {.front card-id="application-bogomolov-rank-two" tags="application"}
Can a rank-two torsion-free sheaf on a smooth complex projective surface with $c_1^2=9$ and $c_2=2$ be slope-semistable for an ample polarization? Does $c_2=3$ force semistability?
:::

::: {.back card-id="application-bogomolov-rank-two"}
For $c_2=2$, the discriminant is $4\cdot2-9=-1$, so Bogomolov's inequality rules out semistability for every ample polarization. For $c_2=3$, the discriminant is $3$, which satisfies a necessary condition but does not imply semistability; that requires checking slopes of subsheaves.
:::

::: {.front card-id="application-splitting-bundle-deformations" tags="application"}
Let $E=\mathcal O\oplus\mathcal O(2)$ on $\mathbb P^1_k$. Compute the tangent space dimension for deformations of $E$ with $\mathbb P^1$ fixed. Are these deformations obstructed? Express the answer using the splitting of $\mathcal E nd(E)$.
:::

::: {.back card-id="application-splitting-bundle-deformations"}
The tangent space is $H^1(\mathbb P^1,\mathcal E nd(E))$, and obstructions lie in $H^2(\mathbb P^1,\mathcal E nd(E))$. Here
$$\mathcal E nd(E)\simeq\mathcal O^{\oplus2}\oplus\mathcal O(2)\oplus\mathcal O(-2).$$
Only $\mathcal O(-2)$ contributes to $H^1$, with dimension one. The obstruction group vanishes because the base is a curve, so deformations are unobstructed.
:::

::: {.front card-id="card-908c9b1975baecaf" tags="definition"}
What is the definition of Adic completion?
:::

::: {.back card-id="card-908c9b1975baecaf"}
Let $A$ be a ring and $I\subseteq A$ an ideal. The $I$-adic completion is $\hat A=\varprojlim_nA/I^n$, and for an $A$-module $M$, $\hat M=\varprojlim_nM/I^nM$. A ring or module is $I$-adically complete if the natural map to its completion is an isomorphism.
:::

::: {.front card-id="card-fa3280b335bb471e" tags="definition"}
What is the definition of Chern character?
:::

::: {.back card-id="card-fa3280b335bb471e"}
For a complex vector bundle $E$ with Chern roots $x_i$, so that $c(E)=\prod_i(1+x_i)$, the Chern character is $\operatorname{ch}(E)=\sum_i e^{x_i}=r+c_1+\frac12(c_1^2-2c_2)+\cdots$. It is additive on direct sums and multiplicative on tensor products, and defines a ring homomorphism $K^0(X)\to H^{\mathrm{even}}(X;\mathbb Q)$ (or to Chow).
:::

::: {.front card-id="card-16dba6ebfc4da924" tags="definition"}
What is the definition of Coherent sheaf?
:::

::: {.back card-id="card-16dba6ebfc4da924"}
An $\mathcal O_X$-module $\mathcal F$ that is locally finitely presented: every point has an open neighborhood $U$ with an exact sequence $\mathcal O_U^{\oplus p}\to\mathcal O_U^{\oplus q}\to\mathcal F|_U\to0$. On a locally Noetherian scheme this is equivalent to $\mathcal F$ being quasi-coherent and locally finitely generated.
:::

::: {.front card-id="card-ace0c2938920f9ce" tags="definition"}
What is the definition of De rham complex?
:::

::: {.back card-id="card-ace0c2938920f9ce"}
For a smooth morphism $f:X\to S$, the relative de Rham complex is $(\Omega^\bullet_{X/S},d)$ with $\Omega^p_{X/S}=\bigwedge^p\Omega^1_{X/S}$ and exterior derivative $d$. For $X$ smooth over $\mathbb C$, the holomorphic de Rham complex computes $H^*(X;\mathbb C)$.
:::

::: {.front card-id="card-0769f306cf9658f6" tags="definition"}
What is the definition of Determinant line bundle?
:::

::: {.back card-id="card-0769f306cf9658f6"}
For a locally free $\mathcal O_X$-module $\mathcal E$ of rank $r$, the determinant line bundle is $\det\mathcal E=\bigwedge^r\mathcal E$. It satisfies $\det(\mathcal E\otimes\mathcal F)\cong(\det\mathcal E)^{\otimes\operatorname{rank}\mathcal F}\otimes(\det\mathcal F)^{\otimes\operatorname{rank}\mathcal E}$ and $\det(\mathcal E^\vee)\cong(\det\mathcal E)^{-1}$. The canonical sheaf is $\omega_{X/S}=\det\Omega_{X/S}$.
:::

::: {.front card-id="card-1293c7c7ab45cc4d" tags="definition"}
What is the definition of Discriminant of a coherent sheaf?
:::

::: {.back card-id="card-1293c7c7ab45cc4d"}
For a torsion-free coherent sheaf $E$ of rank $r$ on a smooth projective surface $X$, the discriminant is $\Delta(E)=2r\,c_2(E)-(r-1)c_1(E)^2$, with Chern classes evaluated on $X$. Bogomolov's inequality says $\Delta(E)\ge0$ when $E$ is slope-semistable for an ample polarization.
:::

::: {.front card-id="card-3e7e3f4ff64aefbc" tags="definition"}
What is the definition of Dual sheaf?
:::

::: {.back card-id="card-3e7e3f4ff64aefbc"}
For an $\mathcal O_X$-module $\mathcal F$, the dual sheaf is $\mathcal F^\vee=\mathop{\mathcal H\!\mathit{om}}_{\mathcal O_X}(\mathcal F,\mathcal O_X)$. If $\mathcal F$ is locally free of finite rank, so is $\mathcal F^\vee$ and $\mathcal F^{\vee\vee}\cong\mathcal F$; for a vector bundle $E$, $E^\vee$ is the dual bundle.
:::

::: {.front card-id="card-67996880ed82c036" tags="definition"}
What is the definition of Flat module?
:::

::: {.back card-id="card-67996880ed82c036"}
An $R$-module $M$ is flat if $-\otimes_RM$ is exact, equivalently $\operatorname{Tor}_1^R(N,M)=0$ for all $N$. Over a Noetherian local ring, a finitely generated flat module is free. An $\mathcal O_X$-module is flat if all its stalks are flat modules.
:::

::: {.front card-id="card-335fc8d773ec3615" tags="definition"}
What is the definition of Global generation?
:::

::: {.back card-id="card-335fc8d773ec3615"}
A sheaf $\mathcal F$ on a scheme $X$ is globally generated (generated by global sections) if the evaluation map $H^0(X,\mathcal F)\otimes_k\mathcal O_X\to\mathcal F$ is surjective. Equivalently, $\mathcal F$ is a quotient of a free $\mathcal O_X$-module.
:::

::: {.front card-id="card-fa7c72c455f002a2" tags="definition"}
What is the definition of Invertible sheaf?
:::

::: {.back card-id="card-fa7c72c455f002a2"}
A coherent $\mathcal O_X$-module $\mathcal L$ that is locally free of rank one: every point of $X$ has an open neighborhood $U$ with $\mathcal L|_U\cong\mathcal O_U$. Isomorphism classes of invertible sheaves form the Picard group $\operatorname{Pic}(X)$ under tensor product.
:::

::: {.front card-id="card-9e38f6a7ebcfafbd" tags="definition"}
What is the definition of Locally closed subscheme?
:::

::: {.back card-id="card-9e38f6a7ebcfafbd"}
A subscheme $Z\subseteq X$ is locally closed if it factors as a closed immersion followed by an open immersion, $Z\hookrightarrow U\hookrightarrow X$ with $U\subseteq X$ open; equivalently, $Z$ is closed in some open subscheme of $X$.
:::

::: {.front card-id="card-821eed739824f067" tags="definition"}
What is the definition of Quasi-coherent sheaf?
:::

::: {.back card-id="card-821eed739824f067"}
An $\mathcal O_X$-module $\mathcal F$ such that every point has an affine open neighborhood $\operatorname{Spec}A\subseteq X$ with $\mathcal F|_{\operatorname{Spec}A}\cong\widetilde M$ for some $A$-module $M$. Equivalently, the natural map $\widetilde{\Gamma(U,\mathcal F)}\to\mathcal F|_U$ is an isomorphism for every affine open $U$.
:::

::: {.front card-id="card-108b8c6794adf283" tags="definition"}
What is the definition of Sheaf of sections?
:::

::: {.back card-id="card-108b8c6794adf283"}
For a vector bundle $\pi:E\to X$, the sheaf of sections is the $\mathcal O_X$-module $\mathcal E$ with $\mathcal E(U)=\Gamma(U,\pi^{-1}(U))$. The functor sending a vector bundle to its sheaf of sections is an equivalence between rank-$r$ geometric vector bundles and rank-$r$ locally free $\mathcal O_X$-modules; the inverse sends a locally free sheaf $\mathcal E$ to $\mathbf V(\mathcal E^\vee)=\operatorname{Spec}\operatorname{Sym}(\mathcal E^\vee)$. With the convention $\mathbf V(\mathcal E)=\operatorname{Spec}\operatorname{Sym}\mathcal E$, the sheaf of sections of $\mathbf V(\mathcal E)$ is $\mathcal E^\vee$.
:::

::: {.front card-id="card-bf0b7cb5e4e96d23" tags="definition"}
What is the definition of Todd class?
:::

::: {.back card-id="card-bf0b7cb5e4e96d23"}
The Todd class of a complex vector bundle $E$ with Chern roots $x_i$ is $\operatorname{td}(E)=\prod_i\frac{x_i}{1-e^{-x_i}}=1+\frac12c_1+\frac1{12}(c_1^2+c_2)+\frac1{24}c_1c_2+\cdots$. For a smooth complex variety $X$, Hirzebruch–Riemann–Roch states $\chi(X,E)=\int_X\operatorname{ch}(E)\operatorname{td}(T_X)$.
:::

::: {.front card-id="card-cbf5274d915bb1de" tags="definition"}
What is the definition of Transition map?
:::

::: {.back card-id="card-cbf5274d915bb1de"}
Given a vector bundle trivialized on an open cover $\{U_i\}$, the transition maps are the isomorphisms $g_{ij}:U_i\cap U_j\to\operatorname{GL}_r$ obtained by composing the two trivializations. They satisfy the cocycle condition $g_{ij}g_{jk}=g_{ik}$ on $U_i\cap U_j\cap U_k$ and determine the bundle up to isomorphism.
:::

::: {.front card-id="card-1607f09d94068d2f" tags="definition"}
What is the definition of Upper shriek functor?
:::

::: {.back card-id="card-1607f09d94068d2f"}
For a proper morphism $f:X\to Y$, the upper shriek (exceptional inverse image) $f^!$ is the right adjoint of $Rf_*$ on the derived category of quasi-coherent sheaves, characterized by Grothendieck duality; in the six-functor formalism it is right adjoint to $Rf_!$. For a smooth proper morphism of relative dimension $n$, $f^!\mathcal O_Y\cong\omega_{X/Y}[n]$.
:::

::: {.front card-id="card-5eb338b953c97fe3" tags="definition"}
What is the definition of Vector bundle?
:::

::: {.back card-id="card-5eb338b953c97fe3"}
A locally free sheaf of finite rank: an $\mathcal O_X$-module $\mathcal E$ such that every point has an open neighborhood $U$ with $\mathcal E|_U\cong\mathcal O_U^{\oplus r}$. Equivalently, the geometric vector bundle $\operatorname{Spec}_{\mathcal O_X}(\operatorname{Sym}^\bullet\mathcal E^\vee)\to X$.
:::

::: {.front card-id="card-fe386c7fc751fa8c" tags="definition"}
What is the definition of Étalé space?
:::

::: {.back card-id="card-fe386c7fc751fa8c"}
For a presheaf $F$ on $X$, the étalé space is $\coprod_{x\in X}F_x$ with the topology making the projection to $X$ a local homeomorphism; its sheaf of continuous sections is the sheafification $F^+$. A sheaf is equivalent to a local homeomorphism over $X$.
:::
