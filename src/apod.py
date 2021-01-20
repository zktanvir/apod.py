import requests
from errors.errors import NoApiKey, InvalidApiKey

class Client:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def fetch(self):
        if self.api_key is None:
            raise NoApiKey()
        resp = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}")
        data = resp.json()
        if "error" in data:
            if data['error']['code'] == 'API_KEY_INVALID':
                raise InvalidApiKey()
        return data

