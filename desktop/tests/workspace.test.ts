import { afterEach, expect, test } from "bun:test";
import { mkdtemp, mkdir } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";
import { z } from "zod";
import {
  documentSchema,
  assetsSchema,
  generatedSchema,
  manifestSchema,
  cachedManifestSchema,
  sourcesSchema,
  checksSchema,
  problemCacheSchema,
  problemStoredSchema,
  searchCacheSchema,
  organizedSchema,
  reviewSchema,
  workspaceSchema,
  type Request,
} from "../src/bridge";

const temporaryWorkspaces: string[] = [];
afterEach(() => {
  for (const directory of temporaryWorkspaces.splice(0)) {
    const cleanup = Bun.spawnSync(["trash", directory]);
    expect(cleanup.exitCode, cleanup.stderr.toString()).toBe(0);
  }
});

test("search summaries persist with exact source and parser identities", async () => {
  const workspace = await mkdtemp(join(tmpdir(), "flashcards-search-cache-"));
  temporaryWorkspaces.push(workspace);
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode).toBe(0);
  const path = "Study.md";
  const source =
    '---\ntitle: "Study"\n---\n\n::: {.front card-id="proof"}\nA question\n:::\n\n::: {.back card-id="proof"}\nA proof\n:::\n';
  await Bun.write(join(workspace, path), source);
  const revision = new Bun.CryptoHasher("sha256").update(source).digest("hex");
  const producer = new Bun.CryptoHasher("sha256")
    .update("parser fixture")
    .digest("hex");
  const call = async (payload: Request) => {
    const process = Bun.spawn([find.stdout.toString().trim(), backend], {
      stdin: new Blob([JSON.stringify(payload) + "\n"]),
      stdout: "pipe",
      stderr: "pipe",
      env: {
        ...Bun.env,
        XDG_CACHE_HOME: join(workspace, "cache"),
        UV_OFFLINE: "1",
      },
    });
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    expect(await process.exited, error).toBe(0);
    return searchCacheSchema.parse(JSON.parse(output));
  };
  const input = {
    workspace,
    generation: 4,
    producer,
    entries: [{ path, revision }],
  };
  expect((await call({ ...input, action: "search" })).results).toEqual([
    { state: "pending", path },
  ]);
  const cards = [
    {
      id: "proof",
      label: "A question",
      front: "A question",
      back: "A proof",
      tags: "",
    },
  ];
  const stored = await call({
    ...input,
    action: "store-search",
    entries: [{ path, revision, cards }],
  });
  expect(stored.results).toEqual([
    { state: "ready", path, revision, producer, source, cards },
  ]);
  const reused = await call({ ...input, generation: 5, action: "search" });
  expect(reused.session).toEqual({ root: workspace, generation: 5 });
  expect(reused.results).toEqual(stored.results);
  const damaged = Bun.spawnSync([
    find.stdout.toString().trim(),
    "-c",
    "import sqlite3, sys; connection=sqlite3.connect(sys.argv[1]); connection.execute(\"UPDATE search_summaries SET record = 'damaged'\"); connection.commit()",
    join(workspace, "cache/math-flashcards/derived.sqlite3"),
  ]);
  expect(damaged.exitCode, damaged.stderr.toString()).toBe(0);
  expect((await call({ ...input, action: "search" })).results[0]).toMatchObject(
    { state: "failed", path, kind: "CacheFailure" },
  );
  expect(
    (
      await call({
        ...input,
        action: "store-search",
        entries: [{ path, revision, cards }],
      })
    ).results,
  ).toEqual(stored.results);
  expect(
    (await call({ ...input, producer: "0".repeat(64), action: "search" }))
      .results,
  ).toEqual([{ state: "pending", path }]);
  const edited = source.replace("A proof", "B proof");
  const changed = Bun.spawnSync([
    find.stdout.toString().trim(),
    "-c",
    "from pathlib import Path; import os, sys; path=Path(sys.argv[1]); before=path.stat(); path.write_text(path.read_text().replace('A proof', 'B proof')); os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns)); after=path.stat(); assert before.st_size == after.st_size and before.st_mtime_ns == after.st_mtime_ns",
    join(workspace, path),
  ]);
  expect(changed.exitCode, changed.stderr.toString()).toBe(0);
  expect((await call({ ...input, action: "search" })).results).toEqual([
    { state: "superseded", path },
  ]);
  const current = new Bun.CryptoHasher("sha256").update(edited).digest("hex");
  expect(
    (
      await call({
        ...input,
        entries: [{ path, revision: current }],
        action: "search",
      })
    ).results,
  ).toEqual([{ state: "pending", path }]);
  expect(
    (
      await call({
        ...input,
        action: "store-search",
        entries: [{ path, revision, cards }],
      })
    ).results,
  ).toEqual([{ state: "superseded", path }]);
  expect(await Bun.file(join(workspace, path)).text()).toBe(edited);
}, 30000);

test("generation bundles the prepared renderer pair without network access", async () => {
  const workspace = await mkdtemp(join(tmpdir(), "flashcards-offline-export-"));
  temporaryWorkspaces.push(workspace);
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode).toBe(0);
  const resources = join(workspace, "runtime");
  await mkdir(join(resources, "asset-sets"), { recursive: true });
  for (const name of ["backend.py", "paired-cards.lua", "assets.json"])
    await Bun.write(
      join(resources, name),
      Bun.file(resolve(import.meta.dir, "..", name)),
    );
  const initialAssets = assetsSchema.parse(
    await Bun.file(join(resources, "assets.json")).json(),
  );
  await Bun.write(
    join(resources, "asset-sets", initialAssets.identity + ".json"),
    Bun.file(join(resources, "assets.json")),
  );
  const source = await Bun.file(
    resolve(import.meta.dir, "../../decks/Analysis/Precalculus.md"),
  ).text();
  await Bun.write(join(workspace, "Study.md"), source);
  const call = async (payload: Request) => {
    const process = Bun.spawn(
      [
        "unshare",
        "--user",
        "--map-root-user",
        "--net",
        find.stdout.toString().trim(),
        join(resources, "backend.py"),
      ],
      {
        stdin: new Blob([JSON.stringify(payload) + "\n"]),
        stdout: "pipe",
        stderr: "pipe",
        env: { ...Bun.env, XDG_CACHE_HOME: join(workspace, "cache") },
      },
    );
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    expect(await process.exited, error).toBe(0);
    return JSON.parse(output);
  };
  const assets = assetsSchema.parse(await call({ action: "assets" }));
  const update = Bun.spawnSync(
    [
      find.stdout.toString().trim(),
      "-c",
      "from pathlib import Path; import backend; old=backend.installed_assets(); macros=old.macros | {'flashcardsAssetProof': r'\\mathrm{updated}'}; updated=backend.AssetSet(identity=backend.asset_identity(macros, old.stmaryrd, old.renderer), macros=macros, stmaryrd=old.stmaryrd, renderer=old.renderer); directory=Path('asset-sets'); (directory / (updated.identity + '.json')).write_text(updated.model_dump_json()); Path('assets.json').write_text(updated.model_dump_json())",
    ],
    { cwd: resources },
  );
  expect(update.exitCode, update.stderr.toString()).toBe(0);
  const updated = assetsSchema.parse(await call({ action: "assets" }));
  expect(updated.identity).not.toBe(assets.identity);
  const result = generatedSchema.parse(
    await call({
      action: "generate",
      workspace,
      path: "Study.md",
      assets: assets.identity,
    }),
  );
  expect(result.status).toBe("Up to date");
  const mediaFile = Bun.spawnSync(["unzip", "-p", result.package, "media"]);
  expect(mediaFile.exitCode).toBe(0);
  const media = z
    .record(z.string(), z.string())
    .parse(JSON.parse(mediaFile.stdout.toString()));
  const macroFile = Object.entries(media).find(
    ([, name]) => name === "_ankdown_macros.js",
  );
  if (!macroFile)
    throw new Error("The package did not include its renderer script.");
  const script = Bun.spawnSync(["unzip", "-p", result.package, macroFile[0]]);
  expect(script.exitCode).toBe(0);
  // The protected script assignment is the exporter's package-media contract.
  const [stmaryrd, assignment] = z
    .tuple([z.string(), z.string()])
    .parse(script.stdout.toString().split("\nwindow.ANKDOWN_MACROS = "));
  expect(stmaryrd).toBe(assets.stmaryrd);
  expect(assignment.endsWith(";")).toBe(true);
  expect(
    assetsSchema.shape.macros.parse(JSON.parse(assignment.slice(0, -1))),
  ).toEqual(assets.macros);
  const previous = checksSchema.parse(
    await call({
      action: "checks",
      workspace,
      generation: 1,
      paths: ["Study.md"],
      assets: assets.identity,
    }),
  );
  expect(previous.results[0]).toMatchObject({
    state: "ready",
    assets: assets.identity,
    status: "Up to date",
  });
  const current = checksSchema.parse(
    await call({
      action: "checks",
      workspace,
      generation: 2,
      paths: ["Study.md"],
      assets: updated.identity,
    }),
  );
  expect(current.results[0]).toMatchObject({
    state: "ready",
    assets: updated.identity,
    status: "Unsynced",
    reasons: ["The renderer assets changed."],
  });
  const unavailable = checksSchema.parse(
    await call({
      action: "checks",
      workspace,
      generation: 3,
      paths: ["Study.md"],
      assets: "0".repeat(64),
    }),
  );
  expect(unavailable.results[0]).toMatchObject({
    state: "failed",
    kind: "InvalidAssets",
  });
  const adopted = generatedSchema.parse(
    await call({
      action: "generate",
      workspace,
      path: "Study.md",
      assets: updated.identity,
    }),
  );
  expect(adopted.status).toBe("Up to date");
  const adoptedScript = Bun.spawnSync([
    "unzip",
    "-p",
    adopted.package,
    macroFile[0],
  ]);
  expect(adoptedScript.exitCode).toBe(0);
  const adoptedAssignment = adoptedScript.stdout
    .toString()
    .split("\nwindow.ANKDOWN_MACROS = ")[1];
  expect(
    assetsSchema.shape.macros.parse(JSON.parse(adoptedAssignment.slice(0, -1))),
  ).toEqual(updated.macros);
}, 30000);

test("persisted problems require current file bytes, checker, and renderer identities", async () => {
  const workspace = await mkdtemp(join(tmpdir(), "flashcards-cache-"));
  temporaryWorkspaces.push(workspace);
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode).toBe(0);
  const source = await Bun.file(
    resolve(import.meta.dir, "../../decks/Analysis/Precalculus.md"),
  ).text();
  const path = "Study.md";
  await Bun.write(join(workspace, path), source);
  const revision = new Bun.CryptoHasher("sha256").update(source).digest("hex");
  const producer = new Bun.CryptoHasher("sha256")
    .update("checker-v1")
    .digest("hex");
  const assets = new Bun.CryptoHasher("sha256")
    .update("renderer-v1")
    .digest("hex");
  const call = async (payload: Request) => {
    const process = Bun.spawn([find.stdout.toString().trim(), backend], {
      stdin: new Blob([JSON.stringify(payload) + "\n"]),
      stdout: "pipe",
      stderr: "pipe",
      env: { ...Bun.env, XDG_CACHE_HOME: join(workspace, "cache") },
    });
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    expect(await process.exited, error).toBe(0);
    return JSON.parse(output);
  };
  const input = { workspace, generation: 3, producer, assets };
  const entry = { path, revision };
  const cold = problemCacheSchema.parse(
    await call({ ...input, action: "problems", entries: [entry] }),
  );
  expect(cold.results).toEqual([{ state: "pending", path }]);
  const saved = problemStoredSchema.parse(
    await call({
      ...input,
      action: "store-problems",
      entries: [{ ...entry, problems: [] }],
    }),
  );
  expect(saved.results).toEqual([{ state: "stored", path }]);
  const warm = problemCacheSchema.parse(
    await call({ ...input, action: "problems", entries: [entry] }),
  );
  expect(warm.results).toEqual([
    { state: "ready", path, revision, producer, assets, problems: [] },
  ]);
  for (const changed of [{ producer: revision }, { assets: revision }]) {
    const response = problemCacheSchema.parse(
      await call({
        ...input,
        ...changed,
        action: "problems",
        entries: [entry],
      }),
    );
    expect(response.results).toEqual([{ state: "pending", path }]);
  }
  const edited = source.replace("Precalculus", "Local study");
  await Bun.write(join(workspace, path), edited);
  const stale = problemCacheSchema.parse(
    await call({ ...input, action: "problems", entries: [entry] }),
  );
  expect(stale.results).toEqual([{ state: "superseded", path }]);
  const superseded = problemStoredSchema.parse(
    await call({
      ...input,
      action: "store-problems",
      entries: [{ ...entry, problems: [] }],
    }),
  );
  expect(superseded.results).toEqual([{ state: "superseded", path }]);
  expect(await Bun.file(join(workspace, path)).text()).toBe(edited);
}, 30000);

test("local discovery and bounded reads isolate a damaged deck and retain revision identity", async () => {
  const directory = await mkdtemp(join(tmpdir(), "flashcards-discovery-"));
  temporaryWorkspaces.push(directory);
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode).toBe(0);
  const source = await Bun.file(
    resolve(import.meta.dir, "../../decks/Analysis/Precalculus.md"),
  ).text();
  await Bun.write(join(directory, "Study.md"), source);
  await Bun.write(join(directory, "Damaged.md"), new Uint8Array([0xff, 0xfe]));
  await mkdir(join(directory, "apkg"));
  await Bun.write(join(directory, "apkg/Notes.md"), "Package notes");
  const execute = async (payload: string) => {
    const process = Bun.spawn([find.stdout.toString().trim(), backend], {
      stdin: new Blob([payload + "\n"]),
      stdout: "pipe",
      stderr: "pipe",
      env: {
        ...Bun.env,
        XDG_CACHE_HOME: join(directory, "cache"),
        UV_OFFLINE: "1",
      },
    });
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    return { code: await process.exited, output, error };
  };
  const call = async (payload: Request) => {
    const result = await execute(JSON.stringify(payload));
    expect(result.code, result.error).toBe(0);
    return JSON.parse(result.output);
  };
  for (const invalid of [
    { action: "manifest", workspace: directory },
    { action: "manifest", workspace: directory, generation: -1 },
    { action: "manifest", workspace: directory, generation: true },
    {
      action: "sources",
      workspace: directory,
      generation: 7,
      paths: ["../Outside.md"],
    },
    {
      action: "sources",
      workspace: directory,
      generation: 7,
      paths: Array(9).fill("Study.md"),
    },
    { action: "unrecognized", workspace: directory, generation: 7 },
  ]) {
    const rejected = await execute(JSON.stringify(invalid));
    expect(rejected.code).not.toBe(0);
    expect(rejected.output).toBe("");
  }
  const manifest = manifestSchema.parse(
    await call({ action: "manifest", workspace: directory, generation: 7 }),
  );
  expect(manifest).toEqual({
    session: { root: directory, generation: 7 },
    entries: [{ path: "Damaged.md" }, { path: "Study.md" }],
  });
  const coldNavigation = cachedManifestSchema.parse(
    await call({
      action: "cached-manifest",
      workspace: directory,
      generation: 7,
    }),
  );
  expect(coldNavigation).toEqual({
    state: "pending",
    session: manifest.session,
  });
  const savedNavigation = cachedManifestSchema.parse(
    await call({
      action: "cache-manifest",
      workspace: directory,
      generation: 7,
    }),
  );
  expect(savedNavigation).toEqual({ state: "cached", ...manifest });
  const cachedNavigation = cachedManifestSchema.parse(
    await call({
      action: "cached-manifest",
      workspace: directory,
      generation: 8,
    }),
  );
  expect(cachedNavigation).toEqual({
    state: "cached",
    entries: manifest.entries,
    session: { ...manifest.session, generation: 8 },
  });
  const response = sourcesSchema.parse(
    await call({
      action: "sources",
      workspace: directory,
      generation: 7,
      paths: ["Damaged.md", "Study.md"],
    }),
  );
  expect(response.session).toEqual(manifest.session);
  expect(response.results[0]).toMatchObject({
    state: "failed",
    path: "Damaged.md",
    kind: "UnreadablePath",
  });
  const study = response.results[1];
  expect(study).toEqual({
    state: "ready",
    path: "Study.md",
    source,
    revision: new Bun.CryptoHasher("sha256").update(source).digest("hex"),
  });
  const edited = source.replace("Precalculus", "Local study");
  await Bun.write(join(directory, "Study.md"), edited);
  const next = sourcesSchema.parse(
    await call({
      action: "sources",
      workspace: directory,
      generation: 8,
      paths: ["Study.md"],
    }),
  );
  expect(next.results[0]).toEqual({
    state: "ready",
    path: "Study.md",
    source: edited,
    revision: new Bun.CryptoHasher("sha256").update(edited).digest("hex"),
  });
  const checks = checksSchema.parse(
    await call({
      action: "checks",
      assets: assetsSchema.parse(await call({ action: "assets" })).identity,
      workspace: directory,
      generation: 8,
      paths: ["Damaged.md", "Study.md"],
    }),
  );
  expect(checks.results[0]).toMatchObject({
    state: "failed",
    kind: "UnreadablePath",
  });
  expect(checks.results[1]).toMatchObject({
    state: "ready",
    path: "Study.md",
    status: "Unsynced",
    revision:
      next.results[0].state === "ready" ? next.results[0].revision : "invalid",
  });
}, 30000);

test("a deck folder supports discovery, editing, and organization beside its export directory", async () => {
  const directory = await mkdtemp(join(tmpdir(), "flashcards-workspace-"));
  const workspace = join(directory, "study");
  const backend = resolve(import.meta.dir, "../backend.py");
  const find = Bun.spawnSync(["uv", "python", "find", "--script", backend]);
  expect(find.exitCode, find.stderr.toString()).toBe(0);
  const python = find.stdout.toString().trim();
  const request = async (payload: Request) => {
    const process = Bun.spawn([python, backend], {
      stdin: new Blob([JSON.stringify(payload) + "\n"]),
      stdout: "pipe",
      stderr: "pipe",
      env: { ...Bun.env, XDG_CACHE_HOME: join(directory, "cache") },
    });
    const output = await new Response(process.stdout).text();
    const error = await new Response(process.stderr).text();
    return { output, error, code: await process.exited };
  };
  const source =
    '---\ntitle: "Algebra::Groups"\n---\n\n' +
    '::: {.front card-id="identity"}\nIdentity element\n:::\n\n' +
    '::: {.back card-id="identity"}\n$eg=ge=g$\n:::\n';
  try {
    await mkdir(join(workspace, "Algebra"), { recursive: true });
    await mkdir(join(workspace, "apkg"));
    await Bun.write(join(workspace, "Algebra/Groups.md"), source);
    await Bun.write(join(workspace, "apkg/Export notes.md"), "Export metadata");
    await Bun.write(join(directory, "Outside.md"), source);

    const listed = await request({ action: "list", workspace });
    expect(listed.code, listed.error).toBe(0);
    const listing = workspaceSchema.parse(JSON.parse(listed.output));
    expect(listing.root).toBe(workspace);
    expect(listing.decks.map((deck) => deck.path)).toEqual([
      "Algebra/Groups.md",
    ]);

    const loaded = await request({
      action: "load",
      generation: 0,
      workspace,
      path: "Algebra/Groups.md",
    });
    expect(loaded.code, loaded.error).toBe(0);
    const deck = documentSchema.parse(JSON.parse(loaded.output));
    expect(deck.source).toBe(source);
    expect(deck.session).toEqual({ root: workspace, generation: 0 });
    expect(deck.package).toBe(join(workspace, "apkg/Algebra__Groups.apkg"));

    const edited = source.replace(
      "Identity element",
      "Define an identity element.",
    );
    const saved = await request({
      action: "save",
      generation: 0,
      workspace,
      path: "Algebra/Groups.md",
      source: edited,
      expected: deck.hash,
    });
    expect(saved.code, saved.error).toBe(0);
    expect(await Bun.file(join(workspace, "Algebra/Groups.md")).text()).toBe(
      edited,
    );
    const savedDeck = documentSchema.parse(JSON.parse(saved.output));
    const moved = await request({
      action: "organize",
      workspace,
      changes: [
        { path: "Groups.md", source: edited, expected: null },
        { path: "Algebra/Groups.md", source: null, expected: savedDeck.hash },
      ],
    });
    expect(moved.code, moved.error).toBe(0);
    expect(
      organizedSchema
        .parse(JSON.parse(moved.output))
        .changed.map((item) => item.path),
    ).toEqual(["Groups.md", "Algebra/Groups.md"]);
    expect(await Bun.file(join(workspace, "Groups.md")).text()).toBe(edited);
    expect(await Bun.file(join(workspace, "Algebra/Groups.md")).exists()).toBe(
      false,
    );
    const assets = await request({ action: "assets" });
    expect(assets.code, assets.error).toBe(0);
    const reviewed = await request({
      action: "review",
      workspace,
      assets: assetsSchema.parse(JSON.parse(assets.output)).identity,
    });
    expect(reviewed.code, reviewed.error).toBe(0);
    expect(
      reviewSchema
        .parse(JSON.parse(reviewed.output))
        .decks.map((item) => item.path),
    ).toEqual(["Groups.md"]);

    for (const path of ["../Outside.md", "apkg/Export notes.md"]) {
      const rejected = await request({
        action: "load",
        workspace,
        path,
        generation: 0,
      });
      expect(rejected.code).not.toBe(0);
      expect(rejected.error).toContain("deck");
      const invalidMove = await request({
        action: "organize",
        workspace,
        changes: [{ path, source, expected: null }],
      });
      expect(invalidMove.code).not.toBe(0);
      expect(invalidMove.error).toContain("deck");
    }
    expect(await Bun.file(join(directory, "Outside.md")).text()).toBe(source);
    expect(await Bun.file(join(workspace, "apkg/Export notes.md")).text()).toBe(
      "Export metadata",
    );
  } finally {
    const cleanup = Bun.spawnSync(["trash", directory]);
    expect(cleanup.exitCode, cleanup.stderr.toString()).toBe(0);
  }
}, 60000);
