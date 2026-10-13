# Pandoc parser

`lezer-markdown-pandoc.tgz` contains the unmodified parser package from
[Zettlr-Pandoc](https://github.com/dzackgarza/Zettlr-pandoc-mathjax),
`vendor/lezer-markdown-pandoc`, at commit
`26c97a3d65b34e87846462a89334ae2e78b3def3`.
The package includes its GPL-3.0-only license and Pandoc provenance file.

The package supplies Pandoc div, attribute, math, table, and LaTeX syntax.
The dependency override makes CodeMirror use the same parser as card pairing.
The editor follows Zettlr's `markdown-parser.ts` and `math-parser.ts` mounting
of TeX highlighting on the parser's math nodes. Preview HTML comes from Pandoc
and the existing Ankdown media and MathJax filter.
