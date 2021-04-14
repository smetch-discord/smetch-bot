from discord.ext.commands import Bot
from .information import Information


def setup(bot: Bot):
    bot.add_cog(Information(bot))
