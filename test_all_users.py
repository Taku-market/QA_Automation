from logger import get_logger

logger = get_logger(__name__)

def test_all_users_have_email(all_users):
    for user in all_users:
        logger.info(f"Checking email for: {user['name']}")
        assert "@" in user["email"]

def test_all_users_have_name(all_users):
    for user in all_users:
        logger.info(f"Checking name for: {user['name']}")
        assert len(user["name"]) > 0