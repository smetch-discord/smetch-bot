import bot.log_setup
from discord.ext.commands import Bot
from discord import Intents
from yaml import safe_load

intents = Intents.default()
intents.members = True
intents.presences = True

bot: Bot = Bot('lol ', intents=intents)

config = safe_load(open('config.yml'))

bot.load_extension('bot.exts')
bot.load_extension('bot.backend')

bot.run(config['token'])
