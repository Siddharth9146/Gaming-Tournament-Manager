from pydantic import BaseModel
from typing import List

class Tournament(BaseModel):
    # add the name of tournament creator, which will be the person logging in.....
    tournamentName: str
    tournamentType: str
    tournamentParticipants: List[str] #usernames of the players in the tournament
    tournamentMatches: List[str] #list of match obj ids in the tournament
    winner: str
    tournamentIsOver: bool
    tournamentCode: str

    


