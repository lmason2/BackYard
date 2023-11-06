"""
User authorization and permissions.
"""
from typing import Any

import firebase_admin
from firebase_admin import credentials

from ..conf import settings


def setup_firebase():
    """
    Initialize Firebase application.

    It's required to provide either the Firebase service account literal value, or the
    path to a file which contains the Firebase service account key.  The literal value
    takes precedence.

    The literal value is more useful for deployments while path is easier for local
    development.
    """
    if settings.firebase_service_account_value is not None:
        creds = credentials.Certificate(settings.firebase_service_account_value)
    elif settings.firebase_service_account_path is not None:
        creds = credentials.Certificate(settings.firebase_service_account_path)
    else:
        raise Exception("You must provide either `FIREBASE_SERVICE_ACCOUNT_VALUE` or `FIREBASE_SERVICE_ACCOUNT_PATH`.")

    firebase_admin.initialize_app(credential=creds)
    firebase_admin.get_app()
