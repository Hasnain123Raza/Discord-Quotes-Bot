import discord

from discord.ext import commands
from Utilities import PermissionDataManager
from Utilities.StringsManager import stringsData

def is_me():
    async def predicate(ctx):
        return ctx.author.id == 177314728824143873
    return commands.check(predicate)

class PermissionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["gp", "giveperms"], help="Gives permissions to the specified person")
    @is_me()
    async def givepermissions(self, ctx, member: discord.Member):
        if not member.id in PermissionDataManager.data:
            PermissionDataManager.data.append(member.id)
            PermissionDataManager.saveData()
            reply = stringsData["PermissionGivenReply"]
        else:
            reply = stringsData["PermissionAlreadyGivenReply"]
        
        await ctx.send(reply)
    
    @commands.command(aliases=["tp", "takeperms"], help="Takes permissions from the specified person")
    @is_me()
    async def takepermissions(self, ctx, member: discord.Member):
        if member.id in PermissionDataManager.data:
            PermissionDataManager.data.remove(member.id)
            PermissionDataManager.saveData()
            reply = stringsData["PermissionTakenReply"]
        else:
            reply = stringsData["PermissionAlreadyTakenReply"]
        
        await ctx.send(reply)