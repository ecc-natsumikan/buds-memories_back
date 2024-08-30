#いいねの削除
from flask import Blueprint, request, jsonify, abort
from api.models import LikePostModel

# ルーティング設定
posts_like_delete = Blueprint("posts_like_delete", __name__)

@posts_like_delete.route("", methods=["POST"])
def delete_posts_like():
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
        # いいねした投稿情報を削除
        like_post_model.delete_posts_like(user_id, post_id)

        return jsonify({
            "code": 200,
            "message": "Post successfully unliked",
        })
    except Exception as e:
        abort(500, f"Error occurred while unliking post: {e}")