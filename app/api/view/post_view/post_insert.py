from flask import Blueprint, request, jsonify, abort
from api.models import PostModel
from datetime import datetime

# ルーティング設定
post_insert = Blueprint("post_insert", __name__)

@post_insert.route("", methods=["POST"])
def insert_post():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()
    print(requested_data)

    # 必須フィールドのチェック
    required_fields = ["user_id", "tag_id", "post_image_url", "event_name", "comment"]
    for field in required_fields:
        if field not in requested_data:
            abort(400, f"{field} is a required field")

    # PostModelクラスのインスタンスを生成
    post_model = PostModel()

    # 投稿データの作成
    post_data = {
        "user_id": requested_data["user_id"],
        "tag_id": requested_data["tag_id"],
        "post_image_url": requested_data["post_image_url"],
        "event_name": requested_data["event_name"],
        "comment": requested_data["comment"],
        "post_date": datetime.now(),  # 現在の日付を保存
        "like": [], # いいね初期状態は空
    }

    try:
        # 投稿データを保存
        post_model.insert_post(post_data)

        return jsonify({
            "code": 200,
            "message": "Post successfully inserted",
        })
    except Exception as e:
        abort(500, f"Error occurred while inserting post: {e}")
