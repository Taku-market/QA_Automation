import pytest
import requests
from config import BASE_URL

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_exists(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_user_has_email(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    data = response.json()
    assert "@" in data["email"]

def test_user_not_found():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404