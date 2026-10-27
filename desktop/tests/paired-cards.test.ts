import { expect, test } from "bun:test";
import { cards, replaceField, removeCard, newCard } from "../src/cards";
import { diagramTargets, replaceDiagram, EMPTY_TIKZCD } from "../src/diagrams";

test("card sides pair by ID and edit independently without changing authored math", () => {
  const source = `---\ntitle: Test\n---\n\n::: {.back card-id="first"}\n$$\\frac{1}{2}$$\n\n- One\n- Two\n:::\n\n::: {.front card-id="second"}\nOther question\n:::\n\n::: {.front card-id="first" tags="formula"}\nQuestion\n\nSecond paragraph\n:::\n\n::: {.back card-id="second"}\nOther answer\n:::\n`;
  const deck = cards(source);
  expect(deck.map((card) => card.id)).toEqual(["second", "first"]);
  expect(deck[1].front.value).toBe("Question\n\nSecond paragraph");
  expect(deck[1].back.value).toBe("$$\\frac{1}{2}$$\n\n- One\n- Two");
  const edited = replaceField(
    source,
    deck[1].front,
    "New question\n\nMore detail",
  );
  expect(cards(edited)[1].back.value).toBe(deck[1].back.value);
  expect(cards(edited)[0].front.value).toBe(deck[0].front.value);
  expect(cards(edited)[0].back.value).toBe(deck[0].back.value);
  const remaining = cards(removeCard(edited, cards(edited)[1]));
  expect(remaining.map((card) => card.id)).toEqual(["second"]);
  const added = cards(edited + "\n" + newCard("third"));
  expect(added[2].id).toBe("third");
});

test("a deck rejects unpaired, duplicate, and unclosed card sides", () => {
  for (const source of [
    '::: {.front card-id="one"}\nQuestion\n:::\n',
    '::: {.back card-id="one"}\nAnswer\n:::\n',
    newCard("one") + newCard("one"),
    '::: {.front card-id="one"}\nQuestion\n',
    "::: {.front}\nQuestion\n:::\n",
  ])
    expect(() => cards(source)).toThrow();
});

test("Quiver share links become editable TikZ-cd without leaving a URL suffix", () => {
  const diagram = String.raw`\begin{tikzcd}
	A & B \\
	\arrow[from=1-1, to=1-2]
\end{tikzcd}`;
  for (const legacy of [
    "<https://q.uiver.app/?q=YWJj=>https://q.uiver.app/?q=YWJj=",
    "<https://q.uiver.app/?q=YWJj>https://q.uiver.app/?q=YWJj",
    "<https://q.uiver.app/?q=YWJj>=>https://q.uiver.app/?q=YWJj",
    "<https://q.uiver.app/?q=YWJj>",
  ]) {
    const back = "A universal property. " + legacy + "\n\nMore text.";
    const targets = diagramTargets(back);
    expect(targets).toHaveLength(1);
    expect(targets[0].source).toBe(legacy);
    const updated = replaceDiagram(back, targets[0], diagram);
    expect(updated).toContain(diagram);
    expect(updated).toContain("More text.");
    expect(updated).not.toContain("q.uiver.app");
    const deck = `::: {.front card-id="universal"}\nWhat?\n:::\n\n::: {.back card-id="universal"}\n${updated}\n:::\n`;
    expect(cards(deck)[0].back.value).toContain(diagram);
    expect(diagramTargets(updated).map((item) => item.kind)).toEqual([
      "tikzcd",
    ]);
    expect(() => replaceDiagram("Changed source", targets[0], diagram)).toThrow(
      "The diagram changed",
    );
  }
  expect(replaceDiagram("Answer", null, EMPTY_TIKZCD)).toBe(
    "Answer\n\n" + EMPTY_TIKZCD + "\n",
  );
});

test("diagram discovery excludes literal TikZ-cd and links inside code", () => {
  const raw = String.raw`\begin{tikzcd}
A & B
\end{tikzcd}`;
  const url = "<https://q.uiver.app/?q=YWJj>";
  const code = "~~~tex\n" + raw + "\n" + url + "\n~~~\n";
  expect(diagramTargets(code)).toEqual([]);
  expect(diagramTargets("`" + url + "`")).toEqual([]);
  const mixed = code + "\n" + raw + "\n\n" + url;
  expect(diagramTargets(mixed).map((item) => item.kind)).toEqual([
    "tikzcd",
    "quiver-url",
  ]);
  expect(diagramTargets("<https://q.uiver.app/?q=%ZZ>")).toEqual([]);
});
