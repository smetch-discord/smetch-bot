from discord.ext.commands import Bot, Cog, Context, command, has_permissions
from discord.ext.commands.converter import Greedy
from discord import Member, Embed
from typing import Optional

from utils.checks import can_ban

class Moderation(Cog):
    '''
    Basic moderation capabilites including:
    - Ban
    - Kick
    '''

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        print(can_ban)
        return

    @command(description='Bans a user')
    @can_ban()
    async def ban(self, ctx: Context, users: Greedy[Member], reason: str = 'None was provided', message_deletion_days: int = None):
        print('Hi')
        for user in users:
            await user.ban(
                delete_message_days=message_deletion_days,
                reason=f'Banned by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}'
            )
