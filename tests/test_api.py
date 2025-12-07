import requests

def test_api_status_code():
    response = requests.get("http://localhost:5000/api/status")
    assert response.status_code == 200
    assert response.json()['status'] == "active"