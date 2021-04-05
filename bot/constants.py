import yaml
import io
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Constants:

    def __init__(self, bot, color) -> None:
        self.bot = bot
        self.color = color


class Bot:

    def __init__(self, prefix: str, token: str) -> None:
        self.prefix = prefix
        self.token = token
        return


class Color:

    def __init__(self, color_dict) -> None:
        for key in color_dict.keys():
            current_hex = color_dict[key]
            current_hex.replace('#', '0x')
            color_dict[key] = hex(current_hex)

        for key in color_dict.keys():
            setattr(self, key, color_dict[key])


def load_config_file(config_filename: str = 'config.yml'):
    '''Load all configuration constants from file'''
    try:
        config_file: io.TextIOWrapper = io.open(config_filename)
        log.info(f'Successfully opened the {config_filename} file')
        return config_file
    except FileNotFoundError as err:
        log.critical(
            f"No {config_filename} file was found. \
            Please make sure the file is called '{config_filename}'. \
            Make sure it is in the top level directory."
        )
        log.exception(f'Missing {config_filename}', exc_info=True)
        raise err


def parse_config_file(config_file: io.TextIOWrapper):
    '''Parse the config file into a dictionary'''
    try:
        config: dict = yaml.safe_load(config_file)
        log.info('Successfully parsed the config file')
        return config
    except Exception as err:
        log.critical('Failed to parse the config file for an unknown reason')
        log.exception('Failed YAML parsing', exc_info=True)
        raise err


def load_configuration(config_filename: str = 'config.yml'):
    config_file = load_config_file(config_filename)
    config_dict = parse_config_file(config_file)

    required: list = ['bot-token', 'prefix']

    for key in required:
        try:
            config_dict.__getitem__(key)
            log.info(f'Successfully loaded the required constant: \'{key}\'')
        except KeyError as err:
            log.critical(f'Missing {key} from {config_filename}')
            log.exception(f'Missing {key}', exc_info=True)
            raise err

    config = {}
    for yaml_key in config_dict.keys():
        new_key = yaml_key.upper().replace('-', '_')
        config[new_key] = config_dict[yaml_key]

    return config


def get_constants(config_filename: str = 'config.yml'):
    config = load_configuration(config_filename)
    constants = Constants(
        bot=Bot(
            prefix=config['PREFIX'],
            token=config['BOT_TOKEN']
        ),
        color=Color(
            color_dict=config['COLOR']
        )
    )
    return constants
