import discord
import keep_alive
from util_commands import util_commands
from thank import thank
import helpcmd
import mathcmds
import helperping
from gitcmds import Github
import os
import pymongo
import datetime
from moderation import Moderation
from discord.ext import tasks, commands
from dotenv import load_dotenv, find_dotenv

bot = commands.AutoShardedBot(command_prefix='!')

db = pymongo.MongoClient(os.environ.get('MONGO_URI')).SMETCH
bot.current = datetime.datetime.now().date().day
bot.week_check = datetime.date.today().isocalendar()[1]

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
    
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='SMETCH Vibes'))
  print('Logged in')
  resetter.start(bot)

keep_alive.keep_alive()

load_dotenv(find_dotenv())

TOKEN = os.environ.get('TOKEN')

print(TOKEN)

bot.add_cog(util_commands(bot))
bot.add_cog(Github(bot))
bot.add_cog(thank(bot))
bot.add_cog(Moderation(bot))

bot.run(TOKEN)