from discord.ext.commands import Bot
from .error_handler import ErrorHandler


def setup(bot: Bot):
    bot.add_cog(ErrorHandler(bot))
