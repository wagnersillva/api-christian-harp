from schema.schema_song import serializeList
from database.mongodb import dataBase

db = dataBase()
harp = db.harp
song = harp.song


def find_one_song():
    return serializeList(song.find_one())

def find_all_songs():
    return  serializeList(song.find())