from controller.find import find_all_songs, find_one_song
from controller.create import create_song
from fastapi import FastAPI
from datetime import datetime
from model.model_song import Song

app = FastAPI()

@app.get("/harp/")
async def find(body: Song):
    song = find_one_song(body)
    return song

@app.get("/harp/")
async def find(body: Song):
    song = find_all_songs(body)
    return song

@app.post("/harp/create/")
async def create(body: Song):
    song = create_song(body)
    return song
