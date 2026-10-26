import { isAbsolute, relative } from "pathe";
import type { Entry, PackageCheck, SourceResult } from "./bridge";

export function previousPackage(check: PackageCheck | undefined) {
  if (!check) return null;
  return check.state === "ready" ? check : check.previous;
}

// Use normalized relative paths for containment, including directory events:
// https://github.com/unjs/pathe
function touches(path: string, changes: string[]) {
  return changes.some((change) => {
    const name = relative(change, path);
    return name !== ".." && !name.startsWith("../") && !isAbsolute(name);
  });
}

export function refreshTargets(
  root: string,
  entries: Entry[],
  sources: ReadonlyMap<string, SourceResult>,
  checks: ReadonlyMap<string, PackageCheck>,
  pending: ReadonlySet<string>,
  changes: string[] | null,
) {
  const read = new Set<string>();
  const verify = new Set<string>();
  for (const { path } of entries) {
    const changed = changes === null || touches(root + "/" + path, changes);
    if (changed || !sources.has(path) || pending.has(path)) read.add(path);
    const check = checks.get(path);
    const previous = previousPackage(check);
    if (
      changed ||
      !check ||
      check.state === "pending" ||
      check.state === "checking" ||
      (changes && previous?.dependencies.some((path) => touches(path, changes)))
    )
      verify.add(path);
  }
  return { read, verify };
}
