from discord import Role, DMChannel
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
        if any([role in ctx.author.roles for role in (mod_role, admin_role)]):
            return True
        else:
            return False
    return check(predicate)


def can_kick():
    '''
    Checks if a user has kick priveliges. Only people with:
    1. The administrator role
    2. The moderator role
    3. The trainee moderator role
    Should be able to kick.
    '''
    def predicate(ctx: Context) -> bool:
        trainee_mod_role: Role = get(ctx.guild.roles, id=807410624438861875)
        mod_role: Role = get(ctx.guild.roles, id=807229822799446036)
        admin_role: Role = get(ctx.guild.roles, id=806922773649555469)
        if any([role in ctx.author.roles for role in (trainee_mod_role, mod_role, admin_role)]):
            return True
        else:
            return False
    return check(predicate)
