import yaml
import io
import os


class MockYAMLConfig:

    def __init__(self, *missing: tuple, filename: str = 'test_config.yml') -> None:
        self.filename = filename
        yaml_keys: dict = {
            'prefix': 's!',
            'bot-token': 'bOt-ToKeN-gOeS-hErE',
            'mongo-uri': 'mongodb+srv://db_uri.com',
            'github-token': 'gItHuB-tOkEn-GoEs-HeRe'
        }

        for key in missing:
            yaml_keys.pop(key, None)

        yaml_file = io.open(self.filename, 'w')

        with io.open(self.filename, 'w') as yaml_file:
            yaml.dump(yaml_keys, yaml_file, default_flow_style=False)

    def destroy(self):
        os.remove(self.filename)
