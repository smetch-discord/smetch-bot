from discord.ext.commands import Bot, Cog, Context, command
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
        print('This cog was loaded')
        self.bot: Bot = bot
        return

    @command
    async def test(self, ctx: Context):
        await ctx.send('Test returned')

    @command(description='Bans a user')
    @can_ban()
    async def ban(self, ctx: Context, users: Greedy[Member], reason: str = 'None was provided'):
        for user in users:
            await ctx.guild.ban(
                user=user,
                reason=f'Banned by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}'
            )
