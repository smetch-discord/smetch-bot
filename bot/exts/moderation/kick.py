from typing import Optional
from discord.ext.commands import command, Context
from discord import Member
from discord.ext.commands.core import has_permissions
from ...bot import constants


@has_permissions(kick=True)
@command
async def kick(ctx: Context, user: Member, reason: Optional[str] = 'No reason was provided') -> None:
    if user == ctx.author or user.top_role > ctx.author.top_role:
        return
    await user.kick(reason=f'Kicked by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}')
    constants.database.add_infraction(
        type_='kick',
        moderator=ctx.author,
        user=user,
        reason=reason
    )
    return
