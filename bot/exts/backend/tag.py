
from pathlib import Path
from discord import Embed


def load_util_files():
    resource_folder = Path('.', 'bot', 'resources')
    util_files = list(resource_folder.glob('*.md'))
    util_files = {file.name[:-3]: open(file).read() for file in util_files}
    return util_files


def markdown_to_embed(markdown: str):
    embed = Embed()
    title = markdown.split('\n')[0].strip('*')
    embed.title = title
    content = '\n'.join(markdown.split('\n')[1:])
    embed.description = content
    return embed
