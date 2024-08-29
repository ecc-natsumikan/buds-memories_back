from flask import request, jsonify, abort, Blueprint
from api.models import UserModel

# ルーティング設定
user_insert = Blueprint("user_insert", __name__)

@user_insert.route("", methods=["POST"])
def insert_user():
    # JSONデータを取得する
    requested_data = request.get_json()

    # 必須フィールドのチェック
    required_fields = ["_id", "user_name", "phone_number", "email", "password", "date_of_birth", "icon_image_url"]
    for field in required_fields:
        if field not in requested_data:
            abort(400, f"{field} is a required field")

    user_model = UserModel()

    try:
        # ユーザー情報を登録する
        result = user_model.create_user(requested_data)
        return jsonify({
            "code": 200,
            "message": "User successfully created",
            "inserted_id": str(result.inserted_id)
        })
    except Exception as e:
        abort(400, f"Error occurred while inserting user: {e}")
