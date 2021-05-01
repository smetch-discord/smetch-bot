from typing import Dict

from yaml import safe_load
from logging import getLogger, Logger, DEBUG
from pathlib import Path

import os

log: Logger = getLogger(__name__)
log.setLevel(DEBUG)

if Path("config.yml").exists():
    log.info("Config file found")
    with open("config.yml") as config_file:
        config: dict = safe_load(config_file)
    log.info("Successfully parsed YAML file")
else:
    # log.critical("No config file was found")
    # raise FileNotFoundError("config.yml")
    config: dict = {'secrets': {'bot-token': os.environ.get('TOKEN'), 'prefix': os.environ.get('PREFIX')}}


class Secrets:

    def __init__(self) -> None:
        if not ("secrets" in config.keys()):
            log.critical("No secrets field was located in config")
            raise KeyError("No secrets key found")

        secrets_list: dict = config["secrets"]

        self.prefix: str = secrets_list.get("prefix")
        self.bot_token: str = secrets_list.get("bot-token")
        self.mongo_uri: str = secrets_list.get("mongo-uri")
        self.github_token: str = secrets_list.get("github-token")

        pretty_print_names: dict[str, str] = {
            "prefix": "Discord bot prefix",
            "bot-token": "Discord bot token",
            "mongo-uri": "MongoDB connection URI",
            "github-token": "GitHub token"
        }

        for secret in (self.prefix, self.bot_token, self.mongo_uri, self.github_token):
            if secret is None:
                log.critical("Something is missing")

    @staticmethod
    def bot_token_check(token: str):
        pass

secrets = Secrets()
