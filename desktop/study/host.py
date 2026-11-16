"""One request per line; one writer of each workspace's learning data."""

import sys
from contextlib import closing
from pathlib import Path

from pydantic import TypeAdapter

from diagnostics import Diagnostics
from study.session import viewed
from study.store import Stores
from study.sync import sync
from study.values import (
    AttachRequest,
    Existing,
    New,
    Request,
    StudyFailure,
    StudyError,
    SyncRequest,
    ViewedRequest,
    WorkspaceRequest,
)


def main(*, release: str) -> None:
    with closing(Diagnostics("study-host", release)) as diagnostics:
        with diagnostics.operation("startup"):
            stores = Stores(release)
            requests = TypeAdapter(Request)
        try:
            for line in sys.stdin:
                try:
                    with diagnostics.operation("request", line) as details:
                        request = requests.validate_json(line)
                        workspace = str(Path(request.workspace).resolve(strict=True))
                        details["action"] = request.action
                        details["workspace"] = workspace
                        match request:
                            case WorkspaceRequest(action="study-open"):
                                result = stores.open(workspace)
                            case AttachRequest(choice=Existing(store=identity)):
                                result = stores.attach(workspace, identity)
                            case AttachRequest(choice=New()):
                                result = stores.create(workspace).opened()
                            case ViewedRequest():
                                result = viewed(stores, request, workspace)
                            case SyncRequest():
                                store = stores.attached(workspace)
                                if store is None:
                                    raise StudyFailure(
                                        StudyError(
                                            kind="UnknownStore",
                                            message="Attach a study store before synchronizing cards.",
                                        )
                                    )
                                result = sync(store, Path(workspace), request)
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
                        '{"ok":true,"result":' + result.model_dump_json() + "}",
                        flush=True,
                    )
        finally:
            with diagnostics.operation("shutdown"):
                stores.close()
