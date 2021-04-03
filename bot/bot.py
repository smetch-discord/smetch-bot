from constants import BOT_TOKEN
import logging
from discord.ext import commands

# Filter out info to include warnings and above in order to not clog bot.log
discord_log = logging.getLogger('discord')
discord_log.setLevel(logging.WARNING)
asyncio_log = logging.getLogger('asyncio')
asyncio_log.setLevel(logging.WARNING)

# Set up logging
logging.basicConfig(
    filename='bot.log',
    filemode='w',
    format='%(name)s: %(levelname)s - %(message)s',
    level=logging.DEBUG
)
log = logging.getLogger(__name__)

# Initialise bot
bot = commands.Bot(command_prefix='s!')


@bot.event
async def on_ready():
    log.info('Bot is running')


@bot.command(name='test')
async def test(ctx):
    print('This is a test command')

bot.run(BOT_TOKEN)
