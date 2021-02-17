import github, os, asyncio, discord
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
repo = (github.Github(os.environ.get('GITHUB_TOKEN'))).get_organization('smetch-discord').get_repo('smetch-bot')

class github(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='issue')
  async def issue(self, ctx, method, issue_close_param = None):
    if method.lower() == 'new':
      confirmation = await ctx.send(embed=discord.Embed(color=0xaaffff, description=f'<@{ctx.author.id}> please react to this message if you want to make an issue with SMETCH Bot.\n**Please remember to check if your issue has already been found by using `!issues`.**\n**Creating spam or unnecessary issues is a bannable offence**'))
      await confirmation.add_reaction('✅')
      try:
        await self.bot.wait_for('reaction_add', check=(lambda x, y: (str(x.emoji) == '✅') and (y.id == ctx.author.id)), timeout=45)
        try:
          intro_dm = await ctx.author.send('**Thank you for taking the time to report an issue**\nWe greatly appreciate it!\nPlease could you enter a short title for the issue:')
          dm_channel_id = intro_dm.channel.id
          title = (await self.bot.wait_for('message', check=(lambda x: x.author.id == ctx.author.id and x.channel.id == dm_channel_id), timeout=600)).content
          title += f' by {ctx.author.name}#{ctx.author.discriminator}'
        except discord.Forbidden:
          await confirmation.edit(content=f'Failed to DM <@{ctx.author.id}>. Please make sure you have DMs open.', embed=None)
          return
        prompts, body = ['Please give a clear and concise description about the issue', 'Please enter a description on how to reproduce the bug if possible. Else enter None', 'What should happen if the feature was working correctly?'], ''
        try:
          for prompt in prompts:
            await ctx.author.send(prompt) 
            body += (await self.bot.wait_for('message', check=(lambda x: x.author.id == ctx.author.id and x.channel.id == dm_channel_id), timeout=600)).content
            body += '\n'
          repo.create_issue(title, body)
          await ctx.author.send('**Issue has been created. Thank you.**')
          return
        except asyncio.TimeoutError:
          await ctx.author.send('Issue creation timed out')
          return
      except asyncio.TimeoutError:
        await confirmation.delete()
        return

    elif method.lower() == 'close':
      if issue_close_param == None:
        await ctx.send('Please provide the number of the issue you would like to close')
      issue = repo.get_issue(int(issue_close_param))
      if not(f'{ctx.author.name}#{ctx.author.discriminator}' == issue.title.split()[-1] or ctx.author.id == 805903287723229294):
        await ctx.send(embed=discord.Embed(color=0xaaffff, description=f'<@{ctx.author.id}>, you don\'t have the power to do this'))
        return
      confirmation = await ctx.send(embed=discord.Embed(color=0xaaffff, description=f'Would you like to close this issue: {issue.title}?'))
      await confirmation.add_reaction('✅')
      try:
        await self.bot.wait_for('reaction_add', check=(lambda x, y: str(x.emoji) == '✅' and (y.id == ctx.author.id)), timeout=45)
        issue.edit(state='closed')
        await confirmation.edit(embed=discord.Embed(color=0xaaffff, description=f'Issue: {issue.title} has been closed'))
        await confirmation.clear_reactions()
        return
      except asyncio.TimeoutError:
        await ctx.delete()
        return
      
    elif method.lower() == 'list':
      issues = ''
      if repo.get_issues().totalCount == 0:
        ctx.send(embed=discord.Embed(title='There are currently no issues on SMETCH Bot'))
        return
      for issue in repo.get_issues():
        issues += f'**{" ".join(issue.title.split()[:-2])}**\nIssue created by **{issue.title.split("#")[-2].split()[-1]}#{issue.title.split("#") [-1]}** on **{issue.created_at.strftime("%d/%m/%Y")}**\nFor more info on this issue click [here]({issue.html_url})\n*This is issue #{issue.number}*\n\n'
      await ctx.send(embed=discord.Embed(title='Current issues on SMETCH Bot', description=issues, color=0xaaffff))
    return

  @commands.command(name='version')
  async def version(self, ctx):
    await ctx.send(embed=discord.Embed(description=f'I am currently operating on {repo.get_releases()[0].tag_name}'))
    return



