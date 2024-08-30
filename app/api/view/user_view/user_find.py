from flask import Blueprint, request, jsonify, abort
from api.models import UserModel

# ルーティング設定
user_find = Blueprint("user_find", __name__)

@user_find.route("", methods=["POST"])
def find_user():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()
    print(requested_data)

    # 必須フィールドのチェック(user_id or phone_number)
    if not "user_id" in requested_data and not "phone_number" in requested_data:
        abort(400, "user_id or phone_number is a required field")

    
    # user_idがあればuser_idを取得し、なければphone_numberを取得
    user_identification_info = requested_data["user_id"] if "user_id" in requested_data else requested_data["phone_number"]

    # UserModelクラスのインスタンスを生成
    user_model = UserModel()

    try:
        # ユーザー情報を取得
        user_data = user_model.find_user(user_identification_info)
        user_data["_id"] = str(user_data['_id'])
        return jsonify({
            "code": 200,
            "user":user_data
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting user: {e}")
