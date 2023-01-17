import json


def test_create_user(user):
    data = {
        "username": "test1",
        "email": "testuser@du.com",
        "password": "testing",
    }
    response = user.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@du.com"
    assert response.json()["is_active"] == True
