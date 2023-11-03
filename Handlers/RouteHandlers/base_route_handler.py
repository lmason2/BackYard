import json
import base64
from Interfaces.postgres_connection import PostgresClient

class BaseRouteHandler:
    def __init__(self, request_body) -> None:
        self.request_body       = request_body
        self.decoded_body       = json.loads(base64.b64decode(self.request_body).decode())
        self.psql_client        = PostgresClient('back_yard', 'lukemason', 'Lukrative11!')
        self.results            = None
        self.process_route()

    def process_route(self):
        pass