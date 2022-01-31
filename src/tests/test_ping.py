"""test_ping
Tests to check the /ping routes
"""

from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ping(test_app):
    """test_ping
    Test to perform /ping route

    Parameters:
    -----------
    test_app : TestClient

    """
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}
