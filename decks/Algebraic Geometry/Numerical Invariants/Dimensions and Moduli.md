---
title: "Algebraic Geometry::Numerical Invariants::Dimensions and Moduli"
---

::: {.front card-id="application-moduli-complete-intersection-counts" tags="application"}
Compute the dimensions up to projective equivalence of smooth $(2,2)$ surfaces in $\mathbb P^4$ and smooth $(2,3)$ K3 surfaces in $\mathbb P^4$. Which redundancies in their defining equations must be removed?
:::

::: {.back card-id="application-moduli-complete-intersection-counts"}
Quadrics in $\mathbb P^4$ form a vector space of dimension $15$. A $(2,2)$ ideal is determined by its two-dimensional space of quadrics, so its parameter space is open in $\operatorname{Gr}(2,15)$ of dimension $26$. Subtracting $\dim\operatorname{PGL}_5=24$ gives moduli dimension $2$.

For a $(2,3)$ surface, choose the quadric in a projective space of dimension $14$. Cubics have vector-space dimension $35$, but adding any of the five linear multiples of the quadric leaves the ideal unchanged. The cubic therefore contributes $35-5-1=29$ parameters. The result is $14+29-24=19$. Smooth members have finite projective stabilizers, so these subtractions apply.
:::

::: {.front card-id="application-moduli-stabilizer-quadric" tags="application"}
Why does subtracting $\dim\operatorname{PGL}_4$ from the parameter-space dimension of quadric surfaces give the wrong moduli dimension? Compare smooth cubic surfaces.
:::

::: {.back card-id="application-moduli-stabilizer-quadric"}
Quadrics have projective parameter-space dimension $9$, while $\operatorname{PGL}_4$ has dimension $15$. A smooth quadric has projective stabilizer of dimension $6$, coming from $\operatorname{PGL}_2\times\operatorname{PGL}_2$ (and a discrete factor interchanging rulings). Thus the orbit has dimension $15-6=9$, and the moduli dimension is zero.

Cubic surfaces have projective parameter-space dimension $19$ and finite stabilizer, giving dimension $19-15=4$. The orbit dimension, not the group dimension alone, is what must be subtracted.
:::

::: {.front card-id="numerical-general-position-versus-interpolation" tags="definition application"}
Define linear general position for distinct points in $\mathbb P^n$. Does it imply independence of their conditions on forms of every degree? Give a plane counterexample and the correct test for interpolation.
:::

::: {.back card-id="numerical-general-position-versus-interpolation"}
For the point set $Z$, every subset $I\subseteq Z$ with $|I|\le n+1$ must be linearly independent; equivalently, $|Z\cap\Lambda|\le r+1$ for every $r$-plane $\Lambda\subset\mathbb P^n$ with $r<n$. In $\mathbb P^2$ this means no three are collinear.

Six distinct points on a smooth conic satisfy linear general position, but their conditions on conics are dependent: there is a nonzero conic through all six. For a reduced finite set $Z$, independence in degree $d$ means the evaluation map
$$H^0(\mathbb P^n,\mathcal O(d))\longrightarrow H^0(Z,\mathcal O_Z(d))$$
is surjective, equivalently $H^1(\mathcal I_Z(d))=0$ for $d\ge0$. “General position” must name the incidence or interpolation condition needed.
:::

::: {.front card-id="numerical-point-configurations-moduli" tags="application"}
For $r\ge4$ ordered general points of $\mathbb P^2_{\mathbb C}$, compute the dimension of their configurations up to projective equivalence. How does this recover familiar del Pezzo moduli dimensions?
:::

::: {.back card-id="numerical-point-configurations-moduli"}
A general ordered quadruple with no three collinear is a projective frame, so its stabilizer is trivial. The configuration space has dimension $2r$ and $\operatorname{PGL}_3$ has dimension $8$, giving $2r-8$.

| Points blown up | 4 | 5 | 6 | 7 | 8 |
| --- | --- | --- | --- | --- | --- |
| Del Pezzo degree | 5 | 4 | 3 | 2 | 1 |
| Moduli dimension | 0 | 2 | 4 | 6 | 8 |

Restricting to the del Pezzo general-position locus does not change dimension. Forgetting the ordering and blowdown marking makes only a finite identification.
:::

::: {.front card-id="card-a3226206edbadebd"}
What are the dimensions of moduli of all and just algebraic Kummer surfaces?
:::

::: {.back card-id="card-a3226206edbadebd"}
All: 4-dimensional

Algebraic: 3-dimensional.
:::

::: {.front card-id="card-4bf015e09e65996f"}
What is the dimension of quartics in ${\mathbf{P}}^3$? Up to coordinate changes?
:::

::: {.back card-id="card-4bf015e09e65996f"}
$h^0({\mathcal{O}}_{{\mathbf{P}}^3}(4)) = {4+3\choose 4} = 35$ and its projective dimension is 34.

$\dim \operatorname{PGL}_4(\CC) = 16-1 = 15$

So $34-15 = 19$ moduli.
:::

::: {.front card-id="card-feb6d5dd0d9fef49"}
What are the dimensions of moduli for $S_{2,3}, S_{2,2,2}$, and the double plane $S\to {\mathbf{P}}^2$?
:::

::: {.back card-id="card-feb6d5dd0d9fef49"}
All 19.
:::

::: {.front card-id="card-b5a57050c6bdb637" cite="[@GS07, §5]"}
Compute the dimension of moduli of K3s with an order 3 symplectic automorphism.
:::

::: {.back card-id="card-b5a57050c6bdb637"}
For algebraic complex K3 surfaces, the dimension is $7$. An order-three symplectic automorphism has six fixed points. The Lefschetz formula gives $6=2+\operatorname{tr}(\sigma^*|H^2)$; with eigenvalue multiplicities $a$ for $1$ and $b$ for each primitive cube root, $a-b=4$ and $a+2b=22$. Thus $a=10$, $b=6$, and the coinvariant lattice has rank $12$ in $\operatorname{NS}(X)$. An invariant ample class raises the generic Picard rank to $13$, leaving $20-13=7$ moduli. Families attain this bound.
:::

::: {.front card-id="formula-k3-stable-sheaf-tangent" tags="formula"}
For an $H$-stable coherent sheaf $E$ on a complex projective K3 surface, compute $\dim\operatorname{Ext}^1(E,E)$ from its Mukai vector.
:::

::: {.back card-id="formula-k3-stable-sheaf-tangent"}
$$\dim\operatorname{Ext}^1(E,E)=\langle v(E),v(E)\rangle+2.$$
:::

::: {.front card-id="formula-k3-sheaf-moduli-dimension" tags="formula"}
For a nonempty moduli space $M_H(v)$ of stable sheaves on a complex projective K3 surface, with primitive Mukai vector $v$ and $v$-generic polarization $H$, compute its dimension.
:::

::: {.back card-id="formula-k3-sheaf-moduli-dimension"}
$$\dim M_H(v)=\langle v,v\rangle+2.$$
:::

::: {.front card-id="card-8ac3fbe77305abd9"}
What is the dimension of moduli of Enriques surfaces?
:::

::: {.back card-id="card-8ac3fbe77305abd9"}
10-dimensional.
:::

::: {.front card-id="formula-surface-hilbert-points-dimension" tags="theorem"}
For a smooth connected complex quasi-projective surface $S$, state Fogarty's theorem about $\operatorname{Hilb}^n(S)$ and the Hilbert–Chow morphism.
:::

::: {.back card-id="formula-surface-hilbert-points-dimension"}
The scheme $\operatorname{Hilb}^n(S)$ is smooth and irreducible of dimension $2n$. The Hilbert–Chow morphism
$$\operatorname{Hilb}^n(S)\longrightarrow\operatorname{Sym}^n(S)$$
is a resolution of singularities.
:::

::: {.front card-id="formula-severi-dimension" tags="formula"}
For the nonempty Severi variety $V_{d,\delta}$ of integral degree-$d$ plane curves over $\mathbb C$ with exactly $\delta$ nodes and geometric genus $g$, compute $\delta$ and $\dim V_{d,\delta}$.
:::

::: {.back card-id="formula-severi-dimension"}
$$\delta=\frac{(d-1)(d-2)}2-g,\qquad \dim V_{d,\delta}=\binom{d+2}{2}-1-\delta.$$
:::

::: {.front card-id="formula-jacobian-tangent" tags="formula"}
For $X=V(f_1,\ldots,f_r)\subset\mathbb A^n_{\mathbb C}$ and $p\in X$, compute the tangent-space dimension from the Jacobian $J(p)$.
:::

::: {.back card-id="formula-jacobian-tangent"}
$$\dim_{\mathbb C}T_pX=n-\operatorname{rank}J(p).$$
:::

::: {.front card-id="formula-stable-map-virtual-dimension" tags="formula"}
For a smooth projective complex $m$-fold $X$, compute the virtual dimension of $\overline M_{g,n}(X,\beta)$.
:::

::: {.back card-id="formula-stable-map-virtual-dimension"}
$$\operatorname{vdim}\overline M_{g,n}(X,\beta)=(1-g)(m-3)-K_X\beta+n.$$
:::

::: {.front card-id="numerical-grassmannian-dimension" tags="formula"}
For $0\le k\le n$, what is $\dim\operatorname{Gr}(k,n)$, where points are $k$-dimensional vector subspaces?
:::

::: {.back card-id="numerical-grassmannian-dimension"}
$$\dim\operatorname{Gr}(k,n)=k(n-k).$$
A standard affine chart is the space of $k\times(n-k)$ matrices. Thus projective $r$-planes in $\mathbb P^n$ form a family of dimension $(r+1)(n-r)$.
:::

::: {.front card-id="numerical-linear-groups" tags="formula"}
Over $\mathbb C$, compute the dimensions of $\operatorname{GL}_n,\operatorname{SL}_n,\operatorname{PGL}_n$ and $\operatorname{Aut}(\mathbb P^n)$.
:::

::: {.back card-id="numerical-linear-groups"}
$$\dim\operatorname{GL}_n=n^2,\qquad \dim\operatorname{SL}_n=\dim\operatorname{PGL}_n=n^2-1,\qquad \dim\operatorname{Aut}(\mathbb P^n)=(n+1)^2-1.$$
:::

::: {.front card-id="numerical-hypersurface-parameters" tags="formula"}
For $n\ge1,d\ge1$, what is the dimension of the parameter space of degree-$d$ hypersurfaces in $\mathbb P^n$?
:::

::: {.back card-id="numerical-hypersurface-parameters"}
$$\dim\mathbb P H^0(\mathbb P^n,\mathcal O(d))=\binom{n+d}{n}-1.$$
Nonzero equations differing by a scalar define the same hypersurface.
:::

::: {.front card-id="numerical-orbit-stabilizer" tags="formula"}
An algebraic group $G$ acts on an irreducible variety $X$ over $\mathbb C$, with generic stabilizer dimension $s$. What is the generic orbit dimension and the dimension of a rational quotient?
:::

::: {.back card-id="numerical-orbit-stabilizer"}
$$\dim(Gx)=\dim G-s,\qquad \dim(X/G)=\dim X-\dim G+s.$$
The quotient formula applies on a dense open set admitting a geometric quotient.
:::

::: {.front card-id="numerical-hypersurface-moduli" tags="formula"}
For smooth degree-$d$ hypersurfaces in $\mathbb P^n_{\mathbb C}$ with finite projective stabilizer, what is the dimension of their moduli up to projective equivalence?
:::

::: {.back card-id="numerical-hypersurface-moduli"}
$$\binom{n+d}{n}-(n+1)^2.$$
Subtract the dimension of $\operatorname{PGL}_{n+1}$ from the projective parameter space. Positive-dimensional stabilizers require a correction.
:::

::: {.front card-id="numerical-point-conditions" tags="formula"}
How many independent linear conditions does vanishing to order at least $m$ at a fixed point impose on degree-$d$ hypersurfaces in $\mathbb P^n$, when $d\ge m-1$?
:::

::: {.back card-id="numerical-point-conditions"}
$$\binom{n+m-1}{n}.$$
These are the coefficients of local monomials of total degree less than $m$. Conditions at several points need not be independent.
:::

::: {.front card-id="numerical-pointed-curves" tags="formula"}
For $2g-2+n>0$, what is the dimension of the moduli stack $\mathcal M_{g,n}$ of smooth pointed complex curves?
:::

::: {.back card-id="numerical-pointed-curves"}
$$\dim\mathcal M_{g,n}=3g-3+n.$$
In particular, $\dim\mathcal M_g=3g-3$ for $g\ge2$, $\dim\mathcal M_{1,1}=1$, and $\dim\mathcal M_{0,n}=n-3$ for $n\ge3$.
:::

::: {.front card-id="numerical-hyperelliptic-locus" tags="formula"}
For $g\ge2$, compute the dimension of the hyperelliptic locus $\mathcal H_g\subset\mathcal M_g$ over $\mathbb C$ and its codimension.
:::

::: {.back card-id="numerical-hyperelliptic-locus"}
$$\dim\mathcal H_g=2g-1,\qquad \operatorname{codim}_{\mathcal M_g}\mathcal H_g=g-2.$$
The branch divisor has $2g+2$ distinct unordered points on $\mathbb P^1$; quotienting by $\operatorname{PGL}_2$ subtracts three parameters.
:::

::: {.front card-id="numerical-abelian-moduli" tags="formula"}
What is the dimension of the moduli space $\mathcal A_g$ of principally polarized complex abelian varieties?
:::

::: {.back card-id="numerical-abelian-moduli"}
$$\dim\mathcal A_g=\frac{g(g+1)}2.$$
Siegel upper half-space is open in the space of symmetric complex $g\times g$ matrices.
:::

::: {.front card-id="numerical-jacobian-dimension" tags="formula"}
For a smooth connected projective curve $C$ of genus $g$, compute $\dim\operatorname{Pic}^d(C)$ and $\dim|L|$ for a line bundle $L$ with a nonzero section.
:::

::: {.back card-id="numerical-jacobian-dimension"}
$$\dim\operatorname{Pic}^d(C)=g,\qquad \dim|L|=h^0(C,L)-1.$$
:::

::: {.front card-id="numerical-determinantal-dimension" tags="formula"}
In the space of $m\times n$ matrices, what are the dimension and codimension of the locus of rank at most $r$, for $0\le r\le\min(m,n)$?
:::

::: {.back card-id="numerical-determinantal-dimension"}
$$\dim D_r=r(m+n-r),\qquad \operatorname{codim}D_r=(m-r)(n-r).$$
:::

::: {.front card-id="numerical-flags" tags="formula"}
What is the dimension of the complete flag variety of an $n$-dimensional vector space?
:::

::: {.back card-id="numerical-flags"}
$$\dim\operatorname{Fl}(n)=\frac{n(n-1)}2.$$
:::

::: {.front card-id="numerical-lines-hypersurface" tags="formula"}
What is the expected dimension of the scheme of lines on a degree-$d$ hypersurface in $\mathbb P^n$?
:::

::: {.back card-id="numerical-lines-hypersurface"}
$$2(n-1)-(d+1)=2n-d-3.$$
Lines form $\operatorname{Gr}(2,n+1)$; restricting the equation to a line gives $d+1$ coefficients. The expected dimension alone does not prove nonemptiness or smoothness.
:::

::: {.front card-id="numerical-plane-curve-moduli" tags="formula"}
For $d\ge4$, compute the dimension of smooth plane curves of degree $d$ up to projective equivalence. Specialize to quartics.
:::

::: {.back card-id="numerical-plane-curve-moduli"}
$$\binom{d+2}{2}-9.$$
For quartics this is $6$, equal to $\dim\mathcal M_3$; nonhyperelliptic genus-three curves have canonical plane-quartic models.
:::

