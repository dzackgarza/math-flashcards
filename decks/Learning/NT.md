---
title: "Learning::NT"
---

- Define a DVR

    A PID with a unique nonzero prime, and thus a uniformizer: any $ \pi $ with $ v(\pi) = 1 $.

- Give an example of a local ring which is not a DVR.

    $ R = k{\llbracket x^2, x^3 \rrbracket  } $ is local with $ {\mathfrak{m}}_R = \left\langle{x^2, x^3}\right\rangle $, so not a PID.

- Discuss valuation rings for $ K $ a DVR.

    $ R = \left\{{x\in K {~\mathrel{\Big\vert}~}v(x) \geq 0}\right\} $

    Has unique maximal ideal $ {\mathfrak{m}}_R = \left\{{\in K {~\mathrel{\Big\vert}~}v(x) > 0}\right\} = \left\langle{\pi}\right\rangle $ for $ \pi $ a uniformizer with $ v(\pi) = 1 $.

    Always a PID and $ \operatorname{Spec}R = \left\{{{\mathfrak{m}}_R}\right\} $.

- Define a Dedekind domain.

    Noetherian, integral, integrally closed, with $ \operatorname{Spec}R = \operatorname{mSpec}R $.

    Implies every localization is a DVR.

- Why are complete DVRs $ K $ with valuation ring $ A $ great?

    Every $ x\in \operatorname{ff}(A) $ is of the form $ \sum_{n\geq n_0} s_n \pi^n $ with $ s_n\in S\subset A $ a set of representatives of $ A/{\mathfrak{m}} $.

    Compare to $ x = \sum a_n p^n $ with $ 0\leq a_n\leq p-1 $ for $ { {\mathbf{Z}}_{\widehat{p}} } $.

    If $ [L: \operatorname{ff}(A)] = n $ then $ B \coloneqq \operatorname{cl}^{\mathrm{int}}_L(A) $ is a DVR and $ B \in   {}_{A}{\mathsf{Mod}}^{{\mathrm{free}}, \operatorname{rank}=n} $ and complete wrt the topology induced by $ B $.

- Define $ {\left\lvert {a\over b} \right\rvert}_p $.

    $ \qty{1\over p}^{v_p(a/b)} $.

- What is the ultrametric triangle inequality?

    $ {\left\lvert {x+y} \right\rvert}_p \leq \max\left\{{{\left\lvert {x} \right\rvert}_p, {\left\lvert {y} \right\rvert}_p}\right\}\leq {\left\lvert {x} \right\rvert}_p + {\left\lvert {y} \right\rvert}_p $.

    $ v_p(x+y) \geq \min\left\{{v_p(x), v_p(y)}\right\} $.

- Describe $ { {\mathbf{Z}}_{\widehat{p}} } $ in terms of valuations.

    $ \left\{{x\in {\mathbf{Q}}{~\mathrel{\Big\vert}~}v_p(x) \geq 0}\right\} $ or $ \left\{{x\in {\mathbf{Q}}{~\mathrel{\Big\vert}~}{\left\lvert {x} \right\rvert}_p \leq 1}\right\} $.

    Explicitly $ { {\mathbf{Z}}_{\widehat{p}} }\coloneqq\left\{{{a\over b} \in {\mathbf{Q}}{~\mathrel{\Big\vert}~}p\nmid b}\right\} = {\mathbf{Z}} { \left[ \scriptstyle {{1\over \ell} {~\mathrel{\Big\vert}~}\ell \neq p} \right] }  $.

- Discuss ring-theoretic properties of $ { {\mathbf{Z}}_{\widehat{p}} } $.

    Has maximal ideal $ \left\langle{p}\right\rangle = \left\{{{a\over b} {~\mathrel{\Big\vert}~}p\nmid a}\right\} $

    Every element in $ { {\mathbf{Z}}_{\widehat{p}} }\setminus\left\langle{p}\right\rangle $ is a unit, so this is a local ring with residue field $ { \mathbf{F} }_p $.

    Take completion to get $ { {\mathbf{Z}}_{\widehat{p}} } $.

- Explicitly describe elements in $ { {\mathbf{Z}}_{\widehat{p}} } $.

    $ { {\mathbf{Z}}_{\widehat{p}} }= \left\{{\sum a_i p^i {~\mathrel{\Big\vert}~}0 \leq a_i \leq p-1}\right\} $

    Equivalently $ { {\mathbf{Z}}_{\widehat{p}} }= \cocolim_n {\mathbf{Z}}/\left\langle{p^n}\right\rangle $ which contains sequences $ \mathbf{a} = {\left[ {a_0, a_0 + a_1 p, a_0 + a_1 p + a_2 p^2, \cdots} \right]} $ of partial sums so that $ \mathbf{a}_n \operatorname{mod}p^n \cong \mathbf{a}_{n-1} $.

- For a DVR $ A $, setting $ {\left\lvert {{-}} \right\rvert}_v \coloneqq a^{v_p({-})} $, why should one choose $ a \coloneqq 1/q $ for $ q \coloneqq{\sharp}A/p $?

    For the Haar measure, satisfies $ \mu(xT) = {\left\lvert {x} \right\rvert} \mu(T) $.

- Interpret local fields geometrically.

    For $ X $ a variety with coordinate ring $ R $, points $ p\in X $ correspond to $ p\in \operatorname{Spec}R $ and localizing $ L_p R $ yields the ring of functions with no pole at $ p $.

    E.g. $ L_3 {\mathbf{Z}} $ allows fractions with no 3 in the denominator.

- Discuss the AKLB setup when $ L/K $ is finite and $ B = \operatorname{cl}^{\mathrm{int}}_L(A) $ is a DVR.

    The extension satisfies $ {\mathfrak{m}}_A B = {\mathfrak{m}}_B^e $ with $ [\kappa_B : \kappa_A] = f $ and $ n \coloneqq[L: K] = ef $. Two extreme cases:

    If $ e=1, f=n $ (so no ramification) and $ \kappa_B = \kappa_A(\overline{\alpha}) $ is simple (e.g. if the residue field extension is separable) then $ B $ is monogenic: $ B\cong A[x]/\left\langle{f}\right\rangle $ where $ f $ is the minimal polynomial over $ K $ of a lift of $ \overline{\alpha} $ to $ B $.

    If $ e=n, f=1 $ then $ B = A[x]/\left\langle{f}\right\rangle $ where $ f $ is the minimal polynomial of $ \pi_B $

    Useful: rings of integers of extensions become much easier to express! Ramification and splitting is simpler because of the single prime.

- What is the decomposition group?

    For $ L/K $ Galois and $ p\in \operatorname{Spec}A $, write $ pB = \prod_{i\leq g} q_i^e $ where $ q_i\in \operatorname{Spec}B $, all $ e $ the same since Galois, and $ f \coloneqq[B/b_i : A/p] $. Then $ D_{q_i}\coloneqq{\operatorname{Stab}}_{{ \mathsf{Gal}}(L/K)}(q_i) $, elements of Galois fixing $ q_i $.

    All $ D_{q_i} $ are conjugate in $ { \mathsf{Gal}}(L/K) $ and thus the corresponding fields $ K_{D_{q_i}} $ are isomorphic.

    Not necessarily normal.

- Why is the decomposition group useful?

    Have $ n=efg $ and $ [{ \mathsf{Gal}}(L/K): D_{q_i}] = g \implies [K_{D_{q_i}} : K] = g $.

    All conjugate, so suffices to consider a single $ P\mathrel{\Big|}p $ and the tower:

    Precisely the condition to induce a map on residue fields: $ \sigma \in D\implies \overline{\sigma}: B/P\to B/P $ where $ b+P\mapsto \sigma(b) + P $, well-defined since $ \sigma $ fixed $ P $.

    Also fixes $ A $, so descends to the local Galois group, yielding a group morphism $ D\twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B / \kappa_A) $.

- What is a **normal** extension $ L/K $?

    If $ \alpha\in L $ then all Galois conjugates are again in $ L $, so $ L $ contains all roots of $ {\operatorname{minpoly}}_K(\alpha) $.

- What is the inertia group?

    $ T_P \coloneqq\ker\qty{D_P\twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B/\kappa_A)} $.

    Idea: elements in Galois that make sense on residue fields and satisfy $ \sigma(b) = b \operatorname{mod}P $ for all $ b\in B $.

- Discuss the inertia/decomposition SES.

    $ T_P \hookrightarrow D_P \twoheadrightarrow\mathop{\mathrm{Aut}}(\kappa_B/\kappa_A) $.

- Why care about inertia/decomposition groups?

    Factors $ L/K $ into a tower of extensions where all splitting happens first and all ramification happens last:

- Describe the filtration on $ D/T \cong { \mathsf{Gal}}(\widehat{L} / \widehat{K}) $.

    $ \sigma\in G_i \iff \sigma $ is the identity on $ \widehat{B}/P^{i+1} $.

    What this is doing: write $ B\ni b = \sum b_i \pi^i $, then

    $ \sigma \in T = G_0 \iff \sigma(b) = b_0 + { \mathsf{O}}(\pi) $

    $ \sigma\in G_1\iff \sigma(b) = b_0 + b_1\pi + { \mathsf{O}}(\pi^2) $

    Allowed to change coefficients $ k\geq i+1 $.

    Terminates, so $ 1 = G_i {~\trianglelefteq~}\cdots {~\trianglelefteq~}G_1 {~\trianglelefteq~}G_0 = D $.

- Describe tame and wld ramification

    Locally:

    Globally:

- What is the profinite completion?

    Regard objects $ X $ in $ \mathsf{pro}\mathsf{C} $ as sequences $ X = \left\{{X_\alpha}\right\}_{\alpha\in I} $ where $ X_\alpha\in \mathsf{C} $.

    Let $ {\mathsf{Spaces}}_{{\mathsf{Fin}}{\mathsf{Grp}}} $ be the full subcategory of spaces with $ \pi_i \in {\mathsf{Fin}}{\mathsf{Grp}} $.

    The profinite completion of $ X\in{\mathsf{Spaces}} $ is the left-adjoint to the inclusion $ \mathsf{pro}{\mathsf{Spaces}}_{{\mathsf{Fin}}{\mathsf{Grp}}} \to \mathsf{pro}{\mathsf{Spaces}} $.

- What are Witt vectors?

    For a $ K\in { {}_{{ \mathbf{F} }_p}  \mathsf{Alg}}^{\mathrm{perf}} $, the unique lift $ W(K)\in { {}_{{ {\mathbf{Z}}_{\widehat{p}} }}  \mathsf{Alg}} $ which is $ p{\hbox{-}} $adically complete and $ p{\hbox{-}} $torsionfree.

    $ W({ \mathbf{F} }_p) = { {\mathbf{Z}}_{\widehat{p}} } $.

- What is the ghost map for Witt vectors?

    $ w: W_r(A)\to A{ {}^{ \scriptscriptstyle\times^{r} }  } $ where $ \mathbf{x}\mapsto {\left[ {w_0(x_0), w_1(x_0, x_1) \cdots, w_{r-1}(x_0,\cdots, x_{r-1})} \right]} $ where $ w_i(x_0,\cdots, x_n) \coloneqq x_0^{p^n} + p x_1^{p^{n-1}} + \cdots + p^n x_n $.

- What is tilting?

    For $ A\in {}_{{\mathbf{Z}}}  \mathsf{Alg} $ $ \pi{\hbox{-}} $adically complete for some $ \pi\mathrel{\Big|}p $, the tilt is $ A^\flat \coloneqq\cocolim_{\operatorname{Frob}} A/pA $ where $ \operatorname{Frob}: A/pA \to A/pA $.

    Always have $ A^\flat \in { {}_{{ \mathbf{F} }_p}  \mathsf{Alg}}^{\mathrm{perf}} $.

    Think of $ \mathbf{x}\in A^\flat \cong \cocolim_{x\mapsto x^p} A $ as $ x_{i+1}^p =x_i $.

- What is $ {\mathbf{A}}_\inf(A) $?

    $ {\mathbf{A}}_\inf(A) \coloneqq W(A^\flat) $.

    Interpolates between characteristic zero geometry of $ A $ and characteristic $ p $ geometry of $ A^\flat $.

    $ A $ may not have a Frobenius, but $ {\mathbf{A}}_\inf(A) $ does.

- What is a perfectoid ring $ S $?

    $ S $ is $ \pi{\hbox{-}} $adically complete for some $ \pi\in S $ with $ \pi^p \mathrel{\Big|}p $

    $ \operatorname{Frob}: S/pS \to S/pS $ is surjective.

    $ \ker \qty{{\mathbf{A}}_\inf(S) \xrightarrow{\theta }S} = \left\langle{\xi}\right\rangle $ is principal.

    Precisely the rings so that $ \theta $ is a pro-infinitesimal 1-parameter degeneration, deforming $ S $ in a preferred $ \xi $ direction.

    If $ S $ is characteristic $ p $, then $ S $ is perfect iff perfectoid.

- What is $ A_{{\mathrm{crys}}} $?

    Setup: $ K = { {\mathbf{C}}_p }, S\coloneqq{\mathcal{O}}_K, A_\inf \coloneqq{\mathbf{A}}_\inf({\mathcal{O}}_K) $.

    $ A_{\mathrm{crys}} $ is the $ p{\hbox{-}} $adic completion of the subalgebra $ \left\langle{\xi^m/m!}\right\rangle \leq A_\inf{ \left[ { \scriptstyle \frac{1}{p} } \right] } $ .

    Universal $ p{\hbox{-}} $adically complete divided power thickening of $ {\mathcal{O}}_K $ over $ { {\mathbf{Z}}_{\widehat{p}} } $.

- What is $ B_{\mathrm{crys}} $ and $ B_{\mathrm{crys}}^+ $? $ B_\mathrm{dR} $?

    $ B^+_{\mathrm{crys}}\coloneqq A_{\mathrm{crys}}{ \left[ { \scriptstyle \frac{1}{p} } \right] } $ and $ B_{\mathrm{crys}}= B_{\mathrm{crys}}^+{ \left[ { \scriptstyle \frac{1}{\mu} } \right] } $

    $ B_\mathrm{dR}^+ $ is the $ \xi{\hbox{-}} $adic completion of $ B^+_{\mathrm{crys}} $ and $ B_\mathrm{dR}= \operatorname{ff}B^+_\mathrm{dR} $.

    $ B^+_\mathrm{dR} $ is a DVR with residue field $ { {\mathbf{C}}_p } $.

- What is the etale homotopy type of a scheme $ X $?

    For $ X $ quasiprojective, $ {\mathsf{ho}}\text{Ét}(X) \coloneqq\left\{{\pi_0 { {\left\lvert {{ \mathcal{N}({{\mathcal{U}}}) }} \right\rvert} }}\right\}_{{\mathcal{U}}\in X_\text{ét}} \in \mathsf{pro}{\mathsf{Spaces}} $

    For general $ X $, replace $ { \mathcal{N}({{\mathcal{U}}}) } $ by hypercovers, and $ X_\text{ét} $ only provides a left-filtering category up to homotopy, so generally in $ {\mathsf{ho}}\mathsf{pro}{\mathsf{Spaces}} $.

    Since $ \left\{{{ {\left\lvert {{ \mathcal{N}({{\mathcal{U}}}) }} \right\rvert} }}\right\}_{{\mathcal{U}}\in X_\text{ét}} $ is a cofibrant replacement, $ {\mathsf{ho}}\text{Ét}({-}) = {\mathbf{L}}\pi_0({-}) $ is a derived functor.

- What is the sheaf-theoretic definition of a DM stack?

    An etale sheaf $ F\in {\mathsf{Sh}}_\text{ét} $ which admits a surjective etale morphism $ {\textstyle\coprod}\operatorname{Spec}R_i\to F $.

- What is an etale sheaf?

    A full subcategory $ {\mathsf{Sh}}_\text{ét}\coloneqq{\mathsf{Sh}}_\text{ét}(\mathsf{CAlg}_{/ {{\mathbf{Z}}}}) \leq {\mathsf{Fun}}(\mathsf{CAlg}_{/ {{\mathbf{Z}}}}, {\mathsf{Spaces}}) $ where if $ R\to S $ is etale anred faithfully flat, there is a weak equivalence $ F(R) \to { \operatorname{Tot} }F(S{ {}^{ \scriptstyle\otimes_{R}^{\bullet} }  }) $.

- What is the section conjecture?

    For $ X $ smooth hyperbolic and proper over $ k $, there is a set bijection

    $$X(k)  { \, \xrightarrow{\sim}\, }\pi_0 \mathsf{pro}{\mathsf{Spaces}}_{/ {\operatorname{Spec}k}}(\text{Ét}(\operatorname{Spec}k) \to \text{Ét}(X))  { \, \xrightarrow{\sim}\, }\text{Ét}(X_{\overline{k}})^{h G_k},$$

    regarding the RHS as homotopy classes of morphisms.

    Thus conjecturally $ X(k) { \, \xrightarrow{\sim}\, }\text{Ét}(X_{\overline{k}})^{h G_k} $ can be recovered from homotopy fixed points.

    This is a section since morphisms are triangles over $ \text{Ét}(\operatorname{Spec}k) $, so such maps are sections to the structure morphism $ \text{Ét}(X)\to \text{Ét}(\operatorname{Spec}k) $.

- What inspires the anabelian conjectures?

    For $ K\coloneqq{\mathbf{Q}}(\sqrt a), L\coloneqq{\mathbf{Q}}(\sqrt b) $,

    $${ \mathsf{Gal}}(K) \cong { \mathsf{Gal}}(L) \iff K\cong L \iff a=b\in {\mathbf{Q}}^{\times}/{ {{\mathbf{Q}}^{\times}}_{\scriptscriptstyle \square} }$$

    so $ {\mathsf{Sch}}(\operatorname{Spec}L  { \, \xrightarrow{\sim}\, }\operatorname{Spec}K) \cong {\mathsf{ho}}\mathsf{pro}{\mathsf{Spaces}}(\text{Ét}(L) { \, \xrightarrow{\sim}\, }\text{Ét}(K)) $.

    For $ K, L\in \mathsf{Field}_{/ {{\mathbf{Q}}}} $, $ \mathsf{Field}_{/ {{\mathbf{Q}}}}(K  { \, \xrightarrow{\sim}\, }L) \cong {\mathsf{Top}}{\mathsf{Grp}}(G_K { \, \xrightarrow{\sim}\, }_{\mathop{\mathrm{Out}}} G_L) $.

- What are the anabelian conjectures?

    Existence of $ \mathsf{An}_k \leq {\mathsf{Sch}}_{/ {k}} $ a full subcategory including smooth hyperbolic curves, closed under taking fibrations with base and fiber in $ \mathsf{An}_k $, and

    $${\mathsf{Sch}}(X_1\to X_2 {~\mathrel{\Big\vert}~}\text{open image}) \cong {\mathsf{Top}}{\mathsf{Grp}}_{/ {G_k}}(\pi_1 X_1 \to \pi_1 X_2 {~\mathrel{\Big\vert}~}\text{open morphisms})$$

- Describe geometric Langlands.

    $ \rho \in {\mathcal{X}}(\pi_1\Sigma_g, G)\leadsto $ a flat connection $ \nabla_\rho $ on a principal $ G{\hbox{-}} $bundle over $ C $

    Irreducible such connections $ \rightleftharpoons $ $ R\in    {}_{\mathcal{D}}{\mathsf{Mod}} ({\mathsf{Bun}}_{{}^L G}) $.
