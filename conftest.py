import pytest
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RAWG_API_KEY')
BASE_URL = 'https://api.rawg.io/api'

@pytest.fixture
def api_params():
    return {'key': API_KEY}

@pytest.fixture
def base_url():
    return BASE_URL