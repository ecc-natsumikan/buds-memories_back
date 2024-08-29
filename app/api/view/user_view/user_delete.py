from flask import request, jsonify, abort, Blueprint
from api.models import UserModel

# ルーティング設定
user_delete = Blueprint("user_delete", __name__)

@user_delete.route("", methods=["POST"])
def delete_user():
    # JSONデータを取得する
    requested_data = request.get_json()

    # 必須フィールドのチェック
    if not "user_id" in requested_data:
        abort(400, "user_id is a required field")

    user_model = UserModel()

    try:
        # ユーザー情報の削除を実行
        result = user_model.delete_user(requested_data["user_id"])

        if result.deleted_count == 0:
            return jsonify({
                "code": 400,
                "message": "User not found."
            })

        return jsonify({
            "code": 200,
            "message": "User successfully deleted",
            "deleted_count": result.deleted_count
        })
    except Exception as e:
        abort(400, f"Error occurred while deleting user: {e}")
