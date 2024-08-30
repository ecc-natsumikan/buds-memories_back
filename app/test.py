from flask import Flask, request, jsonify
from app.auth_handler import verify_username_and_password, verify_phone_and_password

app = Flask(__name__)

@app.route('/login', methods=['POST'])
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
    app.run(host='0.0.0.0', port=5001)
