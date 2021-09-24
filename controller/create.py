from database.mongodb import dataBase
from schema.schema_song import serializeList
from datetime import datetime

db = dataBase()
harp = db.harp
song = harp.song

def create_song(body):
    request_body = body
    data = {"datatime" : datetime.utcnow()}
    data.update(request_body)
    try:
        song.insert_one(dict(data))
        data_response = serializeList(song.find())
        if data_response:
            return data_response
        else:
            return False
    except:
        return False