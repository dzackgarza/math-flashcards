"""Shared local rendering assets for editing, export, and Study."""

from __future__ import annotations

import hashlib
import json
from functools import cache
from pathlib import Path
from typing import Annotated

from pydantic import BaseModel, Field, ValidationError, model_validator


type MacroDefinition = str | tuple[str, int] | tuple[str, int, str]


type Digest = Annotated[str, Field(pattern=r"^[a-f0-9]{64}$")]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def asset_identity(
    macros: dict[str, MacroDefinition], stmaryrd: str, renderer: str
) -> str:
    return digest(
        json.dumps(
            [macros, stmaryrd, renderer], sort_keys=True, separators=(",", ":")
        ).encode()
    )


class AssetSet(BaseModel):
    identity: Digest
    macros: dict[str, MacroDefinition]
    stmaryrd: str = Field(min_length=1)
    renderer: str = Field(min_length=1)

    @model_validator(mode="after")
    def verify_identity(self) -> AssetSet:
        if self.identity != asset_identity(self.macros, self.stmaryrd, self.renderer):
            raise ValueError(
                "The installed renderer assets are damaged. Run just desktop-install."
            )
        return self


class InvalidAssetsError(ValueError):
    """The requested installed renderer set cannot be used."""


@cache
def asset_set(identity: Digest) -> AssetSet:
    path = Path(__file__).with_name("asset-sets") / (identity + ".json")
    try:
        result = AssetSet.model_validate_json(path.read_bytes())
    except (OSError, ValidationError) as error:
        raise InvalidAssetsError(
            "The requested renderer assets are unavailable. Run just desktop-install."
        ) from error
    if result.identity != identity:
        raise InvalidAssetsError(
            "The renderer asset identity is damaged. Run just desktop-install."
        )
    return result
