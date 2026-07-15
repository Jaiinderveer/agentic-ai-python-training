from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://jaiinderveersingh_db_user:Jai12345@jaidb.9o2qkps.mongodb.net/?appName=jaidb"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)