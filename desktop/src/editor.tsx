import { useCallback, useMemo, useRef, useState } from "react";
import { Box, Button, Group, Text } from "@mantine/core";
import CodeMirror from "@uiw/react-codemirror";
import {
  markdownEditor,
  markdownParser,
  previewConfig,
} from "@dzack/pandoc-editor";
import "@dzack/pandoc-editor/editor.css";
import { type MathJaxRuntime } from "./math";
import { diagramTargets, type DiagramTarget } from "./diagrams";
import { QuiverPreview } from "./quiver";

export const cardLanguage = markdownParser();
export type Side = "front" | "back";

export function SideEditor({
  side,
  value,
  mathjax,
  editable,
  onChange,
  onNewDiagram,
  onEditDiagram,
  workspace,
  path,
}: {
  side: Side;
  value: string;
  mathjax: MathJaxRuntime | null;
  editable: boolean;
  onChange: (value: string) => void;
  onNewDiagram?: () => void;
  onEditDiagram?: (target: DiagramTarget) => void;
  workspace: string;
  path: string;
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
  const latestSource = useRef(value);
  const [sourceMode, setSourceMode] = useState(false);
  const acknowledged = emitted.current.lastIndexOf(value);
  if (acknowledged > 0) emitted.current = emitted.current.slice(acknowledged);
  else if (acknowledged < 0) {
    emitted.current = [value];
    if (value !== shown) {
      latestSource.current = value;
      setShown(value);
    }
  }
  const onChangeRef = useRef(onChange);
  onChangeRef.current = onChange;
  const change = useCallback((next: string) => {
    latestSource.current = next;
    emitted.current.push(next);
    setShown(next);
    onChangeRef.current(next);
  }, []);
  const diagrams = useMemo(() => diagramTargets(shown), [shown]);
  const textParts = useMemo(() => {
    let from = 0;
    const parts: { from: number; to: number; text: string }[] = [];
    for (const diagram of diagrams) {
      parts.push({
        from,
        to: diagram.from,
        text: shown.slice(from, diagram.from),
      });
      from = diagram.to;
    }
    parts.push({ from, to: shown.length, text: shown.slice(from) });
    return parts;
  }, [shown, diagrams]);
  const basicSetup = useMemo(
    () => ({
      lineNumbers: false,
      foldGutter: false,
      highlightActiveLine: false,
      syntaxHighlighting: false,
    }),
    [],
  );
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
      <Group
        justify="space-between"
        align="center"
        className="side-editor-heading"
      >
        <Text className="eyebrow" component="h3">
          {label}
        </Text>
        <Group gap="xs">
          {diagrams.length > 0 && (
            <Button
              variant="subtle"
              size="compact-xs"
              onClick={() => setSourceMode((previous) => !previous)}
            >
              {sourceMode ? "Visual view" : "Edit source"}
            </Button>
          )}
          {onNewDiagram && (
            <Button
              variant="subtle"
              size="compact-xs"
              onClick={onNewDiagram}
              disabled={!editable}
            >
              New diagram
            </Button>
          )}
        </Group>
      </Group>
      {sourceMode || diagrams.length === 0 ? (
        <CodeMirror
          value={shown}
          minHeight="160px"
          extensions={extensions}
          basicSetup={basicSetup}
          editable={editable}
          onChange={change}
          aria-label={label}
        />
      ) : (
        <div className="diagram-flow">
          {textParts.map((part, i) => (
            <div key={"part-" + i}>
              {(part.text.trim() !== "" || i === diagrams.length) && (
                <CodeMirror
                  value={part.text}
                  minHeight="48px"
                  extensions={extensions}
                  basicSetup={basicSetup}
                  editable={editable}
                  aria-label={label + " text " + (i + 1)}
                  onChange={(text) => {
                    const source = latestSource.current;
                    const current = diagramTargets(source);
                    if (current.length !== diagrams.length) return;
                    const from = i === 0 ? 0 : current[i - 1].to;
                    const to =
                      i === current.length ? source.length : current[i].from;
                    change(source.slice(0, from) + text + source.slice(to));
                  }}
                />
              )}
              {i < diagrams.length && (
                <div className="diagram-field-entry">
                  <Group justify="space-between" gap="xs" mb={6}>
                    <Text size="xs" c="dimmed">
                      Commutative diagram {i + 1}
                    </Text>
                    {onEditDiagram && (
                      <Button
                        variant="light"
                        size="compact-xs"
                        disabled={!editable}
                        onClick={() => onEditDiagram(diagrams[i])}
                      >
                        Edit in Quiver
                      </Button>
                    )}
                  </Group>
                  <QuiverPreview
                    target={diagrams[i]}
                    workspace={workspace}
                    path={path}
                  />
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </Box>
  );
}
