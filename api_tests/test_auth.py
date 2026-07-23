import requests
import pytest
from config import BASE_URL

@pytest.fixture
def auth_token():
    credentials = {
        "username": "emilys",
        "password": "emilyspass"
    }
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=credentials
    )
    return response.json()["accessToken"]

def test_login_and_get_profile(auth_token):
    profile = requests.get(
        "https://dummyjson.com/auth/me",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert profile.status_code == 200
    assert profile.json()["username"] == "emilys"

def test_login_returns_token():
    credentials = {
        "username": "emilys",
        "password": "emilyspass"
    }
    response = requests.post(
        "https://dummyjson.com/auth/login",
        json=credentials
    )
    assert response.status_code == 200
    assert "accessToken" in response.json()

def test_access_without_token_is_rejected():
    response = requests.get("https://dummyjson.com/auth/me")
    assert response.status_code == 401