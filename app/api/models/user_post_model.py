from flask import abort
from api.database import get_db
from bson import ObjectId

class UserPostModel:
    def __init__(self):
        self.db = get_db()
        self.post_collection = self.db['Post']  # 'Post' コレクションにアクセス
        self.growth_collection = self.db['GrowItem']  # 'GrowItem' コレクションにアクセス

    # 特定のユーザーの投稿を取得
    def find_user_posts(self, user_id):
        try:
            pipeline = [
                {"$match": {"user_id": user_id}},
                {
                    "$addFields": {
                        "tag_id": {"$toObjectId": "$tag_id"}  # 文字列のtag_idをObjectIdに変換
                    }
                },
                {
                    "$lookup": {
                        "from": "Tag",
                        "localField": "tag_id",
                        "foreignField": "_id",
                        "as": "tag_info"
                    }
                },
                { "$unwind": "$tag_info" },
                {
                    "$project": {
                        "_id": 1,
                        "tag_name": "$tag_info.tag_name",
                        "post_image_url": 1,
                        "event_name": 1,
                        "comment": 1,
                        "post_date": 1
                    }
                }
            ]            
            # 投稿情報を取得
            user_post_list = list(self.post_collection.aggregate(pipeline))

            if not user_post_list:
                abort(404, "Posts not found")
            
            return user_post_list
        
        except Exception as e:
            abort(500, f"Error occurred while finding posts: {e}")

    # 特定のユーザーの特定のタグをつけた投稿の取得
    def find_user_tag_posts(self, user_id, tag_id):
        try:
            pipeline = [
                {"$match": {"user_id": user_id, "tag_id": tag_id}},
                {
                    "$addFields": {
                        "tag_id": {"$toObjectId": "$tag_id"}  # 文字列のtag_idをObjectIdに変換
                    }
                },
                {
                    "$lookup": {
                        "from": "Tag",
                        "localField": "tag_id",
                        "foreignField": "_id",
                        "as": "tag_info"
                    }
                },
                { "$unwind": "$tag_info" },
                {
                    "$project": {
                        "_id": 1,
                        "tag_name": "$tag_info.tag_name",
                        "post_image_url": 1,
                        "event_name": 1,
                        "comment": 1,
                        "post_date": 1
                    }
                }
            ]            
            # 投稿情報を取得
            user_tag_post_list = list(self.post_collection.aggregate(pipeline))

            if not user_tag_post_list:
                abort(404, "Posts not found")
            
            return user_tag_post_list
        
        except Exception as e:
            abort(500, f"Error occurred while finding posts: {e}")

    
    #特定のユーザーの特定のタグをつけた育成期間内の投稿の取得
    def find_user_tag_posts_growth_period(self, user_id, tag_id, grow_item_id):
        if isinstance(grow_item_id, str):
            grow_item_id = ObjectId(grow_item_id)

        try:
            # 育成アイテムのデータを取得
            grow_item = self.grow_item_collection.find_one({"_id": grow_item_id, "tag_id": tag_id})
            if not grow_item:
                abort(404, "Grow item not found")

            # 育成期間の開始日と終了日を取得
            start_date = grow_item["start_date"]
            end_date = grow_item["end_date"]

            # 投稿データを育成期間内で絞り込み
            pipeline = [
                {"$match": {
                    "tag_id": tag_id,
                    "user_id": user_id,
                    "post_date": {"$gte": start_date, "$lte": end_date}
                }},
                {
                    "$addFields": {
                        "tag_id": {"$toObjectId": "$tag_id"}  # 文字列のtag_idをObjectIdに変換
                    }
                },
                {
                    "$lookup": {
                        "from": "Tag",
                        "localField": "tag_id",
                        "foreignField": "_id",
                        "as": "tag_info"
                    }
                },
                {"$unwind": "$tag_info"},
                {
                    "$project": {
                        "_id": 1,
                        "tag_name": "$tag_info.tag_name",
                        "post_image_url": 1,
                        "event_name": 1,
                        "comment": 1,
                        "post_date": 1
                    }
                }
            ]
            
            result = list(self.post_collection.aggregate(pipeline))
            if not result:
                abort(404, "Posts not found during the grow period")
            
            return result

        except Exception as e:
            abort(500, f"Error occurred while retrieving posts: {e}")



