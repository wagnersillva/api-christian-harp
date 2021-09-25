from schema.schema_song import serializeDict, serializeList
from database.mongodb import dataBase
from typing import Optional

db = dataBase()
letters = db.letters
song = letters.song



def find_one_song(key):
    try:
        songs = serializeDict(song.find_one({"number" : key}))
        if songs: 
            return songs 
        else:
            return False 
    except:
        return False

def find_all_songs(limit: Optional[int] = None):
    if limit:
        try:   
            songs = serializeList(song.find().limit(limit))
            if songs: 
                return songs 
            else:
                return False 
        except:
            return False 
    else:
        try:
            songs = serializeList(song.find())
            if songs: 
                return songs 
            else:
                return False 
        except:
            return False 
