from pymongo import MongoClient
from pymongo.server_api import ServerApi

class DBHelper:
    
    def __init__(self,db_name='jai2026'):
        uri = "mongodb+srv://jaiinderveersingh_db_user:Jai12345@jaidb.9o2qkps.mongodb.net/?appName=jaidb"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client[db_name]
        print(' [DBHelper] Connection Created')
        
    def select_collection(self,collection_name = 'users'):
        self.collection = self.db[collection_name]
        print(' [DBHelper] Collection Selected',collection_name)
    def save(self,document):
        inserted_id = self.collection.insert_one(document)
        print(' [DBHelper] Document Saved. ID is:',inserted_id)
