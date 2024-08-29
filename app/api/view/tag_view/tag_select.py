from flask import Blueprint, jsonify, abort
from api.models import TagModel

# ルーティング設定
tag_select = Blueprint("tag_select", __name__)

@tag_select.route("", methods=["POST"])
def select_tag():
    # 現在の月を取得
    import datetime
    month = datetime.datetime.now().month

    # 季節を判定
    if month >= 3 and month <= 5:
        tag_season = "spring"
    elif month >= 6 and month <= 8:
        tag_season = "summer"
    elif month >= 9 and month <= 11:
        tag_season = "autumn"
    else:
        tag_season = "winter"

    # TagModelクラスのインスタンスを生成
    tag_model = TagModel()

    try:
        # 該当する季節のタグ情報を取得
        tag_data_list = tag_model.find_tag(tag_season)
        # _idを文字列に変換
        for tags_data in tag_data_list:
            tags_data["_id"] = str(tags_data["_id"])

        return jsonify({
            "code": 200,
            "tags": tag_data_list
        })
    except Exception as e:
        abort(500, f"Error occurred while selecting tags: {e}")
