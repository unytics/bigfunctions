from setuptools import setup

setup(
    name='bigfun',
    version='0.1.0',
    packages=['bigfun'],
    include_package_data=False,
    install_requires=[
        'google-cloud-bigquery',
        'pyyaml',
        'click',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'bigfun = bigfun.cli:cli',
        ],
    },
)
