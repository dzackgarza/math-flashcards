import { expect, test } from "bun:test";
import { cards, newCard, reorderCards, transferCards } from "../src/cards";

test("reorder and transfer preserve both authored sides, IDs, and deck metadata", () => {
  const source =
    '---\ntitle: "Origin"\n---\n\n' +
    newCard("one") +
    "\n" +
    newCard("two") +
    "\n" +
    newCard("three");
  const destination = '---\ntitle: "Destination"\n---\n\n' + newCard("four");
  const reordered = reorderCards(source, ["three", "one", "two"]);
  expect(cards(reordered).map((card) => card.id)).toEqual([
    "three",
    "one",
    "two",
  ]);
  const moved = transferCards(source, destination, ["three", "one"], "four");
  expect(cards(moved.source).map((card) => card.id)).toEqual(["two"]);
  expect(cards(moved.destination).map((card) => card.id)).toEqual([
    "one",
    "three",
    "four",
  ]);
  expect(moved.destination.startsWith('---\ntitle: "Destination"\n---')).toBe(
    true,
  );
  expect(cards(moved.destination)[0].back.value).toBe(
    cards(source)[0].back.value,
  );
  const empty = transferCards(source, destination, ["one", "two", "three"]);
  expect(cards(empty.source)).toEqual([]);
  expect(cards(empty.destination).map((card) => card.id)).toEqual([
    "four",
    "one",
    "two",
    "three",
  ]);
  expect(() => transferCards(source, source, ["one"])).toThrow();
});

test("moving cards keeps relative media links attached to their original files", () => {
  const source =
    '::: {.front card-id="plot"}\n![Plot](assets/plot.png)\n:::\n\n::: {.back card-id="plot"}\n$$x^2$$\n:::\n';
  const moved = transferCards(
    source,
    '---\ntitle: "Target"\n---\n',
    ["plot"],
    undefined,
    { source: "Algebra/source.md", destination: "Analysis/target.md" },
  );
  expect(cards(moved.destination)[0].front.value).toBe(
    "![Plot](../Algebra/assets/plot.png)",
  );
  expect(cards(moved.destination)[0].back.value).toBe("$$x^2$$");
});
