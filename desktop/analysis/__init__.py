"""Independent analyses; research.md R17 owns the boundary.

SQLite URI mode=ro supplies read-only access, including during host writes:
https://docs.python.org/3/library/sqlite3.html#sqlite3-uri-tricks
"""

import importlib
import logging
import pkgutil
import sqlite3
from contextlib import closing
from pathlib import Path
from typing import Literal, Protocol, cast

from platformdirs import user_data_path
from pydantic import BaseModel, ConfigDict, FiniteFloat, RootModel

from analysis import catalog

logger = logging.getLogger(__name__)


class Value(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Analysis(Value):
    name: str
    title: str
    summary: str
    failure: str | None = None


class Column(Value):
    name: str
    unit: str | None = None


type Cell = str | int | FiniteFloat | None


class AnalysisTable(Value):
    analysis: Analysis
    columns: list[Column]
    rows: list[list[Cell]]


class AnalysisError(Value):
    kind: Literal["UnknownAnalysis", "AnalysisFailed", "RecordUnreadable"]
    message: str


class AnalysisModule(Protocol):
    title: str
    summary: str

    def run(self, connection: sqlite3.Connection) -> AnalysisTable: ...


def modules() -> list[str]:
    return [
        item.name for item in pkgutil.iter_modules(catalog.__path__) if not item.ispkg
    ]


def load(name: str) -> AnalysisModule:
    # importlib is the dynamic module boundary. The catalog contract declares
    # these attributes; metadata and returned tables are validated by Pydantic.
    return cast(AnalysisModule, importlib.import_module(f"analysis.catalog.{name}"))


def list_analyses() -> RootModel[list[Analysis]]:
    result = []
    for name in modules():
        try:
            module = load(name)
            item = Analysis(name=name, title=module.title, summary=module.summary)
        except Exception as error:
            logger.exception("Cannot import analysis %s", name)
            item = Analysis(name=name, title=name, summary="", failure=str(error))
        result.append(item)
    return RootModel[list[Analysis]](sorted(result, key=lambda item: item.title))


def run(name: str, record: str) -> AnalysisTable | AnalysisError:
    if name not in modules():
        return AnalysisError(
            kind="UnknownAnalysis", message=f"Unknown analysis: {name}"
        )
    try:
        path = Path(record).resolve(strict=True)
        root = (user_data_path("math-flashcards") / "study").resolve()
        if path.name != "record.sqlite3" or not path.is_relative_to(root):
            raise ValueError("Choose record.sqlite3 inside the Study data directory.")
        connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    except (OSError, ValueError, sqlite3.Error) as error:
        return AnalysisError(kind="RecordUnreadable", message=f"{record}: {error}")
    with closing(connection):
        try:
            connection.execute("begin")
            result = AnalysisTable.model_validate(load(name).run(connection))
            if result.analysis.name != name or any(
                len(row) != len(result.columns) for row in result.rows
            ):
                raise ValueError("The analysis returned inconsistent table metadata.")
            return result
        except Exception as error:
            logger.exception("Analysis %s failed", name)
            return AnalysisError(kind="AnalysisFailed", message=f"{name}: {error}")
