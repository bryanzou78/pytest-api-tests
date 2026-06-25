import requests
import pytest

def test_get_game_results(base_url, api_params):
    response = requests.get(f'{base_url}/games', params=api_params)
    data = response.json()
    assert response.status_code == 200
    assert 'results' in data
    assert len(data['results']) > 0

def test_get_game_by_id(base_url, api_params):
    response = requests.get(f'{base_url}/games/3498', params=api_params)
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Grand Theft Auto V'
    assert data['rating'] == 4.47

def test_get_invalid_game_returns_404(base_url, api_params):
    response = requests.get(f'{base_url}/games/9999999', params=api_params)
    data = response.json()
    assert response.status_code == 404
    assert 'detail' in data

@pytest.mark.parametrize('game_id', [3498, 5286, 4200])
def test_game_id_exists(game_id, base_url, api_params):
    response = requests.get(f'{base_url}/games/{game_id}', params=api_params)
    assert response.status_code == 200