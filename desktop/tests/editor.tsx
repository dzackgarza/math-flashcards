import React, { useState } from "react";
import { createRoot } from "react-dom/client";
import { MantineProvider } from "@mantine/core";
import "@mantine/core/styles.css";
import "../src/App.css";
import { SideEditor } from "../src/editor";

const source =
  "# Groups\n\n- A **group** has an identity and inverses, and this long item wraps onto another line in a narrow card editor.\n    - Nested *item*\n\n1. First axiom\n2. Second axiom\n\n> A quoted statement\n\n`identity`\n\nEnd.";

function EditorFixture() {
  const [value, setValue] = useState(source);
  return (
    <MantineProvider>
      <main style={{ width: 440, padding: 20 }}>
        <SideEditor
          side="front"
          value={value}
          mathjax={null}
          editable
          onChange={setValue}
        />
        <button>Outside the editor</button>
        <output style={{ display: "none" }}>{value}</output>
      </main>
    </MantineProvider>
  );
}

createRoot(document.getElementById("root")!).render(<EditorFixture />);
