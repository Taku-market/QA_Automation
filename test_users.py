def test_name_not_empty(sample_user):
    assert len(sample_user["name"]) > 0

def test_email_contains(sample_user):
    assert "@" in sample_user["email"] 

def test_age_check(sample_user):
    assert sample_user["age"] >= 0

def test_active_is(sample_user):
    assert sample_user["is_active"] == True