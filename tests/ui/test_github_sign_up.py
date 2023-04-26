
def test_go_though_signup_page(github_ui_app):
    sign_up_page = github_ui_app.SignUpPage

    sign_up_page.go_to()

    assert sign_up_page.check_error_message()
