class GitHubUI:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://github.com")

    def go_to_login_page(self):
        login_link = self.driver.find_element_by_link_text("Sign in")
        login_link.click()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://github.com/login"

    def go_to(self):
        self.driver.get(self.url)

    def try_sign_in(self, username, password):
        username_field = self.driver.find_element_by_id("login_field")
        password_field = self.driver.find_element_by_id("password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.submit()

    def check_error_message(self):
        error_message = self.driver.find_element_by_css_selector(
            "#js-flash-container .flash-error")
        return error_message.is_displayed()


class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://github.com/join"

    def go_to(self):
        self.driver.get(self.url)

    def fill_signup_form(self, name, email, password):
        name_field = self.driver.find_element_by_id("user_login")
        email_field = self.driver.find_element_by_id("user_email")
        password_field = self.driver.find_element_by_id("user_password")

        name_field.send_keys(name)
        email_field.send_keys(email)
        password_field.send_keys(password)

    def submit_signup_form(self):
        submit_button = self.driver.find_element_by_css_selector(
            ".btn-mktg[type='submit']")
        submit_button.click()

    def check_error_message(self):
        error_message = self.driver.find_element_by_css_selector(
            "#js-flash-container .flash-error")
        return error_message.is_displayed()
