
def test_sign_in_pom(github_ui_app):
    login_page = github_ui_app.LoginPage

    login_page.go_to()
    login_page.try_sign_in('username', 'password')

    assert login_page.check_error_message()


def test_sign_in_with_inv_name(github_ui_app):
    login_page = github_ui_app.LoginPage

    login_page.go_to()
    login_page.try_sign_in('invalid_username', 'password')

    assert login_page.check_error_message()


def test_sign_in_with_inv_pass(github_ui_app):
    login_page = github_ui_app.LoginPage

    login_page.go_to()
    login_page.try_sign_in('username', 'invalid_password')

    assert login_page.check_error_message()


def test_signup_with_val(github_ui_app):
    signup_page = github_ui_app.SignUpPage

    signup_page.go_to()
    signup_page.try_sign_up("email@example.com")

    assert signup_page.check_error_message()


def test_signup_with_inv(github_ui_app):
    signup_page = github_ui_app.SignUpPage

    signup_page.go_to()
    signup_page.try_sign_up("invalid_email")

    assert signup_page.check_error_message()
