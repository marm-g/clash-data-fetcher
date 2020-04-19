import requests


class RiotApi:
    base_api_url = 'https://na1.api.riotgames.com/lol'

    def __init__(self, api_key):
        self.api_key = api_key

    def make_request(self, api_endpoint, type='get'):
        headers = {"X-Riot-Token": self.api_key}
        return requests.get('{}/{}'.format(self.base_api_url, api_endpoint), headers=headers)
