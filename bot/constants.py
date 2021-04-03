import yaml
import io
import logging

log = logging.getLogger(__name__)

# Load all configuration constants from file
config_file: io.TextIOWrapper = io.open('config.yml')
log.info('Successfully opened the config.yaml file')

# Parse YAML file
config: dict = yaml.safe_load(config_file)
log.info('Successfully parsed the config.yaml file')

# Define constants for use in the bot
BOT_TOKEN: str = config.__getitem__('bot-token')
MONGO_URI: str = config.__getitem__('mongo-uri')
GITHUB_TOKEN: str = config.__getitem__('github-token')
log.info('Loaded all constants')
