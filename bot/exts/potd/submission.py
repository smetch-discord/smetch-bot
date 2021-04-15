from discord.ext.commands import Cog, Bot
from discord import Message, DMChannel


class POTDSubmissions(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot

    @Cog.listener('on_message')
    async def problem_submission(self, message: Message):
        # Exit early if the message was not sent in a DM as there is no point in taking further action
        if not isinstance(message.channel, DMChannel):
            return
        command: str = message.content

        # Exit early if they haven't used the submit command
        if not command.startswith('!submit'):
            return
