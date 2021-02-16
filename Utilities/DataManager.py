import os
import json

from Models.Person import Person

if os.path.exists("QuotesBot\\Storage\\DynamicQuotes.json"):
    with open("QuotesBot\\Storage\\DynamicQuotes.json") as file:
        data = json.load(file)
else:
    with open("QuotesBot\\Storage\\Quotes.json") as file:
        data = json.load(file)

people = []
for personName in data:
    person = Person(personName, data[personName])
    people.append(person)

def saveData():
    with open("QuotesBot\\Storage\\DynamicQuotes.json", "w") as file:
        json.dump(data, file)