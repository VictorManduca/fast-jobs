import json


def create_payload():
    return {
        "username": "VictorHotmail",
        "email": "victor@hotmail.com",
        "password": "pass"
    }


def test_create_user(client, normal_user_token_headers):
    data = create_payload()
    response = client.post("/user", json.dumps(data), headers=normal_user_token_headers)

    assert response.status_code == 201


def test_error_duplicated_user(client, normal_user_token_headers):
    data = create_payload()
    response = client.post("/user", json.dumps(data), headers=normal_user_token_headers)

    assert response.status_code == 400


def test_error_wrong_payload(client, normal_user_token_headers):
    data = {}
    response = client.post("/user", json.dumps(data), headers=normal_user_token_headers)

    assert response.status_code == 422

