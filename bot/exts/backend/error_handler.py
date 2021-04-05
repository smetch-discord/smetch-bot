import logging
import difflib
from discord import Embed
from discord.ext.commands import Cog, Context, Bot, Command, errors

from .tag import load_util_files,  markdown_to_embed


log = logging.getLogger(__name__)


class ErrorHandler(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: errors.CommandError) -> None:
        if isinstance(error, errors.CommandNotFound):
            self.try_to_send_tag(ctx)

        return

    async def try_to_send_tag(self, ctx: Context) -> None:
        '''
        Attempt to send a tag if there are any markdown files matching that tag in `bot/resources`
        If a tag exists, it sends the tag
        Else it suggests any possible commands
        '''

        tags = load_util_files()
        attemped_tag = ctx.command
        if attemped_tag in tags:
            embed_markdown = tags[attemped_tag]
            discord_embed = markdown_to_embed(embed_markdown)
            await ctx.send(embed=discord_embed)
        else:
            await self.send_command_suggestion(ctx, ctx.invoked_with)

        return

    async def send_command_suggestion(self, ctx: Context, command_name: str) -> None:

        raw_commands: list = []

        for tag in load_util_files():
            raw_commands.append((tag))

        for command in self.bot.walk_commands():
            raw_commands.append((command.name, *command.aliases))

        if similar_command_data := difflib.get_close_matches(command_name, raw_commands, 1):
            similar_command_name: str = similar_command_data[0]
            similar_command: Command = self.bot.get_command(similar_command_name)

            if not similar_command or not await similar_command.can_run(ctx):
                return

            misspelled_content: str = ctx.message.content
            embed: Embed = Embed()
            embed.set_author(name='Did you mean: ')
            embed.description = f'{misspelled_content.replace(command_name, similar_command_name, 1)}'
            await ctx.send(
                embed=embed,
                delete_after=10.0
            )

        return


def setup(bot: Bot) -> None:
    bot.add_cog(ErrorHandler(bot))
    return
