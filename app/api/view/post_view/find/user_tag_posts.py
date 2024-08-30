from flask import Blueprint, request, jsonify, abort
from api.models import UserPostModel

# ルーティング設定
user_tag_posts_find = Blueprint("user_tag_posts_find", __name__)

@user_tag_posts_find.route("", methods=["POST"])
def find_user_tag_posts():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(user_id, tag_id)
    if "user_id" not in requested_data:
        abort(400, "user_id is required")
    if "tag_id" not in requested_data:
        abort(400, "tag_id is required")

    # user_idとtag_idを取得
    user_id = requested_data["user_id"]
    tag_id = requested_data["tag_id"]
    # UserPostModelクラスのインスタンスを生成
    user_post_model = UserPostModel()

    try:
        # 特定のユーザーの特定のタグの投稿情報を取得
        user_tag_post_list = user_post_model.find_user_tag_posts(user_id, tag_id)

        # _idを文字列に変換
        for user_tag_post in user_tag_post_list:
            user_tag_post["_id"] = str(user_tag_post['_id'])

        return jsonify({
            "code": 200,
            "user_tag_post": user_tag_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")