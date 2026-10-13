---
title: "Quals::Topology"
---

::: {.front card-id="card-3a917df8f423b44f"}
What is the Euler characteristic in terms of genus?
:::

::: {.back card-id="card-3a917df8f423b44f"}
$ \chi(\Sigma_g) = 2-2g $ if $ \Sigma_g $ is orientable, $ \chi(M_g) = 2-g $ if $ M_g $ is nonorientable.

Puncturing reduces $ \chi $ by 1.
:::

::: {.front card-id="card-9e8114fdc2e6992d"}
$ \chi(\Sigma) = 2 \implies\cdots $
:::

::: {.back card-id="card-9e8114fdc2e6992d"}
$ g=0 $ so $ \Sigma \cong S^2 $.
:::

::: {.front card-id="card-89e50babfc15999b"}
$ \chi(\Sigma) = 0 \implies\cdots $
:::

::: {.back card-id="card-89e50babfc15999b"}
$ g=1 $ so $ \Sigma \cong T^1 $ (no boundary, orientable), or

$ K $ the Klein bottle (no boundary, nonorientable).

$ M $ the Mobius band (1 boundary, nonorientable), or

$ S^2\setminus\left\{{ {\operatorname{pt}}_1, {\operatorname{pt}}_2 }\right\} \cong S^1\times I $ an annulus (2 boundaries), or
:::

::: {.front card-id="card-ea0ba476b1570b73"}
$ \chi(\Sigma) = -2 \implies\cdots $
:::

::: {.back card-id="card-ea0ba476b1570b73"}
$ g=2 $ so $ \Sigma\cong \Sigma_2 $ is a 2-holed torus, or

$ S^2\setminus\left\{{ {\operatorname{pt}}_1,\cdots, {\operatorname{pt}}_4 }\right\} $.
:::

::: {.front card-id="card-e6106ff75ead6897"}
What is $ \chi(A\# B) $?
:::

::: {.back card-id="card-e6106ff75ead6897"}
$ \chi(A) + \chi(B) - 2 $
:::

::: {.front card-id="card-6ad5dd725c330752"}
Kunneth isomorphism (nice case)
:::

::: {.back card-id="card-6ad5dd725c330752"}
$$H_{k}(X\times Y;R) \cong \bigoplus_{i+j=k}H_{i}(X;R)\otimes H_{j}(Y;R)$$
:::

::: {.front card-id="card-0a2b571ba3db3475"}
Prove $ \mathop{\mathrm{Hom}}_R(R, A) \cong A $.
:::

::: {.back card-id="card-0a2b571ba3db3475"}
Take the map $ \Phi $ where $ f\mapsto f(1) $,

Surjects by defining $ f_a(1) \coloneqq a $ for any $ a\in A $ and extending by $ f_a(n) \coloneqq na $

Injects: if $ f(1) = g(1) = a $ then $ f(n) \coloneqq na $ and $ g(n) \coloneqq na $ so $ f\equiv g $.
:::

::: {.front card-id="card-455916a5a5f17b7d"}
The tor complex between $ C_n $ and $ A $.
:::

::: {.back card-id="card-455916a5a5f17b7d"}
$$\operatorname{Tor}^{\mathbf{Z}}_*(C_n, A) = (A/nA)\cdot t^0 \oplus A[n]\cdot t^1 \oplus \cdots$$
:::

::: {.front card-id="card-9bf5130224135f26"}
The ext complex between $ C_n $ and $ A $.
:::

::: {.back card-id="card-9bf5130224135f26"}
$$ \operatorname{Ext}^*_{\mathbf{Z}}(C_n, A) = A[n]\cdot t^0 \oplus (A/nA) \cdot t^1 \oplus \cdots$$
:::

::: {.front card-id="card-c32162ef36bb98b4"}
Full tor complex table:
:::

::: {.back card-id="card-c32162ef36bb98b4"}
E.g. top-left is $ \operatorname{Tor}_*^{\mathbf{Z}}(C_n, C_m) $.

First row: $ C_n\otimes_{\mathbf{Z}}A = A/nA $ and $ \operatorname{Tor}_1^{\mathbf{Z}}(C_n, A) = A[n] $.

Second row: $ {\mathbf{Z}}\otimes_{\mathbf{Z}}A = A $ and $ \operatorname{Tor}_1^{\mathbf{Z}}({\mathbf{Z}}, A) = 0 $ since $ {\mathbf{Z}} $ is projective.

Third row: $ G\otimes_{\mathbf{Z}}{\mathbf{Q}}= {\mathbf{Q}}\otimes_{\mathbf{Z}}G = 0 $ for $ G $ any group

Also $ \operatorname{Tor}(A, B) = \operatorname{Tor}(B, A) $. | $ \operatorname{Tor}_*^{\mathbf{Z}}(V, H) $ | $ C_m $ | $ {\mathbf{Z}} $ | $ {\mathbf{Q}} $ | |:---------------------|:-----------------------------------------------|:----------------------------------------------|:------------------------------------------| | $ C_n $ | $ C_m/nC_m \oplus C_m[n]t = C_d \oplus C_d t $ | $ {\mathbf{Z}}/n{\mathbf{Z}}\oplus {\mathbf{Z}}[n]t = C_n \oplus C_nt $ | $ {\mathbf{Q}}/n{\mathbf{Q}}\oplus {\mathbf{Q}}[n]t =0\oplus 0t $ | | $ {\mathbf{Z}} $ | $ {\mathbf{Z}}/m{\mathbf{Z}}+ {\mathbf{Z}}[m]t = C_m + C_m t $ | $ {\mathbf{Z}}+ 0t $ | $ {\mathbf{Q}}+ 0t $ | | $ {\mathbf{Q}} $ | $ {\mathbf{Q}}/n{\mathbf{Q}}+ {\mathbf{Q}}[n]t = 0 + 0t $ | $ {\mathbf{Q}}+ 0t $ | $ 0 + 0t $ |
:::

::: {.front card-id="card-47515f1125a40ca3"}
Homology of real projective space, $ H_* {\mathbf{RP}}^2 $
:::

::: {.back card-id="card-47515f1125a40ca3"}
$$H_* {\mathbf{RP}}^2 = {\mathbf{Z}}\cdot t^0 + C_2 \cdot t^1$$
:::
