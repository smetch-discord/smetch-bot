from discord.ext.commands import Bot
from .information import Information
from .moderation import Detector
from .moderation import Moderation


def setup(bot: Bot):
    bot.add_cog(Information(bot))
    bot.add_cog(Detector(bot))
    bot.add_cog(Moderation(bot))
