import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react";
import { viteStaticCopy } from "vite-plugin-static-copy";
import { spawn } from "node:child_process";
import { text } from "node:stream/consumers";
import { fileURLToPath } from "node:url";

// Vite's development middleware runs the same bridge as the native command.
// https://vite.dev/guide/api-plugin.html#configureserver
function workbenchBackend(): Plugin {
  return {
    name: "workbench-backend",
    configureServer(server) {
      server.middlewares.use("/api/request", async (request, response) => {
        if (request.method !== "POST" || request.headers["x-flashcards"] !== "1") {
          response.writeHead(403).end("Use the editor to access this endpoint.");
          return;
        }
        const child = spawn("uv", ["run", "--locked", "--script", fileURLToPath(new URL("./backend.py", import.meta.url))]);
        const stdout = text(child.stdout);
        const stderr = text(child.stderr);
        child.on("error", (error) => response.writeHead(500).end(error.message));
        child.on("close", async (code) => {
          const result = await stdout;
          const diagnostics = await stderr;
          response.setHeader("Content-Type", code === 0 ? "application/json" : "text/plain");
          response.writeHead(code === 0 ? 200 : 422).end(code === 0 ? result : diagnostics);
        });
        child.stdin.end((await text(request)) + "\n");
      });
    },
  };
}

export default defineConfig({
  plugins: [react(), workbenchBackend(), viteStaticCopy({ targets: [{ src: "node_modules/mathjax/es5", dest: ".", rename: "mathjax" }] })],
  clearScreen: false,
  server: { port: 1420, strictPort: true, host: "127.0.0.1", watch: { ignored: ["**/src-tauri/**", "**/test-artifacts/**"] } },
});
