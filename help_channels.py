import discord, random, asyncio
from discord.ext import commands

class Help_Channels(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        return
    
    @commands.Cog.listener('on_message')
    async def help_channel_listener(self, message):
        FREE = 809474026375479337
        OCCUPIED = 814176201924673566
        DORMANT = 809491305222635540
        if message.channel.category_id == FREE:
            await message.channel.edit(category=discord.utils.get(message.guild.categories, id=OCCUPIED))
            dormant_category = discord.utils.get(message.guild.categories, id = DORMANT)
            channel_to_move = random.choice(dormant_category.channels)
            await channel_to_move.purge(limit=2)
            await channel_to_move.send(embed=discord.Embed(color=0x00ff8f).set_author(name="This help channel has been marked as free", icon_url="https://images-ext-1.discordapp.net/external/4W5YNj_vtSOdVCktXbG3wy8_rC0T8Xpdv5n56SSuncQ/https/raw.githubusercontent.com/python-discord/branding/master/icons/checkmark/green-checkmark-dist.png").add_field(name="Send your question here to claim the channel", value="This channel will be dedicated to answering your question only. Others will try to answer and help you solve the issue.", inline=False).add_field(name="Keep in mind:", value="• It's always ok to just ask your question. You don't need permission.\n• Explain what you are trying to do and what you actually need help with.", inline=False).add_field(name="More info:", value="For more tips, check out <#809130188964495360> or [this website](https://dontasktoask.com/)", inline=False).set_footer(text="The channel will be released after 30 minutes or when you type '!close'"))
            await message.author.add_roles(message.guild.get_role(809184355485351966))
            await channel_to_move.edit(category=discord.utils.get(message.guild.categories, id=FREE))
            await channel_to_move.edit(overwrites=channel_to_move.category.overwrites)
            await asyncio.sleep(1800)

    @commands.command(name='close')
    async def close_help_channel(self, ctx):
        if ctx.channel.category.id != 814176201924673566:
            return
        await ctx.channel.edit(category=discord.utils.get(ctx.guild.categories, id=809491305222635540))
        await ctx.send(embed=discord.Embed(colour=0xff3300).add_field(name='What happened?', value='This help channel has been marked as **dormant**, and has been moved into dormant category. It is no longer possible to send messages in this channel until it becomes available again.', inline=False).add_field(name='My question hasn\'t been answered!', value='If your question wasn\'t answered yet, you can claim a newavailable help channel by simply asking your question in an available channel again. Consider rephrasing the question to maximize your chance of getting a good answer. If you\'re not sure how, have at either <#809130188964495360> or [this website](https://dontasktoask.com/)', inline=False).set_author(name="This help channel has been marked as dormant", icon_url='https://yfcfredericton.ca/wp-content/uploads/icon-no-entry-300x298.png').set_footer(text="Dormant channel"))
        await ctx.channel.edit(overwrites=ctx.channel.category.overwrites)