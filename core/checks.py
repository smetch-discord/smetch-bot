from .files import Data
from discord.ext import commands

config = Data("config").yaml_read()

permissions = Data("permissions").yaml_read()

def manager():
    def predicate(ctx):
        return ctx.author.id in config["managers"]
    return commands.check(predicate)

def canReply():
    def predicate(ctx):
        if not ctx.guild or not ctx.guild.id == config["support_guild"]: return False
        if ctx.guild.get_role(config["support_role"]) in ctx.author.roles: return True
        else: return False
    return commands.check(predicate)

def mainServer():
    def predicate(ctx):
        return ctx.guild.id == config["server"]
    return commands.check(predicate)

def canBan():
    def predicate(ctx):
        return ctx.guild.get_role(permissions["banRole"]) in ctx.author.roles or ctx.author.guild_permissions.ban_members
    return commands.check(predicate)

def canKick():
    def predicate(ctx):
        return ctx.guild.get_role(permissions["kickRole"]) in ctx.author.roles or ctx.author.guild_permissions.kick_members
    return commands.check(predicate)

def canMute():
    def predicate(ctx):
        return ctx.guild.get_role(permissions["banRole"]) in ctx.author.roles or ctx.guild.get_role(permissions["banRole"]) in ctx.author.roles or ctx.author.guild_permissions.administrator
    return commands.check(predicate)

def canWarn():
    def predicate(ctx):
        return ctx.guild.get_role(permissions["warnRole"]) in ctx.author.roles or ctx.guild.get_role(permissions["banRole"]) in ctx.author.roles or ctx.author.guild_permissions.administrator
    return commands.check(predicate)
