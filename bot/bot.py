from discord.ext.commands import Bot, Context
from discord import Embed
from datetime import datetime
from yaml import safe_load

bot: Bot = Bot('lol ', help_command=None)


@bot.command()
async def ping(ctx: Context):
    bot_ping = (datetime.utcnow() - ctx.message.created_at).total_seconds() * 1000
    bot_ping: str = f'{bot_ping:.3f} ms'
    discord_ping: str = f'{bot.latency * 1000:.3f} ms'

    embed: Embed = Embed(
        title='Ping!',
        colour=0x00d166
    )

    for description, latency in zip(['Command Processing Time', 'Discord API Latency'], [bot_ping, discord_ping]):
        embed.add_field(
            name=description,
            value=latency,
            inline=False
        )

    await ctx.send(embed=embed)
    return


@bot.command()
async def server(ctx: Context):
    guild = ctx.message.guild
    embed = Embed(
        title=guild.name,
        description='SMETCH is a community that helps those in need!',
        colour=0x00d166
    )

    embed.set_thumbnail(
        url=guild.icon_url
    )

    embed.add_field(
        name='Server was created on:',
        value=guild.created_at.strftime('%d %B %Y'),
        inline=False
    )

    embed.add_field(
        name='Member count:',
        value=guild.member_count,
        inline=False
    )

    embed.add_field(
        name='Current owner:',
        value=f'<@{guild.owner_id}>'
    )

    embed.add_field(
        name='Current boosts:',
        value=guild.premium_subscription_count
    )

    await ctx.send(embed=embed)

config = safe_load(open('config.yml'))

bot.run(config['bot-token'])
