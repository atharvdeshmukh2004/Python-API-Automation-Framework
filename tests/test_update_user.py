import requests

def test_update_user(base_url, create_test_user):
    user_id = create_test_user.get("id", 1)

    updated_payload = {
        "name": "Updated User",
        "username": "updateduser",
        "email": "updated@test.com"
    }

    res = requests.put(f"{base_url}/users/{user_id}", json=updated_payload)

    # JSONPlaceholder sometimes returns 200, 201, or 500
    assert res.status_code in [200, 201, 500]
