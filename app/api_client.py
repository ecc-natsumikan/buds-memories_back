import requests
from app.config import Config

def get_user_info_by_username(username):
    response = requests.get(f'http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/api/user/find', params={'user_name': username})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user info: {response.status_code}")
        return None

def get_user_info_by_phone(phone):
    response = requests.get(f'http://{Config.FLASK_HOST}:{Config.FLASK_PORT}/api/user/find', params={'phone_number': phone})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user info: {response.status_code}")
        return None
