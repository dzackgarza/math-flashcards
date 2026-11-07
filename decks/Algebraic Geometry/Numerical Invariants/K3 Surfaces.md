---
title: "Algebraic Geometry::Numerical Invariants::K3 Surfaces"
---

::: {.front card-id="formula-mukai-vector-computation" tags="formula"}
For a coherent sheaf $E$ on a complex projective K3 surface, compute its Mukai vector using $r=\operatorname{rk}E,c_1(E),c_2(E)$.
:::

::: {.back card-id="formula-mukai-vector-computation"}
$$v(E)=\left(r,c_1(E),r+\frac12c_1(E)^2-c_2(E)\right).$$
:::

::: {.front card-id="formula-mukai-pairing-euler" tags="formula"}
For coherent sheaves $E,F$ on a complex projective K3 surface with Mukai vectors $v=(r,c,s)$ and $v'=(r',c',s')$, compute their Mukai pairing and $\chi(E,F)=\sum_i(-1)^i\dim\operatorname{Ext}^i(E,F)$.
:::

::: {.back card-id="formula-mukai-pairing-euler"}
$$\langle v,v'\rangle=cc'-rs'-r's,\qquad \chi(E,F)=-\langle v(E),v(F)\rangle.$$
:::

::: {.front card-id="card-dca3b01c137d5f80"}
What is the Hodge diamond of a K3?
:::

::: {.back card-id="card-dca3b01c137d5f80"}
For a complex K3 surface, $q=0$, $p_g=1$, and $h^{1,1}=20$.

$h^{p, q}(X) = 1$ for the corners: $h^{0,0} = h^{2,2} = 1$ and $h^{2,0} = h^{0,2} = 1$ since $\Omega^2_X\cong{\mathcal{O}}_X$. $h^{0, 1}(X) = h^{1,0}(X) = 0$, and $h^{2,1} = h^{1,2} = 0$ by Serre duality.

By HRR, Serre duality, and $\Omega_X \cong {\mathbf{T}}_X$,
$$2 h^0\left(\Omega_X\right)-h^1\left(\Omega_X\right)=\operatorname{ch}_2\left(\Omega_X\right)+4=4-\mathrm{c}_2\left(\Omega_X\right)=-20$$
so $h^1(\Omega_X) = 20$ since $h^0(\Omega_X) = h^{1,0}(X) = 0$. The Hodge diamond is
$$\begin{matrix}&&1&&\\&0&&0&\\1&&20&&1\\&0&&0&\\&&1&&\end{matrix}.$$
:::

::: {.front card-id="formula-k3-tangent-invariants" tags="formula"}
For a complex K3 surface $S$, compute $\chi(T_S)$ and $h^1(T_S)$.
:::

::: {.back card-id="formula-k3-tangent-invariants"}
$$\chi(T_S)=-20,\qquad h^1(T_S)=20.$$
:::

::: {.front card-id="formula-polarized-k3-sections" tags="formula"}
For an ample line bundle $L$ on a complex K3 surface with $L^2=2g-2$, compute $h^0(S,L)$.
:::

::: {.back card-id="formula-polarized-k3-sections"}
$$h^0(S,L)=g+1.$$
:::

::: {.front card-id="numerical-k3-basic-numbers" tags="formula"}
For a complex K3 surface $S$, give $b_2,e(S),\chi(\mathcal O_S),K_S^2$ and the signature of $H^2(S,\mathbb Z)$.
:::

::: {.back card-id="numerical-k3-basic-numbers"}
$$b_2=22,\qquad e(S)=24,\qquad \chi(\mathcal O_S)=2,\qquad K_S^2=0,\qquad \operatorname{sign}H^2(S,\mathbb Z)=(3,19).$$
:::

