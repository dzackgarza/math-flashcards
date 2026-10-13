import { expect, test } from "bun:test";
import { cards, replaceField, removeCard, newCard } from "../src/cards";

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
