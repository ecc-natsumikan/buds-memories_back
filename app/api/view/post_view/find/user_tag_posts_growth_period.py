from flask import Blueprint, request, jsonify, abort
from api.models import UserPostModel

# ルーティング設定
user_tag_posts_growth_period_find = Blueprint("user_tag_posts_growth_period_find", __name__)

@user_tag_posts_growth_period_find.route("", methods=["POST"])
def find_user_tag_posts_growth_period():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(user_id, tag_id, grow_item_id)
    if "user_id" not in requested_data:
        abort(400, "user_id is required")
    if "tag_id" not in requested_data:
        abort(400, "tag_id is required")
    if "grow_item_id" not in requested_data:
        abort(400, "grow_item_id is required")

    # user_id, tag_id, grow_item_idを取得
    user_id = requested_data["user_id"]
    tag_id = requested_data["tag_id"]
    grow_item_id = requested_data["grow_item_id"]
    # UserModelクラスのインスタンスを生成
    user_model = UserPostModel()

    try:
        # 特定のユーザーの特定のタグをつけた投稿情報を取得
        user_tag_post_list = user_model.find_user_tag_posts_growth_period(user_id, tag_id, grow_item_id)

        # _idを文字列に変換
        for user_tag_post in user_tag_post_list:
            user_tag_post["_id"] = str(user_tag_post['_id'])

        return jsonify({
            "code": 200,
            "user_tag_post": user_tag_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")