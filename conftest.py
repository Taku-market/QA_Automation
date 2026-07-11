import pytest

@pytest.fixture
def sample_user():
    return {
        "name": "John",
        "email": "john@example.com",
        "age": 25,
        "is_active": True,
    }

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