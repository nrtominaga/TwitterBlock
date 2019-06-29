import requests
import json

KEYS_FILE = 'KEYS.json'


def load_api_key(key_name, file_name=KEYS_FILE):
    with open(file_name) as json_file:
        return json.load(json_file)[key_name]


API_KEY = load_api_key('API_KEY')
API_SECRET_KEY = load_api_key('API_SECRET_KEY')
ACCESS_TOKEN = load_api_key('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = load_api_key('ACCESS_TOKEN_SECRET')


if __name__ == "__main__":
    print("Hello World")
