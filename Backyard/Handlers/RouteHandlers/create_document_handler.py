from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class CreateDocumentRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        document_id = self.decoded_body['document_id']
        job_id = self.decoded_body['job_id']
        base64 = self.decoded_body['base64']
        type = self.decoded_body['type']
        metadata = self.decoded_body['metadata']

        try:
            self.psql_client.insert_postgress(f'''INSERT INTO documents(document_id, job_id, base64, type, metadata) 
                   VALUES ('{document_id}', '{job_id}', '{base64}', '{type}', '{metadata}')''')
            self.results = 'success'
        except Exception as error:
            print(f'erorr creating document: {error}')

        return