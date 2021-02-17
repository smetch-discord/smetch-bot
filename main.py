import discord
import keep_alive
from util_commands import util_commands
from thank import thank
import helpcmd
import mathcmds
import helperping
from gitcmds import github
import os
import pymongo
import datetime
from discord.ext import tasks, commands
from dotenv import load_dotenv, find_dotenv
from multiprocessing import Process
import time

bot = commands.AutoShardedBot(command_prefix='!')

db = pymongo.MongoClient(os.environ.get('MONGO_URI')).SMETCH
bot.current = datetime.datetime.now().date().day
bot.week_check = datetime.date.today().isocalendar()[1]

# TODO: store this in the db later lol
# bot.latest_daily_update = time.time()

# instead of this, set something on init
@tasks.loop(seconds=1)
async def resetter(bot):
  # sounds like a really bad idea right?
  if datetime.datetime.now().date().day != bot.current:
    db = pymongo.MongoClient(os.environ.get('MONGO_URI')).SMETCH
    db.data.update_many({}, {'$set': {'daily_thanks': 0}})
    if datetime.date.today().isocalendar()[1] != bot.week_check:
      db.data.update_many({}, {'$set': {'daily_thanks': 0}})
      bot.week_check = datetime.date.today().isocalendar()[1]
  bot.current = datetime.datetime.now().date().day


# async def update_daily(bot):
#   # instead of storing bot.current as day, store it as a 
#   # unix timestamp integer, or even better, a mongodb date object, why is a mongodb date object better? because it looks nice on the database explorer. lol, just bc it looks nice?
#   # does bot have a .latest_daily_update attribute
#   async def do_update(update_week=False):
#     try:
#       db.data.update_many({}, {'$set': {'daily_thanks': 0}})
#       if update_week:
#         # do update week thanks here
#         db.data.update_many({}, {'$set': {'daily_thanks': 0}})
#       bot.latest_daily_update = time.time()
#     except Exception as e:
#       print("unable to update daily and weekly", e)
#       return False
#     return True
    
#   async def timeout_next():
#     try:
#       # this system will ensure that even if the bot goes down when it should
#       # update the db, it wil update the db later
#       ds = 24 * 60 * 60
#       # get closest week
#       ws = 7 * ds
#       while True:
#         #       v the normal time it should update
#         delay = (bot.latest_daily_update % ds + 1) * ds - time.time()
#         week_delay = (bot.latest_daily_update % ws + 1 - 4) * ws - time.time()
#         print(f"next daily delay is { delay / 3600 } hours, next weekly delay is { week_delay / 3600 } hours")
#         do_week = week_delay <= delay or week_delay < 0
#         time.sleep(max(delay, 0))
#         while not do_update(do_week):
#           print("something went wrong. retrying in 10 seconds")
#           time.sleep(10)
#         print("successfully updated")
#     except Exception as e:
#       print(e)

#   while True:
#     await timeout_next()
#     print("loop terminated unexpectedly. retrying")
    
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='SMETCH Vibes'))
  print('Logged in')
  resetter.start(bot)
#  Process(target=await update_daily(bot)).start()

# @bot.event
# async def on_message(message):

#     if message.author == bot.user:
#       return
    
#     if message.content.startswith('-'):
#       message.content = message.content.lower()
#       if message.content.startswith('-math'):
#         if message.content == '-math linear equations' or message.content == '-math linear equation':
#           await mathcmds.linear_equations(message)
#         elif message.content == '-math quadratic equations' or message.content == '-math quadratic equation':
#           await mathcmds.quadratic_equations(message)
#         elif message.content == '-math binomial':
#           await mathcmds.binomial(message)
#         elif message.content == '-math binomial theorem':
#           await mathcmds.binomial_theorem(message)
#         elif message.content == '-math system' or message.content == '-math systems':
#           await mathcmds.systems(message)    
#         elif message.content == '-math system substitution' or message.content == '-math systems substitution':
#           await mathcmds.system_substitution(message) 

#     if message.content.startswith('!'):
#       message.content = message.content.lower()
#       if message.content == '!acd':
#         await util_commands.academic_dishonesty(message)

#       elif message.content == '!justask':
#         await util_commands.justask(message)

#       elif message.content == '!multipost':
#         await util_commands.multipost(message)
      
#       elif message.content == '!ping':
#         await util_commands.ping(message, client)
      
#       elif message.content == '!pong':
#         await util_commands.pong(message, client)

#       elif message.content == '!pingpong':
#         await util_commands.pingpong(message)
      
#       elif message.content == '!help':
#         await helpcmd.help(message, client)

#       elif message.content == '!support':
#         await util_commands.support(message)

#       elif message.content == '!thank':
#         await util_commands.thank(message)

#       elif message.content == '!smetch':
#         await message.channel.send('Smetch = S + M + Etch\nH = Etch\nSmetch = S + M + H\nSmetch = SMH')

#       elif message.content.startswith('!check'):
#         await thank.check(message)

#       elif message.content == '!issues':
#         await gitcmds.issues(message)

#       elif message.content == '!version':
#         await gitcmds.version(message)

#       elif message.content.startswith('!issue'):
#         if message.content == '!issue':
#           await gitcmds.issue(message, client)
#         elif message.content.startswith('!issue close'):
#           await gitcmds.issue_close(message, client)

#       elif message.content.startswith('!top'):
#         if message.content == '!top alltime':
#           await thank.top(message, 'alltime')
#         if message.content == '!top weekly':
#           await thank.top(message, 'weekly')
#         if message.content == '!top daily':
#           await thank.top(message, 'daily')

#     if message.content.lower().startswith('advanced math'):
#       await util_commands.advanced_math(message)

#     helper_roles = [809948709479383040, 809956139788664902, 809956785548165122]
#     ping_roles = [809358621091692566, 809955790101151755, 809956974455947294]

#     for role in message.role_mentions:
#       if role.id in helper_roles:
#         await helperping.ping_helper(message, ping_roles
#         [helper_roles.index(role.id)], client)
    
#      jk
#     for tywords in thank_words:
#       for words in message.content.lower().replace('*', '').replace('_','').replace('~', '').split():
#         if words == tywords and not message.author.bot:
#           await thank.thank(message, client)
#           break

#     else:
#       return

keep_alive.keep_alive()

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

bot.add_cog(util_commands(bot))
bot.add_cog(github(bot))
bot.add_cog(thank(bot))

bot.run(TOKEN)