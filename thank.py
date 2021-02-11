import discord
import asyncio
import pymongo
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

MONGO_URI = os.environ.get('MONGO_URI')

client = pymongo.MongoClient(MONGO_URI)
db = client.SMETCH

async def thank(message, client):
  if len(message.mentions) > 0:
    selected = []
    if (message.mentions[0].id == message.author.id) or (message.mentions[0].bot):
      pass
    else:
      thanked_embed_desc = '<@' + str(message.author.id) + '> **thanked** <@' + str(message.mentions[0].id) + '>'
      selected.append(message.mentions[0].id)
    if len(message.mentions) > 1:
      for i in range(len(message.mentions) - 1):
        if (message.mentions[i + 1].id == message.author.id) or (message.mentions[i + 1].bot):
          pass
        else:
          thanked_embed_desc += ' **and** <@' + str(message.mentions[i + 1].id) + '>'
        selected.append(message.mentions[i + 1].id)
    thanked_embed = discord.Embed()
    try:
      thanked_embed.description = thanked_embed_desc
    except UnboundLocalError:
      thanked_embed_desc = "Don't thank a bot or yourself <:barry:807982386285510696> <:kek:808518861182992415>"
      thanked_embed.description = thanked_embed_desc
    thanked_embed.color = 0x8647a0
    if thanked_embed_desc != "Don't thank a bot or yourself <:barry:807982386285510696> <:kek:808518861182992415>":
      thank = {
        "from": message.author.id,
        "to": selected,
        "channel": message.channel.id,
        "date": message.created_at
      }
      db.Members.update_one({"member": selected[0]}, {"$inc": {"thanks": 1}}, upsert=True)
      db.Thanks.insert_one(thank)
    await message.channel.send(embed=thanked_embed)
    return
  else:
    messages = await message.channel.history(limit=30).flatten()
    users = []
    for m in messages:
      if m.author.bot:
        continue
      else:
        users.append(m.author.id)
    users = list(set(users))
    if message.author.id in users:
      users.remove(message.author.id)
    final_users = ''
    for i in range(4):
      try:
        final_users = final_users + "**" + str(i + 1) + ".** " + "<@" + str(users[i]) + ">\n"
      except IndexError:
        break
    thanking_embed = discord.Embed()
    thanking_embed.description = "**Who would you like to thank** <@" + str(message.author.id) + ">\n" + final_users
    thanking_embed.color = 0x8647a0
    bot_message = await message.channel.send("<@" + str(message.author.id) + ">",embed=thanking_embed)
    emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣','🗑']
    for i in range(len(users)):
      if i > 4:
        break
      else:
        await bot_message.add_reaction(emojis[i])
    await bot_message.add_reaction(emojis[4])

    def check(reaction, user):
      return (str(reaction.emoji) in emojis) and (user.id == message.author.id)

    try:
      reaction = await client.wait_for('reaction_add', check=check, timeout=30)
      k = 0;
      if reaction[0].emoji == '🗑':
        await bot_message.delete()
        return
      if reaction[0].emoji == '1️⃣': 
        k = 1
      elif reaction[0].emoji == '2️⃣':
        k = 2
      elif reaction[0].emoji == '3️⃣':
        k = 3
      elif reaction[0].emoji == '4️⃣':
        k = 4
      selected = users[k - 1]
      if k!= 0:
        thank = {
          "from": message.author.id,
          "to": [selected],
          "channel": message.channel.id,
          "date": message.created_at
        }
        db.Members.update_one({"member": selected}, {"$inc": {"thanks": 1}}, upsert=True)
        db.Thanks.insert_one(thank)
      thanked_embed_desc = '<@' + str(message.author.id) + '> **thanked** <@' + str(selected) + '>\n'
      thanked_embed = discord.Embed()
      thanked_embed.description = thanked_embed_desc
      thanked_embed.color = 0x8647a0
      await bot_message.edit(content='', embed=thanked_embed)
      await bot_message.clear_reactions()
      return
    except asyncio.TimeoutError:
      await bot_message.delete()
  

async def check(message):
  user = message.author
  if len(message.mentions) == 1:
    user = message.mentions[0]
    print(user)
  alltime_thanks = db.Members.find({'member': message.author.id})
  try:
    for document in alltime_thanks:
      alltime_thanks = document['thanks']
  except:
    alltime_thanks = 0
  weekly_thanks = db.Thanks.count_documents({"to": { '$in': [user.id] }, "date": { '$gt': datetime.today() - timedelta(days=7)}})
  embed = discord.Embed()
  embed.set_thumbnail(url=user.avatar_url)
  embed.set_author(name=user.display_name, icon_url=user.avatar_url)
  embed.description = '<a:star_blue:809072328192688159> **Joined on**\n' + datetime.strftime(user.joined_at, '%d/%m/%Y') + '\n\n<a:star_blue:809072328192688159> **Registered on**\n' + datetime.strftime(user.created_at, '%d/%m/%Y') + '\n\n<a:star_blue:809072328192688159> **Thanks (Last 7 days)**\n' + str(weekly_thanks) + '\n\n<a:star_blue:809072328192688159> **Thanks (all time)**\n' + str(alltime_thanks)
  embed.title = user.display_name
  embed.color = 0x8647a0
  await message.channel.send(embed=embed)

async def top_alltime(message):
  alltime_thanks = list(db.Members.aggregate([{'$sort': {'thanks': -1}}]))
  alltime_thanks_a = []
  for document in alltime_thanks:
    alltime_thanks_a.append(document)
  alltime_thanks = alltime_thanks_a
  embed = discord.Embed()
  embed.title = 'All time leaderboard'
  embed.set_thumbnail(url='https://cdn.discordapp.com/icons/806922773607874590/890935573076ea1ea4dd706d5859a532.png?size=4096')
  description = ''
  i = 0
  for thank in alltime_thanks:
    if i == 10:
      break
    description += str(i + 1) + ' ‣ <@' + str(thank['member']) + '> **with** ' + str(thank['thanks']) + ' thanks\n'
    i += 1
  embed.description = description
  await message.channel.send(embed=embed)
