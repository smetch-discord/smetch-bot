from yaml import safe_load
from logging import getLogger, Logger, DEBUG
from pathlib import Path
from dataclasses import dataclass

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
        self.token: str = secrets.get("bot-token")
        self.mongo_uri: str = secrets.get("mongo-uri")

