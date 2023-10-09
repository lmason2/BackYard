from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider


def print_header(header: str):
    """
    Helper function to print debug header
    """
    print('############################')
    print(f'##\t{header}\t##')
    print('############################')
    print()

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
        self.session.execute(command)


    ## Public Functions
    ## ------------------------------
    def create_keyspace(self, keyspace_name: str):
        """
        Passed a keyspace_name, create the keyspace if it doesn't already exist
        """
        print(f'Creating keyspace: {keyspace_name}')
        replication_strategy = '{ \'class\' : \'SimpleStrategy\', \'replication_factor\' : 3 }'
        command = f'CREATE  KEYSPACE [IF NOT EXISTS] {keyspace_name} WITH REPLICATION = {replication_strategy};'
        self._execute_command(command)

    def use_keyspace(self, keyspace_name: str):
        """
        Passed a keyspace_name, use the keyspace
        """
        print(f'Using keyspace: {keyspace_name}')
        command = f'USE {keyspace_name};'
        self.keyspace = keyspace_name
        self._execute_command(command)

    def create_table(self, table_name: str, columns: str):
        """
        Passed a table_name and column design, create the table
        """
        command = f'CREATE TABLE {table_name} ({columns});'
        self._execute_command(command)

    def describe_keyspaces(self):
        """
        Describe the keyspaces
        """
        command = f'DESCRIBE KEYSPACES'
        self._execute_command(command)

    def describe_tables(self):
        """
        Describe the tables in the keyspace
        """
        command = f'DESCRIBE TABLES'
        self._execute_command(command)

    def execute_generic_command(self, command: str):
        self._execute_command(command)

if __name__ == '__main__':
    print_header('Running test driver')
    db_connection = Cassandra()
    KEYSPACE_NAME = 'backyard_dev'
    TABLE_NAME_USERS = 'Users'
    USERS_TABLE_COLUMNS = '( user_id UUID PRIMARY KEY, first_name text, last_name text, email text, password text );'
    TABLE_NAME_JOBS = 'Jobs'
    JOBS_TABLE_COLUMNS = '( job_id UUID PRIMARY KEY, contractor_id text, client_id text );'

    print_header('Describing keyspaces')
    db_connection.describe_keyspaces()
    print_header(f'Creating keyspace: {KEYSPACE_NAME}')
    db_connection.create_keyspace(KEYSPACE_NAME)
    print_header('Describing keyspaces')
    db_connection.describe_keyspaces()
    print_header(f'Using keyspace: {KEYSPACE_NAME}')
    db_connection.use_keyspace(KEYSPACE_NAME)
    print_header('Describing tables')
    db_connection.describe_tables()
    print_header(f'Creating table: {TABLE_NAME_USERS}')
    print(f'Table columns: {USERS_TABLE_COLUMNS}')
    db_connection.create_table(TABLE_NAME_USERS, USERS_TABLE_COLUMNS)
    print_header(f'Created table: {TABLE_NAME_JOBS}')
    print(f'Table columns: {JOBS_TABLE_COLUMNS}')
    db_connection.create_table(TABLE_NAME_JOBS, JOBS_TABLE_COLUMNS)

