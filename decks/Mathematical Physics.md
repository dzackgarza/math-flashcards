---
title: "Mathematical Physics"
---

::: {.front card-id="curve-counting-gw-dt-pt-comparison" tags="comparison"}
Compare the objects and discrete data in GW, ideal-sheaf DT, and PT curve counting on a smooth projective complex threefold. Where can extra points occur?
:::

::: {.back card-id="curve-counting-gw-dt-pt-comparison"}
| Theory | Object | Fixed data | Extra geometry |
| --- | --- | --- | --- |
| GW | Stable map $f:(C,p_i)\to X$ | $g,\beta=f_*[C]$, number of marks | Multiple covers, contracted components, nodal domains |
| DT | Ideal sheaf $I_Z\subset\mathcal O_X$, $\dim Z\le1$ | $\beta=[Z]$, $n=\chi(\mathcal O_Z)$ | Embedded and isolated zero-dimensional components |
| PT | Section $s:\mathcal O_X\to F$; $F$ pure one-dimensional, cokernel supported at finitely many points (possibly zero) | $\beta=[F]\ne0$, $n=\chi(F)$ | Cokernel on the supporting curve; no zero-dimensional subsheaf of $F$ |

All require obstruction theory and a virtual class. GW uses a proper Deligne–Mumford stack; DT and PT here use projective moduli schemes. For threefolds their complex virtual dimensions are $\int_\beta c_1(TX)+m$ for GW with $m$ marks and $\int_\beta c_1(TX)$ for DT/PT. Zero virtual dimension permits integration of $1$.
:::

::: {.front card-id="curve-counting-gw-lines-and-constant-maps" tags="application"}
Compute the genus-zero GW invariant of $\mathbb P^2$ counting lines through two distinct points. What does the degree-zero, three-point invariant recover?
:::

::: {.back card-id="curve-counting-gw-lines-and-constant-maps"}
For $\beta=[\text{line}]$ and two marks, $v=-1+3+2=4$. Each point insertion has complex codimension two, so
$$\langle[\mathrm{pt}],[\mathrm{pt}]\rangle^{\mathbb P^2}_{0,1}=1.$$
There is a unique line through the points; its degree-one parametrization has no automorphisms commuting with the map. Convexity of $\mathbb P^2$ makes genus-zero maps unobstructed. Distinct incidence points exclude contracted tails in this case.

For any smooth projective $X$, $\overline{\mathcal M}_{0,3}(X,0)=X$ and the obstruction $H^1(\mathbb P^1,\mathcal O)\otimes TX$ vanishes. Thus
$$\langle\alpha,\beta,\gamma\rangle^X_{0,0}=\int_X\alpha\cup\beta\cup\gamma.$$
Unmarked degree-zero genus-zero maps are unstable; this calculation cannot use $\overline{\mathcal M}_{0,0}(X,0)=X$.
:::

::: {.front card-id="curve-counting-symplectic-and-noncompact" tags="definition comparison"}
Define symplectic GW invariants. What extra issue occurs for a noncompact target?
:::

::: {.back card-id="curve-counting-symplectic-and-noncompact"}
For a closed symplectic manifold $(X,\omega)$ of real dimension $2d$, choose an $\omega$-tame almost-complex structure $J$: $\omega(v,Jv)>0$ for $v\ne0$. Stable $J$-holomorphic maps satisfy $df\circ j=J\circ df$ and have fixed genus, markings, and class $\beta$.
$$\operatorname{vdim}_{\mathbb R}=2\bigl((1-g)(d-3)+\langle c_1(TX,J),\beta\rangle+n\bigr).$$
Gromov compactness adds nodal bubble trees; virtual perturbation theory gives the class used for the same evaluation/descendant integrals. The invariants are independent of the auxiliary tame $J$ and invariant under symplectic deformation. Smooth moduli of the expected dimension are not required. For projective $X$ with its Kähler form, algebraic and symplectic GW invariants agree.

Noncompact $X$ can allow curves or points to escape, so an ordinary integral need not exist. One must establish properness of the relevant moduli or specify an equivariant theory with proper torus-fixed loci. Virtual localization then integrates fixed-locus virtual classes divided by equivariant Euler classes of virtual normal bundles; the result can depend on equivariant parameters. “Toric” alone does not make a nonequivariant count proper.
:::

::: {.front card-id="curve-counting-dt-definition" tags="definition"}
Define the ideal-sheaf Donaldson–Thomas moduli space and invariant. How do a general threefold and a Calabi–Yau threefold differ?
:::

::: {.back card-id="curve-counting-dt-definition"}
$X/\mathbb C$ smooth projective of dimension three:
$$I_n(X,\beta)=\{I_Z\subset\mathcal O_X:\dim Z\le1,\ [Z]=\beta,\ \chi(\mathcal O_Z)=n\}.$$
The curve class counts generic lengths along one-dimensional components. Fixing $\beta,n$ fixes the Hilbert polynomial. Rank-one ideal sheaves have determinant $\mathcal O_X$.

Fixed-determinant deformation theory has tangent and obstruction spaces $\operatorname{Ext}^1(I_Z,I_Z)_0$ and $\operatorname{Ext}^2(I_Z,I_Z)_0$, where the subscript denotes the trace-free part. It gives
$$[I_n(X,\beta)]^{\mathrm{vir}}\in A_{\int_\beta c_1(TX)}(I_n(X,\beta)).$$
If $\int_\beta c_1(TX)=0$, define $\mathrm{DT}_{n,\beta}=\deg[I_n(X,\beta)]^{\mathrm{vir}}$. Otherwise numerical invariants require insertions of matching codimension. For $K_X\cong\mathcal O_X$, Serre duality makes this obstruction theory symmetric and the virtual dimension zero.

This is rank-one curve-counting DT theory. Higher-rank DT theory instead fixes Chern data and a stability condition for sheaves or complexes; strictly semistable objects require additional theory.
:::

::: {.front card-id="curve-counting-pt-definition" tags="definition comparison"}
Define a PT stable pair, its moduli space, and its invariant. Distinguish PT stability from KSBA stability.
:::

::: {.back card-id="curve-counting-pt-definition"}
On a smooth projective complex threefold $X$, a PT pair is
$$s:\mathcal O_X\longrightarrow F,\qquad
F\text{ pure of dimension }1,\quad\dim\operatorname{Supp}(\operatorname{coker}s)\le0.$$
The cokernel may be zero.
Purity: every nonzero coherent subsheaf of $F$ has one-dimensional support. Isomorphisms $\phi:F\to F'$ satisfy $\phi s=s'$; a stable pair has no nontrivial automorphisms.

The projective scheme $P_n(X,\beta)$ fixes the fundamental cycle class $[F]=\beta\ne0$ and $\chi(F)=n$. Use the complex $I^\bullet=[\mathcal O_X\to F]$ in degrees $0,1$ with fixed determinant, rather than arbitrary independent deformations of $F$ and $s$. Its trace-free $\operatorname{Ext}^{1,2}$ give a perfect obstruction theory of virtual dimension $\int_\beta c_1(TX)$.
$$\mathrm{PT}_{n,\beta}=\deg[P_n(X,\beta)]^{\mathrm{vir}}
\quad\text{when }\int_\beta c_1(TX)=0.$$
This includes $K_X\cong\mathcal O_X$; other dimensions require insertions.

KSBA pairs are varieties with boundary $(Y,\Delta)$ satisfying semi-log-canonicity and ampleness of $K_Y+\Delta$. They are different objects.

Reference: Pandharipande–Thomas, [Curve counting via stable pairs](https://people.math.ethz.ch/~rahul/pt.pdf), §§1–2.
:::

::: {.front card-id="curve-counting-pairs-on-smooth-curve" tags="application comparison"}
Let $i:C\hookrightarrow X$ be a smooth connected curve in a smooth threefold. Construct PT pairs from effective divisors on $C$, compute their Euler characteristics, and contrast DT extra points.
:::

::: {.back card-id="curve-counting-pairs-on-smooth-curve"}
For an effective divisor $D$ of degree $d$,
$$\mathcal O_X\longrightarrow i_*\mathcal O_C(D),\qquad
0\longrightarrow\mathcal O_C\longrightarrow\mathcal O_C(D)
\longrightarrow\mathcal O_D(D)\longrightarrow0.$$
The middle sheaf is pure; the cokernel has length $d$. Thus $\beta=[C]$ and
$$n=\chi(\mathcal O_C(D))=1-g(C)+d.$$
Pairs whose sheaf has generic rank one and scheme-theoretic support exactly this smooth $C$ are parametrized by $\operatorname{Sym}^dC$. For $C=\mathbb P^1$, this is $\mathbb P^d$ and $n=d+1$. This describes the fixed-support locus, not its virtual contribution in an arbitrary ambient $X$.

DT permits $Z=C\sqcup Q$ with a disjoint length-$d$ subscheme $Q$: then $\chi(\mathcal O_Z)=1-g+d$ too. PT excludes $F=i_*\mathcal O_C\oplus\mathcal O_Q$, because $\mathcal O_Q$ is a zero-dimensional subsheaf. Equal numerical data do not identify the moduli problems.
:::

::: {.front card-id="curve-counting-behrend-weight" tags="definition application"}
How does the Behrend function recover numerical DT/PT invariants on a proper Calabi–Yau threefold moduli space? Compute the one-point DT invariant.
:::

::: {.back card-id="curve-counting-behrend-weight"}
A proper complex scheme $M$ with symmetric perfect obstruction theory has
$$\deg[M]^{\mathrm{vir}}=\chi(M,\nu_M)
=\sum_{k\in\mathbb Z}k\,\chi_c(\nu_M^{-1}(k)),$$
where $\nu_M:M\to\mathbb Z$ is Behrend's constructible function. If $M$ is smooth of complex dimension $d$, $\nu_M=(-1)^d$. Smooth positive-dimensional moduli can therefore have nonzero virtual counts.

For $X$ a smooth projective threefold with $K_X\cong\mathcal O_X$,
$$I_1(X,0)=\operatorname{Hilb}^1(X)=X,\qquad
\mathrm{DT}_{1,0}=-\chi(X).$$
This is not the ordinary number of points of $X$. PT has no nonzero pure one-dimensional sheaf of class zero on projective $X$; the constant term $1$ used in PT partition functions is a convention for the empty configuration.

Reference: Behrend, [Donaldson–Thomas invariants via microlocal geometry](https://arxiv.org/abs/math/0507523).
:::

::: {.front card-id="curve-counting-local-rational-pt" tags="application"}
Compute the primitive-class PT invariants of the local $(-1,-1)$ rational curve.
:::

::: {.back card-id="curve-counting-local-rational-pt"}
Let $X=\operatorname{Tot}(\mathcal O_{\mathbb P^1}(-1)\oplus\mathcal O_{\mathbb P^1}(-1))$ and $\beta$ the zero-section class. Every compact curve of class $\beta$ is the rigid zero section $C$; the normal bundle has $H^0(N_{C/X})=0$.

A pair in class $\beta$ is $\mathcal O_X\to i_*\mathcal O_C(D)$ with $D$ effective of degree $d=n-1$. Hence
$$P_n(X,\beta)=\operatorname{Sym}^{n-1}\mathbb P^1=\mathbb P^{n-1}
\quad(n\ge1),\qquad P_n(X,\beta)=\varnothing\quad(n\le0).$$
These moduli are proper despite noncompact $X$. The compactly supported Calabi–Yau obstruction theory is symmetric and the moduli are smooth, so
$$\mathrm{PT}_{n,\beta}=(-1)^{n-1}\chi(\mathbb P^{n-1})=(-1)^{n-1}n,\qquad
\sum_n\mathrm{PT}_{n,\beta}q^n=\frac{q}{(1+q)^2}.$$
The first terms are $q-2q^2+3q^3$. The sign comes from the Behrend function, not from the Euler characteristic alone.

Reference: Pandharipande–Thomas, [Curve counting via stable pairs](https://people.math.ethz.ch/~rahul/pt.pdf), §4.1.
:::

::: {.front card-id="curve-counting-correspondence-normalizations" tags="comparison"}
What normalization and change of variables enter the GW/DT/PT correspondences for a projective Calabi–Yau threefold?
:::

::: {.back card-id="curve-counting-correspondence-normalizations"}
Use formal curve variables $Q^\beta$ and Euler-characteristic variable $q$:
$$Z_{\mathrm{DT}}=\sum_{\beta,n}\mathrm{DT}_{n,\beta}q^nQ^\beta,\qquad
Z_{\mathrm{PT}}=1+\sum_{\beta\ne0,n}\mathrm{PT}_{n,\beta}q^nQ^\beta.$$
The degree-zero DT factor counts points:
$$Z_{\mathrm{DT},0}=M(-q)^{\chi(X)},\qquad
M(q)=\prod_{m\ge1}(1-q^m)^{-m}.$$
The DT/PT correspondence identifies $Z_{\mathrm{DT}}/Z_{\mathrm{DT},0}$ with $Z_{\mathrm{PT}}$ in the projective Calabi–Yau setting.

For GW, first form the disconnected partition function from connected invariants, excluding degree-zero connected components:
$$Z'_{\mathrm{GW}}=\exp\left(\sum_{\beta\ne0,g\ge0}
N_{g,\beta}u^{2g-2}Q^\beta\right).$$
The GW/PT correspondence predicts $Z'_{\mathrm{GW}}=Z_{\mathrm{PT}}$ after $q=-e^{iu}$, interpreted through rational functions and their expansions, not termwise substitution into arbitrary formal Laurent series. GW/PT is a theorem in important classes such as toric threefolds with the required equivariant conventions; do not assert the unrestricted correspondence for every threefold. Raw GW, DT, and PT coefficients are not equal.

Reference: Bridgeland, [Hall algebras and curve-counting invariants](https://arxiv.org/abs/1002.4374), for the DT/PT theorem.
:::

::: {.front card-id="gauge-asd-equation-and-quotient" tags="definition comparison"}
Define the ASD equations and instanton moduli space on an oriented Riemannian four-manifold. Explain gauge equivalence, reducibility, and dependence on orientation and metric.
:::

::: {.back card-id="gauge-asd-equation-and-quotient"}
For a principal compact group bundle $P\to X$,
$$*^2=1\text{ on }\Omega^2,\qquad F_A^\pm=\tfrac12(F_A\pm*F_A),\qquad
F_A^+=0\iff *F_A=-F_A.$$
The gauge group $\mathcal G(P)$ consists of bundle automorphisms over $\mathrm{id}_X$; locally,
$$A\mapsto u^{-1}Au+u^{-1}du,\qquad F_A\mapsto u^{-1}F_Au,\qquad
\mathcal M_{\mathrm{ASD}}(P,g)=\{A:F_A^+=0\}/\mathcal G(P).$$
An irreducible connection $A$ satisfies $\operatorname{Stab}_{\mathcal G}(A)=Z(G)$; a larger stabilizer is reducible. For $\mathrm{SU}(2)$, reducibility means a parallel splitting $E=L\oplus L^{-1}$.

Orientation reversal exchanges self-dual and anti-self-dual forms. The star on two-forms in real dimension four is conformally invariant, so ASD depends on the conformal class of the metric. Since $d_AF_A=0$, ASD implies $d_A*F_A=0$, hence Yang–Mills.
:::

::: {.front card-id="gauge-asd-energy-and-charge" tags="formula application"}
For an $\mathrm{SU}(2)$ connection on a closed oriented Riemannian four-manifold, relate instanton number, Yang–Mills energy, and ASD. Fix all sign and energy conventions.
:::

::: {.back card-id="gauge-asd-energy-and-charge"}
Use skew-Hermitian matrices and $\langle a,b\rangle=-\operatorname{tr}(ab)$ in the defining representation; energy has no factor $\tfrac12$:
$$k=\langle c_2(E),[X]\rangle=\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A),\qquad
\mathrm{YM}(A)=-\int_X\operatorname{tr}(F_A\wedge*F_A).$$
Orthogonality of the two star eigenspaces gives
$$8\pi^2k=\|F_A^-\|^2-\|F_A^+\|^2,\qquad
\mathrm{YM}(A)=8\pi^2k+2\|F_A^+\|^2\ge8\pi^2k.$$
Thus ASD minimizes energy in a fixed bundle and has energy $8\pi^2k$. In general $\mathrm{YM}\ge8\pi^2|k|$, with equality for the corresponding duality sign. An ASD connection with $k=0$ is flat; with $k<0$ none exists. A charge-one ASD instanton on the round $S^4$ has energy $8\pi^2$.

Reference: Lotay, [Calibrated Geometry and Gauge Theory](https://people.maths.ox.ac.uk/lotay/cggt2022.pdf), §6.3.
:::

::: {.front card-id="gauge-asd-deformation-complex" tags="definition formula"}
Give the deformation complex and expected dimension of the unframed $\mathrm{SU}(2)$ ASD moduli space. When does the expected dimension equal the local dimension?
:::

::: {.back card-id="gauge-asd-deformation-complex"}
At an ASD connection on a closed connected oriented four-manifold,
$$0\longrightarrow\Omega^0(\operatorname{ad}P)
\xrightarrow{d_A}\Omega^1(\operatorname{ad}P)
\xrightarrow{d_A^+}\Omega^2_+(\operatorname{ad}P)\longrightarrow0.$$
The composite is $[F_A^+,-]=0$. Its cohomology gives infinitesimal stabilizers $H_A^0$, deformations $H_A^1$, and an obstruction space $H_A^2$. Coulomb gauge imposes $d_A^*a=0$; the nonlinear equation is $d_A^+a+(a\wedge a)^+=0$.
$$\operatorname{ind}(d_A^*\oplus d_A^+)
=\dim H_A^1-\dim H_A^0-\dim H_A^2
=8k-3(1-b_1+b_2^+).$$
At an irreducible regular point ($H_A^0=H_A^2=0$), the effective gauge quotient is smooth of this real dimension. Otherwise use the Kuranishi zero locus in $H_A^1$ modulo the stabilizer.

For $S^4$ and $k=1$, $b_1=b_2^+=0$, so the unframed expected dimension is $5$; retaining a framing adds the three gauge directions.
:::

::: {.front card-id="gauge-uhlenbeck-and-donaldson" tags="definition comparison"}
What does Uhlenbeck compactification add, and how do Donaldson invariants use ASD moduli?
:::

::: {.back card-id="gauge-uhlenbeck-and-donaldson"}
For fixed-charge $\mathrm{SU}(2)$ ASD connections on a closed four-manifold, a sequence can concentrate curvature at finitely many points. After gauge transformations it converges smoothly away from them to charge $k-\ell$. The ideal limit records a zero-cycle of length $\ell$:
$$\overline{\mathcal M}_k\subseteq
\coprod_{\ell=0}^k\mathcal M_{k-\ell}\times\operatorname{Sym}^{\ell}X.$$
Each unit of lost charge carries energy $8\pi^2$. This is bubbling, not a failure of the topological charge formula.

On the irreducible moduli, the universal adjoint bundle $\mathbb P$ defines
$$\mu(\alpha)=-\tfrac14p_1(\mathbb P)/\alpha
\in H^{4-i}(\mathcal M;\mathbb Q),\qquad \alpha\in H_i(X),$$
where $/$ is slant product. Donaldson invariants evaluate products of $\mu$-classes of total degree equal to the moduli dimension, using regularized moduli, compactification, and geometric representatives. They require orientation data and control of reducibles; they are not naive integrals over an arbitrary singular quotient. For closed simply connected $X$ with $b_2^+>1$, the resulting invariants are independent of generic metric choices; $b_2^+=1$ requires chambers. Point and surface classes have degrees four and two.
:::

::: {.front card-id="gauge-asd-kahler-surface" tags="comparison application"}
Translate ASD for a unitary connection on a Kähler surface into complex-geometric equations. Compare with Hermitian–Einstein connections.
:::

::: {.back card-id="gauge-asd-kahler-surface"}
Use the complex orientation:
$$\Lambda^2_+\otimes\mathbb C
=\mathbb C\omega\oplus\Lambda^{2,0}\oplus\Lambda^{0,2},\qquad
\Lambda^2_-\otimes\mathbb C=\Lambda^{1,1}_0.$$
Consequently,
$$F_A^+=0\iff F_A^{0,2}=0\ \text{and}\ \Lambda_\omega F_A=0.$$
Unitarity supplies $F_A^{2,0}=-(F_A^{0,2})^*$. The first equation defines an integrable holomorphic structure; the second says its curvature is primitive.

A Hermitian–Einstein connection satisfies $F_A^{0,2}=0$ and $i\Lambda_\omega F_A=\lambda\,\mathrm{id}$, with $\lambda$ determined by slope. The Donaldson–Uhlenbeck–Yau theorem identifies polystable holomorphic bundles on compact Kähler manifolds with bundles admitting such a metric. On a surface, slope zero gives $\lambda=0$, hence ASD; nonzero slope gives ASD only for the trace-free curvature. Stability corresponds to irreducibility.
:::

::: {.front card-id="card-8edb2235ecd7bad5"}
Describe geometric Langlands.
:::

::: {.back card-id="card-8edb2235ecd7bad5"}
$\rho \in \mcx(\pi_1\Sigma_g, G)\leadsto$ a flat connection $\nabla_\rho$ on a principal $G\dash$bundle over $C$

Irreducible such connections $\rightleftharpoons$ $R\in    {}_\mcd\Mod (\Bun_{{}^L G})$.
:::

::: {.front card-id="card-e0267814e9c4ee2e"}
What is a large complex structure limit?
:::

::: {.back card-id="card-e0267814e9c4ee2e"}
Idea: line bundle $L$ over the total space of a family which specifies $c_1(L)$ and thus a symplectic class.

A polarized algebraic family of $n$-dim CY manifolds $X \rightarrow S \backslash\{0\}$ over a punctured algebraic curve, whose 'essential skeleton' (simplicial subcomplex of dual complex) has dimension $n$.

Also called "maximal degeneration"

Semistable SNC model.
:::

::: {.front card-id="card-a62507d3e1e915e7"}
What is $\Bun_G$?
:::

::: {.back card-id="card-a62507d3e1e915e7"}
$\Bun_G(k)$ is the maximal subgroupoid of ${\mathsf{G}\dash\mathsf{Torsors}}_{/ {X}}$.

Forms an algebraic stack.

Observation due to Weil: $\dcoset{G(F)}{G({\mathbf{A}}_F)}{\prod_{x\in {\left\lvert {X} \right\rvert}}' G({\mathcal{O}}_x)}  { \, \xrightarrow{\sim}\, }\Bun_G$ where $F= k(X)$, $F_x$ is the completion at $x$, and ${\mathcal{O}}_x$ is its valuation ring. Supposed to resemble
$$\dcoset{G(F)}{G({\mathbf{A}}_F)}{K }$$
:::

::: {.front card-id="card-8e8acdcff9808d4b"}
What are Higgs bundles? Why care?
:::

::: {.back card-id="card-8e8acdcff9808d4b"}
$(E, \theta)$ where $E$ is a holomorphic bundle and $\theta: E\to E\otimes\Omega^1_{X}$ is an endomorphism-valued 1-form satisfying $\theta\wedge \theta =0$.

On a curve $C$, $\theta\wedge\theta=0$ is automatic and $\theta\in H^0(C,\operatorname{End}(E)\otimes K_C)$, so $\bar\partial_E\theta=0$. Fixed determinant and trace-free Higgs fields use $\operatorname{End}_0(E)$.

On a compact Kähler manifold, polystable Higgs bundles with vanishing rational Chern classes correspond to semisimple complex representations of $\pi_1(X)$ up to conjugacy. Stable bundles correspond to irreducible representations. On a curve the Chern-class condition is $\deg E=0$; stability tests only $\theta$-invariant subbundles. Harmonic metrics construct the correspondence.
:::

::: {.front card-id="card-5ab68700993ee9f6"}
What is Batyrev-Borisov's mirror symmetry?
:::

::: {.back card-id="card-5ab68700993ee9f6"}
For e.g. complete intersections in Fanos, $H^1(X; {\mathbf{T}} {}^{ \vee }X) \cong H^1(X {}^{ \vee }; {\mathbf{T}}X {}^{ \vee })$.

LHS: variations of $\omega_X$ a symplectic form (A-model)

RHS: variations of complex structure (B-model)
:::

::: {.front card-id="card-6b4152564621a373"}
What is EM duality in Maxwell theory?
:::

::: {.back card-id="card-6b4152564621a373"}
Setup: $\nabla$ a connection on a principal ${\operatorname{U}}_1\dash$bundle over $X\in \Mfd^4$.

Equations of motion: $d\star d\nabla = 0$.

Theory invariant under $d\nabla \mapsto \star d\nabla$, exchanges $E_i$ and $B_i$.
:::

::: {.front card-id="card-88579f2dff310206"}
What is Yang-Mills theory?
:::

::: {.back card-id="card-88579f2dff310206"}
Nonabelian gauge theory.

Let $P\to X$ be a principal compact Lie group bundle on a closed Riemannian manifold, with an invariant inner product on its Lie algebra. A connection $A$ has curvature $F_A=dA+A\wedge A$ in a local trivialization.
$$\mathrm{YM}(A)=\int_X|F_A|^2\,d\mathrm{vol},\qquad d_A^*F_A=0.$$
The second formula is the Euler–Lagrange equation; equivalently $d_A*F_A=0$. The Bianchi identity $d_AF_A=0$ holds for every connection. In oriented dimension four, $*F_A=\pm F_A$ implies Yang–Mills by Bianchi.
:::

::: {.front card-id="card-e45dc9a233508299"}
What is AB symmetry on a CY?
:::

::: {.back card-id="card-e45dc9a233508299"}
A: path integral localized on holomorphic maps to $M$, computes GW, depends only on symplectic structure

B: path integral localized on constant maps, deformation theory of $M$, depends only on complex structure
:::

::: {.front card-id="card-8668e3c5ffaa389d"}
What is mirror symmetry for the Hitchin moduli space?
:::

::: {.back card-id="card-8668e3c5ffaa389d"}
SYZ: $\mcm_H(G, C) \rightleftharpoons\mcm_H({}^L G, C)$ are SYZ mirrors

HMS: A-branes on $\mcm_H(G, C)$ is derived equivalent to $\mathbf{D}{\Coh}(\mcm_{\flat}({}^L G, C))$.

GL: $\mathbf{D}{\Coh}(\mcm_{\flat}({}^L G, C))  { \, \xrightarrow{\sim}\, }   {}_\mcd\Mod (\Bun_G(C))$ sending points to Hecke eigensheaves.
:::

::: {.front card-id="card-7285b57d6a08451f"}
Motivate the affine Grassmannian.
:::

::: {.back card-id="card-7285b57d6a08451f"}
Hecke transformations modify a $G\dash$bundle at a point, such modifications are parameterized by $\Gr_G$, transformations from 't Hooft operators $T_\mu$ correspond to Schubert cells $\mu$.
:::

::: {.front card-id="card-bdf64736043c43b5"}
What is geometric Satake?
:::

::: {.back card-id="card-bdf64736043c43b5"}
Equivariant perverse sheaves on $\Gr_G$ is equivalent to $\Rep({}^L G)^\fd$.
:::

::: {.front card-id="card-c4ac7649a95611d6"}
What is the strong force?
:::

::: {.back card-id="card-c4ac7649a95611d6"}
Holds protons and neutrons together in the nucleus of an atom

Holds quarks together in protons/neutrons
:::

::: {.front card-id="card-40e26ae9de203073"}
What is the standard model?
:::

::: {.back card-id="card-40e26ae9de203073"}
Yang Mills for the gauge group $\SU_3 \times \SU_2 \times {\operatorname{U}}_1$.
:::

::: {.front card-id="card-7d9882a64aabff25"}
What is the defining property of a $D\dash$brane?
:::

::: {.back card-id="card-7d9882a64aabff25"}
Dirichlet boundary conditions: surfaces which can occur at the ends of open strings.
:::

::: {.front card-id="card-7ffecd2148901865"}
What is quantization?
:::

::: {.back card-id="card-7ffecd2148901865"}
Replacing Poisson brackets with commutators.
:::

::: {.front card-id="card-e205faa8a99ea77a"}
What is the central charge?
:::

::: {.back card-id="card-e205faa8a99ea77a"}
*(Answer was a figure; image not recovered.)*
:::

::: {.front card-id="card-08bd9b5aba58c5e2"}
What is Faraday's law?
:::

::: {.back card-id="card-08bd9b5aba58c5e2"}
$$\nabla \times\mathbf{E} = -{\frac{\partial }{\partial t}\,} \mathbf{B}$$
:::

::: {.front card-id="card-31fbea10343f7a8e" tags="definition"}
What is the definition of 't hooft operator?
:::

::: {.back card-id="card-31fbea10343f7a8e"}
A line operator in gauge theory defined by a prescribed singularity or monodromy around a loop, labelled by a coweight.
:::

::: {.front card-id="card-6e87f6216988d1ab" tags="definition"}
What is the definition of A-brane?
:::

::: {.back card-id="card-6e87f6216988d1ab"}
An A-model boundary condition supported on a Lagrangian submanifold, together with a flat bundle.
:::

::: {.front card-id="card-2fc755a41f204657" tags="definition"}
What is the definition of A-model?
:::

::: {.back card-id="card-2fc755a41f204657"}
The topological sigma model whose path integral localizes on holomorphic maps and depends only on the symplectic structure.
:::

::: {.front card-id="card-5b2c5c6a1eb3a292" tags="definition"}
What is the definition of Action?
:::

::: {.back card-id="card-5b2c5c6a1eb3a292"}
The functional $S=\int L\,dt$ (or $\int\mathcal{L}\,d^nx$) whose stationary points are classical trajectories.
:::

::: {.front card-id="card-9779983cd9c95af8" tags="definition"}
What is the definition of Adjoint bundle?
:::

::: {.back card-id="card-9779983cd9c95af8"}
For a principal $G$-bundle $P$, $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$; for a vector bundle $E$, $\operatorname{ad}E=\operatorname{End}(E)$.
:::

::: {.front card-id="card-71f374f882a5e646" tags="definition"}
What is the definition of B-model?
:::

::: {.back card-id="card-71f374f882a5e646"}
The topological sigma model localizing on constant maps and depending only on the complex structure.
:::

::: {.front card-id="card-15859a678408b378" tags="definition"}
What is the definition of Canonical bundle?
:::

::: {.back card-id="card-15859a678408b378"}
$K_X=\bigwedge^n T^*X$, the top exterior power of the cotangent bundle; for a curve $C$, $K_C=T^*C$.
:::

::: {.front card-id="card-dcf257317bd1eb28" tags="definition"}
What is the definition of Chern class?
:::

::: {.back card-id="card-dcf257317bd1eb28"}
Characteristic classes $c_k(E)\in H^{2k}(X;\mathbb{Z})$ of a vector bundle; for a line bundle $L$, $c_1(L)$ is the class of the divisor of a rational section.
:::

::: {.front card-id="card-7e3131de44d182e2" tags="definition"}
What is the definition of Covariant derivative?
:::

::: {.back card-id="card-7e3131de44d182e2"}
$d_A=d+A$, the derivative defined by a connection $A$; it acts tensorially on associated bundles.
:::

::: {.front card-id="card-0bf387eecb83fd27" tags="definition"}
What is the definition of D-module?
:::

::: {.back card-id="card-0bf387eecb83fd27"}
A module over the sheaf $\mathcal{D}_X$ of differential operators on $X$.
:::

::: {.front card-id="card-c9a3f09ff7c9b49e" tags="definition"}
What is the definition of Deformation theory?
:::

::: {.back card-id="card-c9a3f09ff7c9b49e"}
The study of families of geometric objects and their infinitesimal deformations, usually controlled by cohomology.
:::

::: {.front card-id="card-44b9d890e2bb3446" tags="definition"}
What is the definition of Degree of a line bundle?
:::

::: {.back card-id="card-44b9d890e2bb3446"}
For a line bundle $L$ on a smooth projective curve $C$, $\deg L=\int_C c_1(L)\in\mathbb{Z}$.
:::

::: {.front card-id="card-5af2e41696aa8876" tags="definition"}
What is the definition of Derived equivalence?
:::

::: {.back card-id="card-5af2e41696aa8876"}
An equivalence between the derived categories $D(\mathcal A)$ and $D(\mathcal B)$ of two abelian categories, or between their differential graded enhancements; equivalently, a quasi-equivalence of the corresponding dg categories.
:::

::: {.front card-id="card-81678f003293771c" tags="definition"}
What is the definition of Dolbeault operator?
:::

::: {.back card-id="card-81678f003293771c"}
$\bar\partial:\Omega^{p,q}(X)\to\Omega^{p,q+1}(X)$, the $(0,1)$-part of the exterior derivative.
:::

::: {.front card-id="card-7db4e967ee343782" tags="definition"}
What is the definition of Dual bundle?
:::

::: {.back card-id="card-7db4e967ee343782"}
For a vector bundle $E$, $E^*=\operatorname{Hom}(E,\mathcal{O}_X)$, the bundle of fiberwise linear functionals.
:::

::: {.front card-id="card-41a40951754e3e4f" tags="definition"}
What is the definition of Equivariant perverse sheaf?
:::

::: {.back card-id="card-41a40951754e3e4f"}
A perverse sheaf equipped with a compatible action of an algebraic group.
:::

::: {.front card-id="card-1e7f1c884bb20e21" tags="definition"}
What is the definition of Essential skeleton?
:::

::: {.back card-id="card-1e7f1c884bb20e21"}
A simplicial subcomplex of the dual complex of a semistable degeneration that captures the essential part of the Berkovich skeleton.
:::

::: {.front card-id="card-63d025d594c74d03" tags="definition"}
What is the definition of Family?
:::

::: {.back card-id="card-63d025d594c74d03"}
A morphism $X\to S$; the fiber $X_s$ is the member over $s\in S$.
:::

::: {.front card-id="card-b39ffee1d62b3366" tags="definition"}
What is the definition of Gauge field?
:::

::: {.back card-id="card-b39ffee1d62b3366"}
A connection on a principal bundle, locally a $\mathfrak{g}$-valued $1$-form $A$; its curvature is the field strength.
:::

::: {.front card-id="card-354cfbbc2e045525" tags="definition"}
What is the definition of Gauge group?
:::

::: {.back card-id="card-354cfbbc2e045525"}
The structure group $G$ of a principal bundle or gauge theory, in which gauge transformations take values.
:::

::: {.front card-id="card-337a8836aa4f87ae" tags="definition"}
What is the definition of Gauge theory?
:::

::: {.back card-id="card-337a8836aa4f87ae"}
A field theory whose dynamical field is a connection on a principal bundle, with gauge transformations as bundle automorphisms.
:::

::: {.front card-id="card-bb6cd09c110aa6a7" tags="definition"}
What is the definition of Genus?
:::

::: {.back card-id="card-bb6cd09c110aa6a7"}
(1) The number of handles of a compact surface; for a Riemann surface $C$, $\dim H^0(C,K_C)$. (2) For a closed connected orientable surface $\Sigma$, the genus $g$ is the number of handles: $\Sigma \cong \#^g T^2$ and $\chi(\Sigma) = 2 - 2g$. For a closed connected nonorientable surface $M$, the nonorientable genus $k$ satisfies $M \cong \#^k \mathbb{RP}^2$ and $\chi(M) = 2 - k$.
:::

::: {.front card-id="card-707a9eb2b4510716" tags="definition"}
What is the definition of Gromov-witten invariant?
:::

::: {.back card-id="card-707a9eb2b4510716"}
$X/\mathbb C$ smooth projective; $\beta\in H_2(X,\mathbb Z)$ effective. For cohomology insertions $\gamma_i$ and integers $a_i\ge0$,
$$\left\langle\prod_{i=1}^n\tau_{a_i}(\gamma_i)\right\rangle^X_{g,\beta}
=\int_{[\overline{\mathcal M}_{g,n}(X,\beta)]^{\mathrm{vir}}}
\prod_{i=1}^n\psi_i^{a_i}\operatorname{ev}_i^*\gamma_i.$$
Here $\operatorname{ev}_i([f:C\to X,p_1,\ldots,p_n])=f(p_i)$ and $\psi_i=c_1(L_i)$, with $(L_i)_{[f,C,p]}=T^*_{p_i}C$. The complex virtual dimension is
$$v=(1-g)(\dim X-3)+\int_\beta c_1(TX)+n.$$
A numerical integral requires $\sum_i(2a_i+\deg_{\mathbb R}\gamma_i)=2v$; incompatible degrees give zero. Primary invariants have all $a_i=0$. The virtual class includes obstruction multiplicities; stack stabilizers can give rational weights. These are not generally literal counts of embedded curves.

Reference: Fulton–Pandharipande, [Notes on stable maps and quantum cohomology](https://arxiv.org/abs/alg-geom/9608011).
:::

::: {.front card-id="card-18f8e402fe607f20" tags="definition"}
What is the definition of Hamiltonian?
:::

::: {.back card-id="card-18f8e402fe607f20"}
The Legendre transform $H(q,p)=p\dot q-L$; it generates time evolution.
:::

::: {.front card-id="card-623807cb6f42af06" tags="definition"}
What is the definition of Hecke eigensheaf?
:::

::: {.back card-id="card-623807cb6f42af06"}
A sheaf or D-module on $\Bun_G$ that is an eigenobject for all Hecke operators.
:::

::: {.front card-id="card-3729ee72b95c0d8d" tags="definition"}
What is the definition of Hecke transformation?
:::

::: {.back card-id="card-3729ee72b95c0d8d"}
The correspondence on $\Bun_G$ that modifies a bundle at a point; it acts on sheaves and D-modules.
:::

::: {.front card-id="card-d437eb9295109467" tags="definition"}
What is the definition of Hitchin moduli space?
:::

::: {.back card-id="card-d437eb9295109467"}
For a smooth projective complex curve $C$, fix rank $r$ and degree $d$. The Higgs moduli space parametrizes S-equivalence classes of semistable $(E,\theta:E\to E\otimes K_C)$; closed points have polystable representatives.
$$h:M_{\mathrm{Higgs}}(r,d)\longrightarrow\bigoplus_{i=1}^rH^0(C,K_C^i),
\qquad \det(t-\theta)=t^r+a_1t^{r-1}+\cdots+a_r.$$
The Hitchin map sends $(E,\theta)$ to $(a_1,\ldots,a_r)$ and is proper. Fixing $\det E=L$ and imposing $\operatorname{tr}\theta=0$ removes the $i=1$ summand. The zero fiber is the nilpotent cone.

For $g(C)\ge2$, the stable $\mathrm{GL}_r$ locus has dimension $2r^2(g-1)+2$; the base has half this dimension. A smooth spectral curve in $\operatorname{Tot}(K_C)$ gives a generic fiber described by line bundles of fixed degree on that curve; fixed determinant gives a norm constraint. The whole moduli space can be singular when strictly semistable objects occur.
:::

::: {.front card-id="card-2615be10eee7932b" tags="definition"}
What is the definition of Hodge star?
:::

::: {.back card-id="card-2615be10eee7932b"}
The isomorphism $*:\Omega^k(M)\to\Omega^{n-k}(M)$ determined by a metric and orientation, with $\alpha\wedge*\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$.
:::

::: {.front card-id="card-9b9825102e0d2e8e" tags="definition"}
What is the definition of Holomorphic vector bundle?
:::

::: {.back card-id="card-9b9825102e0d2e8e"}
A complex vector bundle $E\to X$ over a complex manifold $X$ whose transition functions are holomorphic maps between open subsets of $\mathbb C^r$.
:::

::: {.front card-id="card-679c5e6e299fbac0" tags="definition"}
What is the definition of Irreducible connection?
:::

::: {.back card-id="card-679c5e6e299fbac0"}
A connection whose only parallel subbundles are $0$ and the whole bundle.
:::

::: {.front card-id="card-c71ad1c0cbdf4611" tags="definition"}
What is the definition of Lagrangian?
:::

::: {.back card-id="card-c71ad1c0cbdf4611"}
A function $L(q,\dot q,t)$ whose time integral is the action; in field theory, a Lagrangian density.
:::

::: {.front card-id="card-bdc1aadb29d1f7bf" tags="definition"}
What is the definition of Langlands dual group?
:::

::: {.back card-id="card-bdc1aadb29d1f7bf"}
The complex reductive group ${}^LG$ whose root datum is dual to that of $G$.
:::

::: {.front card-id="card-1bbb90a5c3b42d78" tags="definition"}
What is the definition of Maxwell theory?
:::

::: {.back card-id="card-1bbb90a5c3b42d78"}
The $U(1)$ gauge theory with field strength $F=dA$ and action $-\frac14\int F\wedge *F$.
:::

::: {.front card-id="card-3789a4cc24cc774b" tags="definition"}
What is the definition of Mirror symmetry?
:::

::: {.back card-id="card-3789a4cc24cc774b"}
An equivalence between the A-model on a Calabi-Yau $X$ and the B-model on a mirror Calabi-Yau $X^\circ$.
:::

::: {.front card-id="card-b495461f81808024" tags="definition"}
What is the definition of Moduli space?
:::

::: {.back card-id="card-b495461f81808024"}
A space whose points parametrize isomorphism classes of a given kind of geometric object.
:::

::: {.front card-id="card-d24058c8ef549c5c" tags="definition"}
What is the definition of Moduli stack?
:::

::: {.back card-id="card-d24058c8ef549c5c"}
A stack parametrizing objects together with their automorphisms; for example, $\Bun_G$.
:::

::: {.front card-id="card-e87a9daaa42c5b55" tags="definition"}
What is the definition of Open string?
:::

::: {.back card-id="card-e87a9daaa42c5b55"}
A string whose worldsheet has a boundary, with endpoints constrained to lie on a D-brane.
:::

::: {.front card-id="card-21523e70a090f206" tags="definition"}
What is the definition of Path integral?
:::

::: {.back card-id="card-21523e70a090f206"}
The formal integral $\int\mathcal{D}\phi\,e^{iS[\phi]/\hbar}$ over all field configurations, used to compute quantum amplitudes.
:::

::: {.front card-id="card-0049910abe60c052" tags="definition"}
What is the definition of Poisson bracket?
:::

::: {.back card-id="card-0049910abe60c052"}
On a symplectic manifold, $\{f,g\}=\sum_i(\partial_{q_i}f\,\partial_{p_i}g-\partial_{p_i}f\,\partial_{q_i}g)$; it is a Lie bracket on functions.
:::

::: {.front card-id="card-843c09d0ebcee54b" tags="definition"}
What is the definition of Polarized algebraic family?
:::

::: {.back card-id="card-843c09d0ebcee54b"}
A family $X\to S$ of algebraic varieties equipped with a relatively ample line bundle $L$.
:::

::: {.front card-id="card-99ea41deed4d638a" tags="definition"}
What is the definition of Principal bundle?
:::

::: {.back card-id="card-99ea41deed4d638a"}
A fiber bundle $P\to X$ with a free transitive right action of a group $G$ on each fiber; locally $P\cong G\times U$. Also called a principal $G$-bundle or $G$-bundle.
:::

::: {.front card-id="card-54f72ea67d1d08ed" tags="definition"}
What is the definition of Punctured curve?
:::

::: {.back card-id="card-54f72ea67d1d08ed"}
A curve with finitely many points removed, $C\setminus\{p_1,\dots,p_n\}$; it is noncompact.
:::

::: {.front card-id="card-dcf29d066a252dc2" tags="definition"}
What is the definition of Representation category?
:::

::: {.back card-id="card-dcf29d066a252dc2"}
The category $\mathrm{Rep}(G)$ whose objects are representations of $G$ and whose morphisms are $G$-equivariant linear maps (intertwiners).
:::

::: {.front card-id="card-a0734d7d6091da10" tags="definition"}
What is the definition of Riemann surface?
:::

::: {.back card-id="card-a0734d7d6091da10"}
A connected one-dimensional complex manifold; equivalently, a smooth surface with a complex structure.
:::

::: {.front card-id="card-95726bce0be647ef" tags="definition"}
What is the definition of Schubert cell?
:::

::: {.back card-id="card-95726bce0be647ef"}
The orbit $\mathrm{Gr}_G^\mu$ of a coweight $\mu$ under $G[[t]]$; the affine Grassmannian is their disjoint union.
:::

::: {.front card-id="card-a3094ab97f1c1e56" tags="definition"}
What is the definition of Semistable snc model?
:::

::: {.back card-id="card-a3094ab97f1c1e56"}
A model $\mathcal{X}\to S$ whose special fiber is a divisor with simple normal crossings and whose total space is semistable.
:::

::: {.front card-id="card-a313a6a3647a8a0d" tags="definition"}
What is the definition of Stable bundle?
:::

::: {.back card-id="card-a313a6a3647a8a0d"}
A vector bundle $E$ is stable if every proper subbundle $F$ satisfies $\mu(F)<\mu(E)$, where $\mu(F)=\deg F/\operatorname{rk}F$.
:::

::: {.front card-id="card-fea19a0d73723e60" tags="definition"}
What is the definition of Subgroupoid?
:::

::: {.back card-id="card-fea19a0d73723e60"}
A subcategory $\mathcal H\subseteq\mathcal G$ of a groupoid $\mathcal G$ that is itself a groupoid; equivalently, it contains every identity of its objects and is closed under composition and inverses.
:::

::: {.front card-id="card-8d1077d8a397ee58" tags="definition"}
What is the definition of Symplectic class?
:::

::: {.back card-id="card-8d1077d8a397ee58"}
The de Rham class $[\omega]\in H^2(X;\mathbb{R})$ of a symplectic form $\omega$.
:::
