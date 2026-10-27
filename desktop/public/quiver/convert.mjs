// Conversion uses Quiver's own importer and exporter, not a second diagram implementation.
window.__ZETTLR_QUIVER_HOST__ = true;

const [{ DOM }, { UI, load_katex }, { QuiverImportExport }] = await Promise.all([
  import("./dom.mjs"),
  import("./ui.mjs"),
  import("./quiver.mjs"),
]);

const requestId = new URL(location.href).searchParams.get("requestId");
const rawQuery = new URL(location.href).search.slice(1).split("&");
const encoded = rawQuery.find((part) => part.startsWith("q="))?.slice(2);
const result = { type: "flashcards:quiver-converted", requestId, source: null, error: null };

try {
  if (!encoded || encoded.length > 500000) throw new Error("Invalid Quiver diagram URL.");
  await load_katex();
  const ui = new UI(new DOM.Element(document.body));
  ui.initialise();
  ui.settings.set("quiver.renderer", "katex");
  ui.settings.set("quiver.autosave", false);
  ui.settings.set("export.centre_diagram", false);
  ui.settings.set("export.standalone", false);
  QuiverImportExport.base64.import(ui, decodeURIComponent(encoded).replaceAll(" ", "+"));
  const { data } = ui.quiver.export("tikz-cd", ui.settings, ui.options(), ui.definitions());
  result.source = data.replace(/^%\s+[^\n]*#[^\n]*q=[^\n]*\n/u, "").trim();
  if (!result.source.includes("\\begin{tikzcd}"))
    throw new Error("Quiver did not export a TikZ-cd environment.");
} catch (failure) {
  result.source = null;
  result.error = String(failure);
}

window.__flashcardsQuiverConversion = result;
if (window.parent !== window) window.parent.postMessage(result, location.origin);
