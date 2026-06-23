import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RAWG_API_KEY')
BASE_URL = 'https://api.rawg.io/api'

def test_get_game_by_id():
    response = requests.get(f'{BASE_URL}/games/3498', params={'key': API_KEY})
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Grand Theft Auto V'
    assert data['rating'] == 4.47

def test_get_invalid_game_returns_404():
    response = requests.get(f'{BASE_URL}/games/invalid_id', params={'key': API_KEY})
    data = response.json()
    assert response.status_code == 404
    assert 'detail' in data

def test_get_game_results():
    response = requests.get(f'{BASE_URL}/games', params={'key': API_KEY})
    data = response.json()
    assert response.status_code == 200
    assert 'results' in data
    assert len(data['results']) > 0