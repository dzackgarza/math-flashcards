import { EditorView, WidgetType } from "@codemirror/view";
import { renderBlockWidgets } from "@dzack/pandoc-editor/renderers/base-renderer";
import { decodeString } from "micromark-util-decode-string";
import { convertFileSrc, isTauri } from "@tauri-apps/api/core";
import { lookup } from "mrmime";

// The shared editor's render-math.ts supplies this WidgetType/renderBlockWidgets
// construction. Its renderer owns line layout, syntax nodes, and widget lifetime.
class CardImage extends WidgetType {
  constructor(
    readonly url: string,
    readonly alt: string,
    readonly mime: string,
  ) {
    super();
  }
  eq(other: CardImage) {
    return (
      other.url === this.url &&
      other.alt === this.alt &&
      other.mime === this.mime
    );
  }
  toDOM(view: EditorView) {
    const container = document.createElement("span");
    const image = document.createElement("img");
    image.alt = this.alt;
    image.className = "card-image";
    container.append(image);
    image.onload = () => view.requestMeasure();
    image.onerror = () => {
      URL.revokeObjectURL(image.src);
      container.textContent = `Cannot decode image: ${this.alt}`;
      container.setAttribute("role", "alert");
      view.requestMeasure();
    };
    // Digest paths have no extension. Tauri cannot infer SVG's MIME from bytes;
    // a typed Blob preserves the authored file type on both browser engines.
    // https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL_static
    void fetch(this.url)
      .then(async (response) => {
        if (!response.ok)
          throw new Error(`Image request failed: ${response.status}`);
        const bytes = await response.arrayBuffer();
        if (container.dataset.disposed) return;
        image.src = URL.createObjectURL(new Blob([bytes], { type: this.mime }));
      })
      .catch((failure) => {
        if (container.dataset.disposed) return;
        container.textContent = `Cannot load image: ${String(failure)}`;
        container.setAttribute("role", "alert");
        view.requestMeasure();
      });
    return container;
  }
  destroy(dom: HTMLElement) {
    dom.dataset.disposed = "true";
    const image = dom.querySelector("img");
    if (image?.src.startsWith("blob:")) URL.revokeObjectURL(image.src);
  }
}

export function cardImages(
  media: Record<string, string>,
  references: Record<string, string>,
  scope: "study" | "workspace",
  revision: string,
) {
  return renderBlockWidgets(
    ["Image"],
    (node) => node.name === "Image",
    (state, ref) => {
      const node = ref.node;
      const marks = node.getChildren("LinkMark");
      const alt = decodeString(state.sliceDoc(marks[0].to, marks[1].from));
      const target = node.getChild("URL");
      let name: string | undefined;
      if (target) {
        const raw = state.sliceDoc(target.from, target.to);
        name = decodeString(raw.startsWith("<") ? raw.slice(1, -1) : raw);
      } else {
        const labelNode = node.getChild("LinkLabel");
        const label = (text: string) =>
          decodeString(text).trim().replace(/\s+/g, " ").toUpperCase();
        const reference = label(
          labelNode && labelNode.to > labelNode.from + 2
            ? state.sliceDoc(labelNode.from + 1, labelNode.to - 1)
            : alt,
        );
        name = references[reference];
      }
      if (name === undefined || media[name] === undefined)
        throw new Error(
          `No retained media for image: ${state.sliceDoc(node.from, node.to)}`,
        );
      const filename = decodeURIComponent(new URL(name, "file:///").pathname);
      const mime = lookup(filename);
      if (!mime) throw new Error(`Unknown image type: ${name}`);
      const url = isTauri()
        ? convertFileSrc(media[name]) +
          "?revision=" +
          encodeURIComponent(revision)
        : `/api/${scope}-media?` +
          new URLSearchParams({
            path: media[name],
            name: filename,
            revision,
          });
      return new CardImage(url, alt, mime);
    },
  );
}
