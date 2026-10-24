import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import { viteStaticCopy } from "vite-plugin-static-copy";
import { execFile, spawn } from "node:child_process";
import { promisify } from "node:util";
import { text } from "node:stream/consumers";
import { fileURLToPath } from "node:url";

// Vite's development middleware runs the same bridge as the native command.
// https://vite.dev/guide/api-plugin.html#configureserver
function workbenchBackend(): Plugin {
  return {
    name: "workbench-backend",
    configureServer(server) {
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
        // Listing and generation upgrade the script environment to the latest
        // versions; every request runs its interpreter, so
        // no other request reads the network.
        // https://docs.astral.sh/uv/guides/scripts/
        const script = fileURLToPath(new URL("./backend.py", import.meta.url));
        const { action } = JSON.parse(body) as { action: string };
        const uv = async (args: string[]) =>
          (
            await promisify(execFile)("uv", [...args, "--script", script])
          ).stdout.trim();
        let python: string;
        try {
          if (action === "list" || action === "generate")
            await uv(["sync", "--upgrade"]);
          python = await uv(["python", "find"]);
        } catch (error) {
          response.writeHead(500).end((error as Error).message);
          return;
        }
        const child = spawn(python, [script]);
        const stdout = text(child.stdout);
        const stderr = text(child.stderr);
        child.on("error", (error) =>
          response.writeHead(500).end(error.message),
        );
        child.on("close", async (code) => {
          const result = await stdout;
          const diagnostics = await stderr;
          response.setHeader(
            "Content-Type",
            code === 0 ? "application/json" : "text/plain",
          );
          response
            .writeHead(code === 0 ? 200 : 422)
            .end(code === 0 ? result : diagnostics);
        });
        child.stdin.end(body + "\n");
      });
    },
  };
}

export default defineConfig({
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
