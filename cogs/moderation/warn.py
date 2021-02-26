import discord, datetime

from core.database import Punishments

from core import embeds, checks, files

commands = discord.ext.commands

class WarnCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @checks.mainServer()
    @checks.canWarn()
    @commands.command()
    async def warn(self, ctx, user:discord.Member, *, reason=None):
        if user.id == ctx.author.id: return await ctx.send(embed=embeds.Embeds("What the fuck are you trying to do?").error())
        if user.top_role >= ctx.author.top_role: return await ctx.send(embed=embeds.Embeds("You cannot warn users with an equal or higher role than you.").error())
        if ctx.guild.get_member(self.bot.user.id).top_role <= user.top_role: return await ctx.send(embed=embeds.Embeds("My role is not high enough to warn this user.").error())

        try:
            await user.send(embed=discord.Embed(
                title=f"You were WARNED in {ctx.guild}",
                description=f"""You were **WARNED** in **{ctx.guild}**.
This means that you have violated our **Rules & Guidelines**.

**Reason:** {reason}""",
                color=discord.Color.orange()
            )
            .set_footer(text="If you think you were falsely warned, contact a Moderator!", icon_url=user.avatar_url_as(static_format="png")))
        except: pass

        Punishments(user.id).addCase(mod=ctx.author.id, type="warn", date=datetime.datetime.now(), reason=reason)

        modLog = self.bot.get_channel(files.Data("logs").yaml_read()["modLog"])

        await modLog.send(embed=discord.Embed(
            description=f"""**Member:** {user.mention} `({user} | {user.id})`
**Action:** Warn
**Reason:** {reason}""",
            color=discord.Color.orange(),
            timestamp=datetime.datetime.now()
        )
        .set_footer(text=f"Case #{len(Punishments().getCases())-1}"))

        await ctx.message.add_reaction("✅")

        return await ctx.send(embed=embeds.Embeds(f"Successfully warned {user.mention} `({user})`").success())

def setup(bot):
    bot.add_cog(WarnCommand(bot))