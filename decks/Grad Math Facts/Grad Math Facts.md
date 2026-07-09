---
title: "Grad Math Facts::Grad Math Facts"
---

- $f^{-1} \left( \coprod U_i \right) =_? \coprod_i f^{-1} U_i$?

    Yes:
    $$
    \begin{align}
    f^{-1}\left[\bigcup_{i \in I} Y_{i}\right] &=\left\{x \in X \mid f(x) \in \bigcup_{i \in I} Y_{i}\right\} \\
    &=\left\{x \in X \mid \exists i \in I \text { such that } f(x) \in Y_{i}\right\} \\
    &=\bigcup_{i \in I}\left\{x \in X \mid f(x) \in Y_{i}\right\} \\
    &=\bigcup_{i \in I} f^{-1}\left[Y_{i}\right]
    \end{align}
    $$

    tags: misc

- $f^{-1} \left( \bigcap U_i \right) =_? \bigcap_i f^{-1} U_i$?

    Yes

    tags: misc

- True or false: $ X =_? (f^{-1} \circ f)(X) $

    Only when $f$ is injective, otherwise just $ \subseteq $.

    tags: misc

- True or false: $ X =_? (f\circ f^{-1})(X) $

    Only when $f$ is surjective, otherwise just $ \subseteq $.

    tags: misc

- True or false: $ f^{-1}(A) \setminus f^{-1}(B) =_? f^{-1}(A\setminus B) $

    Yes.
    For forward direction, only an inclusion.

    tags: misc

- True or false: $ \log(a-b) = \log(a) / \log(b) $

    False: take $b=1$, this would force dividing by zero.

    tags: unsorted

- True or false: $ \log(a+b) = \log(a) + \log(b) $

    False

    tags: unsorted

- True or false: $ \log(a+b) = \log(a) \log(b) $

    False

    tags: unsorted

- Write $ \log $ as a group homomorphism. What are the domain and codomain?

    $$
    \log: \GG_m(\RR) \to \GG_a(\RR) 
    .$$

    tags: unsorted

- Write $ \exp $  as a group homomorphism.

    $$
    \exp: \GG_a(\RR) \to \GG_m(\RR) 
    .$$

    tags: unsorted

- What inverses exist for injective (resp. surjective) functions?

    - Injections: left inverses, i.e. $f(x) = f(y) \implies x=y$
    - Surjections: right inverses

    tags: unsorted
