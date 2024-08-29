from flask import Flask
from .database import initialize_db

def create_app():
    app = Flask(__name__)

    # データベースの初期化
    initialize_db(app)

    # 他のブループリントや設定の登録
    

    return app

# app = create_app()