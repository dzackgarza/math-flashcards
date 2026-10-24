import { useMemo } from "react";
import { Box, Text } from "@mantine/core";
import CodeMirror from "@uiw/react-codemirror";
import {
  markdownEditor,
  markdownParser,
  previewConfig,
} from "@dzack/pandoc-editor";
import "@dzack/pandoc-editor/editor.css";
import { type MathJaxRuntime } from "./math";

export const cardLanguage = markdownParser();
export type Side = "front" | "back";

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
      previewConfig.of({ previewModeShowSyntaxWhenCursorIsAdjacent: false }),
      markdownEditor({
        math: mathjax
          ? {
              render(equation, element, mode) {
                element.replaceChildren(
                  mathjax.tex2chtml(equation, { display: mode === "display" }),
                );
                mathjax.startup.document.clear();
                mathjax.startup.document.updateDocument();
              },
            }
          : undefined,
      }),
    ],
    [mathjax],
  );
  return (
    <Box className={"side-editor card-face " + side}>
      <Text className="eyebrow" component="h3">
        {label}
      </Text>
      <CodeMirror
        value={value}
        minHeight="160px"
        extensions={extensions}
        basicSetup={{
          lineNumbers: false,
          foldGutter: false,
          highlightActiveLine: false,
          syntaxHighlighting: false,
        }}
        editable={editable}
        onChange={onChange}
        aria-label={label}
      />
    </Box>
  );
}
