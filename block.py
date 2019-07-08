import requests
from requests_oauthlib import OAuth1
import json

KEYS_FILE = 'KEYS.json'
BASE_URL = 'https://api.twitter.com/1.1'
FOLLOWERS_ID_PATH = '/followers/ids.json'
BLOCK_IDS_PATH = '/blocks/ids.json'
BLOCK_CREATE_PATH = '/blocks/create.json'
BLOCK_DESTROY_PATH = '/blocks/destroy.json'


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
    return requests.get(url, auth=AUTH).json()['ids']


def get_blocks():
    url = BASE_URL + BLOCK_IDS_PATH
    return requests.get(url, auth=AUTH).json()['ids']


def create_block(id):
    user_id_param = 'user_id='
    url = BASE_URL + BLOCK_CREATE_PATH + '?' + user_id_param + str(id)
    requests.post(url, auth=AUTH)


def create_blocks(ids):
    for id in ids:
        create_block(id)


def destory_block(id):
    user_id_param = 'user_id='
    url = BASE_URL + BLOCK_DESTROY_PATH + '?' + user_id_param + str(id)
    requests.post(url, auth=AUTH)


def destroy_blocks(ids):
    for id in ids:
        destory_block(id)


def block():
    follower_ids = get_followers()
    create_blocks(follower_ids)
    blocked_ids = get_blocks()
    destroy_blocks(blocked_ids)


# TODO: cursoring
# TODO: check for privacy settings
# TODO: follow back maybe


if __name__ == "__main__":
    block()