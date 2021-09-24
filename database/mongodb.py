from pymongo import MongoClient


def dataBase():

    dbUser = "koaladev"
    dbPassword = "XhZI6P49Ah4u1uEQ"
    
    try:
        connection_db_url = f'mongodb+srv://{dbUser}:{dbPassword}@pymongocluster.jjtue.mongodb.net/test'
        client = MongoClient(connection_db_url, serverSelectionTimeoutMS = 5000)
        return client
    except:
        return {"Error": "Error connection database"}