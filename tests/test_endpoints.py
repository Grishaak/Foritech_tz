from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_create_request_wallet():
    response = client.post(
        url='/wallet-info',
        json={"address": "TNMcQVGPzqH9ZfMCSY4PNrukevtDgp24dK"}
    )
    assert response.status_code == 200


def test_get_requested_wallets():
    response = client.get(
        "/requests-history?skip=0&limit=1"
    )
    assert response.status_code == 200
    assert isinstance(response.json(), list)
