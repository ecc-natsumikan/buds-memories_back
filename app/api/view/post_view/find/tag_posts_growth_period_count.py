#特定のタグの育成期間内の投稿数を取得する   
from flask import Blueprint, request, jsonify, abort
from api.models import PostModel

# ルーティング設定
tag_posts_growth_period_count_find = Blueprint("tag_posts_growth_period_count_find", __name__)

@tag_posts_growth_period_count_find.route("", methods=["POST"])

def find_tag_posts_growth_period_count():
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
        tag_post_count = post_model.find_tag_posts_growth_period_count(tag_id , grow_item_id)

        return jsonify({
            "code": 200,
            "tag_post_count": len(tag_post_count)
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")