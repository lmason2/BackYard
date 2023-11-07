from __future__ import annotations

from enum import Enum
from typing import Dict, List, Optional

from fastapi import Query
from fastapi_pagination.bases import AbstractParams, RawParams
from fastapi_pagination.default import Params as BaseParams
from pydantic import BaseModel


class SortOrder(str, Enum):
    ascending = "ascending"
    descending = "descending"


class Params(BaseParams):
    size: int = Query(50, gt=0, le=1000, description="Page size")


class DefaultPageParams(BaseModel, AbstractParams):
    page: int = Query(1, ge=1, description="Page number")
    size: int = Query(50, ge=1, le=5000, description="Page size")

    def to_raw_params(self) -> RawParams:
        return RawParams(
            limit=self.size,
            offset=self.size * (self.page - 1),
        )


class GenericMessageResponseSchema(BaseModel):
    message: str


class BasicReponseSchema(BaseModel):
    message: str


class FirebaseUser(BaseModel):
    id: str
    organization_id: Optional[str]
    fdp_edition: Optional[Dict]
    permissions: Optional[List[str]]
    impersonating_org_user: Optional[bool] = False


class BackyardUser(BaseModel):
    auth_type: AuthType
    id: str
    organization_id: Optional[str]
    fdp_edition: Optional[Dict]
    permissions: Optional[List[str]]


class AuthType(str, Enum):
    firebase = "firebase"


class AuthenticationResponse(BaseModel):
    """
    Authentication test output.
    """

    success: Optional[bool]
    uid: str = None
    email: Optional[str] = None
    auth_type: Optional[str] = None
    organization_id: Optional[str] = None


class AuthorizationResponse(BaseModel):
    """
    Authorization test output.
    """

    is_admin: bool
    has_access: bool
    show_id: str = None
    show_exists: bool = None


class SettingsOut(BaseModel):
    firebase_service_account_path: Optional[str]


class VersionOut(BaseModel):
    """
    Platform version.
    """

    version: str
