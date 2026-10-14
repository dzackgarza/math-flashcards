import { useMemo } from "react";
import { Box, Title } from "@mantine/core";
import CodeMirror from "@uiw/react-codemirror";
import { commonmarkLanguage, markdown } from "@codemirror/lang-markdown";
import { StreamLanguage } from "@codemirror/language";
import { stexMath } from "@codemirror/legacy-modes/mode/stex";
import { parseMixed } from "@lezer/common";
import { Pandoc } from "@lezer/markdown";
import { EditorView } from "@codemirror/view";
import { type MathJaxRuntime, renderedMath } from "./math";

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

export type Side = "front" | "back";

// One card side: Markdown and TeX source with math rendered in place.
export function SideEditor({
  side,
  value,
  mathjax,
  editable,
  onChange,
}: {
  side: Side;
  value: string;
  mathjax: MathJaxRuntime | null;
  editable: boolean;
  onChange: (value: string) => void;
}) {
  const label = side === "front" ? "Front" : "Back";
  const extensions = useMemo(
    () => [
      cardLanguage,
      EditorView.lineWrapping,
      ...(mathjax ? [renderedMath(mathjax)] : []),
    ],
    [mathjax],
  );
  return (
    <Box className={"side-editor " + side}>
      <Title order={4} size="h6" mb="xs">
        {label}
      </Title>
      <CodeMirror
        value={value}
        minHeight="100px"
        maxHeight="60vh"
        extensions={extensions}
        basicSetup={{
          lineNumbers: false,
          foldGutter: false,
          highlightActiveLine: false,
        }}
        editable={editable}
        onChange={onChange}
        aria-label={label}
      />
    </Box>
  );
}
