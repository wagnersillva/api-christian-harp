from controller.song.find import find_all_songs, find_one_song
from controller.song.create import create_song
from fastapi import FastAPI
from model.model_song import Song
from typing import Optional

app = FastAPI()

@app.get("/{song_key}")
async def find(song_key: int):
    if song_key:
        song = find_one_song(song_key)
    if song:
        return {"Status" :  song['status'], "data" : song['data'] }
    else:
        return {"Status":  False, "data" :"An error has occurred"}
        
@app.get("/")
async def find(limit: Optional[int] = None):
    songs = find_all_songs(limit)
    if songs:
        return {"Status" :  songs['status'], "data" : songs['data'] }
    else:
        return {"Status":  False, "data" :"An error has occurred"}

@app.post("/create/")
async def create(body: Song):
    songs = create_song(body)
    if songs:
        return {"status" : songs['status'], "data" : songs['data'] }
    else:
        return {"status":  False, "data" : 'An error has occurred' }
