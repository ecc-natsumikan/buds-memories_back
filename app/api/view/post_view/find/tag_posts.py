from flask import Blueprint, request, jsonify, abort
from api.models import PostModel

# ルーティング設定
tag_posts_find = Blueprint("tag_posts_find", __name__)

@tag_posts_find.route("", methods=["POST"])
def find_tag_posts():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(tag_id)
    if not "tag_id" in requested_data:
        abort(400, "tag_id is a required field")

    # tag_idを取得
    tag_id = requested_data["tag_id"]
    # PostModelクラスのインスタンスを生成
    post_model = PostModel()

    try:
        # 特定のタグの投稿情報を取得
        tag_post_list = post_model.find_tag_posts(tag_id)

        # _idを文字列に変換
        for tag_post in tag_post_list:
            tag_post["_id"] = str(tag_post['_id'])

        return jsonify({
            "code": 200,
            "tag_post": tag_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")
