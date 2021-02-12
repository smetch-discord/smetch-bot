import discord
import keep_alive
import util_commands
import thank
import helpcmd
import mathcmds
import helperping
import gitcmds
import os
import pymongo
import datetime
from discord.ext import tasks
from dotenv import load_dotenv, find_dotenv

client = discord.Client()

client.current = datetime.datetime.now().date().day
client.week_check = datetime.date.today().isocalendar()[1]

@tasks.loop(seconds=1)
async def resetter(client):
  if datetime.datetime.now().date().day != client.current:
    db = pymongo.MongoClient(os.environ.get('MONGO_URI')).SMETCH
    db.data.update_many({}, {'$set': {'daily_thanks': 0}})
    if datetime.date.today().isocalendar()[1] != client.week_check:
      db.data.update_many({}, {'$set': {'daily_thanks': 0}})
      client.week_check = datetime.date.today().isocalendar()[1]
  client.current = datetime.datetime.now().date().day

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='SMETCH Vibes'))
  print('We have logged in as {0.user}'.format(client))
  resetter.start(client)

@client.event
async def on_member_join(member):
  # student = member.guild.get_role(806922773649555470)
  embed = discord.Embed()
  print('Some kid joined')
  embed.title = 'Welcome to the SMETCH Server'
  embed.description = '**Introduction**\nThis server is for all students willing to learn and teach others! Our goal for this server is to provide everybody with the help they need: be it with schoolwork or something out of school. Members of our server can provide tips and advices on fields of study and productivity. The SMETCH Server is managed and run by your favorite Smetchers that are all ready to help out whenever they can!\n<a:star_blue:809072328192688159> What Can This Server Offer to students\n✔︎ Help and advice from students studying the same subject as you!\n✔︎ Daily Challenges to motivate you with your studies︎\n✔ Tips and Tutorials on interesting topics︎\n✔ Relax and Socialize with other members about different topics!✔︎ And so much more!\n<a:star_blue:809072328192688159> **Learn the rules of the server**\n[Full rules](https://trello.com/b/xCCEP4zw/smetch-maths-study-help-rules)\n\n**Type continue to proceed**'
  embed.set_thumbnail(url='https://cdn.discordapp.com/icons/806922773607874590/890935573076ea1ea4dd706d5859a532.png?size=4096')
  await member.send(embed=embed)
  # await member.add_roles(student)


@client.event
async def on_message(message):

    if message.author == client.user:
      return
    
    if message.content.startswith('-'):
      message.content = message.content.lower()
      if message.content.startswith('-math'):
        if message.content == '-math linear equations' or message.content == '-math linear equation':
          await mathcmds.linear_equations(message)
        elif message.content == '-math quadratic equations' or message.content == '-math quadratic equation':
          await mathcmds.quadratic_equations(message)
        elif message.content == '-math binomial':
          await mathcmds.binomial(message)
        elif message.content == '-math binomial theorem':
          await mathcmds.binomial_theorem(message)
        elif message.content == '-math system' or message.content == '-math systems':
          await mathcmds.systems(message)    
        elif message.content == '-math system substitution' or message.content == '-math systems substitution':
          await mathcmds.system_substitution(message) 

    if message.content.startswith('!'):
      message.content = message.content.lower()
      if message.content == '!acd':
        await util_commands.academic_dishonesty(message)

      elif message.content == '!justask':
        await util_commands.justask(message)

      elif message.content == '!multipost':
        await util_commands.multipost(message)
      
      elif message.content == '!ping':
        await util_commands.ping(message, client)
      
      elif message.content == '!pong':
        await util_commands.pong(message, client)

      elif message.content == '!pingpong':
        await util_commands.pingpong(message)
      
      elif message.content == '!help':
        await helpcmd.help(message, client)

      elif message.content == '!support':
        await util_commands.support(message)

      elif message.content == '!smetch':
        await message.channel.send('Smetch = S + M + Etch\nH = Etch\nSmetch = S + M + H\nSmetch = SMH')

      elif message.content.startswith('!check'):
        await thank.check(message)

      elif message.content == '!issues':
        await gitcmds.issues(message)

      elif message.content.startswith('!issue'):
        if message.content == '!issue':
          await gitcmds.issue(message, client)
        elif message.content.startswith('!issue close'):
          pass

      elif message.content.startswith('!top'):
        if message.content == '!top alltime':
          await thank.top(message, 'alltime')
        if message.content == '!top weekly':
          await thank.top(message, 'weekly')
        if message.content == '!top daily':
          await thank.top(message, 'daily')

    if message.content.lower().startswith('advanced math'):
      await util_commands.advanced_math(message)

    helper_roles = [809358621091692566]

    for role in message.role_mentions:
      if role.id in helper_roles:
        await helperping.ping_helper(message, role, client)
    
    thank_words = ['thank', 'thanks', 'thx', 'thnx', 'tanks', 'tanq', 'thank u', 'tank u', 'ty', 'tysm', 'thank you so much', 'thank u so much', 'thank u sm', 'thanks sm', 'danke', 'merci', 'mrc', 'mrc bcp', 'mrc beaucoup', 'danke sehr', 'danke schön', 'vielen danke', 'tank', 'tanqs', 'gracias', 'mucho gracias', 'tak', 'mange tak']

    for tywords in thank_words:
      for words in message.content.lower().replace('*', '').replace('_','').replace('~', '').split():
        if words == tywords and not message.author.bot:
          await thank.thank(message, client)
          break

    else:
      return

keep_alive.keep_alive()

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

client.run(TOKEN)