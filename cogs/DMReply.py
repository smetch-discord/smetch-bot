import discord, asyncio

from core import files, embeds, checks

commands = discord.ext.commands

class DMReply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def inCategory(self, message):
        category = files.Data("config").yaml_read()["dmCategory"]
        if not message.channel.category: return False
        if message.channel.category.id != category: return False
        return True
    
    def getChannel(self, message):
        category = self.bot.get_channel(files.Data("config").yaml_read()["dmCategory"])
        try:
            return next(channel for channel in category.text_channels if channel.topic == str(message.author.id))
        except:
            return None

    async def createChannel(self, message):
        category = self.bot.get_channel(files.Data("config").yaml_read()["dmCategory"])
        channel = await category.create_text_channel(name=str(message.author).replace("#", "-"), topic=str(message.author.id))
        return channel
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot: return
        if not isinstance(message.channel, discord.DMChannel) and not self.inCategory(message): return

        if isinstance(message.channel, discord.DMChannel):
            channel = self.getChannel(message)
            if not channel:
                channel = await self.createChannel(message)
            return await channel.send(embed=embeds.DMMessage(message).userEmbed())

        if self.inCategory(message):

            if message.content.lower().startswith("-i") or message.content.lower().startswith(files.Data("config").yaml_read()['prefix']): return

            try:
                user = await self.bot.fetch_user(int(message.channel.topic))
                return await user.send(embeds.DMMessage(message).papyrusMessage())
            except Exception as e:
                return await message.channel.send(embed=embeds.Embeds("There was a problem replying to that user.").error(Error=e))

    @commands.guild_only()
    @checks.manager()
    @commands.command()
    async def closedm(self, ctx):
        if not self.inCategory(ctx.message): return await ctx.send(embed=embeds.Embeds("This command cannot be used here!").error())
        await ctx.send(embed=discord.Embed(
            title="Closing the channel...",
            color=discord.Color.red()
        ))
        await asyncio.sleep(3)
        return await ctx.channel.delete()

def setup(bot):
    bot.add_cog(DMReply(bot))