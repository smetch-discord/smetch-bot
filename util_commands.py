import discord

async def academic_dishonesty(message):
  embed = discord.Embed()
  embed.title = '__Academic Dishonesty__'
  embed.color = 0x8647a0
  embed.description = '**Cheating and other forms of academic dishonesty are strictly forbidden and will result in a mute/ban\nFor more info go to [here](https://www.berkeleycitycollege.edu/wp/de/what-is-academic-dishonesty/)**'
  await message.channel.send(embed=embed)

async def justask(message):
  embed = discord.Embed()
  embed.title = '__Don\'t ask to ask__'
  embed.color = 0x8647a0
  embed.description = '**Don\'t ask if you can ask a question.\n[Just ask](https://justasktoask.com)**'
  await message.channel.send(embed=embed)

async def multipost(message):
  embed = discord.Embed()
  embed.title = '__Post in one channel__'
  embed.color = 0x8647a0
  embed.description = '**Please don\'t post in multiple channels\nRefer to #how-to-ask for more information\nSomeone will help you eventually!**'
  await message.channel.send(embed=embed)

async def ping(message, client):
  embed = discord.Embed()
  embed.color = 0x8647a0
  embed.title = '__PONG__'
  embed.description = 'Response in ' + str(round(client.latency * 1000)) + 'ms <@' + str(message.author.id) + '>'
  await message.channel.send(embed=embed)

async def pong(message, client):
  embed = discord.Embed()
  embed.color = 0x8647a0
  embed.title = '__PING__'
  embed.description = 'Response in ' + str(round(client.latency * 1000)) + 'ms <@' + str(message.author.id) + '>'
  await message.channel.send(embed=embed)

async def pingpong(message):
  embed = discord.Embed()
  embed.color = 0x8647a0
  embed.title = '**Play a game of Ping Pong**'
  embed.url = 'https://pong-2.com/'
  embed.set_footer(text='Courtesy of Slurp#2718')
  await message.channel.send(embed=embed)
  
async def advanced_math(message):
  staff_role = message.guild.get_role( 808099724904759297)
  role = message.guild.get_role(809184355485351966)
  if staff_role not in message.author.roles:
    await message.channel.send('We don\'t trust you enough to use this command yet')
    return
  else:
    if len(message.mentions) == 0:
      return
    else:
      for person in message.mentions:
        await person.add_roles(role)
        await message.channel.send('Advanced math role given to <@' + str(person.id) + '>')