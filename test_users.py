import pytest
import json
import os

@pytest.fixture
def sample_user():
    path = os.path.join(os.path.dirname(__file__), "test_data", "users.json")
    with open(path, "r") as f:
        users = json.load(f)
    return users[0]

def test_name_not_empty(sample_user):
    assert len(sample_user["name"]) > 0

def test_email_contains(sample_user):
    assert "@" in sample_user["email"] 

def test_age_check(sample_user):
    assert sample_user["age"] >= 0

def test_active_is(sample_user):
    assert sample_user["is_active"] == True