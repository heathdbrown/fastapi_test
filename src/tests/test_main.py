from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_pint():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
