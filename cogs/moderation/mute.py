import discord, datetime

from dateparser import parse
from core import embeds, files, checks
from core.database import Punishments

from discord.ext import tasks

commands = discord.ext.commands

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.checkMutes.start()
    
    @tasks.loop(seconds=1, reconnect=True)
    async def checkMutes(self):
        await self.bot.wait_until_ready()
        config = files.Data("config").yaml_read()
        guild = self.bot.get_guild(config["server"])
        role = guild.get_role(config["muteRole"])
        mutes = Punishments().getCases(type="mute")
        for mute in mutes:
            member = guild.get_member(mute["user"])
            if not member:
                Punishments().removeCase(user=mute["user"], type="mute")
            elif not role in member.roles:
                Punishments().removeCase(user=mute["user"], type="mute")
                Punishments(mute["user"]).addCase(mod=mute["mod"], type="expired mute", date=datetime.datetime.now(), reason=mute["reason"])
            elif mute["due"] <= datetime.datetime.now():
                try:
                    await member.remove_roles(role)
                    await member.send(embed=embeds.Embeds("Your mute was expired!").success())
                except: pass
                Punishments().removeCase(user=mute["user"], type="mute")
                Punishments(mute["user"]).addCase(mod=mute["mod"], type="expired mute", date=datetime.datetime.now(), reason=mute["reason"])

    @commands.guild_only()
    @checks.mainServer()
    @checks.canMute()
    @commands.command()
    async def mute(self, ctx, user:discord.Member, time, *, reason=None):
        if user.id == ctx.author.id: return await ctx.send(embed=embeds.Embeds("What the fuck are you trying to do?").error())
        if user.top_role >= ctx.author.top_role: return await ctx.send(embed=embeds.Embeds("You cannot warn users with an equal or higher role than you.").error())
        if ctx.guild.get_member(self.bot.user.id).top_role <= user.top_role: return await ctx.send(embed=embeds.Embeds("My role is not high enough to warn this user.").error())

        muteRole = ctx.guild.get_role(files.Data("config").yaml_read()["muteRole"])

        if muteRole in user.roles: return await ctx.send(embed=embeds.Embeds("This user is already muted.").error())

        expire_date = parse(f"in {time}")

        if not expire_date: return await ctx.send(embed=embeds.Embeds("Invalid time!").error())

        if expire_date < datetime.datetime.now(): return await ctx.send(embed=embeds.Embeds("Invalid time!").error())

        await user.add_roles(muteRole)

        try:
            await user.send(embed=discord.Embed(
                title=f"You were MUTED in {ctx.guild}",
                description=f"""You were **MUTED** in **{ctx.guild}**.
This means that you have violated our chat **Rules & Guidelines**.

**Reason:** {reason}""",
                color=discord.Color.orange()
            )
            .set_footer(text="If you think you were falsely muted, contact a Moderator!", icon_url=user.avatar_url_as(static_format="png")))
        except: pass

        Punishments(user.id).addCase(mod=ctx.author.id, type="mute", date=datetime.datetime.now(), due=expire_date,reason=reason)

        modLog = self.bot.get_channel(files.Data("logs").yaml_read()["modLog"])

        await modLog.send(embed=discord.Embed(
            description=f"""**Member:** {user.mention} `({user} | {user.id})`
**Action:** Mute
**Reason:** {reason}""",
            color=discord.Color.orange(),
            timestamp=datetime.datetime.now()
        )
        .set_footer(text=f"Case #{len(Punishments().getCases())-1}"))

        await ctx.message.add_reaction("✅")

        return await ctx.send(embed=embeds.Embeds(f"Successfully muted {user.mention} `({user})`").success())

    @commands.guild_only()
    @checks.mainServer()
    @checks.canMute()
    @commands.command()
    async def unmute(self, ctx, user:discord.Member):
        muteRole = ctx.guild.get_role(files.Data("config").yaml_read()["muteRole"])
        if not muteRole in user.roles:
            return await ctx.send(embed=embeds.Embeds("This user is not muted!").error())
        await user.remove_roles(muteRole)
        
        try:
            await user.send(embed=embeds.Embeds("You were unmuted!").success())
        except: pass
        
        Punishments().removeCase(type="mute", user=user.id)

        return await ctx.send(embed=embeds.Embeds(f"Successfully unmuted {user.mention} `({user})`").success())

def setup(bot):
    bot.add_cog(MuteCommand(bot))