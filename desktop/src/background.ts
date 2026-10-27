// Background card summaries, search, and Problems use one cooperative
// priority boundary. A quiet period after user input reserves the next frames
// for editing; idle work resumes automatically when input stops.
let inputDeadline = 0;

export function noteForegroundInput() {
  inputDeadline = performance.now() + 350;
}

export async function backgroundTurn(): Promise<void> {
  while (true) {
    const remaining = inputDeadline - performance.now();
    if (remaining > 0) {
      await new Promise<void>((resolve) =>
        window.setTimeout(resolve, remaining),
      );
      continue;
    }
    await new Promise<void>((resolve) => {
      if (typeof window.requestIdleCallback === "function")
        window.requestIdleCallback(() => resolve(), { timeout: 250 });
      else window.setTimeout(resolve, 16);
    });
    if (performance.now() >= inputDeadline) return;
  }
}
