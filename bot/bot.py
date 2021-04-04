from constants import get_constants
from discord.ext import commands
import logging
from log_setup import log_setup

log_setup()
constants = get_constants()

# Filter out info to include warnings and above in order to not clog bot.log
discord_log = logging.getLogger('discord')
discord_log.setLevel(logging.WARNING)
asyncio_log = logging.getLogger('asyncio')
asyncio_log.setLevel(logging.WARNING)

# Set up logging
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# Initialise bot
bot = commands.Bot(command_prefix=constants.bot.prefix)


@bot.event
async def on_ready():
    logger.info('Bot is running')


@bot.command(name='test')
async def test(ctx):
    await ctx.send('This is a test command')

# Run the bot
bot.run(constants.bot.token)
