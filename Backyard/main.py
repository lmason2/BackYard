from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from fastapi.requests import Request
from Factories.route_factory import RouteFactory
from pydantic import BaseModel, Base64Bytes
from Interfaces.postgres_connection import PostgresClient
from Interfaces.postgres_orm import PostgresORM

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello world'}

class RequestModel(BaseModel):
    base64_bytes: Base64Bytes

async def parse_body(request: Request):
    data: bytes = await request.body()
    return data

ParsingDependency = Annotated[str, Depends(parse_body)]


@app.post('/api/backyard/v1/{route_endpoint}')
async def handle_route(route_endpoint, request_body: ParsingDependency):
    route_handler = RouteFactory.get_handler(route_endpoint, request_body)
    return route_handler.results

@app.on_event('startup')
async def startup():
    app.state.psql_client   = PostgresClient('back_yard', 'lukemason', 'Lukrative11!')
    app.state.psql_orm      = PostgresORM('lukemason', 'Lukrative11!', 'localhost', '5432', 'back_yard')

if __name__ == '__main__':
    from Interfaces.postgres_connection import PostgresClient
    psql_client = PostgresClient('db_name', 'username', 'password')
    rows = psql_client.execute_postgres("SELECT * FROM table;")
    for row in rows:
        print(row)