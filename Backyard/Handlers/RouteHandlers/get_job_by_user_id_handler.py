from .base_route_handler import BaseRouteHandler


class GetJobByUserIdRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        user_id = self.decoded_body["user_id"]
        client_id = self.decoded_body["client_id"]
        print(f"getting job with id: {user_id}")
        print(f"Client ID: {client_id}")
        column = "gc_id"
        if client_id:
            column = "client_id"

        try:
            psql_results = self.psql_client.execute_postgres(f"SELECT * FROM jobs WHERE {column}='{user_id}';")
            self.results = psql_results
        except Exception as error:
            print(f"erorr retrieving all jobs: {error}")

        return
