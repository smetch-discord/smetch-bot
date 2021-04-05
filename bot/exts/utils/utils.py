
from pathlib import Path
from discord import Embed
from discord.ext.commands import Cog
from bot.constants import constants


def load_util_files():
    resource_folder = Path('.', 'bot', 'resources')
    util_files = list(resource_folder.glob('*.md'))
    util_files = list(util_files.map(lambda file: open(file, 'r').read()))
    return util_files


def markdown_to_embed(markdown: str):
    embed = Embed
    title = markdown.split('\n')[0].strip('*')
    embed.title = title
    content = '\n'.join(markdown.split('\n')[1:])
    embed.description = content
    embed.color = constants.color.white
    return embed


def create_command(embed: Embed):
    pass


class Utility(Cog):

    def __init__(self):
        pass
