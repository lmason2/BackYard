from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid


def print_header(header: str):
    """
    Helper function to print debug header
    """
    print()
    print('############################')
    print(f'##\t{header}\t##')
    print('############################')

class Cassandra:
    def __init__(self) -> None:
        ap = PlainTextAuthProvider(username='cassandra', password='cassandra')
        cluster = Cluster(auth_provider=ap)
        self.session = cluster.connect()
        self.keyspace = None

    ## Private Functions
    ## ------------------------------
    def _execute_command(self, command: str):
        """
        Private function to execute passed command
        """
        print(f'Executing command: {command}')
        response = self.session.execute(command)
        return response


    ## Public Functions
    ## ------------------------------
    def create_keyspace(self, keyspace_name: str):
        """
        Passed a keyspace_name, create the keyspace if it doesn't already exist
        """
        print(f'Creating keyspace: {keyspace_name}')
        replication_strategy = '{ \'class\' : \'SimpleStrategy\', \'replication_factor\' : 3 }'
        command = f'CREATE  KEYSPACE IF NOT EXISTS {keyspace_name} WITH REPLICATION = {replication_strategy};'
        response = self._execute_command(command)
        return response

    def use_keyspace(self, keyspace_name: str):
        """
        Passed a keyspace_name, use the keyspace
        """
        print(f'Using keyspace: {keyspace_name}')
        command = f'USE {keyspace_name};'
        self.keyspace = keyspace_name
        response = self._execute_command(command)
        return response

    def create_table(self, table_name: str, columns: str):
        """
        Passed a table_name and column design, create the table
        """
        command = f'CREATE TABLE IF NOT EXISTS {table_name} {columns};'
        response = self._execute_command(command)
        return response

    def describe_keyspaces(self):
        """
        Describe the keyspaces
        """
        command = f'DESCRIBE KEYSPACES'
        response = self._execute_command(command)
        return response

    def describe_tables(self):
        """
        Describe the tables in the keyspace
        """
        command = f'DESCRIBE TABLES'
        response = self._execute_command(command)
        return response
    
    def insert_into_table(self, table_name, columns, values):
        """
        Insert values into table name
        """
        command = f'INSERT INTO {table_name} {columns} VALUES {values};'
        response = self._execute_command(command)
        return response
    
    def delete_table(self, table_name):
        """
        Delete table
        """
        command = f'DROP TABLE {table_name};'
        response = self._execute_command(command)
        return response

    def execute_generic_command(self, command: str):
        response = self._execute_command(command)
        return response

if __name__ == '__main__':
    """
    Test driver for cassandra_connection and database SEED
    """
    ## SEED DATABASE
    ## -----------------------
    seed = False

    ## Connection and constant values
    print_header('Running test driver')
    db_connection = Cassandra()
    KEYSPACE_NAME = 'backyard_dev'
    TABLE_NAME_USERS = 'Users'
    USERS_TABLE_COLUMNS = '( user_id UUID PRIMARY KEY, first_name text, last_name text, email text, password text )'
    TABLE_NAME_JOBS = 'Jobs'
    JOBS_TABLE_COLUMNS = '( job_id UUID PRIMARY KEY, contractor_id UUID, client_id UUID )'

    ## Describing keyspaces
    ##------------------------------
    print_header('Describing keyspaces')
    keyspaces = db_connection.describe_keyspaces()
    print(keyspaces)

    ## Creating keyspace
    ##------------------------------
    print_header(f'Creating keyspace: {KEYSPACE_NAME}')
    keyspace = db_connection.create_keyspace(KEYSPACE_NAME)
    print(keyspace)

    ## Describing keyspaces
    ##------------------------------
    print_header('Describing keyspaces')
    new_keyspaces = db_connection.describe_keyspaces()
    print(new_keyspaces)

    ## Using keyspace
    ##------------------------------
    print_header(f'Using keyspace: {KEYSPACE_NAME}')
    used_keyspace = db_connection.use_keyspace(KEYSPACE_NAME)
    print(used_keyspace)

    ## Describing tables
    ##------------------------------
    print_header('Describing tables')
    tables = db_connection.describe_tables()
    print(tables)

    ## Creating table
    ##------------------------------
    print_header(f'Creating table: {TABLE_NAME_USERS}')
    print(f'Table columns: {USERS_TABLE_COLUMNS}')
    users_table = db_connection.create_table(TABLE_NAME_USERS, USERS_TABLE_COLUMNS)
    print(users_table)

    ## Creating table
    ##------------------------------
    print_header(f'Created table: {TABLE_NAME_JOBS}')
    print(f'Table columns: {JOBS_TABLE_COLUMNS}')
    jobs_table = db_connection.create_table(TABLE_NAME_JOBS, JOBS_TABLE_COLUMNS)
    print(jobs_table)

    if seed:
        ## Structure users insert
        ##------------------------------
        mike_uuid = uuid.uuid4()
        insert_columns_users = '( user_id, first_name, last_name, email, password )'
        insert_values_users = f'( {mike_uuid}, \'Mike\', \'Mason\', \'michael.l.mason19@gmail.com\', \'runner09\' )'
        response = db_connection.insert_into_table(TABLE_NAME_USERS, insert_columns_users, insert_values_users)
        print(response)

        zach_uuid = uuid.uuid4()
        insert_columns_users = '( user_id, first_name, last_name, email, password )'
        insert_values_users = f'( {zach_uuid}, \'Zach\', \'Mason\', \'zta.mason@gmail.com\', \'verus\' )'
        response = db_connection.insert_into_table(TABLE_NAME_USERS, insert_columns_users, insert_values_users)
        print(response)

        ## Structure jobs insert
        ##------------------------------
        jenan_job_id = uuid.uuid4()
        insert_columns_jobs = '( job_id, contractor_id, client_id )'
        insert_values_jobs = f'( {jenan_job_id}, {mike_uuid}, {zach_uuid} )'
        response = db_connection.insert_into_table(TABLE_NAME_JOBS, insert_columns_jobs, insert_values_jobs)
        print(response)
