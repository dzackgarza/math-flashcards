import { syntaxTree } from "@codemirror/language";
import {
  type EditorState,
  type Range,
  StateEffect,
  StateField,
} from "@codemirror/state";
import {
  Decoration,
  type DecorationSet,
  EditorView,
  WidgetType,
} from "@codemirror/view";
import { type SyntaxNode, type SyntaxNodeRef } from "@lezer/common";
import { deckParser } from "./cards";
import { pandocLatexMathEnvironmentAtStart } from "@lezer/markdown";
import type { Macros } from "./bridge";

// Adapted from Zettlr-pandoc-mathjax (GPL-3.0):
// source/common/modules/markdown-editor/renderers/render-math.ts,
// base-renderer.ts, click-and-select.ts, and util/math-delimiters.ts.

// MathJax 3 component API: https://docs.mathjax.org/en/v3.2/web/typeset.html#converting-a-math-string-to-other-formats
export interface MathJaxRuntime {
  startup: {
    promise: Promise<void>;
    document: { clear(): void; updateDocument(): void };
  };
  tex2chtml(math: string, options: { display: boolean }): HTMLElement;
}

declare global {
  interface Window {
    MathJax: MathJaxRuntime;
  }
}

let runtime: Promise<MathJaxRuntime> | undefined;

// MathJax reads its configuration once, when the component script loads.
export function loadMathJax(macros: Macros): Promise<MathJaxRuntime> {
  runtime ??= new Promise((resolve, reject) => {
    Object.assign(window, {
      MathJax: {
        startup: { typeset: false },
        tex: {
          macros,
          inlineMath: [
            ["$", "$"],
            ["\\(", "\\)"],
          ],
          displayMath: [
            ["$$", "$$"],
            ["\\[", "\\]"],
          ],
        },
      },
    });
    const script = document.createElement("script");
    script.src = "/mathjax/tex-chtml.js";
    script.onerror = () => reject(new Error("MathJax failed to load."));
    script.onload = () => {
      window.MathJax.startup.promise.then(
        () => resolve(window.MathJax),
        reject,
      );
    };
    document.head.append(script);
  });
  return runtime;
}

const delimiters = [
  { open: "$$", close: "$$", display: true },
  { open: "\\[", close: "\\]", display: true },
  { open: "\\(", close: "\\)", display: false },
  { open: "$", close: "$", display: false },
];

class MathWidget extends WidgetType {
  constructor(
    readonly mathjax: MathJaxRuntime,
    readonly equation: string,
    readonly display: boolean,
    readonly sourceLength: number,
  ) {
    super();
  }

  eq(other: MathWidget) {
    return (
      other.equation === this.equation &&
      other.display === this.display &&
      other.sourceLength === this.sourceLength
    );
  }

  toDOM(view: EditorView) {
    const element = document.createElement(this.display ? "div" : "span");
    element.className = "rendered-math";
    element.append(
      this.mathjax.tex2chtml(this.equation, { display: this.display }),
    );
    // CHTML adds the stylesheet for new characters on document update.
    this.mathjax.startup.document.clear();
    this.mathjax.startup.document.updateDocument();
    // Clicking a rendered equation selects its source. The widget keeps no
    // position; the view knows where it is after earlier edits.
    element.addEventListener("mousedown", (event) => {
      event.preventDefault();
      const from = view.posAtDOM(element);
      view.focus();
      view.dispatch({
        selection: { anchor: from, head: from + this.sourceLength },
      });
    });
    return element;
  }

  ignoreEvent() {
    return true;
  }
}

// `text` is the source of `node`.
function equation(
  text: string,
  node: SyntaxNodeRef,
): { equation: string; display: boolean } | null {
  if (node.name === "RawInline") {
    const environment = pandocLatexMathEnvironmentAtStart(text);
    return environment && environment.end === text.length
      ? { equation: text, display: environment.display }
      : null;
  }
  const mark = node.node.firstChild;
  if (mark?.name !== "CodeMark") return null;
  const trimmed = text.endsWith("\n") ? text.slice(0, -1) : text;
  for (const { open, close, display } of delimiters) {
    if (
      trimmed.length >= open.length + close.length &&
      trimmed.startsWith(open) &&
      trimmed.endsWith(close)
    )
      return {
        equation: trimmed.slice(open.length, trimmed.length - close.length),
        display,
      };
  }
  return null;
}

// While the editor has focus, the equation under a selection shows its source.
function decorate(
  state: EditorState,
  mathjax: MathJaxRuntime,
  focused: boolean,
): DecorationSet {
  const widgets: Range<Decoration>[] = [];
  syntaxTree(state).iterate({
    enter(node) {
      if (!["InlineCode", "FencedCode", "RawInline"].includes(node.name))
        return;
      if (
        focused &&
        state.selection.ranges.some(
          (range) => range.from <= node.to && range.to >= node.from,
        )
      )
        return false;
      const math = equation(state.sliceDoc(node.from, node.to), node);
      if (!math) return;
      widgets.push(
        Decoration.replace({
          widget: new MathWidget(
            mathjax,
            math.equation,
            math.display,
            node.to - node.from,
          ),
        }).range(node.from, node.to),
      );
      return false;
    },
  });
  return Decoration.set(widgets);
}

const focusEffect = StateEffect.define<boolean>();

// Replacements that span line breaks must come from a state field:
// https://codemirror.net/docs/ref/#view.Decoration^replace
const rendered = StateField.define<{
  mathjax: MathJaxRuntime | null;
  focused: boolean;
  decorations: DecorationSet;
}>({
  create: () => ({
    mathjax: null,
    focused: false,
    decorations: Decoration.none,
  }),
  update(value, transaction) {
    let { focused } = value;
    for (const effect of transaction.effects)
      if (effect.is(focusEffect)) focused = effect.value;
    if (
      !value.mathjax ||
      (focused === value.focused &&
        !transaction.docChanged &&
        !transaction.selection)
    )
      return value;
    return {
      mathjax: value.mathjax,
      focused,
      decorations: decorate(transaction.state, value.mathjax, focused),
    };
  },
  provide: (field) =>
    EditorView.decorations.from(field, (value) => value.decorations),
});

export function renderedMath(mathjax: MathJaxRuntime) {
  return [
    rendered.init((state) => ({
      mathjax,
      focused: false,
      decorations: decorate(state, mathjax, false),
    })),
    EditorView.focusChangeEffect.of((_, focusing) => focusEffect.of(focusing)),
  ];
}

const skipped = new Set([
  "EmphasisMark",
  "CodeMark",
  "LinkMark",
  "URL",
  "LinkLabel",
  "LinkTitle",
  "HeaderMark",
  "ListMark",
  "QuoteMark",
  "Image",
  "HTMLTag",
  "PandocDivMark",
  "PandocAttribute",
]);
const tags: Record<string, string> = {
  StrongEmphasis: "strong",
  Emphasis: "em",
};
const escape = (text: string) =>
  text.replace(/[&<>"]/g, (character) => "&#" + character.charCodeAt(0) + ";");
const previews = new Map<string, string>();

// One line of card Markdown as inline HTML, for card lists. The deck parser
// finds emphasis and math as the editor does; MathJax renders the math.
export function previewHtml(mathjax: MathJaxRuntime, text: string): string {
  const cached = previews.get(text);
  if (cached !== undefined) return cached;
  const render = (node: SyntaxNode): string => {
    const source = text.slice(node.from, node.to);
    if (["InlineCode", "FencedCode", "RawInline"].includes(node.name)) {
      const math = equation(source, node);
      if (math)
        return mathjax.tex2chtml(math.equation, { display: false }).outerHTML;
    }
    if (skipped.has(node.name)) return "";
    let html = "";
    let position = node.from;
    for (let child = node.firstChild; child; child = child.nextSibling) {
      html += escape(text.slice(position, child.from)) + render(child);
      position = child.to;
    }
    html += escape(text.slice(position, node.to));
    const tag = tags[node.name];
    return tag ? `<${tag}>${html}</${tag}>` : html;
  };
  const html = render(deckParser.parse(text).topNode).replace(/\s+/g, " ");
  // CHTML adds the stylesheet for new characters on document update.
  mathjax.startup.document.clear();
  mathjax.startup.document.updateDocument();
  previews.set(text, html);
  return html;
}
