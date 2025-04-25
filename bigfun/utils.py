import math
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request

import click
import google.api_core.exceptions
import google.auth.exceptions
import google.cloud.bigquery
import google.cloud.bigquery_connection_v1
import google.cloud.storage
import google.iam.v1.policy_pb2


def print_color(msg):
    click.echo(click.style(msg, fg="cyan"))


def print_success(msg):
    click.echo(click.style(f"SUCCESS: {msg}", fg="green"))


def print_info(msg):
    click.echo(click.style(f"INFO: {msg}", fg="yellow"))


def print_command(msg):
    click.echo(click.style(f"INFO: `{msg}`", fg="magenta"))


def print_warning(msg):
    click.echo(click.style(f"WARNING: {msg}", fg="cyan"))


def handle_error(msg, details=""):
    click.echo(click.style(f"ERROR: {msg}", fg="red"))
    if details:
        click.echo(click.style(f"ERROR_DETAILS: {details}", fg="red"))
    sys.exit()


def merge_dict(a: dict, b: dict, path=[]):
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dict(a[key], b[key], path + [str(key)])
            elif type(a[key]) != type(b[key]):
                raise Exception('Conflict at ' + '.'.join(path + [str(key)]) + ': key is in both dicts but type is different')
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]
    return a


def exec(command):
    print_command(command)
    try:
        return subprocess.check_output(command, shell=True).decode().strip()
    except subprocess.CalledProcessError as e:
        handle_error("See error above. " + e.output.decode(errors="ignore").strip())


def prefix_lines_with_line_number(string: str, starting_index: int = 1) -> str:
    """Example:

    >>> print(prefix_lines_with_line_number('Hello\\nWorld!'))
    1: Hello
    2: World!
    """
    lines = string.split("\n")
    max_index = starting_index + len(lines) - 1
    nb_zeroes = int(math.log10(max_index)) + 1
    numbered_lines = [
        str(index + starting_index).zfill(nb_zeroes) + ": " + line
        for index, line in enumerate(lines)
    ]
    return "\n".join(numbered_lines)


def dataset_access_entry2user(access_entry):
    if access_entry.entity_id == 'allAuthenticatedUsers':
        return 'allAuthenticatedUsers'
    if access_entry.entity_id == 'allUsers':
        return 'allAuthenticatedUsers'
    entity_type = 'user'
    if access_entry.entity_id.endswith('gserviceaccount.com'):
        entity_type = 'serviceAccount'
    elif access_entry.entity_type == 'groupByEmail':
        entity_type = 'group'
    return f'{entity_type}:{access_entry.entity_id}'


class BigQuery:
    def __init__(self, project):
        self.project = project
        self._client = None
        self._bq_connection_client = None

    @property
    def client(self):
        if self._client is None:
            try:
                self._client = google.cloud.bigquery.Client(self.project)
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error(
                    "Google Cloud Application-Default-Credentials are not set. Authenticate with `gcloud auth application-default login` and retry"
                )
        return self._client

    @property
    def bq_connection_client(self):
        if self._bq_connection_client is None:
            try:
                self._bq_connection_client = (
                    google.cloud.bigquery_connection_v1.ConnectionServiceClient()
                )
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error(
                    "Google Cloud Application-Default-Credentials are not set. Authenticate with `gcloud auth application-default login` and retry"
                )
        return self._bq_connection_client

    def get_dataset(self, dataset):
        print_info("Getting dataset")
        try:
            dataset = self.client.get_dataset(dataset.replace("`", ""))
        except google.api_core.exceptions.NotFound as e:
            handle_error("Dataset Not Found", e.message)
        dataset.users = [
            dataset_access_entry2user(access_entry)
            for access_entry in dataset.access_entries
            if access_entry.entity_id not in ['projectOwners', 'projectWriters', 'projectReaders']
        ]
        return dataset

    def query(self, query, **kwargs):
        try:
            return self.client.query(query, **kwargs).result()
        except google.api_core.exceptions.Forbidden as e:
            handle_error("Access Denied", e.message)
        except (
            google.api_core.exceptions.BadRequest,
            google.api_core.exceptions.NotFound,
        ) as e:
            handle_error(e.message, "Query:\n" + prefix_lines_with_line_number(query))

    def create_or_replace_destination_table(self, table, conf):
        return self.query(
            f'''
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
        '''
        )

    def load_table_from_file(self, *args, **kwargs):
        return self.client.load_table_from_file(*args, **kwargs)

    def get_remote_connection(self, project, location, name):
        print_info("Getting remote connection")
        parent = self.bq_connection_client.common_location_path(project, location)
        try:
            connections = self.bq_connection_client.list_connections(parent=parent)
        except google.api_core.exceptions.PermissionDenied as e:
            handle_error("Permission Denied", e.message)
        return next(
            (conn for conn in connections if conn.name.split("/")[-1] == name), None
        )

    def create_remote_connection(self, project, location, name):
        print_info("Creating remote connection")
        parent = self.bq_connection_client.common_location_path(project, location)
        return self.bq_connection_client.create_connection(
            parent=parent,
            connection_id=name,
            connection=google.cloud.bigquery_connection_v1.types.Connection(
                name=name,
                cloud_resource=google.cloud.bigquery_connection_v1.types.CloudResourceProperties(),
            ),
        )

    def get_or_create_remote_connection(self, project, location, name):
        connection = self.get_remote_connection(project, location, name)
        if connection:
            return connection
        self.create_remote_connection(project, location, name)
        return self.get_remote_connection(project, location, name)

    def set_remote_connection_users(self, remote_connection, members):
        print_info("Set remote connection users to: " + ", ".join(members))
        policy = self.bq_connection_client.get_iam_policy(resource=remote_connection)
        connection_user_binding = next(
            (
                binding
                for binding in policy.bindings
                if binding.role == "roles/bigquery.connectionUser"
            ),
            None,
        )
        if connection_user_binding:
            connection_user_binding.members[:] = members
        else:
            binding = google.iam.v1.policy_pb2.Binding(
                role="roles/bigquery.connectionUser", members=members
            )
            policy.bindings.append(binding)
        self.bq_connection_client.set_iam_policy(
            request=dict(resource=remote_connection, policy=policy)
        )


class Storage:
    def __init__(self, project):
        self.project = project
        self._client = None

    @property
    def client(self):
        if self._client is None:
            try:
                self._client = google.cloud.storage.Client(self.project)
            except google.auth.exceptions.DefaultCredentialsError as e:
                handle_error(
                    "Google Cloud Application-Default-Credentials are not set. Authenticate with `gcloud auth application-default login` and retry"
                )
        return self._client

    def upload(self, source_filename, destination_filename):
        print_info(f"Uploading file {source_filename} to {destination_filename}")
        if not os.path.isfile(source_filename):
            handle_error(f"{source_filename} file does not exist")
        destination_filename = destination_filename.replace("gs://", "")
        bucket_name, destination_filename = destination_filename.split("/", 1)
        bucket = self.client.bucket(bucket_name)
        blob = bucket.blob(destination_filename)
        blob.upload_from_filename(source_filename)


class CloudRun:
    def __init__(self, service, project, region):
        self.service = service
        self.project = project
        self.region = region

    def exec(self, command, options=None):
        if shutil.which('gcloud') is None:
            handle_error('`gcloud` is not installed while needed to deploy a Remote Function.')
        gcloud = "gcloud"
        if "gcloud-version" in options:
            gcloud = "gcloud " + options['gcloud-version']
            del options['gcloud-version']
        command = gcloud + " run " + command + " " + self.service
        options = options or {}
        if 'regions' not in options:
            options["region"] = self.region
        options["project"] = self.project
        options_str = "".join([f" --{name} {value}" for name, value in options.items()])
        command += options_str
        return exec(command)

    def deploy(self, source_folder, options):
        if self.service in os.environ:
            # This service has already been deployed
            return

        print_info(f"Deploy Cloud Run service `{self.service}`")
        options = {
            **{
                "max-instances": 20,
                "memory": "512Mi",
                "cpu": 1,
                "concurrency": 8,
                "platform": "managed",
                "quiet": "",
                "no-allow-unauthenticated": "",
                "ingress": "all",
            },
            **{k.replace("_", "-"): v for k, v in options.items()},
        }

        if 'regions' in options:
            # Multi-region deploy needs to build first the image
            image = f'{self.region}-docker.pkg.dev/{self.project}/cloud-run-source-deploy/{self.service}:latest'
            exec(f'gcloud builds submit --tag {image} --region {self.region}  --project {self.project} {source_folder}/')
            options['image'] = image
        else:
            options["source"] = source_folder

        self.exec("deploy", options=options)
        os.environ[self.service] = 'deployed'

    @property
    def url(self):
        print_info(f"Get Cloud Run url of service `{self.service}`")
        return self.exec(
            "services describe",
            options={
                "platform": "managed",
                "format": '"value(status.url)"',
            },
        )

    def add_invoker_permission(self, member):
        print_info(f"Give invoker permission to {member} for service `{self.service}`")
        return self.exec(
            "services add-iam-policy-binding",
            options={
                "member": member,
                "role": "roles/run.invoker",
            },
        )


def build_npm_package(npm_package, output_filename, destination_folder="."):
    if shutil.which("npm") is None:
        handle_error(
            f"`npm` is not installed while needed to build {npm_package} npm package."
        )

    if not "@" in npm_package:
        handle_error(
            f"expecting npm package with a version formatted as `package_name@x.x.x` but got: {npm_package}"
        )

    name, version = npm_package.split("@")
    package_path = f"./node_modules/{name}"
    if "/" in name:
        name, _ = name.split("/", 1)
    js_entrypoint_variable = name.replace("-", "_")

    print_info(
        f"Installing {name}@{version} npm package and webpack in tmp folder {destination_folder}"
    )
    command = (
        f"cd {destination_folder} && npm install webpack webpack-cli {name}@{version}"
    )
    exec(command)

    print_info(f"Building {npm_package} into a single file using webpack")
    command = f"cd {destination_folder} && npx webpack --mode production --entry {package_path} --output-path . --output-filename {output_filename} --output-library {js_entrypoint_variable} --output-library-type var"
    exec(command)


def build_and_upload_npm_package(npm_package, bucket, project):
    with tempfile.TemporaryDirectory() as folder:
        folder = folder.replace("\\", "/")
        output_filename = f'{npm_package.replace("/", ".")}.min.js'
        storage_filename = f"gs://{bucket}/{output_filename}"
        if storage_filename in os.environ:
            # This npm package has already been built and uploaded, let's use it
            return storage_filename
        print_info(f"Starting to build and upload npm package {npm_package}")
        build_npm_package(npm_package, output_filename, folder)
        Storage(project).upload(f"{folder}/{output_filename}", storage_filename)
        os.environ[storage_filename] = "uploaded"
        return storage_filename


def download(url, destination_filename):
    try:
        urllib.request.urlretrieve(url, destination_filename)
    except Exception as e:
        handle_error(f'Could not download file at url `{url}`. Reason: {e}')


def generate_content(prompt):
    import google.auth
    import google.genai
    _, project = google.auth.default()
    genai = google.genai.Client(vertexai=True, project=project, location='europe-west1')
    response = genai.models.generate_content(model='gemini-2.0-flash-001', contents=prompt)
    return response.text
