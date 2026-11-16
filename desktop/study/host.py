"""One request per line; one writer of each workspace's learning data."""

import sys
from pathlib import Path

from pydantic import TypeAdapter

from study.store import Stores
from study.values import (
    AttachRequest,
    Existing,
    New,
    Request,
    StudyFailure,
    WorkspaceRequest,
)


def main(*, release: str) -> None:
    stores = Stores(release)
    requests = TypeAdapter(Request)
    try:
        for line in sys.stdin:
            request = requests.validate_json(line)
            workspace = str(Path(request.workspace).resolve(strict=True))
            try:
                match request:
                    case WorkspaceRequest(action="study-open"):
                        result = stores.open(workspace)
                    case AttachRequest(choice=Existing(store=identity)):
                        result = stores.attach(workspace, identity)
                    case AttachRequest(choice=New()):
                        result = stores.create(workspace).opened()
                    case _:
                        raise NotImplementedError(
                            f"Study action is not implemented: {request.action}"
                        )
            except StudyFailure as error:
                print(
                    '{"ok":false,"error":' + error.error.model_dump_json() + "}",
                    flush=True,
                )
            else:
                print(
                    '{"ok":true,"result":' + result.model_dump_json() + "}", flush=True
                )
    finally:
        stores.close()
