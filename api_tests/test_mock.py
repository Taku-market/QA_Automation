import requests
from unittest.mock import patch, Mock

def get_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()

def test_get_user_mocked():
    mock_response = Mock()
    mock_response.json.return_value = {"id": 1, "name": "John", "email": "john@example.com"}
    mock_response.status_code = 200

    with patch("requests.get", return_value=mock_response):
        result = get_user(1)

    assert result["name"] == "John"
    assert result["email"] == "john@example.com"

def test_get_user_server_error():
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "Internal Server Error"}

    with patch("requests.get", return_value=mock_response):
        response_status = mock_response.status_code

    assert response_status == 500