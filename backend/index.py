from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from urllib.parse import quote_plus
from routes.routes import router


app = FastAPI()

app.include_router(router)

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.db import conn_string
try:
    conn = MongoClient(conn_string)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# code used for testing
# playerCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[]))
# tournamentCollection.insert_one(dict(tournamentName="t1", tournamentType="knockout", tournamentParticipants=[], tournamentMatches=[], winner="", tournamentId=0, tournamentIsOver=False))
# matchCollection.insert_one(dict(matchName="m1", matchType="knockout", matchParticipants=[], matchWinner=""))
# leaderboardCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[], Leaderboard={}))


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

@app.get("/")
async def root():
    return {"message": "Hello World"}

#remove all matchName from matchcollection
from config.db import matchCollection
@app.get("/removeMatchName")
async def remove_matchName():
    matchCollection.update_many({}, {"$unset": {"matchName": ""}})
    return {"message": "All matchName removed"}