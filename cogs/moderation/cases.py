import discord, requests, asyncio

from typing import Union
from textwrap import dedent

from core.database import Punishments
from core import checks, embeds

commands = discord.ext.commands

class Cases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    @commands.command()
    async def removeCase(self, ctx, case:int):
        case = Punishments().getCase(_id=case)

        if not case: return await ctx.send(embed=embeds.Embeds("Case not found!").error())
        
        Punishments().removeCase(_id=case['_id'])

        user = await self.bot.fetch_user(case['user'])

        mod = await self.bot.fetch_user(case['mod'])

        msg = await ctx.send(embed=discord.Embed(
            title="Case Removed",
            description=dedent(f"""**User:** `{user}`
            **Mod:** `{mod}`
            **Date:** `{case['date'].strftime('%B %d, %Y')}`
            **Reason:** {case['reason']}"""),
            color=discord.Color.green()
        )
        .set_footer(text="Restore case by reacting below!"))

        await msg.add_reaction("♻️")
        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', check=lambda reaction, user: reaction.message.id == msg.id and user.id == ctx.author.id and reaction.emoji == "♻️", timeout=60)
        except:
            return await msg.clear_reactions()
        
        Punishments().col.insert_one(case)

        await msg.clear_reactions()

        return await ctx.send(embed=embeds.Embeds("Case restored!").success())

    @commands.guild_only()
    @checks.canWarn()
    @commands.command(aliases=["cases"])
    async def history(self, ctx, user:Union[discord.Member, int], page=1):
        if isinstance(user, int):
            cases = sorted(Punishments().getCases(user=user))
            name = await self.bot.fetch_user(user)
            name = str(name)
        else:
            cases = Punishments().getCases(user=user.id)
            name = str(user)
        
        pages = [cases[x:x+10] for x in range(0, len(cases), 10)]

        current_page = page-1

        msg = await ctx.send(embed=discord.Embed(
            title=f"Cases | {name} ({len(cases)})",
            description='\n\n'.join([f"`Case #{case['_id']}` | {case['type']} | By `{await self.bot.fetch_user(case['mod'])}`\n*{case['reason']}*" for case in pages[current_page]]),
            color=discord.Color.red()
        )
        .set_footer(text=f"Page {current_page+1}/{len(pages)}"))

        emojis = ["⏪", "⬅️", "➡️", "⏩"]

        for emoji in emojis: await msg.add_reaction(emoji)

        def isValid(reaction, user):
            return reaction.message.id == msg.id and user.id == ctx.author.id and reaction.emoji in emojis and not user.bot

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=isValid, timeout=120)
            except asyncio.TimeoutError:
                return await msg.clear_reactions()

            if reaction.emoji == emojis[0]:
                current_page = 0
            elif reaction.emoji == emojis[-1]:
                current_page = len(pages)-1
            elif reaction.emoji == emojis[1]:
                if current_page != 0: current_page -= 1
            else:
                if current_page != len(pages)-1: current_page += 1

            try:
                await msg.remove_reaction(reaction.emoji, ctx.author)
            except: pass

            await msg.edit(embed=discord.Embed(
            title=f"Cases | {name} ({len(cases)})",
            description='\n\n'.join([f"`Case #{case['_id']}` | {case['type']} | By `{await self.bot.fetch_user(case['mod'])}`\n*{case['reason']}*" for case in pages[current_page]]),
            color=discord.Color.red()
            )
            .set_footer(text=f"Page {current_page+1}/{len(pages)}"))
        
    @commands.guild_only()
    @checks.canKick()
    @commands.command()
    async def case(self, ctx, case:int):
        case = Punishments().getCase(_id=case)

        if not case: return await ctx.send(embed=embeds.Embeds("Case not found!").error())

        user = await self.bot.fetch_user(case['user'])

        mod = await self.bot.fetch_user(case['mod'])

        return await ctx.send(embed=discord.Embed(
            title="Inspecting Case",
            description=dedent(f"""**User:** `{user}`
            **Mod:** `{mod}`
            **Date:** `{case['date'].strftime('%B %d, %Y')}`
            **Reason:** {case['reason']}"""),
            color=discord.Color.green()
        ))
        

def setup(bot):
    bot.add_cog(Cases(bot))