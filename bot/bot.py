from constants import get_constants
from discord.ext import commands
import logging
from log_setup import log_setup
from exts.backend.error_handler import ErrorHandler

log_setup()

# Filter out info to include warnings and above in order to not clog bot.log
asyncio_log = logging.getLogger('asyncio')
asyncio_log.setLevel(logging.WARNING)

# Set up logging
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# Initialise bot
bot = commands.Bot(command_prefix='s!')

constants = get_constants(bot)


@bot.event
async def on_ready():
    logger.info('Bot is running')

bot.add_cog(ErrorHandler(bot))

# Run the bot
bot.run(constants.bot.token)
