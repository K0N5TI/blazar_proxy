"""
This file contains the tests for the v1 module.
"""
import json

def test_v1_info(client):
    """
    GIVEN a Flask application
    WHEN the '/v1/' page is requested (GET)
    THEN check that the response is valid
    THEN check that the response is correct
    """
    response = client.get("/v1/")
    assert response.status_code == 200
    assert response.json == {
        "version": "1.0",
        "description": "This is the first version of the Blazar Proxy API",
        "endpoints": {
            "cats": "/cats",
            "vertices": "/vertices"
        },
    }


def test_v1(client):
    """
    GIVEN a Flask application
    WHEN the '/v1/' page is requested (GET)
    THEN check that the response is valid
    THEN check that the response is correct
    """
    response = client.get("/v1/")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["version"] == "1.0"
    assert data["description"] == "This is the first version of the Blazar Proxy API"
    assert data["endpoints"] == {
        "cats": "/cats",
        "vertices": "/vertices"
    }

def test_cats_pagination(client):
    """
    GIVEN a Flask application
    WHEN the '/v1/cats' page is requested (GET)
    THEN check that the response is valid
    THEN check that the response is correct
    """
    response = client.get("/v1/cats?page=1&per_page=5")
    assert response.status_code == 200
    data = response.get_json()
    assert data['page'] == 1
    assert data['per_page'] == 5

def test_vertices_pagination(client):
    """
    GIVEN a Flask application
    WHEN the '/v1/cats' page is requested (GET)
    THEN check that the response is valid
    THEN check that the response is correct
    """
    response = client.get("/v1/vertices?page=1&per_page=5")
    assert response.status_code == 200
    data = response.get_json()
    assert data['page'] == 1
    assert data['per_page'] == 5
