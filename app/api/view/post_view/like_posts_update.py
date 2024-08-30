from flask import Blueprint, request, jsonify, abort
from api.models import LikePostModel

# ルーティング設定
like_post_update = Blueprint("like_post_update", __name__)

@like_post_update.route("", methods=["POST"])
def update_like_post():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(user_id, post_id)
    if "user_id" not in requested_data:
        abort(400, "user_id is required")
    if "post_id" not in requested_data:
        abort(400, "post_id is required")

    # user_idとpost_idを取得
    user_id = requested_data["user_id"]
    post_id = requested_data["post_id"]
    # LikePostModelクラスのインスタンスを生成
    like_post_model = LikePostModel()

    try:
        # いいねした投稿情報を保存
        like_post_model.update_like_posts(user_id, post_id)

        return jsonify({
            "code": 200,
            "message": "Post successfully liked",
        })
    except Exception as e:
        abort(500, f"Error occurred while liking post: {e}")