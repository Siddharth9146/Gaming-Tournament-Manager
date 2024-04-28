def matchSerializer(match)-> dict:
    return {
        "matchId": str(match["_id"]),
        "matchType": match["matchType"],
        "matchParticipants": match["matchParticipants"],
        "matchWinner": match["matchWinner"]
    }

def playerSerializer(player) -> dict:
    return {
        "playerId": str(player["_id"]),
        "username": player["username"],
        "tournamentHistory": player["tournamentHistory"],
        "matchHistory": player["matchHistory"]
    }

def tournamentSerializer(tournament) -> dict:
    return {
        "tournamentId": str(tournament["_id"]),
        "tournamentName": tournament["tournamentName"],
        "tournamentType": tournament["tournamentType"],
        "tournamentParticipants": tournament["tournamentParticipants"],
        "tournamentMatches": tournament["tournamentMatches"],
        "winner": tournament["winner"],
        "tournamentIsOver": tournament["tournamentIsOver"],
        "tournamentCode": tournament["tournamentCode"]
    }