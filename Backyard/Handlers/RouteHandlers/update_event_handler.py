import json
from .base_route_handler import BaseRouteHandler


def get_value_representation_of_column_value(column_key, column_value):
    if column_key == "date":
        return f"'{column_value}'"
    if column_key == "metadata":
        double_quoted_string = json.dumps(column_value)
        single_quoted_string = f"'{double_quoted_string[1:-1]}'"
        return single_quoted_string


class UpdateEventRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        event_id = self.decoded_body["event_id"]
        values = json.loads(self.decoded_body["values"])

        print(f"updating event with event id: {event_id}")
        update_list = []

        for k, v in values.items():
            update_list.append(f"{k} = {get_value_representation_of_column_value(k, v)}")

        update_string = ", ".join(update_list)

        try:
            psql_results = self.psql_client.update_postgres(
                f"UPDATE events SET {update_string} WHERE event_id='{event_id}';"
            )
            self.results = psql_results
        except Exception as error:
            print(f"erorr retrieving all jobs: {error}")

        return
