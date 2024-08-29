import firebase_admin
from firebase_admin import auth
from pymongo import MongoClient
import bcrypt

# Firebase初期化
cred = firebase_admin.credentials.Certificate('firebase_credentials.json')
firebase_admin.initialize_app(cred)

# MongoDBクライアントの設定
client = MongoClient('mongodb://localhost:27017/')
# クライアントとdbを後で書き換える
db = client['your_database_name']
users_collection = db['users']

def verify_username_and_password(username, password):
    user = users_collection.find_one({"username": username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        email = user['email']
        try:
            user_record = auth.get_user_by_email(email)
            return user_record.uid
        except Exception as e:
            print(f"メールアドレスが設定されてません {e}")
            return None
    return None

def verify_phone_and_password(phone, password):
    user = users_collection.find_one({"phone": phone})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        try:
            user_record = auth.get_user_by_phone_number(phone)
            return user_record.uid
        except Exception as e:
            print(f"携帯番号が違います {e}")
            return None
    return None
