import json


def create_payload():
    return {
        "username": "VictorHotmail",
        "email": "victor@hotmail.com",
        "password": "pass"
    }


def test_create_user(client):
    data = create_payload()
    response = client.post("/user", json.dumps(data))

    assert response.status_code == 201


def test_error_duplicated_user(client):
    data = create_payload()
    response = client.post("/user", json.dumps(data))

    assert response.status_code == 400


def test_error_wrong_payload(client):
    data = {}
    response = client.post("/user", json.dumps(data))

    assert response.status_code == 422

