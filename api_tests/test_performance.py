import requests
from config import BASE_URL

def test_get_user_response_time():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.elapsed.total_seconds() < 2.0

def test_get_all_users_response_time():
    response = requests.get(f"{BASE_URL}/users")
    assert response.elapsed.total_seconds() < 3.0

def test_create_user_response_time():
    new_user = {"name": "John", "email": "john@example.com"}
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    assert response.elapsed.total_seconds() < 2.0

def test_response_time_with_log():
    response = requests.get(f"{BASE_URL}/users/1")
    duration = response.elapsed.total_seconds()
    print(f"\nResponse time: {duration:.3f}s")
    assert duration < 2.0