---
title: "Quals::Topology"
---

- What is the Euler characteristic in terms of genus?

    $ \chi(\Sigma_g) = 2-2g $ if $ \Sigma_g $ is orientable, $ \chi(M_g) = 2-g $ if $ M_g $ is nonorientable.

    Puncturing reduces $ \chi $ by 1.

- $ \chi(\Sigma) = 2 \implies\cdots $

    $ g=0 $ so $ \Sigma \cong S^2 $.

- $ \chi(\Sigma) = 0 \implies\cdots $

    $ g=1 $ so $ \Sigma \cong T^1 $ (no boundary, orientable), or

    $ K $ the Klein bottle (no boundary, nonorientable).

    $ M $ the Mobius band (1 boundary, nonorientable), or

    $ S^2\setminus\left\{{ {\operatorname{pt}}_1, {\operatorname{pt}}_2 }\right\} \cong S^1\times I $ an annulus (2 boundaries), or

- $ \chi(\Sigma) = -2 \implies\cdots $

    $ g=2 $ so $ \Sigma\cong \Sigma_2 $ is a 2-holed torus, or

    $ S^2\setminus\left\{{ {\operatorname{pt}}_1,\cdots, {\operatorname{pt}}_4 }\right\} $.

- What is $ \chi(A\# B) $?

    $ \chi(A) + \chi(B) - 2 $

- Kunneth isomorphism (nice case)

    $$H_{k}(X\times Y;R) \cong \bigoplus_{i+j=k}H_{i}(X;R)\otimes H_{j}(Y;R)$$

- Prove $ \mathop{\mathrm{Hom}}_R(R, A) \cong A $.

    Take the map $ \Phi $ where $ f\mapsto f(1) $,

    Surjects by defining $ f_a(1) \coloneqq a $ for any $ a\in A $ and extending by $ f_a(n) \coloneqq na $

    Injects: if $ f(1) = g(1) = a $ then $ f(n) \coloneqq na $ and $ g(n) \coloneqq na $ so $ f\equiv g $.

- The tor complex between $ C_n $ and $ A $.

    $$\operatorname{Tor}^{\mathbf{Z}}_*(C_n, A) = (A/nA)\cdot t^0 \oplus A[n]\cdot t^1 \oplus \cdots$$

- The ext complex between $ C_n $ and $ A $.

    $$ \operatorname{Ext}^*_{\mathbf{Z}}(C_n, A) = A[n]\cdot t^0 \oplus (A/nA) \cdot t^1 \oplus \cdots$$

- Full tor complex table:

    E.g. top-left is $ \operatorname{Tor}_*^{\mathbf{Z}}(C_n, C_m) $.

    First row: $ C_n\otimes_{\mathbf{Z}}A = A/nA $ and $ \operatorname{Tor}_1^{\mathbf{Z}}(C_n, A) = A[n] $.

    Second row: $ {\mathbf{Z}}\otimes_{\mathbf{Z}}A = A $ and $ \operatorname{Tor}_1^{\mathbf{Z}}({\mathbf{Z}}, A) = 0 $ since $ {\mathbf{Z}} $ is projective.

    Third row: $ G\otimes_{\mathbf{Z}}{\mathbf{Q}}= {\mathbf{Q}}\otimes_{\mathbf{Z}}G = 0 $ for $ G $ any group

    Also $ \operatorname{Tor}(A, B) = \operatorname{Tor}(B, A) $. | $ \operatorname{Tor}_*^{\mathbf{Z}}(V, H) $ | $ C_m $ | $ {\mathbf{Z}} $ | $ {\mathbf{Q}} $ | |:---------------------|:-----------------------------------------------|:----------------------------------------------|:------------------------------------------| | $ C_n $ | $ C_m/nC_m \oplus C_m[n]t = C_d \oplus C_d t $ | $ {\mathbf{Z}}/n{\mathbf{Z}}\oplus {\mathbf{Z}}[n]t = C_n \oplus C_nt $ | $ {\mathbf{Q}}/n{\mathbf{Q}}\oplus {\mathbf{Q}}[n]t =0\oplus 0t $ | | $ {\mathbf{Z}} $ | $ {\mathbf{Z}}/m{\mathbf{Z}}+ {\mathbf{Z}}[m]t = C_m + C_m t $ | $ {\mathbf{Z}}+ 0t $ | $ {\mathbf{Q}}+ 0t $ | | $ {\mathbf{Q}} $ | $ {\mathbf{Q}}/n{\mathbf{Q}}+ {\mathbf{Q}}[n]t = 0 + 0t $ | $ {\mathbf{Q}}+ 0t $ | $ 0 + 0t $ |

- Homology of real projective space, $ H_* {\mathbf{RP}}^2 $

    $$H_* {\mathbf{RP}}^2 = {\mathbf{Z}}\cdot t^0 + C_2 \cdot t^1$$
