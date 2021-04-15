from discord.ext.commands import Bot, Cog, Context, group, command


class POTD(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @group(invoke_without_command=True)
    async def potd(self, ctx: Context):
        ctx.send('Problem of the day')

    @potd.command()
    async def new(self, cttx: Context):
        pass

    @potd.command()
    async def post(self, ctx: Context):
        pass

    @potd.command()
    async def detail(self, ctx: Context):
        pass
