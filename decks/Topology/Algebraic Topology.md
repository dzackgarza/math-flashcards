---
title: "Topology::Algebraic Topology"
---

- Long Exact Sequence of a Pair $(A, B)$

    $$\ldots H_n(B) \to H_n(A) \to H_n(A,B) \to H_{n-1}(B) \ldots$$

    tags: math

- UCT: Change of Coefficients SES

    $${\displaystyle 0\to \mathrm{Tor}_\mathbb{Z}^0 (H_{i}(X;\mathbb{Z}), A)\,{\to }\,H_{i}(X;A)\to \mathrm{Tor}_\mathbb{Z}^1 (H_{i-1}(X;\mathbb{Z} ),A)\to 0}$$

    tags: math

- UCT: Cohomology and Homology SES

    $${ 0\to \mathrm{Ext}_{\mathbb{Z}}^{1}(H_{i-1}(X; \mathbb{Z}),A)\to H^{i}(X; A)\to \mathrm{Ext}_{\mathbb{Z}}^{0}(H_{i}(X; \mathbb{Z}),A) \to 0}$$

    tags: math

- Kunneth SES

    $$0\to \bigoplus_{i+j=k}H_{i}(X;R)\otimes _{R}H_{j}(Y;R)\to H_{k}(X\times Y;R)\to \bigoplus_{i+j=k-1}{\mathrm  {Tor}}_{R}^{1}(H_{i}(X;R),H_{j}(Y;R))\to 0$$

    tags: math

- Cohomology in terms of homology (nice case)

    $$
    H^i(X; \mathbb{Z}) = F(H_i(X; \mathbb{Z})) \times T(H_{i-1}(X; \mathbb{Z}))
    .$$

    tags: math, definition

- Homology in terms of cohomology (nice case)

    $$H_i(X; \mathbb{Z}) = F(H^i(X; \mathbb{Z})) \times T(H^{i+1}(X; \mathbb{Z}))$$

    tags: math

- Kunneth (nice case)

    $$
    H_{k}(X\times Y;F) \cong \bigoplus_{i+j=k}H_{i}(X;F)\otimes H_{j}(Y;F)
    .$$

    tags: math, definition

- Hom Table

    $$
    \begin{array}{c|c|c|c}
    Hom & Z_m & Z & Q \\\hline
    Z_n  & Z_d & 0 & 0 \\\hline
    Z   & Z_m & Z & Q \\\hline
    Q   & 0  & 0 & Q
    \end{array}
    $$

    tags: math

- Tor Table

    $$
    \begin{array}{c|c|c|c}
    Tor & Z_m & Z & Q \\\hline
    Z_n  & Z_d & 0 & 0 \\\hline
    Z   & 0  & 0 & 0 \\\hline
    Q   & 0  & 0 & 0
    \end{array}
    $$

    tags: math

- Ext Table

    $$
    \begin{array}{c|c|c|c}
    Ext & Z_m & Z    & Q \\\hline
    Z_n  & Z_d & Z_n   & 0 \\\hline
    Z   & 0  & 0    & 0 \\\hline
    Q   & 0  & A_p/Q & 0
    \end{array}
    $$

    tags: math

- $ H_* \mathbb{RP}^2 $

    $$  
    \RP^2 = [\mathbb{Z}, \mathbb{Z}_2, 0, 0, 0, 0\rightarrow ]
    .$$

    tags: definition
