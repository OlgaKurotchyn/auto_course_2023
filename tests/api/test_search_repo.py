import requests
import uuid


def test_existing_repo_can_be_found():
    # login
    # token = requests.post(url="https://api.github.com/login", data={
    #     "username": 'kjsdkjf',
    #     'password': 'sdlkfnkjsdnf'
    #     }
    # )

    json_object = requests.get(
        url="https://api.github.com/search/repositories",
        params="become",
        # headers={'Authorization': f"Bearer {token}"}
    )

    assert json_object.json()["total_count"] > 0


def test_non_existing_repo_cannot_be_found(github_api_client):
    # TODO: Use random string generator. UUID.v4
    json_object = github_api_client.search_repo("become")

    assert json_object["total_count"] == 0


def test_search_not_working_without_q():
    pass
