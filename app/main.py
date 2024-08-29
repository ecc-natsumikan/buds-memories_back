from flask import Flask
from config import Config
from api import create_app


# Flaskアプリケーションの生成
app = create_app()

if __name__ == "__main__":
    app.run(host=Config.HOST, port=Config.PORT, debug=Config.DEBUG)
