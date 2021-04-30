import bot.log_setup
from bot import constants
from discord.ext.commands import Bot
from discord import Intents
from yaml import safe_load

intents = Intents.default()
intents.members = True
intents.presences = True

smetch: Bot = Bot(constants.secrets.prefix, intents=intents)

smetch.load_extension('bot.exts')
smetch.load_extension('bot.backend')

smetch.run(constants.secrets.bot_token)
