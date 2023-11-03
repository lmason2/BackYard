import base64
import json
from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class GetAllUsersRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []

        try:
            psql_results = self.psql_client.execute_postgres('SELECT * FROM users;')
            self.results = psql_results
        except Exception as error:
            print(f'erorr retrieving all jobs: {error}')

        return