from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class CreateEventRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        event_id = self.decoded_body['event_id']
        job_id = self.decoded_body['job_id']
        date = self.decoded_body['date']
        metadata = self.decoded_body['metadata']

        print(f'inserting event with job_id: {job_id}')

        try:
            self.psql_client.insert_postgress(f'''INSERT INTO events(event_id, job_id, date, metadata) 
                   VALUES ('{event_id}', '{job_id}', '{date}', '{metadata}')''')
            self.results = 'success'
        except Exception as error:
            print(f'erorr creating event: {error}')

        return