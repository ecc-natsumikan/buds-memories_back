from flask import Blueprint, request, jsonify, abort
from api.models import UserPostModel

# ルーティング設定
post_select_user = Blueprint("post_select_user", __name__)

@post_select_user.route("", methods=["POST"])
def select_user_post():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()
    print(requested_data)

    # 必須フィールドのチェック(user_id)
    if not "user_id" in requested_data:
        abort(400, "user_id is a required field")

    # user_idがあればuser_idを取得
    user_id = requested_data["user_id"]
    # UserModelクラスのインスタンスを生成
    user_post_model = UserPostModel()

    try:
        # 投稿情報を取得
        user_post_list = user_post_model.find_user_posts(user_id)

        # _idを文字列に変換
        for user_post in user_post_list:
            user_post["_id"] = str(user_post['_id'])

        return jsonify({
            "code": 200,
            "posts": user_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")
