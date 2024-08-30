from flask import Blueprint, jsonify, abort
from api.models import TagModel

# ルーティング設定
tags_find = Blueprint("tag_find", __name__)

@tags_find.route("", methods=["POST"])
def find_tags():
    # 現在の月を取得
    import datetime
    month = datetime.datetime.now().month

    # 季節を判定
    if month >= 3 and month <= 5:
        tags_season = "spring"
    elif month >= 6 and month <= 8:
        tags_season = "summer"
    elif month >= 9 and month <= 11:
        tags_season = "autumn"
    else:
        tags_season = "winter"

    # TagModelクラスのインスタンスを生成
    tags_model = TagModel()

    try:
        # 該当する季節のタグ情報を取得
        tags_data_list = tags_model.find_tag(tags_season)
        # _idを文字列に変換
        for tags_data in tags_data_list:
            tags_data["_id"] = str(tags_data["_id"])

        return jsonify({
            "code": 200,
            "tags": tags_data_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting tags: {e}")
