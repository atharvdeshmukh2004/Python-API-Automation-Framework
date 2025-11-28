import requests


def test_create_user(base_url):
    payload = {
        "name": "New User",
        "username": "newuser123",
        "email": "new@user.com"
    }
    res = requests.post(f"{base_url}/users", json=payload)
    assert res.status_code == 201
    body = res.json()
    assert body["name"] == payload["name"]
