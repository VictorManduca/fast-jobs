import json


def create_payload():
    return {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://wwww.fdj.com",
        "location": "USA,NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }


def test_create_job(client):
    data = create_payload()
    response = client.post("/job", json.dumps(data))

    assert response.status_code == 201

def test_wrong_payload(client):
    data = {}
    response = client.post("/job", json.dumps(data))

    assert response.status_code == 422
