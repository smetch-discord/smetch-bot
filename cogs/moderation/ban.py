import discord, datetime

from core.database import Punishments

from typing import Union

from core import embeds, checks, files

commands = discord.ext.commands

class BanCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @checks.mainServer()
    @checks.canBan()
    @commands.command()
    async def ban(self, ctx, user:Union[discord.Member, int], *, reason=None):
        if isinstance(user, int):
            user = await self.bot.fetch_user(user)

        else:
            if user.id == ctx.author.id: return await ctx.send(embed=embeds.Embeds("What the fuck are you trying to do?").error())
            if user.top_role >= ctx.author.top_role: return await ctx.send(embed=embeds.Embeds("You cannot ban users with an equal or higher role than you.").error())
            if ctx.guild.get_member(self.bot.user.id).top_role <= user.top_role: return await ctx.send(embed=embeds.Embeds("My role is not high enough to ban this user.").error())

        try:
            await user.send(embed=discord.Embed(
                title=f"You were BANNED from {ctx.guild}",
                description=f"""You were **BANNED** from **{ctx.guild}**.
This means that you cannot rejoin the server, and making alternative accounts in order to bypass this punishment is not allowed either.

**Reason:** {reason}""",
                color=discord.Color.red()
            )
            .set_footer(text="Bans are permanent and not appealable • Adios!", icon_url=user.avatar_url_as(static_format="png")))
        except: pass

        await ctx.guild.ban(user, reason=f"{reason} - by {ctx.author}");

        Punishments(user.id).addCase(mod=ctx.author.id, type="ban", date=datetime.datetime.now(), reason=reason)

        modLog = self.bot.get_channel(files.Data("logs").yaml_read()["modLog"])

        await modLog.send(embed=discord.Embed(
            description=f"""**Member:** {user.mention} `({user} | {user.id})`
**Action:** Ban
**Reason:** {reason}""",
            color=discord.Color.red(),
            timestamp=datetime.datetime.now()
        )
        .set_footer(text=f"Case #{len(Punishments().getCases())-1}"))

        await ctx.message.add_reaction("✅")

        return await ctx.send(embed=embeds.Embeds(f"Successfully banned {user.mention} `({user})`").success())
    
    @commands.guild_only()
    @checks.mainServer()
    @checks.canBan()
    @commands.command()
    async def unban(self, ctx, userID:int):
        await ctx.guild.unban(discord.Object(id=userID))

        await ctx.message.add_reaction("✅")

        return await ctx.send(embed=embeds.Embeds(f"Successfully unbanned <@{userID}> `({userID})`").success())

def setup(bot):
    bot.add_cog(BanCommand(bot))