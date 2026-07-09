# Recovery Manifest — math-flashcards `.md` card sources

Recovered on: 2026-06-26T12:42:29Z
Source repo: `/home/dzack/gitclones/math-flashcards` (HEAD `5871456`, 856 commits across all refs; read-only — history untouched)
Staging dir: `/home/dzack/gitclones/math-flashcards-recovered/`

## Summary

- Files recovered: **120 / 120** historical `.md` paths
- Total size: **286457 bytes** (~279.7 KB)
- Method: for each `.md` path that ever existed in history, the **most recent commit/blob with non-empty content** was extracted via `git cat-file`. For files removed from the tree, the version was taken from the parent of their deletion commit. Original directory structure preserved.
- Byte sizes verified to match source blobs exactly (0 mismatches).
- Paths with **more than one distinct non-empty historical version**: **57** (flagged `*`). For these, the **latest non-empty** version was recovered.

## Notes

- `NonQualDecks/test.md` is a LaTeX scratch file, not an ankdown deck; recovered verbatim as it last appeared in history.
- All other recovered files use the ankdown card format (`front % back % tags` separated, cards delimited by `---`).

## Recovered files

| # | Path | Source commit | Commit date | Bytes | Distinct versions in history |
|---|------|---------------|-------------|-------|------------------------------|
| 1 | `2020-04-03.md` | `f8d28e88bfce` | 2020-05-15 | 192 | 1 |
| 2 | `Complex.md` | `f8d28e88bfce` | 2020-05-15 | 1111 | 1 |
| 3 | `Decks/2020-04-03.md` | `4b2f8915c44b` | 2020-06-17 | 192 | 1 |
| 4 | `Decks/AG.md` | `4b2f8915c44b` | 2020-06-17 | 82 | 1 |
| 5 | `Decks/Algebra.md` | `4b2f8915c44b` | 2020-06-17 | 591 | 3 \* |
| 6 | `Decks/Basics/Basics.md` | `158a1a91d8f9` | 2020-08-11 | 629 | 1 |
| 7 | `Decks/Basics.md` | `ff3c2fe94ccd` | 2020-08-11 | 629 | 14 \* |
| 8 | `Decks/CategoryTheory.md` | `4b2f8915c44b` | 2020-06-17 | 142 | 1 |
| 9 | `Decks/Complex.md` | `4b2f8915c44b` | 2020-06-17 | 1560 | 4 \* |
| 10 | `Decks/Definitions.md` | `4b2f8915c44b` | 2020-06-17 | 406 | 2 \* |
| 11 | `Decks/FunctionalAnalysis.md` | `4b2f8915c44b` | 2020-06-17 | 703 | 3 \* |
| 12 | `Decks/LieAlgebras.md` | `4b2f8915c44b` | 2020-06-17 | 720 | 1 |
| 13 | `Decks/Misc/Algebra/Algebraic Groups.md` | `cd71ac3b68ac` | 2022-02-06 | 98 | 1 |
| 14 | `Decks/Misc/Algebra/Category Theory.md` | `cd71ac3b68ac` | 2022-02-06 | 233 | 1 |
| 15 | `Decks/Misc/Algebra/Commutative Algebra.md` | `66a1b4e3f8bc` | 2022-12-25 | 891 | 3 \* |
| 16 | `Decks/Misc/Algebraic Geometry/AG.md` | `cd71ac3b68ac` | 2022-02-06 | 400 | 1 |
| 17 | `Decks/Misc/Algebra/Lie Algebras.md` | `cd71ac3b68ac` | 2022-02-06 | 653 | 1 |
| 18 | `Decks/Misc/Algebra/Number Theory.md` | `cd71ac3b68ac` | 2022-02-06 | 518 | 1 |
| 19 | `Decks/Misc/Analysis/Analysis 1.md` | `66a1b4e3f8bc` | 2022-12-25 | 5357 | 4 \* |
| 20 | `Decks/Misc/Analysis/Functional Analysis.md` | `66a1b4e3f8bc` | 2022-12-25 | 624 | 2 \* |
| 21 | `Decks/Misc/Grad Math Facts/Grad Math Facts.md` | `66a1b4e3f8bc` | 2022-12-25 | 1268 | 4 \* |
| 22 | `Decks/Misc/Topology/Algebraic Topology.md` | `66a1b4e3f8bc` | 2022-12-25 | 1985 | 1 |
| 23 | `Decks/Misc/Topology/Point-Set Topology.md` | `58e544fe482c` | 2022-02-06 | 125 | 1 |
| 24 | `Decks/Orals/2022-11-23.md` | `d175fc9f2424` | 2022-11-23 | 11065 | 55 \* |
| 25 | `Decks/QualAlgebraFields.md` | `ff3c2fe94ccd` | 2020-08-11 | 2520 | 7 \* |
| 26 | `Decks/QualAlgebraGroups.md` | `ff3c2fe94ccd` | 2020-08-11 | 4432 | 15 \* |
| 27 | `Decks/QualAlgebraicTopology.md` | `ff3c2fe94ccd` | 2020-08-11 | 1714 | 2 \* |
| 28 | `Decks/QualAlgebra.md` | `11930ea1f8d4` | 2020-06-01 | 1480 | 9 \* |
| 29 | `Decks/QualAlgebraModules.md` | `ff3c2fe94ccd` | 2020-08-11 | 530 | 3 \* |
| 30 | `Decks/QualAlgebra/QualAlgebraFields.md` | `89ba7a01e68b` | 2020-08-11 | 2520 | 1 |
| 31 | `Decks/Qual Algebra/QualAlgebraFields.md` | `eee8a18bda59` | 2020-10-28 | 4195 | 28 \* |
| 32 | `Decks/QualAlgebra/QualAlgebraGroups.md` | `89ba7a01e68b` | 2020-08-11 | 4432 | 1 |
| 33 | `Decks/Qual Algebra/QualAlgebraGroups.md` | `eee8a18bda59` | 2020-10-28 | 5055 | 12 \* |
| 34 | `Decks/QualAlgebra/QualAlgebraModules.md` | `89ba7a01e68b` | 2020-08-11 | 530 | 1 |
| 35 | `Decks/Qual Algebra/QualAlgebraModules.md` | `eee8a18bda59` | 2020-10-28 | 2994 | 29 \* |
| 36 | `Decks/Qual Algebra/Rings.md` | `eee8a18bda59` | 2020-10-28 | 2160 | 23 \* |
| 37 | `Decks/Qual Basics/Basics.md` | `eee8a18bda59` | 2020-10-28 | 895 | 8 \* |
| 38 | `Decks/QualComplexAnalysis.md` | `ff3c2fe94ccd` | 2020-08-11 | 3970 | 14 \* |
| 39 | `Decks/QualComplexAnalysis/QualComplexAnalysis.md` | `b063c552a45c` | 2020-08-11 | 3970 | 1 |
| 40 | `Decks/Qual Complex Analysis/QualComplexAnalysis.md` | `eee8a18bda59` | 2020-10-28 | 4253 | 13 \* |
| 41 | `Decks/QualPointSetTopology.md` | `ff3c2fe94ccd` | 2020-08-11 | 4904 | 5 \* |
| 42 | `Decks/QualRealAnalysis.md` | `ff3c2fe94ccd` | 2020-08-11 | 17753 | 80 \* |
| 43 | `Decks/Qual Real Analysis/QualClassReview.md` | `6ad37ce639a5` | 2020-08-17 | 5344 | 3 \* |
| 44 | `Decks/QualRealAnalysis/QualRealAnalysis.md` | `b063c552a45c` | 2020-08-11 | 17796 | 3 \* |
| 45 | `Decks/Qual Real Analysis/QualRealAnalysis.md` | `eee8a18bda59` | 2020-10-28 | 14732 | 60 \* |
| 46 | `Decks/Quals/Qual Algebra/QualAlgebraFields.md` | `66a1b4e3f8bc` | 2022-12-25 | 3625 | 1 |
| 47 | `Decks/Quals/Qual Algebra/QualAlgebraGroups.md` | `66a1b4e3f8bc` | 2022-12-25 | 5080 | 1 |
| 48 | `Decks/Quals/Qual Algebra/QualAlgebraModules.md` | `66a1b4e3f8bc` | 2022-12-25 | 2851 | 2 \* |
| 49 | `Decks/Quals/Qual Algebra/Rings.md` | `66a1b4e3f8bc` | 2022-12-25 | 2164 | 1 |
| 50 | `Decks/Quals/Qual Basics/Basics.md` | `66a1b4e3f8bc` | 2022-12-25 | 1267 | 1 |
| 51 | `Decks/Quals/Qual Basics/Special Angles.md` | `66a1b4e3f8bc` | 2022-12-25 | 941 | 1 |
| 52 | `Decks/Quals/Qual Complex Analysis/000_Proof Sketches.md` | `66a1b4e3f8bc` | 2022-12-25 | 829 | 1 |
| 53 | `Decks/Quals/Qual Complex Analysis/Basics.md` | `66a1b4e3f8bc` | 2022-12-25 | 600 | 1 |
| 54 | `Decks/Quals/Qual Complex Analysis/Conformal Maps.md` | `66a1b4e3f8bc` | 2022-12-25 | 722 | 1 |
| 55 | `Decks/Quals/Qual Complex Analysis/Definitions.md` | `66a1b4e3f8bc` | 2022-12-25 | 1133 | 2 \* |
| 56 | `Decks/Quals/Qual Complex Analysis/Examples.md` | `66a1b4e3f8bc` | 2022-12-25 | 600 | 1 |
| 57 | `Decks/Quals/Qual Complex Analysis/Formulas and Technical Theorems.md` | `66a1b4e3f8bc` | 2022-12-25 | 1997 | 1 |
| 58 | `Decks/Quals/Qual Complex Analysis/Hyperbolic Formulas.md` | `66a1b4e3f8bc` | 2022-12-25 | 1359 | 1 |
| 59 | `Decks/Quals/Qual Complex Analysis/Theorems facts and statements.md` | `66a1b4e3f8bc` | 2022-12-25 | 2233 | 1 |
| 60 | `Decks/Quals/Qual Real Analysis/QualRealAnalysis.md` | `66a1b4e3f8bc` | 2022-12-25 | 14737 | 3 \* |
| 61 | `Decks/Quals/Qual Topology/QualAlgebraicTopology.md` | `66a1b4e3f8bc` | 2022-12-25 | 1688 | 2 \* |
| 62 | `Decks/Quals/Qual Topology/QualPointSetTopology.md` | `66a1b4e3f8bc` | 2022-12-25 | 4951 | 2 \* |
| 63 | `Decks/QualTopology.md` | `4b2f8915c44b` | 2020-06-17 | 4674 | 19 \* |
| 64 | `Decks/QualTopology/QualAlgebraicTopology.md` | `b063c552a45c` | 2020-08-11 | 1714 | 1 |
| 65 | `Decks/Qual Topology/QualAlgebraicTopology.md` | `eee8a18bda59` | 2020-10-28 | 1687 | 2 \* |
| 66 | `Decks/QualTopology/QualPointSetTopology.md` | `b063c552a45c` | 2020-08-11 | 4904 | 1 |
| 67 | `Decks/Qual Topology/QualPointSetTopology.md` | `eee8a18bda59` | 2020-10-28 | 4950 | 6 \* |
| 68 | `Decks/Schemes.md` | `4b2f8915c44b` | 2020-06-17 | 126 | 1 |
| 69 | `Definitions.md` | `f8d28e88bfce` | 2020-05-15 | 279 | 1 |
| 70 | `LieAlgebras.md` | `f8d28e88bfce` | 2020-05-15 | 720 | 1 |
| 71 | `NonQualDecks/2020-04-03.md` | `2d5292d44d10` | 2020-09-04 | 192 | 1 |
| 72 | `NonQualDecks/AG.md` | `2d5292d44d10` | 2020-09-04 | 82 | 1 |
| 73 | `NonQualDecks/Algebra/Algebraic Groups.md` | `fba35efdfabd` | 2022-02-06 | 98 | 1 |
| 74 | `NonQualDecks/Algebra/Category Theory.md` | `fba35efdfabd` | 2022-02-06 | 233 | 2 \* |
| 75 | `NonQualDecks/Algebra/Commutative Algebra.md` | `fba35efdfabd` | 2022-02-06 | 1253 | 4 \* |
| 76 | `NonQualDecks/Algebraic Geometry/AG.md` | `fba35efdfabd` | 2022-02-06 | 400 | 1 |
| 77 | `NonQualDecks/AlgebraicTopology.md` | `2d5292d44d10` | 2020-09-04 | 1598 | 1 |
| 78 | `NonQualDecks/Algebra/Lie Algebras.md` | `fba35efdfabd` | 2022-02-06 | 653 | 2 \* |
| 79 | `NonQualDecks/Algebra.md` | `2d5292d44d10` | 2020-09-04 | 755 | 2 \* |
| 80 | `NonQualDecks/Algebra/Number Theory.md` | `fba35efdfabd` | 2022-02-06 | 518 | 1 |
| 81 | `NonQualDecks/Analysis/Analysis 1.md` | `fba35efdfabd` | 2022-02-06 | 5556 | 2 \* |
| 82 | `NonQualDecks/Analysis/FunctionalAnalysis.md` | `397e15795aa6` | 2020-09-04 | 703 | 1 |
| 83 | `NonQualDecks/Analysis/Functional Analysis.md` | `fba35efdfabd` | 2022-02-06 | 703 | 1 |
| 84 | `NonQualDecks/Analysis/QualClassReview.md` | `86e70095d843` | 2020-09-04 | 5344 | 1 |
| 85 | `NonQualDecks/CategoryTheory.md` | `2d5292d44d10` | 2020-09-04 | 142 | 1 |
| 86 | `NonQualDecks/Definitions.md` | `2d5292d44d10` | 2020-09-04 | 406 | 1 |
| 87 | `NonQualDecks/FunctionalAnalysis.md` | `2d5292d44d10` | 2020-09-04 | 703 | 1 |
| 88 | `NonQualDecks/Grad Math Facts/Grad Math Facts.md` | `fba35efdfabd` | 2022-02-06 | 1576 | 1 |
| 89 | `NonQualDecks/LieAlgebras.md` | `2d5292d44d10` | 2020-09-04 | 720 | 1 |
| 90 | `NonQualDecks/Misc/2020-09-16.md` | `eee8a18bda59` | 2020-10-28 | 848 | 4 \* |
| 91 | `NonQualDecks/NumberTheory.md` | `2d5292d44d10` | 2020-09-04 | 568 | 8 \* |
| 92 | `NonQualDecks/QualClassReview.md` | `f664d28a2eae` | 2020-09-04 | 5344 | 1 |
| 93 | `NonQualDecks/RepTheory.md` | `2d5292d44d10` | 2020-09-04 | 98 | 1 |
| 94 | `NonQualDecks/Schemes.md` | `2d5292d44d10` | 2020-09-04 | 126 | 1 |
| 95 | `NonQualDecks/test.md` | `0705c8578330` | 2020-07-27 | 635 | 1 |
| 96 | `NonQualDecks/Topology/AlgebraicTopology.md` | `397e15795aa6` | 2020-09-04 | 1598 | 1 |
| 97 | `NonQualDecks/Topology/Algebraic Topology.md` | `fba35efdfabd` | 2022-02-06 | 1985 | 2 \* |
| 98 | `NonQualDecks/Topology.md` | `397e15795aa6` | 2020-09-04 | 125 | 1 |
| 99 | `NonQualDecks/Topology/Point-Set Topology.md` | `fba35efdfabd` | 2022-02-06 | 125 | 1 |
| 100 | `Orals/2022-11-23.md` | `c3c5e8604774` | 2022-11-23 | 66 | 2 \* |
| 101 | `QualDecks/Qual Algebra/QualAlgebraFields.md` | `fba35efdfabd` | 2022-02-06 | 3625 | 6 \* |
| 102 | `QualDecks/Qual Algebra/QualAlgebraGroups.md` | `fba35efdfabd` | 2022-02-06 | 5080 | 6 \* |
| 103 | `QualDecks/Qual Algebra/QualAlgebraModules.md` | `fba35efdfabd` | 2022-02-06 | 2963 | 2 \* |
| 104 | `QualDecks/Qual Algebra/Rings.md` | `fba35efdfabd` | 2022-02-06 | 2164 | 2 \* |
| 105 | `QualDecks/Qual Basics/Basics.md` | `fba35efdfabd` | 2022-02-06 | 1267 | 1 |
| 106 | `QualDecks/Qual Basics/Special Angles.md` | `fba35efdfabd` | 2022-02-06 | 941 | 3 \* |
| 107 | `QualDecks/Qual Complex Analysis/000_Proof Sketches.md` | `fba35efdfabd` | 2022-02-06 | 829 | 4 \* |
| 108 | `QualDecks/Qual Complex Analysis/2021-12-18.md` | `bde013b640b7` | 2021-12-18 | 37 | 1 |
| 109 | `QualDecks/Qual Complex Analysis/Basics.md` | `fba35efdfabd` | 2022-02-06 | 600 | 3 \* |
| 110 | `QualDecks/Qual Complex Analysis/Conformal Maps.md` | `fba35efdfabd` | 2022-02-06 | 722 | 2 \* |
| 111 | `QualDecks/Qual Complex Analysis/Definitions.md` | `fba35efdfabd` | 2022-02-06 | 1127 | 5 \* |
| 112 | `QualDecks/Qual Complex Analysis/Examples.md` | `fba35efdfabd` | 2022-02-06 | 600 | 1 |
| 113 | `QualDecks/Qual Complex Analysis/Formulas and Technical Theorems.md` | `fba35efdfabd` | 2022-02-06 | 1997 | 15 \* |
| 114 | `QualDecks/Qual Complex Analysis/Hyperbolic Formulas.md` | `fba35efdfabd` | 2022-02-06 | 1359 | 7 \* |
| 115 | `QualDecks/Qual Complex Analysis/Theorems facts and statements.md` | `fba35efdfabd` | 2022-02-06 | 2233 | 4 \* |
| 116 | `QualDecks/Qual Real Analysis/QualRealAnalysis.md` | `fba35efdfabd` | 2022-02-06 | 14732 | 1 |
| 117 | `QualDecks/Qual Topology/QualAlgebraicTopology.md` | `fba35efdfabd` | 2022-02-06 | 1686 | 1 |
| 118 | `QualDecks/Qual Topology/QualPointSetTopology.md` | `fba35efdfabd` | 2022-02-06 | 4950 | 1 |
| 119 | `README.md` | `0b71b256ebb1` | 2020-05-15 | 4098 | 16 \* |
| 120 | `Test/2021-12-18.md` | `097f864aac28` | 2022-01-02 | 110 | 1 |

_\* = multiple distinct non-empty versions existed in history; the most recent non-empty one was recovered._
