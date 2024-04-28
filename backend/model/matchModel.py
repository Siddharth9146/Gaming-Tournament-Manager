from pydantic import BaseModel
from typing import List

class Match(BaseModel):
    matchType: str
    matchParticipants: List[str] #usernames of the players in the match
    matchWinner: str #username of the winner
    tournamentCode: str

