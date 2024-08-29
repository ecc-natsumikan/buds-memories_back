from flask import request, jsonify, abort, Blueprint
from api.models import UserModel

# ルーティング設定
user_update = Blueprint("user_update", __name__)

@user_update.route("", methods=["POST"])
def update_user():
    # JSONデータを取得する
    requested_data = request.get_json()
    print(requested_data)

    # 必須フィールドのチェック
    if not "user_id" in requested_data:
        abort(400, "user_id is a required field")

    user_model = UserModel()

    try:
        # ユーザー情報の更新を実行
        result = user_model.update_user(requested_data["user_id"], requested_data["update_data"])
        if result.modified_count == 0:
            return jsonify({
                "message": "User not found or no fields were updated."
            })

        return jsonify({
            "code": 200,
            "message": "User successfully updated",
            "modified_count": result.modified_count
        })
    except Exception as e:
        abort(500, f"Error occurred while updating user: {e}")
