from discord.ext.commands import Bot, Context
from discord import Embed
from datetime import datetime

bot: Bot = Bot('lol ', help_command=None)


@bot.command()
async def ping(ctx: Context):
    bot_ping = (datetime.utcnow() - ctx.message.created_at).total_seconds() * 1000
    bot_ping: str = f'{bot_ping:.3f} ms'
    discord_ping: str = f'{bot.latency * 1000:.3f} ms'

    embed: Embed = Embed(
        title='Ping!'
    )

    for description, latency in zip(['Command Processing Time', 'Discord API Latency'], [bot_ping, discord_ping]):
        embed.add_field(
            name=description,
            value=latency,
            inline=False
        )

    await ctx.send(embed=embed)
    return

bot.run('ODA4MjgyNzEyMzY3NTYyNzYy.YCER7w.bRD1xhdUtJWdcI5TYhJ9CkVoJ7Q')
