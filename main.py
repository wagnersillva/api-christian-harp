from controller.find import find_all_songs, find_one_song
from controller.create import create_song
from fastapi import FastAPI
from datetime import datetime
from model.model_song import Song
from typing import Optional

app = FastAPI()

@app.get("/harp/{song_key}")
async def find(song_key: int):
    if song_key:
        song = find_one_song(song_key)
    if song:
        return {"Status" : "true", "data" : song }
    else:
        return {"Status": "false", "data" :"No song found"}
        
@app.get("/harp/")
async def find(limit: Optional[int] = None):
    songs = find_all_songs(limit)
    if songs:
        return {"Status" : "true", "data" : songs }
    else:
        return {"Status": "false", "data" :"No song found"}

@app.post("/harp/create/")
async def create(body: Song):
    songs = create_song(body)
    if songs:
        return {"Status" : "true", "data" : songs }
    else:
        return {"Status": "false", "data" :"There was a mistake in trying to add music"}
