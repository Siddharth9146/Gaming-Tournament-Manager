from fastapi import APIRouter, HTTPException, status
from config.db import matchCollection, playerCollection, tournamentCollection
from model.matchModel import Match
from model.playerModel import Player
from model.tournamentModel import Tournament
from bson import ObjectId
from schema.serializer import tournamentSerializer, playerSerializer, matchSerializer
import random


router = APIRouter()

@router.get("/matchInfoByWinner/{matchWinner}")
async def get_match(matchWinner: str):
    matchInfo = matchCollection.find_one({"matchWinner": (matchWinner)})
    if matchInfo:
        return matchSerializer(matchInfo)
    raise HTTPException(status_code=404, detail="Match not found")

@router.get("/findPlayer/{username}")
async def get_player(username: str):
    playerInfo = playerCollection.find_one({"username": username})
    if playerInfo:
        return playerSerializer(playerInfo)
    raise HTTPException(status_code=404, detail="Player not found")

@router.post("/addMatch/{tournamentCode}")
async def add_match(tournamentCode: str, match: Match):
    matchDict = match.dict()
    matchCollection.insert_one(matchDict)
    tournament = tournamentCollection.find_one({"tournamentCode": tournamentCode})
    if tournament:
        tournamentCollection.update_one({"_id": ObjectId(tournament["_id"])}, {"$push": {"tournamentMatches": str(matchDict["_id"])}})
    
        #set tournamentCode in match
        matchCollection.update_one({"_id": ObjectId(matchDict["_id"])}, {"$set": {"tournamentCode": tournamentCode}})
    
    else:
        raise HTTPException(status_code=404, detail="Tournament not found")
@router.post("/addPlayer")
async def add_player(player: Player):
    playerDict = player.dict()
    playerCollection.insert_one(playerDict)

@router.post("/addNewTournament")
async def add_tournament(tournament: Tournament):
    tournamentDict = tournament.dict()
    tournamentCollection.insert_one(tournamentDict)

    #put tournamentIsOver is False by default
    tournamentCollection.update_one({"_id": ObjectId(tournamentDict["_id"])}, {"$set": {"tournamentIsOver": False}})

    #update tournamentHistory in playerCollection
    for player in tournamentDict["tournamentParticipants"]:
        playerCollection.update_one({"username": player}, {"$push": {"tournamentHistory": str(tournamentDict["_id"])}})
   
    #create a random 6 digit tournament code
    while True:
        tournamentCode = str(random.randint(100000, 999999))
        if not tournamentCollection.find_one({"tournamentCode": tournamentCode}):   #check if code already exists
            break
    tournamentCollection.update_one({"_id": ObjectId(tournamentDict["_id"])}, {"$set": {"tournamentCode": tournamentCode}})


# add user input column to matches in a tournament
@router.post("/addMatchColumn/{tournamentId}")
async def add_match_column(tournamentId: str, columnName: str):
    tournament = tournamentCollection.find_one({"_id": ObjectId(tournamentId)})
    if tournament:
        for match in tournament["tournamentMatches"]:
            matchCollection.update_one({"_id": ObjectId(match)}, {"$set": {columnName: ""}})
    else:
        raise HTTPException(status_code=404, detail="Tournament not found")