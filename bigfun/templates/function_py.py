import time
import json
import datetime
import traceback

from flask import Flask, request, jsonify
import google.auth
import google.cloud.error_reporting


error_reporter = google.cloud.error_reporting.Client()
app = Flask(__name__)


CACHE = {}

QUOTAS = {{ quotas }}


_, PROJECT = google.auth.default()


def get_current_service_account():
    if 'current_service_account' not in CACHE:
        import urllib.request
        url = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/email'
        req = urllib.request.Request(url)
        req.add_header('Metadata-Flavor', 'Google')
        with urllib.request.urlopen(req) as f:
            CACHE['current_service_account'] = f.read().decode('utf-8')
    return CACHE['current_service_account']


class QuotaException(Exception):
    pass



class SimpleQuotaManager:

    def __init__(self, data):
        self.created_at = datetime.datetime.utcnow()
        self.created_time = time.time()
        self.user = data['sessionUser']
        self.row_count = len(data['calls'])
        self.message = {
            "bigfunction": '{{ name }}',
            "status": 'started',
            "user": self.user,
            "row_count": self.row_count,
            "request_id": data['requestId'],
            "caller": data['caller'],
        }

    def save_log(self, **kwargs):
        duration = 1000 * (time.time() - self.created_time)
        self.message = {**self.message, **kwargs}
        self.message['elapsed_ms'] = duration
        print(json.dumps({
            **self.message,
            **{
                'message': f"{self.message['status'].upper()}: {{ name }} from {self.user} with {self.row_count} rows (elasped {duration} ms)",
                'severity': 'INFO',
            }
        }))

    def check_quotas(self):
        if QUOTAS.get('max_rows_per_query') and self.row_count > QUOTAS['max_rows_per_query']:
            raise QuotaException(f"It only accepts {QUOTAS['max_rows_per_query']} rows per query and you called it now on {self.row_count} rows or more.")


class DatastoreQuotaManager:

    kind = 'bigfunction_call'

    def __init__(self, data):
        import google.cloud.datastore
        self.datastore = google.cloud.datastore.Client()
        self.created_at = datetime.datetime.utcnow()
        self.created_time = time.time()
        self.date = self.created_at.strftime("%Y-%m-%d")
        self.user = data['sessionUser']
        self.user_date = f'{self.user}/{self.date}'
        self.user_bigfunction_date = f'{self.user}/{{ name }}/{self.date}'
        self.row_count = len(data['calls'])
        self.key = self.datastore.key(self.kind)
        self.entity = google.cloud.datastore.Entity(self.key)
        self.message = {
            "timestamp": self.created_at,
            "bigfunction": '{{ name }}',
            "status": 'started',
            "user": self.user,
            "row_count": self.row_count,
            "request_id": data['requestId'],
            "caller": data['caller'],
            'date': self.date,
            'user_date': self.user_date,
            'user_bigfunction_date': self.user_bigfunction_date,
        }

    def save_log(self, **kwargs):
        duration = 1000 * (time.time() - self.created_time)
        self.message = {**self.message, **kwargs}
        self.message['elapsed_ms'] = duration
        print(json.dumps({
            **{k: v for k, v in self.message.items() if k != 'timestamp'},
            **{
                'message': f"{self.message['status'].upper()}: {{ name }} from {self.user} with {self.row_count} rows (elasped {duration} ms)",
                'severity': 'INFO',
            }
        }))
        self.entity.update(self.message)
        self.datastore.put(self.entity)

    def get_user_stats(self):
        query = self.datastore.query(kind=self.kind)
        query.add_filter("user_bigfunction_date", "=", self.user_bigfunction_date)
        today_logs_for_this_bigfunction = query.fetch()
        today_row_count_for_this_bigfunction = sum(r.get('row_count', 0) for r in today_logs_for_this_bigfunction)

        query = self.datastore.query(kind=self.kind)
        query.add_filter("user_date", "=", self.user_date)
        today_request_count = self.datastore.aggregation_query(query).count().fetch()
        today_request_count = list(list(today_request_count)[0])[0].value

        return {
            'today_row_count_for_this_bigfunction': today_row_count_for_this_bigfunction,
            'today_request_count': today_request_count,
        }

    def check_quotas(self):
        if QUOTAS.get('max_rows_per_query') and (self.row_count > QUOTAS['max_rows_per_query']):
            raise QuotaException(f"It only accepts {QUOTAS['max_rows_per_query']} rows per query and you called it now on {self.row_count} rows or more.")

        if self.user in QUOTAS['whitelisted_users']:
            return

        user_stats = self.get_user_stats()
        print(user_stats)

        if user_stats['today_request_count'] + 1 > QUOTAS['max_cloud_run_requests_per_user_per_day']:
            raise QuotaException(f"This project only accepts {QUOTAS['max_cloud_run_requests_per_user_per_day']} requests per user per day over all bigfunctions and you made {user_stats['today_request_count'] + 1} requests.")

        if QUOTAS.get('max_rows_per_user_per_day') and (
            user_stats['today_row_count_for_this_bigfunction'] + self.row_count > QUOTAS['max_rows_per_user_per_day']
        ):
            raise QuotaException(f"It only accepts {QUOTAS['max_rows_per_user_per_day']} rows per day per user and you called it today for {user_stats['today_row_count_for_this_bigfunction'] + self.row_count} rows.")


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


{% if code_process_rows_as_batch %}

def compute_all_rows(rows):
    {{ code|replace('\n', '\n    ') }}

{% else %}

def compute_one_row(args):
    {% for argument in arguments %}{{ argument.name }}, {% endfor %} = args
    {{ code|replace('\n', '\n    ') }}

{% endif %}


@app.route("/", methods=['POST'])
def handle():
    try:
        data = request.get_json()
        rows = data['calls']
        if QUOTAS['backend'] == 'datastore':
            quota_manager = DatastoreQuotaManager(data)
        else:
            quota_manager = SimpleQuotaManager(data)
        quota_manager.check_quotas()
        quota_manager.save_log()
        {% if code_process_rows_as_batch %}
        replies = compute_all_rows(rows)
        {% else %}
        replies = [compute_one_row(row) for row in rows]
        {% endif %}
        response = jsonify( { "replies" :  replies} )
        quota_manager.save_log(status='success')
        return response
    except QuotaException as e:
        error_message = e.args[0]
        quota_manager.save_log(status='quota_error', status_info=error_message)
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
        quota_manager.save_log(status='assertion_error', status_info=error_message)
        return jsonify({'errorMessage': error_message}), 400
    except Exception as e:
        error_reporter.report_exception(google.cloud.error_reporting.build_flask_context(request))
        error_message = (str(e) + ' --- ' + traceback.format_exc())[:1000]
        quota_manager.save_log(status='error', status_info=error_message)
        return jsonify({'errorMessage': f"{type(e).__name__}: {str(e)}"}), 400
