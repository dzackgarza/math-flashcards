---
title: "Orals::Varieties, Definitions"
---

- For $ V $ a affine variety, what is $ k[V] $? What is $ A(V) $? What is $ k(V) $?

    For $ V\subseteq {\mathbf{A}}^n $, these are polynomial functions $ f\in k[x_1,\cdots, x_n] $ restricted to $ V $, i.e. $ k[V] = k[x_1,\cdots, x_n]\mathrel{\Big|}_V $. This can be written as $ k[V] = k[x_0,\cdots, x_n]/I(V) $, and is sometimes written $ A(V) \coloneqq k[V] $. Then $ k(V) $ are rational such functions.

- What is a **Noetherian** space?

    DCC on closed subsets (not necessarily irreducible)

- What is $ {\mathcal{O}}_X $ for an affine variety?

    The sheaf of regular functions: sections over $ U $ are functions $ \phi: U\to k $ where for every $ p\in U $ there exists an open neighborhood $ U_p\ni p $ and polynomials $ f, g\in k[X] $ with $ { \left.{{\phi(x)}} \right|_{{U_p}} } = {f(x)\over g(x)} $.

- How is $ {\mathcal{O}}_X $ defined for an *affine scheme* $ \operatorname{Spec}A $?

    For $ X = \operatorname{Spec}A $, define $ {\mathcal{O}}(U) $ to be functions $ \phi: U\to \coprod_{p\in U} A_p $ such that $ \phi(p) \in A_p $ for every $ p $ and $ s $ is locally a quotient, i.e. for every $ p $ there is a $ V_p\ni p $ and elements $ f, g\in A $ such that for each $ q\in V_p $, with $ f\not\in q $ and $ \phi(q) = {f\over g} $.

- What are the **Zariski closed** subsets of $ {\mathbb{A}}^n $?

    For $ {\mathbf{A}}^1 $ (and any irreducible curve), the Zariski topology on the closed points is the cofinite topology. For $ {\mathbf{A}}^n $, not cofinite, just take the usual basis $ V(I) $ for $ I{~\trianglelefteq~}k[x_1, \cdots, x_{n}] $.

- Is the Zariski topology on $ {\mathbf{A}}^2 $ the product topology?

    No: $ V(x-y) \subseteq {\mathbf{A}}^2 $ is clearly closed in the Zariski topology but not closed in the product topology. If it were, $ {\mathbf{A}}^2\setminus\Delta $ would be open, so find $ U\times V\subset {\mathbf{A}}^2\setminus\Delta $ an open box. Then $ U,V $ have finite complements since $ {\mathbf{A}}^1 $ has the cofinite topology, $ U = {\mathbf{A}}^1\setminus\left\{{p_i}\right\}_{i\leq n_1} $ and $ V = {\mathbf{A}}^1\setminus\left\{{ q_i }\right\}_{i\leq n_2} $. Pick any $ z\neq p_i, q_i $, then $ (z,z)\in U\times V \cap\Delta $.

- What is a distinguished open set?

    $ D_f \coloneqq X\setminus V(f) $.

- What is an **affine variety**? A **projective variety**?

    Affine: an irreducible closed subset of $ {\mathbf{A}}^n $. Projective: an irreducible algebraic subset of $ {\mathbf{P}}^n $, where $ Y $ is an algebraic subset if $ Y = V(T) $ for $ T $ a collection of homogeneous elements in $ k[x_0,\cdots, x_n] $.

- What is an **irreducible** subset of an affine variety?

    Can't be expressed as the union of proper closed subsets.

- What is a **proper** variety?

    Separated, finite type, universally closed. Can leave out finite type, since all varieties are.

- Give an example of a non-proper variety.

    $ {\mathbf{A}}^n $: separated and finite type over $ k $, but not universally closed: take $ X = {\mathbf{A}}^1, Y= {\mathbf{A}}^1 $, then $ X \underset{\scriptscriptstyle {k} }{\times} Y $ is the projection $ {\mathbf{A}}^2\to {\mathbf{A}}^1 $ onto the coordinate axis, but e.g. $ V(xy-c)\mapsto {\mathbf{G}}_m $ which is not closed.

- What is a complete variety?

    Integral separated scheme of finite type over a field $ k $, where $ X\to \operatorname{Spec}k $ is proper.

- What is a normal affine variety?

    Irreducible and local rings are integrally closed.

- What is a Fano variety?

    A complete variety with ample anticanonical $ -K_X $. Note: always projective.

- What is a del Pezzo surface?

    Fano of dimension 2.

- Give several examples of Fano varieties.

    $ -K_{{\mathbf{P}}^n} = {\mathcal{O}}(n+1) $ which is very ample.

    Any $ D\in \operatorname{Div}({\mathbf{P}}^n) $ when $ \deg D < n+1 $, since adjunction yields

    $$K_D = (K_{{\mathbf{P}}^n} + D)\mathrel{\Big|}_D = \qty{-(n+1)H + \deg(D)\cdot H}\mathrel{\Big|}_D > 0$$

- What is a Calabi-Yau variety?

    $ K_X \sim_{\mathbf{Q}}0 $. Sometimes require $ \omega_X\cong {\mathcal{O}}_X $ instead, with $ h^j({\mathcal{O}}_X) = 0 $ for $ 1\leq j\leq n-1 $.

- Give examples of Calabi-Yau varieties.

    Hypersurfaces $ D $ of $ \deg D = n+1 $, since adjunction yields

    $$K_D = (K_{{\mathbf{P}}^n} + D)\mathrel{\Big|}_D = \qty{-(n+1)H + \deg(D)\cdot H}\mathrel{\Big|}_D = 0H\mathrel{\Big|}_D = 0,$$

    using the Lefschetz hyperplane theorem to show that the $ h^i $ vanish.

- What is the **dimension** of an affine variety?

    Supremum over all $ n $ of lengths of chains $ C_0 \subseteq \cdots C_n $ of irreducible closed subsets.

- What is the **degree** of a variety?

    For $ \dim X = n $, the number of points in $ X $ intersected with $ n $ general hyperplanes.

- What is a **smooth point** of a variety? A **singular point**?

    Jacobian criterion: let $ I(Y) = \left\langle{f_1,\cdots, f_r}\right\rangle {~\trianglelefteq~}k[x_1, \cdots, x_{n}] $ and $ J_Y \coloneqq\left[ {\frac{\partial f_i}{\partial x_j}\,} \right] $ the corresponding Jacobian matrix, then $ Y $ is smooth at $ p $ iff $ \operatorname{rank}J_Y(p) = n-r $ (maximal rank), otherwise if $ \operatorname{rank}J_Y(p) < n-r $ it is a singular point.

    Alternatively, $ \dim {\mathbf{T}}_p X = \dim X $ if smooth and $ \dim {\mathbf{T}}_p X > \dim X $ if singular, where $ {\mathbf{T}}_p X \coloneqq({\mathfrak{m}}_p /{\mathfrak{m}}_p^2) {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}_{  {}_{k}{\mathsf{Mod}}}({\mathfrak{m}}_p/{\mathfrak{m}}_p^2, k) $.

- What is a separated variety?

    Separated iff diagonal is closed iff at $ \leq 1 $ lift exists for the valuative criterion (to exclude double points).

- What is the tautological bundle on $ {\mathbf{P}}^n $?

    $ {\mathcal{O}}_{{\mathbf{P}}^n}(-1) $, the bundle whose fiber above $ p\in {\mathbf{P}}^n $ is the line in $ {\mathbf{A}}^{n+1} $ defined by $ p $.

- What is the **Serre twisting line bundle**?

    The dual of the tautological, $ {\mathcal{O}}(-1) {}^{ \vee }= {\mathcal{O}}(1) $.

- How can you check if $ X = V(I) $ is irreducible?

    Iff $ I $ is prime in $ k[x_1, \cdots, x_{n}] $.

- Why does the exceptional curve $ E $ in $ \operatorname{Bl}_p(X) $ satisfy $ E^2=-1 $?

    Take $ \pi:\operatorname{Bl}_0 {\mathbf{P}}^2\to {\mathbf{P}}^2 $. Take two lines $ L_1, L_2 $ intersecting transversally away from 0 in $ {\mathbf{P}}^2 $, then $ \pi^* L_1.\pi^* L_2 = L_1.L_2 = 1 $ since $ \pi $ is an isomorphism away from zero. Now move them to $ L_1', L_2' $ intersecting at 0; then $ \pi^* L_1' = \tilde L_1' + E $ and $ \pi^* L_2' = \tilde L_2' + E $, and

    $$1 = (\pi^*L_1' . \pi^* L_2') = (\tilde L_1' + E).(\tilde L_2' + E) = \tilde L_1'.\tilde L_2' + \tilde L_1'.E + E.\tilde L_2' + E^2 = 0 + 1 + 1 + E^2 \implies E^2=-1$$

    .

    Use the following theorem:  For $ \pi: \operatorname{Bl}_p X\to X $, let $ C $ be a curve in $ X $, smooth at $ p $. Then the proper transform $ \tilde C $ intersects $ E $ transversely at one point $ q $, and $ \pi^* C = \tilde C + E $. Intersect both sides with $ E $ to get $ \pi^* C . E = (\tilde C + E).E $. The LHS is zero since $ \pi^* A.E = 0 $ for any divisor $ A\in X $. The RHS is $ \tilde C.E + E^2 = q + E^2 $; taking degrees yields $ 0 = 1 + E^2 \implies E^2 = -1 $.

- Why is the normalization a resolution of singularities in dimension 1?

    The normalization is normal, hence regular in codimension 1, hence regular hence smooth.

- What is the canonical class of a blowup?

    For $ \pi: \tilde X\to X $, $ K_{\tilde X} = \pi^* K_X + E $.
