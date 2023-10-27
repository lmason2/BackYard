from fastapi import Depends, FastAPI
from typing_extensions import Annotated
from fastapi.requests import Request
from Factories.route_factory import RouteFactory
from pydantic import BaseModel, Base64Bytes

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


if __name__ == '__main__':
    from Interfaces.cassandra_connection import CDB
    cdb = CDB()
    rows = cdb.execute_generic_command("SELECT * FROM backyard_dev.jobs;")
    for row in rows:
        print(row)