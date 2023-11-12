
import uuid
import psycopg2

class PostgresClient:

    def __init__(self, p_db_name, p_user, p_pass) -> None:
        self.client = psycopg2.connect("dbname=" + p_db_name + " user=" + p_user + " password=" + p_pass)

    def insert_postgress(self, query):
        try:
            print('executing')
            print(query)
            # create a cursor
            cur = self.client.cursor()
            
            # execute a statement
            cur.execute(query)
            self.client.commit()
            return
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'error'

    def execute_postgres(self, query):
        try:
            print('executing')
            print(query)
            # create a cursor
            cur = self.client.cursor()
            
            # execute a statement
            cur.execute(query)
            results = cur.fetchall()
            if results:
                return results
            return []
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return 'error'
        
    def close_connection(self):
        self.client.close()


if __name__ == '__main__':
    psql_client = PostgresClient('back_yard', 'lukemason', 'Lukrative11!')
    psql_client.insert_postgress(f'''INSERT INTO users(user_id, name, email) 
                   VALUES ('{uuid.uuid4()}', 'new user', 'new@test.com')''')
