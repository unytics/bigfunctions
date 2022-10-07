import sys
import math

import google.api_core.exceptions
import google.auth.exceptions
import google.cloud.bigquery
import google.cloud.bigquery_connection_v1
import click


def print_color(msg):
    click.echo(click.style(msg, fg='cyan'))


def print_success(msg):
    click.echo(click.style(f'SUCCESS: {msg}', fg='green'))

def print_info(msg):
    click.echo(click.style(f'INFO: {msg}', fg='yellow'))

def handle_error(msg):
    click.echo(click.style(f'ERROR: {msg}', fg='red'))
    sys.exit()


def prefix_lines_with_line_number(string: str, starting_index: int = 1) -> str:
    """Example:

    >>> print(prefix_lines_with_line_number('Hello\\nWorld!'))
    1: Hello
    2: World!
    """
    lines = string.split("\n")
    max_index = starting_index + len(lines) - 1
    nb_zeroes = int(math.log10(max_index)) + 1
    numbered_lines = [str(index + starting_index).zfill(nb_zeroes) + ": " + line for index, line in enumerate(lines)]
    return "\n".join(numbered_lines)


class BigQuery:

    def __init__(self):
        self._client = None
        self._bq_connection_client = None

    @property
    def client(self):
        if self._client is None:
            try:
                self._client = google.cloud.bigquery.Client()
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error('Google Cloud not Authenticated. Authenticate with `gcloud auth application-default login` and retry')
        return self._client

    @property
    def bq_connection_client(self):
        if self._bq_connection_client is None:
            try:
                self._bq_connection_client = google.cloud.bigquery_connection_v1.ConnectionServiceClient()
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error('Google Cloud not Authenticated. Authenticate with `gcloud auth application-default login` and retry')
        return self._bq_connection_client

    def get_dataset(self, *args, **kwargs):
        return self.client.get_dataset(*args, **kwargs)

    def query(self, query):
        try:
            return self.client.query(query).result()
        except google.api_core.exceptions.BadRequest as e:
            e.message += "\nQuery:\n" + prefix_lines_with_line_number(query)
            raise e

    def create_or_replace_destination_table(self, table, conf):
        return self.query(f'''
            create or replace table `{table}`
            (
                {','.join([col['name'] + ' ' + col['type'] + ' options(description="' + col['description'] + '")' for col in conf['schema']])}
            )
            options(
                description="""{conf['description']}"""
            )
        ''')

    def load_table_from_file(self, *args, **kwargs):
        return self.client.load_table_from_file(*args, **kwargs)

    def get_bigfunctions_remote_connection(self, project, location):
        parent = self.bq_connection_client.common_location_path(project, location)
        connections = self.bq_connection_client.list_connections(parent=parent)
        bigfunctions_connections = [conn for conn in connections if conn.name.endswith('remote-bigfunctions')]
        if not bigfunctions_connections:
            return None
        assert len(bigfunctions_connections) == 1, 'more than one remote connection found'
        return bigfunctions_connections[0]

    def create_bigfunctions_remote_connection(self, project, location):
        parent = self.bq_connection_client.common_location_path(project, location)
        return self.bq_connection_client.create_connection(
            parent=parent,
            connection_id='remote-bigfunctions',
            connection=google.cloud.bigquery_connection_v1.types.Connection(
                name='remote-bigfunctions',
                cloud_resource=google.cloud.bigquery_connection_v1.types.CloudResourceProperties()
            )
        )

    def get_or_create_bigfunctions_remote_connection(self, project, location):
        connection = self.get_bigfunctions_remote_connection(project, location)
        if connection is not None:
            return connection
        self.create_bigfunctions_remote_connection(project, location)
        return self.get_bigfunctions_remote_connection(project, location)

    def share_bigfunctions_remote_connection(self, remote_connection):
        iam = self.bq_connection_client.get_iam_policy(resource=remote_connection)
        self.bq_connection_client.set_iam_policy(resource=remote_connection, policy=iam)
        print(iam)
        breakpoint()




bigquery = BigQuery()



