import { type SyntaxNode, type SyntaxNodeRef } from "@lezer/common";
import { deckParser } from "./cards";
import { pandocLatexMathEnvironmentAtStart } from "@lezer/markdown";
import type { Macros } from "./bridge";

// MathJax 4 component API: https://docs.mathjax.org/en/v4.0/web/typeset.html#converting-a-math-string-to-other-formats
export interface MathJaxRuntime {
  startup: {
    promise: Promise<void>;
    defaultReady(): void;
    document: {
      clear(): void;
      updateDocument(): void;
      outputJax: { font: { loadDynamicFiles(): Promise<void> } };
    };
  };
  tex2chtml(math: string, options: { display: boolean }): HTMLElement;
  tex2mml(math: string, options: { display: boolean }): string;
}

let texErrors: string[] = [];

// TeX input options shared by the editor and the deck check, with the packages
// of the Anki card template. The macros use mathtools and stmaryrd. Without the
// noundefined package an unknown macro is an error, as in LaTeX. MathJax
// reports every TeX error through formatError:
// https://docs.mathjax.org/en/v4.0/options/input/tex.html#tex-options
export function texOptions(macros: Macros) {
  return {
    macros,
    packages: { "[+]": ["mathtools", "stmaryrd"], "[-]": ["noundefined"] },
    formatError(jax: { formatError(error: Error): unknown }, error: Error) {
      texErrors.push(error.message);
      return jax.formatError(error);
    },
    inlineMath: [
      ["$", "$"],
      ["\\(", "\\)"],
    ],
    displayMath: [
      ["$$", "$$"],
      ["\\[", "\\]"],
    ],
  };
}

// The TeX error in one equation, or null.
export function texError(
  mathjax: Pick<MathJaxRuntime, "tex2mml">,
  equation: string,
  display: boolean,
): string | null {
  texErrors = [];
  mathjax.tex2mml(equation, { display });
  return texErrors[0] ?? null;
}

declare global {
  interface Window {
    MathJax: MathJaxRuntime;
  }
  // Defined by pandoc-config's templates/js/mathjax-stmaryrd.js.
  function registerStmaryrd(mathjax: MathJaxRuntime): void;
}

// Runs pandoc-config's stmaryrd script, which defines registerStmaryrd. Call
// registerStmaryrd in startup.ready, before MathJax builds the TeX input.
export function defineStmaryrd(script: string) {
  new Function(script)();
}

let runtime: Promise<MathJaxRuntime> | undefined;

// MathJax reads its configuration once, when the component script loads. The
// editor converts equations synchronously, so the font data that MathJax 4
// loads on demand is loaded first:
// https://docs.mathjax.org/en/v4.0/upgrading/whats-new-4.0/promises.html
export function loadMathJax(
  macros: Macros,
  stmaryrd: string,
): Promise<MathJaxRuntime> {
  runtime ??= new Promise((resolve, reject) => {
    defineStmaryrd(stmaryrd);
    Object.assign(window, {
      MathJax: {
        startup: {
          typeset: false,
          ready() {
            registerStmaryrd(window.MathJax);
            window.MathJax.startup.defaultReady();
          },
        },
        loader: { load: ["[tex]/mathtools"], paths: { fonts: "/fonts" } },
        tex: texOptions(macros),
      },
    });
    const script = document.createElement("script");
    script.src = "/mathjax/tex-chtml.js";
    script.onerror = () => reject(new Error("MathJax failed to load."));
    script.onload = () => {
      window.MathJax.startup.promise
        .then(() =>
          window.MathJax.startup.document.outputJax.font.loadDynamicFiles(),
        )
        .then(() => resolve(window.MathJax), reject);
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

// `text` is the source of `node`.
export function equation(
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
