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

async def support(message):
  embed = discord.Embed()
  embed.title = 'Support us!'
  embed.color = 0xf81ba0
  embed.description = 'To keep our server growing and have a bigger helping community, there are 2 ways to help us out! ✨\n<a:star_blue:809072328192688159> Vote on Top.GG.\nVote for us on: (https://top.gg/servers/806922773607874590).\nVoting is every 12 hours! You also get a special voter role when you do it.\n<a:star_blue:809072328192688159> Bump our Server on Disboard.\nGo to #bot-commands and type !d bump! If nobody has bumped the server yet, you can do the command.'
  await message.channel.send(embed=embed)
  embed = discord.Embed()
  embed.title = 'To those considering being boosters! 💫'
  embed.color = 0xf81ba0
  embed.description = ' <a:star_blue:809072328192688159> You will be given the @Booster role and your name will be put up in the online members list, making you stand out on the server chats.\n<a:star_blue:809072328192688159> You can choose to change your name colour.\n<a:star_blue:809072328192688159> You will be given a shoutout at the shoutouts channel as thanks for your support for the server.\n<a:star_blue:809072328192688159> You may add 2 Emojis of your choice to be added for use on this server (if slots are available).\n<a:star_blue:809072328192688159> You get access to a private channel for Boosters.\n<a:star_blue:809072328192688159> You will have priority in getting a tutor (feature to be implemented soon).\n<a:star_blue:809072328192688159> More Perks to be added!'
  await message.channel.send(embed=embed)
  embed=discord.Embed()
  embed.color = 0xf81ba0
  embed.title = 'THANK YOU'
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