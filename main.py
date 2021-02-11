import discord
import keep_alive
import util_commands
import thank
import helpcmd
import mathcmds
import os
from dotenv import load_dotenv, find_dotenv

client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='SMETCH Vibes'))
    print('We have logged in as {0.user}'.format(client))

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

      elif message.content.startswith('!check'):
        await thank.check(message)

      elif message.content.startswith('!top'):
        if message.content == '!top alltime':
          await thank.top_alltime(message)

    if message.content.lower().startswith('advanced math'):
      await util_commands.advanced_math(message)
    
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