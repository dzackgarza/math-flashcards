---
title: "Number Theory::Lattices and Quadratic Forms"
---

::: {.front card-id="lattice-divisibility-doubled-dual" tags="definition comparison example"}
Distinguish primitivity and divisibility of a vector. Define the doubled dual of a 2-elementary lattice and coeven/coodd.
:::

::: {.back card-id="lattice-divisibility-doubled-dual"}
For a nonzero vector $v$ in a nondegenerate integral lattice $L$:

- Primitive: $L/\mathbb Zv$ torsion-free.
- Divisibility: $(v,L)=\operatorname{div}(v)\mathbb Z$, with $\operatorname{div}(v)>0$.

Example: in $U(2)$ with $e^2=f^2=0$, $(e,f)=2$, $e$ is primitive but $\operatorname{div}(e)=2$.

For $2L^\vee\subset L$, define the **doubled dual**
$$L^\dagger=L^\vee(2),\qquad (x,y)_\dagger=2(x,y).$$
It is integral. Coeven means $L^\dagger$ even; coodd means odd. For even 2-elementary $L$, these correspond to coparity $\delta=0,1$. Thus $U(2)^\dagger\simeq U$ is coeven, while $\langle2\rangle^\dagger\simeq\langle1\rangle$ is coodd.

Reference: Alexeev, *Reflective hyperbolic 2-elementary lattices*, §2.
:::

::: {.front card-id="lattice-coxeter-diagrams" tags="definition comparison example"}
Read a hyperbolic Coxeter diagram using negative-square wall normals. Define elliptic and parabolic subdiagrams.
:::

::: {.back card-id="lattice-coxeter-diagrams"}
Let $L$ have signature $(1,n)$ and take a chamber in one positive-cone component. Choose wall roots $\alpha_i^2<0$ with $(x,\alpha_i)\ge0$ on the chamber.

| Facets | Diagram |
| --- | --- |
| Orthogonal | No edge |
| Angle $\pi/m$ | Edge labeled $m$; omit label $3$ |
| Parallel, meeting at infinity | Bold edge |
| Disjoint in hyperbolic space and at infinity | Dotted/broken edge |

For intersecting facets,
$$\frac{(\alpha_i,\alpha_j)}{\sqrt{\alpha_i^2\alpha_j^2}}=\cos(\pi/m).$$
An elliptic subdiagram has negative-definite Gram form. A connected parabolic subdiagram has negative-semidefinite Gram form with one-dimensional radical and is an affine Dynkin diagram in the crystallographic case. Its null direction gives an ideal boundary direction.

Example: two $(-2)$-roots with pairing $1$ give $A_2$; pairing $2$ gives a parabolic two-wall diagram. Root-length colors and multiplicity arrows need their own stated convention.

Reference: Alexeev, *Reflective hyperbolic 2-elementary lattices*, §2.
:::

::: {.front card-id="lattice-folding-diagram" tags="definition construction example"}
What does folding a root or Coxeter diagram by a symmetry mean geometrically? Compute the $A_3$ involution example.
:::

::: {.back card-id="lattice-folding-diagram"}
Let a finite group $H$ preserve the form and a reflection chamber in $V$. Intersect the chamber with $V^H$. Restrict its wall functionals to $V^H$; a normal is the nonzero projection
$$\overline\alpha=\frac1{|H|}\sum_{h\in H}h\alpha.$$
Remove redundant inequalities and identify proportional normals. The restricted Gram form determines angles and root-length ratios; multiplicities of diagram edges cannot simply be copied.

For negative $A_3$, interchange $\alpha_1,\alpha_3$ and fix $\alpha_2$. Use $\beta=\alpha_1+\alpha_3$, $\gamma=\alpha_2$:
$$\beta^2=-4,\qquad\gamma^2=-2,\qquad(\beta,\gamma)=2.$$
Hence angle $\pi/4$ and a $B_2/C_2$ diagram. The primitive integral normal in the fixed lattice and the averaged rational normal can differ by a scalar.

Reference: Alexeev–Engel–Garza–Schaffler, *Compact moduli of Enriques surfaces of degree 2*, §3.7.
:::

::: {.front card-id="card-a11f16d91f65c85e"}
Discuss Milnor's classification.
:::

::: {.back card-id="card-a11f16d91f65c85e"}
Let $\Lambda$ be an indefinite lattice of signature $(s_+, s_-)$ where $s_+,\, s_- > 0$.

If $\Lambda$ is odd the $\Lambda \cong (1){ {}^{ \scriptscriptstyle\oplus^{n} }  } \oplus (-1){ {}^{ \scriptscriptstyle\oplus^{n} }  }$ where $n>0$.

If $\Lambda$ is even then $\Lambda \cong U{ {}^{ \scriptscriptstyle\oplus^{h} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{k} }  }$ where $h > 0$ and $k\geq 0$.
:::

::: {.front card-id="card-2d755f3e60381c7b"}
What is $L^\perp$?
:::

::: {.back card-id="card-2d755f3e60381c7b"}
$L^\perp \coloneqq\left\{{v\in \Lambda_{\mathrm{K3}}\st{\left\langle {v},~{x} \right\rangle} = 0 \, \forall x\in L}\right\}$.
:::

::: {.front card-id="card-216712199a6ebf7f"}
What is the signature of a lattice?
:::

::: {.back card-id="card-216712199a6ebf7f"}
The signature of the associated bilinear form $\beta$.

Change variables to write $\beta(x) = \sum \lambda_i x_i^2$ where $\lambda_i \in \left\{{0, \pm 1}\right\}$, then the signature is $(n_+, n_-)$, the counts of how many times $+1$ and $-1$ appear respectively.
:::

::: {.front card-id="card-10f6c4add9036d11"}
What is a positive/negative definite form? A nondegenerate form?
:::

::: {.back card-id="card-10f6c4add9036d11"}
Positive: $\lambda_i = +1$ for all $i$.

Negative: $\lambda_i = -1$ for all $i$.

Nondegenerate: $\lambda_i \neq 0$ for all $i$.
:::

::: {.front card-id="card-2bf19339cb018d17"}
What is an integral lattice? What is a common mistake here?
:::

::: {.back card-id="card-2bf19339cb018d17"}
${\left\langle {x},~{y} \right\rangle}\in \ZZ$ for all $x,y\in \Lambda$, i.e. $\operatorname{im}\beta \subseteq \ZZ$.

Equivalently $\Lambda \subseteq \Lambda {}^{ \vee }$.

Common mistake: $\operatorname{im}Q \subseteq \ZZ$ is not sufficient. E.g. $Q(\mathbf{x}) = x_1^2 -x_1 x_2 + x_2^2$ has $Q(\ZZ^2) \subseteq \ZZ$, but $\beta(x, y) = {1\over 2}(Q(x+y) - Q(x) - Q(y))$ has Gram matrix ${ \begin{bmatrix} {1} & {-1/2}  \\ {-1/2} & {1} \end{bmatrix} }$, so $\beta((1,0), (0, 1)) = -1/2\not\in \ZZ$. The integral matrix ${ \begin{bmatrix} {2} & {-1}  \\ {-1} & {2} \end{bmatrix} }$ is the Gram matrix of $2\beta$.
:::

::: {.front card-id="card-f349776d80d82282"}
What is a unimodular lattice?
:::

::: {.back card-id="card-f349776d80d82282"}
Integral and generated by columns of a matrix $M$ with $\operatorname{det}M = \pm 1$.

Volume of fundamental domain is 1.
:::

::: {.front card-id="card-df0de9369c2a65c8"}
Discuss classification of **even**, **unimodular**, **definite** integral lattices
:::

::: {.back card-id="card-df0de9369c2a65c8"}
Only possible in dimensions divisible by 8.

Definite means losing uniqueness, compared to indefinite.

$\dim = 8$: $E_8 = \Gamma_8$.

$\dim = 16$: $E_8{ {}^{ \scriptscriptstyle\oplus^{2} }  }$ and $\Gamma_{16} = D_{16}^+$.

$\dim = 24$: 24 Niemeier lattices $N_i$, including the Leech lattice: uniquely has no roots.

$\dim = 32$: billions.
:::

::: {.front card-id="card-d5f5aa469e5492cc"}
What is an even lattice?
:::

::: {.back card-id="card-d5f5aa469e5492cc"}
${\left\lVert {x} \right\rVert}_L \in 2\ZZ$ for any $x\in L$.
:::

::: {.front card-id="card-0b1de76812224304"}
What are Type I and Type II lattices?
:::

::: {.back card-id="card-0b1de76812224304"}
Usually said of unimodular lattices.

Type II $\iff$ even, e.g. even unimodular.

Type I $\iff$ not even (odd), e.g. odd unimodular.
:::

::: {.front card-id="card-0afaf8bbc4fee730"}
What is the $E_8$ lattice?
:::

::: {.back card-id="card-0afaf8bbc4fee730"}
The unique positive-definite, even, unimodular lattice of rank 8.

Points in ${\mathbf{R}}^8$ whose coordinates are either all integers or all half-integers and the sum of coordinates is even.

Root lattice of $E_8$: with simple roots numbered along the chain $1-3-4-5-6-7-8$ and node $2$ attached to $4$, the positive-definite $E_8$ Gram matrix is
$$\begin{pmatrix}2&0&-1&0&0&0&0&0\\0&2&0&-1&0&0&0&0\\-1&0&2&-1&0&0&0&0\\0&-1&-1&2&-1&0&0&0\\0&0&0&-1&2&-1&0&0\\0&0&0&0&-1&2&-1&0\\0&0&0&0&0&-1&2&-1\\0&0&0&0&0&0&-1&2\end{pmatrix}.$$
:::

::: {.front card-id="card-2849b78e6c806bb4"}
What is a lattice?
:::

::: {.back card-id="card-2849b78e6c806bb4"}
A lattice is a free abelian group with a $\ZZ\dash$valued symmetric bilinear form.

In $V \in {}_{{\mathbf{R}}}\Mod$: $\Lambda \subseteq V$ a discrete cocompact subgroup, i.e. the free $\ZZ\dash$submodule of ${\mathbf{G}}_a(V)$ generated by a basis of $V$. Usually equipped with $\beta: \operatorname{Sym}^2 V\to {\mathbf{R}}$.
:::

::: {.front card-id="card-14330685cdb904e7"}
What is a root in a lattice?
:::

::: {.back card-id="card-14330685cdb904e7"}
A vector $v\in \Lambda$ with $v^2 = -2$.
:::

::: {.front card-id="card-2494d83618adef0b"}
What is the hyperbolic lattice $H$? What is its bilinear form?
:::

::: {.back card-id="card-2494d83618adef0b"}
$H = U = \ZZ e \oplus \ZZ f$ with Gram matrix $\left(\begin{array}{ll}0 & 1 \\1 & 0\end{array}\right)$: bilinear form $\beta(x_1 e + y_1 f, x_2 e + y_2 f) = x_1 y_2 + x_2 y_1$, quadratic form $Q(xe + yf) = xy$.

Hyperbolic module: $H(M) \coloneqq M \oplus M {}^{ \vee }$ with quadratic form $Q(v+v {}^{ \vee }) \coloneqq v {}^{ \vee }(v)$. Yields $Q(\sum x_i e_i + \sum y_i e_i {}^{ \vee }) = \sum x_i y_i$, so for $n=1$ this yields $Q(x e + ye {}^{ \vee }) = xy$, and $H = H(\ZZ)$.
:::

::: {.front card-id="card-11c3a26bca981e84"}
What is the Weyl group $W(\Lambda)$ of a lattice? What is $W^{(2)}(\Lambda)$?
:::

::: {.back card-id="card-11c3a26bca981e84"}
$W(\Lambda) = W^r(\Lambda)\normal{\operatorname{O}}(\Lambda)$ is the subgroup generated by all reflections $s_\alpha(x)=x-2(x,\alpha)\alpha/(\alpha,\alpha)$ that preserve $\Lambda$.

$W^{(2)}(\Lambda)\normal{\operatorname{O}}(\Lambda)$ is generated by reflections in the roots, i.e. $(-2)\dash$vectors $\delta\in\Lambda$ with $\delta^2=-2$; for these, $s_\delta(v)=v+(v,\delta)\delta$.
:::

::: {.front card-id="card-d8c9badde3ed8d51"}
What is the dual of a lattice?
:::

::: {.back card-id="card-d8c9badde3ed8d51"}
$L {}^{ \vee }\coloneqq  {}_{\ZZ}\Mod(L\to \ZZ) \cong \left\{{q\in L_\QQ\st(q, \Lambda) \subseteq \ZZ}\right\}$.
:::

::: {.front card-id="card-efdb8edc0bd7e20a"}
What is $\mathop{\mathrm{len}}\Lambda$?
:::

::: {.back card-id="card-efdb8edc0bd7e20a"}
$\mathop{\mathrm{len}}\Lambda = \ell(D_\Lambda)$, the minimal number of generators of $D_\Lambda$.
:::

::: {.front card-id="card-be95a7f3cdeabdc9"}
What is a $p\dash$elementary lattice?
:::

::: {.back card-id="card-be95a7f3cdeabdc9"}
$D_\Lambda \cong C_p{ {}^{ \scriptscriptstyle\oplus^{k} }  }$ for some $k$; $\implies \mathop{\mathrm{len}}\Lambda = k$.

E.g. a 2-elementary lattice is $\Lambda$ with discriminant group $D_\Lambda\cong C_2^a$ for some $a$.
:::

::: {.front card-id="card-1fbac6a158da1bbe"}
What is a quadratic form on $V\in {}_{R}\Mod$?
:::

::: {.back card-id="card-1fbac6a158da1bbe"}
$Q: V\to R$ where $Q(rx) = r^2 Q(x)$ and $\beta(x,y) \coloneqq Q(x+y) - Q(x) - Q(y)$ defines $\beta:\operatorname{Sym}^2(V)\to R$.

Generalizes the polarization identity
$$2{\left\langle {x},~{y} \right\rangle} = {\left\langle {x+y},~{x+y} \right\rangle} - {\left\langle {x},~{x} \right\rangle} -{\left\langle {y},~{y} \right\rangle}$$
.
:::

::: {.front card-id="card-91b2b56605166572"}
What is the Gram matrix of a bilinear form?
:::

::: {.back card-id="card-91b2b56605166572"}
$M_{ij} = \beta(e_i, e_j)$ where $\left\langle{e_i}\right\rangle_\ZZ= \Lambda$ for a choice of $\ZZ\dash$basis.
:::

::: {.front card-id="card-0302c59509013bff"}
What is the reflection formula for a quadratic module?
:::

::: {.back card-id="card-0302c59509013bff"}
$$\tau_z(x) \coloneqq x - {\beta(x,z) \over Q(x)}\cdot z$$
:::

::: {.front card-id="card-fddde22020cafe92"}
What is Witt's theorem on quadratic modules?
:::

::: {.back card-id="card-fddde22020cafe92"}
If $(V, Q)\in   {}_{R}\Mod$ is a quadratic space, then ${\operatorname{O}}(V) = \left\langle{\tau_z \st z\in V}\right\rangle_R$ and in fact every element is a product of at most $\dim V$ reflections.
:::

::: {.front card-id="card-4abe9b7ef41fa2f1"}
What is a nondegenerate pairing on $\Lambda$?
:::

::: {.back card-id="card-4abe9b7ef41fa2f1"}
The linear extension of $\beta$ to $V = \Lambda\otimes_\ZZ{\mathbf{R}}$ induces an isomorphism $V { \, \xrightarrow{\sim}\, }V {}^{ \vee }$.

Equivalently ${\operatorname{disc}}\Lambda \neq 0$.

For a quadratic module $(V, \beta)$ over a field $k$: $\mathop{\mathrm{Rad}}\beta = 0$.

Equivalently, ${\operatorname{disc}}Q \neq 0$, so ${\operatorname{disc}}Q \in k^{\times}/{ {k^{\times}}_{\scriptscriptstyle \square} }$.

Equivalently, $q_V: V { \, \xrightarrow{\sim}\, }V {}^{ \vee }$ where $q_V(x) \coloneqq\beta(x, {-})$.
:::

::: {.front card-id="card-a9ed496009a79a9e"}
What is ${\operatorname{disc}}(\Lambda)$ for a lattice $(\Lambda, \beta)$?
:::

::: {.back card-id="card-a9ed496009a79a9e"}
${\operatorname{disc}}(\Lambda) \coloneqq\operatorname{det}G(\beta)$ where $G(\beta)$ is the Gram matrix.

Interpret as ${\operatorname{disc}}(\Lambda) = \operatorname{covol}(\Lambda)^2 \coloneqq\operatorname{vol}(V/\Lambda)^2$.

When integral, ${\operatorname{disc}}(\Lambda ) = {\sharp}(\Lambda {}^{ \vee }/\Lambda)$.

Can compute by taking $M$ a generator matrix for $\Lambda$, then ${\operatorname{disc}}\Lambda = M^tM = (\operatorname{det}M)^2$.
:::

::: {.front card-id="card-443490d362df78a6"}
Give a consequence of having a unimodular lattice.
:::

::: {.back card-id="card-443490d362df78a6"}
If $M\leq \Lambda$ is unimodular then there is an isometry $\Lambda  { \, \xrightarrow{\sim}\, }M\oplus M^\perp$.
:::

::: {.front card-id="card-c987fae249683c99"}
What is an overlattice? Give an example.
:::

::: {.back card-id="card-c987fae249683c99"}
$\Lambda$ is an overlattice of $M$ iff $M\leq \Lambda$ is a sublattice and $[\Lambda: M] < \infty$, so $\operatorname{rank}_\ZZ\Lambda = \operatorname{rank}_\ZZ M$.

$\Lambda {}^{ \vee }$ is always an overlattice of $\Lambda$,

$\Lambda$ is always an overlattice of $M\oplus M^\perp$ for any $M\leq \Lambda$.
:::

::: {.front card-id="card-89fe712e79552f01"}
What is an even unimodular lattices?
:::

::: {.back card-id="card-89fe712e79552f01"}
$\Lambda = \Lambda {}^{ \vee }$ and $Q(\Lambda) \subseteq R$, or equivalently $\beta(x,x)\in 2R$ for all $x\in \Lambda$.

Equivalently the Gram matrix is in $\operatorname{GL}_n(\ZZ)$ with even diagonal entries.
:::

::: {.front card-id="card-6be68a12176fe66d"}
Give example computations of Witt groups.
:::

::: {.back card-id="card-6be68a12176fe66d"}
$W(\CC) = C_2$.

$W({\mathbf{R}}) = \ZZ$
:::

::: {.front card-id="card-b35065f6e72d2342"}
What are the rank, signature, and discriminant of $U$?
:::

::: {.back card-id="card-b35065f6e72d2342"}
$\operatorname{rank}U = 2, \operatorname{sgn}U = (1,1), {\operatorname{disc}}U = \operatorname{det}\left(\begin{array}{ll}0 & 1 \\1 & 0\end{array}\right) = -1$, so $U$ is unimodular.
:::

::: {.front card-id="card-0e2ae77c94bce67c"}
What are the rank, signature, and discriminant of $E_8$?
:::

::: {.back card-id="card-0e2ae77c94bce67c"}
$\operatorname{rank}E_8 = 8, \operatorname{sgn}E_8 = (8, 0), {\operatorname{disc}}E_8 = 1$.
:::

::: {.front card-id="card-da297df105afce2a"}
What is the twist $\Lambda(n)$ of a lattice $\Lambda$?
:::

::: {.back card-id="card-da297df105afce2a"}
$\beta_{\Lambda(n)}(x,y) = n\beta_\Lambda(x, y)$.
:::

::: {.front card-id="card-35c314a0c95ae0c8"}
What is the signature of a discriminant form $q_\Lambda$?
:::

::: {.back card-id="card-35c314a0c95ae0c8"}
If $\operatorname{sgn}\Lambda = (\ell_+, \ell_-)$ then $\operatorname{sgn}q_\Lambda = \ell_+ - \ell_-$.
:::

::: {.front card-id="card-ad48a683108ca8b3"}
What is the theta series of an even lattice of dimension $n=2k$ and level $\ell$?
:::

::: {.back card-id="card-ad48a683108ca8b3"}
For $\Lambda$ positive definite,
$$\theta_{\Lambda}(z)=\sum_{x \in \Lambda} q^{\frac{1}{2}\beta(x, x)}, \qquad q = \exp(2\pi i z), \,\,z\in {\mathbb{H}}$$
Coefficients count the number of vectors of a fixed norm: for $\Lambda$ even,
$$\theta_\Lambda(q) = \sum_{m\in \ZZ_{\geq 0}} f_\Lambda(m) q^m,\qquad f_\Lambda(m) \coloneqq{\sharp}\left\{{x\in \Lambda \st\beta(x,x) = 2m}\right\}$$
For $\Lambda$ even of dimension $n = 2k$ and level $\ell$: a modular form of weight $k$ for $\Gamma_0(\ell)$ and a quadratic character $\varepsilon: \Gamma_0(\ell) \to \mu_2$.
:::

::: {.front card-id="card-ebcdecba98093a84"}
What is a primitive sublattice?
:::

::: {.back card-id="card-ebcdecba98093a84"}
$R \leq \Lambda$ a co-torsionfree sublattice, ie $\Lambda/R$ is torsionfree.

Yields a split SES $R\hookrightarrow\Lambda \twoheadrightarrow\Lambda/R$ so $\Lambda \cong R \oplus \Lambda/R$, not necessarily orthogonal wrt $\beta$.

Examples: any $R \leq \Lambda$ of the form $R = S^\perp$ for some $S\leq \Lambda$ is always primitive.
:::

::: {.front card-id="card-a9d006ec7e1731af"}
What is the importance of primitive sublattices?
:::

::: {.back card-id="card-a9d006ec7e1731af"}
If $H\leq\Lambda$ is primitive, it admits a complement as a free abelian group: $\Lambda\simeq H\oplus C$. The complement need not be orthogonal.

If $H$ is also nondegenerate, $H\oplus H^\perp$ has finite index in $\Lambda$, but equality need not hold. In $U=\mathbb Ze+\mathbb Zf$, take $H=\mathbb Z(e+f)$. Then $H^\perp=\mathbb Z(e-f)$ and $[U:H\oplus H^\perp]=2$.
:::

::: {.front card-id="card-7af7ca207863f1de"}
What is a primitive element of a lattice?
:::

::: {.back card-id="card-7af7ca207863f1de"}
$x\in \Lambda$ where $\left\langle{x}\right\rangle_\ZZ$ is a primitive sublattice.

Corresponds to $x$ being the closest element in $\left\langle{x}\right\rangle_\QQ\cap\Lambda$ to the origin.

Equivalently, $v$ is primitive iff ${1\over n} v\not \in \Lambda$ for any $n$.
:::

::: {.front card-id="card-efeef44e832694c6"}
What is a root lattice?
:::

::: {.back card-id="card-efeef44e832694c6"}
A sublattice $\Lambda' \leq \Lambda$ generated by all $-2$ vectors.
:::

::: {.front card-id="card-50aedcf33fbf7e3a"}
What is a lattice isometry?
:::

::: {.back card-id="card-50aedcf33fbf7e3a"}
A map $f: (\Lambda_1, \beta_1) \to (\Lambda_2, \beta_2)$ where $\beta_2(f(x), f(y)) = \beta_1(x,y)$.

Forms a group ${\operatorname{O}}(\Lambda)$.
:::

::: {.front card-id="card-f9d44610f8a0817c"}
Discuss roots in an even unimodular lattice.
:::

::: {.back card-id="card-f9d44610f8a0817c"}
Could generally have $\beta(x,x) = -n$, but even and unimodular forces $n=2$ for every $x$.
:::

::: {.front card-id="card-a4d459cfe34fe98a"}
What is a fundamental domain for $W(\Lambda)$ in $\Lambda_{\mathbf{R}}$?
:::

::: {.back card-id="card-a4d459cfe34fe98a"}
For a hyperbolic lattice, choose a positive-cone component $\mathcal C$ and the roots whose reflections generate $W(\Lambda)$. Take **one connected component**
$$\mathcal C\setminus\bigcup_{\delta\ \mathrm{root}}\delta^\perp.$$
Its closure in $\mathcal C$ is a fundamental chamber. The union runs over roots, not group elements; the whole complement is the union of all chambers. For $W^{(2)}$, use only $(-2)$-roots.
:::

::: {.front card-id="card-8a98615e2a813d40"}
What is the discriminant group? Why care?
:::

::: {.back card-id="card-8a98615e2a813d40"}
$D_\Lambda \coloneqq\Lambda {}^{ \vee }/\Lambda$.

$\Lambda$ not unimodular $\implies D_\Lambda \neq 0$.
:::

::: {.front card-id="card-c790e1446d1f6e1d"}
What is the discriminant form?
:::

::: {.back card-id="card-c790e1446d1f6e1d"}
For an even lattice,
$$\begin{align*}q_\Lambda: D_\Lambda &\to \QQ/2\ZZ\\ x + \Lambda &\mapsto \beta(x,x) +2\ZZ\end{align*}$$
Obtained by extending $\beta$ to $\Lambda {}^{ \vee }$ and then mapping to the quotient.
:::

::: {.front card-id="card-1f456f015eddc365"}
What is the bilinear form associated to the discriminant form $q_\Lambda$?
:::

::: {.back card-id="card-1f456f015eddc365"}
$$\begin{align*}\beta_\Lambda: \operatorname{Sym}^2 D_\Lambda &\to \QQ/\ZZ\\x\otimes y&\mapsto {1\over 2}\qty{ q_{\Lambda}(x+y,x+y) - q_{\Lambda}(x,x)-q_{\Lambda}(y,y)} \\ \\ \implies q_\Lambda(x) &= \beta_\Lambda(x,x)\end{align*}$$
:::

::: {.front card-id="card-69773fd89c4c3104"}
What is an isotropic element of a lattice $V$? An isotropic subspace?
:::

::: {.back card-id="card-69773fd89c4c3104"}
$x\in V$ with $Q(x) = 0$.

Subspaces $U$: $U \subseteq U^\perp \iff{ \left.{{Q}} \right|_{{U}} } = 0$.
:::

::: {.front card-id="card-2208f4041672b913"}
What is the radical of a bilinear form?
:::

::: {.back card-id="card-2208f4041672b913"}
For $(V, \beta)$, set $\mathop{\mathrm{Rad}}V \coloneqq V^\perp \coloneqq\left\{{x\in V \st\beta(x,v) = 0\, \forall v\in V}\right\} = \bigcap_{x\in V}$.
:::

::: {.front card-id="card-93ed2db0f05a22b0"}
What are 2-reflective and reflective lattices?
:::

::: {.back card-id="card-93ed2db0f05a22b0"}
$[{\operatorname{O}}(\Lambda): W_2]<\infty$ and $[{\operatorname{O}}(\Lambda): W_r]<\infty$

Equivalently, the fundamental polyhedra have finite volume.
:::

::: {.front card-id="card-8a6181d000ea1e43"}
What is the coparity invariant $\delta$?
:::

::: {.back card-id="card-8a6181d000ea1e43"}
For $\Lambda$ a 2-elementary lattice, $\delta = 0 \iff q_M(D_\Lambda) \subseteq \ZZ/2\ZZ\subset \QQ/2\ZZ$ and 1 otherwise.
:::

::: {.front card-id="card-d6a1c18965688638"}
What is a hyperbolic lattice?
:::

::: {.back card-id="card-d6a1c18965688638"}
$\operatorname{sgn}\Lambda = (1, m)$ for any $m$.
:::

::: {.front card-id="card-750ea4f9a3313acf"}
When are two lattices in the same genus?
:::

::: {.back card-id="card-750ea4f9a3313acf"}
$\operatorname{sgn}L_1 = \operatorname{sgn}L_2$ and their $p\dash$adic completions $(L_i)_p \coloneqq L_i \otimes_\ZZ{ \ZZ_{\widehat{p}} }$ are isomorphic for all primes as ${ \ZZ_{\widehat{p}} }\dash$bilinear forms, i.e. $L_p \cong M_p$ for all primes $p$ and $\infty$.

Equivalently: equivalence classes under "isometry under all localizations".

For even lattices: same signature and isomorphic discriminant forms. Notation: $g(M)\coloneqq\mathrm{II}_{p,q}(D_M)$.

Genus determines $L_\QQ$ uniquely, and each genus has only finitely many iso classes.
:::

::: {.front card-id="card-b716dfb60f082452"}
What is the index of a lattice?
:::

::: {.back card-id="card-b716dfb60f082452"}
${\mathsf{Ind}}\Lambda = n_+ - n_- \in C_8$.
:::

::: {.front card-id="card-fb3d8ce894f1ebb7"}
What is the exponent of a lattice?
:::

::: {.back card-id="card-fb3d8ce894f1ebb7"}
The exponent of $D_\Lambda$: the minimal $n$ such that $n \Lambda {}^{ \vee }\subseteq \Lambda$.
:::

::: {.front card-id="card-dc5d7d83d1d2b2ce"}
What is the level of a lattice?
:::

::: {.back card-id="card-dc5d7d83d1d2b2ce"}
For even lattices: the smallest $n$ such that $\Lambda {}^{ \vee }(n)$ is again even.

Always have level = $c\cdot \exp\Lambda$ where $c= 1,2$.

The smallest $n$ such that $n\cdot {\left\langle {v},~{v} \right\rangle}\in 2\ZZ$ for all $v\in \Lambda$.
:::

::: {.front card-id="card-aec93e8f59dd792c"}
When are lattice similar?
:::

::: {.back card-id="card-aec93e8f59dd792c"}
$\sigma: \Lambda_1 \to \Lambda_2$ with $\beta_{\Lambda_2}(\sigma v_1, \sigma v_2) = c \beta_{\Lambda_1}(v_1, v_2)$ for some $c$.
:::

::: {.front card-id="card-316531e731be6efa"}
What is a reflective modular form?
:::

::: {.back card-id="card-316531e731be6efa"}
Modular form: $f\in \mathop{\mathrm{Hol}}(\Aff\Omega_{\Lambda}, \CC)$ where $f(tz) = t^{-k}f(z)$ for $t\in \CC^{\times}$ and $f(gz) = \chi(g) f(z)$ for $g\in \Gamma \leq {\operatorname{O}}^+(\Lambda)$ where $\Omega_{\Lambda}\coloneqq\left\{{z\in {\mathbf{P}}(\Lambda\otimes\CC)\st z^2 = 0, {\left\lVert {z} \right\rVert} < 0}\right\}$ and $\Aff$ is its affine cone.

$f$ is reflective iff zeros of $f$ are contained in $\cup\gamma^\perp$ for $\gamma$ roots of $\Lambda$.
:::

::: {.front card-id="card-b28399c98a2e49fd"}
Discuss classification of lattices.
:::

::: {.back card-id="card-b28399c98a2e49fd"}
- Over algebraic number fields: classified by Hasse-Minkowski
- Unimodular, indefinite, integral: classified by Milnor.
- Odd: $\Lambda \cong \left\langle{1}\right\rangle^{n_+} \oplus \left\langle{-1}\right\rangle^{n_-}$.
- Even: Exist $\iff \operatorname{sgn}\Lambda \equiv 0 \operatorname{mod}8$; if indefinite, classified by $\operatorname{sgn}\Lambda$.
- Indefinite, integral: Nikulin, using discriminant forms.
- Even:
- Indefinite, unimodular, nondegenerate: determined by $\operatorname{sgn}\Lambda = (n_+, n_-)$
- (Negative) definite ($n_+ = 0$), unimodular, nondegenerate: Only in ranks $r\equiv 0 \operatorname{mod}8$, not unique for $r\neq 8$.
- Indefinite, $\mathop{\mathrm{len}}\Lambda \leq\operatorname{rank}\Lambda - 2$: determined by $(\operatorname{sgn}\Lambda, q_\Lambda)$.
:::

::: {.front card-id="card-3a514cb7f54c1e95"}
Discuss classification of 2-elementary lattices.
:::

::: {.back card-id="card-3a514cb7f54c1e95"}
Indefinite 2-elementary lattices classified by $(r, a,\delta)$:

Rank, $\ZZ/2\ZZ\dash$rank, and coparity.

Alternatively: $(g,k,\delta)$ where $g= 11 - {r+a\over 2}$ and $k={r-a\over 2}$; $\mathrm{Fix}(\iota)$ has $k+1$ connected components of genera summing to $g$.

Nikulin's classifications: 75 K3 lattices

K3 = hyperbolic, admitting a primitive embedding into $\Lambda_{{\mathsf{K}}3}$.
:::

::: {.front card-id="card-270598bc626a9161"}
What is Nikulin's theorem on lattices?
:::

::: {.back card-id="card-270598bc626a9161"}
For $\Lambda$ even, negative definite, $\operatorname{rank}_\ZZ(\Lambda) \geq \ell(D_\Lambda) + 2$:

$\Lambda$ is determined up to isometry by its rank, signature, and discriminant form.
:::

::: {.front card-id="card-24ce2bd142183187"}
Discuss classification of 2-modular lattices?
:::

::: {.back card-id="card-24ce2bd142183187"}
If 2-modular and indefinite, uniquely determined by rank, signature, $\ell(A_\Lambda)$, and $\Delta$ where $\Delta = 0 \iff q_\Lambda(\Lambda) \subseteq \left\{{0, 1}\right\}$ and 1 otherwise.
:::

::: {.front card-id="card-063aedd8547e505a"}
Give a classification of indefinite unimodular integral lattices.
:::

::: {.back card-id="card-063aedd8547e505a"}
An indefinite unimodular integral lattice of signature $(p,q)$, with $p,q>0$, is determined up to isometry by its signature and parity.

The odd lattice is $I_{p,q}=\langle1\rangle^p\oplus\langle-1\rangle^q$.

An even lattice exists exactly when $p\equiv q\pmod8$. It is
$$\mathrm{II}_{p, q} = U{ {}^{ \scriptscriptstyle\oplus^{p} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{m} }  }, \qquad q-p=8m \geq 0$$
or
$$\mathrm{II}_{p, q} = U{ {}^{ \scriptscriptstyle\oplus^{q} }  }\oplus E_8{ {}^{ \scriptscriptstyle\oplus^{m} }  }, \qquad p-q = 8m \geq 0$$
:::

::: {.front card-id="card-9231b7486b441845"}
Discuss consequences of having a nondegenerate pairing.
:::

::: {.back card-id="card-9231b7486b441845"}
Induces $V { \, \xrightarrow{\sim}\, }V {}^{ \vee }$, so $\Lambda {}^{ \vee }, \Lambda \subset V$ can be identified as lattices in the same space $V\coloneqq\Lambda\otimes_\ZZ{\mathbf{R}}$.

If $\Lambda$ is integral then $\Lambda {}^{ \vee }\supseteq\Lambda$ and $[\Lambda {}^{ \vee }: \Lambda] = {\left\lvert {{\operatorname{disc}}\Lambda} \right\rvert}$.
:::

::: {.front card-id="card-c4d2553683307270"}
Describe ADE dynkin diagrams.
:::

::: {.back card-id="card-c4d2553683307270"}
The simply laced connected finite Dynkin diagrams are $A_n$ (a chain of $n$ nodes), $D_n$ ($n\geq4$, a chain with a fork at one end), and $E_6,E_7,E_8$ (three arms of lengths $1,2,2$, $1,2,3$, and $1,2,4$, measured from the trivalent node). Each edge joins simple roots with Cartan pairing $-1$; each node has diagonal pairing $2$.
:::

::: {.front card-id="card-8543646d4f518a53"}
Discuss the lattice structure on $\operatorname{Pic}(F_4)$
:::

::: {.back card-id="card-8543646d4f518a53"}
Rank 20, Signature $(1, 19)$, Discriminant -64.

Generated by the 48 lines it contains.
:::

::: {.front card-id="card-066dd0227e0fd0e7"}
Describe the Leech lattice.
:::

::: {.back card-id="card-066dd0227e0fd0e7"}
There exists a unique even unimodular lattice **without roots** in $\mathbf{R}^{24}$.

It has 196560 vectors of weight 4.

$\Lambda = \Lambda {}^{ \vee }$ and $\operatorname{det}\Lambda = 1$ so $\Theta_\Lambda(z)$ is a modular form of weight 12.

The unique even unimodular negative definite lattice with no elements of square $-2$ and $\operatorname{Aut}(\Lambda) / \pm 1=$ $C o_1$

Conway's group ${\operatorname{O}}(N)$ the isometries of the Leech lattice, contains the Mathieu group $M_{23}$
:::

::: {.front card-id="card-ddf5b9166ecf9426"}
Discuss Niemeier lattices.
:::

::: {.back card-id="card-ddf5b9166ecf9426"}
Niemeier classifies definite even unimodular lattices of rank 24.

All obtained as primitive sublattices of $\Pi_{1, 25} =U \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{3} }  }$ by specifying a primitive isotropic vector.
:::

::: {.front card-id="card-03d51c1a3802b2e9"}
What are Conway's groups $C_{o_0}$ and $C_{o_1}$?
:::

::: {.back card-id="card-03d51c1a3802b2e9"}
$C_{o_0} = \mathop{\mathrm{Aut}}(\Lambda_{\mathrm{Leech}})$ and $C_{o_1} = {\mathbf{P}}C_{o_0} = C_{o_0}/ \pm \operatorname{id}$ the quotient by the center.

$C_{o_1}$ is Conway's "first sporadic group", known to be simple.
:::

::: {.front card-id="card-fab385d86937463f"}
Why are 8 and 24 special?
:::

::: {.back card-id="card-fab385d86937463f"}
8 is the smallest dimension of an even unimodular lattice, namely $E_8$

24 is the smallest dimension of an even unimodular lattice with no roots (check $\theta$ functions)

$0^2 + 1^2 + \cdot + 24^2 = 70^2$ and this is the only $n$ for which the sum of the first $n$ squares is a square.
:::

::: {.front card-id="card-afea05976ed45fa8"}
What are the generators of $\SL_2(\ZZ)$?
:::

::: {.back card-id="card-afea05976ed45fa8"}
$\operatorname{SL}_2(\mathbb Z)$ is generated by $S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}$ and $T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$. They act on the upper half-plane by $S:z\mapsto-1/z$ and $T:z\mapsto z+1$.
:::

::: {.front card-id="card-c0eec7c8ed8635df"}
What is Rokhlin's theorem?
:::

::: {.back card-id="card-c0eec7c8ed8635df"}
If $X$ is a smooth closed oriented spin four-manifold, the intersection lattice $H^2(X,\mathbb Z)/\mathrm{torsion}$ is even and $\sigma(X)\equiv0\pmod{16}$.

For simply connected $X$, even intersection form is equivalent to $w_2(TX)=0$, hence to existence of a spin structure. This is a criterion for being spin, not a converse asserting that signature divisibility implies spin.

Evenness alone need not imply spin when $\pi_1X\ne1$: a complex Enriques surface has $\pi_1X=C_2$, torsion subgroup $H^2(X,\mathbb Z)_{\mathrm{tors}}\cong\mathbb Z/2$, and free intersection lattice $E_8(-1)\oplus U$. Here $E_8$ is positive definite and $U=\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Its complex orientation gives $\sigma=-8$, so Rokhlin excludes a spin structure.
:::

::: {.front card-id="card-a7450e5dae597a93"}
What are the Eisenstein series $E_4$ and $E_6$?
:::

::: {.back card-id="card-a7450e5dae597a93"}
$$E_4(z)=1+240 \sum_{m=1}^{\infty} \sigma_3(m) q^m \quad \text { and } \quad E_6(z)=1-504 \sum_{m=1}^{\infty} \sigma_5(m) q^m$$
:::

::: {.front card-id="card-5b9d09114ff677aa"}
What is the Eisenstein series $G_k$?
:::

::: {.back card-id="card-5b9d09114ff677aa"}
$$G_k(z)=\sum_{\substack{(m, n) \in \mathbb{Z}^2 \\ (m, n) \neq (0,0)}} \frac{1}{(m z+n)^k}$$
Modular form of weight $k$ for any even $k\geq 4$.
:::

::: {.front card-id="card-8f2112e4f36ebcc7"}
What is the normalized Eisenstein series $E_k$?
:::

::: {.back card-id="card-8f2112e4f36ebcc7"}
$$E_k = \frac{1}{2 \zeta(k)} G_k$$
Explicitly,
$$E_k(z)=1-\frac{2 k}{B_k} \sum_{m=1}^{\infty} \sigma_{k-1}(m) q^m$$
:::

::: {.front card-id="card-36dddf7e357e70c4" tags="definition"}
What is the definition of Bernoulli number?
:::

::: {.back card-id="card-36dddf7e357e70c4"}
The Bernoulli numbers $B_n$ are the rational numbers defined by $\frac{t}{e^t-1}=\sum_{n\ge0}B_n\frac{t^n}{n!}$. With the convention $B_1=-\frac12$, one has $B_0=1$, $B_2=\frac16$, $B_4=-\frac1{30}$, and $B_{2k+1}=0$ for $k\ge1$.
:::

::: {.front card-id="card-5c8305b1d4a8d8b7" tags="definition"}
What is the definition of Cartan matrix?
:::

::: {.back card-id="card-5c8305b1d4a8d8b7"}
For a root system with simple roots $\alpha_1,\dots,\alpha_n$, the Cartan matrix is $C_{ij}=2(\alpha_i,\alpha_j)/(\alpha_j,\alpha_j)$. For a simply laced root system (type ADE), $C_{ii}=2$ and $C_{ij}\in\{0,-1\}$ for $i\ne j$.
:::

::: {.front card-id="card-0d8eed2df9802c4b" tags="definition"}
What is the definition of Co-torsionfree?
:::

::: {.back card-id="card-0d8eed2df9802c4b"}
A submodule $R\subseteq\Lambda$ is co-torsionfree if the quotient $\Lambda/R$ is torsionfree. For a lattice, this is equivalent to $R$ being a primitive sublattice; then the exact sequence $0\to R\to\Lambda\to\Lambda/R\to0$ splits.
:::

::: {.front card-id="card-4d1a0ca83d5dd848" tags="definition"}
What is the definition of Congruence subgroup?
:::

::: {.back card-id="card-4d1a0ca83d5dd848"}
A congruence subgroup of $\mathrm{SL}_2(\mathbb{Z})$ is a subgroup containing a principal congruence subgroup $\Gamma(N)=\{\gamma\in\mathrm{SL}_2(\mathbb{Z}):\gamma\equiv I\pmod N\}$ for some $N\ge1$. The standard examples are $\Gamma_0(N)=\{\gamma:c\equiv0\pmod N\}$ and $\Gamma_1(N)=\{\gamma:c\equiv0,\ a\equiv d\equiv1\pmod N\}$.
:::

::: {.front card-id="card-12b87e834fc03b9a" tags="definition"}
What is the definition of Covolume?
:::

::: {.back card-id="card-12b87e834fc03b9a"}
For a lattice $\Lambda\subseteq V$ in a Euclidean vector space $V$ of dimension $n$, the covolume is $\operatorname{covol}(\Lambda)=\operatorname{vol}(V/\Lambda)$, the volume of a fundamental parallelepiped. If $G$ is the Gram matrix of a basis, then $\operatorname{covol}(\Lambda)=\sqrt{\det G}$, and $\operatorname{disc}(\Lambda)=\operatorname{covol}(\Lambda)^2$.
:::

::: {.front card-id="card-567ff60f7069fe31" tags="definition"}
What is the definition of Discriminant of a quadratic form?
:::

::: {.back card-id="card-567ff60f7069fe31"}
For a quadratic form $Q$ on a free $R$-module with Gram matrix $G=(\beta(e_i,e_j))$, where $\beta(x,y)=Q(x+y)-Q(x)-Q(y)$, the discriminant is $\operatorname{disc}(Q)=\det G$ (well defined up to the square of a unit after a change of basis). For a lattice $(\Lambda,\beta)$ this is $\operatorname{disc}(\Lambda)=\det G(\beta)=\operatorname{covol}(\Lambda)^2$.
:::

::: {.front card-id="card-2742f470f313b98b" tags="definition"}
What is the definition of Hasse-minkowski theorem?
:::

::: {.back card-id="card-2742f470f313b98b"}
The Hasse-Minkowski theorem states that a quadratic form over a number field $K$ represents zero nontrivially iff it does so over every completion $K_v$ of $K$ (including the real and $p$-adic completions). Equivalently, two quadratic forms over $K$ are isometric iff they are isometric over every $K_v$.
:::

::: {.front card-id="card-739234bef229f4e3" tags="definition"}
What is the definition of Hyperbolic module?
:::

::: {.back card-id="card-739234bef229f4e3"}
For a projective module $M$ over a ring $R$, the hyperbolic module is $H(M)=M\oplus M^\vee$ with quadratic form $Q(v+f)=f(v)$ for $v\in M$, $f\in M^\vee$. For $M=R=\mathbb{Z}$, $H(\mathbb{Z})$ is the hyperbolic lattice $U$ with Gram matrix $\begin{pmatrix}0&1\\1&0\end{pmatrix}$.
:::

::: {.front card-id="card-5140259e944d96d7" tags="definition"}
What is the definition of K3 lattice?
:::

::: {.back card-id="card-5140259e944d96d7"}
The K3 lattice is the unique even unimodular lattice of rank $22$ and signature $(3,19)$, isometric to $U^3\oplus E_8(-1)^2$. It is the lattice $H^2(X,\mathbb{Z})$ with the intersection form for a K3 surface $X$.
:::

::: {.front card-id="card-1355b31873688595" tags="definition"}
What is the definition of Level of a modular form?
:::

::: {.back card-id="card-1355b31873688595"}
The level of a modular form is the smallest positive integer $N$ such that $f$ is modular for the congruence subgroup $\Gamma_0(N)$ (or $\Gamma_1(N)$). Equivalently, it is the level of the congruence subgroup in its modular transformation law.
:::

::: {.front card-id="card-cc5ef3faa8521def" tags="definition"}
What is the definition of Modular form?
:::

::: {.back card-id="card-cc5ef3faa8521def"}
A modular form of weight $k$ for a congruence subgroup $\Gamma\subseteq\mathrm{SL}_2(\mathbb{Z})$ is a holomorphic function $f:\mathbb{H}\to\mathbb{C}$ such that $f(\gamma z)=(cz+d)^k f(z)$ for all $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma$ and $f$ is holomorphic at the cusps. If $f$ vanishes at the cusps, it is a cusp form.
:::

::: {.front card-id="card-190de4f7cb5045c4" tags="definition"}
What is the definition of Odd lattice?
:::

::: {.back card-id="card-190de4f7cb5045c4"}
A lattice is odd if it is not even, i.e. if there exists $x\in\Lambda$ with $\beta(x,x)\notin2\mathbb{Z}$ (for an integral lattice). Equivalently, its quadratic form takes an odd value.
:::

::: {.front card-id="card-06adb8f96341c22e" tags="definition"}
What is the definition of P-adic completion?
:::

::: {.back card-id="card-06adb8f96341c22e"}
For a lattice or abelian group $L$, its $p$-adic completion is $L_p=L\otimes_{\mathbb{Z}}\mathbb{Z}_p$, where $\mathbb{Z}_p=\varprojlim_n\mathbb{Z}/p^n\mathbb{Z}$. For a lattice $L\cong\mathbb{Z}^n$, $L_p\cong\mathbb{Z}_p^n$ is a $\mathbb{Z}_p$-lattice.
:::

::: {.front card-id="card-ea6aade100c08fae" tags="definition"}
What is the definition of Quadratic character?
:::

::: {.back card-id="card-ea6aade100c08fae"}
A quadratic character is a homomorphism $\chi:(\mathbb{Z}/N\mathbb{Z})^\times\to\{\pm1\}$ (equivalently a real Dirichlet character with $\chi^2=1$). The quadratic character associated to a fundamental discriminant $D$ is the Kronecker character $\chi_D(n)=(D/n)$.
:::

::: {.front card-id="card-ebc4fe716c6f2807" tags="definition"}
What is the definition of Quadratic space?
:::

::: {.back card-id="card-ebc4fe716c6f2807"}
A quadratic space is a pair $(V,Q)$ consisting of a vector space $V$ over a field or ring $R$ and a quadratic form $Q:V\to R$. The associated bilinear form is $\beta(x,y)=Q(x+y)-Q(x)-Q(y)$.
:::

::: {.front card-id="card-1a0092ebb18709ca" tags="definition"}
What is the definition of Simple root?
:::

::: {.back card-id="card-1a0092ebb18709ca"}
Let $\Phi$ be a root system with a choice of positive roots $\Phi^+$. A root $\alpha\in\Phi^+$ is simple if it cannot be written as a sum of two positive roots. The simple roots form a basis of the root lattice, and their Cartan matrix encodes the root system.
:::

::: {.front card-id="card-93f96f2cebb7bcee" tags="definition"}
What is the definition of Spin manifold?
:::

::: {.back card-id="card-93f96f2cebb7bcee"}
A spin manifold is an oriented Riemannian manifold whose second Stiefel-Whitney class vanishes, $w_2(M)=0$, together with a choice of spin structure. Equivalently, the oriented orthonormal frame bundle lifts to a principal $\mathrm{Spin}(n)$-bundle.
:::

::: {.front card-id="card-21e08ae6b126b692" tags="definition"}
What is the definition of Spin structure?
:::

::: {.back card-id="card-21e08ae6b126b692"}
A spin structure on an oriented Riemannian manifold $M$ is a principal $\mathrm{Spin}(n)$-bundle $\widetilde{P}\to M$ with a two-sheeted covering $\widetilde{P}\to P_{\mathrm{SO}}(M)$ that restricts to the spin covering $\mathrm{Spin}(n)\to\mathrm{SO}(n)$ on fibers. It exists iff $w_2(M)=0$.
:::

::: {.front card-id="card-5935a4320dc00f9a" tags="definition"}
What is the definition of Sporadic group?
:::

::: {.back card-id="card-5935a4320dc00f9a"}
A sporadic group is one of the $26$ finite simple groups that are neither cyclic of prime order, alternating, nor of Lie type. Examples include the Mathieu groups $M_{11},M_{12},M_{22},M_{23},M_{24}$ and the Conway groups $Co_1,Co_2,Co_3$.
:::

::: {.front card-id="card-8cb1b6dc92ecd709" tags="definition"}
What is the definition of Theta function?
:::

::: {.back card-id="card-8cb1b6dc92ecd709"}
A theta function is a holomorphic function on the upper half-plane with a transformation law under a lattice or congruence subgroup, typically a sum $\theta(z)=\sum_{n\in\mathbb{Z}}q^{n^2/2}$ with $q=e^{2\pi iz}$. The theta series of a lattice is the theta function whose coefficients count vectors of a given norm.
:::

::: {.front card-id="card-463a836d19e8f22e" tags="definition"}
What is the definition of Weight of a modular form?
:::

::: {.back card-id="card-463a836d19e8f22e"}
A modular form $f$ of weight $k$ for a congruence subgroup $\Gamma\subseteq\mathrm{SL}_2(\mathbb{Z})$ satisfies $f(\gamma z)=(cz+d)^k f(z)$ for all $\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\Gamma$, with $f$ holomorphic on the upper half-plane and at the cusps. The integer $k$ is the weight.
:::
