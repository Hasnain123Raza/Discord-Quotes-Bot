from Utilities.DataManager import data
from Utilities.DataManager import people
from Utilities.DataManager import saveData
from Models.Person import Person

def getPeople():
    return people

def getPersonByNameOrAlias(nameOrAlias):
    for person in people:
        if person.checkNameOrAlias(nameOrAlias):
            return person

def addPersonByName(name):
    data[name] = {
        "Quotes" : [],
        "Aliases" : []
    }
    saveData()
    people.append(Person(name, data[name]))

def addAliasToPerson(person, newAlias):
    person.addAlias(newAlias)
    saveData()

def addQuoteToPerson(person, newQuote):
    person.addQuote(newQuote)
    saveData()

def removePerson(person):
    del data[person.name]
    people.remove(person)
    saveData()

def removeAliasFromPerson(person, aliasToRemove):
    person.removeAlias(aliasToRemove)
    saveData()

def removeQuoteFromPerson(person, quoteToRemove):
    person.removeQuote(quoteToRemove)
    saveData()