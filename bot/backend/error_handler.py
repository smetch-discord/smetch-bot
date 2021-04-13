from discord.ext.commands import Cog, Bot, Context, errors
import difflib


class ErrorHandler(Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: errors.CommandError):
        if isinstance(error, errors.CommandNotFound):
            await self.get_tag(ctx)

    async def get_tag(self, ctx: Context):
        await self.suggest_similar_command(ctx, ctx.invoked_with)

    async def suggest_similar_command(self, ctx: Context, command_name: str):
        raw_commands = []
        for command in self.bot.walk_commands():
            if not command.hidden:
                raw_commands.append(command.name)

        if similar_command_data := difflib.get_close_matches(command_name, raw_commands, 1):
            similar_command_name = similar_command_data[0]
            misspelled_content = ctx.message.content
            description = f'{misspelled_content.replace(command_name, similar_command_name, 1)}'
            await ctx.send(f'**Did you mean** `{description}` **?**')


def setup(bot: Bot):
    bot.add_cog(ErrorHandler(bot))
