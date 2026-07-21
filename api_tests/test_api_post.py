import requests
import pytest
from config import BASE_URL

@pytest.fixture
def post_response():
    new_user = {
        "name": "John",
        "email": "john@example.com",
        "age": 25
    }

    response = requests.post(
        f"{BASE_URL}/users",
        json=new_user
    )

    return response

def test_create_user(post_response):
    assert post_response.status_code == 201

def test_create_user_returns_name(post_response):

    data = post_response.json()
    assert data["name"] == "John"

def test_create_user_returns_id(post_response):

    data = post_response.json()
    assert data["id"] is not None