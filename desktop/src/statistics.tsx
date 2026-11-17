import { useEffect, useRef, useState } from "react";
import {
  Alert,
  Button,
  Loader,
  Modal,
  Stack,
  Table,
  Text,
} from "@mantine/core";
import {
  analysisListSchema,
  analysisResultSchema,
  request,
  type Analysis,
  type AnalysisTable,
} from "./bridge";

const numbers = new Intl.NumberFormat(undefined, {
  maximumSignificantDigits: 6,
});

export function Statistics({
  record,
  onClose,
}: {
  record: string;
  onClose: () => void;
}) {
  const [analyses, setAnalyses] = useState<Analysis[]>([]);
  const [result, setResult] = useState<AnalysisTable | null>(null);
  const [error, setError] = useState("");
  const [pending, setPending] = useState(true);
  const [selected, setSelected] = useState("");
  const generation = useRef(0);
  useEffect(() => {
    let active = true;
    request({ action: "analysis-list" }, analysisListSchema)
      .then((items) => {
        if (active) setAnalyses(items);
      })
      .catch((failure) => {
        if (active) setError(String(failure));
      })
      .finally(() => {
        if (active) setPending(false);
      });
    return () => {
      active = false;
      generation.current++;
    };
  }, []);

  async function run(analysis: Analysis) {
    const token = ++generation.current;
    setSelected(analysis.name);
    setResult(null);
    setError("");
    setPending(true);
    try {
      const table = await request(
        { action: "analysis-run", record, name: analysis.name },
        analysisResultSchema,
      );
      if (token !== generation.current) return;
      if ("kind" in table) {
        setError(table.message);
        if (table.kind === "UnknownAnalysis") {
          const items = await request(
            { action: "analysis-list" },
            analysisListSchema,
          );
          if (token === generation.current) setAnalyses(items);
        }
      } else setResult(table);
    } catch (failure) {
      if (token === generation.current) setError(String(failure));
    } finally {
      if (token === generation.current) setPending(false);
    }
  }

  return (
    <Modal
      opened
      title="Statistics"
      onClose={onClose}
      size="xl"
      closeOnEscape={false}
      onKeyDown={(event) => {
        if (event.key === "Escape") {
          event.preventDefault();
          event.stopPropagation();
          onClose();
        }
      }}
    >
      <Stack className="statistics">
        {analyses.map((analysis) => (
          <Stack key={analysis.name} gap="xs">
            <Button
              variant={selected === analysis.name ? "light" : "default"}
              onClick={() => void run(analysis)}
            >
              {analysis.title}
            </Button>
            <Text size="sm">{analysis.summary}</Text>
            {analysis.failure && (
              <Text size="sm" c="red">
                {analysis.failure}
              </Text>
            )}
          </Stack>
        ))}
        {pending && <Loader aria-label="Running analysis" />}
        {error && (
          <Alert color="red" title="Analysis could not run">
            {error}
          </Alert>
        )}
        {result && (
          <>
            <Table.ScrollContainer minWidth={550}>
              <Table captionSide="top" striped>
                <Table.Caption>{result.analysis.title}</Table.Caption>
                <Table.Thead>
                  <Table.Tr>
                    {result.columns.map((column, index) => (
                      <Table.Th key={index}>
                        {column.name}
                        {column.unit && (
                          <Text size="xs" c="dimmed">
                            {column.unit}
                          </Text>
                        )}
                      </Table.Th>
                    ))}
                  </Table.Tr>
                </Table.Thead>
                <Table.Tbody>
                  {result.rows.map((row, index) => (
                    <Table.Tr key={index}>
                      {row.map((cell, column) => (
                        <Table.Td
                          key={column}
                          title={cell === null ? "Not recorded" : undefined}
                        >
                          {cell === null
                            ? "—"
                            : typeof cell === "number"
                              ? numbers.format(cell)
                              : cell}
                        </Table.Td>
                      ))}
                    </Table.Tr>
                  ))}
                </Table.Tbody>
              </Table>
            </Table.ScrollContainer>
            {!result.rows.length && <Text>No observations yet.</Text>}
          </>
        )}
      </Stack>
    </Modal>
  );
}
