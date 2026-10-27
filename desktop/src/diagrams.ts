// The authored representation of a commutative diagram is TikZ-cd.
// Legacy Quiver share URLs are import inputs, never the persisted diagram.
import { deckParser } from "./cards";
export const EMPTY_TIKZCD = "\\begin{tikzcd}\n\n\\end{tikzcd}";

export interface DiagramTarget {
  kind: "tikzcd" | "quiver-url";
  from: number;
  to: number;
  source: string;
  encoded?: string;
}

const tikzcd = /\\begin\{tikzcd\}(?:\[[^\n]*\])?[\s\S]*?\\end\{tikzcd\}/gu;
// An older deck contains <URL>URL (the final '=' base64 padding makes this
// look like <URL=>URL). Accept both that and the explicit <URL>=>URL spelling.
const quiverLink =
  /<https:\/\/q\.uiver\.app\/\?q=[^<>\s]+>(?:(?:=>)?https:\/\/q\.uiver\.app\/\?q=[^<>\s]+)?/gu;

export function diagramTargets(source: string): DiagramTarget[] {
  const results: DiagramTarget[] = [];
  const rawBlocks: { from: number; to: number }[] = [];
  const literals: { from: number; to: number }[] = [];
  deckParser.parse(source).iterate({
    enter(node) {
      if (node.name === "RawBlock")
        rawBlocks.push({ from: node.from, to: node.to });
      if (node.name === "FencedCode" || node.name === "InlineCode") {
        literals.push({ from: node.from, to: node.to });
        return false;
      }
    },
  });
  for (const match of source.matchAll(tikzcd)) {
    if (
      !rawBlocks.some(
        (block) =>
          block.from <= match.index &&
          match.index + match[0].length <= block.to,
      )
    )
      continue;
    results.push({
      kind: "tikzcd",
      from: match.index,
      to: match.index + match[0].length,
      source: match[0],
    });
  }
  for (const match of source.matchAll(quiverLink)) {
    if (
      literals.some(
        (block) =>
          block.from < match.index + match[0].length && match.index < block.to,
      )
    )
      continue;
    const link = match[0].slice(1, match[0].indexOf(">"));
    let encoded: string;
    try {
      encoded = decodeURIComponent(link.slice(link.indexOf("?q=") + 3));
    } catch {
      // Malformed external links remain ordinary source text. The editor must
      // not crash or discard the entire card because of one invalid URL.
      continue;
    }
    if (!encoded || !/^[A-Za-z0-9+/=_-]+$/u.test(encoded)) continue;
    results.push({
      kind: "quiver-url",
      from: match.index,
      to: match.index + match[0].length,
      source: match[0],
      encoded,
    });
  }
  return results.sort((a, b) => a.from - b.from);
}

export function replaceDiagram(
  source: string,
  target: DiagramTarget | null,
  exported: string,
): string {
  const replacement = exported.trim();
  if (
    !/^\\begin\{tikzcd\}(?:\[[^\n]*\])?[\s\S]*\\end\{tikzcd\}$/u.test(
      replacement,
    )
  )
    throw new Error("Quiver must export a complete TikZ-cd environment.");
  if (target === null)
    return (
      source.trimEnd() + (source.trim() ? "\n\n" : "") + replacement + "\n"
    );
  if (source.slice(target.from, target.to) !== target.source)
    throw new Error("The diagram changed before it could be saved.");
  if (target.kind === "tikzcd")
    return source.slice(0, target.from) + replacement + source.slice(target.to);
  const before = source.slice(0, target.from);
  const after = source.slice(target.to);
  const leading =
    before.length && !before.endsWith("\n\n")
      ? before.endsWith("\n")
        ? "\n"
        : "\n\n"
      : "";
  const trailing =
    after.length && !after.startsWith("\n\n")
      ? after.startsWith("\n")
        ? "\n"
        : "\n\n"
      : "";
  return before + leading + replacement + trailing + after;
}
