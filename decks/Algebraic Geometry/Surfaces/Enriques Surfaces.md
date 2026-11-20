---
title: "Algebraic Geometry::Surfaces::Enriques Surfaces"
---

::: {.front card-id="enriques-bidouble-six-fibers" tags="construction calculation" cite="[@Sch22, §2.1]"}
Construct an Enriques surface as a bidouble cover of $\operatorname{Bl}_3\mathbb P^2$ using pairs of fibers. Compute its eigensheaves and numerical invariants.
:::

::: {.back card-id="enriques-bidouble-six-fibers"}
Over $\mathbb C$, blow up three noncollinear points. Write $F_i=H-E_i$ for the three rational pencils. Choose two distinct smooth fibers in each pencil, with no triple intersection among the six curves. Set $D_i\sim2F_i$, labeled by the three nonzero elements of $(\mathbb Z/2)^2$.

The character line bundles are
$$L_i=F_j+F_k=2H-E_j-E_k,\qquad
\pi_*\mathcal O_S=\mathcal O_Y\oplus\bigoplus_{i=1}^3\mathcal O_Y(-L_i).$$
Distinct branch labels meet transversely, so $S$ is smooth. Since $\sum D_i\sim-2K_Y$, Hurwitz gives $2K_S\sim0$. Also
$$\chi(\mathcal O_S)=4\chi(\mathcal O_Y)+\frac12\sum_iL_i(L_i+K_Y)
=4+\frac12(-6)=1.$$
Here $K_Y+L_i=-H+E_i$ has no sections, so $p_g(S)=0$ and then $q(S)=0$. Thus $K_S$ is nontrivial two-torsion and $S$ is Enriques.

For a branch fiber $C\in|F_i|$, write $\pi^*C=2R_C$. The connected smooth curve $R_C$ is genus one, and pulling back the pencil gives $|2R_C|$: its branch fibers yield half-fibers. Each exceptional $E_i$ splits into two disjoint $(-2)$-curves upstairs.
:::

::: {.front card-id="enriques-d16-polarization" tags="definition construction" cite="[@Sch22, §2.1]"}
Define $D_{p,q}$ and the geometric conditions on a $D_{1,6}$-polarization of an Enriques surface.
:::

::: {.back card-id="enriques-d16-polarization"}
Let $I_{p,q}=\mathbb Z^{p+q}$ with diagonal form $(1^p,-1^q)$. Its even sublattice is
$$D_{p,q}=\{v\in I_{p,q}:v^2\in2\mathbb Z\}
=\{(v_i):\sum_i v_i\in2\mathbb Z\}.$$
For $I_{1,6}$ use basis $e_0,e_1,\ldots,e_6$ with $e_0^2=1$ and $e_i^2=-1$.

A $D_{1,6}$-polarization includes a primitive embedding into $\operatorname{Pic}(S)$, preserving the intersection pairing, such that $2e_0$ is represented by a nef divisor and
$$e_1\pm e_2,\quad e_3\pm e_4,\quad e_5\pm e_6$$
are represented by six irreducible $(-2)$-curves. They are mutually orthogonal. Thus an abstract embedding without nefness and effective curve representatives is insufficient.

In the bidouble-cover construction, $2e_0$ is the pullback of a line in $\mathbb P^2$, with square four; the six curves are the two lifts of each exceptional curve.
:::

::: {.front card-id="enriques-quotient-dual-complex" tags="construction comparison" cite="[@AEGS25, Proposition 4.8 and §7.3]"}
How do the involution on a Kulikov dual complex and its action on components determine the topology and singularities of an Enriques quotient degeneration?
:::

::: {.back card-id="enriques-quotient-dual-complex"}
Use a regular involution on the model, with an equivariant subdivision when needed.

| K3 dual complex and action | Quotient complex | Component behavior |
| --- | --- | --- |
| Type III: $S^2$, antipodal | $\mathbb{RP}^2$ | Components exchanged in pairs |
| Type III: $S^2$, reflection | Disk | Exchanged pairs off the fixed equator; preserved components on it |
| Type II: interval, reversal | Interval | Components paired, possibly a preserved middle component or double curve |
| Type II: interval, identity | Interval | Every component preserved |

For an exchanged pair, the normalization of its quotient is one of the components. In the AEGS type III reflection models, a preserved component has four isolated fixed points, lying in pairs on two boundary curves; its quotient has four $A_1$ points.

A nontrivial involution of $\mathbb P^1$ is conjugate to $t\mapsto-t$ and has two fixed points. On an elliptic double curve, preserving its one-form gives translation by nonzero two-torsion; negating the form gives $p\mapsto a-p$ with four fixed points. Opposite residues on the two branches determine which action is compatible with a nonsymplectic involution that exchanges, or preserves, the adjacent components.

The quotient complex records incidence, not the gluing isomorphisms or the singularities on each normalized component; retain those separately.
:::

::: {.front card-id="enriques-affine-to-stable-example" tags="application calculation" cite="[@AEGS25, Example 4.14, Corollary 4.9, and §6.5]"}
Recover the stable Enriques limit from the following divisor-model construction: the mirror polygon has successive edge vectors $(2,0),(-1,1),(-1,0),(0,-1)$, with a unit Symington surgery on the diagonal edge. The doubled sphere yields four invariant components with ramification squares $(0,8,4,4)$; the first is ruled, the others are a $D_8$ pair and two $D_4$ pairs. Determine the surviving quotient components and polarization degree.
:::

::: {.back card-id="enriques-affine-to-stable-example"}
Putting the edge vectors end to end gives vertices
$$ (0,0),\ (2,0),\ (1,1),\ (0,1).$$
Perform the unit shear surgery on $(2,0)\!\to\!(1,1)$, then double the resulting affine disk with opposite orientation. In this construction the Enriques and del Pezzo reflections have the same equator. Choose the equivariant triangulation and component gluings giving the stated divisor model.

Each component is preserved, so each component map to the quotient has degree two. With $q^*R_i=\widetilde R_i$:

| Component | $\widetilde R_i^2$ upstairs | $R_i^2$ downstairs | Stable-model map |
| --- | --- | --- | --- |
| Ruled component | $0$ | $0$ | Contracts along its ruling |
| $D_8$ anticanonical pair | $8$ | $4$ | Survives as its index-two folded quotient |
| Each $D_4$ anticanonical pair | $4$ | $2$ | Survives as its index-two folded quotient |

The surviving shapes are $D_8:2={}_2'B_4^-$ and two copies of $D_4:2={}_2'B_2^-$. The global ramification degree is
$$R_Z^2=4+2+2=8,$$
as required for the square of the degree-two numerical polarization. On each surviving component, contract any remaining $R_i$-orthogonal curves and retain the induced conductor gluing.

Square zero alone would not specify the contraction: here the restricted polarization is nontrivial and semiample with one-dimensional image. A numerically trivial restriction would instead contract the component to a point.
:::

::: {.front card-id="enriques-degree-two-projective-model" tags="construction comparison formula" cite="[@AEGS25, Introduction and §§2.1–2.2, with Cossec's classification of Enriques linear systems cited there]"}
For an ADE Enriques surface with an ample numerical polarization of square two, which line bundle defines its quartic del Pezzo model? Distinguish the ordinary and special cases.
:::

::: {.back card-id="enriques-degree-two-projective-model"}
Over $\mathbb C$, let $[L]\in\operatorname{Pic}(Z)/\langle K_Z\rangle$, $L^2=2$. The lifts $L$ and $L\otimes K_Z$ have the same square
$$M=L^{\otimes2},\qquad M^2=8,\qquad h^0(Z,M)=5.$$
The complete system $|M|$ is basepoint-free and gives a degree-two map to a quartic del Pezzo surface $W\subset\mathbb P^4$. Degree check: $8=2\cdot4$.

| Case | Intermediate surface $Y$ in the K3 covering diagram | Singularities of $W$ |
| --- | --- | --- |
| Ordinary | $\mathbb P^1\times\mathbb P^1$ | $4A_1$ |
| Special Heegner locus | $\mathbb P(1,1,2)$ | $A_3+2A_1$ |

The reduced ramification divisor $R_Z\in|M|$ supplies the stable-pair polarization. On a smooth resolution with only big and nef polarization, first contract the orthogonal $(-2)$-curves to obtain the ADE polarized model. Numerical equivalence does not select one of the two lifts $L$, but it does select $M$.
:::

::: {.front card-id="enriques-horikawa-involutions-residue" tags="construction calculation" cite="[@AEGS25, §2.1]"}
Construct a smooth Enriques surface from an invariant $(4,4)$ curve on $\mathbb P^1\times\mathbb P^1$. Identify all three involutions of its K3 covering diagram, their fixed loci, and their actions on the two-form.
:::

::: {.back card-id="enriques-horikawa-involutions-residue"}
Take $Y=\mathbb P^1\times\mathbb P^1$, $\tau(x,y)=(-x,-y)$, and a smooth invariant branch curve $B=(f=0)$ avoiding the four fixed points of $\tau$. The double cover $X$ has local equation $z^2+f(x,y)=0$, with $z$ a fiber coordinate of $\mathcal O_Y(2,2)$.

| Involution | Formula | Action on $\omega$ | Fixed locus |
| --- | --- | --- | --- |
| $d$ | $(x,y,-z)$ | $-1$ | Ramification curve |
| $a$ | $(-x,-y,-z)$ | $-1$ | Empty |
| $b=da$ | $(-x,-y,z)$ | $+1$ | Eight points |

Use the residue $\omega=\operatorname{Res}(dx\wedge dy\wedge dz/(z^2+f))=dx\wedge dy/(2z)$. The product of the coordinate signs gives the character. The equation is invariant under each map. At a fixed point of $\tau$, $f\ne0$, so the two points above it have $z\ne0$: $a$ exchanges them and $b$ fixes them.

Thus $Z=X/a$ is Enriques, $X/b$ has eight $A_1$ singularities and K3 minimal resolution, and $W=Y/\tau=X/\langle d,a\rangle$. The invariant monomials have $i+j$ even. In bidegree $(4,4)$ there are $3^2+2^2=13$ of them; projectivizing and dividing by the two-dimensional connected coordinate torus gives dimension $12-2=10$.
:::

::: {.front card-id="enriques-half-fibers" tags="definition construction example" cite="[@MRS22, §2.2]"}
For a complex Enriques surface $S$, relate primitive nef isotropic classes, half-fibers, and genus-one pencils. Why need the pencil have no section?
:::

::: {.back card-id="enriques-half-fibers"}
$\operatorname{Num}(S)=\operatorname{Pic}(S)/\langle K_S\rangle\simeq U\oplus E_8(-1)$.

- A primitive nef class $f\ne0$ with $f^2=0$ is represented by a half-fiber $F$; $|2F|$ defines a genus-one fibration $S\to\mathbb P^1$.
- Its two multiple fibers are $2F$ and $2F'$, with $F'\sim F+K_S$. Thus $F\equiv F'$ but $F\not\sim F'$.
- “Half” means division of the fiber divisor by two. Over $\mathbb C$, half-fibers are reduced: smooth genus-one curves or multiplicative Kodaira fibers. General reducible fibers must still be read with their Kodaira component multiplicities.
- A section $C$ would satisfy $C\cdot(2F)=1$, impossible since $C\cdot F\in\mathbb Z$. “Genus-one fibration” does not assume a section; the associated Jacobian fibration has one.
:::

::: {.front card-id="enriques-isotropic-sequences-nd" tags="definition comparison formula" cite="[@MRS22, Definitions 2.6–2.11]"}
Define isotropic and non-degenerate isotropic sequences on a complex Enriques surface. Define $\mathrm{nd}(S)$ and distinguish lattice existence from nef realization.
:::

::: {.back card-id="enriques-isotropic-sequences-nd"}
An isotropic sequence consists of primitive isotropic classes $f_1,\ldots,f_n\in\operatorname{Num}(S)$ with
$$f_i\cdot f_j=1-\delta_{ij}.$$
Non-degenerate: every $f_i$ is nef, hence represented by a half-fiber. Then
$$\mathrm{nd}(S)=\max\{n:\text{a non-degenerate isotropic sequence of length }n\text{ exists}\}.$$
The Gram matrix is $J_n-I_n$: eigenvalues $n-1,-1,\ldots,-1$ for $n>1$. The signature $(1,9)$ gives $n\le10$.

The abstract Enriques lattice admits length-ten sequences. On a specified surface, intersections with effective $(-2)$-curves can obstruct nefness. Unnodal surfaces have $\mathrm{nd}(S)=10$; the numerical lattice alone does not determine the non-degeneracy invariant.
:::
