import requests


def test_get_all_users(base_url):
    res = requests.get(f"{base_url}/users")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
