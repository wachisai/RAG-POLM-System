import pymongo
from pymongo import MongoClient

def get_mongo_client(uri):
    try:
        client = MongoClient(uri)
        print("Connection to MongoDB successful")
        return client
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None