import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv
from riot_api import RiotApi


# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

user_id = '57Oc7FxFB2rQVsTfQJln5EIbhhr_A75uXoKLxqRk0wtMTw'
api = RiotApi(os.getenv('RIOT_API_KEY'))
print(api.api_key)
headers = {"X-Riot-Token": os.getenv('RIOT_API_KEY')}
clash_match_id = 700

base_api_url = 'https://na1.api.riotgames.com/lol'
response = api.make_request(
    'match/v4/matchlists/by-account/{}'.format(user_id))
# response = requests.get(
# '{}/match/v4/matchlists/by-account/{}'.format(base_api_url, user_id), headers=headers)
data = response.json()
matches = [match for match in data['matches'] if match['queue'] == 700]
for match in matches:
    response = api.make_request(
        'match/v4/matches/{}'.format(match['gameId']))
    data = response.json()
    print('Gamers in this game: {}'.format(', '.join(
        [participant['player']['summonerName'] for participant in data['participantIdentities']])))
