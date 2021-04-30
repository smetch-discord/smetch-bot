import bot.log_setup
from discord.ext.commands import Bot
from discord import Intents
from yaml import safe_load

intents = Intents.default()
intents.members = True
intents.presences = True

config = safe_load(open('config.yml'))

smetch: Bot = Bot(config['prefix'], intents=intents)

smetch.load_extension('bot.exts')
smetch.load_extension('bot.backend')

smetch.run(config['bot-token'])
