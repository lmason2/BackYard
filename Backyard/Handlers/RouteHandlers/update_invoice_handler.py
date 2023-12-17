import json
from .base_route_handler import BaseRouteHandler


def get_value_representation_of_column_value(column_key, column_value):
    if column_key == "created_date" or column_key == "due_date":
        return f"'{column_value}'"


class UpdateInvoiceRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        invoice_id = self.decoded_body["invoice_id"]
        values = json.loads(self.decoded_body["values"])

        print(f"updating event with event id: {invoice_id}")
        update_list = []

        for k, v in values.items():
            update_list.append(f"{k} = {get_value_representation_of_column_value(k, v)}")

        update_string = ", ".join(update_list)

        try:
            psql_results = self.psql_client.update_postgres(
                f"UPDATE invoices SET {update_string} WHERE invoice_id='{invoice_id}';"
            )
            self.results = psql_results
        except Exception as error:
            print(f"erorr retrieving all jobs: {error}")

        return
