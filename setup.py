import setuptools


VERSION = '0.11'


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name='bigfunctions',
    packages=['bigfun'],
    version=VERSION,
    author='Unytics',
    author_email='paul.marcombes@unytics.io',
    description='Supercharge BigQuery with BigFunctions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url=f'https://github.com/unytics/bigfunctions/archive/refs/tags/v{VERSION}.tar.gz',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    package_data={'bigfun': ['templates/**/*', 'website/**/*', 'datastore/**/*']},
    include_package_data=True,
    install_requires=[
        'google-cloud-bigquery',
        'google-cloud-bigquery-connection',
        'google-cloud-storage',
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
