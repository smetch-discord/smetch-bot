from discord.ext.commands import Cog, Bot, Context, Command
from discord import Embed
from datetime import datetime
from dateutil.relativedelta import relativedelta

from bot.utils.time import humanize_delta


class Information(Cog):

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Command(description='Returns bot latency')
    async def ping(self, ctx: Context):
        bot_ping = (datetime.utcnow() - ctx.message.created_at).total_seconds() * 1000
        bot_ping: str = f'{bot_ping:.3f} ms'
        discord_ping: str = f'{self.bot.latency * 1000:.3f} ms'

        embed: Embed = Embed(
            title='Ping!',
            colour=0x00d166
        )

        for description, latency in zip(['Command Processing Time', 'Discord API Latency'], [bot_ping, discord_ping]):
            embed.add_field(
                name=description,
                value=latency,
                inline=False
            )

        await ctx.send(embed=embed)
        return

    @Command(description='Returns information about the server')
    async def server(self, ctx: Context):
        guild = ctx.message.guild
        embed = Embed(
            title='Server information',
            description='SMETCH is a community that helps those in need!',
            colour=0x00d166
        )

        embed.set_thumbnail(
            url=guild.icon_url
        )

        now = datetime.utcnow()
        delta = abs(relativedelta(now, guild.created_at))
        humanized = humanize_delta(delta)

        created_at = f'{humanized} ago'

        embed.add_field(
            name='Server was created on:',
            value=f'{guild.created_at.strftime("%d %B %Y")}\n{created_at}',
            inline=False
        )

        members_not_bots = len([x for x in filter(lambda member: not member.bot, guild.members)])
        bots_not_members = guild.member_count - members_not_bots
        invite = await self.bot.fetch_invite('discord.gg/RqPtwNxd8h')
        online = invite.approximate_presence_count
        offline = invite.approximate_member_count - invite.approximate_presence_count

        embed.add_field(
            name='Member count:',
            value=f'👥 {members_not_bots} humans\n🤖 {bots_not_members} bots\nTotal: {guild.member_count}\
                 \n🟢 {online}  ⚪ {offline}',
            inline=False
        )

        embed.add_field(
            name='Current owner:',
            value=f'<@{guild.owner_id}>',
            inline=False
        )

        embed.add_field(
            name='Current boosts:',
            value=f'{guild.premium_subscription_count} boosts at Level {guild.premium_tier}'
        )

        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Information)
