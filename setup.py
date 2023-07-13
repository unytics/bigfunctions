from setuptools import setup

setup(
    name='bigfun',
    version='0.1.0',
    packages=['bigfun'],
    package_data={'': ['*']},
    include_package_data=True,
    install_requires=[
        'google-cloud-bigquery',
        'google-cloud-bigquery_connection',
        'pyyaml',
        'jinja2',
        'mkdocs-material',
        'click',
        'click-help-colors',
    ],
    entry_points={
        'console_scripts': [
            'bigfun = bigfun.cli:cli',
        ],
    },
)
