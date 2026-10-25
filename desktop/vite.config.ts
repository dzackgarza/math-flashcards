import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import { viteStaticCopy } from "vite-plugin-static-copy";
import { spawn } from "node:child_process";
import { readFile } from "node:fs/promises";
import { text } from "node:stream/consumers";
import { fileURLToPath } from "node:url";
import pLimit from "p-limit";
import { z } from "zod";

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
          "sources",
          "checks",
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
            const child = spawn(python, [script]);
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
