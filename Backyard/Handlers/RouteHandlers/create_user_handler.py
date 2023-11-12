from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class CreateUserRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        user_id = self.decoded_body['user_id']
        name = self.decoded_body['name']
        email = self.decoded_body['email']

        record = f"(\'{user_id}\', \'{name}\', \'{email}\')"

        try:
            self.psql_client.insert_postgress(f'''INSERT INTO users(user_id, name, email) 
                   VALUES ('{user_id}', '{name}', '{email}')''')
            self.results = 'success'
        except Exception as error:
            print(f'erorr retrieving all jobs: {error}')

        return