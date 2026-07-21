import pytest
import json
import os

@pytest.fixture
def sample_user():
    path = os.path.join(os.path.dirname(__file__), "test_data", "users.json")
    with open(path, "r") as f:
        users = json.load(f)
    return users[0]

@pytest.fixture
def all_users():
    path = os.path.join(os.path.dirname(__file__), "test_data", "users.json")
    with open(path, "r") as f:
        return json.load(f)

@pytest.fixture
def sample_product():
    return {
        "name": "Wireless Mouse",
        "price": 29.99,
        "stock": 50,
        "category": "Electronics",
    }

@pytest.fixture
def sample_order():
    return {
        "order_id": 5001,
        "customer": "John",
        "items": ["Wireless Mouse", "Keyboard"],
        "total": 79.99,
        "status": "pending",
    }