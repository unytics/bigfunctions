import base64
import datetime
import json
import re
import time
import traceback
import uuid

import google.auth
import google.cloud.datastore
import google.cloud.datastore.query
import google.cloud.error_reporting
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from flask import Flask, g, jsonify, request

error_reporter = google.cloud.error_reporting.Client()
app = Flask(__name__)


CACHE = {}
CURRENT_LOCATION = '{{ cloud_run_location }}'

QUOTAS = {{ quotas if quotas is defined else {} }}


_, PROJECT = google.auth.default()

PRIVATE_KEY_SECRET_NAME = 'bigfunctions_private_key'


def get_current_service_account():
    if 'current_service_account' not in CACHE:
        import urllib.request
        url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email'
        req = urllib.request.Request(url)
        req.add_header('Metadata-Flavor', 'Google')
        with urllib.request.urlopen(req) as f:
            CACHE['current_service_account'] = f.read().decode('utf-8')
    return CACHE['current_service_account']


def create_temp_dataset(default_table_expiration_days=0.042):
    bigquery = google.cloud.bigquery.Client(location=g.bigfunction_dataset_location)
    random_id = str(uuid.uuid4()).replace('-', '_')
    dataset_id = f'{PROJECT}.temp_{random_id}'
    is_user_service_account = 'iam.gserviceaccount.com' in g.user
    member = 'serviceAccount:' + g.user if is_user_service_account else 'user:' + g.user
    query = f'''

    create schema `{dataset_id}`
    options(
        default_table_expiration_days={default_table_expiration_days},
        description="Temporary Dataset created by `{{ name }}` bigfunction to store temporary data"
    );

    grant `projects/bigfunctions/roles/bigquery_table_reader_and_deleter`
    on schema `{dataset_id}`
    to '{member}';

    '''
    bigquery.query(query).result()
    return dataset_id


class QuotaException(Exception):
    pass



def init_global_context(data):
    g.created_time = time.time()
    g.row_count = len(data['calls'])
    g.request_id = data['requestId']
    g.caller = data['caller']
    g.user = data['sessionUser']
    user_project_matches = re.findall(r'bigquery.googleapis.com/projects/([^/]*)/', data['caller'])
    g.user_project = user_project_matches[0] if user_project_matches else None
    g.bigfunction_dataset_location = data.get('userDefinedContext', {}).get('dataset_location')



def log(status, status_info='', **kwargs):
    duration = 1000 * (time.time() - g.created_time)
    message = {
        **{
            'status': status,
            "severity": 'INFO',
            'message': f"{status.upper()}: {{ name }} from {g.user} with {g.row_count} rows (elasped {duration} ms)",
            "bigfunction": '{{ name }}',
            "user": g.user,
            "row_count": g.row_count,
            "request_id": g.request_id,
            "caller": g.caller,
            'elapsed_ms': duration,
            'status_info': status_info,
        },
        **kwargs,
    }
    print(json.dumps(message))


def report_exception(exception):
    error_message = (str(exception) + ' --- ' + traceback.format_exc())[:1000]
    log('error', error_message)
    error_reporter.report_exception(google.cloud.error_reporting.build_flask_context(request))



class Store:

    _datastore = None

    def __init__(self, kind):
        self.kind = kind

    def get(self, key):
        key = self.datastore.key(self.kind, key)
        entity = self.datastore.get(key)
        if entity:
            return entity.get('value')

    def set(self, key, value):
        if key is None:
            key = self.datastore.key(self.kind)
        else:
            key = self.datastore.key(self.kind, key)
        entity = google.cloud.datastore.Entity(key)
        if not isinstance(value, dict):
            value = {'value': value}
        entity.update(value)
        self.datastore.put(entity)

    def compute_aggregate(self, aggregate_function, aggregate_attribute=None, filter=None):
        aggregate_attributes = aggregate_attribute or []
        filter = filter or []
        query = self.datastore.query(kind=self.kind)
        if filter:
            query.add_filter(filter=google.cloud.datastore.query.PropertyFilter(*filter))
        result = getattr(self.datastore.aggregation_query(query), aggregate_function)(aggregate_attribute).fetch()
        result = list(list(result)[0])[0].value
        print(f'{aggregate_function}({aggregate_attributes}) where {"".join(filter)}:', result)
        return result

    @property
    def datastore(self):
        if self._datastore is None:
            self._datastore = google.cloud.datastore.Client()
        return self._datastore


class Cache:

    def __init__(self, name='cache'):
        self.cache = {}
        self.store = Store(name)

    def get(self, key):
        value = self.cache.get(key)
        if value is not None:
            return value
        value = self.store.get(key)
        if value is not None:
            self.cache[key] = value
            return value

    def set(self, key, value):
        self.cache[key] = value
        self.store.set(key, value)


cache = Cache()


def check_max_rows_per_query_quota():
    max_rows_per_query = min(QUOTAS.get('max_rows_per_query'), QUOTAS.get('max_rows_per_user_per_day'))
    if max_rows_per_query and (g.row_count > max_rows_per_query):
        raise QuotaException(f"It only accepts {max_rows_per_query} rows per query and you called it now on {g.row_count} rows or more.")


def check_max_rows_per_user_per_day_quota():
    if QUOTAS.get('backend') == 'datastore':
        if 'max_rows_per_user_per_day' in QUOTAS:
            store = Store('bigfunction_call')
            today = datetime.datetime.now(datetime.UTC).strftime('%Y-%m-%d')
            user_bigfunction_date = f'{g.user}/{{ name }}/{today}'
            today_row_count_for_this_bigfunction = store.compute_aggregate(
                'sum',
                aggregate_attribute='row_count',
                filter=["user_bigfunction_date", "=", user_bigfunction_date]
            )
            if today_row_count_for_this_bigfunction + g.row_count > QUOTAS['max_rows_per_user_per_day']:
                raise QuotaException(f"It only accepts {QUOTAS['max_rows_per_user_per_day']} rows per day per user and you called it today for {today_row_count_for_this_bigfunction + g.row_count} rows.")
            store.set(None, {
                'timestamp': datetime.datetime.now(datetime.UTC),
                'user_bigfunction_date': user_bigfunction_date,
                "row_count": g.row_count,
            })


def check_quotas():
    check_max_rows_per_query_quota()
    check_max_rows_per_user_per_day_quota()


class SecretManager:

    secret_manager = None
    secrets = {}

    def get(self, name):
        if name in self.secrets:
            return self.secrets[name]
        if self.secret_manager is None:
            import google.cloud.secretmanager
            self.secret_manager = google.cloud.secretmanager.SecretManagerServiceClient()
        self.secrets[name] = self.secret_manager.access_secret_version(
            name=f'projects/{PROJECT}/secrets/{name}/versions/latest'
        ).payload.data.decode('UTF-8')
        return self.secrets[name]


secrets = SecretManager()
{% if secrets is defined %}
{% for secret in secrets %}
{{ secret.name }} = secrets.get('{{ secret.name }}')
{% endfor %}
{% endif %}



def decrypt(text):
    ciphertext = base64.b64decode(text)
    private_key = secrets.get(PRIVATE_KEY_SECRET_NAME)
    private_key = serialization.load_pem_private_key(
        private_key.encode(),
        password=None,
    )
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()


def decrypt_secrets(value):
    if isinstance(value, dict):
        return {k: decrypt_secrets(v) for k, v in value.items()}

    if not isinstance(value, str):
        return value

    encrypted_secrets = re.findall(r'ENCRYPTED_SECRET\(([^\)]*)\)', value)
    for encrypted_secret in encrypted_secrets:
        decrypted_secret = decrypt(encrypted_secret)
        decrypted_secret = json.loads(decrypted_secret)
        log('decrypted_json_secret', decrypted_secret['secret'])
        assert g.user in decrypted_secret['authorized_users'], f'Permission Error: User `{g.user}` do not belong to secret `authorized readers`'
        assert decrypted_secret['function'] == '{{ name }}', f'Permission Error: Secret was not created to be used with this function'
        decrypted_secret = decrypted_secret['secret']
        value = value.replace(f'ENCRYPTED_SECRET({encrypted_secret})', decrypted_secret)
    return value







{{ init_code }}

{% if code_process_rows_as_batch %}

def compute_all_rows(rows):
    {{ code | replace('\n', '\n    ') | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) }}

{% else %}

def compute_one_row(args):
    {% if arguments %}{% for argument in arguments %}{{ argument.name }}, {% endfor %} = args{% endif %}
    {% for argument in arguments if argument.contains_secret -%}
    {{ argument.name }} = decrypt_secrets({{ argument.name }})
    {% endfor %}

    {{ code | replace('\n', '\n    ') | replace('{BIGFUNCTIONS_DATASET}',  '`' +  project + '`.`' + dataset + '`' ) }}

{% endif %}


@app.route("/", methods=['POST'])
def handle():
    try:
        data = request.get_json()
        init_global_context(data)
        log('started')
        check_quotas()
        rows = data['calls']
        {% if code_process_rows_as_batch %}
        replies = compute_all_rows(rows)
        {% else %}
        replies = [compute_one_row(row) for row in rows]
        {% endif %}
        response = jsonify( { "replies" :  replies} )
        log('success')
        return response
    except QuotaException as e:
        error_message = e.args[0]
        log('quota_error', error_message)
        return jsonify({
            'errorMessage': f'''
                Thanks for using BigFunctions!
                The use of this function `{{ name }}` is limited by quotas.
                {error_message}.
                To remove this limit, you can ask for quotas increase to `{QUOTAS['contact']}` or deploy the function in your own project.
                Details are here: https://github.com/unytics/bigfunctions
                If you need help, please reach out to the slack: https://join.slack.com/t/bigfunctions/shared_invite/zt-1gbv491mu-cs03EJbQ1fsHdQMcFN7E1Q
            '''.replace('\n', ' ').replace('  ', ' ').replace('  ', ' '),
        }), 400
    except AssertionError as e:
        error_message = e.args[0]
        log('assertion_error', error_message)
        return jsonify({'errorMessage': error_message}), 400
    except Exception as e:
        report_exception(e)
        return jsonify({'errorMessage': f"{type(e).__name__}: {str(e)}"}), 400
