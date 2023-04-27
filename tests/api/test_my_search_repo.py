import uuid
import requests
import unittest


def test_user_age_is_42(user):
    assert user.age == 42


class TestGitHubAPI(unittest.TestCase):

    def test_search_repo(self):
        body = "become"
        url = f"https://api.github.com/search/repositories?q={body}"
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue("total_count" in response.json())

        total_count = response.json()["total_count"]
        self.assertTrue(total_count > 0)


def test_search_repo():
    body = "become"
    url = f"https://api.github.com/search/repositories?q={body}"
    response = requests.get(url)

    assert response.status_code == 200
    assert "total_count" in response.json()
    assert response.json()["total_count"] > 0


def test_search_repo_not_found():
    body = str(uuid.uuid4())  # Generate a random UUID string
    url = f"https://api.github.com/search/repositories?q={body}"
    response = requests.get(url)

    assert response.status_code == 200
    assert "total_count" in response.json()
    assert response.json()["total_count"] == 0


def test_search_repo_without_q_param():
    url = "https://api.github.com/search/repositories"
    response = requests.get(url)

    assert response.status_code == 422
    assert "message" in response.json()
    assert response.json()["message"] == "Validation Failed"


def test_search_repo_without_q():
    body = requests.get(
        url="https://api.github.com/search/repositories"
    )

    assert body.status_code == 422
    assert "message" in body.json()
    assert body.json()["message"] == "Validation Failed"
