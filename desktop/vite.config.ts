import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import { viteStaticCopy } from "vite-plugin-static-copy";
import { spawn } from "node:child_process";
import { readFile } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { text } from "node:stream/consumers";
import { fileURLToPath } from "node:url";
import pLimit from "p-limit";
import { z } from "zod";

const checkerIdentity = createHash("sha256");
const parserIdentity = createHash("sha256");
for (const source of [
  "./src/cards.ts",
  "./src/search.ts",
  "./bun.lock",
  import.meta.resolve("@lezer/markdown"),
])
  parserIdentity
    .update(readFileSync(new URL(source, import.meta.url)))
    .update("\0");
for (const source of [
  "./src/cards.ts",
  "./src/math.ts",
  "./src/problems.ts",
  "./src/bridge.ts",
  "./bun.lock",
  import.meta.resolve("@lezer/markdown"),
]) {
  checkerIdentity
    .update(readFileSync(new URL(source, import.meta.url)))
    .update("\0");
}

// Vite's development middleware runs the same bridge as the native command.
// https://vite.dev/guide/api-plugin.html#configureserver
function workbenchBackend(): Plugin {
  return {
    name: "workbench-backend",
    configureServer(server) {
      // Separate limits reserve foreground capacity during verification:
      // https://github.com/sindresorhus/p-limit#usage
      const foreground = pLimit(1);
      const background = pLimit(1);
      const watched = new Set<string>();
      server.middlewares.use("/api/watch", async (request, response) => {
        if (
          request.method !== "POST" ||
          request.headers["x-flashcards"] !== "1"
        ) {
          response
            .writeHead(403)
            .end("Use the editor to access this endpoint.");
          return;
        }
        const root = await text(request);
        if (!watched.has(root)) {
          watched.add(root);
          server.watcher.add(root);
        }
        response.writeHead(204).end();
      });
      for (const event of ["add", "change", "unlink"] as const)
        server.watcher.on(event, (path) => {
          for (const root of watched)
            if (path.startsWith(root + "/"))
              server.ws.send("flashcards:changed", { root, path });
        });
      server.middlewares.use("/api/request", async (request, response) => {
        if (
          request.method !== "POST" ||
          request.headers["x-flashcards"] !== "1"
        ) {
          response
            .writeHead(403)
            .end("Use the editor to access this endpoint.");
          return;
        }
        const body = await text(request);
        // Installation prepares this interpreter; document work never installs dependencies.
        const script = fileURLToPath(new URL("./backend.py", import.meta.url));
        const scope = z
          .object({ action: z.string() })
          .safeParse(JSON.parse(body));
        if (!scope.success) {
          response.writeHead(400).end(scope.error.message);
          return;
        }
        const { action } = scope.data;
        const queue = [
          "assets",
          "asset-version",
          "problems",
          "store-problems",
          "search",
          "store-search",
          "cache-manifest",
          "sources",
          "checks",
          "cached-checks",
          "review",
          "generate",
          "list",
        ].includes(action)
          ? background
          : foreground;
        await queue(async () => {
          let python: string;
          try {
            python = (
              await readFile(new URL("./runtime.txt", import.meta.url), "utf8")
            ).trim();
          } catch (error) {
            response
              .writeHead(500)
              .end(
                "The prepared Python runtime is missing. Run just desktop-dependencies. " +
                  String(error),
              );
            return;
          }
          await new Promise<void>((resolve) => {
            const child = spawn(python, ["-I", script]);
            const stdout = text(child.stdout);
            const stderr = text(child.stderr);
            child.on("error", (error) => {
              response.writeHead(500).end(error.message);
              resolve();
            });
            child.on("close", async (code) => {
              if (response.writableEnded) {
                resolve();
                return;
              }
              const result = await stdout;
              const diagnostics = await stderr;
              response.setHeader(
                "Content-Type",
                code === 0 ? "application/json" : "text/plain",
              );
              response
                .writeHead(code === 0 ? 200 : 422)
                .end(code === 0 ? result : diagnostics);
              resolve();
            });
            child.stdin.end(body + "\n");
          });
        });
      });
    },
  };
}

export default defineConfig({
  resolve: {
    preserveSymlinks: true,
    dedupe: [
      "@codemirror/state",
      "@codemirror/view",
      "@codemirror/language",
      "@lezer/common",
      "@lezer/highlight",
      "@lezer/markdown",
    ],
  },
  define: {
    __PARSER_IDENTITY__: JSON.stringify(parserIdentity.digest("hex")),
    __CHECKER_IDENTITY__: JSON.stringify(checkerIdentity.digest("hex")),
    __DEFAULT_WORKSPACE__: JSON.stringify(
      fileURLToPath(new URL("../decks", import.meta.url)),
    ),
  },
  plugins: [
    react(),
    workbenchBackend(),
    viteStaticCopy({
      targets: [
        {
          src: "node_modules/mathjax/**/*",
          dest: "mathjax",
          rename: { stripBase: 2 },
        },
        {
          src: "node_modules/@mathjax/mathjax-newcm-font/chtml/**/*",
          dest: "fonts/mathjax-newcm-font/chtml",
          rename: { stripBase: 4 },
        },
        // Reuse the maintained Quiver editor fork, not a second diagram
        // implementation. Its KaTeX and host bridge are part of the installed
        // release, so cards can be edited and viewed offline.
        {
          src: "../../visual-tikz-editor/vendor/quiver/src/**/*",
          dest: "quiver",
          rename: { stripBase: 4 },
          transform(content, filename) {
            if (filename.endsWith("/zettlr-host.mjs")) {
              // The passive flashcard view uses Quiver's own embedded mode
              // and viewport fit, rather than attempting to scale its SVG
              // ourselves. The modal retains the ordinary Quiver controls.
              const imports = "{ UI, load_katex }";
              const display =
                'document.body.classList.toggle("zettlr-fullscreen", fullscreen);';
              const origin =
                "const host_origin = new URL(document.referrer).origin;";
              if (
                !content.includes(imports) ||
                !content.includes(display) ||
                !content.includes(origin)
              )
                throw new Error("The vendored Quiver host protocol changed.");
              return (
                content
                  // The Tauri resource protocol does not set iframe referrers.
                  // Both the iframe and its owning card editor are same-origin
                  // local resources. Keep the existing message-origin validation
                  // without requiring the optional Referer header.
                  .replace(
                    origin,
                    "const host_origin = window.location.origin;",
                  )
                  .replace(imports, "{ UI, UIMode, load_katex }")
                  .replace(
                    display,
                    display +
                      `
        if (message.readonly === true) {
            ui.switch_mode(new UIMode.Embedded());
            // WebKit/Tauri may retain a pending FontFaceSet.ready promise
            // even though the diagram has been laid out. Do not make the
            // visible preview depend on that optional completion signal.
            // Quiver's scale_to_fit applies a *relative* zoom via pan_view.
            // Multiple fits (initial layout, font settlement, resize) must
            // first reset zoom; otherwise every call exponentially shrinks
            // the same diagram until it is unreadable.
            const fit = () => requestAnimationFrame(() => requestAnimationFrame(() => {
                ui.pan_to(ui.view, 0);
                ui.scale_to_fit();
            }));
            fit();
            document.fonts.ready.then(fit);
            window.addEventListener("resize", fit, { passive: true });
        }`,
                  )
              );
            }
            if (!filename.endsWith("/parser.mjs")) return content;
            // The pinned Quiver exporter emits `Rightarrow, nfold` for
            // 2-cells, but its TikZ-cd importer only accepts `double line`.
            // Teach that importer its own option so every emitted diagram can
            // be reopened without losing higher-cell semantics. Do not patch
            // the separate visual-tikz-editor checkout.
            const needle = 'if (this.eat("double line")) {';
            if (!content.includes(needle))
              throw new Error(
                "The vendored Quiver parser changed its level grammar.",
              );
            return content.replace(
              needle,
              'if (this.eat("nfold")) { edge.options.level = 2; return; }\n        ' +
                needle,
            );
          },
        },
        {
          src: "../../visual-tikz-editor/vendor/quiver/LICENSE",
          dest: "quiver",
          rename: { stripBase: 3 },
        },
        {
          src: "../../visual-tikz-editor/vendor/quiver/KATEX-LICENSE.txt",
          dest: "quiver",
          rename: { stripBase: 3 },
        },
      ],
    }),
  ],
  clearScreen: false,
  server: {
    port: 1420,
    strictPort: true,
    host: "127.0.0.1",
    watch: { ignored: ["**/src-tauri/**", "**/test-artifacts/**"] },
  },
});
