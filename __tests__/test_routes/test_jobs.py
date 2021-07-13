import json


def create_payload():
    return {
        "title": "SDE 1 Yahoo",
        "company": "test Yahoo",
        "company_url": "https://wwww.yahoo.com",
        "location": "USA, NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }


def create_payload_update_job():
    return {
        "title": "[updated] SDE 1 Yahoo"
    }


def test_create_job(client, normal_user_token_headers):
    data = create_payload()
    response = client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    assert response.status_code == 201


def test_wrong_payload(client, normal_user_token_headers):
    data = {}
    response = client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    assert response.status_code == 422


def test_retrieve_job(client, normal_user_token_headers):
    data = create_payload()
    client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    response = client.get("/job/1", headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
    assert response.json()["company"] == "test Yahoo"
    assert response.json()["company_url"] == "https://wwww.yahoo.com"
    assert response.json()["description"] == "Testing"
    assert response.json()["location"] == "USA, NY"
    assert response.json()["date_posted"] == "2022-07-20"


def test_retrieve_all_jobs(client, normal_user_token_headers):
    data = create_payload()
    client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    response = client.get("/job", headers=normal_user_token_headers)
    assert response.status_code == 200


def test_retrieve_all_active_jobs(client, normal_user_token_headers):
    data = create_payload()
    client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    response = client.get("/job/all/active", headers=normal_user_token_headers)
    assert response.status_code == 200


def test_update_job(client, normal_user_token_headers):
    data_post = create_payload()
    data_patch = create_payload_update_job()

    client.post("/job", json.dumps(data_post), headers=normal_user_token_headers)
    response_patch = client.patch("/job/1", json.dumps(data_patch), headers=normal_user_token_headers)
    response_get = client.get("/job/1", headers=normal_user_token_headers)

    assert response_patch.status_code == 200
    assert response_get.status_code == 200
    assert response_get.json()["title"] == "[updated] SDE 1 Yahoo"


def test_update_job_wrong_id(client, normal_user_token_headers):
    data_post = create_payload()
    data_patch = create_payload_update_job()

    client.post("/job", json.dumps(data_post), headers=normal_user_token_headers)
    response_patch = client.patch("/job/2000000", json.dumps(data_patch), headers=normal_user_token_headers)

    assert response_patch.status_code == 400


def test_delete_job(client, normal_user_token_headers):
    data = create_payload()
    client.post("/job", json.dumps(data), headers=normal_user_token_headers)

    response = client.delete("/job/1", headers=normal_user_token_headers)
    assert response.status_code == 200


def test_delete_job_wrong_id(client, normal_user_token_headers):
    response = client.delete("/job/1", headers=normal_user_token_headers)
    assert response.status_code == 400
