import random

class Person():
    def __init__(self, personName, personData):
        self.name = personName
        self.data = personData
    
    def checkNameOrAlias(self, nameOrAlias):
        if self.name.lower() == nameOrAlias.lower():
            return True
        
        for alias in self.getAliases():
            if (alias.lower() == nameOrAlias.lower()):
                return True
        
        return False

    ## QUOTES ##
    def getQuotes(self):
        return self.data["Quotes"]

    def containsQuote(self, quoteToLookFor):
        for quote in self.data["Quotes"]:
            if quote.lower() == quoteToLookFor.lower():
                return True
        return False

    def addQuote(self, newQuote):
        self.data["Quotes"].append(newQuote)

    def removeQuote(self, quoteToRemove):
        for quote in self.data["Quotes"]:
            if quote.lower() == quoteToRemove.lower():
                self.data["Quotes"].remove(quoteToRemove)
                break

    ## ALIASES ##
    def getAliases(self):
        return self.data["Aliases"]

    def containsAlias(self, aliasToLookFor):
        for alias in self.data["Aliases"]:
            if alias.lower() == aliasToLookFor.lower():
                return True
        return False

    def addAlias(self, newAlias):
        self.data["Aliases"].append(newAlias)
    
    def removeAlias(self, aliasToRemove):
        for alias in self.data["Aliases"]:
            if alias.lower() == aliasToRemove.lower():
                self.data["Aliases"].remove(aliasToRemove)
                break