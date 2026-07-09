---
title: "Research::K3s"
---

- Discuss the number of fixed points of a symplectic automorphism with finite order $ n $.

    Computed by Mukai using the Lefschetz fixed point formula:

- Discuss the classification of symplectic actions.

    Xiao: 80 possible groups, maximal size of 960.

- Give $ \dim {\mathbf{P}}(V) $ in terms of $ \dim V $.

    $ \dim {\mathbf{P}}(V) = \dim V - 1 $.

- Why does every K3 contain a rational curve?

    Bogomolov-Mumford: degenerate to a Kummer which is a product of two special elliptic curves

    Construct a configuration of rational curves there

    Use irreducibility of $ F_{2d} $ to deform to the general K3, possibly making it reducible, but has at least one irreducible.

    Use one of the irreducible curves, then specialize to any K3 in $ F_{2d} $, the curve can only break into rational curves.

- Discuss rational curves on K3s.

    Always has at least one.

    Any nonzero $ D\in \operatorname{Pic}(X)^\mathsf{eff} $ satisfies $ D\sim \sum R_i $ for some rational curves.

    Over $ k={\mathbf{C}} $ $ X $ is never uniruled, i.e. no rational curves move.

    Conjecture: $ X/\overline{k} $ has infinitely many rational curves.

- What is a Kummer surface?

    $ \widetilde{T/\iota} $ where $ T = {\mathbf{C}}^2/\Lambda $ is a torus and $ \iota $ is an involution with 16 ordinary double point singularities of type $ A_1 $.

- What are the dimensions of moduli of all and just algebraic K3s?

    All K3s: 20-dimensional

    Algebraic K3s: 19-dimensional

- What are the dimensions of moduli of all and just algebraic Kummer surfaces?

    All: 4-dimensional

    Algebraic: 3-dimensional.

- What is the dimension of moduli of Enriques surfaces?

    10-dimensional.

- What is the exceptional curve of a blowup of a point in a surface?

    A rational $ (-1){\hbox{-}} $curve, so $ E^2 = -1 $ with $ E\cong {\mathbf{P}}^1 $.

- What is a minimal surface?

    No rational $ (-1){\hbox{-}} $curves

- What is a ruled surface?

    $ \exists S\dashrightarrow C\times {\mathbf{P}}^1 $ with $ g(C) \geq 0 $.

- What is an abelian surface?

    $ {\mathbf{C}}^2/\Lambda \hookrightarrow{\mathbf{P}}^N $ with $ \Lambda $ a rank 4 lattice.

- What is an Enriques surface?

    Exactly quotients of K3s by fixed point free involutions.

    Smooth projective $ Y $ with $ 2K_Y \sim 0 $ and $ h^1({\mathcal{O}}_Y) = h^2({\mathcal{O}}_Y) = 0 $; the canonical induces an unramified 2-to-1 cover $ X\to Y $ for $ X $ a K3.

- What are bielliptic surfaces?

    Quotients of $ E\times E' $ elliptic curves.

- What is a special fact about proper elliptic surfaces?

    Always have an elliptic fibration.

- Classify surfaces by $ \kappa(S) $.

    $ -\infty $: Rational or ruled.

    $ 0 $: Four types; abelian, K3s, Enriques, bielliptic.

    $ 1: $ Proper elliptic.

    $ 2 $: General type.

- What's the etymology of K3?

    Named after K2 mountains

    Or Kummer, Kahler, Kodaira.

- Let $ X_4 $ be the Fermat quartic, what is $ K_{X_4} $?

    By adjunction, $ K_{X_4} = (K_{{\mathbf{P}}^3} + X_4)\mathrel{\Big|}_{X_4} = (-4H + 4H)\mathrel{\Big|}_{X_4} = 0 $.

- What is the irregularity of $ S $?

    $ q(S) \coloneqq h^1({\mathcal{O}}_S) $ or $ h^0(\Omega^1) $, so $ h^{1, 0} $ or $ h^{0, 1} $.

- What is the geometric genus of $ S $?

    $ h^{0}(\Omega^2) $, so $ h^{2, 0} $.

- What is $ \pi_1(X_4) $?

    By Lefschetz, $ \pi_1(X_4) = \pi_1({\mathbf{P}}^3) = 1 $.

- Compute $ q(X_4) $.

    $ H_1(X; {\mathbf{Z}}) = \pi_1(X)_{\operatorname{ab}}= 1 $ so $ 1 = H^1(X;{\mathbf{C}}) = H^{0,1 } \oplus H^{1, 0} $ so $ q(X_4) = 0 $.

- Give a birational definition of a K3.

    A compact complex surface with $ K_S \sim 0 $ and $ q(S) = 0 $.

- How does one show a surface is K3?

    Show $ q(S) = 0 $, e.g. using Lefschetz, and show $ K_S \sim 0 $ e.g. using adjunction.

- Give examples of K3s

    Any smooth quartic in $ {\mathbf{P}}^3 $.

    Complete intersections of type (2,3) or (2,2,2)

    $ S\to {\mathbf{P}}^2 $ 2x ramified over a sextic curve.

- Show that the double plane is K3.

    Check $ K_S = \pi^* K_{{\mathbf{P}}^2} + R $ where $ \pi_*(R) = C_6 $ and $ \pi_*(C_6) = 2R $, use $ K_{{\mathbf{P}}^2} = -3H $ and $ C_6 = 6H $ to get

    $$2K_S = \pi^*(2K_{{\mathbf{P}}^2}) + 2R = \pi^*(2K_{{\mathbf{P}}^2}) + \pi^*(C_6) = \pi^*(-6H) + \pi^*(6H) = 0$$

    If $ K_S\neq 0 $ but $ 2K_S = 0 $, note $ h^0(K_S) = 0 $.

    Check

    $$\chi(S) = 2(\chi({\mathbf{P}}^2) - \chi(C_6)) + \chi(R) = 2(3+18)-18 =24$$

    using that $ \chi(C_6) = 2\cdot 2g $.

    Check $ \chi({\mathcal{O}}_S) = 2 $ and use Noether to conclude $ 1-h^1({\mathcal{O}}_S) = 2 $, a contradiction.

- What is the Noether formula?

    $ \chi({\mathcal{O}}_X) = {1\over 12}(K_X^2 + \chi(X)) $.

- Give an equation for the double plane.

    $ S: t^2 = f_6(x_0, x_1, x_2) \subseteq {\mathbf{P}}(3,1,1,1) $ where $ C_6 = V(f_6) $.

- What is the involution on an abelian surface? What are its fixed points?

    $ A = {\mathbf{C}}^2/\Lambda $ with $ \operatorname{rank}_{\mathbf{Z}}\Lambda = 4 $, take $ (x,y)\mapsto (-x,y) $ on $ {\mathbf{C}}^2 $ to get $ 2(x,y)\in \Lambda $, there are 16 such points and thus 16 $ A_1 $ singularities in $ A/\iota $.

- What does an $ A_1 $ singularity look like?

    Locally the vertex of a cone, rational double points.

- If $ A{\circlearrowleft}_\iota $ is the involute on an abelian surface, what is the induced involution on the blowup at the 16 fixed points?

    Write $ \left\{{{\left[ { x_0: x_1} \right]}, {\left[ {x, y} \right]} \in {\mathbf{P}}^1 \times {\mathbf{C}}^2 {~\mathrel{\Big\vert}~}x_0 y = x_1 x}\right\} $ and send $ {\left[ {x_0, x_1} \right]}, {\left[ {x, y} \right]}\mapsto {\left[ { x_0: x_1} \right]}, {\left[ {-x, -y} \right]} $.

- What type of curve is the resolution of an $ A_1 $ singularity?

    $ D\cong {\mathbf{P}}^1 $ with $ D^2 = -2 $.

- What is $ \chi({\mathsf{K}}3) $?

    $ \chi({\mathsf{K}}3) = 24 $, all diffeomorphic to the Fermat quartic.

- Describe $ \Lambda_{{\mathsf{K}}3} $.

    Lattice structure on (all of) $ H^2({\mathsf{K}}3; {\mathbf{Z}}) $.

    Rank $ 22 $

    Signature $ (3, 19) $

    Isometric to $ U{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  } $ where

    $ U = \qty{{\mathbf{Z}}^2, \left(\begin{array}{ll}0 & 1 \\1 & 0\end{array}\right)} $

    $ E_8(-1) = $ unique even unimodular negative-definite lattice of rank 8.

- What is the rank of $ \Lambda_{{\mathsf{K}}3} $? Proof?

    $ \chi({\mathsf{K}}3) = 24 $ and $ p_{{\mathsf{K}}3}(t) = 1 + b_2 t^2 + t^4 $ since $ b_1 = b_3 = 0 $ from $ \pi_1({\mathsf{K}}3) = 1 $ and $ b_0 = b_4 = 1 $ from connectedness, thus $ \beta_2 = 22 $.

- Why is $ H^2({\mathsf{K}}3; {\mathbf{Z}}) $ torsionfree?

    By UCT, $ H^2({\mathsf{K}}3;{\mathbf{Z}})_{\operatorname{tors}}\cong H_2({\mathsf{K}}3; {\mathbf{Z}})_{\operatorname{tors}} $. If $ m\tau = 0 $ in the latter, construct an unramified cover $ i: \tilde S\to S $ with $ \chi(\tilde S) = m\chi(S) = 24m $.

    Since $ i $ is unramified, pulling back a top form yields $ K_{\tilde S} \sim 0 $.

    Noether formula: $ \chi({\mathcal{O}}_{\tilde S}) = {1\over 12} (K_{\tilde S}^2 + \chi(\tilde S)) = 2m $.

    The LHS is $ 2-h^1({\mathcal{O}}_{\tilde S}) \leq 2 $, the RHS is $ \geq 2 $, so $ m=1 $.

- What is the lattice associated to a K3?

    The intersection pairing:

    $$\begin{align*}H^2(X; {\mathbf{Z}}){ {}^{ \scriptstyle\otimes_{{\mathbf{Z}}}^{2} }  } &\to {\mathbf{Z}}\\ \alpha\otimes\beta \mapsto \int_X \alpha\wedge \beta\end{align*}$$

    Nondegenerate and unimodular by Poincare duality.

- What is $ \operatorname{sgn}\Lambda_{\mathrm{K3}} $?

    Have $ \operatorname{sgn}\Lambda_{{\mathsf{K}}3} = (s_+, s_-) $ where $ s_+ + s_- = 22 $, can take topological trace to get

    $$\operatorname{Trace}(\beta) = s_+- s_- = {1\over 3}(c_1^2  -2c_2) = {1\over 3}(0-2\cdot24)= -16$$

    $ c_1 = c_1({\mathbf{T}}X) = -K_X $

    $ c_2 = \chi(X) = 24 $.

    Combine $ s_+ + s_- = 22 $ and $ s_+ - s_- = -16 $ to solve for $ \operatorname{sgn}\Lambda_{\mathrm{K3}}= (3, 19) $,

- Why is $ \Lambda_{\mathrm{K3}} $ even?

    Take an irreducible curve $ C\subseteq X $ and use the genus formula:

    $$g(C) = 1 + {1\over 2}\qty{C.K_X + C^2} \implies C^2 = 2g-2 \in 2{\mathbf{Z}}$$

- Discuss Milnor's classification.

    Let $ \Lambda $ be an indefinite lattice of signature $ (s_+, s_-) $ where $ s_+,\, s_- > 0 $.

    If $ \Lambda $ is odd the $ \Lambda \cong (1){ {}^{ \scriptscriptstyle\oplus^{n} }  } \oplus (-1){ {}^{ \scriptscriptstyle\oplus^{n} }  } $ where $ n>0 $.

    If $ \Lambda $ is even then $ \Lambda \cong U{ {}^{ \scriptscriptstyle\oplus^{h} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{k} }  } $ where $ h > 0 $ and $ k\geq 0 $.

- What is $ \operatorname{sgn}U $?

    $ (1, 1) $

- What is $ \operatorname{sgn}E_8 $?

    $ (8, 0) $

- Discuss positivity of $ \beta_{{\mathsf{K}}3}({-}, {-}) $ on $ \omega_X $.

    $$\beta(\omega_X, \overline{\omega}_X)=\int_S \omega_X \wedge \overline{\omega}_X = \int_X {\left\lvert {f} \right\rvert}\,dz_1\wedge\,dz_2 \wedge\overline{\,dz_1} \wedge \overline{\,dz_2} > 0$$

    Similarly $ \beta(\omega_X, \omega_X) = 0 $.

    If $ \beta(\omega_X, H^{1, 1}) = 0 $ so $ H^{1, 1} \perp_\beta (H^{2, 0} \oplus H^{0,2}) $

- Discuss the period domain.

    $ {\mathbf{C}}\omega_X \in {\mathbf{P}}H^2(X;{\mathbf{C}}) $.

    Take a marking $ \Phi: H^2(X;{\mathbf{Z}})\to \Lambda_{\mathrm{K3}} $ and define

    $$\Omega = \left\{{[\omega]\in {\mathbf{P}}(\Lambda_{\mathrm{K3}}\otimes{\mathbf{C}}) {~\mathrel{\Big\vert}~}\omega^2 = 0, {\left\lvert {\omega} \right\rvert} > 0}\right\}, \quad {\left\lvert {\omega} \right\rvert} \coloneqq\omega.\overline{\omega}$$

    Can write as

    $$\Omega \cong \left\{{{\left[ {z_0:\cdots:z_{21}} \right]}\in {\mathbf{P}}^{21}{~\mathrel{\Big\vert}~}z_0^2+z_1^2 + z_2^2 - z_3^2 -\cdots - z_{21}^2 = 0,\, \sum_{i=0}^{21} {\left\lvert {z_i} \right\rvert}^2 > 0}\right\}$$

    which is an open subset of a quadric in $ {\mathbf{P}}^{21} $ and thus 20-dimensional.

    One has $ \Phi({\mathbf{C}}\omega_X) \subseteq \Omega $; define this as the period domain of a marked K3.

    Torelli gives surjectivity.

- What is a marking?

    $ \Phi: H^2(X; {\mathbf{Z}}) { \, \xrightarrow{\sim}\, }\Lambda_{\mathrm{K3}} $ an isometry.

- What is $ \dim {\mathbf{P}}^n $.

    $ \dim {\mathbf{P}}^n = n $, locally $ n $ degrees of freedom: $ p \sim {\left[ {1: x_1/x_0:\cdots :x_n/x_0} \right]} $.

- What is the moduli space of all K3s vs projective K3s?

    All K3s: $ \dcosetr{\Omega}{{\operatorname{O}}(\Lambda_{\mathrm{K3}})} $, 20-dimensional.

    Projective: 19-dimensonal, since one has to vary periods in the orthogonal complement of an ample class.

- What is the dimension of quartics in $ {\mathbf{P}}^3 $? Up to coordinate changes?

    $ h^0({\mathcal{O}}_{{\mathbf{P}}^3}(4)) = {4+3\choose 4} = 35 $ and its projective dimension is 34.

    $ \dim \operatorname{PGL}_4({\mathbf{C}}) = 16-1 = 15 $

    So $ 34-15 = 19 $ moduli.

- What is $ h^0({\mathcal{O}}_{{\mathbf{P}}^n}(m)) $?

    $ {m+n\choose m} $.

- What is $ \dim \operatorname{PGL}_n({\mathbf{C}}) $?

    $ n^2 - 1 $.

- What are the dimensions of moduli for $ S_{2,3}, S_{2,2,2} $, and the double plane $ S\to {\mathbf{P}}^2 $?

    All 19.

- What does $ \Omega/{\operatorname{O}}(\Lambda_{\mathrm{K3}}) $ parameterize?

    All K3s, including non-projective.

- What is the ample divisor associated to an embedding?

    If $ \phi: S\hookrightarrow{\mathbf{P}}^n $, take the hyperplane section $ L = \phi(S) \cap H $ for $ H $ any hyperplane.

- What is the degree of a projective K3?

    $ L^2 = 2d $ for $ L $ a hyperplane section of its projective embedding.

    Even since $ L = \phi(S) \cap H \in H^2(S; {\mathbf{Z}}) \cap H^{1, 1}(S) $ which is an even lattice.

- What is $ L^\perp $?

    $ L^\perp \coloneqq\left\{{v\in \Lambda_{\mathrm{K3}}{~\mathrel{\Big\vert}~}{\left\langle {v},~{x} \right\rangle} = 0 \, \forall x\in L}\right\} $.

- Describe $ [\omega_S] $.

    $$[\omega_S]\in \left\{{[\omega] \in {\mathbf{P}}(L^\perp\otimes{\mathbf{C}}) {~\mathrel{\Big\vert}~}{\left\lvert {\omega} \right\rvert} > 0,\, \omega^2 = 0 }\right\}$$

    Here $ \dim L = 1 $ so $ \dim L^\perp = 20-1 = 19 $.

- What is the degree of $ F_4 $?

    Embed $ F_4\hookrightarrow{\mathbf{P}}^3 $ and slice by a hyperplane to get 4 points, so $ L^2 = 4 $ and $ d=2 $.

- Describe $ c_1(L) $ for a K3 and its relation to $ \operatorname{Pic} $ and $ {\operatorname{NS}} $.

    Take the exponential SES $ {\mathbf{Z}}\hookrightarrow{\mathcal{O}}_S \twoheadrightarrow{\mathcal{O}}_S^{\times} $ to get $ \delta^1: H^1(S; {\mathcal{O}}_S^{\times}) \to H^2(S; {\mathbf{Z}}) $, identify $ H^1 $ with $ \operatorname{Pic} $ and $ c_1 = \delta^1 $.

    Get $ \operatorname{Pic}^0(S) = \ker c_1 $ and $ \operatorname{Pic}(S)/\operatorname{Pic}^0(S)\cong \operatorname{im}c_1 = {\operatorname{NS}}(X) $.

- Discuss $ {\operatorname{NS}}(X) $ for $ X $ a K3.

    $ \operatorname{Pic}^0(X) = 0 $ so $ \operatorname{Pic}(X) \cong {\operatorname{NS}}(X) $.

    The sublattice of $ H^{2}(X; {\mathbf{Z}}) $ generated by algebraic cycles.

- Describe $ {\operatorname{NS}}(X) $ and $ \operatorname{Pic}(X) $ in terms of divisors.

    $ {\operatorname{NS}}(X) = \operatorname{CDiv}(X)/\sim $ modulo algebraic equivalence.

    $ \operatorname{Pic}(X) = \operatorname{CDiv}(X)/\sim $ modulo linear equivalence.

    $ {\operatorname{CH}}_k(X) = Z_k(X)/\sim $ modulo rational equivalence

- What is the lattice structure on $ {\operatorname{NS}}(X) $?

    $ \operatorname{Pic}(X) = {\operatorname{NS}}(X)\hookrightarrow H^2(X; {\mathbf{Z}}) $ so it is an even primitive sublattice of $ \Lambda_{\mathrm{K3}} $.

    $ T_X \coloneqq{\operatorname{NS}}(X)^\perp $ is also a lattice (transcendental)

- What is the Lefschetz 1-1 theorem?

    There is a surjection $ c_1: \operatorname{Pic}(X) \twoheadrightarrow H^{1,1} \cap H^2(X; {\mathbf{Z}}) $.

- How is the Lefschetz 1-1 theorem used for K3s?

    $ {\operatorname{NS}}(X) = \operatorname{Pic}(X) = H^{1, 1}(X) \cap H^2(X; {\mathbf{Z}}) = \omega_S^\perp \cap H^2(X;{\mathbf{Z}}) $.

- What is $ \rho(X) $?

    $ \operatorname{rank}_{\mathbf{Z}}\operatorname{Pic}(X) = \operatorname{rank}_{\mathbf{Z}}{\operatorname{NS}}(X) $.

    Since $ {\operatorname{NS}}(X) \leq H^{1, 1}(X) $, there is a bound $ \rho(X) \leq 20 $.

- What is $ \operatorname{sgn}H^2(X; {\mathbf{Z}}) $?

    $ (3, 19) $

- Discuss $ \operatorname{sgn}{\operatorname{NS}}(X) $ and $ \operatorname{sgn}T_X $.

    $ (a, b) $ where $ a\leq 1 $ since $ \operatorname{sgn}H^2(X;{\mathbf{Z}}) = (3, 19) $ and if $ H^{0, 1} \oplus H^{1,0} = {\mathbf{C}}\omega_X \oplus {\mathbf{C}}\overline{\omega_X} $ one can form a 2-dimensional space $ V = \left\langle{\omega_X + \overline{\omega}_X, i(\omega_X - \overline{\omega}_X)}\right\rangle $ where both generators have positive square. and $ V\subseteq (H^{1,1})^\perp $.

    For $ X $ projective, $ L $ an ample class with $ L^2 > 0 $ yields

    $$\operatorname{sgn}{\operatorname{NS}}(X) = (1, \rho(X) - 1) \implies \operatorname{sgn}T_X = (2, 20-\rho(X))$$

    since they must add up to $ (3, 19) $.

- Discuss the transcendental lattice $ T_X $.

    $ T_X \coloneqq{\operatorname{NS}}(X)^\perp \subseteq H^2(X; {\mathbf{Z}}) $.

    $ T_X \otimes{\mathbf{C}}\supseteq H^{2, 0} \oplus H^{0, 2} $, so the periods move in $ T_X $.

    $ [\omega_X] \in \left\{{ {\mathbf{P}}(T_X^L\otimes{\mathbf{C}}) {~\mathrel{\Big\vert}~}\omega^2 = 0, {\left\lvert {\omega} \right\rvert} > 0}\right\} $ where $ T_X^L = L^\perp $.

- Discuss $ \operatorname{Pic}(X) $ for a generic projective K3.

    Generically $ \operatorname{Pic}(X) = \left\langle{L}\right\rangle_{\mathbf{Z}} $ for $ L $ associated to the hyperplane section.

- Discuss projective models of K3s.

    Saint-Donat 74: if $ {\mathcal{L}}\in \operatorname{Pic}(X) $ with $ {\mathcal{L}}^2 > 0 $ with no base components (so bpf), then the induced embedding $ \phi_{{\left\lvert {{\mathcal{L}}} \right\rvert}}:X\to {\mathbf{P}}^N $ where $ N = h^0({\mathcal{O}}_X({\mathcal{L}})) - 1 = {1\over 2}{\mathcal{L}}^2 -1 $ is either

    Hyperelliptic: 2-to-1 cover and $ \deg \operatorname{im}\phi_{{\left\lvert {{\mathcal{L}}} \right\rvert}} = {1\over 2}{\mathcal{L}}^2 $, or

    Non-hyperelliptic: birational with $ \deg \operatorname{im}\phi_{{\left\lvert {{\mathcal{L}}} \right\rvert}} = {\mathcal{L}}^2 $.

    $ {\mathcal{L}}^2 = 2 $ is the double plane.

    $ {\mathcal{L}}^2 = 4 $ non-hyperelliptic is $ X\to {\mathbf{P}}^3 $ a quartic

    $ {\mathcal{L}}^2 = 6 $ non-hyperelliptic is $ X\to {\mathbf{P}}^4 $ a complete intersection $ (2, 3) $

    $ {\mathcal{L}}^2 = 8 $ non-hyperelliptic is $ X\to {\mathbf{P}}^5 $ a complete intersection $ (2, 2, 2) $

- Discuss $ \mathop{\mathrm{Aut}}(X) $.

    Torelli induces $ \mathop{\mathrm{Aut}}(X) \hookrightarrow{\operatorname{O}}(H^2(X; {\mathbf{Z}})) $

    Image is effective Hodge isometries: preserves 2-forms and Kahler cones.

    Discrete and finitely generated.

    Generically trivial when $ \operatorname{Pic}(X) = \left\langle{L}\right\rangle_{\mathbf{Z}} $ for $ d\neq 1 $.

    If $ \sigma $ preserves an ample class then it must have finite order.

- What is a symplectic automorphism?

    $ \sigma^* \omega_X = \omega_X $, i.e. preserves the symplectic form.

    Possibly forces $ \operatorname{rank}_{\mathbf{Z}}\operatorname{Pic}(X) \geq 8 $.

- What is the SES involving the symplectic automorphisms of $ G\leq \mathop{\mathrm{Aut}}(X) $ a finite subgroup?

    Take $ \alpha: G\to {\mathbf{C}}^{\times} $ where $ f\mapsto \alpha(f) $ where $ f^* \omega_X = \alpha(f)\omega_X $.

    Restrict to its image $ \mu_m $ to get a SES defining $ G_0 \hookrightarrow G\twoheadrightarrow\mu_m $ where $ G_0 \coloneqq\left\{{f\in G{~\mathrel{\Big\vert}~}f^*\omega_X = \omega_X}\right\} $ .

- What are symplectic, non-symplectic, and purely non-symplectic automorphisms?

    Symplectic: $ g^*\omega_X = \omega_X $

    Non-symplectic: $ g^*\omega_X = \alpha(g)\omega_X $ where $ \alpha\neq 0,1 $.

    Purely non-symplectic: $ g^* \omega_X = \alpha(g)\omega_X $ where $ \alpha(g) = \zeta_m $ a *primitive* root of unity $ m={\left\lvert {g} \right\rvert} $.

- Why are non-symplectic automorphisms important? (Proof sketch)

    If $ X $ admits a finite order non-symplectic automorphism, $ X $ is automatically projective.

    Proof idea: use Kodaira embedding, find a rational Kahler class.

    Use that $ H^2(X;{\mathbf{Q}})\hookrightarrow H^2(X;{\mathbf{R}}) $ is dense and $ {\mathcal{K}} $ is open in $ H^{1, 1}\otimes{\mathbf{R}} $.

    Find $ c\in H^2(X; {\mathbf{Q}}) $, decompose into $ c_{2,0} + c_{1,1} + c_{0, 2} $ in $ H^2(X;{\mathbf{C}}) $ where $ c_{1,1} $ is a real Kahler form, and kill $ c_{2,0}, c_{0, 2} $ using the automorphism:

    Average to define $ h \coloneqq\sum_{i=0}^{{\left\lvert {g} \right\rvert} - 1}(g^*)^i c $ which is $ g{\hbox{-}} $invariant.

    Use that $ g $ respects the Hodge decomposition, and $ h_{1,1} = h\in H^2(X;{\mathbf{Q}}) $ since $ H^{2,0}, H^{0, 2} $ does not contain $ g{\hbox{-}} $invariant elements.

    By Kodaira embedding, some multiple of $ h $ gives the embedding.

- Give examples of automorphisms of K3s.

    $ \iota: F_4\to F_4 $ where $ {\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:-x_2:-x_3} \right]} $, symplectic, $  \mathrm{Fix}(\iota) $ is 8 points.

    $ \iota: F_4\to F_4 $ where $ {\left[ {x_0:x_1:x_2:x_3} \right]}\mapsto {\left[ {x_0:x_1:\zeta_4 x_2: \zeta_4 x_3} \right]} $.

    Set $ \omega\coloneqq({\partial}_0 f_4)^{-1}\,dx_2 \wedge \,dx_3 $, then $ \omega\mapsto -\omega $, so non-symplectic but not purely non-symplectic.

- Describe symplectic automorphisms locally.

    Can find local coordinates where $ \sigma \in \operatorname{GL}_2({\mathbf{C}}) $ is of the form $ { \begin{bmatrix} {\lambda } & {0}  \\ {0} & {\overline{\lambda}} \end{bmatrix} } $ with $ \lambda $ an $ n $th root of unity where $ n={\left\lvert {\sigma} \right\rvert} $.

    Has only isolated fixed points, at most 8.

    Nikulin counts $ {\sharp} \mathrm{Fix}(\sigma) $ when $ {\left\lvert {\sigma} \right\rvert} $ has small prime order.

    Quotient has only type $ A $ singularities.

- Describe the Lefschetz number of a symplectic automorphism.

    $ L(\sigma) \coloneqq\sum (-1)^i \operatorname{Tr}(\sigma^* \curvearrowright H^i({\mathcal{O}}_S) ) $.

    $ L(\sigma)\neq 0 \implies  \mathrm{Fix}(\sigma)\neq\emptyset $

    $ L(\sigma) = 2 $ for a symplectic automorphism.

- Why are symplectic automorphisms important?

    Quotients are again K3.

    Not the case for non-symplectic automorphisms!

- For $ \sigma $ symplectic on $ X $ of order $ p $, sketch how to compute $ {\sharp} \mathrm{Fix}(\sigma) $.

    Take $ X\twoheadrightarrow X/\sigma $ and resolve to $ Y $ to get $ X\to Y $ a $ p{\hbox{-}} $to-$ 1 $ map; resolving $ A_{p-1} $ singularities.

    Write $ X' \coloneqq X\setminus \mathrm{Fix}(\sigma) $ and $ Y' \coloneqq Y\setminus\widetilde{ \mathrm{Fix}(\sigma)} $ where $ \widetilde{ \mathrm{Fix}}(\sigma) $ are the corresponding rational curves to get $ \chi(X') = p\chi(Y') $.

    Check $ \widetilde{ \mathrm{Fix}}(\sigma) $ is a chain of $ p-1 $ copies of $ {\mathbf{P}}^1 $ meeting at $ p-2 $ points, so $ \chi\widetilde{ \mathrm{Fix}}(\sigma) = 2(p-1) - (p-2) = p $.

    Combine these to get

    $$\chi(X) - {\sharp} \mathrm{Fix}(\sigma) = p\cdot \chi(Y)- p\cdot {\sharp} \mathrm{Fix}(\sigma) \implies {\sharp} \mathrm{Fix}(\sigma) = {24\over p-1}$$

    since $ Y $ is also a K3 and thus $ \chi(X) = \chi(Y) = 24 $.

- What is the Kodaira embedding theorem?

    If $ X $ is compact Kahler and $ {\mathcal{L}}\in \operatorname{Pic}(X) $ then $ {\mathcal{L}}> 0 \iff {\mathcal{L}}\in \operatorname{Pic}(X)^{\mathrm{amp}} $.

    $ \impliedby $: if $ {\mathcal{L}}{ {}^{ \scriptstyle\otimes_{}^{n} }  } = {\mathcal{O}}_{{\mathbf{P}}^N}(1)\mathrel{\Big|}_X $, the hyperplane bundle is positive since its curvature is the Fubini-Study form.

    Positive: $ {\mathcal{L}}> 0 \iff {\mathcal{L}} $ admits a metric $ h $ such that the associated curvature $ \sqrt{-1}\Theta({\mathcal{L}}, h) $ is a positive 1-1 form.

    Comes from the Chern connection induced by $ { \overline{{\partial}}}:{\mathcal{L}}\to {\mathcal{L}}\otimes H^{0, 1}(M) $, namely $ \nabla^{0, 1} = { \overline{{\partial}}} $.

- Give an example of how having too many rational curves can be used in a proof.

    If $ {\left\lvert {\sigma} \right\rvert} = p = 11 $ then $ {\sharp} \mathrm{Fix}(\sigma) = 2 $ yields 2 $ A_{10} $ singularities, thus 20 independent $ (-2){\hbox{-}} $curves in $ H^2(X; {\mathbf{Z}}) $ which generate a sublattice of signature $ (0, 20) $.

    This contradicts $ \operatorname{sgn}H^2 = (3, 19) $.

- What is an elliptic fibration?

    Proper morphism, connected fibers are smooth genus 1 algebraic curves.

    Equivalently, by proper base change, the generic fiberis a smooth genus 1 curve.

    E.g. any product of elliptic curves, surfaces with $ \kappa(X) = 1 $, Enriques surfaces

- What is the classification of $ G\in {}_{{\mathbf{Z}}}{\mathsf{Mod}}^{\mathrm{fin}}\curvearrowright X $ symplectically?

    By Nikulin, 14 possibilities:

    $ C_n $ where $ n=2,\cdots, 8 $.

    $ C_n^2 $ where $ n=2,3,4 $.

    $ C_2\times C_n $ where $ n=4,6 $.

    $ C_2^3 $

    $ C_2^4 $.

- What is the classification of $ G\in{\mathsf{Fin}}{\mathsf{Grp}}\curvearrowright X $ symplectically?

    Mukai: maximal order $ {\sharp}G \leq 360 $, with equality if $ G = M_{20} $.

- Discuss $ G\in {\mathsf{Fin}}{\mathsf{Grp}}\curvearrowright X $ not necessarily symplectically.

    Kondo: $ {\sharp}G \leq 3840 $, proved using isometries of lattices.

    Equality if $ M_{20}\hookrightarrow G\twoheadrightarrow C_4 $.

- What is the Mathieu group?

    $ M_{20} = A_5\rtimes C_2^4 $, order 960.

- What are the possible orders of CM on an elliptic curve?

    $ 2,3,4,6 $.

- Give an example of an elliptic curve with CM.

    $ y^2 = x^3 + x $ has CM by $ \zeta_3 $.

- Define the invariant lattice.

    $$H^2(X; {\mathbf{Z}})^\sigma \coloneqq\left\{{x\in H^2(X;{\mathbf{Z}}) {~\mathrel{\Big\vert}~}\sigma.x = x}\right\}$$

- Give an example of a K3 with maximal Picard rank.

    $ X = \mathrm{Kummer}(E_3{ {}^{ \scriptscriptstyle\times^{2} }  }) $ where $ E_3 $ is an elliptic curve with CM by $ \zeta_3 $.

    Satisfies $ \rho(X) = 20 $.

    Given by $ X\hookrightarrow{\mathbf{P}}^3 $ by $ \sum x_i^4 - 12\prod x_i $.

- Discuss $ (H^2(X; {\mathbf{Z}})^\sigma)^\perp $.

    $$(H^2(X; {\mathbf{Z}})^\sigma)^\perp \subseteq {\operatorname{NS}}(X) \implies H^2(X;{\mathbf{Z}})^\sigma \subseteq T_X$$

    Nikulin shows $ (H^2(X;{\mathbf{Z}})^\sigma)^\perp $ is a negative definite lattice.

- Compute $ \operatorname{rank}_{\mathbf{Z}}(H^2(X; {\mathbf{Z}})^\sigma)^\perp $.

    Start with $ \operatorname{rank}_{\mathbf{Z}}(H^2(X;{\mathbf{Z}}))^\perp = m(p-1) $.

    $$\begin{align*}{\sharp} \mathrm{Fix}(\sigma) &= \chi( \mathrm{Fix}(\sigma)) \\ &= \sum_{i=0}^4 (-1)^i \operatorname{Tr}(\sigma \curvearrowright H^i(X;{\mathbf{Z}})) \\ &= 2 + \operatorname{Tr}(\sigma \curvearrowright H^2(X;{\mathbf{Z}})^\sigma) + \operatorname{Tr}(\sigma \curvearrowright( H^2(X;{\mathbf{Z}})^\sigma) ^\perp) \\ &= 2 + (22 - m(p-1)) - m \\&\implies m = {24\over p+1}\end{align*}$$

    using that $ \sum_{i=1}^{m-1}\zeta_m^i = -1 $.

- Give lower bounds on $ \rho(X) $ when $ \zeta_p\curvearrowright X $.

    *(Answer was a figure; image not recovered.)*

- Why are K3s with automorphisms special?

    Gives a lower bound on $ \rho(X) $.

- Compute the dimension of moduli of K3s with an order 3 symplectic automorphism.

    Dimension 7. How to show: ...?

- Discuss $ {\operatorname{NS}}(X) $ when $ X $ has an order 3 automorphism.

    Always get the Coxeter-Todd lattice, whose points give highest density sphere packing in dimension 12.

- How is a variety defined scheme-theoretically?

    Separated geometrically integral scheme of finite type over $ k $.

- What is a geometric point?

    A morphism $ \operatorname{Spec}k \to X $ where $ k={ \overline{k} } $.

- What is a geometric fiber?

    The fiber over a geometric point, i.e. for $ f:X\to Y $, the fiber product with $ p_i: \operatorname{Spec}k \to Y $ given by $ X \underset{\scriptscriptstyle {Y} }{\times}\operatorname{Spec}k $.

- What is a geometrically integral scheme?

    Idea: prevents becoming reduced or reducible after a field extension.

    The structure morphism $ f: X\to \operatorname{Spec}k $ is geometrically integral, i.e.for all geometric points $ p_i: \operatorname{Spec}L \to \operatorname{Spec}k $ the fiber $ X \underset{\scriptscriptstyle {\operatorname{Spec}k} }{\times} \operatorname{Spec}L $ is integral.

    Thm: geometrically integral iff geometrically reduced and geometrically irreducible.

- When is a variety smooth?

    If $ \Omega_{X} $ is locally free of rank $ \dim X $

    Equivalently, $ X \underset{\scriptscriptstyle {k} }{\times}{ \overline{k} } $ is a regular scheme.

- What is an **algebraic** K3 surface?

    Smooth complete variety $ X $ over a field $ k $, $ \dim X = 2 $, where $ \omega_{X} \cong {\mathcal{O}}_X $ and $ H^1({\mathcal{O}}_X) = 0 $.

- Discuss the cotangent sheaf of a K3.

    Locally free of rank 2, $ \Omega_X^2 = \operatorname{det}\Omega_X = \omega_X \cong {\mathcal{O}}_X $.

    Carries an algebraic symplectic structure $ (\Omega_X){ {}^{ \scriptscriptstyle\times^{2} }  } \to {\mathcal{O}}_X $ inducing an isomorphism $ {\mathbf{T}}_X\cong \Omega_X {}^{ \vee }\coloneqq\mathop{\mathcal{H}\! \mathit{om}}(\Omega_X, {\mathcal{O}}_X) \cong \Omega_X $.

- When is a K3 surface projective?

    Always: any smooth complete surface is projective.

- Why is a smooth quartic a K3?

    If $ X \subseteq {\mathbf{P}}^3 $ then take the LES for $ {\mathcal{O}}_{{\mathbf{P}}^3}(-4) \hookrightarrow{\mathcal{O}}_{{\mathbf{P}}^3} \twoheadrightarrow{\mathcal{O}}_X $ and use that $ H^1({\mathcal{O}}_{{\mathbf{P}}^3}) = H^2({\mathcal{O}}_{{\mathbf{P}}^3}(-4)) = 0 $ to conclude $ H^1({\mathcal{O}}_X) = 0 $.

    The adjunction formula yields $ \omega_X = \omega_{{\mathbf{P}}^3}\otimes{\mathcal{O}}(4)\mathrel{\Big|}_X \cong {\mathcal{O}}_X $.

- Give several examples of K3s.

    A smooth quartic, e.g. $ x_0^4 + \cdots + x_3^4\subset {\mathbf{P}}^3 $ when $ \operatorname{ch}k \neq 2 $.

    A smooth complete intersection of type $ (d_1,\cdots, d_n) \subset {\mathbf{P}}^{n+2} $ when $ \sum d_i = n+3 $.

    Kummer surfaces: the quotient of an abelian surface by the involution $ x\mapsto -x $ after resolving 16 singular points.

    A branched double cover $ X\to {\mathbf{P}}^2 $ branched along a smooth curve $ C $ of degree 6, using $ \pi_* {\mathcal{O}}_X \cong {\mathcal{O}}_{{\mathbf{P}}^2} \oplus {\mathcal{O}}(-3) \implies H^1({\mathcal{O}}_X) = 0 $ and $ \omega_X \cong \pi^*(\omega_{{\mathbf{P}}^2} \otimes{\mathcal{O}}(3)) \cong {\mathcal{O}}_X $.

- For $ L_1, L_2\in \operatorname{Pic}X $, define $ L_1.L_2 $.

    The coefficient of $ ab $ in $ \chi(L_1^1\otimes L_2^b) $.

- Compute $ L_1.{\mathcal{O}}(C) $ for $ C $ an integral curve.

    $ \deg L_2 \mathrel{\Big|}_C $.

- Compute $ {\mathcal{O}}(C_1).{\mathcal{O}}(C_2) $ for $ C_1, C_2 $ integral curves intersecting at finitely many points.

    $$\sum_{i=x \in C_1 \pitchfork C_2} \dim_k {{\mathcal{O}}_{X, x}\over \left\langle{f_{1, x}, f_{2, x}}\right\rangle }$$

- Discuss $ L.{\mathcal{O}}(C) $ when $ L $ is ample.

    Always positive: $ L_1.C = \deg L_1\mathrel{\Big|}_C > 0 $.

- What is Riemann-Roch for line bundles on surfaces?

    $ \chi(L) - \chi({\mathcal{O}}_X) = {1\over 2} (L.L \otimes\omega_X {}^{ \vee }) $.

- Define the Nron-Severi group.

    $ {\operatorname{NS}}(X) \coloneqq\operatorname{Pic}(X) / \operatorname{Pic}^0(X) $, line bundles algebraically equivalent to zero.

- What does it mean for a line bundle $ L $ to be numerically trivial?

    $ L. {\mathcal{L}}= 0 $ for all $ {\mathcal{L}}\in \operatorname{Pic}(X) $, e.g. any $ L\in \operatorname{Pic}^0(X) $.

- What is $ \mathrm{Num}(X) $?

    $ \operatorname{Pic}(X)/\operatorname{Pic}(X)^\tau $. quotienting by the subgroup of numerically trivial line bundles.

    A $   {}_{{\mathbf{Z}}}{\mathsf{Mod}} $ with a nondegenerate symmetric integral pairing.

- What is the Picard number?

    $ p(X) = \operatorname{rank}_{\mathbf{Z}}{\operatorname{NS}}(X) $ where $ {\operatorname{NS}}(X) \coloneqq\operatorname{coker}(\operatorname{Pic}^0(X) \hookrightarrow\operatorname{Pic}(X)) $.

- What is the signature of the intersection form on $ \operatorname{Num}(X) $?

    $ (1, p(X) - 1) $ for $ p(X) $ the Picard number, so its real form diagonalizes to $ (1, -1,\cdots, -1) $.

- What is $ \chi({\mathcal{O}}_X) $ for a K3?

    2: $ h^0({\mathcal{O}}_X) = h^1({\mathcal{O}}_X) = 0 $ by definition, and by Serre duality $ h^2({\mathcal{O}}_X) = h^0(\omega_X) = 1 $.

- What is $ \pi_1^\text{ét}(X) $ for a K3?

    Trivial: if $ Y\to X $ is an irreducible finite etale cover of degree $ d $ then $ Y $ is a smooth complete surface, $ \omega_Y \cong{\mathcal{O}}_Y $, and $ \chi({\mathcal{O}}_Y) = d\chi({\mathcal{O}}_X) =2d $ with $ h^0({\mathcal{O}}_Y) = h^2({\mathcal{O}}_Y) = 1 $.

    Thus $ 2-h^1({\mathcal{O}}_Y) = 2d \implies d=1 $.

- What is the statement of RR for $ L\in \operatorname{Pic}(X) $ for $ X $ a K3? How does this change if $ L $ is ample?

    $ \chi(L) = {1\over 2}L^2 + 2 $.

    If $ L $ is ample then $ H^1(L) = 0 $ so the LHS is $ h^0(L) $.

- Give an equivalent characterization of when a line bundle is trivial.

    Both $ H^0(L) $ and $ H^0(L {}^{ \vee }) $ are nontrivial.

- What is the Hirzebruch-Riemann-Roch theorem?

    $ \chi({\mathcal{F}}) = \int {\mathrm{ch}}({\mathcal{F}})\operatorname{Td}(X) = {\mathrm{ch}}_2({\mathcal{F}}) + 2\operatorname{rank}({\mathcal{F}}) $.

- What is $ c_2(X) $ for a K3?

    24 by the Noether formula.

- What is the Hodge diamond for a K3?

    Use that $ h^{p, q}(X) = 1 $ for the corners by definition, $ h^{0, 1}(X) = 0 $, and

    $$2 h^0\left(\Omega_X\right)-h^1\left(\Omega_X\right)=\operatorname{ch}_2\left(\Omega_X\right)+4=4-\mathrm{c}_2\left(\Omega_X\right)=-20$$

    so $ h^1(\Omega_X) = 20 $ since $ h^0(\Omega_X) = 0 $ by HRR.

- Discuss $ h^0({\mathbf{T}}_X) $ for $ X $ a K3.

    $ h^0({\mathbf{T}}_X) = h^0(\Omega_X)= 0 $ using the isomorphism $ {\mathbf{T}}_X\cong \Omega_X $. So no global vector fields.

- Discuss GAGA

    To any $ X\in{\mathsf{Sch}}^{\mathrm{ft}}_{/ {{\mathbf{C}}}} $ there exist $ X^{\mathrm{an}}\to X $ a morphism of ringed spaces from an analytic space where the points of $ X^{\mathrm{an}} $ correspond to the closed points of $ X $ and there is an induced equivalence $ {\mathsf{Coh}}(X) { \, \xrightarrow{\sim}\, }{\mathsf{Coh}}(X^{\mathrm{an}}) $.

- What is a **complex** K3 surface?

    A compact connected complex manifold, $ \dim X = 2 $, with $ \Omega^2_X \cong {\mathcal{O}}_X $ and $ h^1({\mathcal{O}}_X) = 0 $.

    If $ X $ is an algebraic K3 then $ X^{\mathrm{an}} $ is a (projective) complex K3.

- Why is $ X^{\mathrm{an}} $ projective when $ X $ is an algebraic K3?

    GAGA: the ideal sheaf $ I $ of $ X\subseteq {\mathbf{P}}^n $ is coherent analytic and thus isomorphic to an algebraic ideal sheaf.

- Are all complex K3s projective?

    No: most complex tori $ X={\mathbf{C}}^2/\Gamma $ are not.

- Discuss $ H^*_{\mathrm{sing}}(X) $ for a K3.

    Take the LES $ H^1(X;{\mathbf{Z}}) \to H^1(X;{\mathcal{O}})\to H^1(X;{\mathcal{O}}^{\times}) $ to show $ H^1(X;{\mathbf{Z}}) = H^3(X;{\mathbf{Z}}) = 0 $ mod torsion and $ H^0(X;{\mathbf{Z}}) = H^4(X;{\mathbf{Z}}) = {\mathbf{Z}} $. The only other nontrivial group is $ H^2(X; {\mathbf{Z}}) $.

- Discuss $ H^2(X; {\mathbf{Z}}) $

    Torsionfree, since $ 0\to \operatorname{Pic}(X) \to H^2(X;{\mathbf{Z}}) \to H^2(X; {\mathcal{O}}) $ using $ \operatorname{Pic}(X)\cong H^1(X; {\mathcal{O}}^{\times}) $; since $ H^2(X;{\mathcal{O}})\cong {\mathbf{C}} $ and $ \operatorname{Pic}(X) $ are torsionfree, so is $ H^2 $. The intersection form on $ \operatorname{Pic}(X) $ corresponds to the intersection form on $ H^2 $ under this embedding.

    $ \operatorname{rank}_{\mathbf{Z}}H^2 = 22 $ since $ e(X) = c_2(X) = 24 $ and $ b_2(X) = 22 $, and this defines a unimodular lattice $ {\mathbf{E}}_8(-1){ {}^{ \scriptscriptstyle\oplus^{2} }  } \oplus U{ {}^{ \scriptscriptstyle\oplus^{3} }  } $.

- What is the Hodge-Frlicher spectral sequence?

    \[$H^q(X; \Omega^p_X) \Rightarrow H^{p+q}(X; {\mathbf{C}})\]

- Discuss bounds on $ p(X) $.

    By Lefschetz $ (1,1) $ one has $ \operatorname{Pic}(X) \cong H^2(X;{\mathbf{Z}})\cap H^{1, 1}(X) $ and $ (H^2(X;{\mathbf{Z}})\cap H^{1, 1}(X))\otimes{\mathbf{C}}\subseteq H^1(\Omega_X) $ which is a 20-dimensional space, so $ p(X) \leq 20 $. Each $ 0\leq i\leq 20 $ is obtained.

- Give a bundle-theoretic condition for projectivity of surfaces.

    If $ X $ is a smooth compact complex surface, $ X $ is projective iff $ \exists L\in \operatorname{Pic}(X) $ with $ L^2 > 0 $.

- What is the signature of the intersection form on $ H^2 $?

    By the Thom-Hirzebruch index theorem, $ {1\over 3}p_1(X) = {1\over 3}(c_1^2(X) - 2c_2(X)) = -16 $, use that $ b_2(X) = 22 $ to get $ (3, 19) $.

- How is $ \rho(X)\leq 22 $ proved for K3s over positive characteristic fields?

    Take the LES in $ H^*_\text{ét} $ for the Kummer sequence $ \mu_n\hookrightarrow{\mathbf{G}}_m\twoheadrightarrow{\mathbf{G}}_m $ for $ n $ prime to $ p $, use $ \operatorname{Pic}(X) \cong H^1(X;{\mathbf{G}}_m) $ to show $ H^1_\text{ét}(X; \mu_n) = k^{\times}/(k^{\times})^n $.

    Use $ k $ separably closed and duality to get $ H^1_\text{ét}(X; { {\mathbf{Z}}_{\widehat{\ell}} }) = H^3(X;{ {\mathbf{Z}}_{\widehat{\ell}} }) = 0 $.

    Use $ c_2(X) = 24 $ to conclude $ \operatorname{rank}_{\mathbf{Z}}H^2_\text{ét}(X; { {\mathbf{Z}}_{\widehat{\ell}} }) = 22 $.

- How is $ c_1 $ realized as a morphism:

    $ c_1: \operatorname{Pic}(X) \to H^2_\text{ét}(X; { {\mathbf{Z}}_{\widehat{\ell}} }(1)) $.

- What is an elliptic surface?

    $ \pi:X\to {\mathbf{P}}^1 $ surjective with generic fiber a smooth elliptic curve. Admit Weierstrass normal forms.

- Define the linear system $ {\left\lvert {L} \right\rvert} $ for $ L\in \operatorname{Pic}(X) $.

    $ {\mathbf{P}}H^0(L) $ or all $ L'\in \operatorname{Div}(X)^\mathsf{eff} $ with $ L'\sim L $ linearly equivalent.

- Define the base locus $ \mathrm{Bs}{\left\lvert {L} \right\rvert} $.

    The maximal closed subscheme of $ X $ contained in every $ D\in {\left\lvert {L} \right\rvert} $.

    Equivalently

    $$\mathrm{Bs}{\left\lvert {L} \right\rvert} = \bigcap_{s\in H^0(L)} Z(s)$$

- When does $ L $ induce a rational map?

    If $ h^0(L) > 1 $, inducing $ \phi_L: X\dashrightarrow{\mathbf{P}}H^0(L) {}^{ \vee } $ regular on $ X\setminus\mathrm{Bs}{\left\lvert {L} \right\rvert} $.

- What is the fixed-mobile decomposition $ L = M + F $ for $ L\in \operatorname{Pic}(X) $?

    $ F $ is the 1-dimensional part of $ \mathrm{Bs}{\left\lvert {L} \right\rvert} $.

    $ M\coloneqq L(-F) $ is the mobile part, is nef, satisfies $ M^2 \geq 0 $. Has a finite set of base points, contains the zero-dimensional locus of $ \mathrm{Bs}{\left\lvert {L} \right\rvert} $.

- What is a hyperelliptic curve in the context of K3s?

    $ C $ with a degree 2 morphism $ C\to {\mathbf{P}}^1 $.

    Usually $ g(C) \geq 2 $, $ \omega_C $ is bpf, and the canonical embedding $ \phi_{\omega_C} $ is non-constant.

- Are there hyperelliptic curves $ C $ with $ g(C) > 2 $?

    Yes, and $ C $ is hyperelliptic iff $ \omega_C $ is not hyperelliptic.

- What is a projectively normal morphism?

    The restriction $ H^0\left(\mathbf{P}^{g-1}, \mathcal{O}(k)\right) \longrightarrow H^0\left(C, \omega_C^k\right) $ is surjective for all $ k $.

- What is the adjunction formula for a curve $ C $ on a surface $ X $?

    $ \omega_C = (\omega_X \otimes{\mathcal{O}}(C))\mathrel{\Big|}_C $.

- What is the geometric genus of a reduced curve?

    $ g(\tilde C) $ where $ \nu:\tilde C\to C $ is the normalization.

- How are geometric and arithmetic genus related for a reduced curve?

    $ p_a(C) = g(C) + h^0(\nu_* {\mathcal{O}}_{\tilde C}/{\mathcal{O}}_C) $ where the latter sheaf is concentrated on $ C^{\mathrm{sing}} $.

- Give a lower bound for $ C^2 $ for an integral curve on a K3.

    $ C^2 \geq -2 $, using

    $$2 p_a(C)-2=\left(C . \omega_X \otimes \mathcal{O}(C)\right)\implies 2 p_a(C)-2=(C)^2$$

    and $ p_a(C) \geq 0 $.

- Discuss curves on a K3.

    By adjunction, $ C^2\geq -2 $. Automatically smooth, since $ g(C) \leq p_a(G) $ with equality iff $ C $ is smooth, and here $ p_a(C) = p_g(C) = 0 $. Any $ (-2){\hbox{-}} $curve is integral.

- When is a line bundle on a K3 ample?

    $ L $ is ample iff $ L\in {\mathcal{C}}_X \subset {\operatorname{NS}}(X)_{\mathbf{R}} $ (the positive cone) and $ (L.C) > 0 $ for every smooth rational curve $ C\cong {\mathbf{P}}^1 \subseteq X $.

- What is a nef line bundle $ L $ for a complete variety $ X $?

    $ (L.C) > 0 $ for all closed curves.

- What does it mean for a line bundle on a surface to be big and nef? Why care?

    $ L^2 > 0 $ and $ L $ is nef.

    Weaker than ample, but results for ample often still hold for just big and nef. Note that $ L^2 > 0 $ is not quite the right definition of "big" alone.

    Big and nef on a K3 implies effective.

- What is the generalization of Kodaira vanishing for projective surfaces (KodairaRamanujam vanishing theorem)?

    For $ X $ a smooth projective surface over $ \operatorname{ch}k = 0 $, if $ L $ is big and nef then

    $$H^{> 0}(L\otimes\omega_X) = 0$$

    Since $ H^1(\omega_X\otimes L) {}^{ \vee }\cong H^1(L {}^{ \vee }) $ by Serre duality, this is a vanishing theorem for $ L {}^{ \vee } $ with sufficient "positivity".

- Does Kodaira vanishing hold in positive characteristic?

    Generally no, see Mumford's normal projective surface as a counterexample, or Raynaud finds for any smooth projective surface $ X $ over $ k={ \overline{k} } $ an $ L\in \operatorname{Pic}(X) $ with $ H^1(L\otimes\omega_X) \neq 0 $.

    However it *does* hold for K3s, using $ H^1({\mathcal{O}}_X) = 0 $ and any big and nef $ L $ on a K3 is effective. This is explained by Deligne-Illusie for surfaces that lift to characteristic zero (which K3s do).

- Discuss $ L^2 $ and $ h^0(L) $ for $ L = {\mathcal{O}}_X(C) $, $ C $ a curve on a K3 $ X $.

    Let $ L= {\mathcal{O}}_X(C) $ for $ C\subseteq X $ a smooth irreducible curve of genus $ g $ on a K3 $ X $, then

    $$L^2 = 2g-2,\qquad h^0(L) = g+1$$

    Use adjunction to prove the first, and RR + Serre duality + $ H^0({ \left.{{L}} \right|_{{C}} }) \cong H^0(\omega_C) $ and the SES $ H^0(X; {\mathcal{O}}_X) \hookrightarrow H^0(X; L)\twoheadrightarrow H^0(C; { \left.{{L}} \right|_{{C}} }) $.

- Discuss projective embeddings of curves in K3s.

    For $ C\subseteq X $ smooth irreducible with $ g(C) \geq 1 $, $ L\coloneqq{\mathcal{O}}(C) $ is bpf and $ \phi_L: X\to {\mathbf{P}}^g $ restricts to the canonical embedding $ C\to {\mathbf{P}}^{g-1} $.

    For $ g=2 $, $ C $ is hyperelliptic so $ C\to {\mathbf{P}}^1 $ is degree 2. Since $ L^2 = 2 $ and $ L = \phi_L^* {\mathcal{O}}(1) $, $ \phi_L $ is degree 2, so $ X $ is a double cover of $ {\mathbf{P}}^2 $ over a degree 6 curve.

- Discuss the analog of Noether's theorem on projective normality of non-hyperelliptic curves.

    For $ C\subseteq X $ irreducible smooth non-hyperelliptic with $ g(C) > 2 $ on a K3 $ X $, $ L\coloneqq{\mathcal{O}}(C) $ is projectively normal, so $ \phi_L^* $ defines surjections $ H^0({\mathbf{P}}^g; {\mathcal{O}}(k)) \twoheadrightarrow H^0(X; L^k) $ for all $ k $.

- Discuss ampleness of line bundles on abelian varieties.

    If $ L\in \operatorname{Pic}(A) $ is ample in any characteristic, $ L^k $ is very ample for $ k\geq 3 $ independent of $ \dim A $.

- Discuss projective embeddings of K3s in arbitrary characteristic.

    If $ C\subseteq X $ is smooth irreducible and $ L\coloneqq{\mathcal{O}}(C) $, then for $ k\geq 2, g>2 $ or $ k\geq 3, g=2 $ the induced embedding $ \phi_{L^k}:X\to {\mathbf{P}}^n, n= k^2(g-1)+1 $ is birational onto its image.

- What is Fujita's conjecture?

    For $ L\in \operatorname{Pic}(X)^{\mathrm{amp}} $ for $ X $ smooth projective over $ {\mathbf{C}} $, $ L^k\otimes\omega_X $ is

    Globally generated for $ k\geq \dim(X) + 1 $ and

    Very ample for $ k\geq \dim(X) + 2 $.

    True for surfaces, a stronger version is true for K3s.

- Discuss $ \operatorname{Pic}(X)^{\mathrm{v.amp}} $ for $ X $ a K3.

    If $ L $ is ample and bpf, the $ L^k $ is very ample for $ k\geq 3 $.

    Consequence of a general result of Mumford, see 439.Thm.3.

- Discuss big and nef line bundles on K3s.

    $ H^1(L) = 0 $ by the Kodaira-Ramanujam vanishing theorem.

    If $ C $ is an irreducible curve with $ C^2 > 0 $, then $ {\mathcal{O}}(C) $ is big and nef.

- What is Ramanujam's lemma?

    If $ C $ is 1-connected and $ H^1({\mathcal{O}}_X) = 0 $, then $ H^1({\mathcal{O}}_X(-C)) =0 $.

    In characteristic zero, can drop $ H^1({\mathcal{O}}_X) = 0 $ assumption.

- Let $ L\in \operatorname{Pic}(X) $ be big and nef. Show that $ {\left\lvert {L} \right\rvert} $ is bpf.

    Decompose $ L = M + F $.

    Mobile $ \implies $ effective $ \implies $ nef, so $ M^2 \geq 0 $.

    If $ M^2 > 0 $, then $ M $ is big and nef so $ L $ has at most isolated base points.

    Check $ H^1(X; M) = 0 = H^1(X; L) $ so $ \chi(M) = h^0(M) = h^0(L) = \chi(L) $.

    By RR, $ M^2 = L^2 $, so $ 2(M.F) + F^2 = 0 $

    $ L $ nef $ \implies (M.F) + F^2 = L.F\geq 0 \implies M.F = F^2 = 0 $

    By RR on $ F\neq 0 $, reach a contradiction $ 1 = h^0(F) \geq \chi(F) $, so $ F=0 $.|

- What is the Base Point Free theorem?

    If $ L\in \operatorname{Pic}(X) $ is big and nef, then $ L^n $ is globally generated for some $ n $.

    Holds for smooth projective varieties over $ {\mathbf{C}} $ when $ L\otimes\omega_X {}^{ \vee } $ is big and nef.

- Discuss when $ L\in \operatorname{Pic}(X) $ for $ X $ a K3 is bpf.

    Sufficient condition: $ L^2 > 0 $ and $ {\left\lvert {L} \right\rvert} $ contains an irreducible curve.

- Discuss irreducible curves on a K3 in $ \operatorname{ch}k \neq 2 $.

    Always have $ C^2 > 0 $, $ {\left\lvert {{\mathcal{O}}_X(C)} \right\rvert} $ is bpf, its generic member $ C' $ is smooth.

    Either $ C' $ is hyperelliptic (so $ \deg \phi = 2 $) or not (then $ \deg \phi = 1 $ is birational)

- Discuss curves with $ C^2 = 0 $ on a K3.

    If $ L \in \operatorname{Pic}(X)^\mathrm{nef} $ is nontrivial and $ L^2=0 $ then $ L $ is bpf.

    Away from characteristics 2 and 3, $ \exists E $ a smooth irreducible elliptic curve with $ mE \in {\left\lvert {L} \right\rvert} $ for some $ m $.

    If $ L.C \geq 0 $ for all $ C\cong {\mathbf{P}}^1 $ then $ L\cong {\mathcal{O}}(m E) $ for some $ m $.

- Does the Fermat quartic contain any lines?

    Yes: $ {\left[ {x_0, \zeta_8 x_0, x_2, \zeta_8 x_2} \right]} $.

- When is a K3 surface elliptic?

    $ X $ is elliptic $ \iff \exists L\in \operatorname{Pic}(X) $ with $ L^2 =0 $ away from characteristic 2,3.

    Idea: pass from $ L $ with $ L^2 = 0 $ to a nef $ L' $ with $ (L')^2 = 0 $ through a series of reflections $ L\mapsto L + (L.C)C $ for $ C $ a $ (-2){\hbox{-}} $curve with $ L.C < 0 $.

- Discuss base points of complete linear systems on a K3.

    $ \operatorname{Bs}{\left\lvert {L} \right\rvert} = F $, i.e. $ {\left\lvert {L} \right\rvert} $ has no base points outside of its fixed part.

- Discuss big and nef line bundles $ L $ on a K3.

    Decompose $ L = M + F $ its fixed and mobile parts.

    If $ M $ is big, then $ L $ is bpf and $ F $ is trivial.

    If $ L $ is not bpf then $ L = {\mathcal{O}}(mE + C) $ with $ E $ smooth elliptic, $ C\cong{\mathbf{P}}^1 $, and $ m\geq 2 $.

- What is a polarized K3 of degree $ 2d $?

    A projective K3 $ X $ with $ L\in \operatorname{Pic}(X)^{\mathrm{amp}} $ which is primitive and satisfies $ L^2 = 2d $.

- What is the genus of a polarized K3?

    Write $ 2d = 2g-2 $, then $ g = g(C) $ for any $ C\in {\left\lvert {L} \right\rvert} $, we say $ (X, L) $ is a polarized K3 of genus $ g $.

- Do there exist K3s of arbitrary degree over $ k={ \overline{k} } $?

    Yes, for $ g\geq 3 $ over $ k={ \overline{k} } $ there exists K3s of degree $ 2g-2 $ in $ {\mathbf{P}}^g $.

    Idea: for $ g=3k $, take a generic quartic $ X $ in $ {\mathbf{P}}^3 $ containing a line $ \ell $.

    Let $ H $ be the hyperplane section and consider $ {\left\lvert {H-\ell} \right\rvert} $

    This defines an elliptic pencil $ {\left\lvert {E} \right\rvert} $.

    Consider $ L_k \coloneqq H + (k-1)E \in \operatorname{Pic}(X)^{\mathrm{v.amp}} $, for generic $ X $ it is primitive.

    Yields a polarized K3 of degree $ L_k^2 = 6k-2 $.

- Do there exist K3s of arbitrary degree over $ k\neq { \overline{k} } $?

    No: for $ k={ \mathbf{F} }_q $, the degree of a polarized K3 defined over $ k $ is bounded.

    Related to questions about rational points on the moduli of K3s.

- Discuss $ \operatorname{Pic}(X)^{\mathrm{amp}}\subseteq \operatorname{Pic}(X) $.

    An open subspace, i.e. ampleness is an open property.

- What is the Zariski decomposition of an effective divisor?

    $ D = P + N $ where $ P, N \in {\operatorname{NS}}(X)_{\mathbf{Q}} $ with $ P\in \operatorname{Nef}(X) $ the positive part and $ N = \sum a_i C_i $ effective (with $ a_i \in {\mathbf{Q}}_{\gt 0}) $ where $ P.C_i = 0 $ for all $ i $ and the intersection matrix $ (C_i . C_j) $ is negative definite.

- Discuss finite generation of the section ring $ R(X; L) $ for $ L\in \operatorname{Pic}(X) $.

    If $ X $ is a smooth surface and $ L $ is big, then $ R(X; L) $ is finitely generated iff $ P $ is semiample.

    $ R(; L) $ is finitely generated for any $ L\in \operatorname{Pic}(X) $ whatsoever for a K3.

- What is a Hodge structure of weight $ n $?

    For $ V\in   {}_{{\mathbf{C}}}{\mathsf{Mod}} $, a Hodge structure of weight $ n \in \mathbf{Z} $ on $ V $ is given by a direct sum decomposition of the complex vector space $ V_{\mathbf{C}} $

    $$V_{\mathbf{C}}=\bigoplus_{p+q=n} V^{p, q} \quad\text{such that} \quad \overline{V^{p, q}}=V^{q, p}$$

- What are isogenous Hodge structures?

    $ V, W $ with integral Hodge structures are isogenous iff $ V_{\mathbf{Q}}\cong W_{\mathbf{Q}} $.

- What are Hodge classes?

    For $ V $ a Hodge structure of even weight $ 2k $, the intersection $ V\cap V^{k, k} $.

- What are $ {\mathbf{Z}}(1), {\mathbf{Q}}(1) $?

    The Tate Hodge structure $ \mathbf{Z}(1) $ is the Hodge structure of weight $ -2 $ given by the free $ \mathbf{Z} $-module of rank one $ (2 \pi i) \mathbf{Z} $ (as a submodule of $ \mathbf{C} $ ) such that $ \mathbf{Z}(1)^{-1,-1} $ is one-dimensional. Similarly, one defines the rational Tate Hodge structure $ \mathbf{Q}(1) $.

- What is $ {\mathbf{Z}}(k) $ for $ k\in {\mathbf{Z}} $?

    $ {\mathbf{Z}}(-1) = {\mathbf{Z}}(1) {}^{ \vee }\coloneqq\mathop{\mathrm{Hom}}_{  {}_{ {\mathbf{C}}}{\mathsf{Mod}}}(V_{\mathbf{C}}, {\mathbf{C}}) $ and $ {\mathbf{Z}}(k) \coloneqq{\mathbf{Z}}(1){ {}^{ \scriptstyle\otimes_{{\mathbf{C}}}^{k} }  } $ whose underlying module is $ (2\pi i )^k {\mathbf{Z}} $.

    $ {\mathbf{Z}}(0) $ is the trivial Hodge structure of weight zero and rank one.

- What is the Tate twist $ V(k) $ for $ V $ a Hodge structure of weight $ n $?

    $ V(k) \coloneqq V\otimes_{\mathbf{C}}{\mathbf{Z}}(k) $, so $ V(k)^{p, q} = V^{p+k, q+k} $ which is weight $ n-2k $.

- What is the Hodge filtration?

    $ {\operatorname{Fil}}^i V_{\mathbf{C}}\coloneqq\bigoplus_{p\geq i} V^{p, q}_{\mathbf{C}} $, satisfies $ {\operatorname{Fil}}^p V_{\mathbf{C}}\oplus\overline{{\operatorname{Fil}}^q V_{\mathbf{C}}} = V_{\mathbf{C}} $ for all $ p+q=n+1 $.

- What is the Hodge structure associated to an arbitrary Hodge filtration?

    For $ {\operatorname{Fil}}^* V $ a Hodge filtration, define $ V^{p, n-p} \coloneqq{\operatorname{Fil}}^p V \cap\overline{{\operatorname{Fil}}^{n-p} V} $.

- Discuss the Hodge conjecture.

    The even part $ \bigoplus H^{2 k}(X, \mathbf{Q}) $ contains all algebraic classes, i.e. classes obtained as fundamental classes $ [Z] $ of subvarieties $ Z \subset X $. It is not difficult to see that $ [Z] $ is an integral class, i.e. that it comes from an element in $ H^{2 k}(X, \mathbf{Z}) $, and that it is contained in $ H^{k, k}(X) $.

    The Hodge conjecture asserts that the space spanned by those is determined entirely by the Hodge structure itself.

    (Hodge conjecture). For a smooth projective variety $ X $ over $ \mathbf{C} $ the subspace of $ H^{2 k}(X, \mathbf{Q}) $ spanned by all algebraic classes $ [Z] $ coincides with the space of Hodge classes, i.e.

    $$H^{2 k}(X; \mathbf{Q}) \cap H^{k, k}(X)=\left\langle{[Z] {~\mathrel{\Big\vert}~}Z \subset X}\right\rangle_{\mathbf{Q}}$$

- Discuss the status of the Hodge conjecture.

    Can fail for nonprojective hyperkhlers, integral version known not to hold.

    Known for $ (1, 1){\hbox{-}} $classes and $ (\dim X-1, \dim X - 1){\hbox{-}} $classes.

    Known for K3s, but not for products of K3s.

- What is a polarization and a polarized Hodge structure?

    A polarization of a rational Hodge structure $ V $ of weight $ n $ is a morphism of Hodge structures $ \psi: V \otimes V \rightarrow \mathbf{Q}(-n) $ such that its $ \mathbf{R} $-linear extension yields a positive definite symmetric form $ (v, w) \longmapsto \psi(v, C w) $ on the real part of $ V^{p, q} \oplus V^{q, p} $. Then $ (V, \psi) $ is called a polarized Hodge structure.

- What is a Hodge isometry?

    An isomorphism $ V_1 { \, \xrightarrow{\sim}\, }V_2 $ of Hodge structures compatible with their polarizations?

- What is the Hodge-Riemann pairing?

    Consider a rational (or integral) Khler class $ \omega \in H^2(X, \mathbf{Q}) $ on a smooth projective manifold $ X $. Then define on $ H^n(X, \mathbf{Q}) $ with $ n \leq d=\operatorname{dim}_{\mathbf{C}} X $ the following pairing:

    $$(v, w) \longmapsto(-1)^{n(n-1) / 2} \int_X v \wedge w \wedge \omega^{d-n}$$

- What is the primitive part of cohomology with respect to a rational Khler class $ \omega\in H^2(X; {\mathbf{Q}}) $?

    $$H^n(X, \mathbf{Q})_{\mathrm{p}}:=\operatorname{Ker}\left(\wedge \omega^{d-n+1}: H^n(X; \mathbf{Q}) \longrightarrow H^{2 d-n+2}(X; \mathbf{Q})\right)$$

    The Hodge-Riemann pairing on this defines a polarization, so primitive cohomology of a smooth complex projective variety over $ {\mathbf{C}} $ is always polarizable.

- How can one interpret Hodge structures as representations of the Deligne torus?

    Given $ V $ a Hodge structure of weight $ n $, define

    $$\begin{align}

    \rho: {\mathbf{C}}^{\times}&\to \operatorname{GL}(V_{\mathbf{R}}) \quad \in {\mathsf{Grp}}\

    z &\mapsto (v\mapsto z^p \overline{z}^q\cdot v), \quad v\in V^{p, q}

    .\end{align}$$

    $ {\mathbf{Q}}{\hbox{-}} $Hodge structures of weight $ n $ biject with algebraic representations $ \rho $ with an $ {\mathbf{R}}^{\times} $ action defined by $ \rho(t).v\coloneqq t^n.v $.

    The inverse construction sends $ \rho $ to $ V^{p, q}:=\left\{v \in V_{\mathbf{C}} \mathrel{\Big|}\rho_{\mathbf{C}}(z)(v)=\left(z^p \overline{z}^q\right) \cdot v \text { for all } z \in \mathbf{C}^*\right\} $ where $ \rho_{\mathbf{C}}: {\mathbf{C}}^{\times}\to \operatorname{GL}(V_{\mathbf{C}}) $ is a $ {\mathbf{C}}{\hbox{-}} $linear extension.

    Then $ \rho_{\mathbf{C}} $ splits into a sum of characters and $ V_{\mathbf{C}}= \bigoplus V^{p, q} $.

- What is the Deligne torus?

    $ T\coloneqq\mathop{\mathrm{Res}}_{{\mathbf{C}}/{\mathbf{R}}} {\mathbf{G}}_m({\mathbf{C}}) $, the real algebraic group where $ T(A) \coloneqq(A\otimes_{\mathbf{R}}{\mathbf{C}})^{\times} $ for $ A\in{ {}_{{\mathbf{R}}}  \mathsf{Alg}} $.

- What is the Tate Hodge structure, and what representation does it correspond to?\

    - $ {\mathbf{Q}}(1) $ which corresponds to

    $$\begin{align}

    {\mathbf{C}}^{\times}&\to {\mathbf{R}}^{\times}\

    z &\mapsto (z\overline{z})^{-1}

    .\end{align}$$

- What does the Kummer construction do?

    The Kummer construction allows one to pass from Hodge structures of weight one of a two-dimensional torus to the Hodge structure of weight two of its associated Kummer surface.

- Discuss bijections for Hodge structures of weight one.

    All of geometric origin, using that projective tori are abelian varieties:

    $$\begin{align}

    \left{{T/{\mathbf{C}}\text{ tori}}\right} &\rightleftharpoons{\mathbf{Z}}\operatorname{HS}^1 \

    \left{{T/{\mathbf{C}}\text{ abelian varieties}}\right} &\rightleftharpoons\left{{V\in {\mathbf{Z}}\operatorname{HS}^1 \text{ polarizable}}\right} \

    \left{{T/{\mathbf{C}}\text{ polarized abelian varieties}}\right} &\rightleftharpoons\left{{V\in {\mathbf{Z}}\operatorname{HS}^1 \text{ polarized}}\right}

    .\end{align}$$

- What is the global Torelli theorem for curves?

    Two smooth compact complex curves $ C $ and $ C^{\prime} $ are isomorphic if and only if there exists an isomorphism $ H^1(C, \mathbf{Z}) \simeq H^1\left(C^{\prime}, \mathbf{Z}\right) $ of integral Hodge structures respecting the intersection pairing (i.e. the polarization).

- What is a Hodge structure of K3 type?

    Weight 2 with

    $$\operatorname{dim}_{\mathbf{C}}\left(V^{2,0}\right)=1 \text { and } V^{p, q}=0 \text { for }|p-q|>2$$

- Is the Hodge structure on a K3 polarizable?

    If algebraic, always. If not, there are counterexamples.

- What is the transcendental part of a Hodge structure of K3 type?

    For an integral or rational Hodge structure of K3 type $ V $ one defines the transcendental lattice or transcendental part $ T $ as the minimal primitive sub-Hodge structure

    $$\begin{align}T \subset V \text { with } V^{2,0}=T^{2,0} \subset T_{\mathbf{C}}\end{align}$$

    The primitivity, i.e. the condition that $ V / T $ is torsion free, has to be added for integral Hodge structures, as otherwise minimality cannot be achieved.

- What is the transcendental lattice of a K3 surface?

    If $ V $ is the Hodge structure $ H^2(X, \mathbf{Z}) $ of a K3 surface $ X $, then

    $$\begin{align}

    V^{1,1} \cap V=H^{1,1}(X) \cap H^2(X, \mathbf{Z}) \simeq \mathrm{NS}(X) \simeq \operatorname{Pic}(X),

    \end{align}$$

    see Section 1.3.3, and $ T $ is called the transcendental lattice

    $$\begin{align}

    T(X) \subset H^2(X, \mathbf{Z})

    \end{align}$$

    of the K3 surface $ X $. It is usually considered as an integral Hodge structure.

- What is the lattice for $ H^1({\mathbf{C}}^2/\Gamma; {\mathbf{Z}}) $?

    $ U{ {}^{ \scriptscriptstyle\oplus^{3} }  } $; always has a Hodge structure of K3 type.

- What is the Kummer lattice?

    The unique even negative definite rank 16 lattice of discriminant $ 2^{16} $.

- Discuss the transcendental lattice of a K3 surface.

    $ T(X) = {\operatorname{NS}}(X)^\perp $, and if $ X $ is projective then $ T(X) $ is a polarizable irreducible Hodge structure.

    For nonprojective K3s, $ T(X) + {\operatorname{NS}}(X) \subseteq H^2(X; {\mathbf{Z}}) $ need not be direct and $ T(X) $ need not be irreducible nor polarizable.

- Describe the Hodge isometries of $ T(X) $ for a K3.

    Finite cyclic; any $ \alpha: T(X) { \, \xrightarrow{\sim}\, }T(X) $ satisfies $ \alpha^n=\operatorname{id} $ for some $ n $.

    If $ \rho(X) $ is odd, then $ T(X) = \left\{{\pm \operatorname{id}}\right\} \cong C_2 $.

- What is a CM field?

    $ K $ a purely imaginary quadratic extension of a totally real field, so $ K = K_0(\sqrt\alpha) $ with $ \sigma(\alpha)\in {\mathbf{R}}_{\gt 0} $ for every embedding $ \sigma: K_0 \hookrightarrow{\mathbf{C}} $.

- Discuss $ K\coloneqq K(T) \coloneqq{ \operatorname{End} }_{\mathbf{Q}\kern-0.5pt\operatorname{HS}}(T) $ for a K3.

    Always a number field. If $ T\in \mathbf{Q}\kern-0.5pt\operatorname{HS} $ is polarized irreducible of K3 type, the $ K $ is either totally real or a CM field.

    If CM, $ K = {\mathbf{Q}}(\eta) $ for some Hodge isometry $ \eta $.

    Any totally real field is realized as $ K(T) $ for $ T\in \mathbf{Q}\kern-0.5pt\operatorname{HS} $ polarized of K3 type.

- What are the Hodge and Mumford-Tate groups of $ V\in \mathbf{Q}\kern-0.5pt\operatorname{HS} $ polarizable?

    Identifying the Hodge structure with a representation $ \rho: {\mathbb{S}}\to \operatorname{GL}(V_{\mathbf{R}}) $, the smallest algebraic subgroups of $ \operatorname{GL}(V)/{\mathbf{Q}} $ with

    $$\begin{align}

    \rho(\mathbb{U}({\mathbf{R}})) \subseteq {\mathsf{Hodge}}(V)({\mathbf{R}}) \qquad \rho({\mathbb{S}}({\mathbf{R}})) \subseteq \operatorname{MT}(V)({\mathbf{R}})

    .\end{align}$$

    where $ \mathbb{U}\coloneqq\ker\qty{{\mathbb{S}}\xrightarrow{\operatorname{Nm}} {\mathbf{G}}_m({\mathbf{R}})} = \left\{{z\in {\mathbb{S}}({\mathbf{R}}) {~\mathrel{\Big\vert}~}z\overline{z} = 1}\right\} $.

    Related by a morphism

    $$\begin{align}

    {\mathsf{Hodge}}(V)\times {\mathbf{G}}_m &\to\operatorname{MT}(V) \

    (g, \mu) &\mapsto g\mu

    .\end{align}$$

    What does it mean for a K3 surface to have CM?

    $ {\mathsf{Hodge}}(T) $ is commutative, equivalently $ \dim_K(T) = 1 $. Implies that $ K $ is a CM field.

- What is the $ \ell{\hbox{-}} $adic algebraic monodromy group?

    For $ X\in {\mathsf{sm}}{\mathsf{Var}}^{\mathop{\mathrm{proj}}}_{/ {k}} $ with $ k $ finitely-generated of characteristic zero, the Zariski closure of the image of the Galois representation

    $$\begin{align}

    \rho*\ell: G*k &\to \operatorname{GL}(V), \qquad V = H^2*\text{ét}(X; { {\mathbf{Q}}*\ell }(1))

    .\end{align}$$

- What is the Mumford-Tate conjecture?

    Under the isomorphism $ H^2_\text{ét}(X; { {\mathbf{Q}}_\ell }(1)) { \, \xrightarrow{\sim}\, }H^2(X({\mathbf{C}}); {\mathbf{Q}}) \otimes{ {\mathbf{Q}}_\ell }(1) $, the identity component of the $ \ell{\hbox{-}} $adic monodromy group, $ \overline{\operatorname{im}\rho_\ell}^0 $, bijects with the Mumford-Tate group $ \operatorname{MT}(X) $.

    Proved for K3s over number fields.

- What does HRR say for surfaces?

    $ \chi(X) = {1\over 12}(c_1^2 + c_2) $, i.e. Noether's formula.

- What is the Hodge diamond for a surface?

    *(Answer was a figure; image not recovered.)*

- Discuss $ F_g $.

    Irreducible coarse moduli space of polarized complex K3s of genus $ g\geq 2 $.

    An open subset of a Shimura variety for $ {\operatorname{SO}}_{2, 19}({\mathbf{R}}) $

    Quasiprojective, $ \dim F_g = 19 $ for each $ g $.

- What is $ \kappa(X) $ for $ X $ a K3?

    $ \kappa(X) = 0 $, one of four such classes of minimal surfaces.

- Where do K3s fit into the classification of surfaces?

    Positively curved: del Pezzo

    Flat: K3s (generally CYs and hyperkahlers)

    Negatively curved: general type.

- What is the Hodge diamond of a K3?

    *(Answer was a figure; image not recovered.)*

- What are $ q(X), p_g(X), \beta^+(X), \chi(X), c_1^2(X), c_2(X) $ for a K3?

    $ q(X) = 0 $

    $ p_g(X) = 1 $

    $ \beta^+(X) = 3 $

    $ \chi(X) = 2 $

    $ c_1^2(X) = 0 $

    $ c^2(X) =24 $.

- Describe the lattice $ \Lambda_{{\mathsf{K}}3} $.

    $ \Lambda_{{\mathsf{K}}3} \coloneqq H{ {}^{ \scriptscriptstyle\oplus^{3} }  } \oplus E_8{ {}^{ \scriptscriptstyle\oplus^{2} }  } $, nondegenerate, even, rank 22, signature $ (3, 19) $.

- Define $ {\operatorname{NS}}(X) $.

    $${\operatorname{NS}}(X) \coloneqq H^{1, 1}(X) \cap H^{2}(X; {\mathbf{Z}})\subseteq H^2(X; {\mathbf{C}})$$

    .

- What is the transcendental sublattice?

    The smallest sublattice $ T(X) $ of $ H^2(X; {\mathbf{Z}}) $ containing a generator of $ H^{2, 0}(X) $.

    If $ X $ is projective, $ {\operatorname{NS}}(X) $ is nondegenerate, and $ T(X) = {\operatorname{NS}}(X)^\perp $.

- What is a marking on a K3?

    $ \phi: H^2(X; {\mathbf{Z}}) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3} $ an isometry.

- Define the period domain $ \mathbb{D} $. What is its dimension?

    $$\mathbb{D}\coloneqq\left\{{[\omega]\in {\mathbf{P}}(\Lambda_{{\mathsf{K}}3}\otimes_{\mathbf{Z}}{\mathbf{C}}) {~\mathrel{\Big\vert}~}\omega^2 = 0,\,\, \omega.\overline{\omega }> 0}\right\}$$

    20 dimensional $ {\mathbf{C}}{\hbox{-}} $manifold.

    For a polarized K3 $ (X, \phi) $, drops 1 dimension:

    $$\mathbb{D}_{2k} \coloneqq\left\{{[\omega]\in \mathbb{D}{~\mathrel{\Big\vert}~}\omega.h = 0}\right\}$$

    where $ h\in \Lambda_{{\mathsf{K}}3} $ is a fixed primitive class where $ \phi^{-1}(h)\in {\operatorname{NS}}(X)^{\mathrm{amp}} $. This is a bounded symmetric domain of type IV.

- Describe the period map of a single K3.

    Pick $ \omega\in H^{2, 0}(X) \subseteq H^2(X;{\mathbf{C}}) $ a nonvanishing holomorphic 2-form.

    Check the cup product satisfies $ \omega^2 = 0 $ and $ \omega.\overline{\omega }> 0 $.

    Extend a marking $ \phi $ to $ \phi_{\mathbf{C}}: H^2(X;{\mathbf{C}})\to \Lambda_{{\mathsf{K}}3}\otimes_{\mathbf{Z}}{\mathbf{C}} $.

    Check $ \operatorname{im}\phi_{\mathbf{C}}= \mathop{\mathrm{span}}_{\mathbf{C}}\left\{{\phi_{\mathbf{C}}(\omega)}\right\} $ is a line through the origin

    Thus $ \operatorname{im}\phi \in \mathbb{D} $.

- Why is the period domain used in moduli of K3s?

    Two K3s are isomorphic iff they admit markings defining the same point in $ \mathbb{D} $ by weak Torelli.

    Weak Torelli: $ X { \, \xrightarrow{\sim}\, }X' \iff $ there is an isometry $ H^2(X;{\mathbf{Z}}) { \, \xrightarrow{\sim}\, }H^2(X';{\mathbf{Z}}) $ whose $ {\mathbf{C}}{\hbox{-}} $linear extension preserves Hodge decompositions on $ H^2(X;{\mathbf{C}}) $.

- Describe the period map of a family of K3s.

    Let $ f:{\mathcal{X}}\to B $ be a flat family with fiber $ X $.

    Choosing a marking $ \phi: H^2(X;{\mathbf{Z}}) { \, \xrightarrow{\sim}\, }\Lambda_{{\mathsf{K}}3} $ extends to a sheaf morphism $ \phi_B: {\mathbf{R}}^2 f_*\underline{{\mathbf{Z}}}\to\underline{\Lambda_{{\mathsf{K}}3}} $ where the latter is a constant sheaf.

    Yields a holomorphic map $ B\to \mathbb{D} $.

- How is $ \mathbb{D} $ related to moduli of K3s?

    Local Torelli: for a marked K3 $ (X, \phi) $, the period map from the versal deformation space to $ \mathbb{D} $ is a local isomorphism.

    Surjectivity: every $ d\in \mathbb{D} $ is a period point for some marked K3.

    Thus almost a coarse moduli space: familes $ {\mathcal{X}}\to B $ yield $ B\to \mathbb{D} $ and points correspond to iso classes, but quotienting by change-of-marking yields a non-Hausdorff quotient since it does not act properly discontinuously.

- What are the two most widely studied classes of K3s?

    Sextic double planes: birational to $ X\to {\mathbf{P}}^1 $ a degree 2 cover branched over a sextic curve (equivalently a sextic hypersurface in $ {\mathbf{WP}}(1,1,1,3) $.)

    Quartic hypersurfaces:

    $ X\subseteq {\mathbf{P}}^3 $ a quartic hypersurface

    $ X\to {\mathbf{P}}^1 \times {\mathbf{P}}^1 $ a double cover branched over a bidegree $ (4, 4) $ curve.

    $ X\to C $ an elliptic fibration over the twisted cubic.

- What is a polarized K3 of degree $ 2k $?

    A pair $ (X, h \in {\operatorname{NS}}(X)^{\mathrm{amp}}) $ with $ h $ primitive and $ h^2 = 2k $.

- What is the strong Torellli theorem for polarized K3s?

    Every Hodge isometry $ \varphi: H^2(X;{\mathbf{Z}}) { \, \xrightarrow{\sim}\, }H^2(X';{\mathbf{Z}}) $ is induced by a unique isomorphism $ f:X { \, \xrightarrow{\sim}\, }X' $ with $ \phi = f^* $.

- Discuss degenerations of K3 surfaces?

    Any degeneration can be converted to a Kulikov model after a base change and birational modification.

- What is a semistable degeneration?

    $ \pi:{\mathcal{X}}\to \Delta $ with $ {\mathcal{X}} $ smooth and central fiber reduced normal crossings.

- What is the dual graph of a degeneration?

    Let $ S_0=\bigcup V_i $ be the central fibre in a semistable degeneration. Define the dual graph $ \Gamma $ of $ S_0 $ as follows: $ \Gamma $ is a simplicial complex whose vertices $ P_1, \ldots, P_r $ correspond to the components $ V_1, \ldots, V_r $ of $ S_0 $; the $ k $-simplex $ \left\langle P_{i_0}, \ldots, P_{i_k}\right\rangle $ belongs to $ \Gamma $ if and only if $ V_{i_0} \cap \cdots \cap V_{i_k} \neq \emptyset $.

- What is the classification of Kulikov models?

    Write $ \pi: {\mathcal{X}}\to \Delta $ for a semistable degeneration with $ \omega_{{\mathcal{X}}}\cong {\mathcal{O}}_{{\mathcal{X}}} $ where all components of $ {\mathcal{X}}_0 $ are Kahler.

    Type I: $ {\mathcal{X}}_0 $ is a smooth K3.

    No double curves, no triple points.

    Type II: $ {\mathcal{X}}_0 $ is a chain of elliptic ruled components with rational surfaces at each end where all double curves are smooth elliptic

    Double curves but no triple points

    Type III: $ {\mathcal{X}}_0 $ is rational surfaces meeting along rational curves forming cycles in each component and $ \Gamma $ is a triangulation of $ S^2 $.

    Triple points.

- Define the Neron-Severi group.

    $ {\operatorname{NS}}(X) \coloneqq\operatorname{Pic}(X) / \operatorname{Pic}^0(X) $, line bundles algebraically equivalent to zero.
