import logging
from discord.errors import NotFound
from discord.ext.commands import Cog, Bot
from discord import Message, Role, Invite
from discord.utils import get
from re import findall

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class Detector(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @Cog.listener('on_message')
    async def spam_ping_detection(self, message: Message) -> None:
        """
        Listens for any messages containing >= 5 pings.
        If the message contains >= 5 pings, checks if the message sender was a staff member.
        Returns if the member was a staff member, as they may have legitimate reason for pinging
        """
        user_mentions: list[int] = message.raw_mentions
        role_mentions: list[int] = message.raw_role_mentions
        mentions: list[int] = user_mentions + role_mentions
        number_of_mentions: int = len(mentions)

        # Exit early if there are less than 5 pings in the message
        if number_of_mentions <= 4:
            return

        log.warning("Message with more than 5 pings detected.\n"
                    "Message info:\n"
                    f"Message ID: {message.id}\n"
                    f"Channel ID: {message.channel.id}\n"
                    f"Message Author ID: {message.author.id}")

        # Make sure that the person isn't a staff member
        staff_role: Role = get(message.guild.roles, id=808099724904759297)
        is_staff: bool = staff_role in message.author.roles

        if not is_staff:
            await message.delete()
            await message.channel.send('Spam pings detected')
        else:
            log.info("Message was sent by staff member so no action was taken")
        return

    @Cog.listener('on_message')
    async def invite_detection(self, message: Message) -> None:
        """
        Checks for any potential invite links sent in the chat that don't belong to SMETCH.
        If the message contains an invite link, delete the message and send a prompt in the respective channel.
        """
        regex: str = 'discord.gg/.*'
        invites: list[str] = findall(regex, message.content.lower())
        contains_invites: bool = len(invites) > 0

        # Check if the user is a staff member
        staff_role: Role = get(message.guild.roles, id=808099724904759297)
        is_staff: bool = staff_role in message.author.roles

        # Exit early if the message doesn't contain any invites or the user is staff
        if is_staff or not contains_invites:
            return

        offending_invites: list[str] = []

        # Append valid invites that don't belong to SMETCH to `offending_invites`
        for invite in invites:
            try:
                invite_check: Invite = await self.bot.fetch_invite(invite)
                if invite_check.guild != message.guild:
                    offending_invites.append(invite)
            except NotFound:
                continue

        # If there are any invites in `offending_invites`, delete the message
        if len(offending_invites) > 0:
            await message.delete()

        return
