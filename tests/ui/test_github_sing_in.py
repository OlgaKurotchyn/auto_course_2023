import pytest
from selenium import webdriver
from src.applications.ui.github_ui_app import GitHubUI


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    browser = GitHubUI(driver)

    browser.open()

    yield browser

    browser.quit()


def test_failed_login(browser):

    browser.go_to_login_page()
    browser.try_login_on_login_page()

    assert browser.check_error_message()
