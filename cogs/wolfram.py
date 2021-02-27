import wolfram, discord, os, asyncio

commands = discord.ext.commands

app = wolfram.AsyncApp("7WYAPH-9Y7QELRQ5V")

class Wolfram(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.guild_only()
    @commands.command()
    async def ask(self, ctx, *, query):
        data = (await app.full(query))["queryresult"]["pods"]

        pods = [(i["subpods"][0]["img"]["alt"][:250], i["subpods"][0]["img"]["src"]) for i in data[1:]]

        current_page = 0

        msg = await ctx.send(embed=discord.Embed(
            title=pods[current_page][0],
            color=discord.Color.red()
        )
        .set_image(url=pods[current_page][1])
        .set_footer(text=f"Results {current_page+1}/{len(pods)}"))

        emojis = ["⏪","⬅️","⏹️","➡️", "⏩"]

        for emoji in emojis: await msg.add_reaction(emoji)

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=lambda r,u: r.message.id == msg.id and r.emoji in emojis and u.id == ctx.author.id, timeout=60)
            except asyncio.TimeoutError:
                try:
                    return await msg.clear_reactions()
                except: return

            if reaction.emoji == emojis[1]:
                if current_page != 0:
                    current_page -= 1
            elif reaction.emoji == emojis[3]:
                if current_page+1 != len(pods):
                    current_page += 1
            elif reaction.emoji == emojis[0]:
                current_page = 0
            elif reaction.emoji == emojis[-1]:
                current_page = len(pods)-1
            else:
                await msg.delete()
                return await ctx.message.add_reaction("✅")
            
            try:
                await msg.remove_reaction(reaction.emoji, ctx.author)
            except: pass

            try:
                await msg.remove_reaction(reaction.emoji, user)
            except: pass
        
            await msg.edit(embed=discord.Embed(
            title=pods[current_page][0],
            color=discord.Color.red()
            )
            .set_image(url=pods[current_page][1])
            .set_footer(text=f"Results {current_page+1}/{len(pods)}"))



def setup(bot):
    bot.add_cog(Wolfram(bot))