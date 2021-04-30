from typing import Dict

from yaml import safe_load
from logging import getLogger, Logger, DEBUG
from pathlib import Path

log: Logger = getLogger(__name__)
log.setLevel(DEBUG)

if Path("config.yml").exists():
    log.info("Config file found")
    with open("config.yml") as config_file:
        config: dict = safe_load(config_file)
    log.info("Successfully parsed YAML file")
else:
    log.critical("No config file was found")
    raise FileNotFoundError("config.yml")


class Secrets:

    def __init__(self) -> None:
        if not ("secrets" in config.keys()):
            log.critical("No secrets field was located in config")
            raise KeyError("No secrets key found")
        secrets: dict = config["secrets"]

        self.bot_token: str = secrets.get("bot-token")
        self.mongo_uri: str = secrets.get("mongo-uri")
        self.github_token: str = secrets.get("github-token")

        pretty_print_names: dict[str, str] = {
            "bot-token": "Discord bot token",
            "mongo-uri": "MongoDB connection URI",
            "github-token": "GitHub token"
        }

        for secret in (self.bot_token, self.mongo_uri, self.github_token):
            if secret is None:
                secret_name: str = f'{secret=}'.split("=")[0]
                secret_name: str = pretty_print_names[secret_name]
                log.critical(f'No {secret_name} was found')

    @staticmethod
    def bot_token_check(token: str):
        pass
