from constants import get_constants, Constants
from discord.ext.commands import Bot
from discord import Intents
import logging
from log_setup import log_setup

log_setup()

# Filter out info to include warnings and above in order to not clog bot.log
discord_log = logging.getLogger('discord')
discord_log.setLevel(logging.WARNING)
asyncio_log = logging.getLogger('asyncio')
asyncio_log.setLevel(logging.WARNING)

# Set up logging
logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)

# Set intents
intents = Intents.default()

# Initialise bot
bot = Bot(command_prefix='s!', intents=intents)

constants: Constants = get_constants(bot)

bot.load_extension('exts.moderation.moderation')


@bot.event
async def on_ready():
    logger.info('Bot is running')

# Run the bot
bot.run(constants.bot.token)
