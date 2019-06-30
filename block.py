import requests
from requests_oauthlib import OAuth1
import json

KEYS_FILE = 'KEYS.json'
BASE_URL = 'https://api.twitter.com/1.1'
FOLLOWERS_ID_PATH = '/followers/ids.json'


def load_keys(key_name, file_name=KEYS_FILE):
    with open(file_name) as json_file:
        return json.load(json_file)[key_name]


API_KEY = load_keys('API_KEY')
API_SECRET_KEY = load_keys('API_SECRET_KEY')
ACCESS_TOKEN = load_keys('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = load_keys('ACCESS_TOKEN_SECRET')
SCREEN_NAME = load_keys('SCREEN_NAME')
AUTH = OAuth1(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


def get_followers():
    screen_name_param = 'screen_name='
    url = BASE_URL + FOLLOWERS_ID_PATH + '?' + screen_name_param + SCREEN_NAME
    return requests.get(url, auth=AUTH).json()


if __name__ == "__main__":
    follower_ids = get_followers()
    print(follower_ids)
