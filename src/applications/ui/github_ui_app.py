from src.applications.ui.base_app import BaseAPP
from src.config.config import CONFIG
from src.applications.ui.page_objects.login_page import LoginPage
from src.applications.ui.page_objects.login_page import SignUpPage
from src.applications.ui.page_objects.login_page import Sign_up_Page


class GitHubUI(BaseAPP):

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.LoginPage = LoginPage(self)
        self.SignUpPage = SignUpPage(self)
        self.SignUpPage = Sign_up_Page(self)

    def open(self):
        self.driver.get(CONFIG.get("BASE_URL_UI"))
        return self

    def check_repo_exists(repo_name):
        return True

    def quit(self):
        self.driver.quit()
