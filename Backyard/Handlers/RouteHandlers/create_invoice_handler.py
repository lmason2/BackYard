from Handlers.RouteHandlers.base_route_handler import BaseRouteHandler


class CreateInvoiceRouteHandler(BaseRouteHandler):
    def process_route(self):
        self.results = []
        invoice_id = self.decoded_body['invoice_id']
        job_id = self.decoded_body['job_id']
        created_date = self.decoded_body['created_date']
        due_date = self.decoded_body['due_date']
        amount_outstanding = self.decoded_body['amount_outstanding']
        amount_paid = self.decoded_body['amount_paid']

        print(f'inserting invoice with job_id: {job_id}')

        try:
            self.psql_client.insert_postgress(f'''INSERT INTO invoices(invoice_id, job_id, created_date, due_date, amount_outstanding, amount_paid) 
                   VALUES ('{invoice_id}', '{job_id}', '{created_date}', '{due_date}', '{amount_outstanding}', '{amount_paid}')''')
            self.results = 'success'
        except Exception as error:
            print(f'erorr creating invoice: {error}')

        return