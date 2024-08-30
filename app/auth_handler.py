import bcrypt
from firebase_admin import auth

def verify_username_and_password(username, password):
    user_info = get_user_info_by_username(username)
    if user_info and bcrypt.checkpw(password.encode('utf-8'), user_info['password'].encode('utf-8')):
        email = user_info['email']
        try:
            user_record = auth.get_user_by_email(email)
            return user_record.uid
        except Exception as e:
            print(f"ユーザー名が違います: {e}")
            return None
    return None

def verify_phone_and_password(phone, password):
    user_info = get_user_info_by_phone(phone)
    if user_info and bcrypt.checkpw(password.encode('utf-8'), user_info['password'].encode('utf-8')):
        try:
            user_record = auth.get_user_by_phone_number(phone)
            return user_record.uid
        except Exception as e:
            print(f"電話番号が違います: {e}")
            return None
    return None
