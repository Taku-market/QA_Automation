def test_all_users_have_email(all_users):
    for user in all_users:
        assert "@" in user["email"]

def test_all_users_have_name(all_users):
    for user in all_users:
        assert len(user["name"]) > 0