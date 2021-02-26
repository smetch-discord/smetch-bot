import discord

from core import embeds, files

commands = discord.ext.commands

class Thanking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed = [
            807226206486265886,
            807227119884959766,
            807227628511428608,
            807227983118467072,
            807228592751902760
        ]

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild or message.author.bot: return
        if not message.guild.id == files.Data("config").yaml_read()['server']: return
        if not message.channel.category: return
        if not message.channel.category.id in self.allowed: return

        if (message.content.lower().startswith("thanks ") or message.content.lower().startswith("thank ")) and message.mentions:
            return await message.channel.send(embed=embeds.Embeds(f"{message.author.mention} thanked " + ', '.join(member.mention for member in message.mentions)).success())

def setup(bot):
    bot.add_cog(Thanking(bot))