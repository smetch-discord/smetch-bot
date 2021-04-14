from discord.ext.commands import Bot, Cog, Context, command, has_permissions
from discord.ext.commands.converter import Greedy
from discord import Member


class Moderation(Cog):
    '''
    Basic moderation capabilites including:
    - Ban
    - Kick
    '''

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @has_permissions(ban_members=True)
    @command(description='Bans a user')
    async def ban(self, ctx: Context, users: Greedy[Member], reason: str = 'None was provided'):
        for user in users:
            if user == ctx.author:
                return
