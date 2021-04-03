from discord.ext import commands
from constants import BOT_TOKEN

bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    print('Bot is running')


@bot.command(name='test')
async def test(ctx):
    print('This is a test command')

bot.run(BOT_TOKEN)
