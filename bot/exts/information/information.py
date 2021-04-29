from discord.ext.commands import Cog, Bot, Context, command
from discord import Embed, Guild, Invite, Member
from datetime import datetime
from dateutil.relativedelta import relativedelta

from bot.utils.time import humanize_delta


class Information(Cog):
    """
    Provides information about various things including:
    - The server
    - The bot's latency

    > More to be added
    """

    def __init__(self, bot: Bot) -> None:
        self.bot: Bot = bot
        return

    @command(description='Returns bot latency')
    async def ping(self, ctx: Context) -> None:
        """
        Returns two types of latency:
        1. The processing time it takes for the bot to register a command
        2. The Discord API Latency. Measures the time between a `HEARTBEAT` and a `HEARTBEAT_ACK`
        """
        current_time: datetime = datetime.utcnow()
        message_creation: datetime = ctx.message.created_at
        command_time: float = (current_time - message_creation).total_seconds() * 1000
        command_time: str = f'{command_time:.3f} ms'

        # Discord returns latency in seconds not milliseconds
        api_ping: str = f'{self.bot.latency * 1000:.3f} ms'

        embed: Embed = Embed(
            title='Ping!',
            colour=0x00d166
        )

        for description, latency in zip(['Command Processing Time', 'Discord API Latency'], [command_time, api_ping]):
            embed.add_field(
                name=description,
                value=latency,
                inline=False
            )

        await ctx.send(embed=embed)
        return

    @command(description='Returns information about a certain user')
    async def user(self, ctx: Context, user: Member) -> None:
        """
        Command still a WIP
        """
        name = f'{user.display_name}#{user.discriminator}'
        await ctx.send(name)

    @command(description='Returns information about the server')
    async def server(self, ctx: Context) -> None:
        """
        Returns information about the guild the command was run in.
        Information included:
        - A brief server description
        - Server icon
        - Date server was created (and how long ago that was)
        - Human member count
        - Bot count
        - How many members are online/offline
        - Current server owner
        - Boost information
        """
        # Save guild to variable instead of using `ctx.message.guild` each time
        guild: Guild = ctx.message.guild

        # Calculate when the guild was created and how long ago that was and present it in a human-friendly format
        now: datetime = datetime.utcnow()
        delta: relativedelta = abs(relativedelta(now, guild.created_at))
        humanized: str = humanize_delta(delta)
        created_at: str = guild.created_at.strftime('%d %B %Y')
        created_ago: str = f'{humanized} ago'

        # Get guild's icon
        icon: str = guild.icon_url

        # Get information about the current members of the guild
        humans: int = len([x for x in filter(lambda member: not member.bot, guild.members)])
        bots: int = guild.member_count - humans
        total: int = humans + bots
        invite: Invite = await self.bot.fetch_invite('discord.gg/RqPtwNxd8h')
        online: int = invite.approximate_presence_count
        offline: int = invite.approximate_member_count - invite.approximate_presence_count

        # Get owner information
        owner: str = guild.owner.mention

        # Get server boost information
        number_of_boosts: int = guild.premium_subscription_count
        boost_level: int = guild.premium_tier

        # Declare embed with all fields added
        embed = Embed(
            title='Server information',
            description='SMETCH is a community that helps those in need!',
            colour=0x00d166
        ).add_field(
            name='Server was created on:',
            value=f'{created_at}\n{created_ago}',
            inline=False
        ).add_field(
            name='Member count:',
            value=f'👥 {humans} humans\n🤖 {bots} bots\nTotal: {total}\
                  \n<:online:832185731845062716> {online} <:offline:832185762618671164> {offline}',
            inline=False
        ).add_field(
            name='Current owner:',
            value=owner,
            inline=False
        ).add_field(
            name='Current boosts:',
            value=f'{number_of_boosts} boosts at Level {boost_level}',
            inline=True
        ).set_thumbnail(
            url=icon
        )

        await ctx.send(embed=embed)
        return


def setup(bot: Bot):
    bot.add_cog(Information(bot))
