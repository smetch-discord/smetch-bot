
from pathlib import Path
from discord import Embed
from discord.ext.commands import Cog, Command


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


def create_command(name: str, embed: Embed):

    async def command_template(ctx):
        await ctx.send(embed=embed)

    return Command(
        command_template,
        name=name,
        cog=Utility
    )


class Utility(Cog):

    def __init__(self, bot):
        self.bot = bot
        util_commands_dict = load_util_files()
        for command_name in util_commands_dict:
            command_embed = markdown_to_embed(util_commands_dict[command_name])
            command = create_command(command_name, command_embed)
            self.bot.add_command(command)
        print(self.get_commands())
