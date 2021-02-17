import discord
from discord.ext import commands

class util_commands(commands.Cog):

  def __init__(self, bot):
        self.bot = bot
  
  @commands.command(name='acd')
  async def academic_dishonesty(self, ctx):
    await ctx.send(embed=discord.Embed(title='__Academic Dishonesty__', color=0x8647a0, description='**Cheating and other forms of academic dishonesty are strictly forbidden and will result in a mute/ban\nFor more info go to [here](https://www.berkeleycitycollege.edu/wp/de/what-is-academic-dishonesty/)**'))
    return

  @commands.command(name='justask')
  async def just_ask(self, ctx):
    await ctx.send(embed=discord.Embed(title='__Don\'t ask to ask__', color=0x8647a0, description='**Don\'t ask if you can ask a question.\n[Just ask](https://justasktoask.com)**'))
    return

  @commands.command(name='multipost')
  async def multipost(self, ctx):
    await ctx.send(embed=discord.Embed(title='__Post in one channel__', color=0x8647a0, description='**Please don\'t post in multiple channels\nRefer to #how-to-ask for more information\nSomeone will help you eventually!**'))

  @commands.command(name='ping')
  async def ping(self, ctx):
    await ctx.send(embed=discord.Embed(title = '__PONG__', color=0x8647a0, description = f'Response in {round(self.bot.latency * 1000)} ms <@{ctx.author.id}>'))

  @commands.command(name='remind')
  async def thank(self, ctx):
    await ctx.send(embed=discord.Embed(title='__Don\'t forget to thank our volunteer helpers!__', color=0x8647a0, description='**A thank you to our helpers after you\'re done asking your question would be greatly appreciated!**'))

  @commands.command(name='support')
  async def support(self, ctx):
    await ctx.send(embed=discord.Embed(title='__Support Us!__', color=0xf81ba0, description='To keep our server growing and have a bigger helping community, there are 2 ways to help us out! ✨\n<a:star_blue:809072328192688159> Vote on Top.GG.\nVote for us on: (https://top.gg/servers/806922773607874590).\nVoting is every 12 hours! You also get a special voter role when you do it.\n<a:star_blue:809072328192688159> Bump our Server on Disboard.\nGo to #bot-commands and type !d bump! If nobody has bumped the server yet, you can do the command.').add_field(name='To those considering being boosters 💫', value='<a:star_blue:809072328192688159> You will be given the @Booster role and your name will be put up in the online members list, making you stand out on the server chats.\n<a:star_blue:809072328192688159> You can choose to change your name colour.\n<a:star_blue:809072328192688159> You will be given a shoutout at the shoutouts channel as thanks for your support for the server.\n<a:star_blue:809072328192688159> You may add 2 Emojis of your choice to be added for use on this server (if slots are available).\n<a:star_blue:809072328192688159> You get access to a private channel for Boosters.\n<a:star_blue:809072328192688159> You will have priority in getting a tutor (feature to be implemented soon).\n<a:star_blue:809072328192688159> More Perks to be added!'))
  
  @commands.command(name='advanced')
  async def advanced(self, ctx, members: commands.Greedy[discord.Member]):
    staff_role, advanced_math_role = ctx.guild.get_role(808099724904759297), ctx.guild.get_role(809184355485351966)
    if staff_role not in ctx.author.roles:
      await ctx.send('You do not have the power to execute this command yet')
      return
    for member in members:
      await member.add_roles(advanced_math_role)
      await ctx.send(f'Advanced math role has been given to <@{member.id}>')
    return
