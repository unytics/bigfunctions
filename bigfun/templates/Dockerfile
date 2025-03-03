FROM {{ dockerfile.image if dockerfile is defined and dockerfile.image is defined else 'ghcr.io/astral-sh/uv:python3.11-bookworm-slim' }}

# Install apt packages
{% if dockerfile is defined and dockerfile.apt_packages is defined %}
RUN apt update && apt install -y {{ dockerfile.apt_packages }}
{% endif %}

EXPOSE 8080

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV PORT=8080


# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN uv pip install --system --no-cache-dir -r requirements.txt || pip install -r requirements.txt

{% if dockerfile is defined %}{{ dockerfile.additional_commands }}{% endif %}
{{ additional_install_commands_in_dockerfile }}

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind :8080 --workers 1 --threads {{ cloud_run.concurrency if cloud_run is defined and cloud_run.concurrency is defined else 8 }} --timeout 0 main:app
