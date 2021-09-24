from pymongo import MongoClient
import json

with open('mongoDbCredentials.json') as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

dbUser = jsonObject['dbUser']
dbPassword = jsonObject['dbPassword']

def dataBase():
    try:
        connection_db_url = f'mongodb+srv://{dbUser}:{dbPassword}@pymongocluster.jjtue.mongodb.net/test'
        client = MongoClient(connection_db_url, serverSelectionTimeoutMS = 5000)
        return client
    except:
        return {"Error": "Error connection database"}