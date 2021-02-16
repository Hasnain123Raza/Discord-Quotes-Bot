import random

from discord.ext import commands
from Utilities import DataAccess
from Utilities.StringsManager import stringsData
from Utilities import PermissionDataManager

class ViewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["sp"], help="Shows people")
    async def showpeople(self, ctx):
        people = DataAccess.getPeople()
        peopleNames = []
        for person in people:
            peopleNames.append(person.name)

        if peopleNames:
            reply = ", ".join(peopleNames)
        else:
            reply = stringsData["EmptyPeopleNamesListReply"]
        
        await ctx.send(reply)

    

    @commands.command(aliases=["sa"], help="Shows a persons aliases")
    async def showaliases(self, ctx, *, nameOrAlias):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)
        
        if person:
            aliases = person.getAliases()
            if aliases:
                reply = ", ".join(aliases)
            else:
                reply = stringsData["EmptyAliasesListReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]
        
        await ctx.send(reply)
            

        
    @commands.command(aliases=["sq"], help="Shows a persons quotes")
    async def showquotes(self, ctx, *, nameOrAlias):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)
        
        if person:
            quotes = person.getQuotes()
            if quotes:
                reply = "\n\n".join(quotes)
            else:
                reply = stringsData["EmptyQuotesListReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]
        
        await ctx.send(reply)
    


    @commands.command(aliases=["qt"], help="Use to quote a person")
    async def quote(self, ctx, *, nameOrAlias):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)
        
        if person:
            quotes = person.getQuotes()
            if quotes:
                reply = random.choice(quotes)
            else:
                reply = stringsData["EmptyQuotesListReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]
        
        await ctx.send(reply)
    


    @commands.command(aliases=["showperms"], help="Shows people with permissions")
    async def showpermissions(self, ctx):
        if PermissionDataManager.data:
            reply = ", ".join(str(x) for x in PermissionDataManager.data)
        else:
            reply = stringsData["EmptyPermissionIDsListReply"]
        
        await ctx.send(reply)
