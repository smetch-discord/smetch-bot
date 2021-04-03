import yaml
import io
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Load all configuration constants from file
try:
    config_file: io.TextIOWrapper = io.open('config.yml')
    log.info('Successfully opened the config.yml file')
except FileNotFoundError:
    log.critical(
        "No config.yml file was found. \
        Please make sure the file is called 'config.yml'. \
        Make sure it is in the top level directory."
    )
    log.exception('Missing config.yml found')

# Parse YAML file
config: dict = yaml.safe_load(config_file)
log.info('Successfully parsed the config.yml file')

# Define constants for use in the bot
BOT_TOKEN: str = config.__getitem__('bot-token')
MONGO_URI: str = config.__getitem__('mongo-uri')
GITHUB_TOKEN: str = config.__getitem__('github-token')
log.info('Loaded all constants')
