from database.mongodb import dataBase
from schema.schema_song import serializeDict, serializeList
from datetime import datetime

db = dataBase()
letters = db.letters
song = letters.song

errors_texts = {
    "create_music" : "an error occurred while trying to add music",
    "music_exists" : "there is already a song with this number",
    "an_error" : "an error occurred"
}

def create_song(body):
    request_body = body
    data = {"datatime" : datetime.utcnow()}
    data.update(request_body)
    try:
        serializeDict(song.find_one({"number" : data['number']}))
        return {
            "status" : False,
            "data" : errors_texts["music_exists"]
        }   
    except:
        try:
            song.insert_one(dict(data))
            data_response = serializeList(song.find())
            if data_response:
                return {
                    "status" : True,
                    "data" : data_response
                }
            else:
                return {
                    "status" : False,
                    "data" : errors_texts["create_music"]
                }   
        except:
            return {
                "status" : False,
                "data" : errors_texts["an_error"]
            }   