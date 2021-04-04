from bot.constants import load_configuration
from tests.helpers.mock_yaml import MockYAMLConfig
import pytest


def test_load_config_file():
    mock_yaml = MockYAMLConfig()
    config = load_configuration('test_config.yml')
    assert config == {
        'BOT_TOKEN': 'bOt-ToKeN-gOeS-hErE',
        'MONGO_URI': 'mongodb+srv://db_uri.com',
        'GITHUB_TOKEN': 'gItHuB-tOkEn-GoEs-HeRe',
        'PREFIX': 's!'
    }
    mock_yaml.destroy()


@pytest.mark.parametrize('missing', ['bot-token', 'prefix'])
def test_load_configuration(missing):
    mock_yaml = MockYAMLConfig(missing)
    with pytest.raises(KeyError):
        load_configuration('test_config.yml')
    mock_yaml.destroy()
