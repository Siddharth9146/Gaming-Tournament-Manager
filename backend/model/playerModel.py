from pydantic import BaseModel

class Player(BaseModel):
    username: str
    tournamentHistory: list[int] # list of tournament ids the player has been in
    matchHistory: list[int] # list of match ids the player has been in

    #playerCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[]))