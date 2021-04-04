from bot.constants import load_configuration
from tests.helpers.mock_yaml import MockYAMLConfig
import pytest


def test_load_config_file():
    temp_yaml = MockYAMLConfig()
    config = load_configuration('test_config.yml')
    assert config == {
            'BOT_TOKEN': 'bOt-ToKeN-gOeS-hErE',
            'MONGO_URI': 'mongodb+srv://db_uri.com',
            'GITHUB_TOKEN': 'gItHuB-tOkEn-GoEs-HeRe'
    }
    temp_yaml.destroy()


def test_load_configuration():
    temp_yaml = MockYAMLConfig('bot-token')
    with pytest.raises(KeyError):
        load_configuration('test_config.yml')
    temp_yaml.destroy()
