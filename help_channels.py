import discord
from discord.ext import commands

class Help_Channels(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        return
    
    @commands.Cog.listener('on_message')
    async def help_channel_listener(self, message):
        if message.channel.category_id == 809474026375479337:
            await message.channel.edit(category=discord.utils.get(message.guild.categories, id=814176201924673566))
            await message.pin()
            