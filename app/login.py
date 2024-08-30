from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'username' in data and 'password' in data:
        uid = verify_username_and_password(data['username'], data['password'])
    elif 'phone' in data and 'password' in data:
        uid = verify_phone_and_password(data['phone'], data['password'])
    else:
        return jsonify({"error": "ログインができません"}), 400

    if uid:
        token = auth.create_custom_token(uid)
        return jsonify({"token": token.decode('utf-8')}), 200
    else:
        return jsonify({"error": "入力情報が違います"}), 401

if __name__ == "__main__":
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG)