import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def create_test_user(base_url):
    payload = {
        "name": "Atharv Test User",
        "username": "atharv123",
        "email": "atharv@test.com"
    }
    res = requests.post(f"{base_url}/users", json=payload)
    return res.json()
