from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from config import Config

client = None
db = None

def initialize_db(app):
    global client, db
    try:
        # MongoDBクライアントを作成し、接続を確立
        client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)

        # データベースを取得
        db = client[Config.MONGO_DATABASE]
        
        print("MongoDBへの接続が確立されました。")
        
    except ConnectionFailure as e:
        print(f"MongoDBへの接続に失敗しました: {e}")
        raise e

def get_db():
    return db