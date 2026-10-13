import { Text } from "@codemirror/state";
import { parser, Pandoc, scanPandocAttributeList } from "@lezer/markdown";

export interface FieldRange {
  from: number;
  to: number;
  contentFrom: number;
  contentTo: number;
  value: string;
}

export interface CardRange {
  id: string;
  label: string;
  front: FieldRange;
  back: FieldRange;
  tags: string;
}

export const deckParser = parser.configure(Pandoc());

// Zettlr's div-model code uses these Pandoc syntax nodes and content bounds:
// Zettlr-pandoc-mathjax/source/common/pandoc-util/pandoc-div-model.ts
export function cards(source: string): CardRange[] {
  const document = Text.of(source.split("\n"));
  const pairs = new Map<
    string,
    { front?: FieldRange; back?: FieldRange; tags: string }
  >();
  const order: string[] = [];
  for (
    let node = deckParser.parse(source).topNode.firstChild;
    node;
    node = node.nextSibling
  ) {
    if (node.name === "YAMLFrontmatter") continue;
    if (node.name !== "PandocDiv")
      throw new Error("A deck must contain Front and Back pairs.");
    const attribute = node.getChild("PandocAttribute");
    const attributes =
      attribute &&
      scanPandocAttributeList(source.slice(attribute.from, attribute.to), 0);
    if (!attributes || attributes.status !== "match")
      throw new Error("A card side needs attributes.");
    const tokens = attributes.value.tokens;
    const sides = tokens.filter(
      (token) =>
        token.kind === "class" && ["front", "back"].includes(token.value),
    );
    const id = tokens.find(
      (token) => token.kind === "key-value" && token.key === "card-id",
    )?.value;
    if (sides.length !== 1 || !id)
      throw new Error("Each card side needs Front or Back and a card ID.");
    const marks = node.getChildren("PandocDivMark");
    if (marks.length !== 2) throw new Error(`Card ${id} has an unclosed side.`);
    const contentFrom = document.lineAt(attribute!.to).to + 1;
    const closeFrom = document.lineAt(marks[1].from).from;
    const contentTo = Math.max(contentFrom, closeFrom - 1);
    const field: FieldRange = {
      from: node.from,
      to: node.to,
      contentFrom,
      contentTo,
      value: source.slice(contentFrom, contentTo),
    };
    const pair = pairs.get(id) ?? { tags: "" };
    const side = sides[0].value as "front" | "back";
    if (pair[side]) throw new Error(`Card ${id} has a duplicate ${side}.`);
    pair[side] = field;
    if (side === "front") {
      order.push(id);
      pair.tags =
        tokens.find(
          (token) => token.kind === "key-value" && token.key === "tags",
        )?.value ?? "";
    }
    pairs.set(id, pair);
  }
  for (const [id, pair] of pairs) {
    if (!pair.front || !pair.back)
      throw new Error(`Card ${id} needs both Front and Back.`);
  }
  return order.map((id) => {
    const pair = pairs.get(id)!;
    return {
      id,
      front: pair.front!,
      back: pair.back!,
      tags: pair.tags,
      label:
        pair.front!.value.split("\n").find((line) => line.trim()) ?? "New card",
    };
  });
}

export function replaceField(
  source: string,
  field: FieldRange,
  value: string,
): string {
  return (
    source.slice(0, field.contentFrom) + value + source.slice(field.contentTo)
  );
}

export function replaceTags(
  source: string,
  card: CardRange,
  tags: string[],
): string {
  const node = deckParser.parse(source).resolve(card.front.from, 1);
  let div = node;
  while (div.name !== "PandocDiv" && div.parent) div = div.parent;
  const attribute = div.getChild("PandocAttribute")!;
  const scan = scanPandocAttributeList(
    source.slice(attribute.from, attribute.to),
    0,
  );
  if (scan.status !== "match") throw new Error("Invalid card attributes.");
  const token = scan.value.tokens.find(
    (item) => item.kind === "key-value" && item.key === "tags",
  );
  const from = token ? attribute.from + token.from : attribute.to - 1;
  const to = token ? attribute.from + token.to : from;
  const value = tags.join(", ").replace(/&/g, "&amp;").replace(/"/g, "&quot;");
  return (
    source.slice(0, from) +
    (token ? "" : " ") +
    `tags="${value}"` +
    source.slice(to)
  );
}

export function removeCard(source: string, card: CardRange): string {
  for (const field of [card.front, card.back].sort((a, b) => b.from - a.from)) {
    source = source.slice(0, field.from) + source.slice(field.to);
  }
  return source;
}

// Pandoc owns fenced div syntax: https://pandoc.org/MANUAL.html#divs-and-spans
export function newCard(id: string): string {
  return `::: {.front card-id="${id}"}\nNew question\n:::\n\n::: {.back card-id="${id}"}\nNew answer\n:::\n`;
}
