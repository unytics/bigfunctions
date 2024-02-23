import os

import yaml

from . import deploy
from . import utils

BIGFUNCTIONS_FOLDER = 'bigfunctions'
DEFAULT_CONFIG_FILENAME = './config.yaml'

DEFAULT_CONFIG = yaml.safe_load(open(DEFAULT_CONFIG_FILENAME, encoding='utf-8').read()) if os.path.isfile(DEFAULT_CONFIG_FILENAME) else {}


class BaseBigFunction:

    def __init__(self, name):
        self.name = name
        self._config_from_file = None
        self.config_file_was_found = None

    @property
    def config_filename(self):
        return f'bigfunctions/{self.name}.yaml'

    @property
    def config_from_file(self):
        if not self._config_from_file:
            if not os.path.isfile(self.config_filename):
                utils.handle_error(f'Could not find configuration file {self.config_filename}')
            content = open(self.config_filename, encoding='utf-8').read()
            self._config_from_file = yaml.safe_load(content)
        return self._config_from_file

    @property
    def config(self):
        config = utils.merge_dict(dict(DEFAULT_CONFIG), self.config_from_file)
        config['name'] = self.name
        config['filename'] = self.config_filename
        return config

    def deploy(self, project, dataset):
        deploy.deploy(self, project, dataset)


