import { parser } from "@lezer/markdown";

export interface CardRange {
  from: number;
  to: number;
  label: string;
}

// Lezer owns list syntax and source ranges: https://lezer.codemirror.net/docs/guide/
export function cards(source: string): CardRange[] {
  const ranges: CardRange[] = [];
  parser.parse(source).iterate({
    enter(node) {
      if (node.name !== "ListItem") return;
      const list = node.node.parent;
      if (list?.parent?.name !== "Document") return false;
      const content = node.node.getChild("Paragraph");
      const label = content ? source.slice(content.from, content.to).split("\n")[0] : "Untitled card";
      ranges.push({ from: node.from, to: node.to, label });
      return false;
    },
  });
  return ranges;
}

export function replaceCard(source: string, card: CardRange, replacement: string): string {
  return source.slice(0, card.from) + replacement.trimEnd() + source.slice(card.to);
}
