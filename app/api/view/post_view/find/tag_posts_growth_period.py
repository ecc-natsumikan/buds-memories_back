from flask import Blueprint, request, jsonify, abort
from api.models import PostModel

# ルーティング設定
tag_posts_growth_period_find = Blueprint("tag_posts_growth_period_find", __name__)

@tag_posts_growth_period_find.route("", methods=["POST"])
def find_tag_posts_growth_period():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(tag_idとgrow_item_id)
    if "tag_id" not in requested_data:
        abort(400, "tag_id is required")
    if "grow_item_id" not in requested_data:
        abort(400, "grow_item_id is required")

    # tag_idとgrow_item_idを取得
    tag_id = requested_data["tag_id"]
    grow_item_id = requested_data["grow_item_id"]
    # PostModelクラスのインスタンスを生成
    post_model = PostModel()

    try:
        # 特定のタグの投稿情報を取得
        post_by_tag_list = post_model.find_tag_posts_growth_period(tag_id , grow_item_id)

        # _idを文字列に変換
        for tag_post in post_by_tag_list:
            tag_post["_id"] = str(tag_post['_id'])

        return jsonify({
            "code": 200,
            "tag_post": post_by_tag_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")
