from fastapi import Depends, FastAPI, Security
from typing_extensions import Annotated
from fastapi.requests import Request
from Backyard.Auth.authn import get_user
from Backyard.Auth.authz import setup_firebase
from Backyard.global_models import BackyardUser
from Backyard.Factories.route_factory import RouteFactory
from pydantic import BaseModel, Base64Bytes
from Backyard.Interfaces.postgres_connection import PostgresClient
from Backyard.Interfaces.postgres_orm import PostgresORM
from Backyard.conf import settings

app = FastAPI()
setup_firebase()


@app.get("/")
async def root():
    return {"message": "hello world"}


class RequestModel(BaseModel):
    base64_bytes: Base64Bytes


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data


ParsingDependency = Annotated[str, Depends(parse_body)]


@app.post("/api/backyard/v1/{route_endpoint}")
async def handle_route(
    route_endpoint,
    request_body: ParsingDependency,
    user: BackyardUser = Security(get_user),
):
    route_handler = RouteFactory.get_handler(route_endpoint, request_body)
    return route_handler.results


@app.on_event("startup")
async def startup():
    app.state.psql_client = PostgresClient(settings.db, settings.user_name, settings.password, settings.port)
    app.state.psql_orm = PostgresORM()


if __name__ == "__main__":
    from Interfaces.postgres_connection import PostgresClient

    psql_client = PostgresClient("db_name", "username", "password")
    rows = psql_client.execute_postgres("SELECT * FROM table;")
    for row in rows:
        print(row)
