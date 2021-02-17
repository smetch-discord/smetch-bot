import discord
import asyncio

helper_channels = (807226238896570429, 807226384246243348, 807226722491039754, 807226820113989682, 807226846897897482, 807226904566038578, 807227165363273749, 807227353272025098, 807227320788189204, 807227224445026335, 807227660429557781, 807227701890514975, 807227761298374686, 808948498049138710, 807228003616030720, 807228044397117441, 807228325562548284, 807228024214913074, 807228361373908992, 807306277033082900)

async def ping_helper(message, role, client):
  embed = discord.Embed()
  embed.description = f'**The Helper Role will be pinged in 45 seconds. React with ❎ to cancel the ping.**\n<@{message.author.id}> needs <@&{role}>'
  ping_message = await message.channel.send(embed=embed)
  await ping_message.add_reaction('❎')

  def check(reaction, user):
    return (str(reaction.emoji) == '❎') and (user.id == message.author.id)

  try:
    await client.wait_for('reaction_add', check=check, timeout=45)
    await ping_message.clear_reactions()
    await ping_message.delete()
    return
  except asyncio.TimeoutError:
    await ping_message.edit(content=f'<@{message.author.id}> needs <@&{role}>', embed=None)
    await ping_message.clear_reactions()
    return