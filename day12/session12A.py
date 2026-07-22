from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jaiinderveersingh_db_user:Jai123@jaidb.9o2qkps.mongodb.net/?appName=jaidb"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['jai2026']
names = db.list_collection_names()
print(names)