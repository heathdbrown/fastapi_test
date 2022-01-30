from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_notes(test_app):
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == {
                                "notes": [ 
                                           {"id": 1, "name": "Note 1", "content": "Note content"}, 
                                           {"id": 2, "name": "Note 2", "content": "Note content"},
                                        ]
                              }
