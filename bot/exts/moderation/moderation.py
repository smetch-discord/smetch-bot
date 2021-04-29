from discord.embeds import Embed
from discord.ext.commands import Bot, Cog, Context, command
from discord.ext.commands.converter import Greedy
from discord import Member
from typing import Optional

from bot.utils.checks import can_ban, can_kick


class Moderation(Cog):
    """
    Basic moderation capabilities including:
    - Ban
    - Kick
    """

    def __init__(self, bot: Bot) -> None:
        print('This cog was loaded')
        self.bot: Bot = bot
        return

    @command
    async def test(self, ctx: Context):
        await ctx.send('Test returned')

    @staticmethod
    def generate_confirmation_embeds(type_: str, user: Member, reason: str) -> tuple[Embed, Embed]:
        pass

    @command(description='Bans a user')
    @can_ban()
    async def ban(self, ctx: Context, users: Greedy[Member], *, reason: str) -> None:
        """
        Bans a user after checking for the correct permissions
        Makes sure that the user is either:
        1. An administrator
        2. A moderator
        It also prevents anybody from banning themselves
        """
        for user in users:
            # Make sure the user is not banning themselves or somebody higher than them in the role hierarchy
            if user.id == ctx.author.id or user.top_role >= ctx.author.top_role:
                continue
            await ctx.guild.ban(
                user=user,
                reason=f'Banned by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}'
            )
        return

    @command(description='Kicks a user')
    @can_kick()
    async def kick(self, ctx: Context, users: Greedy[Member], *reason: Optional[tuple[str]]) -> None:
        # Each word in the reason is provided as a separate string, concatenate them together
        reason = ' '.join([word for word in reason]) if reason else 'No reason was provided'
        for user in users:
            # Make sure the user is not kicking themselves or somebody higher than them in the role hierarchy
            if user.id == ctx.author.id or user.top_role >= ctx.author.top_role:
                continue
            await ctx.guild.kick(
                user=user,
                reason=f'Kicked by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}'
            )
        return
