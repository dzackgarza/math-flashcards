import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { MantineProvider } from "@mantine/core";
import { ModalsProvider } from "@mantine/modals";
import "@fontsource-variable/inter";
import "@mantine/core/styles.css";
import "@mantine/spotlight/styles.css";
import "./App.css";

const sans = '"Inter Variable", system-ui, sans-serif';

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <MantineProvider
      defaultColorScheme="light"
      theme={{
        primaryColor: "indigo",
        defaultRadius: "md",
        fontFamily: sans,
        headings: { fontFamily: sans, fontWeight: "600" },
      }}
    >
      <ModalsProvider>
        <App />
      </ModalsProvider>
    </MantineProvider>
  </React.StrictMode>,
);
