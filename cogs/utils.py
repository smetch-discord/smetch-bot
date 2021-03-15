import discord
from discord.ext import commands

class Utils(commands.Cog):
  def __init__(self, bot):
        self.bot = bot
        self.main_color = 0x8647a0
  
  @commands.command(name='acd')
  async def academic_dishonesty(self, ctx):
    return await ctx.send(embed=discord.Embed(
      title="__Academic Dishonesty__",
      color=self.main_color,
      description="""**Cheating and other forms of academic dishonesty are strictly forbidden and will result in a mute/ban
For more info go to [here](https://www.berkeleycitycollege.edu/wp/de/what-is-academic-dishonesty/)**"""))

  @commands.command(aliases=["justask"])
  async def just_ask(self, ctx):
    return await ctx.send(embed=discord.Embed(
      title='__Don\'t ask to ask__',
      color=self.main_color,
      description='**Don\'t ask if you can ask a question.\n[Just ask](https://justasktoask.com)**'))

  @commands.command()
  async def multipost(self, ctx):
    return await ctx.send(embed=discord.Embed(
      title='__Post in one channel__',
      color=self.main_color,
      description='**Please don\'t post in multiple channels\nRefer to #how-to-ask for more information\nSomeone will help you eventually!**'))

  @commands.command()
  async def ping(self, ctx):
    return await ctx.send(embed=discord.Embed(
      title = '__PONG__',
      color=self.main_color,
      description = f'Response in {round(self.bot.latency * 1000)} ms <@{ctx.author.id}>'))

  @commands.command()
  async def remind(self, ctx):
    return await ctx.send(embed=discord.Embed(title='__Don\'t forget to thank our volunteer helpers!__', color=0x8647a0, description='**A thank you to our helpers after you\'re done asking your question would be greatly appreciated!**'))

  @commands.command()
  async def support(self, ctx):
    return await ctx.send(embed=discord.Embed(
      title='__Support Us!__',
      color=0xf81ba0,
      description="""To keep our server growing and have a bigger helping community, there are 2 ways to help us out! ✨
<a:star_blue:809072328192688159> Vote on Top.GG.
Vote for us on: [Top.gg](https://top.gg/servers/806922773607874590).
Voting is every 12 hours! You also get a special voter role when you do it.
<a:star_blue:809072328192688159> Bump our Server on Disboard.
Go to #bot-commands and type !d bump! If nobody has bumped the server yet, you can do the command.""")
      .add_field(name="To those considering being boosters 💫", value="""<a:star_blue:809072328192688159> You will be given the <@&811577160522530837> role and your name will be put up in the online members list, making you stand out on the server chats.
<a:star_blue:809072328192688159> You can choose to change your name colour.
<a:star_blue:809072328192688159> You will be given a shoutout at the shoutouts channel as thanks for your support for the server.
<a:star_blue:809072328192688159> You may add 2 Emojis of your choice to be added for use on this server (if slots are available).
<a:star_blue:809072328192688159> You get access to a private channel for Boosters.
<a:star_blue:809072328192688159> You will have priority in getting a tutor (feature to be implemented soon).
<a:star_blue:809072328192688159> More Perks to be added!"""))
  
def setup(bot):
    bot.add_cog(Utils(bot))