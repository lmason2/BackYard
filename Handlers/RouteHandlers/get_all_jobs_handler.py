from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class GetAllJobsRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        print('getting jobs')

        try:
            psql_results = self.psql_client.execute_postgres('SELECT * FROM jobs;')
            self.results = psql_results
        except Exception as error:
            print(f'erorr retrieving all jobs: {error}')

        return
    