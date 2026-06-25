import requests
import pytest

@pytest.mark.parametrize('genre_names', ['action', 'role-playing-games-rpg', 'shooter', 'strategy'])
def test_genres_return_results(genre_names, base_url, api_params):
    response = requests.get(f'{base_url}/games', params={**api_params, 'genres': genre_names})
    data = response.json()
    assert response.status_code == 200
    assert 'results' in data
    assert len(data['results']) > 0