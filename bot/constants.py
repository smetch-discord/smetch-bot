import yaml
import io
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


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

    try:
        config_dict.__getitem__('bot-token')
        log.info("Successfully loaded all required constants: 'bot-token'")
    except KeyError as err:
        log.critical(f'Missing bot token from {config_filename}')
        log.exception('Missing bot token', exc_info=True)
        raise err

    config = {}
    for yaml_key in config_dict.keys():
        new_key = yaml_key.upper().replace('-', '_')
        config[new_key] = config_dict[yaml_key]

    del config_dict

    return config
