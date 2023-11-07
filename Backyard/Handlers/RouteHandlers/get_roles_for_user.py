from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler
import base64


class GetRolesForUser(BaseRouteHandler):
    def process_route(self):
        self.results = []
        user_id = self.decoded_body['user_id']

        try:
            psql_results = self.psql_client.execute_postgres(f'SELECT * from roles where user_id=\'{user_id}\';')
            self.results = psql_results
        except Exception as error:
            print(f'erorr retrieving all jobs: {error}')

        return
    