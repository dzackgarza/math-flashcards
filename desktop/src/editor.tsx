import { useCallback, useMemo, useRef, useState } from "react";
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
  // @uiw/react-codemirror applies a changed `value` prop as an ExternalChange
  // transaction, which it never reports through onChange. A late render can
  // deliver a value this editor already emitted and overwrite newer text
  // without the parent seeing it. Values the editor emitted are echoes; only
  // other values are external changes.
  // Props arrive in emission order, so an acknowledged value retires every
  // earlier one.
  const emitted = useRef([value]);
  const [shown, setShown] = useState(value);
  const acknowledged = emitted.current.lastIndexOf(value);
  if (acknowledged > 0) emitted.current = emitted.current.slice(acknowledged);
  else if (acknowledged < 0) {
    emitted.current = [value];
    if (value !== shown) setShown(value);
  }
  const onChangeRef = useRef(onChange);
  onChangeRef.current = onChange;
  const change = useCallback((next: string) => {
    emitted.current.push(next);
    setShown(next);
    onChangeRef.current(next);
  }, []);
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
        value={shown}
        minHeight="160px"
        extensions={extensions}
        basicSetup={{
          lineNumbers: false,
          foldGutter: false,
          highlightActiveLine: false,
          syntaxHighlighting: false,
        }}
        editable={editable}
        onChange={change}
        aria-label={label}
      />
    </Box>
  );
}
