
def test_try_go_though_signup_page(github_ui_app):
    sign_up_page = github_ui_app.Sign_up_Page

    sign_up_page.go_to()
    sign_up_page.try_sign_up("email@example.com")

    assert sign_up_page.check_error_message()
