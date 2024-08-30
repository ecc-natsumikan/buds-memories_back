#いいねした投稿の取得
from flask import Blueprint, request, jsonify, abort
from api.models import LikePostModel

# ルーティング設定
like_posts_find = Blueprint("like_posts_find", __name__)

@like_posts_find.route("", methods=["POST"])
def find_like_posts():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(user_id)
    if "user_id" not in requested_data:
        abort(400, "user_id is required")

    # user_idを取得
    user_id = requested_data["user_id"]
    # LikePostModelクラスのインスタンスを生成
    like_post_model = LikePostModel()

    try:
        # いいねした投稿情報を取得
        like_post_list = like_post_model.find_like_posts(user_id)

        # _idを文字列に変換
        for like_post in like_post_list:
            like_post["_id"] = str(like_post['_id'])

        return jsonify({
            "code": 200,
            "like_post": like_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")