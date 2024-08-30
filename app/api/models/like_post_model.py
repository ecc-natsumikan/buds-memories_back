from flask import abort
from api.database import get_db
from bson.objectid import ObjectId

class LikePostModel:
    def __init__(self):
        self.db = get_db()
        self.post_collection = self.db['Post']  # 'Post' コレクションにアクセス

    # いいねした投稿データの保存
    def update_like_posts(self, post_id, user_id):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$addToSet": {"like": {"user_id": user_id}}}
            )

            if result.matched_count == 0:
                abort(404, "Post not found")
            
            return result
        
        except Exception as e:
            abort(500, f"Error occurred while adding like: {e}")


    # いいねした投稿を取得
    def find_like_posts(self, user_id):
        try:
            # user_id に一致する投稿情報を全て取得
            like_post_list = list(self.post_collection.find({"like": user_id}))
            if like_post_list is None:
                abort(400, "Like post not found")

            return like_post_list
        
        except Exception as e:
            abort(500, f"Error occurred while finding like post data: {e}")

    #投稿のいいね削除
    def delete_posts_like(self, post_id, user_id):
        try:
            result = self.collection.update_one(
                {"_id": ObjectId(post_id)},
                {"$pull": {"like": {"user_id": user_id}}}
            )

            if result.matched_count == 0:
                abort(404, "Post not found")
            
            return result
        
        except Exception as e:
            abort(500, f"Error occurred while deleting like: {e}")