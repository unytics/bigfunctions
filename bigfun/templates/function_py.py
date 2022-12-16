import traceback

from flask import Flask, request, jsonify

import google.cloud.error_reporting

error_reporter = google.cloud.error_reporting.Client()
app = Flask(__name__)


def compute(args):
    {% for argument in arguments %}{{ argument.name }}, {% endfor %} = args
    {{ code|replace('\n', '\n    ') }}


@app.route("/", methods=['POST'])
def handle():
    try:
        request_json = request.get_json()
        print(request_json)
        rows = request_json['calls']
        replies = [compute(row) for row in rows]
        return jsonify( { "replies" :  replies} )
    except Exception:
        error_reporter.report_exception(google.cloud.error_reporting.build_flask_context(request))
        return traceback.format_exc(), 400
