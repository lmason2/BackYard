import os
import json
from typing import Any

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # -- firebase --

    # provide one or the other with (value takes precedence over path)
    # value is more useful for deployments while path is easier for local development
    firebase_service_account_value: dict = os.getenv("FIREBASE_SERVICE_ACCOUNT_VALUE", {})
    firebase_service_account_path: str = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "")

    # tables

    # segment

    # -- api config --

    origin_urls: str = os.getenv(
        "ORIGIN_URLS",
        "http://localhost:9000,http://localhost:3000",
    )

    # -- testing --

    test_uid: str = ""
    test_auth_success: bool = False
    test_mode: bool = False
    test_session: Any = None

    # -- redis cache --

    """redis_enabled: bool = os.getenv("REDIS_ENABLED", True)
    redis_host: str = os.getenv("REDIS_HOST")
    redis_port: str = os.getenv("REDIS_PORT")
    redis_expiration: str = os.getenv("REDIS_EXPIRATION")"""

    # -- sqlalchemy --

    pool_size: int = os.getenv("POOL_SIZE", 1)
    pool_recycle: int = os.getenv("POOL_RECYCLE", 30)
    max_overflow: int = os.getenv("MAX_OVERFLOW", 10)

    version_filepath: str = "./Makefile"

    user_name: str = os.getenv("USER_NAME", "dcarr")
    password: str = os.getenv("PASSWORD", "")
    host: str = os.getenv("HOST", "localhost")
    port: str = os.getenv("PORT", "5433")
    db: str = os.getenv("DB", "backyard")


settings = Settings()
