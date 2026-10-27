import { useEffect, useRef, useState } from "react";
import { Alert, Button, Group, Loader, Modal, Text } from "@mantine/core";
import { z } from "zod";
import { request, assetsSchema, renderedDiagramSchema } from "./bridge";
import { EMPTY_TIKZCD, type DiagramTarget } from "./diagrams";

const messageSchema = z.object({
  type: z.string().optional(),
  event: z.string().optional(),
  action: z.string().optional(),
  status: z.string().optional(),
  sessionId: z.string().nullable().optional(),
  revision: z.number().optional(),
  requestId: z.string().nullable().optional(),
  source: z.string().nullable().optional(),
  error: z.string().nullable().optional(),
  message: z.string().optional(),
  diagnostics: z
    .array(z.object({ severity: z.string(), message: z.string() }))
    .optional(),
});

let macroPromise: Promise<Record<string, string>> | null = null;
function quiverMacros(): Promise<Record<string, string>> {
  macroPromise ??= request({ action: "assets" }, assetsSchema).then((assets) =>
    Object.fromEntries(
      Object.entries(assets.macros).flatMap(([name, definition]) => {
        if (typeof definition === "string") return [["\\" + name, definition]];
        if (Array.isArray(definition) && definition.length === 2)
          return [["\\" + name, definition[0]]];
        return [];
      }),
    ),
  );
  return macroPromise;
}

// The original encoded diagram is imported by the vendor itself; no other code
// interprets the encoded diagram or manufactures TikZ-cd geometry.
function LegacyConverter({
  encoded,
  onResult,
}: {
  encoded: string;
  onResult: (source: string | null, error: string | null) => void;
}) {
  const frame = useRef<HTMLIFrameElement>(null);
  const requestId = useRef(crypto.randomUUID());
  const callback = useRef(onResult);
  callback.current = onResult;
  useEffect(() => {
    function receive(event: MessageEvent) {
      if (
        event.origin !== location.origin ||
        event.source !== frame.current?.contentWindow
      )
        return;
      const parsed = messageSchema.safeParse(event.data);
      if (
        parsed.success &&
        parsed.data.type === "flashcards:quiver-converted" &&
        parsed.data.requestId === requestId.current
      )
        callback.current(parsed.data.source ?? null, parsed.data.error ?? null);
    }
    window.addEventListener("message", receive);
    return () => window.removeEventListener("message", receive);
  }, []);
  return (
    <iframe
      ref={frame}
      hidden
      title="Import Quiver link"
      src={
        "/quiver/convert.html?q=" +
        encodeURIComponent(encoded) +
        "&requestId=" +
        requestId.current
      }
    />
  );
}

function ReadOnlyDiagram({
  image,
  expanded = false,
}: {
  image: string;
  expanded?: boolean;
}) {
  // The packaged LaTeX renderer owns the *display* image. The independently
  // transformed SVG/HTML layers in Quiver's embedded UI can have mismatched
  // rasterisation at fractional CSS zoom (especially curved nfold arrows).
  // Quiver remains the sole graphical editor; the image matches Anki export.
  return (
    <div className={"quiver-card-diagram" + (expanded ? " expanded" : "")}>
      <img
        className="quiver-compiled-image"
        src={image}
        alt="Rendered commutative diagram"
      />
    </div>
  );
}

export function QuiverPreview({
  target,
  workspace,
  path,
}: {
  target: DiagramTarget;
  workspace: string;
  path: string;
}) {
  const [source, setSource] = useState<string | null>(
    target.kind === "tikzcd" ? target.source : null,
  );
  const [error, setError] = useState("");
  const [rendered, setRendered] = useState<{
    source: string;
    image: string;
  } | null>(null);
  const [expanded, setExpanded] = useState(false);
  useEffect(() => {
    setSource(target.kind === "tikzcd" ? target.source : null);
    setError("");
    // Quiver can export exactly the same canonical source that the legacy
    // importer already supplied. Retain its compiled image in that case:
    // `source` will not change, so the rendering effect will not rerun.
    // A *different* source is handled by the rendering effect below, and
    // its identity check prevents displaying the old image.
    setExpanded(false);
  }, [target.kind, target.source]);
  useEffect(() => {
    if (source === null) return;
    let current = true;
    setRendered(null);
    setError("");
    void request(
      { action: "render-diagram", workspace, path, source },
      renderedDiagramSchema,
    ).then(
      (result) => {
        if (!current) return;
        if (result.source !== source || result.path !== path) {
          setError("The diagram preview belongs to another document revision.");
          return;
        }
        setRendered({
          source,
          image:
            "data:image/svg+xml;charset=utf-8," +
            encodeURIComponent(result.svg),
        });
      },
      (failure) => {
        if (current) setError(String(failure));
      },
    );
    return () => {
      current = false;
    };
  }, [source, workspace, path]);
  return (
    <>
      {target.kind === "quiver-url" && source === null && !error && (
        <LegacyConverter
          encoded={target.encoded!}
          onResult={(converted, failure) => {
            setSource(converted);
            setError(failure ?? "");
          }}
        />
      )}
      {error && <Alert color="red">{error}</Alert>}
      {source !== null && !rendered && !error && (
        <Text size="xs" c="dimmed">
          Compiling diagram…
        </Text>
      )}
      {source !== null && rendered?.source === source && !error && (
        <>
          <ReadOnlyDiagram image={rendered.image} />
          <Button
            variant="subtle"
            size="compact-xs"
            mt={6}
            onClick={() => setExpanded(true)}
          >
            View larger
          </Button>
          <Modal
            opened={expanded}
            onClose={() => setExpanded(false)}
            fullScreen
            title="Commutative diagram"
            className="quiver-modal"
          >
            <ReadOnlyDiagram image={rendered.image} expanded />
          </Modal>
        </>
      )}
    </>
  );
}

export function QuiverEditor({
  initial,
  onApply,
  onClose,
}: {
  initial: DiagramTarget | null;
  onApply: (source: string) => void;
  onClose: () => void;
}) {
  const frame = useRef<HTMLIFrameElement>(null);
  const sessionId = useRef(crypto.randomUUID());
  const pending = useRef<{
    id: string;
    resolve: (source: string) => void;
    reject: (error: Error) => void;
  } | null>(null);
  const [source, setSource] = useState<string | null>(
    initial?.kind === "quiver-url" ? null : (initial?.source ?? EMPTY_TIKZCD),
  );
  const [macros, setMacros] = useState<Record<string, string> | null>(null);
  const [hostReady, setHostReady] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [warnings, setWarnings] = useState<string[]>([]);
  useEffect(() => {
    let active = true;
    quiverMacros().then(
      (value) => {
        if (active) setMacros(value);
      },
      (failure) => {
        if (active) setError(String(failure));
      },
    );
    return () => {
      active = false;
    };
  }, []);
  useEffect(() => {
    if (!hostReady || source === null || macros === null) return;
    frame.current?.contentWindow?.postMessage(
      {
        type: "zettlr-quiver:load",
        sessionId: sessionId.current,
        revision: 1,
        source,
        macros,
        theme: "light",
      },
      location.origin,
    );
    frame.current?.contentWindow?.postMessage(
      {
        type: "zettlr-quiver:display",
        sessionId: sessionId.current,
        revision: 1,
        fullscreen: true,
      },
      location.origin,
    );
  }, [hostReady, macros, source]);

  function requestCurrentSource(): Promise<string> {
    return new Promise((resolve, reject) => {
      if (!loaded || !frame.current?.contentWindow) {
        reject(new Error("Quiver is not ready to export this diagram."));
        return;
      }
      const id = crypto.randomUUID();
      pending.current?.reject(new Error("Superseded Quiver export."));
      pending.current = { id, resolve, reject };
      frame.current.contentWindow.postMessage(
        {
          action: "source",
          sessionId: sessionId.current,
          revision: 1,
          requestId: id,
        },
        location.origin,
      );
    });
  }
  async function useDiagram() {
    if (busy || !loaded || error) return;
    setBusy(true);
    try {
      onApply(await requestCurrentSource());
    } catch (failure) {
      setError(String(failure));
    } finally {
      setBusy(false);
    }
  }
  const applyRef = useRef(useDiagram);
  applyRef.current = useDiagram;
  const closeRef = useRef(onClose);
  closeRef.current = onClose;
  useEffect(() => {
    function receive(event: MessageEvent) {
      if (
        event.origin !== location.origin ||
        event.source !== frame.current?.contentWindow
      )
        return;
      const parsed = messageSchema.safeParse(event.data);
      if (!parsed.success) return;
      const message = parsed.data;
      if (message.type === "zettlr-quiver:ready") {
        setHostReady(true);
        return;
      }
      if (message.sessionId !== sessionId.current || message.revision !== 1)
        return;
      if (message.type === "zettlr-quiver:loaded") {
        const errors = (message.diagnostics ?? []).filter(
          (d) => d.severity === "error",
        );
        if (errors.length) setError(errors.map((d) => d.message).join("; "));
        else setLoaded(true);
        setWarnings(
          (message.diagnostics ?? [])
            .filter((d) => d.severity === "warning")
            .map((d) => d.message),
        );
      } else if (message.type === "zettlr-quiver:error") {
        setError(message.message ?? "Quiver failed to open the diagram.");
      } else if (message.type === "zettlr-quiver:save") {
        void applyRef.current();
      } else if (message.type === "zettlr-quiver:close-request") {
        closeRef.current();
      } else if (
        message.event === "reply" &&
        message.action === "source" &&
        message.requestId === pending.current?.id
      ) {
        const request = pending.current;
        pending.current = null;
        if (message.status === "ok" && typeof message.source === "string")
          request!.resolve(message.source);
        else
          request!.reject(
            new Error(message.error ?? "Quiver refused to export."),
          );
      }
    }
    window.addEventListener("message", receive);
    return () => {
      window.removeEventListener("message", receive);
      pending.current?.reject(new Error("The diagram editor was closed."));
      pending.current = null;
    };
  }, []);

  return (
    <Modal
      opened
      onClose={onClose}
      title="Edit commutative diagram — Quiver"
      fullScreen
      closeOnEscape={false}
      className="quiver-modal"
    >
      <div className="quiver-dialog">
        {initial?.kind === "quiver-url" && source === null && !error && (
          <LegacyConverter
            encoded={initial.encoded!}
            onResult={(converted, failure) => {
              setSource(converted);
              setError(failure ?? "");
            }}
          />
        )}
        {source !== null && (
          <iframe
            ref={frame}
            src="/quiver/zettlr-host.html"
            className="quiver-edit-frame"
            title="Quiver diagram editor"
          />
        )}
        {source === null && !error && (
          <Group>
            <Loader size="sm" />
            <Text>Importing Quiver diagram…</Text>
          </Group>
        )}
        {error && (
          <Alert color="red" title="Diagram error">
            {error}
          </Alert>
        )}
        {warnings.length > 0 && (
          <Text size="xs" c="orange">
            {warnings.join("; ")}
          </Text>
        )}
        <Group justify="flex-end">
          <Button variant="default" onClick={onClose}>
            Cancel
          </Button>
          <Button
            disabled={!loaded || !!error}
            loading={busy}
            onClick={() => void useDiagram()}
          >
            Use diagram
          </Button>
        </Group>
      </div>
    </Modal>
  );
}
