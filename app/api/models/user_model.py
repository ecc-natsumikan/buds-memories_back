from flask import abort
from api.database import get_db

class UserModel:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db['User']  # 'User' コレクションにアクセス

    # ユーザー情報の登録
    def create_user(self, user_data):
        try:
            result = self.collection.insert_one(user_data)
            return result
        except Exception as e:
            abort(500, f"Error occurred while creating user: {e}")

    # ユーザー情報の取得
    def find_user(self, user_identification_info):
        try:
            # user_identification_info がuser_idの場合は _id で取得し、なければ phone_number で取得
            if isinstance(user_identification_info, str):
                user_data = self.collection.find_one({"_id": user_identification_info})
                if user_data is None:
                    user_data = self.collection.find_one({"phone_number": user_identification_info})
            if user_data is None:
                abort(400, "User not found")
            return user_data
        except Exception as e:
            abort(500, f"Error occurred while finding user: {e}")

    # ユーザー情報の更新
    def update_user(self, user_id, update_data):
        try:
            result = self.collection.update_one({"_id": user_id}, {"$set": update_data})
            print(result)
            if result.matched_count == 0:
                abort(400, "User not found")
            return result
        except Exception as e:
            abort(500, f"Error occurred while updating user: {e}")

    # ユーザー情報の削除
    def delete_user(self, user_id):
        try:

            result = self.collection.delete_one({"_id": user_id})
            if result.deleted_count == 0:
                abort(400, "User not found")
            return result
        except Exception as e:
            abort(500, f"Error occurred while deleting user: {e}")
