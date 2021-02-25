import discord, asyncio

from core import checks, embeds

commands = discord.ext.commands

class PurgeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.max_without_warning = 100
    
    @commands.guild_only()
    @checks.canBan()
    @commands.command(aliases=["clear"])
    async def purge(self, ctx, limit=10, *, author:discord.Member=None):
        
        if limit > self.max_without_warning:
            confirmMsg = await ctx.send(embed=embeds.Embeds(f":warning: You are about to delete **{self.max_without_warning}+** messages! Are you sure?").warn())

            emojis = ["✅", "❎"]

            for emoji in emojis: await confirmMsg.add_reaction(emoji)

            def isValid(reaction, user):
                return user.id == ctx.author.id and reaction.message.id == confirmMsg.id and reaction.emoji in emojis
            
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=isValid, timeout=60)
            except asyncio.TimeoutError:
                await confirmMsg.clear_reactions()
                return await confirmMsg.edit(embed=embeds.Embeds("Purge canceled!").error())
            
            await confirmMsg.delete()

            if reaction.emoji == emojis[1]:
                return await ctx.send(embed=embeds.Embeds("Purge canceled!").error(), delete_after=5)

        await ctx.message.delete()    
        
        messages = await ctx.channel.purge(limit=limit, check=lambda message: message.author == author if author else message)

        return await ctx.send(embed=embeds.Embeds(f"Deleted **{len(messages)}** messages!").success(), delete_after=5)

def setup(bot):
    bot.add_cog(PurgeCommand(bot))