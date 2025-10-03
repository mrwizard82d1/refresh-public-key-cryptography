from fastapi.testclient import TestClient

import pytest

from main import app

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)


def test_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI World"}


def test_item(test_client):
    response = test_client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1}


def test_create_item(test_client):
    response = test_client.post("/items/", json={"name": "Test Item", "price": 10.99})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["price"] == 10.99
