from pydantic import BaseModel
from typing import List

class Leaderboard(BaseModel):
    username: str
    tournamentHistory: List[int] # list of tournament ids the player has been in
    matchHistory: List[int] # list of match ids the player has been in
    Leaderboard: dict # dict of tournament ids and the position of the player in that tournament

#example of a leaderboard
#leaderboardCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[], Leaderboard={}))