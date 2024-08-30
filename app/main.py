from flask import Flask
from config import Config
from api import create_app


# Flaskアプリケーションの生成
app = create_app()

@app.route("/")
def index():
    return "接続成功"

if __name__ == "__main__":
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG)