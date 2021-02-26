import discord, datetime, yaml, asyncio
import forbiddenfruit as ff

from discord.ext import tasks

from core import embeds, files, database, checks

commands = discord.ext.commands

@ff.curses(list, "paginate")
def paginate(self, per_page):
    return [self[x:x+per_page] for x in range(0, len(self), per_page)]
class Thanking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed = [
            807226206486265886,
            807227119884959766,
            807227628511428608,
            807227983118467072,
            807228592751902760,
            814176201924673566
        ]
        self.keywords = [
            "thanks",
            "thank",
            "thx"
        ]

        self.reset_manager.start()

    @tasks.loop(seconds=10, reconnect=True)
    async def reset_manager(self):
        await self.bot.wait_until_ready()
        settings = files.Data("thanks_settings").yaml_read()
        if settings["last_day"] != datetime.datetime.now().strftime("%A"):
            database.Thanks().reset_daily
            settings["last_day"] = datetime.datetime.now().strftime("%A")
        if datetime.datetime.now().strftime("%A") == "Sunday" and settings["do_restart"]:
            database.Thanks().reset_weekly
            settings["do_restart"] = False
        if datetime.datetime.now().strftime("%A") == "Wednesday":
            settings["do_restart"] = True
        with open("data/thanks_settings.yml", "w") as f:
            yaml.dump(settings, f)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        thankings = database.Thanks(member.id)
        if thankings.exists:
            thankings.delete

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild or message.author.bot: return
        if not message.guild.id == files.Data("config").yaml_read()['server']: return
        if not message.channel.category: return
        if not message.channel.category.id in self.allowed: return

        if (message.content.lower().split(" ")[0] in self.keywords) and message.mentions:
            if message.author in message.mentions:
                message.mentions.remove(message.author)
            if not message.mentions: return
            members = [member for member in message.mentions]
            for member in members:
                database.Thanks(member.id).add()
            return await message.channel.send(embed=embeds.Embeds(f"{message.author.mention} thanked " + ', '.join(member.mention for member in message.mentions)).success())

    @commands.guild_only()
    @checks.mainServer()
    @commands.command()
    async def top(self, ctx, timespan : lambda arg: arg.lower() = "alltime", page:int=1):
        spans = [
            "alltime",
            "weekly",
            "daily"
        ]

        if not timespan in spans:
            timespan = "alltime"

        pages = sorted([entry for entry in database.Thanks().col.find({})], key=lambda k:k[f"thanks_{timespan}"], reverse=True).paginate(10)

        current_page = page-1

        msg = await ctx.send(embed=discord.Embed(
            title=f"Thanking Leaderboard | {timespan.capitalize()}",
            description='\n'.join(f"**#{pages[current_page].index(i)+1}** ‣ {ctx.guild.get_member(i['_id']).mention} **with** {i[f'thanks_{timespan}']} thanks" for i in pages[current_page]),
            color=discord.Color.purple()
        )
        .set_thumbnail(url=ctx.guild.icon_url_as(static_format="png"))
        .set_footer(text=f"Page {current_page+1}/{len(pages)}"))

        emojis = ["⏪","⬅️","➡️", "⏩"]

        for emoji in emojis: await msg.add_reaction(emoji)

        while True:
            try:
                reaction, user = await self.bot.wait_for(
                    'reaction_add',
                    timeout=60,
                    check=lambda r, u: r.emoji in emojis and r.message.id == msg.id and u.id == ctx.author.id
                )
            except asyncio.TimeoutError:
                return await msg.clear_reactions()

            if reaction.emoji == emojis[0]:
                current_page = 0
            elif reaction.emoji == emojis[-1]:
                current_page = len(pages)-1
            elif reaction.emoji == emojis[1]:
                if not current_page == 0: current_page -= 1
            else:
                if not current_page == len(pages)-1: current_page += 1
            
            try:
                await msg.remove_reaction(reaction.emoji, ctx.author)
            except: pass

            await ctx.send(embed=discord.Embed(
            title=f"Thanking Leaderboard | {timespan.capitalize()}",
            description='\n'.join(f"**#{pages[current_page].index(i)+1}** ‣ {ctx.guild.get_member(i['_id']).mention} **with** {i[f'thanks_{timespan}']} thanks" for i in pages[current_page]),
            color=discord.Color.purple()
        )
        .set_thumbnail(url=ctx.guild.icon_url_as(static_format="png"))
        .set_footer(text=f"Page {current_page+1}/{len(pages)}"))

def setup(bot):
    bot.add_cog(Thanking(bot))