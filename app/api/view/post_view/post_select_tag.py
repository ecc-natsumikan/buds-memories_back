from flask import Blueprint, request, jsonify, abort
from api.models import PostModel

# ルーティング設定
post_select_tag = Blueprint("post_select_tag", __name__)

@post_select_tag.route("", methods=["POST"])
def select_tag_post():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(tag_id)
    if not "tag_id" in requested_data:
        abort(400, "tag_id is a required field")

    # tag_idを取得
    tag_id = requested_data["tag_id"]
    # UserModelクラスのインスタンスを生成
    tag_post_model = PostModel()

    try:
        # 特定のタグの投稿情報を取得
        tag_post_list = tag_post_model.find_tag_post(tag_id)

        # _idを文字列に変換
        for tag_post in tag_post_list:
            tag_post["_id"] = str(tag_post['_id'])

        return jsonify({
            "code": 200,
            "tag_post": tag_post_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting post: {e}")
