import sys
import subprocess
import math

import google.api_core.exceptions
import google.auth.exceptions
import google.cloud.bigquery
import google.cloud.bigquery_connection_v1
import google.iam.v1.policy_pb2
import click


def print_color(msg):
    click.echo(click.style(msg, fg='cyan'))

def print_success(msg):
    click.echo(click.style(f'SUCCESS: {msg}', fg='green'))

def print_info(msg):
    click.echo(click.style(f'INFO: {msg}', fg='yellow'))

def print_command(msg):
    click.echo(click.style(f'INFO: `{msg}`', fg='magenta'))

def print_warning(msg):
    click.echo(click.style(f'WARNING: {msg}', fg='cyan'))

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

    def get_dataset(self, dataset):
        print_info('Getting dataset')
        return self.client.get_dataset(dataset.replace('`', ''))

    def query(self, query):
        try:
            return self.client.query(query).result()
        except (google.api_core.exceptions.BadRequest, google.api_core.exceptions.NotFound) as e:
            e.message += "\nQuery:\n" + prefix_lines_with_line_number(query)
            raise e

    def create_or_replace_destination_table(self, table, conf):
        return self.query(f'''
            create or replace table `{table}`
            (
                {
                    ','.join([
                    col['name'] + ' ' + col['type'] + ' options(description="' + col['description'] + '")'
                    for col in conf['schema']
                    ])
                }
            )
            options(
                description="""{conf['description']}"""
            )
        ''')

    def load_table_from_file(self, *args, **kwargs):
        return self.client.load_table_from_file(*args, **kwargs)

    def get_remote_connection(self, project, location, name):
        print_info('Getting remote connection')
        parent = self.bq_connection_client.common_location_path(project, location)
        connections = self.bq_connection_client.list_connections(parent=parent)
        return next((conn for conn in connections if conn.name.split('/')[-1] == name), None)

    def create_remote_connection(self, project, location, name):
        print_info('Creating remote connection')
        parent = self.bq_connection_client.common_location_path(project, location)
        return self.bq_connection_client.create_connection(
            parent=parent,
            connection_id=name,
            connection=google.cloud.bigquery_connection_v1.types.Connection(
                name=name,
                cloud_resource=google.cloud.bigquery_connection_v1.types.CloudResourceProperties()
            )
        )

    def get_or_create_remote_connection(self, project, location, name):
        connection = self.get_remote_connection(project, location, name)
        if connection:
            return connection
        self.create_remote_connection(project, location, name)
        return self.get_remote_connection(project, location, name)

    def set_remote_connection_users(self, remote_connection, members):
        print_info('Set remote connection users')
        policy = self.bq_connection_client.get_iam_policy(resource=remote_connection)
        connection_user_binding = next(
            (binding for binding in policy.bindings if binding.role == 'roles/bigquery.connectionUser'),
            None
        )
        if connection_user_binding:
            connection_user_binding.members[:] = members
        else:
            binding = google.iam.v1.policy_pb2.Binding(role='roles/bigquery.connectionUser', members=members)
            policy.bindings.append(binding)
        self.bq_connection_client.set_iam_policy(request=dict(resource=remote_connection, policy=policy))


class CloudRun:

    def __init__(self, service, project, region):
        self.service = service
        self.project = project
        self.region = region

    def exec(self, command, options=None):
        command += ' ' + self.service
        options = options or {}
        options['region'] = self.region
        options['project'] = self.project

        options_str = ''.join([f' --{name} {value}' for name, value in options.items()])
        command += options_str
        print_command(command)
        return subprocess.check_output(command, shell=True).decode().strip()

    def deploy(self, source_folder):
        print_info(f'Deploy Cloud Run service `{self.service}`')
        return self.exec(
            'gcloud run deploy',
            options={
                'source': source_folder,
                'platform': 'managed',
                'quiet': '',
                'no-allow-unauthenticated': '',
            }
        )

    @property
    def url(self):
        print_info(f'Get Cloud Run url of service `{self.service}`')
        return self.exec(
            'gcloud run services describe',
            options={
                'platform': 'managed',
                'format': '"value(status.url)"',
            }
        )

    def add_invoker_permission(self, member):
        print_info(f'Give invoker permission to {member} for service `{self.service}`')
        return self.exec(
            'gcloud run services add-iam-policy-binding',
            options={
                'member': member,
                'role': 'roles/run.invoker',
            }
        )


bigquery = BigQuery()



