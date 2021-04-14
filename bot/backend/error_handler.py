from discord.ext.commands import Cog, Bot, Context, errors
import difflib


class ErrorHandler(Cog):
    '''
    Generic handling of any errors thrown by a command.

    If the error was that the user used a command that doesn't exist:
    1. Try and get a tag from the `resources/tags` folder,
    2. Suggest a similarly spelled command
    '''

    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        return

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: errors.CommandError) -> None:
        '''
        Listen for errors thrown by commands in order to handle them accordingly
        '''
        if isinstance(error, errors.CommandNotFound):
            # Attempt to get a tag
            await self.get_tag(ctx)
        else:
            raise error
        return

    async def get_tag(self, ctx: Context):
        '''
        Attempt to get a tag from the `resources/tags` folder.
        Then adds the markdown to an `Embed` object with:
        - Title: name of the tag's markdown file
        - Description: content of the tag's markdown file
        '''
        await self.suggest_similar_command(ctx, ctx.invoked_with)
        return

    async def suggest_similar_command(self, ctx: Context, command_name: str) -> None:
        '''
        Suggests a command spelt similarly to whatever the user typed using the `difflib` library
        '''
        raw_commands: list[str] = []
        # Append all of the bot's commands' names to the list `raw_commands`
        for command in self.bot.walk_commands():
            # Make sure that the command is not hidden and therefore shouldn't be suggested
            if not command.hidden:
                raw_commands.append(command.name)

        # Check if there are any command names that closely match what the user had written
        if similar_command_data := difflib.get_close_matches(command_name, raw_commands, 1):
            # Get first element because `difflib.get_close_matches()` returns a list
            similar_command_name = similar_command_data[0]
            misspelled_content = ctx.message.content
            # Instead of returning just the command, make sure to include all the other contents
            # of the message as there could be arguments
            description = f'{misspelled_content.replace(command_name, similar_command_name, 1)}'
            await ctx.send(f'**Did you mean** `{description}` **?**')
        return


def setup(bot: Bot) -> None:
    bot.add_cog(ErrorHandler(bot))
