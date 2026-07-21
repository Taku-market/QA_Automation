import pytest
import requests
from config import BASE_URL

@pytest.fixture
def user_response():
    return requests.get(f"{BASE_URL}/users/1")

def test_get_user(user_response):
    assert user_response.status_code == 200

def test_response_is_json(user_response):
    data = user_response.json()
    assert data["id"] == 1

def test_response_empty(user_response):
    data = user_response.json()
    assert len(data["name"]) > 0

def test_email(user_response):
    data = user_response.json()
    assert "@" in data["email"]