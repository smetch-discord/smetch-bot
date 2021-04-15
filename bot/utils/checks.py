from discord.ext.commands import Context, check

def can_ban():
    def predicate(ctx: Context):
        bans = ctx.kwargs['users']
