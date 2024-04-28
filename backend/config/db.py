from pymongo import MongoClient
from urllib.parse import quote_plus
username = "rajopadhyesiddharth"
password = "SidR@2004$Mongo"

# Escape the username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct the connection string with escaped username and password
conn_string = f"mongodb+srv://{escaped_username}:{escaped_password}@gamingtournament.aw1dn2i.mongodb.net/?retryWrites=true&w=majority&appName=GamingTournament"

conn = MongoClient(conn_string)
db = conn.get_database("GamingTournament")
playerCollection = db.get_collection("playerCollection")
tournamentCollection = db.get_collection("tournamentCollection")
matchCollection = db.get_collection("matchCollection")

