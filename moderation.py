import discord
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)  
    async def kick(self, ctx, member: commands.Greedy[discord.Member], *, reason = "No reason was provided") -> None:
        for user in member:
            await user.kick(reason = reason)
            await ctx.send(embed=discord.Embed(title=f"<@{user.id}> was kicked from SMETCH", description=reason, color=0xaaffff))
        
    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.Greedy[discord.Member], *, reason = "No reason was provided") -> None:
        for user in member:
            try:
              await user.send(embed=discord.Embed(color = 0xff0000, title='Ban info', description=f'Hello <@{user.id}>, we are contacting you since you were recently banned from SMETCH. You have banned for the following reason:\n**{reason}**\n\n**I have been wronged**\nIf you feel you have been banned unjustifiably you can always submit an appeal [here](https://forms.gle/t3RhEZtz62LNvGyi7)'))
              await ctx.send(embed=discord.Embed(color = 0x00ff00, description=f'Managed to contact <@{user.id}> successfully.'))
            except discord.Forbidden:
              await ctx.send(embed=discord.Embed(color=0xff0000, description=f'Failed to contact <@{user.id}> successfully'))
            await user.ban(reason = reason)
            await ctx.send(embed=discord.Embed(title=f'<@{user.id}> has been banned from SMETCH', description=reason, color = 0x00ff00))
            
    @ban.error         
    @kick.error
    async def mod_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(description='Who do you think you are trying to do that to the poor kid? Wait till you\'re mod or admin and then try again', color = 0xaaffff))
        else:
            raise error

    @commands.has_permissions(manage_roles=True)
    @commands.command(name='advanced')
    async def advanced(self, ctx, members: commands.Greedy[discord.Member]):
        advanced_math_role = ctx.guild.get_role(809184355485351966)
        for member in members:
            await member.add_roles(advanced_math_role)
            await ctx.send(f'Advanced math role has been given to <@{member.id}>')
        return