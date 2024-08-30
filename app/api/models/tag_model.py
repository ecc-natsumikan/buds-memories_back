from flask import abort
from api.database import get_db

class TagModel:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['Tag']  # 'Tag' コレクションにアクセス

    # タグ情報の取得
    def find_tag(self, tag_season):
        try:
            # tag_season に一致するタグ情報を全て取得
            tags_data_list = list(self.collection.find({"season": tag_season}))
            if tags_data_list is None:
                abort(400, "Tag not found")
            return tags_data_list
        except Exception as e:
            abort(500, f"Error occurred while finding tag: {e}")