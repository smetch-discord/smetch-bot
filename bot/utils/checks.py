from discord import Role
from discord.ext.commands import Context, check
from discord.utils import get


def can_ban():
    '''
    Checks if a user has ban priveliges. Only people with:
    1. The administrator role
    2. The moderator role
    Should be able to ban.
    '''
    def predicate(ctx: Context) -> bool:
        mod_role: Role = get(ctx.guild.roles, id=807229822799446036)
        admin_role: Role = get(ctx.guild.roles, id=806922773649555469)
        if mod_role in ctx.author.roles or admin_role in ctx.author.roles:
            return True
        else:
            return False
    return check(predicate)
