import yaml
import io
import os


class MockYAMLConfig:

    def __init__(self, *missing: tuple, filename: str = 'test_config.yml') -> None:
        self.filename = filename
        yaml_keys: dict = {
            'bot-token': 'bOt-ToKeN-gOeS-hErE',
            'mongo-uri': 'mongodb+srv://db_uri.com',
            'github-token': 'gItHuB-tOkEn-GoEs-HeRe'
        }

        for key in missing:
            yaml_keys.pop(key, None)

        with io.open(self.filename) as yaml_file:
            yaml.dump(yaml_keys, yaml_file, default_flow_style=False)

    def remove(self):
        os.remove(self.filename)
