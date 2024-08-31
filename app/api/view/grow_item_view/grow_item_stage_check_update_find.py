from flask import Blueprint, request, jsonify, abort
from api.models import GrowItemModel

# ルーティング設定
grow_item_stage_check_update_find = Blueprint("grow_item_stage_check_update_find", __name__)

@grow_item_stage_check_update_find.route("", methods=["POST"])
def find_grow_item_stage_check_update():
    # リクエストからJSONデータを取得
    requested_data = request.get_json()

    # 必須フィールドのチェック(progress , grow_item_id)
    if "progress" not in requested_data or "grow_item_id" not in requested_data:
        abort(400, "progress and grow_item_id are required")

    progress = requested_data["progress"]
    grow_item_id = requested_data["grow_item_id"]

    # GrowItemModelクラスのインスタンスを生成
    grow_item_model = GrowItemModel()

    try:
        # 成長度の監視
        grow_item = grow_item_model.find_grow_item_stage_check_update(grow_item_id, progress)

        if not grow_item:
            abort(404, "No grow item found for the provided grow_item_id")

        # _idやtag_idを文字列に変換して返す
        grow_item["_id"] = str(grow_item["_id"])

        return jsonify({
            "code": 200,
            "grow_item": grow_item
        })
    except Exception as e:
        abort(500, f"Error occurred while updating grow item: {e}")