from datetime import datetime
from api.database import get_db
from bson.objectid import ObjectId

class GrowItemModel:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['GrowItem']  # GrowItemコレクションにアクセス

    # 現在の日付が育成期間内かつ、タグIDが一致する育成アイテムを取得
    def find_grow_item(self, tag_id):
        current_date = datetime.now()
        try:
            
            query = {
                "tag_id": tag_id,
                "start_date": {"$lte": current_date},
                "end_date": {"$gte": current_date},
            }
            projection = {
                "_id": 1,
                "tag_id": 1,
                "grow_item_type": 1,
                "grow_item_image_url": 1,
                "season": 1,
                "number_of_required_posts": 1,
                "start_date": 1,
                "end_date": 1
            }
            grow_item = self.collection.find_one(query, projection)
            return grow_item
        except Exception as e:
            raise Exception(f"Error occurred while fetching GrowItem: {e}")


    # 成長度の監視
    def find_grow_item_stage_check_update(self, grow_item_id, progress):
        try:
            # 成長度の監視に必要なフィールドのみ取得
            projection = {
                "_id": 1,
                "tag_id": 1,
                "grow_item_type": 1,
                "grow_item_image_url": 1,
                "season": 1,
                "number_of_required_posts": 1,
                "start_date": 1,
                "end_date": 1,
                "stages": 1
            }

            #クライアントに返す育成アイテムフィールド
            grow_item = {
                "_id": 1,
                "tag_id": 1,
                "grow_item_type": 1,
                "grow_item_image_url": 1,
                "season": 1,
                "number_of_required_posts": 1,
                "start_date": 1,
                "end_date": 1
            }

            # GrowItemコレクションからgrow_item_idに一致する育成アイテムを取得
            grow_item = self.collection.find_one({"_id": ObjectId(grow_item_id)}, projection)
            # 成長度が最大の場合はそのままの育成アイテムを返す
            if progress >= grow_item["stages"][-1]["progress_threshold"]:
                return grow_item
            # 成長度が次の成長度の範囲内にあるかを確認
            for stage in grow_item["stages"]:
                if progress < stage["progress_threshold"]:
                    # 次の成長段階のimage_pathに変更
                    grow_item["grow_item_image_url"] = stage["stage_image_url"]
                    return grow_item
                return grow_item
        except Exception as e:
            raise Exception(f"Error occurred while monitoring growth: {e}")
