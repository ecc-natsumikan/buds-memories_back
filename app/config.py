from dotenv import load_dotenv
import os

class SystemConfig:
    load_dotenv()

    # 環境変数からMongoDBに関する設定を取得
    MONGO_USER = os.getenv("MONGO_USER")
    MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
    MONGO_HOST = os.getenv("MONGO_HOST")
    MONGO_DATABASE = os.getenv("MONGO_DATABASE")

    # MongoDBの接続URIを構築
    MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DATABASE}"

    # Flaskアプリケーションの設定
    HOST = os.getenv("HOST")  # ホスト名
    PORT = os.getenv("PORT")  # ポート番号
    DEBUG = os.getenv("DEBUG")  # デバッグモードの有効化


Config = SystemConfig
