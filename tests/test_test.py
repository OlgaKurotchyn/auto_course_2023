from src.config.config import CONFIG


def test_search_repo():
    assert 1 == 1


def test_user_age_is_42(user):
    assert user.age == 42


def test_user_age_is_50(user):
    assert user.age == 42


def test_http_request():
    print(CONFIG.get("BASE_URL_API"))
