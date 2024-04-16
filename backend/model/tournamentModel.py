from pydantic import BaseModel

class Tournament(BaseModel):
    tournamentName: str
    tournamentType: str
    tournamentParticipants: list[str]
    tournamentMatches: list[str]
    winner: str
    tournamentId: int
    tournamentIsOver: bool


#example of a tournament
#tournamentCollection.insert_one(dict(tournamentName="t1", tournamentType="knockout", tournamentParticipants=[], tournamentMatches=[], winner="", tournamentId=0, tournamentIsOver=False))