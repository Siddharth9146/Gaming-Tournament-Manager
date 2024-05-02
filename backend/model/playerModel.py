from pydantic import BaseModel
from typing import List

class Player(BaseModel):
    username: str
    tournamentHistory: list[str] # list of tournament obj ids the player has been in
    matchHistory: List[str] # list of match obj ids the player has been in
    #password is needed for tournament login page...... ksshitij
    #create password ka bhi soch, player registraion mein mein new password banara...
    
    #playerCollection.insert_one(dict(username="sid", tournamentHistory=[], matchHistory=[]))
