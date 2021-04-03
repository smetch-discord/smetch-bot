from constants import BOT_TOKEN
from discord.ext import commands
import logging
from log_setup import log_setup
log_setup()


# Filter out info to include warnings and above in order to not clog bot.log
discord_log = logging.getLogger('discord')
discord_log.setLevel(logging.WARNING)
asyncio_log = logging.getLogger('asyncio')
asyncio_log.setLevel(logging.WARNING)

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Initialise bot
bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    logger.info('Bot is running')


@bot.command(name='test')
async def test(ctx):
    await ctx.send('This is a test command')

# Run the bot
bot.run(BOT_TOKEN)
