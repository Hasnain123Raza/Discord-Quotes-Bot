import os
import json

with open("QuotesBot\\Storage\\PermissionIDs.json") as file:
        data = json.load(file)

def saveData():
     with open("QuotesBot\\Storage\\PermissionIDs.json", "w") as file:
        json.dump(data, file)