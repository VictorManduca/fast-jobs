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

def test_create_job(client):
    data = create_payload()
    response = client.post("/job", json.dumps(data))

    assert response.status_code == 201


def test_wrong_payload(client):
    data = {}
    response = client.post("/job", json.dumps(data))

    assert response.status_code == 422


def test_retrieve_job(client):
    data = create_payload()
    client.post("/job", json.dumps(data))

    response = client.get("/job/1")
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
    assert response.json()["company"] == "test Yahoo"
    assert response.json()["company_url"] == "https://wwww.yahoo.com"
    assert response.json()["description"] == "Testing"
    assert response.json()["location"] == "USA, NY"
    assert response.json()["date_posted"] == "2022-07-20"


def test_retrieve_all_jobs(client):
    data = create_payload()
    client.post("/job", json.dumps(data))

    response = client.get("/job")
    assert response.status_code == 200


def test_retrieve_all_active_jobs(client):
    data = create_payload()
    client.post("/job", json.dumps(data))

    response = client.get("/job/all/active")
    assert response.status_code == 200


def test_update_job(client):
    data_post = create_payload()
    data_patch = create_payload_update_job()

    client.post("/job", json.dumps(data_post))
    response_patch = client.patch("/job/1", json.dumps(data_patch))
    response_get = client.get("/job/1")

    assert response_patch.status_code == 200
    assert response_get.status_code == 200
    assert response_get.json()["title"] == "[updated] SDE 1 Yahoo"


def test_update_job_wrong_id(client):
    data_post = create_payload()
    data_patch = create_payload_update_job()

    client.post("/job", json.dumps(data_post))
    response_patch = client.patch("/job/2000000", json.dumps(data_patch))

    assert response_patch.status_code == 400


def test_delete_job(client):
    data = create_payload()
    client.post("/job", json.dumps(data))

    response = client.delete("/job/1")
    assert response.status_code == 200


def test_delete_job_wrong_id(client):
    response = client.delete("/job/1")
    assert response.status_code == 400
