import discord

from core import embeds, files

commands = discord.ext.commands

class Thanking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild or message.author.bot: return
        if not message.guild.id == files.Data("config").yaml_read()['server']: return
        if not message.channel.category: return
        if not message.channel.category.id == 814176201924673566: return

        if (message.content.lower().startswith("thanks ") or message.content.lower().startswith("thank ")) and message.mentions:
            return await message.channel.send(embed=embeds.Embeds(f"{message.author.mention} thanked " + ', '.join(member.mention for member in message.mentions)).success())

def setup(bot):
    bot.add_cog(Thanking(bot))