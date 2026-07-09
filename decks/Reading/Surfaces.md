---
title: "Reading::Surfaces"
---

- For $ f: X\to X' $ a generically finite degree $ d $ morphism, describe $ f_* C $ for $ C $ an irreducible curve.

    $ f_*(C) = 0 $ if $ f(C) $ is a point

    $ f_*(C) = r C' $ if $ f(C) = C' $ is a curve where $ { \left.{{f}} \right|_{{C}} }:C\to C' $ is degree $ r $.

- What is the push-pull formula for divisors?

    $ f_* f^* D = \deg(f)\cdot D $.

- What is the local intersection multiplicity $ m_x(C \cap C') $?

    $ m_x(C \cap C') \coloneqq\dim_{\mathbf{C}}{{\mathcal{O}}_x \over \left\langle{f, g}\right\rangle} $ where $ f,g $ are the equations in $ {\mathcal{O}}_x $.

- When are $ C, C' $ transverse?

    $ m_x(C \cap C') = 1 \iff \left\langle{f, g}\right\rangle = {\mathfrak{m}}_x $, so $ f,g $ form a local coordinate system at $ x $.

- What is the ideal sheaf of $ C $?

    $ {\mathcal{O}}_X(-C) $.

- How is $ C . C' $ defined?

    $ C.C' = \sum_{x\in C\cap C'} {\mathfrak{m}}_x(C \cap C') = h^0(X; {\mathcal{O}}_{C\cap C'}) $.

- How is $ L.L' $ defined for $ L, L'\in \operatorname{Pic}(X) $?

    $ L.L' = \chi({\mathcal{O}}_X) - \chi(L^{-1}) - \chi((L')^{-1}) + \chi(L^{-1}\otimes(L')^{-1}) $.

- For $ C_1, C_2 $ curves, what is $ {\mathcal{O}}_X(C_1) . {\mathcal{O}}_X(C_2) $?

    $ {\mathcal{O}}_X(C_1) . {\mathcal{O}}_X(C_2) = C_1.C_2 $

- For $ C $ a smooth irreducible curve and $ L\in \operatorname{Pic}(X) $, what is $ {\mathcal{O}}_X(C) . L $?

    $ {\mathcal{O}}_X(C) . L = \deg{ \left.{{L}} \right|_{{C}} } $

- For $ f:X\to Y $ a generically degree $ d $ morphism, what is $ f^* D_1 . f^* D_2 $?

    $ f^* D_1 . f^* D_2 = \deg(f) (D_1.D_2) $.
