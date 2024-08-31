from flask import Blueprint, request, jsonify, abort
from api.models import GrowItemModel

# ルーティング設定
grow_item_find = Blueprint("grow_item_find", __name__)

@grow_item_find.route("", methods=["POST"])
def find_grow_item():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(tag_id)
    if "tag_id" not in requested_data:
        abort(400, "tag_id is required")

    tag_id = requested_data["tag_id"]

    # GrowItemModelクラスのインスタンスを生成
    grow_item_model = GrowItemModel()

    try:
        # 特定のタグIDに合致する育成アイテムを取得
        grow_item = grow_item_model.find_grow_item(tag_id)

        if not grow_item:
            abort(404, "No grow item found for the provided tag_id")

        # _idやtag_idを文字列に変換して返す
        grow_item["_id"] = str(grow_item["_id"])
        grow_item["tag_id"] = str(grow_item["tag_id"])

        return jsonify({
            "code": 200,
            "grow_item": grow_item
        })
    except Exception as e:
        abort(500, f"Error occurred while fetching grow item: {e}")
