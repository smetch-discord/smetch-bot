from typing import Optional
from discord.errors import DiscordException
from discord.ext.commands import Command, Context, Bot
from discord import Member, Forbidden, Embed
from ..backend.database import Database


class InfractionEmbed(Embed):

    def __init__(self, type_: str, reason: str):
        content = f'You were {type_}ed on SMETCH due to the following reason: {reason}'
        super().__init__(description=content)


@Command
async def ban(ctx: Context, user: Member, reason: Optional[str] = 'No reason was provided') -> None:
    ctx.send('Command called')
    if user == ctx.author or user.top_role > ctx.author.top_role:
        return
    confirmation_embed: Embed = Embed(color=0x0003ff)
    try:
        user.send(embed=InfractionEmbed('ban', reason))
        confirmation_embed.description += f'Successfully DMed user: `{user.name}#{user.discriminator}`\n'
    except Forbidden:
        confirmation_embed.description += f'Failed to DM user: `{user.name}#{user.discriminator}`\n'
    try:
        await user.ban(reason=f'Banned by {ctx.author.name}#{ctx.author.discriminator} for reason: {reason}')
        confirmation_embed.description += f'Successfully banned user: `{user.name}#{user.discriminator}`\n'
    except DiscordException:
        confirmation_embed.description += f'Failed to ban user: `{user.name}#{user.discriminator}`\n'
    ctx.send(embed=confirmation_embed)
    Database().add_infraction(
        type_='ban',
        moderator=ctx.author,
        user=user,
        reason=reason
    )
    return


def setup(bot: Bot):
    print('Added ban command')
    bot.add_command(ban)
