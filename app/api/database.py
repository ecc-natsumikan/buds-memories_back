from pymongo import MongoClient
from config import Config

client = None
db = None

def initialize_db(app):
    global client, db
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.MONGO_DATABASE]
    print("MongoDBへの接続が確立されました。")

def get_db():
    return db
