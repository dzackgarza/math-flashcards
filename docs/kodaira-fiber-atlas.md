# Kodaira fiber atlas

Original schematic drawings used by the recognition cards in
[Curves and Surfaces](../decks/Algebraic%20Geometry/Curves%20and%20Surfaces.md).
The setting is a relatively minimal complex elliptic surface with section.

In the geometric sketches, strokes represent curves and marked points are
singularities or intersections. These are schematic, not literal real loci
of fixed equations. In the graphs, vertices represent rational components,
numbers give their fiber multiplicities, and the double-rim vertex meets the
zero section. All components in a reducible fiber have self-intersection $-2$.

## Geometric configurations

| Type | Sketch | Distinguishing feature |
| --- | --- | --- |
| $I_0$ | ![Smooth genus-one curve](../decks/Algebraic%20Geometry/assets/kodaira/fiber-1.svg) | Smooth fiber; the sketch indicates genus one |
| $I_1$ | ![Nodal curve](../decks/Algebraic%20Geometry/assets/kodaira/fiber-2.svg) | Irreducible nodal rational curve |
| $II$ | ![Cuspidal curve](../decks/Algebraic%20Geometry/assets/kodaira/fiber-3.svg) | Irreducible cuspidal rational curve |
| $I_2$ | ![Two transverse intersections](../decks/Algebraic%20Geometry/assets/kodaira/fiber-4.svg) | Two components meet at two points |
| $III$ | ![Two tangent components](../decks/Algebraic%20Geometry/assets/kodaira/fiber-5.svg) | Two components are tangent at one point |
| $I_3$ | ![Triangle of components](../decks/Algebraic%20Geometry/assets/kodaira/fiber-6.svg) | Three distinct intersection points |
| $IV$ | ![Three concurrent components](../decks/Algebraic%20Geometry/assets/kodaira/fiber-7.svg) | One common intersection point |

The ordinary intersection graph does not distinguish $I_3$ from $IV$.
Similarly, intersection number two does not distinguish the two crossings
of $I_2$ from the tangency of $III$.

## Weighted component configurations

| Type | Graph | General pattern |
| --- | --- | --- |
| $I_5$ | ![Cycle](../decks/Algebraic%20Geometry/assets/kodaira/fiber-8.svg) | $I_n$ is a cycle of $n$ multiplicity-one components for $n\ge3$ |
| $I_0^*$ | ![Affine D4](../decks/Algebraic%20Geometry/assets/kodaira/fiber-9.svg) | Central multiplicity two, four leaves of multiplicity one |
| $I_3^*$ | ![Affine D7](../decks/Algebraic%20Geometry/assets/kodaira/fiber-10.svg) | $I_n^*$ has a chain of $n+1$ double components and four simple leaves |
| $IV^*$ | ![Affine E6](../decks/Algebraic%20Geometry/assets/kodaira/fiber-11.svg) | Central multiplicity three; three arms $2,1$ |
| $III^*$ | ![Affine E7](../decks/Algebraic%20Geometry/assets/kodaira/fiber-12.svg) | Central multiplicity four; arms $3,2,1$; $3,2,1$; $2$ |
| $II^*$ | ![Affine E8](../decks/Algebraic%20Geometry/assets/kodaira/fiber-13.svg) | Central multiplicity six; arms $5,4,3,2,1$; $4,2$; $3$ |

The multiplicities satisfy $F\cdot C_i=0$. For these simply laced graphs,
twice a vertex's multiplicity equals the sum of its neighbors' multiplicities.
Deleting the identity vertex gives the finite root diagram.

## Sources and regeneration

The mathematical reference is
[Schütt–Shioda, Elliptic Surfaces, §§4–7](https://arxiv.org/abs/0907.0298).
The authored [TikZ source](../decks/Algebraic%20Geometry/assets/kodaira/fibers.tex)
contains one page per figure, in the order above. The SVGs are compiled from
that source and are the image files linked by the flashcards.

From the repository root, using the existing TeX and PDF tools:

~~~sh
mkdir -p /tmp/math-flashcards-kodaira
lualatex -interaction=batchmode -halt-on-error -output-directory=/tmp/math-flashcards-kodaira 'decks/Algebraic Geometry/assets/kodaira/fibers.tex'
for page in $(seq 1 13); do
  pdf2svg /tmp/math-flashcards-kodaira/fibers.pdf "decks/Algebraic Geometry/assets/kodaira/fiber-$page.svg" "$page"
done
~~~
