from discord.ext import commands
from Utilities import DataAccess
from Utilities.StringsManager import stringsData
from Utilities import PermissionDataManager

def has_permissions():
    async def predicate(ctx):
        return ctx.author.id in PermissionDataManager.data
    return commands.check(predicate)

class EditCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["ap"], help="Adds a person")
    @has_permissions()
    async def addperson(self, ctx, *, name):
        if DataAccess.getPersonByNameOrAlias(name) is not None:
            reply = stringsData["PersonNameNotUniqueReply"]
        else:
            DataAccess.addPersonByName(name)
            reply = stringsData["PersonAddedReply"]
        
        await ctx.send(reply)



    @commands.command(aliases=["aa"], help="Adds an alias to the specified person")
    @has_permissions()
    async def addalias(self, ctx, nameOrAlias, newAlias):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)
        
        if person:
            if person.containsAlias(newAlias) or person.name.lower() == newAlias.lower():
                reply = stringsData["PersonAliasNotUniqueReply"]
            else:
                DataAccess.addAliasToPerson(person, newAlias)
                reply = stringsData["AliasAddedReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]
        
        await ctx.send(reply)
    


    @commands.command(aliases=["aq"], help="Adds a quote for the specified person")
    @has_permissions()
    async def addquote(self, ctx, nameOrAlias, newQuote):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)
        
        if person:
            if person.containsQuote(newQuote):
                reply = stringsData["PersonQuoteNotUniqueReply"]
            else:
                DataAccess.addQuoteToPerson(person, newQuote)
                reply = stringsData["QuoteAddedReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]
        
        await ctx.send(reply)
    


    @commands.command(aliases=["rp"], help="Removes a person")
    @has_permissions()
    async def removeperson(self, ctx, *, nameOrAlias):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)

        if person:
            DataAccess.removePerson(person)
            reply = stringsData["PersonRemovedReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]

        await ctx.send(reply)
    


    @commands.command(aliases=["ra"], help="Removes an alias for the specified person")
    @has_permissions()
    async def removealias(self, ctx, nameOrAlias, aliasToRemove):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)

        if person:
            if person.containsAlias(aliasToRemove):
                DataAccess.removeAliasFromPerson(person, aliasToRemove)
                reply = stringsData["AliasRemovedReply"]
            else:
                reply = stringsData["AliasNotFoundReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]

        await ctx.send(reply)
    



    @commands.command(aliases=["rq"], help="Removes a quote for the specified person")
    @has_permissions()
    async def removequote(self, ctx, nameOrAlias, quoteToRemove):
        person = DataAccess.getPersonByNameOrAlias(nameOrAlias)

        if person:
            if person.containsQuote(quoteToRemove):
                DataAccess.removeQuoteFromPerson(person, quoteToRemove)
                reply = stringsData["QuoteRemovedReply"]
            else:
                reply = stringsData["QuoteNotFoundReply"]
        else:
            reply = stringsData["PersonNotFoundReply"]

        await ctx.send(reply)