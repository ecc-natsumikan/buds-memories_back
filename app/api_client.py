import requests

def get_user_info_by_username(username):
    response = requests.get(f'http://{IP_ADDRESS}:{PORT}/api/user/select', params={'username': username})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user info: {response.status_code}")
        return None

def get_user_info_by_phone(phone):
    response = requests.get(f'http://{IP_ADDRESS}:{PORT}/api/user/select', params={'phone': phone})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching user info: {response.status_code}")
        return None
