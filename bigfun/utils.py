import sys
import math

import google.api_core.exceptions
import google.auth.exceptions
import google.cloud.bigquery
import click


def print_color(msg):
    click.echo(click.style(msg, fg='cyan'))


def print_success(msg):
    click.echo(click.style(f'SUCCESS: {msg}', fg='green'))


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

    @property
    def client(self):
        if self._client is None:
            try:
                self._client = google.cloud.bigquery.Client()
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error('Google Cloud not Authenticated. Authenticate with `gcloud auth application-default login` and retry')
        return self._client

    def query(self, *args, **kwargs):
        try:
            return self.client.query(*args, **kwargs).result()
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

bigquery = BigQuery()