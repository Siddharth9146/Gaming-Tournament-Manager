from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from urllib.parse import quote_plus


app = FastAPI()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.db import conn_string, playerCollection, tournamentCollection, matchCollection, leaderboardCollection

try:
    conn = MongoClient(conn_string)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

playerCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[]))
tournamentCollection.insert_one(dict(tournamentName="t1", tournamentType="knockout", tournamentParticipants=[], tournamentMatches=[], winner="", tournamentId=0, tournamentIsOver=False))
matchCollection.insert_one(dict(matchName="m1", matchType="knockout", matchParticipants=[], matchWinner=""))
leaderboardCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[], Leaderboard={}))


from fastapi.middleware.cors import CORSMiddleware
origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5000",
    "http://localhost:5500",
    "http://127.0.0.1/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)
import requests

url = "https://trackmania.p.rapidapi.com/players/search"

querystring = {"search_query":"Riolu"}

headers = {
	"X-RapidAPI-Key": "97cf2144f5mshcca3dfb6a90ad1fp1bc664jsnf8d38d8e2ce2",
	"X-RapidAPI-Host": "trackmania.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())