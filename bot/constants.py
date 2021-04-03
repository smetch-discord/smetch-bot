import yaml
import io

# Load all configuration constants from file
config_file: io.TextIOWrapper = io.open('config.yml')

# Parse YAML file
config: dict = yaml.safe_load(config_file)

# Define constants for use in the bot
BOT_TOKEN: str = config.__getitem__('bot-token')
MONGO_URI: str = config.__getitem__('mongo-uri')
GITHUB_TOKEN: str = config.__getitem__('github-token')
