import base64
import json
from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class GetJobRouteHandler(BaseRouteHandler):
    def process_route(self):
        results = []

        if 'by_job_id' in self.decoded_body:
            # process via job id
            COMMAND = f'SELECT * from backyard_dev.jobs where job_id={self.decoded_body["by_job_id"]};'
            rows = self.CDB.execute_generic_command(COMMAND)
            for row in rows:
                results.append(row)

        elif 'by_client_and_contractor_id' in self.decoded_body:
            # process via client and contractor id
            CLIENT_ID = self.decoded_body["by_client_and_contractor_id"]["client_id"]
            CONTRACTOR_ID = self.decoded_body["by_client_and_contractor_id"]["contractor_id"]
            COMMAND = f'SELECT * FROM backyard_dev.jobs where client_id={CLIENT_ID} and contractor_id={CONTRACTOR_ID} ALLOW FILTERING;'
            rows = self.CDB.execute_generic_command(COMMAND)
            for row in rows:
                results.append(row)


        self.results = results