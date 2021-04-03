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
try:
    config: dict = yaml.safe_load(config_file)
    log.info('Successfully parsed the config.yml file')
except Exception:
    log.critical("Failed to parse config.yml for an unknown reason")
    log.exception("Failed YAML parsing", exc_info=True)

# Define constants for use in the bot
try:
    BOT_TOKEN: str = config.__getitem__('bot-token')
except KeyError:
    log.critical("Missing 'bot-token' field from config.yml file. Please insert this field immediately")
    log.exception("Missing bot token", exc_info=True)
