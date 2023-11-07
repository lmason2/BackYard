"""
Firebase Authentication integration.
"""

import json
from http import HTTPStatus

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer, SecurityScopes
from firebase_admin import auth

from ..conf import settings
from ..global_models import AuthType, FirebaseUser, BackyardUser


# -- Firebase Authentication --


def get_firebase_user(uid):
    if not uid:
        return None

    user = auth.get_user(uid)
    return user


def get_firebase_user_email(uid):
    user = get_firebase_user(uid)
    if user:
        return user.email

    return None


class FirebaseAuth(HTTPBearer):
    def __init__(self, auto_error: bool = False):
        # Setting auto_error to false will enable toggling authentication methods.

        super().__init__(auto_error=auto_error)
        self.user = None
        self.scheme_name = "Firebase"

    async def __call__(self, request: Request):
        creds: HTTPAuthorizationCredentials = await super().__call__(request)
        if settings.test_mode:
            self.uid = settings.test_uid
        else:
            if not creds:
                raise HTTPException(
                    detail={
                        "code": "unauthorized",
                        "description": "Missing token for authentication.",
                    },
                    status_code=HTTPStatus.UNAUTHORIZED,
                )
            user, success = self.authenticate(id_token=creds.credentials)
            if not success and self.auto_error:
                raise HTTPException(
                    detail={
                        "code": "unauthorized",
                        "description": "Invalid token for authentication.",
                    },
                    status_code=HTTPStatus.UNAUTHORIZED,
                )
            if user:
                firebase_user = FirebaseUser(
                    id=user.get("uid", ""),
                    organization_id=user.get("customOrgId", ""),
                    fdp_edition=json.loads(user.get("customFdpEdition", "{}")),
                    permissions=user.get("permissions", []),
                    impersonating_org_user=user.get("isImpersonatingOrgUser", False),
                )
                self.user = firebase_user
                return firebase_user

    @staticmethod
    def authenticate(id_token):
        """
        Verify ID token for a user from the client to obtain their corresponding uid.

        https://firebase.google.com/docs/auth/admin/verify-id-tokens
        """
        try:
            user = auth.verify_id_token(id_token)
        except Exception:
            user = None

        success = True if user else False
        return user, success


firebase = FirebaseAuth()


async def get_user(
    security_scopes: SecurityScopes,
    firebase_user: FirebaseUser = Depends(firebase),
):
    user = None
    if firebase_user:
        user = BackyardUser(
            auth_type=AuthType.firebase,
            id=firebase_user.id,
        )
    else:
        raise AuthError(
            error={
                "code": "unauthorized",
                "description": "Invalid or missing token for authentication.",
            },
            status_code=HTTPStatus.UNAUTHORIZED,
        )

    scopes = security_scopes.scopes

    return user


class AuthError(HTTPException):
    def __init__(self, error, status_code):
        super().__init__(status_code=status_code)
        self.detail = error
        self.status_code = status_code


def get_token_auth_header(authorization) -> str:
    """
    Obtains the access token from the Authorization Header
    """

    if not authorization:
        raise AuthError(
            {
                "code": "authorization_header_missing",
                "description": "Authorization header is expected.",
            },
            HTTPStatus.UNAUTHORIZED,
        )
    parts = authorization.split()

    if parts[0].lower() != "bearer":
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must start with Bearer.",
            },
            HTTPStatus.UNAUTHORIZED,
        )
    if len(parts) == 1:
        raise AuthError(
            {"code": "invalid_header", "description": "Token not found."},
            HTTPStatus.UNAUTHORIZED,
        )
    if len(parts) > 2:
        raise AuthError(
            {
                "code": "invalid_header",
                "description": "Authorization header must be Bearer token.",
            },
            HTTPStatus.UNAUTHORIZED,
        )

    return parts[1]
