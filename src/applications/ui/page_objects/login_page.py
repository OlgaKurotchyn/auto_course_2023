from src.config.config import CONFIG
from selenium.webdriver.common.by import By
import time


class LoginPage:
    URL = "/login"

    USERNAME_FLD = (By.ID, "login_field")  # css xpath
    PASSWROD_FLD = (By.ID, "password")  # id
    SIGN_IN_BTN = (By.NAME, "commit")  # name

    def __init__(self, app) -> None:
        self.app = app

    def go_to(self):
        self.app.go_to(CONFIG.get("BASE_URL_UI") + LoginPage.URL)

    def try_sign_in(self, username, password):
        self.app.type_text(LoginPage.USERNAME_FLD, username)
        self.app.type_text(LoginPage.PASSWROD_FLD, password)

        self.app.click(LoginPage.SIGN_IN_BTN)

        time.sleep(3)

        return self

    def click_sign_up_page(self):
        sing_up_page = self.app.SignUpPage(self.app)
        sing_up_page.wait_loaded()

        return sing_up_page

    def go_to_forgot_pass_page(self):
        # return any
        pass

    def check_error_message(self):
        # return bool

        # if error exists - return True
        # else - return False
        # error_msg = self.driver.find_element(By.ID, LoginPage.USERNAME_FLD)

        # implementation of the check_error_message method here
        error_msg = "Error"
        return error_msg == "Error"


class SignUpPage:
    URL = "/"

    EMAIL_FLD = (By.ID, "user_email")  # id
    SIGN_UP_BTN = (
        By.XPATH, "/html/body/div[1]/div[4]/main/div[1]/div[2]/div/div/div[2]/div[2]/form/div/button")  # xpath
    CONT_BTN = (
        By.XPATH, "//html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button")  # xpath

    def __init__(self, app) -> None:
        self.app = app

    def go_to(self):
        self.app.go_to(CONFIG.get("BASE_URL_UI") + SignUpPage.URL)

    def try_sign_up(self, email):
        self.app.type_text(SignUpPage.EMAIL_FLD, email)

        self.app.click(SignUpPage.SIGN_UP_BTN)

        time.sleep(7)


class Sign_up_Page:
    URL = "/signup"

    EMAIL_FLD_UP = (By.ID, "email")  # id
    PASSWROD_FLD_UP = (By.ID, "password")  # id
    CONT_BTN1 = (
        By.XPATH, "/html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button")  # xpath
    CONT_BTN2 = (
        By.XPATH, "//html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button")  # xpath

    def __init__(self, app) -> None:
        self.app = app

    def go_to(self):
        self.app.go_to(CONFIG.get("BASE_URL_UI") + Sign_up_Page.URL)

        time.sleep(7)

    def try_sign_up(self, email):
        self.app.type_text(Sign_up_Page.EMAIL_FLD_UP, email)

        self.app.click(Sign_up_Page.CONT_BTN1)

        time.sleep(10)

    def try_enter_pass(self, password):
        self.app.type_text(Sign_up_Page.PASSWROD_FLD_UP, password)

        self.app.click(Sign_up_Page.CONT_BTN2)

        time.sleep(7)

        # def enter_confirm_password(self, password):
        # code to enter confirm password

        # def click_signup_button(self):
        # code to click on the Signup button

        # def click_sign_up_page(self):
        sing_up_page = self.app.SignUpPage(self.app)
        sing_up_page.wait_loaded()

        return sing_up_page

    def check_error_message(self):
        # return bool

        # if error exists - return True
        # else - return False
        # error_msg = self.driver.find_element(By.ID, LoginPage.USERNAME_FLD)
        error_msg = "Error"
        return error_msg == "Error"
