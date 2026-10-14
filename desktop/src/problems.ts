import { cards, deckParser, type CardRange } from "./cards";
import { equation, texError, type MathJaxRuntime } from "./math";

export interface Problem {
  path: string;
  // The card and side that hold the problem; null for the whole deck.
  card: string | null;
  label: string | null;
  side: "front" | "back" | null;
  kind: "LaTeX" | "Card structure" | "Empty answer";
  message: string;
  source: string | null;
}

type Checker = Pick<MathJaxRuntime, "tex2mml">;

// The equations of one side, found as the editor finds them.
function sideProblems(
  mathjax: Checker,
  path: string,
  card: CardRange,
  side: "front" | "back",
): Problem[] {
  const text = card[side].value;
  const problems: Problem[] = [];
  deckParser.parse(text).iterate({
    enter(node) {
      if (!["InlineCode", "FencedCode", "RawInline"].includes(node.name))
        return;
      const source = text.slice(node.from, node.to);
      const math = equation(source, node);
      if (!math) return false;
      const message = texError(mathjax, math.equation, math.display);
      if (message)
        problems.push({
          path,
          card: card.id,
          label: card.label,
          side,
          kind: "LaTeX",
          message,
          source: source.trim(),
        });
      return false;
    },
  });
  return problems;
}

// Problems that stop a deck from rendering or exporting correctly.
export function deckProblems(
  mathjax: Checker,
  path: string,
  source: string,
): Problem[] {
  let ranges: CardRange[];
  try {
    ranges = cards(source);
  } catch (failure) {
    return [
      {
        path,
        card: null,
        label: null,
        side: null,
        kind: "Card structure",
        message: failure instanceof Error ? failure.message : String(failure),
        source: null,
      },
    ];
  }
  return ranges.flatMap((card) => [
    ...sideProblems(mathjax, path, card, "front"),
    ...sideProblems(mathjax, path, card, "back"),
    ...(card.back.value.trim()
      ? []
      : [
          {
            path,
            card: card.id,
            label: card.label,
            side: "back" as const,
            kind: "Empty answer" as const,
            message: "The exporter rejects a card without an answer.",
            source: null,
          },
        ]),
  ]);
}
