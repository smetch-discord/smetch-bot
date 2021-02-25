import discord, random

from discord.ext import tasks

commands = discord.ext.commands

class HelpChannels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.names = [
            "help-helium",
            "help-hydrogen",
            "help-oxygen",
            "help-carbon",
            "help-lithium",
            "help-beryllium",
            "help-flourine",
            "help-sodium",
            "help-magnesium",
            "help-boron",
            "help-nitrogen",
            "help-neon"
        ]
        self.free = 809474026375479337
        self.occupied = 814176201924673566
        self.helpChannelsUpdate.start()
    
    @tasks.loop(seconds=5)
    async def helpChannelsUpdate(self):
        await self.bot.wait_until_ready()
        free = self.bot.get_channel(self.free)
        occupied = self.bot.get_channel(self.occupied)
        if len(free.text_channels) > 3:
            chn = random.choice(free.text_channels)
            await chn.delete()
        if len(free.text_channels) < 3:
            channels = [channel.name for channel in occupied.text_channels + free.text_channels]
            if len(channels) == len(self.names):
                return
            channel = await free.create_text_channel(name=random.choice([name for name in self.names if name not in channels]), topic=f"Send a message to claim this channel!")
            return await channel.send(embed=discord.Embed(
                color=discord.Color.green()
            )
            .set_author(name="This help channel has been marked as free!", icon_url="https://images-ext-2.discordapp.net/external/4TDeZeRHGZnQSodN58NxcnxHlSbVsNTuwYmn_OsmwsE/https/images-ext-1.discordapp.net/external/4W5YNj_vtSOdVCktXbG3wy8_rC0T8Xpdv5n56SSuncQ/https/raw.githubusercontent.com/python-discord/branding/master/icons/checkmark/green-checkmark-dist.png")
            .add_field(name="Send your question here to claim the channel", value="This channel will be dedicated to answering your question only. Others will try to answer and help you solve the issue.", inline=False)
            .add_field(name="Keep in mind:", value="• It's always ok to just ask your question. You don't need permission.\n• Explain what you are trying to do and what you actually need help with.", inline=False)
            .add_field(name="More info:", value="For more tips, check out <#809130188964495360> or this [website](https://dontasktoask.com/)", inline=False)
            .set_footer(text="Send a message here to occupy this channel!"))
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.channel.category or message.author.bot: return
        if not message.channel.category.id == self.free: return
        occupied = self.bot.get_channel(self.occupied)

        newOverwrites = occupied.overwrites

        newOverwrites[message.author] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

        await message.channel.edit(category=occupied, topic=f"Occupied! Recipient: {message.author.mention} : {message.author.id}", overwrites=newOverwrites)
    
    @commands.guild_only()
    @commands.command()
    async def close(self, ctx):
        if not ctx.channel.category: return
        if not ctx.channel.category.id == self.occupied: return

        if not ctx.channel.topic.split(" ")[-1] == str(ctx.author.id) and not ctx.author.guild_permissions.administrator: return

        return await ctx.channel.delete()

def setup(bot):
    bot.add_cog(HelpChannels(bot))