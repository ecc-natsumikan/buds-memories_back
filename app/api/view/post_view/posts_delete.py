from flask import Blueprint, request, jsonify, abort
from api.models import PostModel


# ルーティング設定
posts_delete = Blueprint("posts_delete", __name__)

@posts_delete.route("", methods=["POST"])

def delete_posts():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(post_id)
    if not "post_id" in requested_data:
        abort(400, "post_id is a required field")

    # post_idを取得
    post_id = requested_data["post_id"]
    # PostModelクラスのインスタンスを生成
    post_model = PostModel()

    try:
        # 投稿情報を削除
        post_model.delete_posts(post_id)

        return jsonify({
            "code": 200,
            "message": "Post successfully deleted",
        })
    except Exception as e:
        abort(500, f"Error occurred while deleting post: {e}")