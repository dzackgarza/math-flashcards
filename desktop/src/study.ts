import { useCallback, useEffect, useRef } from "react";
import { z } from "zod";
import { request, studyOpenSchema, type StudyOpen } from "./bridge";

// React effect cleanup closes the previous view before the next one starts:
// https://react.dev/reference/react/useEffect
export function useEditorViews(
  workspace: string,
  deck: string | null,
  cardId: string | null,
  reportError: (message: string) => void,
) {
  const opening = useRef<Promise<StudyOpen> | null>(null);
  const writing = useRef<Promise<void>>(Promise.resolve());
  const finish = useRef<(() => void) | null>(null);

  useEffect(() => {
    opening.current = workspace
      ? request({ action: "study-open", workspace }, studyOpenSchema)
      : null;
    void opening.current?.catch((failure) => reportError(String(failure)));
  }, [workspace, reportError]);

  useEffect(() => {
    const ready = opening.current;
    if (!workspace || !deck || !cardId || !ready) return;
    // Monotonic duration, independent of wall-clock changes:
    // https://developer.mozilla.org/en-US/docs/Web/API/Performance/now
    const started = performance.now();
    let unfocused = 0;
    let away = document.hidden || !document.hasFocus() ? started : null;
    const focus = () => {
      const now = performance.now();
      if (document.hidden || !document.hasFocus()) {
        away ??= now;
      } else if (away !== null) {
        unfocused += now - away;
        away = null;
      }
    };
    window.addEventListener("focus", focus);
    window.addEventListener("blur", focus);
    document.addEventListener("visibilitychange", focus);
    let ended = false;
    const end = () => {
      if (ended) return;
      ended = true;
      window.removeEventListener("focus", focus);
      window.removeEventListener("blur", focus);
      document.removeEventListener("visibilitychange", focus);
      const now = performance.now();
      if (away !== null) unfocused += now - away;
      const shown_ms = Math.round(now - started);
      const unfocused_ms = Math.round(unfocused);
      writing.current = writing.current.then(async () => {
        if ((await ready).state === "Unattached") return;
        await request(
          {
            action: "study-viewed",
            workspace,
            deck,
            card_id: cardId,
            shown_ms,
            unfocused_ms,
          },
          z.strictObject({}),
        );
      });
      void writing.current.catch((failure) => reportError(String(failure)));
    };
    finish.current = end;
    return end;
  }, [workspace, deck, cardId, reportError]);

  return useCallback(() => {
    finish.current?.();
    return writing.current;
  }, []);
}
