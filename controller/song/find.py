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
            return  {
                    "status" : True,
                    "data" : songs
                }
        else:
            return {
                    "status" : False,
                    "data" : "song not found"
                } 
    except:
        return {
                "status" : False,
                "data" : "An error occurred"
            } 

def find_all_songs(limit: Optional[int] = None):
    if limit:
        try:   
            songs = serializeList(song.find().limit(limit))
            if songs: 
                return {
                    "status" : True,
                    "data" : songs
                } 
            else:
                return {
                    "status" : False,
                    "data" : "song not found"
                } 
        except:
            return {
                "status" : False,
                "data" : "An error occurred"
            } 
    else:
        try:
            songs = serializeList(song.find())
            if songs: 
                return {
                    "status" : True,
                    "data" : songs
                }  
            else:
                return {
                    "status" : False,
                    "data" : "song not found"
                }  
        except:
            return {
                "status" : False,
                "data" : "An error occurred"
            } 
