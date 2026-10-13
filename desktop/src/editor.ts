import { commonmarkLanguage, markdown } from "@codemirror/lang-markdown";
import { StreamLanguage } from "@codemirror/language";
import { stexMath } from "@codemirror/legacy-modes/mode/stex";
import { parseMixed } from "@lezer/common";
import { Pandoc } from "@lezer/markdown";

const tex = StreamLanguage.define(stexMath).parser;

// Zettlr's markdown-parser.ts and math-parser.ts mount TeX on Pandoc math nodes.
export const cardLanguage = markdown({
  base: commonmarkLanguage,
  extensions: [
    Pandoc(),
    {
      wrap: parseMixed((node, input) => {
        if (!["InlineCode", "FencedCode"].includes(node.name)) return null;
        const mark = node.node.getChild("CodeMark");
        if (
          !mark ||
          !["$", "$$", "\\(", "\\["].includes(input.read(mark.from, mark.to))
        )
          return null;
        return { parser: tex, overlay: (child) => child.name === "CodeText" };
      }),
    },
  ],
});
