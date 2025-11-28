import requests


def test_delete_user(base_url):
    user_id = 1
    res = requests.delete(f"{base_url}/users/{user_id}")
    assert res.status_code in [200, 204]
