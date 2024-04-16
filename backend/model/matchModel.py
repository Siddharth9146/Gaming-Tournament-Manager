from pydantic import BaseModel
from typing import List

class Match(BaseModel):
    #matchName="m1", matchType="knockout", matchParticipants=[], matchWinner=""
    matchName: str
    matchType: str
    matchParticipants: List[str]
    matchWinner: str
