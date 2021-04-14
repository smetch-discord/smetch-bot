from discord.ext.commands import Cog, Bot
from discord import Message, Role
from discord.utils import get


class Detector(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @Cog.listener('on_message')
    async def spam_ping_detection(self, message: Message) -> None:
        '''
        Listens for any messages containing >= 5 pings.
        If the message contains >= 5 pings, checks if the message sender was a staff member.
        Returns if the member was a staff member, as they may have legitimate reason for pinging
        '''
        mentions: list[int] = message.raw_mentions
        number_of_mentions: int = len(mentions)

        # Make sure that the person isn't a staff member
        staff_role: Role = get(message.guild.roles, id=808099724904759297)
        is_staff: bool = staff_role in message.author.roles

        if not is_staff and (number_of_mentions >= 5):
            # Insert disciplinary punishment
            await message.channel.send('Spam pings detected')
        return
