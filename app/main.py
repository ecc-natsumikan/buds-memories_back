from flask import request, jsonify
from config import Config
from api import create_app
from auth_handler import verify_username_and_password, verify_phone_and_password


# Flaskアプリケーションの生成
app = create_app()

@app.route("/")
def index():
    return "接続成功"

@app.route("/login")
def login():
    data = request.json
    if 'username' in data and 'password' in data:
        uid = verify_username_and_password(data['username'], data['password'])
    elif 'phone' in data and 'password' in data:
        uid = verify_phone_and_password(data['phone'], data['password'])
    else:
        return jsonify({"error": "ログインできませんでした"}), 400

    if uid:
        token = auth.create_custom_token(uid)
        return jsonify({"token": token.decode('utf-8')}), 200
    else:
        return jsonify({"error": "アカウントがありません"}), 401
    
    

if __name__ == "__main__":
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG)