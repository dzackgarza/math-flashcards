import {
  Badge,
  Button,
  Group,
  Modal,
  Stack,
  Text,
  UnstyledButton,
} from "@mantine/core";
import { cardChanges, type CardChange } from "./cards";
import { previewHtml, type MathJaxRuntime } from "./math";
import { deckName } from "./organize";
import type { Pending } from "./bridge";

const kinds = {
  added: { label: "New", color: "teal" },
  edited: { label: "Edited", color: "indigo" },
  removed: { label: "Removed", color: "red" },
} as const;

// The deck change itself is listed card by card.
const deckChanged = "The deck changed.";

function Rendered({
  mathjax,
  text,
  className,
}: {
  mathjax: MathJaxRuntime | null;
  text: string;
  className: string;
}) {
  return mathjax ? (
    <span
      className={className}
      dangerouslySetInnerHTML={{ __html: previewHtml(mathjax, text) }}
    />
  ) : (
    <span className={className}>{text}</span>
  );
}

function ChangeRow({
  change,
  mathjax,
  open,
}: {
  change: CardChange;
  mathjax: MathJaxRuntime | null;
  open: (() => void) | null;
}) {
  const card = change.after ?? change.before!;
  const sides = (["front", "back"] as const).filter(
    (side) =>
      change.kind === "edited" &&
      change.before![side].value !== change.after![side].value,
  );
  const body = (
    <Stack gap={6}>
      <Group gap="xs" wrap="nowrap" align="start">
        <Badge
          size="sm"
          variant="light"
          color={kinds[change.kind].color}
          className="change-kind"
        >
          {kinds[change.kind].label}
        </Badge>
        <Rendered
          mathjax={mathjax}
          text={card.front.value}
          className="change-front"
        />
      </Group>
      {sides.map((side) => (
        <div key={side} className="change-diff">
          <Text className="eyebrow" component="span">
            {side === "front" ? "Front before" : "Back before"}
          </Text>
          <Rendered
            mathjax={mathjax}
            text={change.before![side].value}
            className="change-before"
          />
          <Text className="eyebrow" component="span">
            {side === "front" ? "Front now" : "Back now"}
          </Text>
          <Rendered
            mathjax={mathjax}
            text={change.after![side].value}
            className="change-after"
          />
        </div>
      ))}
      {change.kind === "edited" && sides.length === 0 && (
        <Text size="sm" c="dimmed">
          Tags changed: {change.before!.tags || "none"} →{" "}
          {change.after!.tags || "none"}
        </Text>
      )}
    </Stack>
  );
  return open ? (
    <UnstyledButton className="change-row" onClick={open}>
      {body}
    </UnstyledButton>
  ) : (
    <div className="change-row">{body}</div>
  );
}

// Lists what each out-of-date deck has that its Anki package lacks, then
// regenerates the listed packages.
export function ReviewChanges({
  decks,
  mathjax,
  opened,
  busy,
  close,
  openCard,
  update,
}: {
  decks: Pending[] | null;
  mathjax: MathJaxRuntime | null;
  opened: boolean;
  busy: boolean;
  close: () => void;
  openCard: (path: string, id: string) => void;
  update: (paths: string[]) => void;
}) {
  const count = decks?.length ?? 0;
  return (
    <Modal
      opened={opened}
      onClose={close}
      size="xl"
      title="Changes not in the Anki packages"
    >
      {decks === null ? (
        <Text c="dimmed">Comparing the decks with their packages…</Text>
      ) : count === 0 ? (
        <Text c="dimmed">Every Anki package is up to date.</Text>
      ) : (
        <Stack gap="lg">
          {decks.map((deck) => {
            let changes: CardChange[] = [];
            let failure = "";
            try {
              changes = cardChanges(deck.built, deck.source);
            } catch (error) {
              failure = String(error);
            }
            const reasons = deck.reasons.filter(
              (reason) => reason !== deckChanged || changes.length === 0,
            );
            return (
              <section key={deck.path} className="review-deck">
                <Group justify="space-between" align="baseline">
                  <Text fw={600}>{deckName(deck.path)}</Text>
                  <Text size="sm" c="dimmed">
                    {deck.path.split("/").slice(0, -1).join(" / ")}
                  </Text>
                </Group>
                {reasons.map((reason) => (
                  <Text key={reason} size="sm" c="dimmed">
                    {reason === deckChanged
                      ? "The card order or deck settings changed."
                      : reason}
                  </Text>
                ))}
                {failure && (
                  <Text size="sm" c="red">
                    {failure}
                  </Text>
                )}
                <Stack gap={4} mt={6}>
                  {changes.map((change) => (
                    <ChangeRow
                      key={change.id}
                      change={change}
                      mathjax={mathjax}
                      open={
                        change.kind === "removed"
                          ? null
                          : () => openCard(deck.path, change.id)
                      }
                    />
                  ))}
                </Stack>
              </section>
            );
          })}
        </Stack>
      )}
      <Group justify="flex-end" className="review-actions">
        <Button variant="default" onClick={close}>
          Close
        </Button>
        <Button
          disabled={count === 0 || busy}
          onClick={() => update(decks!.map((deck) => deck.path))}
        >
          {count === 1
            ? "Update the Anki package"
            : "Update " + count + " Anki packages"}
        </Button>
      </Group>
    </Modal>
  );
}
