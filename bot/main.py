from discord.ext.commands import Bot
from discord import Intents
from yaml import safe_load
from backend.error_handler import ErrorHandler
from exts import Information

intents = Intents.default()
intents.members = True
intents.presences = True

bot: Bot = Bot('lol ', help_command=None, intents=intents)

config = safe_load(open('config.yml'))

bot.add_cog(Information(bot))
bot.add_cog(ErrorHandler(bot))

bot.run(config['token'])
