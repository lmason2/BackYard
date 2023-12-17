from .base_route_handler import BaseRouteHandler


class GetDocumentsByJobIdRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        job_id = self.decoded_body["job_id"]
        print(f"getting documents with job id: {job_id}")

        try:
            psql_results = self.psql_client.execute_postgres(f"SELECT * FROM documents WHERE job_id='{job_id}';")
            self.results = psql_results
        except Exception as error:
            print(f"erorr retrieving all jobs: {error}")

        return
