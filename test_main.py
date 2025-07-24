from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_request():
    response = client.get("/business-seconds", params={
        "start_time": "2025-07-21T09:00:00",
        "end_time": "2025-07-21T10:00:00"
    })
    assert response.status_code == 200
    assert response.json() == 3600

def test_weekend():
    response = client.get("/business-seconds", params={
        "start_time": "2025-07-20T09:00:00",  # Sunday
        "end_time": "2025-07-20T17:00:00"
    })
    assert response.status_code == 200
    assert response.json() == 0

def test_invalid_input():
    response = client.get("/business-seconds", params={
        "start_time": "not-a-date",
        "end_time": "2025-07-21T17:00:00"
    })
    assert response.status_code == 400
