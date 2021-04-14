from discord.ext.commands import Bot
from .information import Information
from .moderation import Detector


def setup(bot: Bot):
    bot.add_cog(Information(bot))
    bot.add_cog(Detector(bot))
