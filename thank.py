import discord
from discord.ext import commands
import asyncio
import pymongo
from datetime import datetime
import os
import re
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

db = pymongo.MongoClient(os.environ.get('MONGO_URI')).SMETCH

class thank(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
      
  async def thank(self, message):
    if isinstance(message.channel, discord.DMChannel): return
    if len(message.mentions) > 0:
      selected = []
      output = f'<@{message.author.id}> thanked '
      for mention in message.mentions:
        if not (mention.bot or mention.id == message.author.id):
          output += f'<@{mention.id}>'
          selected.append(mention.id)
      if output == f'<@{message.author.id}> thanked ': return
      for selectee in selected:
        db.data.update_one({"member": selectee}, {"$inc": {"daily_thanks": 1}}, upsert=True)
        db.data.update_one({"member": selectee}, {"$inc": {"weekly_thanks": 1}}, upsert=True)
        db.data.update_one({"member": selectee}, {"$inc": {"alltime_thanks": 1}}, upsert=True)
      await message.channel.send(embed=discord.Embed(description=output, color=0xaaffff))
      return
    messages = await message.channel.history(limit=50).flatten()
    users = []
    for msg in messages:
      if not msg.author.id == message.author.id or msg.author.bot:
        users.append(msg.author.id)
    a = list(set(users))
    users = a[-4:]
    description = f'**Who would you like to thank <@{message.author.id}>**\n'
    for i in range(len(users)):
      description += f'**{i + 1}**. <@{users[i]}>\n'
    confirmation = await message.channel.send(content=f'<@{message.author.id}>', embed=discord.Embed(description=description, color=0xaaffff))
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
    for i in range(len(users)):
      await confirmation.add_reaction(emojis[i])
    await confirmation.add_reaction('🗑')
    try:
      reaction, user = await self.bot.wait_for('reaction_add', check=(lambda x, y: (str(x.emoji) in emojis or str(x.emoji) == '🗑') and (y.id == message.author.id)), timeout=45)
      if str(reaction.emoji) == '🗑':
        await confirmation.delete()
        return
      elif str(reaction.emoji) == '1️⃣':
        thanked = users[0]
      elif str(reaction.emoji) == '2️⃣':
        thanked = users[1]
      elif str(reaction.emoji) == '3️⃣':
        thanked = users[2]
      elif str(reaction.emoji) == '4️⃣':
        thanked = users[3]
      db.data.update_one({"member": thanked}, {"$inc": {"daily_thanks": 1}}, upsert=True)
      db.data.update_one({"member": thanked}, {"$inc": {"weekly_thanks": 1}}, upsert=True)
      db.data.update_one({"member": thanked}, {"$inc": {"alltime_thanks": 1}}, upsert=True)
      await message.channel.send(embed=discord.Embed(description=f'<@{message.author.id}> **thanked** <@{thanked}>', color=0xaaffff))
      await confirmation.delete()
      await confirmation.clear_reactions()
      return
    except asyncio.TimeoutError:
      await confirmation.delete()
      return

  @commands.Cog.listener('on_message')
  async def on_message(self, message):
        result = re.match('(?<!\w)(?:t(?:han[qk]s*|(?:hn?|h?n)x+|y(?:[sv]m)?)|danke)(?!\w)', message.content.lower())
        if result:
          await thank.thank(self, message)
  
  @commands.command(name='check')
  async def check(self, ctx):
    checkee = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else ctx.author
    data = db.data.find({'member': checkee.id})
    weekly_thanks, daily_thanks, alltime_thanks = 0, 0, 0
    for document in data:
      weekly_thanks = document['weekly_thanks']
      alltime_thanks = document['alltime_thanks']
      daily_thanks = document['daily_thanks']
    embed = discord.Embed()
    embed.set_thumbnail(url=checkee.avatar_url)
    embed.set_author(name=checkee.display_name, icon_url=checkee.avatar_url)
    embed.description = f'<a:star_blue:809072328192688159> **Joined on**\n{datetime.strftime(checkee.joined_at, "%d/%m/%Y")}\n\n<a:star_blue:809072328192688159> **Registered on**\n{datetime.strftime(checkee.created_at, "%d/%m/%Y")}\n\n<a:star_blue:809072328192688159> **Thanks (today)**\n{daily_thanks}\n\n<a:star_blue:809072328192688159> **Thanks (Last 7 days)**\n{weekly_thanks}\n\n<a:star_blue:809072328192688159> **Thanks (all time)**\n{alltime_thanks}'
    embed.title = checkee.display_name
    embed.color = 0x8647a0
    await ctx.send(embed=embed)

  @commands.command(name='top')
  async def top(self, ctx, mode):
    if mode == 'alltime':
      thanks = list(db.data.aggregate([{'$sort': {'alltime_thanks': -1}}]))
    if mode == 'weekly':
      thanks = list(db.data.aggregate([{'$sort': {'weekly_thanks': -1}}]))
    if mode == 'daily':
      thanks = list(db.data.aggregate([{'$sort': {'daily_thanks': -1}}]))
    thanks_a = []
    for document in thanks:
      thanks_a.append(document)
    thanks = thanks_a
    embed = discord.Embed()
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/806922773607874590/890935573076ea1ea4dd706d5859a532.png?size=4096')
    description = ''
    i = 0
    for thank in thanks:
      if i == 10:
        break
      if mode == 'alltime':
        description += str(i + 1) + ' ‣ <@' + str(thank['member']) + '> **with** ' + str(thank['alltime_thanks']) + ' thanks\n'
        embed.title = 'All time leaderboard'
      if mode == 'weekly':
        description += str(i + 1) + ' ‣ <@' + str(thank['member']) + '> **with** ' + str(thank['weekly_thanks']) + ' thanks\n'
        embed.title = 'Weekly leaderboard'
      if mode == 'daily':
        description += str(i + 1) + ' ‣ <@' + str(thank['member']) + '> **with** ' + str(thank['daily_thanks']) + ' thanks\n'
        embed.title = 'Daily leaderboard'
      i += 1
    embed.description = description
    await ctx.send(embed=embed)

  @commands.command(name='setthanks')
  async def setthanks(self, ctx, member: discord.Member, number: int):
    if not(ctx.author.id == 805903287723229294):
      return
    member = member.id
    db.data.update_one({"member": member}, {"$set": {"alltime_thanks": number}}, upsert=True)
    await ctx.send('It is done')
    return
    